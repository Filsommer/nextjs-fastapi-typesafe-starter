# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off
from __future__ import annotations

# global imports for type checking
from builtins import bool as _bool
from builtins import int as _int
from builtins import float as _float
from builtins import str as _str
import sys
import decimal
import datetime
from typing import (
    TYPE_CHECKING,
    Optional,
    Iterable,
    Iterator,
    Sequence,
    Callable,
    ClassVar,
    NoReturn,
    TypeVar,
    Generic,
    Mapping,
    Tuple,
    Union,
    List,
    Dict,
    Type,
    Any,
    Set,
    overload,
    cast,
)
from typing_extensions import TypedDict, Literal


LiteralString = str
# -- template engine/query.py.jinja --

import os
import time
import atexit
import signal
import asyncio
import logging
import subprocess
from pathlib import Path

from . import utils, errors
from .http import HTTPEngine
from .. import config
from ..utils import DEBUG
from ..binaries import platform
from ..utils import time_since, _env_bool
from ..types import DatasourceOverride
from ..builder import dumps


__all__ = ('QueryEngine',)

log: logging.Logger = logging.getLogger(__name__)


class QueryEngine(HTTPEngine):
    dml_path: Path
    url: Optional[str]
    file: Optional[Path]
    process: subprocess.Popen[bytes] | subprocess.Popen[str] | None

    def __init__(self, *, dml_path: Path, log_queries: bool = False, **kwargs: Any) -> None:
        super().__init__(url=None, **kwargs)
        self.dml_path = dml_path
        self._log_queries = log_queries
        self.process = None
        self.file = None

        # ensure the query engine process is terminated when we are
        atexit.register(self.stop)

    def __del__(self) -> None:
        self.stop()

    def close(self, *, timeout: Optional[float] = None) -> None:
        log.debug('Disconnecting query engine...')

        if self.process is not None:
            if platform.name() == 'windows':
                self.process.kill()
                self.process.wait(timeout=timeout)
            else:
                self.process.send_signal(signal.SIGINT)
                try:
                    self.process.wait(timeout=timeout)
                except subprocess.TimeoutExpired:
                    self.process.send_signal(signal.SIGKILL)

            self.process = None

        log.debug('Disconnected query engine')

    async def aclose(self, *, timeout: Optional[float] = None) -> None:
        self.close(timeout=timeout)
        await self._close_session()

    async def _close_session(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()

    def _ensure_file(self) -> Path:
        # circular import
        from ..client import BINARY_PATHS

        return utils.ensure(BINARY_PATHS.query_engine)

    async def connect(
        self,
        timeout: int = 10,
        datasources: Optional[List[DatasourceOverride]] = None,
    ) -> None:
        log.debug('Connecting to query engine')
        if self.process is not None:
            return
            #raise errors.AlreadyConnectedError('Already connected to the query engine')

        start = time.monotonic()
        self.file = file = self._ensure_file()
        #self.file = file =  Path("./api/prisma/query-engine-rhel-openssl-1.0.x")

        try:
            await self.spawn(file, timeout=timeout, datasources=datasources)
        except Exception:
            self.close()
            raise

        log.debug('Connecting to query engine took %s', time_since(start))

    async def spawn(
        self,
        file: Path,
        timeout: int = 10,
        datasources: Optional[List[DatasourceOverride]] = None,
    ) -> None:
        port = utils.get_open_port()
        log.debug('Running query engine on port %i', port)

        self.url = f'http://localhost:{port}'

        env = os.environ.copy()
        env.update(
            PRISMA_DML_PATH=str(self.dml_path.absolute()),
            RUST_LOG='error',
            RUST_LOG_FORMAT='json',
            PRISMA_CLIENT_ENGINE_TYPE='binary',
        )

        if DEBUG:
            env.update(RUST_LOG='info')

        if datasources is not None:
            env.update(OVERWRITE_DATASOURCES=dumps(datasources))

        # TODO: remove the noise from these query logs
        if self._log_queries:
            env.update(LOG_QUERIES='y')

        args: List[str] = [str(file.absolute()), '-p', str(port), '--enable-raw-queries']
        if _env_bool('__PRISMA_PY_PLAYGROUND'):
            env.update(RUST_LOG='info')
            args.append('--enable-playground')

        log.debug('Starting query engine...')
        popen_kwargs: Dict[str,Any] = {
            "env": env,
            "stdout": sys.stdout,
            "stderr": sys.stderr,
            "text": False,
        }
        if platform.name() != 'windows':
            # ensure SIGINT is unblocked before forking the query engine
            # https://github.com/RobertCraigie/prisma-client-py/pull/678
            popen_kwargs["preexec_fn"] = lambda: signal.pthread_sigmask(
                signal.SIG_UNBLOCK, [signal.SIGINT, signal.SIGTERM]
            )

        self.process = subprocess.Popen(
            args,
            **popen_kwargs
        )

        last_exc = None
        for _ in range(int(timeout / 0.1)):
            try:
                data = await self.request('GET', '/status')
            except Exception as exc:
                last_exc = exc
                log.debug(
                    'Could not connect to query engine due to %s; retrying...',
                    type(exc).__name__,
                )
                await asyncio.sleep(0.1)

                continue

            if data.get('Errors') is not None:
                log.debug('Could not connect due to gql errors; retrying...')
                await asyncio.sleep(0.1)

                continue

            break
        else:
            raise errors.EngineConnectionError(
                'Could not connect to the query engine'
            ) from last_exc

    async def query(self, content: str) -> Any:
        return await self.request('POST', '/', content=content)


# black does not respect the fmt: off comment without this
# fmt: on
