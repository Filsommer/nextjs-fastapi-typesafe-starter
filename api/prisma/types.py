# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off

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
# -- template types.py.jinja --
from typing import TypeVar

import httpx
from .utils import _NoneType



# TODO: filters with aggregates should have their own recursive fields
# TODO: cleanup whitespace control
# TODO: add an argument to signify that the last iteration should be skipped


SortMode = Literal['default', 'insensitive']
SortOrder = Literal['asc', 'desc']


class _DatasourceOverrideOptional(TypedDict, total=False):
    env: str
    name: str


class DatasourceOverride(_DatasourceOverrideOptional):
    url: str


# NOTE: we don't support some options as their type hints are not publicly exposed
# https://github.com/encode/httpx/discussions/1977
class HttpConfig(TypedDict, total=False):
    app: Callable[[Mapping[str, Any], Any], Any]
    http1: bool
    http2: bool
    limits: httpx.Limits
    timeout: Union[None, float, httpx.Timeout]
    trust_env: bool
    max_redirects: int


# types that can be serialized to json by our query builder
Serializable = Union[
    None,
    bool,
    float,
    int,
    str,
    datetime.datetime,
    List[Any],
    Dict[None, Any],
    Dict[bool, Any],
    Dict[float, Any],
    Dict[int, Any],
    Dict[str, Any],
]


    

StringFilter = TypedDict(
    'StringFilter',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
        'not': Union[str, 'StringFilterRecursive1'],
        'mode': SortMode,
    },
    total=False,
)


StringFilterRecursive1 = TypedDict(
    'StringFilterRecursive1',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
        'not': Union[str, 'StringFilterRecursive2'],
        'mode': SortMode,
    },
    total=False,
)


StringFilterRecursive2 = TypedDict(
    'StringFilterRecursive2',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
        'not': Union[str, 'StringFilterRecursive3'],
        'mode': SortMode,
    },
    total=False,
)


StringFilterRecursive3 = TypedDict(
    'StringFilterRecursive3',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
        'not': Union[str, 'StringFilterRecursive4'],
        'mode': SortMode,
    },
    total=False,
)


StringFilterRecursive4 = TypedDict(
    'StringFilterRecursive4',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
                'mode': SortMode,
    },
    total=False,
)


class StringWithAggregatesFilter(StringFilter, total=False):
    _max: 'StringFilter'
    _min: 'StringFilter'
    _sum: 'StringFilter'
    _avg: 'StringFilter'
    _count: 'IntFilter'


    

DateTimeFilter = TypedDict(
    'DateTimeFilter',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
        'not': Union[datetime.datetime, 'DateTimeFilterRecursive1'],
    },
    total=False,
)


DateTimeFilterRecursive1 = TypedDict(
    'DateTimeFilterRecursive1',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
        'not': Union[datetime.datetime, 'DateTimeFilterRecursive2'],
    },
    total=False,
)


DateTimeFilterRecursive2 = TypedDict(
    'DateTimeFilterRecursive2',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
        'not': Union[datetime.datetime, 'DateTimeFilterRecursive3'],
    },
    total=False,
)


DateTimeFilterRecursive3 = TypedDict(
    'DateTimeFilterRecursive3',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
        'not': Union[datetime.datetime, 'DateTimeFilterRecursive4'],
    },
    total=False,
)


DateTimeFilterRecursive4 = TypedDict(
    'DateTimeFilterRecursive4',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
            },
    total=False,
)


class DateTimeWithAggregatesFilter(DateTimeFilter, total=False):
    _max: 'DateTimeFilter'
    _min: 'DateTimeFilter'
    _sum: 'DateTimeFilter'
    _avg: 'DateTimeFilter'
    _count: 'IntFilter'


    

BooleanFilter = TypedDict(
    'BooleanFilter',
    {
        'equals': bool,
        'not': Union[bool, 'BooleanFilterRecursive1'],
    },
    total=False,
)


BooleanFilterRecursive1 = TypedDict(
    'BooleanFilterRecursive1',
    {
        'equals': bool,
        'not': Union[bool, 'BooleanFilterRecursive2'],
    },
    total=False,
)


BooleanFilterRecursive2 = TypedDict(
    'BooleanFilterRecursive2',
    {
        'equals': bool,
        'not': Union[bool, 'BooleanFilterRecursive3'],
    },
    total=False,
)


BooleanFilterRecursive3 = TypedDict(
    'BooleanFilterRecursive3',
    {
        'equals': bool,
        'not': Union[bool, 'BooleanFilterRecursive4'],
    },
    total=False,
)


