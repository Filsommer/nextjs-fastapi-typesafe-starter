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
# -- template client.py.jinja --
from pathlib import Path
from types import TracebackType

from pydantic import BaseModel

from . import types, models, errors, actions
from .types import DatasourceOverride, HttpConfig
from ._types import BaseModelT, PrismaMethod
from .bases import _PrismaModel
from .engine import AbstractEngine, QueryEngine
from .builder import QueryBuilder
from .generator.models import EngineType, OptionalValueFromEnvVar, BinaryPaths
from ._compat import removeprefix
from ._raw_query import deserialize_raw_results

__all__ = (
    'ENGINE_TYPE',
    'SCHEMA_PATH',
    'BINARY_PATHS',
    'Batch',
    'Prisma',
    'Client',
    'load_env',
    'register',
    'get_client',
)

SCHEMA_PATH = Path('/Users/filipesommer/Desktop/Desktop - Filipe’s MacBook Pro/FelApps/pynext/api/schema.prisma')
PACKAGED_SCHEMA_PATH = Path(__file__).parent.joinpath('schema.prisma')
ENGINE_TYPE: EngineType = EngineType.binary
BINARY_PATHS = BinaryPaths.parse_obj({'queryEngine': {'darwin-arm64': '/Users/filipesommer/.cache/prisma-python/binaries/4.14.0/d9a4c5988f480fa576d43970d5a23641aa77bc9c/node_modules/prisma/query-engine-darwin-arm64', 'rhel-openssl-1.0.x': '/Users/filipesommer/.cache/prisma-python/binaries/4.14.0/d9a4c5988f480fa576d43970d5a23641aa77bc9c/node_modules/prisma/query-engine-rhel-openssl-1.0.x'}, 'introspectionEngine': {}, 'migrationEngine': {}, 'libqueryEngine': {}, 'prismaFmt': {}})

RegisteredClient = Union['Prisma', Callable[[], 'Prisma']]
_registered_client: Optional[RegisteredClient] = None


class UseClientDefault:
    """For certain parameters such as `timeout=...` we can make our intent more clear
    by typing the parameter with this class rather than using None, for example:

    ```py
    def connect(timeout: Union[int, UseClientDefault] = UseClientDefault()) -> None: ...
    ```

    relays the intention more clearly than:

    ```py
    def connect(timeout: Optional[int] = None) -> None: ...
    ```

    This solution also allows us to indicate an "unset" state that is uniquely distinct
    from `None` which may be useful in the future.
    """


_USE_CLIENT_DEFAULT = UseClientDefault()


def load_env(*, override: bool = False, **kwargs: Any) -> None:
    """Load environemntal variables from dotenv files

    Loads from the following files relative to the current
    working directory:

    - .env
    - prisma/.env
    """
    from dotenv import load_dotenv

    load_dotenv('.env', override=override, **kwargs)
    load_dotenv('prisma/.env', override=override, **kwargs)


def register(client: RegisteredClient) -> None:
    """Register a client instance to be retrieved by `get_client()`

    This function _must_ only be called once, preferrably as soon as possible
    to avoid any potentially confusing errors with threads or processes.
    """
    global _registered_client

    if _registered_client is not None:
        raise errors.ClientAlreadyRegisteredError()

    if not isinstance(client, Prisma) and not callable(client):
        raise TypeError(
            f'Expected either a {Prisma} instance or a function that returns a {Prisma} but got {client} instead.'
        )

    _registered_client = client


def get_client() -> 'Prisma':
    """Get the registered client instance

    Raises errors.ClientNotRegisteredError() if no client instance has been registered.
    """
    registered = _registered_client
    if registered is None:
        raise errors.ClientNotRegisteredError() from None

    if isinstance(registered, Prisma):
        return registered

    client = registered()
    if not isinstance(client, Prisma):  # pyright: ignore[reportUnnecessaryIsInstance]
        raise TypeError(
            f'Registered function returned {client} instead of a {Prisma} instance.'
        )

    return client