BooleanFilterRecursive4 = TypedDict(
    'BooleanFilterRecursive4',
    {
        'equals': bool,
            },
    total=False,
)


class BooleanWithAggregatesFilter(BooleanFilter, total=False):
    _max: 'BooleanFilter'
    _min: 'BooleanFilter'
    _sum: 'BooleanFilter'
    _avg: 'BooleanFilter'
    _count: 'IntFilter'


    

IntFilter = TypedDict(
    'IntFilter',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
        'not': Union[int, 'IntFilterRecursive1'],
    },
    total=False,
)


IntFilterRecursive1 = TypedDict(
    'IntFilterRecursive1',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
        'not': Union[int, 'IntFilterRecursive2'],
    },
    total=False,
)


IntFilterRecursive2 = TypedDict(
    'IntFilterRecursive2',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
        'not': Union[int, 'IntFilterRecursive3'],
    },
    total=False,
)


IntFilterRecursive3 = TypedDict(
    'IntFilterRecursive3',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
        'not': Union[int, 'IntFilterRecursive4'],
    },
    total=False,
)


IntFilterRecursive4 = TypedDict(
    'IntFilterRecursive4',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
            },
    total=False,
)


class IntWithAggregatesFilter(IntFilter, total=False):
    _max: 'IntFilter'
    _min: 'IntFilter'
    _sum: 'IntFilter'
    _avg: 'IntFilter'
    _count: 'IntFilter'


BigIntFilter = IntFilter
BigIntWithAggregatesFilter = IntWithAggregatesFilter
    

FloatFilter = TypedDict(
    'FloatFilter',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
        'not': Union[float, 'FloatFilterRecursive1'],
    },
    total=False,
)


FloatFilterRecursive1 = TypedDict(
    'FloatFilterRecursive1',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
        'not': Union[float, 'FloatFilterRecursive2'],
    },
    total=False,
)


FloatFilterRecursive2 = TypedDict(
    'FloatFilterRecursive2',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
        'not': Union[float, 'FloatFilterRecursive3'],
    },
    total=False,
)


FloatFilterRecursive3 = TypedDict(
    'FloatFilterRecursive3',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
        'not': Union[float, 'FloatFilterRecursive4'],
    },
    total=False,
)


FloatFilterRecursive4 = TypedDict(
    'FloatFilterRecursive4',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
            },
    total=False,
)


class FloatWithAggregatesFilter(FloatFilter, total=False):
    _max: 'FloatFilter'
    _min: 'FloatFilter'
    _sum: 'FloatFilter'
    _avg: 'FloatFilter'
    _count: 'IntFilter'


    

BytesFilter = TypedDict(
    'BytesFilter',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
        'not': Union['fields.Base64', 'BytesFilterRecursive1'],
    },
    total=False,
)


BytesFilterRecursive1 = TypedDict(
    'BytesFilterRecursive1',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
        'not': Union['fields.Base64', 'BytesFilterRecursive2'],
    },
    total=False,
)


BytesFilterRecursive2 = TypedDict(
    'BytesFilterRecursive2',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
        'not': Union['fields.Base64', 'BytesFilterRecursive3'],
    },
    total=False,
)


BytesFilterRecursive3 = TypedDict(
    'BytesFilterRecursive3',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
        'not': Union['fields.Base64', 'BytesFilterRecursive4'],
    },
    total=False,
)


BytesFilterRecursive4 = TypedDict(
    'BytesFilterRecursive4',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
            },
    total=False,
)


class BytesWithAggregatesFilter(BytesFilter, total=False):
    _max: 'BytesFilter'
    _min: 'BytesFilter'
    _sum: 'BytesFilter'
    _avg: 'BytesFilter'
    _count: 'IntFilter'


# TODO: preview feature for improving JSON filtering
JsonFilter = TypedDict(
    'JsonFilter',
    {
        'equals': 'fields.Json',
        'not': 'fields.Json',
    },
    total=False,
)


class JsonWithAggregatesFilter(JsonFilter, total=False):
    _max: 'JsonFilter'
    _min: 'JsonFilter'
    _sum: 'JsonFilter'
    _avg: 'JsonFilter'
    _count: 'IntFilter'


    

DecimalFilter = TypedDict(
    'DecimalFilter',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
        'not': Union[decimal.Decimal, 'DecimalFilterRecursive1'],
    },
    total=False,
)


DecimalFilterRecursive1 = TypedDict(
    'DecimalFilterRecursive1',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
        'not': Union[decimal.Decimal, 'DecimalFilterRecursive2'],
    },
    total=False,
)


DecimalFilterRecursive2 = TypedDict(
    'DecimalFilterRecursive2',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
        'not': Union[decimal.Decimal, 'DecimalFilterRecursive3'],
    },
    total=False,
)


DecimalFilterRecursive3 = TypedDict(
    'DecimalFilterRecursive3',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
        'not': Union[decimal.Decimal, 'DecimalFilterRecursive4'],
    },
    total=False,
)


DecimalFilterRecursive4 = TypedDict(
    'DecimalFilterRecursive4',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
            },
    total=False,
)


class DecimalWithAggregatesFilter(StringFilter, total=False):
    _max: 'DecimalFilter'
    _min: 'DecimalFilter'
    _sum: 'DecimalFilter'
    _avg: 'DecimalFilter'
    _count: 'IntFilter'


class _FloatSetInput(TypedDict):
    set: float


class _FloatDivideInput(TypedDict):
    divide: float


class _FloatMultiplyInput(TypedDict):
    multiply: float


class _FloatIncrementInput(TypedDict):
    increment: float


class _FloatDecrementInput(TypedDict):
    decrement: float


class _IntSetInput(TypedDict):
    set: int


class _IntDivideInput(TypedDict):
    divide: int


class _IntMultiplyInput(TypedDict):
    multiply: int


class _IntIncrementInput(TypedDict):
    increment: int


class _IntDecrementInput(TypedDict):
    decrement: int


AtomicFloatInput = Union[
    _FloatSetInput,
    _FloatDivideInput,
    _FloatMultiplyInput,
    _FloatIncrementInput,
    _FloatDecrementInput,
]
AtomicIntInput = Union[
    _IntSetInput,
    _IntDivideInput,
    _IntMultiplyInput,
    _IntIncrementInput,
    _IntDecrementInput,
]
AtomicBigIntInput = AtomicIntInput

class _StringListFilterEqualsInput(TypedDict):
    equals: Optional[List[_str]]


class _StringListFilterHasInput(TypedDict):
    has: _str


class _StringListFilterHasEveryInput(TypedDict):
    has_every: List[_str]


class _StringListFilterHasSomeInput(TypedDict):
    has_some: List[_str]


class _StringListFilterIsEmptyInput(TypedDict):
    is_empty: bool


StringListFilter = Union[
    _StringListFilterHasInput,
    _StringListFilterEqualsInput,
    _StringListFilterHasSomeInput,
    _StringListFilterIsEmptyInput,
    _StringListFilterHasEveryInput,
]


class _StringListUpdateSet(TypedDict):
    set: List[_str]


class _StringListUpdatePush(TypedDict):
    push: List[_str]


StringListUpdate = Union[
    List[_str],
    _StringListUpdateSet,
    _StringListUpdatePush,
]

class _BytesListFilterEqualsInput(TypedDict):
    equals: Optional[List['fields.Base64']]


class _BytesListFilterHasInput(TypedDict):
    has: 'fields.Base64'


class _BytesListFilterHasEveryInput(TypedDict):
    has_every: List['fields.Base64']


class _BytesListFilterHasSomeInput(TypedDict):
    has_some: List['fields.Base64']


class _BytesListFilterIsEmptyInput(TypedDict):
    is_empty: bool


BytesListFilter = Union[
    _BytesListFilterHasInput,
    _BytesListFilterEqualsInput,
    _BytesListFilterHasSomeInput,
    _BytesListFilterIsEmptyInput,
    _BytesListFilterHasEveryInput,
]


class _BytesListUpdateSet(TypedDict):
    set: List['fields.Base64']


class _BytesListUpdatePush(TypedDict):
    push: List['fields.Base64']


BytesListUpdate = Union[
    List['fields.Base64'],
    _BytesListUpdateSet,
    _BytesListUpdatePush,
]

class _DateTimeListFilterEqualsInput(TypedDict):
    equals: Optional[List[datetime.datetime]]


class _DateTimeListFilterHasInput(TypedDict):
    has: datetime.datetime


class _DateTimeListFilterHasEveryInput(TypedDict):
    has_every: List[datetime.datetime]


class _DateTimeListFilterHasSomeInput(TypedDict):
    has_some: List[datetime.datetime]


class _DateTimeListFilterIsEmptyInput(TypedDict):
    is_empty: bool


DateTimeListFilter = Union[
    _DateTimeListFilterHasInput,
    _DateTimeListFilterEqualsInput,
    _DateTimeListFilterHasSomeInput,
    _DateTimeListFilterIsEmptyInput,
    _DateTimeListFilterHasEveryInput,
]