class Prisma:
    items: 'actions.ItemsActions[models.Items]'

    __slots__ = (
        'items',
        '__engine',
        '_active_provider',
        '_log_queries',
        '_datasource',
        '_connect_timeout',
        '_http_config',
    )

    def __init__(
        self,
        *,
        use_dotenv: bool = True,
        log_queries: bool = False,
        auto_register: bool = False,
        datasource: Optional[DatasourceOverride] = None,
        connect_timeout: int = 10,
        http: Optional[HttpConfig] = None,
    ) -> None:
        self.items = actions.ItemsActions[models.Items](self, models.Items)
        self.__engine: Optional[AbstractEngine] = None
        self._active_provider = 'postgresql'
        self._log_queries = log_queries
        self._datasource = datasource
        self._connect_timeout = connect_timeout
        self._http_config: HttpConfig = http or {}

        if use_dotenv:
            load_env()

        if auto_register:
            register(self)

    def __del__(self) -> None:
        if self.__engine is not None:
            self.__engine.stop()
            self.__engine = None


    async def __aenter__(self) -> 'Prisma':
        await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self.is_connected():
            await self.disconnect()

    def is_connected(self) -> bool:
        """Returns True if the client is connected to the query engine, False otherwise."""
        return self.__engine is not None

    async def connect(
        self,
        timeout: Union[int, UseClientDefault] = _USE_CLIENT_DEFAULT,
    ) -> None:
        """Connect to the Prisma query engine.

        It is required to call this before accessing data.
        """
        if isinstance(timeout, UseClientDefault):
            timeout = self._connect_timeout

        if self.__engine is None:
            self.__engine = self._create_engine(dml_path=PACKAGED_SCHEMA_PATH)

        datasources: Optional[List[types.DatasourceOverride]] = None
        if self._datasource is not None:
            ds = self._datasource.copy()
            ds.setdefault('name', 'db')
            datasources = [ds]

        await self.__engine.connect(
            timeout=timeout,
            datasources=datasources,
        )

    async def disconnect(self, timeout: Optional[float] = None) -> None:
        """Disconnect the Prisma query engine."""
        if self.__engine is not None:
            await self.__engine.aclose(timeout=timeout)
            self.__engine.stop(timeout=timeout)
            self.__engine = None

    async def execute_raw(self, query: LiteralString, *args: Any) -> int:
        resp = await self._execute(
            method='execute_raw',
            arguments={
                'query': query,
                'parameters': args,
            },
            model=None,
        )
        return int(resp['data']['result'])

    @overload
    async def query_first(
        self,
        query: LiteralString,
        *args: Any,
    ) -> dict[str, Any]:
        ...

    @overload
    async def query_first(
        self,
        query: LiteralString,
        *args: Any,
        model: Type[BaseModelT],
    ) -> Optional[BaseModelT]:
        ...

    async def query_first(
        self,
        query: LiteralString,
        *args: Any,
        model: Optional[Type[BaseModelT]] = None,
    ) -> Union[Optional[BaseModelT], dict[str, Any]]:
        """This function is the exact same as `query_raw()` but returns the first result.

        If model is given, the returned record is converted to the pydantic model first,
        otherwise a raw dictionary will be returned.
        """
        results: Sequence[Union[BaseModelT, dict[str, Any]]]
        if model is not None:
            results = await self.query_raw(query, *args, model=model)
        else:
            results = await self.query_raw(query, *args)

        if not results:
            return None

        return results[0]

    @overload
    async def query_raw(
        self,
        query: LiteralString,
        *args: Any,
    ) -> List[dict[str, Any]]:
        ...

    @overload
    async def query_raw(
        self,
        query: LiteralString,
        *args: Any,
        model: Type[BaseModelT],
    ) -> List[BaseModelT]:
        ...

    async def query_raw(
        self,
        query: LiteralString,
        *args: Any,
        model: Optional[Type[BaseModelT]] = None,
    ) -> Union[List[BaseModelT], List[dict[str, Any]]]:
        """Execute a raw SQL query against the database.

        If model is given, each returned record is converted to the pydantic model first,
        otherwise results will be raw dictionaries.
        """
        resp = await self._execute(
            method='query_raw',
            arguments={
                'query': query,
                'parameters': args,
            },
            model=model,
        )
        result = resp['data']['result']
        if model is not None:
            return deserialize_raw_results(result, model=model)

        return deserialize_raw_results(result)

    def batch_(self) -> 'Batch':
        """Returns a context manager for grouping write queries into a single transaction."""
        return Batch(client=self)

    # TODO: don't return Any
    async def _execute(
        self,
        method: PrismaMethod,
        arguments: dict[str, Any],
        model: type[BaseModel] | None = None,
        root_selection: list[str] | None = None
    ) -> Any:
        builder = QueryBuilder(
            method=method,
            model=model,
            arguments=arguments,
            root_selection=root_selection,
        )
        return await self._engine.query(builder.build())

    def _create_engine(self, dml_path: Path = PACKAGED_SCHEMA_PATH) -> AbstractEngine:
        if ENGINE_TYPE == EngineType.binary:
            return QueryEngine(dml_path=dml_path, log_queries=self._log_queries, **self._http_config)

        raise NotImplementedError(f'Unsupported engine type: {ENGINE_TYPE}')

    @property
    def _engine_class(self) -> Type[AbstractEngine]:
        if ENGINE_TYPE == EngineType.binary:
            return QueryEngine
        else:  # pragma: no cover
            raise RuntimeError(f'Unhandled engine type: {ENGINE_TYPE}')

    @property
    def _engine(self) -> AbstractEngine:
        engine = self.__engine
        if engine is None:
            raise errors.ClientNotConnectedError()
        return engine

    def _make_sqlite_datasource(self) -> DatasourceOverride:
        return {
            'name': 'db',
            'url': self._make_sqlite_url(self._default_datasource['url']),
        }

    def _make_sqlite_url(self, url: str, *, relative_to: Path = SCHEMA_PATH.parent) -> str:
        url_path = removeprefix(removeprefix(url, 'file:'), 'sqlite:')
        if url_path == url:
            return url

        if Path(url_path).is_absolute():
            return url

        return f'file:{relative_to.joinpath(url_path).resolve()}'

    @property
    def _default_datasource(self) -> DatasourceOverride:
        return {
            'name': 'db',
            'url': OptionalValueFromEnvVar(**{'value': None, 'fromEnvVar': 'DATABASE_URL'}).resolve(),
        }