class _DateTimeListUpdateSet(TypedDict):
    set: List[datetime.datetime]


class _DateTimeListUpdatePush(TypedDict):
    push: List[datetime.datetime]


DateTimeListUpdate = Union[
    List[datetime.datetime],
    _DateTimeListUpdateSet,
    _DateTimeListUpdatePush,
]

class _BooleanListFilterEqualsInput(TypedDict):
    equals: Optional[List[_bool]]


class _BooleanListFilterHasInput(TypedDict):
    has: _bool


class _BooleanListFilterHasEveryInput(TypedDict):
    has_every: List[_bool]


class _BooleanListFilterHasSomeInput(TypedDict):
    has_some: List[_bool]


class _BooleanListFilterIsEmptyInput(TypedDict):
    is_empty: bool


BooleanListFilter = Union[
    _BooleanListFilterHasInput,
    _BooleanListFilterEqualsInput,
    _BooleanListFilterHasSomeInput,
    _BooleanListFilterIsEmptyInput,
    _BooleanListFilterHasEveryInput,
]


class _BooleanListUpdateSet(TypedDict):
    set: List[_bool]


class _BooleanListUpdatePush(TypedDict):
    push: List[_bool]


BooleanListUpdate = Union[
    List[_bool],
    _BooleanListUpdateSet,
    _BooleanListUpdatePush,
]

class _IntListFilterEqualsInput(TypedDict):
    equals: Optional[List[_int]]


class _IntListFilterHasInput(TypedDict):
    has: _int


class _IntListFilterHasEveryInput(TypedDict):
    has_every: List[_int]


class _IntListFilterHasSomeInput(TypedDict):
    has_some: List[_int]


class _IntListFilterIsEmptyInput(TypedDict):
    is_empty: bool


IntListFilter = Union[
    _IntListFilterHasInput,
    _IntListFilterEqualsInput,
    _IntListFilterHasSomeInput,
    _IntListFilterIsEmptyInput,
    _IntListFilterHasEveryInput,
]


class _IntListUpdateSet(TypedDict):
    set: List[_int]


class _IntListUpdatePush(TypedDict):
    push: List[_int]


IntListUpdate = Union[
    List[_int],
    _IntListUpdateSet,
    _IntListUpdatePush,
]

class _BigIntListFilterEqualsInput(TypedDict):
    equals: Optional[List[_int]]


class _BigIntListFilterHasInput(TypedDict):
    has: _int


class _BigIntListFilterHasEveryInput(TypedDict):
    has_every: List[_int]


class _BigIntListFilterHasSomeInput(TypedDict):
    has_some: List[_int]


class _BigIntListFilterIsEmptyInput(TypedDict):
    is_empty: bool


BigIntListFilter = Union[
    _BigIntListFilterHasInput,
    _BigIntListFilterEqualsInput,
    _BigIntListFilterHasSomeInput,
    _BigIntListFilterIsEmptyInput,
    _BigIntListFilterHasEveryInput,
]


class _BigIntListUpdateSet(TypedDict):
    set: List[_int]


class _BigIntListUpdatePush(TypedDict):
    push: List[_int]


BigIntListUpdate = Union[
    List[_int],
    _BigIntListUpdateSet,
    _BigIntListUpdatePush,
]

class _FloatListFilterEqualsInput(TypedDict):
    equals: Optional[List[_float]]


class _FloatListFilterHasInput(TypedDict):
    has: _float


class _FloatListFilterHasEveryInput(TypedDict):
    has_every: List[_float]


class _FloatListFilterHasSomeInput(TypedDict):
    has_some: List[_float]


class _FloatListFilterIsEmptyInput(TypedDict):
    is_empty: bool


FloatListFilter = Union[
    _FloatListFilterHasInput,
    _FloatListFilterEqualsInput,
    _FloatListFilterHasSomeInput,
    _FloatListFilterIsEmptyInput,
    _FloatListFilterHasEveryInput,
]


class _FloatListUpdateSet(TypedDict):
    set: List[_float]


class _FloatListUpdatePush(TypedDict):
    push: List[_float]


FloatListUpdate = Union[
    List[_float],
    _FloatListUpdateSet,
    _FloatListUpdatePush,
]

class _JsonListFilterEqualsInput(TypedDict):
    equals: Optional[List['fields.Json']]


class _JsonListFilterHasInput(TypedDict):
    has: 'fields.Json'


class _JsonListFilterHasEveryInput(TypedDict):
    has_every: List['fields.Json']


class _JsonListFilterHasSomeInput(TypedDict):
    has_some: List['fields.Json']


class _JsonListFilterIsEmptyInput(TypedDict):
    is_empty: bool


JsonListFilter = Union[
    _JsonListFilterHasInput,
    _JsonListFilterEqualsInput,
    _JsonListFilterHasSomeInput,
    _JsonListFilterIsEmptyInput,
    _JsonListFilterHasEveryInput,
]


class _JsonListUpdateSet(TypedDict):
    set: List['fields.Json']


class _JsonListUpdatePush(TypedDict):
    push: List['fields.Json']


JsonListUpdate = Union[
    List['fields.Json'],
    _JsonListUpdateSet,
    _JsonListUpdatePush,
]

class _DecimalListFilterEqualsInput(TypedDict):
    equals: Optional[List[decimal.Decimal]]


class _DecimalListFilterHasInput(TypedDict):
    has: decimal.Decimal


class _DecimalListFilterHasEveryInput(TypedDict):
    has_every: List[decimal.Decimal]


class _DecimalListFilterHasSomeInput(TypedDict):
    has_some: List[decimal.Decimal]


class _DecimalListFilterIsEmptyInput(TypedDict):
    is_empty: bool


DecimalListFilter = Union[
    _DecimalListFilterHasInput,
    _DecimalListFilterEqualsInput,
    _DecimalListFilterHasSomeInput,
    _DecimalListFilterIsEmptyInput,
    _DecimalListFilterHasEveryInput,
]


class _DecimalListUpdateSet(TypedDict):
    set: List[decimal.Decimal]


class _DecimalListUpdatePush(TypedDict):
    push: List[decimal.Decimal]


DecimalListUpdate = Union[
    List[decimal.Decimal],
    _DecimalListUpdateSet,
    _DecimalListUpdatePush,
]


# Items types

class ItemsOptionalCreateInput(TypedDict, total=False):
    """Optional arguments to the Items create method"""
    id: _str
    created_at: Optional[datetime.datetime]


class ItemsCreateInput(ItemsOptionalCreateInput):
    """Required arguments to the Items create method"""
    name: _str
    price: _int


# TODO: remove this in favour of without explicit relations
# e.g. PostCreateWithoutAuthorInput

class ItemsOptionalCreateWithoutRelationsInput(TypedDict, total=False):
    """Optional arguments to the Items create method, without relations"""
    id: _str
    created_at: Optional[datetime.datetime]


class ItemsCreateWithoutRelationsInput(ItemsOptionalCreateWithoutRelationsInput):
    """Required arguments to the Items create method, without relations"""
    name: _str
    price: _int


class ItemsCreateNestedWithoutRelationsInput(TypedDict, total=False):
    create: 'ItemsCreateWithoutRelationsInput'
    connect: 'ItemsWhereUniqueInput'


class ItemsCreateManyNestedWithoutRelationsInput(TypedDict, total=False):
    create: Union['ItemsCreateWithoutRelationsInput', List['ItemsCreateWithoutRelationsInput']]
    connect: Union['ItemsWhereUniqueInput', List['ItemsWhereUniqueInput']]


_ItemsWhereUnique_id_Input = TypedDict(
    '_ItemsWhereUnique_id_Input',
    {
        'id': '_str',
    },
    total=True
)

ItemsWhereUniqueInput = _ItemsWhereUnique_id_Input


class ItemsUpdateInput(TypedDict, total=False):
    """Optional arguments for updating a record"""
    id: _str
    created_at: Optional[datetime.datetime]
    name: _str
    price: Union[AtomicBigIntInput, _int]


class ItemsUpdateManyMutationInput(TypedDict, total=False):
    """Arguments for updating many records"""
    id: _str
    created_at: Optional[datetime.datetime]
    name: _str
    price: Union[AtomicBigIntInput, _int]


class ItemsUpdateManyWithoutRelationsInput(TypedDict, total=False):
    create: List['ItemsCreateWithoutRelationsInput']
    connect: List['ItemsWhereUniqueInput']
    set: List['ItemsWhereUniqueInput']
    disconnect: List['ItemsWhereUniqueInput']
    delete: List['ItemsWhereUniqueInput']

    # TODO
    # update: List['ItemsUpdateWithWhereUniqueWithoutRelationsInput']
    # updateMany: List['ItemsUpdateManyWithWhereUniqueWithoutRelationsInput']
    # deleteMany: List['ItemsScalarWhereInput']
    # upsert: List['ItemsUpserteWithWhereUniqueWithoutRelationsInput']
    # connectOrCreate: List['ItemsCreateOrConnectWithoutRelationsInput']