# TODO: this should return the results as well
# TODO: don't require copy-pasting arguments between actions and batch actions
class Batch:
    items: 'ItemsBatchActions'

    def __init__(self, client: Prisma) -> None:
        self.__client = client
        self.__queries: List[str] = []
        self._active_provider = client._active_provider
        self.items = ItemsBatchActions(self)

    def _add(self, **kwargs: Any) -> None:
        builder = QueryBuilder(**kwargs)
        self.__queries.append(builder.build_query())

    async def commit(self) -> None:
        """Execute the queries"""
        # TODO: normalise this, we should still call client._execute
        from .builder import dumps

        queries = self.__queries
        self.__queries = []

        payload = {
            'batch': [
                {
                    'query': query,
                    'variables': {},
                }
                for query in queries
            ],
            'transaction': True,
        }
        await self.__client._engine.query(dumps(payload))

    def execute_raw(self, query: LiteralString, *args: Any) -> None:
        self._add(
            method='execute_raw',
            arguments={
                'query': query,
                'parameters': args,
            }
        )

    async def __aenter__(self) -> 'Batch':
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if exc is None:
            await self.commit()


# NOTE: some arguments are meaningless in this context but are included
# for completeness sake
class ItemsBatchActions:
    def __init__(self, batcher: Batch) -> None:
        self._batcher = batcher

    def create(
        self,
        data: types.ItemsCreateInput,
        include: Optional[types.ItemsInclude] = None
    ) -> None:
        self._batcher._add(
            method='create',
            model=models.Items,
            arguments={
                'data': data,
                'include': include,
            },
        )

    def create_many(
        self,
        data: List[types.ItemsCreateWithoutRelationsInput],
        *,
        skip_duplicates: Optional[bool] = None,
    ) -> None:
        if self._batcher._active_provider == 'sqlite':
            raise errors.UnsupportedDatabaseError('sqlite', 'create_many()')

        self._batcher._add(
            method='create_many',
            model=models.Items,
            arguments={
                'data': data,
                'skipDuplicates': skip_duplicates,
            },
            root_selection=['count'],
        )

    def delete(
        self,
        where: types.ItemsWhereUniqueInput,
        include: Optional[types.ItemsInclude] = None,
    ) -> None:
        self._batcher._add(
            method='delete',
            model=models.Items,
            arguments={
                'where': where,
                'include': include,
            },
        )

    def update(
        self,
        data: types.ItemsUpdateInput,
        where: types.ItemsWhereUniqueInput,
        include: Optional[types.ItemsInclude] = None
    ) -> None:
        self._batcher._add(
            method='update',
            model=models.Items,
            arguments={
                'data': data,
                'where': where,
                'include': include,
            },
        )

    def upsert(
        self,
        where: types.ItemsWhereUniqueInput,
        data: types.ItemsUpsertInput,
        include: Optional[types.ItemsInclude] = None,
    ) -> None:
        self._batcher._add(
            method='upsert',
            model=models.Items,
            arguments={
                'where': where,
                'include': include,
                'create': data.get('create'),
                'update': data.get('update'),
            },
        )

    def update_many(
        self,
        data: types.ItemsUpdateManyMutationInput,
        where: types.ItemsWhereInput,
    ) -> None:
        self._batcher._add(
            method='update_many',
            model=models.Items,
            arguments={'data': data, 'where': where,},
            root_selection=['count'],
        )

    def delete_many(
        self,
        where: Optional[types.ItemsWhereInput] = None,
    ) -> None:
        self._batcher._add(
            method='delete_many',
            model=models.Items,
            arguments={'where': where},
            root_selection=['count'],
        )



Client = Prisma