class ItemsUpdateOneWithoutRelationsInput(TypedDict, total=False):
    create: 'ItemsCreateWithoutRelationsInput'
    connect: 'ItemsWhereUniqueInput'
    disconnect: bool
    delete: bool

    # TODO
    # update: 'ItemsUpdateInput'
    # upsert: 'ItemsUpsertWithoutRelationsInput'
    # connectOrCreate: 'ItemsCreateOrConnectWithoutRelationsInput'


class ItemsUpsertInput(TypedDict):
    create: 'ItemsCreateInput'
    update: 'ItemsUpdateInput'  # pyright: ignore[reportIncompatibleMethodOverride]


_Items_id_OrderByInput = TypedDict(
    '_Items_id_OrderByInput',
    {
        'id': 'SortOrder',
    },
    total=True
)

_Items_created_at_OrderByInput = TypedDict(
    '_Items_created_at_OrderByInput',
    {
        'created_at': 'SortOrder',
    },
    total=True
)

_Items_name_OrderByInput = TypedDict(
    '_Items_name_OrderByInput',
    {
        'name': 'SortOrder',
    },
    total=True
)

_Items_price_OrderByInput = TypedDict(
    '_Items_price_OrderByInput',
    {
        'price': 'SortOrder',
    },
    total=True
)

ItemsOrderByInput = Union[
    '_Items_id_OrderByInput',
    '_Items_created_at_OrderByInput',
    '_Items_name_OrderByInput',
    '_Items_price_OrderByInput',
]



# recursive Items types
# TODO: cleanup these types


# Dict[str, Any] is a mypy limitation
# see https://github.com/RobertCraigie/prisma-client-py/issues/45
# switch to pyright for improved types, see https://prisma-client-py.readthedocs.io/en/stable/reference/limitations/

ItemsRelationFilter = TypedDict(
    'ItemsRelationFilter',
    {
        'is': 'Dict[str, Any]',
        'is_not': 'Dict[str, Any]',
    },
    total=False,
)


class ItemsListRelationFilter(TypedDict, total=False):
    some: 'Dict[str, Any]'
    none: 'Dict[str, Any]'
    every: 'Dict[str, Any]'


class ItemsInclude(TypedDict, total=False):
    """Items relational arguments"""


    

class ItemsIncludeFromItems(TypedDict, total=False):
    """Relational arguments for Items"""


class ItemsIncludeFromItemsRecursive1(TypedDict, total=False):
    """Relational arguments for Items"""


class ItemsIncludeFromItemsRecursive2(TypedDict, total=False):
    """Relational arguments for Items"""


class ItemsIncludeFromItemsRecursive3(TypedDict, total=False):
    """Relational arguments for Items"""


class ItemsIncludeFromItemsRecursive4(TypedDict, total=False):
    """Relational arguments for Items"""

    

class ItemsArgsFromItems(TypedDict, total=False):
    """Arguments for Items"""
    include: 'ItemsIncludeFromItemsRecursive1'


class ItemsArgsFromItemsRecursive1(TypedDict, total=False):
    """Arguments for Items"""
    include: 'ItemsIncludeFromItemsRecursive2'


class ItemsArgsFromItemsRecursive2(TypedDict, total=False):
    """Arguments for Items"""
    include: 'ItemsIncludeFromItemsRecursive3'


class ItemsArgsFromItemsRecursive3(TypedDict, total=False):
    """Arguments for Items"""
    include: 'ItemsIncludeFromItemsRecursive4'


class ItemsArgsFromItemsRecursive4(TypedDict, total=False):
    """Arguments for Items"""
    
    

class FindManyItemsArgsFromItems(TypedDict, total=False):
    """Arguments for Items"""
    take: int
    skip: int
    order_by: Union['ItemsOrderByInput', List['ItemsOrderByInput']]
    where: 'ItemsWhereInput'
    cursor: 'ItemsWhereUniqueInput'
    distinct: List['ItemsScalarFieldKeys']
    include: 'ItemsIncludeFromItemsRecursive1'


class FindManyItemsArgsFromItemsRecursive1(TypedDict, total=False):
    """Arguments for Items"""
    take: int
    skip: int
    order_by: Union['ItemsOrderByInput', List['ItemsOrderByInput']]
    where: 'ItemsWhereInput'
    cursor: 'ItemsWhereUniqueInput'
    distinct: List['ItemsScalarFieldKeys']
    include: 'ItemsIncludeFromItemsRecursive2'


class FindManyItemsArgsFromItemsRecursive2(TypedDict, total=False):
    """Arguments for Items"""
    take: int
    skip: int
    order_by: Union['ItemsOrderByInput', List['ItemsOrderByInput']]
    where: 'ItemsWhereInput'
    cursor: 'ItemsWhereUniqueInput'
    distinct: List['ItemsScalarFieldKeys']
    include: 'ItemsIncludeFromItemsRecursive3'


class FindManyItemsArgsFromItemsRecursive3(TypedDict, total=False):
    """Arguments for Items"""
    take: int
    skip: int
    order_by: Union['ItemsOrderByInput', List['ItemsOrderByInput']]
    where: 'ItemsWhereInput'
    cursor: 'ItemsWhereUniqueInput'
    distinct: List['ItemsScalarFieldKeys']
    include: 'ItemsIncludeFromItemsRecursive4'


class FindManyItemsArgsFromItemsRecursive4(TypedDict, total=False):
    """Arguments for Items"""
    take: int
    skip: int
    order_by: Union['ItemsOrderByInput', List['ItemsOrderByInput']]
    where: 'ItemsWhereInput'
    cursor: 'ItemsWhereUniqueInput'
    distinct: List['ItemsScalarFieldKeys']
    


FindManyItemsArgs = FindManyItemsArgsFromItems
FindFirstItemsArgs = FindManyItemsArgsFromItems


    

class ItemsWhereInput(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringFilter']
    created_at: Union[None, datetime.datetime, 'types.DateTimeFilter']
    name: Union[_str, 'types.StringFilter']
    price: Union[_int, 'types.BigIntFilter']

    # should be noted that AND and NOT should be Union['ItemsWhereInputRecursive1', List['ItemsWhereInputRecursive1']]
    # but this causes mypy to hang :/
    AND: List['ItemsWhereInputRecursive1']
    OR: List['ItemsWhereInputRecursive1']
    NOT: List['ItemsWhereInputRecursive1']


class ItemsWhereInputRecursive1(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringFilter']
    created_at: Union[None, datetime.datetime, 'types.DateTimeFilter']
    name: Union[_str, 'types.StringFilter']
    price: Union[_int, 'types.BigIntFilter']

    # should be noted that AND and NOT should be Union['ItemsWhereInputRecursive2', List['ItemsWhereInputRecursive2']]
    # but this causes mypy to hang :/
    AND: List['ItemsWhereInputRecursive2']
    OR: List['ItemsWhereInputRecursive2']
    NOT: List['ItemsWhereInputRecursive2']


class ItemsWhereInputRecursive2(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringFilter']
    created_at: Union[None, datetime.datetime, 'types.DateTimeFilter']
    name: Union[_str, 'types.StringFilter']
    price: Union[_int, 'types.BigIntFilter']

    # should be noted that AND and NOT should be Union['ItemsWhereInputRecursive3', List['ItemsWhereInputRecursive3']]
    # but this causes mypy to hang :/
    AND: List['ItemsWhereInputRecursive3']
    OR: List['ItemsWhereInputRecursive3']
    NOT: List['ItemsWhereInputRecursive3']


class ItemsWhereInputRecursive3(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringFilter']
    created_at: Union[None, datetime.datetime, 'types.DateTimeFilter']
    name: Union[_str, 'types.StringFilter']
    price: Union[_int, 'types.BigIntFilter']

    # should be noted that AND and NOT should be Union['ItemsWhereInputRecursive4', List['ItemsWhereInputRecursive4']]
    # but this causes mypy to hang :/
    AND: List['ItemsWhereInputRecursive4']
    OR: List['ItemsWhereInputRecursive4']
    NOT: List['ItemsWhereInputRecursive4']


class ItemsWhereInputRecursive4(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringFilter']
    created_at: Union[None, datetime.datetime, 'types.DateTimeFilter']
    name: Union[_str, 'types.StringFilter']
    price: Union[_int, 'types.BigIntFilter']



# aggregate Items types


    

class ItemsScalarWhereWithAggregatesInput(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringWithAggregatesFilter']
    created_at: Union[datetime.datetime, 'types.DateTimeWithAggregatesFilter']
    name: Union[_str, 'types.StringWithAggregatesFilter']
    price: Union[_int, 'types.BigIntWithAggregatesFilter']

    AND: List['ItemsScalarWhereWithAggregatesInputRecursive1']
    OR: List['ItemsScalarWhereWithAggregatesInputRecursive1']
    NOT: List['ItemsScalarWhereWithAggregatesInputRecursive1']


class ItemsScalarWhereWithAggregatesInputRecursive1(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringWithAggregatesFilter']
    created_at: Union[datetime.datetime, 'types.DateTimeWithAggregatesFilter']
    name: Union[_str, 'types.StringWithAggregatesFilter']
    price: Union[_int, 'types.BigIntWithAggregatesFilter']

    AND: List['ItemsScalarWhereWithAggregatesInputRecursive2']
    OR: List['ItemsScalarWhereWithAggregatesInputRecursive2']
    NOT: List['ItemsScalarWhereWithAggregatesInputRecursive2']


class ItemsScalarWhereWithAggregatesInputRecursive2(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringWithAggregatesFilter']
    created_at: Union[datetime.datetime, 'types.DateTimeWithAggregatesFilter']
    name: Union[_str, 'types.StringWithAggregatesFilter']
    price: Union[_int, 'types.BigIntWithAggregatesFilter']

    AND: List['ItemsScalarWhereWithAggregatesInputRecursive3']
    OR: List['ItemsScalarWhereWithAggregatesInputRecursive3']
    NOT: List['ItemsScalarWhereWithAggregatesInputRecursive3']


class ItemsScalarWhereWithAggregatesInputRecursive3(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringWithAggregatesFilter']
    created_at: Union[datetime.datetime, 'types.DateTimeWithAggregatesFilter']
    name: Union[_str, 'types.StringWithAggregatesFilter']
    price: Union[_int, 'types.BigIntWithAggregatesFilter']

    AND: List['ItemsScalarWhereWithAggregatesInputRecursive4']
    OR: List['ItemsScalarWhereWithAggregatesInputRecursive4']
    NOT: List['ItemsScalarWhereWithAggregatesInputRecursive4']


class ItemsScalarWhereWithAggregatesInputRecursive4(TypedDict, total=False):
    """Items arguments for searching"""
    id: Union[_str, 'types.StringWithAggregatesFilter']
    created_at: Union[datetime.datetime, 'types.DateTimeWithAggregatesFilter']
    name: Union[_str, 'types.StringWithAggregatesFilter']
    price: Union[_int, 'types.BigIntWithAggregatesFilter']



class ItemsGroupByOutput(TypedDict, total=False):
    id: _str
    created_at: datetime.datetime
    name: _str
    price: _int
    _sum: 'ItemsSumAggregateOutput'
    _avg: 'ItemsAvgAggregateOutput'
    _min: 'ItemsMinAggregateOutput'
    _max: 'ItemsMaxAggregateOutput'
    _count: 'ItemsCountAggregateOutput'


class ItemsAvgAggregateOutput(TypedDict, total=False):
    """Items output for aggregating averages"""
    price: float


class ItemsSumAggregateOutput(TypedDict, total=False):
    """Items output for aggregating sums"""
    price: _int


class ItemsScalarAggregateOutput(TypedDict, total=False):
    """Items output including scalar fields"""
    id: _str
    created_at: datetime.datetime
    name: _str
    price: _int


ItemsMinAggregateOutput = ItemsScalarAggregateOutput
ItemsMaxAggregateOutput = ItemsScalarAggregateOutput


class ItemsMaxAggregateInput(TypedDict, total=False):
    """Items input for aggregating by max"""
    id: bool
    created_at: bool
    name: bool
    price: bool


class ItemsMinAggregateInput(TypedDict, total=False):
    """Items input for aggregating by min"""
    id: bool
    created_at: bool
    name: bool
    price: bool


class ItemsNumberAggregateInput(TypedDict, total=False):
    """Items input for aggregating numbers"""
    price: bool


ItemsAvgAggregateInput = ItemsNumberAggregateInput
ItemsSumAggregateInput = ItemsNumberAggregateInput


ItemsCountAggregateInput = TypedDict(
    'ItemsCountAggregateInput',
    {
        'id': bool,
        'created_at': bool,
        'name': bool,
        'price': bool,
        '_all': bool,
    },
    total=False,
)

ItemsCountAggregateOutput = TypedDict(
    'ItemsCountAggregateOutput',
    {
        'id': int,
        'created_at': int,
        'name': int,
        'price': int,
        '_all': int,
    },
    total=False,
)


ItemsKeys = Literal[
    'id',
    'created_at',
    'name',
    'price',
]
ItemsScalarFieldKeys = Literal[
    'id',
    'created_at',
    'name',
    'price',
]
ItemsScalarFieldKeysT = TypeVar('ItemsScalarFieldKeysT', bound=ItemsScalarFieldKeys)

ItemsRelationalFieldKeys = _NoneType



# we have to import ourselves as types can be namespaced to types
from . import types, enums, models, fields