#  `enum` — Support for enumerations[¶](https://docs.python.org/3/library/enum.html#module-enum "Link to this heading")
Added in version 3.4.
**Source code:**
Important
This page contains the API reference information. For tutorial information and discussion of more advanced topics, see
  * [Basic Tutorial](https://docs.python.org/3/howto/enum.html#enum-basic-tutorial)
  * [Advanced Tutorial](https://docs.python.org/3/howto/enum.html#enum-advanced-tutorial)
  * [Enum Cookbook](https://docs.python.org/3/howto/enum.html#enum-cookbook)


* * *
An enumeration:
  * is a set of symbolic names (members) bound to unique values
  * can be iterated over to return its canonical (i.e. non-alias) members in definition order
  * uses _call_ syntax to return members by value
  * uses _index_ syntax to return members by name


Enumerations are created either by using [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) syntax, or by using function-call syntax:
Copy```
>>> from enum import Enum

>>> # class syntax
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3

>>> # functional syntax
>>> Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])

```

Even though we can use [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) syntax to create Enums, Enums are not normal Python classes. See [How are Enums different?](https://docs.python.org/3/howto/enum.html#enum-class-differences) for more details.
Note
Nomenclature
  * The class `Color` is an _enumeration_ (or _enum_)
  * The attributes `Color.RED`, `Color.GREEN`, etc., are _enumeration members_ (or _members_) and are functionally constants.
  * The enum members have _names_ and _values_ (the name of `Color.RED` is `RED`, the value of `Color.BLUE` is `3`, etc.)


* * *
## Module Contents[¶](https://docs.python.org/3/library/enum.html#module-contents "Link to this heading")
> [`EnumType`](https://docs.python.org/3/library/enum.html#enum.EnumType "enum.EnumType")
>> The `type` for Enum and its subclasses.
> [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum")
>> Base class for creating enumerated constants.
> [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum")
>> Base class for creating enumerated constants that are also subclasses of [`int`](https://docs.python.org/3/library/functions.html#int "int"). ([Notes](https://docs.python.org/3/library/enum.html#notes))
> [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum")
>> Base class for creating enumerated constants that are also subclasses of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). ([Notes](https://docs.python.org/3/library/enum.html#notes))
> [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag")
>> Base class for creating enumerated constants that can be combined using the bitwise operations without losing their [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") membership.
> [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag")
>> Base class for creating enumerated constants that can be combined using the bitwise operators without losing their [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") membership. `IntFlag` members are also subclasses of [`int`](https://docs.python.org/3/library/functions.html#int "int"). ([Notes](https://docs.python.org/3/library/enum.html#notes))
> [`ReprEnum`](https://docs.python.org/3/library/enum.html#enum.ReprEnum "enum.ReprEnum")
>> Used by [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum"), [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum"), and [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") to keep the [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") of the mixed-in type.
> [`EnumCheck`](https://docs.python.org/3/library/enum.html#enum.EnumCheck "enum.EnumCheck")
>> An enumeration with the values `CONTINUOUS`, `NAMED_FLAGS`, and `UNIQUE`, for use with [`verify()`](https://docs.python.org/3/library/enum.html#enum.verify "enum.verify") to ensure various constraints are met by a given enumeration.
> [`FlagBoundary`](https://docs.python.org/3/library/enum.html#enum.FlagBoundary "enum.FlagBoundary")
>> An enumeration with the values `STRICT`, `CONFORM`, `EJECT`, and `KEEP` which allows for more fine-grained control over how invalid values are dealt with in an enumeration.
> [`EnumDict`](https://docs.python.org/3/library/enum.html#enum.EnumDict "enum.EnumDict")
>> A subclass of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") for use when subclassing [`EnumType`](https://docs.python.org/3/library/enum.html#enum.EnumType "enum.EnumType").
> [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto")
>> Instances are replaced with an appropriate value for Enum members. [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum") defaults to the lower-cased version of the member name, while other Enums default to 1 and increase from there.
> [`property()`](https://docs.python.org/3/library/enum.html#enum.property "enum.property")
>> Allows [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") members to have attributes without conflicting with member names. The `value` and `name` attributes are implemented this way.
> [`unique()`](https://docs.python.org/3/library/enum.html#enum.unique "enum.unique")
>> Enum class decorator that ensures only one name is bound to any one value.
> [`verify()`](https://docs.python.org/3/library/enum.html#enum.verify "enum.verify")
>> Enum class decorator that checks user-selectable constraints on an enumeration.
> [`member()`](https://docs.python.org/3/library/enum.html#enum.member "enum.member")
>> Make `obj` a member. Can be used as a decorator.
> [`nonmember()`](https://docs.python.org/3/library/enum.html#enum.nonmember "enum.nonmember")
>> Do not make `obj` a member. Can be used as a decorator.
> [`global_enum()`](https://docs.python.org/3/library/enum.html#enum.global_enum "enum.global_enum")
>> Modify the [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") and [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") of an enum to show its members as belonging to the module instead of its class, and export the enum members to the global namespace.
> [`show_flag_values()`](https://docs.python.org/3/library/enum.html#enum.show_flag_values "enum.show_flag_values")
>> Return a list of all power-of-two integers contained in a flag.
> [`enum.bin()`](https://docs.python.org/3/library/enum.html#enum.bin "enum.bin")
>> Like built-in [`bin()`](https://docs.python.org/3/library/functions.html#bin "bin"), except negative values are represented in two’s complement, and the leading bit always indicates sign (`0` implies positive, `1` implies negative).
Added in version 3.6: `Flag`, `IntFlag`, `auto`
Added in version 3.11: `StrEnum`, `EnumCheck`, `ReprEnum`, `FlagBoundary`, `property`, `member`, `nonmember`, `global_enum`, `show_flag_values`
Added in version 3.13: `EnumDict`
* * *
## Data Types[¶](https://docs.python.org/3/library/enum.html#data-types "Link to this heading")

_class_ enum.EnumType[¶](https://docs.python.org/3/library/enum.html#enum.EnumType "Link to this definition")

_EnumType_ is the [metaclass](https://docs.python.org/3/glossary.html#term-metaclass) for _enum_ enumerations. It is possible to subclass _EnumType_ – see [Subclassing EnumType](https://docs.python.org/3/howto/enum.html#enumtype-examples) for details.
`EnumType` is responsible for setting the correct `__repr__()`, `__str__()`, `__format__()`, and `__reduce__()` methods on the final _enum_ , as well as creating the enum members, properly handling duplicates, providing iteration over the enum class, etc.
Added in version 3.11: Before 3.11 `EnumType` was called `EnumMeta`, which is still available as an alias.

__call__(_cls_ , _value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__call__ "Link to this definition")

This method is called in two different ways:
  * to look up an existing member:
>

cls:

> The enum class being called.

value:

> The value to lookup.
  * to use the `cls` enum to create a new enum (only if the existing enum does not have any members):
>

cls:

> The enum class being called.

value:

> The name of the new Enum to create.

names:

> The names/values of the members for the new Enum.

module:

> The name of the module the new Enum is created in.

qualname:

> The actual location in the module where this Enum can be found.

type:

> A mix-in type for the new Enum.

start:

> The first integer value for the Enum (used by [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto")).

boundary:

> How to handle out-of-range values from bit operations ([`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") only).



__contains__(_cls_ , _member_)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__contains__ "Link to this definition")

Returns `True` if member belongs to the `cls`:
Copy```
>>> some_var = Color.RED
>>> some_var in Color
True
>>> Color.RED.value in Color
True

```

Changed in version 3.12: Before Python 3.12, a `TypeError` is raised if a non-Enum-member is used in a containment check.

__dir__(_cls_)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__dir__ "Link to this definition")

Returns `['__class__', '__doc__', '__members__', '__module__']` and the names of the members in _cls_ :
Copy```
>>> dir(Color)
['BLUE', 'GREEN', 'RED', '__class__', '__contains__', '__doc__', '__getitem__', '__init_subclass__', '__iter__', '__len__', '__members__', '__module__', '__name__', '__qualname__']

```


__getitem__(_cls_ , _name_)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__getitem__ "Link to this definition")

Returns the Enum member in _cls_ matching _name_ , or raises a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError"):
Copy```
>>> Color['BLUE']
<Color.BLUE: 3>

```


__iter__(_cls_)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__iter__ "Link to this definition")

Returns each member in _cls_ in definition order:
Copy```
>>> list(Color)
[<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

```


__len__(_cls_)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__len__ "Link to this definition")

Returns the number of member in _cls_ :
Copy```
>>> len(Color)
3

```


__members__[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__members__ "Link to this definition")

Returns a mapping of every enum name to its member, including aliases

__reversed__(_cls_)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__reversed__ "Link to this definition")

Returns each member in _cls_ in reverse definition order:
Copy```
>>> list(reversed(Color))
[<Color.BLUE: 3>, <Color.GREEN: 2>, <Color.RED: 1>]

```


_class_ enum.Enum[¶](https://docs.python.org/3/library/enum.html#enum.Enum "Link to this definition")

_Enum_ is the base class for all _enum_ enumerations.

name[¶](https://docs.python.org/3/library/enum.html#enum.Enum.name "Link to this definition")

The name used to define the `Enum` member:
Copy```
>>> Color.BLUE.name
'BLUE'

```


value[¶](https://docs.python.org/3/library/enum.html#enum.Enum.value "Link to this definition")

The value given to the `Enum` member:
Copy```
>>> Color.RED.value
1

```

Value of the member, can be set in [`__new__()`](https://docs.python.org/3/library/enum.html#enum.Enum.__new__ "enum.Enum.__new__").
Note
Enum member values
Member values can be anything: [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), etc. If the exact value is unimportant you may use [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto") instances and an appropriate value will be chosen for you. See `auto` for the details.
While mutable/unhashable values, such as [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") or a mutable [`dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass"), can be used, they will have a quadratic performance impact during creation relative to the total number of mutable/unhashable values in the enum.

_name_[¶](https://docs.python.org/3/library/enum.html#enum.Enum._name_ "Link to this definition")

Name of the member.

_value_[¶](https://docs.python.org/3/library/enum.html#enum.Enum._value_ "Link to this definition")

Value of the member, can be set in [`__new__()`](https://docs.python.org/3/library/enum.html#enum.Enum.__new__ "enum.Enum.__new__").

_order_[¶](https://docs.python.org/3/library/enum.html#enum.Enum._order_ "Link to this definition")

No longer used, kept for backward compatibility. (class attribute, removed during class creation).

_ignore_[¶](https://docs.python.org/3/library/enum.html#enum.Enum._ignore_ "Link to this definition")

`_ignore_` is only used during creation and is removed from the enumeration once creation is complete.
`_ignore_` is a list of names that will not become members, and whose names will also be removed from the completed enumeration. See [TimePeriod](https://docs.python.org/3/howto/enum.html#enum-time-period) for an example.

__dir__(_self_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum.__dir__ "Link to this definition")

Returns `['__class__', '__doc__', '__module__', 'name', 'value']` and any public methods defined on _self.__class___ :
Copy```
>>> from enum import Enum
>>> from datetime import date
>>> class Weekday(Enum):
...     MONDAY = 1
...     TUESDAY = 2
...     WEDNESDAY = 3
...     THURSDAY = 4
...     FRIDAY = 5
...     SATURDAY = 6
...     SUNDAY = 7
...     @classmethod
...     def today(cls):
...         print('today is %s' % cls(date.today().isoweekday()).name)
...
>>> dir(Weekday.SATURDAY)
['__class__', '__doc__', '__eq__', '__hash__', '__module__', 'name', 'today', 'value']

```


_generate_next_value_(_name_ , _start_ , _count_ , _last_values_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum._generate_next_value_ "Link to this definition")

>

name:

> The name of the member being defined (e.g. ‘RED’).

start:

> The start value for the Enum; the default is 1.

count:

> The number of members currently defined, not including this one.

last_values:

> A list of the previous values.
A _staticmethod_ that is used to determine the next value returned by [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto"):
Copy```
>>> from enum import auto, Enum
>>> class PowersOfThree(Enum):
...     @staticmethod
...     def _generate_next_value_(name, start, count, last_values):
...         return 3 ** (count + 1)
...     FIRST = auto()
...     SECOND = auto()
...
>>> PowersOfThree.SECOND.value
9

```


__init__(_self_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum.__init__ "Link to this definition")

By default, does nothing. If multiple values are given in the member assignment, those values become separate arguments to `__init__`; e.g.
Copy```
>>> from enum import Enum
>>> class Weekday(Enum):
...     MONDAY = 1, 'Mon'

```

`Weekday.__init__()` would be called as `Weekday.__init__(self, 1, 'Mon')`

__init_subclass__(_cls_ , _** kwds_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum.__init_subclass__ "Link to this definition")

A _classmethod_ that is used to further configure subsequent subclasses. By default, does nothing.

_missing_(_cls_ , _value_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum._missing_ "Link to this definition")

A _classmethod_ for looking up values not found in _cls_. By default it does nothing, but can be overridden to implement custom search behavior:
Copy```
>>> from enum import auto, StrEnum
>>> class Build(StrEnum):
...     DEBUG = auto()
...     OPTIMIZED = auto()
...     @classmethod
...     def _missing_(cls, value):
...         value = value.lower()
...         for member in cls:
...             if member.value == value:
...                 return member
...         return None
...
>>> Build.DEBUG.value
'debug'
>>> Build('deBUG')
<Build.DEBUG: 'debug'>

```


__new__(_cls_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum.__new__ "Link to this definition")

By default, doesn’t exist. If specified, either in the enum class definition or in a mixin class (such as `int`), all values given in the member assignment will be passed; e.g.
Copy```
>>> from enum import Enum
>>> class MyIntEnum(int, Enum):
...     TWENTYSIX = '1a', 16

```

results in the call `int('1a', 16)` and a value of `26` for the member.
Note
When writing a custom `__new__`, do not use `super().__new__` – call the appropriate `__new__` instead.

__repr__(_self_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum.__repr__ "Link to this definition")

Returns the string used for _repr()_ calls. By default, returns the _Enum_ name, member name, and value, but can be overridden:
Copy```
>>> from enum import auto, Enum
>>> class OtherStyle(Enum):
...     ALTERNATE = auto()
...     OTHER = auto()
...     SOMETHING_ELSE = auto()
...     def __repr__(self):
...         cls_name = self.__class__.__name__
...         return f'{cls_name}.{self.name}'
...
>>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
(OtherStyle.ALTERNATE, 'OtherStyle.ALTERNATE', 'OtherStyle.ALTERNATE')

```


__str__(_self_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum.__str__ "Link to this definition")

Returns the string used for _str()_ calls. By default, returns the _Enum_ name and member name, but can be overridden:
Copy```
>>> from enum import auto, Enum
>>> class OtherStyle(Enum):
...     ALTERNATE = auto()
...     OTHER = auto()
...     SOMETHING_ELSE = auto()
...     def __str__(self):
...         return f'{self.name}'
...
>>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
(<OtherStyle.ALTERNATE: 1>, 'ALTERNATE', 'ALTERNATE')

```


__format__(_self_)[¶](https://docs.python.org/3/library/enum.html#enum.Enum.__format__ "Link to this definition")

Returns the string used for _format()_ and _f-string_ calls. By default, returns [`__str__()`](https://docs.python.org/3/library/enum.html#enum.Enum.__str__ "enum.Enum.__str__") return value, but can be overridden:
Copy```
>>> from enum import auto, Enum
>>> class OtherStyle(Enum):
...     ALTERNATE = auto()
...     OTHER = auto()
...     SOMETHING_ELSE = auto()
...     def __format__(self, spec):
...         return f'{self.name}'
...
>>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
(<OtherStyle.ALTERNATE: 1>, 'OtherStyle.ALTERNATE', 'ALTERNATE')

```

Note
Using [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto") with `Enum` results in integers of increasing value, starting with `1`.
Changed in version 3.12: Added [Dataclass support](https://docs.python.org/3/howto/enum.html#enum-dataclass-support)

_add_alias_()[¶](https://docs.python.org/3/library/enum.html#enum.Enum._add_alias_ "Link to this definition")

Adds a new name as an alias to an existing member:
Copy```
>>> Color.RED._add_alias_("ERROR")
>>> Color.ERROR
<Color.RED: 1>

```

Raises a [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError") if the name is already assigned to a different member.
Added in version 3.13.

_add_value_alias_()[¶](https://docs.python.org/3/library/enum.html#enum.Enum._add_value_alias_ "Link to this definition")

Adds a new value as an alias to an existing member:
Copy```
>>> Color.RED._add_value_alias_(42)
>>> Color(42)
<Color.RED: 1>

```

Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the value is already linked with a different member.
Added in version 3.13.

_class_ enum.IntEnum[¶](https://docs.python.org/3/library/enum.html#enum.IntEnum "Link to this definition")

_IntEnum_ is the same as [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum"), but its members are also integers and can be used anywhere that an integer can be used. If any integer operation is performed with an _IntEnum_ member, the resulting value loses its enumeration status.
Copy```
>>> from enum import IntEnum
>>> class Number(IntEnum):
...     ONE = 1
...     TWO = 2
...     THREE = 3
...
>>> Number.THREE
<Number.THREE: 3>
>>> Number.ONE + Number.TWO
3
>>> Number.THREE + 5
8
>>> Number.THREE == 3
True

```

Note
Using [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto") with `IntEnum` results in integers of increasing value, starting with `1`.
Changed in version 3.11: [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__") is now `int.__str__()` to better support the _replacement of existing constants_ use-case. [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__") was already `int.__format__()` for that same reason.

_class_ enum.StrEnum[¶](https://docs.python.org/3/library/enum.html#enum.StrEnum "Link to this definition")

_StrEnum_ is the same as [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum"), but its members are also strings and can be used in most of the same places that a string can be used. The result of any string operation performed on or with a _StrEnum_ member is not part of the enumeration.
Copy```
>>> from enum import StrEnum, auto
>>> class Color(StrEnum):
...     RED = 'r'
...     GREEN = 'g'
...     BLUE = 'b'
...     UNKNOWN = auto()
...
>>> Color.RED
<Color.RED: 'r'>
>>> Color.UNKNOWN
<Color.UNKNOWN: 'unknown'>
>>> str(Color.UNKNOWN)
'unknown'

```

Note
There are places in the stdlib that check for an exact [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") instead of a `str` subclass (i.e. `type(unknown) == str` instead of `isinstance(unknown, str)`), and in those locations you will need to use `str(MyStrEnum.MY_MEMBER)`.
Note
Using [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto") with `StrEnum` results in the lower-cased member name as the value.
Note
[`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__") is `str.__str__()` to better support the _replacement of existing constants_ use-case. [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__") is likewise `str.__format__()` for that same reason.
Added in version 3.11.

_class_ enum.Flag[¶](https://docs.python.org/3/library/enum.html#enum.Flag "Link to this definition")

`Flag` is the same as [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum"), but its members support the bitwise operators `&` (_AND_), `|` (_OR_), `^` (_XOR_), and `~` (_INVERT_); the results of those operations are (aliases of) members of the enumeration.

__contains__(_self_ , _value_)[¶](https://docs.python.org/3/library/enum.html#enum.Flag.__contains__ "Link to this definition")

Returns _True_ if value is in self:
Copy```
>>> from enum import Flag, auto
>>> class Color(Flag):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> purple = Color.RED | Color.BLUE
>>> white = Color.RED | Color.GREEN | Color.BLUE
>>> Color.GREEN in purple
False
>>> Color.GREEN in white
True
>>> purple in white
True
>>> white in purple
False

```


__iter__(self):

Returns all contained non-alias members:
Copy```
>>> list(Color.RED)
[<Color.RED: 1>]
>>> list(purple)
[<Color.RED: 1>, <Color.BLUE: 4>]

```

Added in version 3.11.

__len__(self):

Returns number of members in flag:
Copy```
>>> len(Color.GREEN)
1
>>> len(white)
3

```

Added in version 3.11.

__bool__(self):

Returns _True_ if any members in flag, _False_ otherwise:
Copy```
>>> bool(Color.GREEN)
True
>>> bool(white)
True
>>> black = Color(0)
>>> bool(black)
False

```


__or__(_self_ , _other_)[¶](https://docs.python.org/3/library/enum.html#enum.Flag.__or__ "Link to this definition")

Returns current flag binary or’ed with other:
Copy```
>>> Color.RED | Color.GREEN
<Color.RED|GREEN: 3>

```


__and__(_self_ , _other_)[¶](https://docs.python.org/3/library/enum.html#enum.Flag.__and__ "Link to this definition")

Returns current flag binary and’ed with other:
Copy```
>>> purple & white
<Color.RED|BLUE: 5>
>>> purple & Color.GREEN
<Color: 0>

```


__xor__(_self_ , _other_)[¶](https://docs.python.org/3/library/enum.html#enum.Flag.__xor__ "Link to this definition")

Returns current flag binary xor’ed with other:
Copy```
>>> purple ^ white
<Color.GREEN: 2>
>>> purple ^ Color.GREEN
<Color.RED|GREEN|BLUE: 7>

```


__invert__(self):

Returns all the flags in _type(self)_ that are not in _self_ :
Copy```
>>> ~white
<Color: 0>
>>> ~purple
<Color.GREEN: 2>
>>> ~Color.RED
<Color.GREEN|BLUE: 6>

```


_numeric_repr_()[¶](https://docs.python.org/3/library/enum.html#enum.Flag._numeric_repr_ "Link to this definition")

Function used to format any remaining unnamed numeric values. Default is the value’s repr; common choices are [`hex()`](https://docs.python.org/3/library/functions.html#hex "hex") and [`oct()`](https://docs.python.org/3/library/functions.html#oct "oct").
Note
Using [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto") with `Flag` results in integers that are powers of two, starting with `1`.
Changed in version 3.11: The _repr()_ of zero-valued flags has changed. It is now:
Copy```
>>> Color(0)
<Color: 0>

```


_class_ enum.IntFlag[¶](https://docs.python.org/3/library/enum.html#enum.IntFlag "Link to this definition")

`IntFlag` is the same as [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag"), but its members are also integers and can be used anywhere that an integer can be used.
Copy```
>>> from enum import IntFlag, auto
>>> class Color(IntFlag):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> Color.RED & 2
<Color: 0>
>>> Color.RED | 2
<Color.RED|GREEN: 3>

```

If any integer operation is performed with an _IntFlag_ member, the result is not an _IntFlag_ :
Copy```
>>> Color.RED + 2
3

```

If a [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") operation is performed with an _IntFlag_ member and:
  * the result is a valid _IntFlag_ : an _IntFlag_ is returned
  * the result is not a valid _IntFlag_ : the result depends on the [`FlagBoundary`](https://docs.python.org/3/library/enum.html#enum.FlagBoundary "enum.FlagBoundary") setting


The [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") of unnamed zero-valued flags has changed. It is now:
Copy```
>>> Color(0)
<Color: 0>

```

Note
Using [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto") with `IntFlag` results in integers that are powers of two, starting with `1`.
Changed in version 3.11: [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__") is now `int.__str__()` to better support the _replacement of existing constants_ use-case. [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__") was already `int.__format__()` for that same reason.
Inversion of an `IntFlag` now returns a positive value that is the union of all flags not in the given flag, rather than a negative value. This matches the existing [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") behavior.

_class_ enum.ReprEnum[¶](https://docs.python.org/3/library/enum.html#enum.ReprEnum "Link to this definition")

`ReprEnum` uses the [`repr()`](https://docs.python.org/3/library/enum.html#enum.Enum.__repr__ "enum.Enum.__repr__") of [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum"), but the [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") of the mixed-in data type:
  * `int.__str__()` for [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") and [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag")
  * `str.__str__()` for [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum")


Inherit from `ReprEnum` to keep the [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") / [`format()`](https://docs.python.org/3/library/functions.html#format "format") of the mixed-in data type instead of using the [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum")-default [`str()`](https://docs.python.org/3/library/enum.html#enum.Enum.__str__ "enum.Enum.__str__").
Added in version 3.11.

_class_ enum.EnumCheck[¶](https://docs.python.org/3/library/enum.html#enum.EnumCheck "Link to this definition")

_EnumCheck_ contains the options used by the [`verify()`](https://docs.python.org/3/library/enum.html#enum.verify "enum.verify") decorator to ensure various constraints; failed constraints result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

UNIQUE[¶](https://docs.python.org/3/library/enum.html#enum.EnumCheck.UNIQUE "Link to this definition")

Ensure that each value has only one name:
Copy```
>>> from enum import Enum, verify, UNIQUE
>>> @verify(UNIQUE)
... class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3
...     CRIMSON = 1
Traceback (most recent call last):
...
ValueError: aliases found in <enum 'Color'>: CRIMSON -> RED

```


CONTINUOUS[¶](https://docs.python.org/3/library/enum.html#enum.EnumCheck.CONTINUOUS "Link to this definition")

Ensure that there are no missing values between the lowest-valued member and the highest-valued member:
Copy```
>>> from enum import Enum, verify, CONTINUOUS
>>> @verify(CONTINUOUS)
... class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 5
Traceback (most recent call last):
...
ValueError: invalid enum 'Color': missing values 3, 4

```


NAMED_FLAGS[¶](https://docs.python.org/3/library/enum.html#enum.EnumCheck.NAMED_FLAGS "Link to this definition")

Ensure that any flag groups/masks contain only named flags – useful when values are specified instead of being generated by [`auto()`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto"):
Copy```
>>> from enum import Flag, verify, NAMED_FLAGS
>>> @verify(NAMED_FLAGS)
... class Color(Flag):
...     RED = 1
...     GREEN = 2
...     BLUE = 4
...     WHITE = 15
...     NEON = 31
Traceback (most recent call last):
...
ValueError: invalid Flag 'Color': aliases WHITE and NEON are missing combined values of 0x18 [use enum.show_flag_values(value) for details]

```

Note
CONTINUOUS and NAMED_FLAGS are designed to work with integer-valued members.
Added in version 3.11.

_class_ enum.FlagBoundary[¶](https://docs.python.org/3/library/enum.html#enum.FlagBoundary "Link to this definition")

`FlagBoundary` controls how out-of-range values are handled in [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") and its subclasses.

STRICT[¶](https://docs.python.org/3/library/enum.html#enum.FlagBoundary.STRICT "Link to this definition")

Out-of-range values cause a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to be raised. This is the default for [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag"):
Copy```
>>> from enum import Flag, STRICT, auto
>>> class StrictFlag(Flag, boundary=STRICT):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> StrictFlag(2**2 + 2**4)
Traceback (most recent call last):
...
ValueError: <flag 'StrictFlag'> invalid value 20
    given 0b0 10100
  allowed 0b0 00111

```


CONFORM[¶](https://docs.python.org/3/library/enum.html#enum.FlagBoundary.CONFORM "Link to this definition")

Out-of-range values have invalid values removed, leaving a valid [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") value:
Copy```
>>> from enum import Flag, CONFORM, auto
>>> class ConformFlag(Flag, boundary=CONFORM):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> ConformFlag(2**2 + 2**4)
<ConformFlag.BLUE: 4>

```


EJECT[¶](https://docs.python.org/3/library/enum.html#enum.FlagBoundary.EJECT "Link to this definition")

Out-of-range values lose their [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") membership and revert to [`int`](https://docs.python.org/3/library/functions.html#int "int").
Copy```
>>> from enum import Flag, EJECT, auto
>>> class EjectFlag(Flag, boundary=EJECT):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> EjectFlag(2**2 + 2**4)
20

```


KEEP[¶](https://docs.python.org/3/library/enum.html#enum.FlagBoundary.KEEP "Link to this definition")

Out-of-range values are kept, and the [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") membership is kept. This is the default for [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag"):
Copy```
>>> from enum import Flag, KEEP, auto
>>> class KeepFlag(Flag, boundary=KEEP):
...     RED = auto()
...     GREEN = auto()
...     BLUE = auto()
...
>>> KeepFlag(2**2 + 2**4)
<KeepFlag.BLUE|16: 20>

```

Added in version 3.11.

_class_ enum.EnumDict[¶](https://docs.python.org/3/library/enum.html#enum.EnumDict "Link to this definition")

_EnumDict_ is a subclass of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") that is used as the namespace for defining enum classes (see [Preparing the class namespace](https://docs.python.org/3/reference/datamodel.html#prepare)). It is exposed to allow subclasses of [`EnumType`](https://docs.python.org/3/library/enum.html#enum.EnumType "enum.EnumType") with advanced behavior like having multiple values per member. It should be called with the name of the enum class being created, otherwise private names and internal classes will not be handled correctly.
Note that only the [`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping") interface ([`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__") and [`update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "dict.update")) is overridden. It may be possible to bypass the checks using other `dict` operations like [`|=`](https://docs.python.org/3/reference/datamodel.html#object.__ior__ "object.__ior__").

member_names[¶](https://docs.python.org/3/library/enum.html#enum.EnumDict.member_names "Link to this definition")

A list of member names.
Added in version 3.13.
* * *
### Supported `__dunder__` names[¶](https://docs.python.org/3/library/enum.html#supported-dunder-names "Link to this heading")
[`__members__`](https://docs.python.org/3/library/enum.html#enum.EnumType.__members__ "enum.EnumType.__members__") is a read-only ordered mapping of `member_name`:`member` items. It is only available on the class.
[`__new__()`](https://docs.python.org/3/library/enum.html#enum.Enum.__new__ "enum.Enum.__new__"), if specified, must create and return the enum members; it is also a very good idea to set the member’s `_value_` appropriately. Once all the members are created it is no longer used.
### Supported `_sunder_` names[¶](https://docs.python.org/3/library/enum.html#supported-sunder-names "Link to this heading")
  * [`_name_`](https://docs.python.org/3/library/enum.html#enum.Enum._name_ "enum.Enum._name_") – name of the member
  * [`_value_`](https://docs.python.org/3/library/enum.html#enum.Enum._value_ "enum.Enum._value_") – value of the member; can be set in `__new__`
  * [`_missing_()`](https://docs.python.org/3/library/enum.html#enum.Enum._missing_ "enum.Enum._missing_") – a lookup function used when a value is not found; may be overridden
  * [`_ignore_`](https://docs.python.org/3/library/enum.html#enum.Enum._ignore_ "enum.Enum._ignore_") – a list of names, either as a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") or a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), that will not be transformed into members, and will be removed from the final class
  * [`_order_`](https://docs.python.org/3/library/enum.html#enum.Enum._order_ "enum.Enum._order_") – no longer used, kept for backward compatibility (class attribute, removed during class creation)
  * [`_generate_next_value_()`](https://docs.python.org/3/library/enum.html#enum.Enum._generate_next_value_ "enum.Enum._generate_next_value_") – used to get an appropriate value for an enum member; may be overridden
Note
For standard [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") classes the next value chosen is the highest value seen incremented by one.
For [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") classes the next value chosen will be the next highest power-of-two.
  * [`_add_alias_()`](https://docs.python.org/3/library/enum.html#enum.Enum._add_alias_ "enum.Enum._add_alias_") – adds a new name as an alias to an existing member.
  * [`_add_value_alias_()`](https://docs.python.org/3/library/enum.html#enum.Enum._add_value_alias_ "enum.Enum._add_value_alias_") – adds a new value as an alias to an existing member.
  * While `_sunder_` names are generally reserved for the further development of the [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") class and can not be used, some are explicitly allowed:
    * `_repr_*` (e.g. `_repr_html_`), as used in


Added in version 3.6: `_missing_`, `_order_`, `_generate_next_value_`
Added in version 3.7: `_ignore_`
Added in version 3.13: `_add_alias_`, `_add_value_alias_`, `_repr_*`
* * *
## Utilities and Decorators[¶](https://docs.python.org/3/library/enum.html#utilities-and-decorators "Link to this heading")

_class_ enum.auto[¶](https://docs.python.org/3/library/enum.html#enum.auto "Link to this definition")

_auto_ can be used in place of a value. If used, the _Enum_ machinery will call an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum")’s [`_generate_next_value_()`](https://docs.python.org/3/library/enum.html#enum.Enum._generate_next_value_ "enum.Enum._generate_next_value_") to get an appropriate value. For `Enum` and [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") that appropriate value will be the last value plus one; for [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") and [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") it will be the first power-of-two greater than the highest value; for [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum") it will be the lower-cased version of the member’s name. Care must be taken if mixing _auto()_ with manually specified values.
_auto_ instances are only resolved when at the top level of an assignment, either by itself or as part of a tuple:
  * `FIRST = auto()` will work (auto() is replaced with `1`);
  * `SECOND = auto(), -2` will work (auto is replaced with `2`, so `2, -2` is used to create the `SECOND` enum member;
  * `THREE = [auto(), -3]` will _not_ work (`[<auto instance>, -3]` is used to create the `THREE` enum member)


Changed in version 3.11.1: In prior versions, `auto()` had to be the only thing on the assignment line to work properly.
`_generate_next_value_` can be overridden to customize the values used by _auto_.
Note
in 3.13 the default `_generate_next_value_` will always return the highest member value incremented by 1, and will fail if any member is an incompatible type.

@enum.property[¶](https://docs.python.org/3/library/enum.html#enum.property "Link to this definition")

A decorator similar to the built-in _property_ , but specifically for enumerations. It allows member attributes to have the same names as members themselves.
Note
the _property_ and the member must be defined in separate classes; for example, the _value_ and _name_ attributes are defined in the _Enum_ class, and _Enum_ subclasses can define members with the names `value` and `name`.
Added in version 3.11.

@enum.unique[¶](https://docs.python.org/3/library/enum.html#enum.unique "Link to this definition")

A [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) decorator specifically for enumerations. It searches an enumeration’s [`__members__`](https://docs.python.org/3/library/enum.html#enum.EnumType.__members__ "enum.EnumType.__members__"), gathering any aliases it finds; if any are found [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised with the details:
Copy```
>>> from enum import Enum, unique
>>> @unique
... class Mistake(Enum):
...     ONE = 1
...     TWO = 2
...     THREE = 3
...     FOUR = 3
...
Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE

```


@enum.verify[¶](https://docs.python.org/3/library/enum.html#enum.verify "Link to this definition")

A [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) decorator specifically for enumerations. Members from [`EnumCheck`](https://docs.python.org/3/library/enum.html#enum.EnumCheck "enum.EnumCheck") are used to specify which constraints should be checked on the decorated enumeration.
Added in version 3.11.

@enum.member[¶](https://docs.python.org/3/library/enum.html#enum.member "Link to this definition")

A decorator for use in enums: its target will become a member.
Added in version 3.11.

@enum.nonmember[¶](https://docs.python.org/3/library/enum.html#enum.nonmember "Link to this definition")

A decorator for use in enums: its target will not become a member.
Added in version 3.11.

@enum.global_enum[¶](https://docs.python.org/3/library/enum.html#enum.global_enum "Link to this definition")

A decorator to change the [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") and [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") of an enum to show its members as belonging to the module instead of its class. Should only be used when the enum members are exported to the module global namespace (see [`re.RegexFlag`](https://docs.python.org/3/library/re.html#re.RegexFlag "re.RegexFlag") for an example).
Added in version 3.11.

enum.show_flag_values(_value_)[¶](https://docs.python.org/3/library/enum.html#enum.show_flag_values "Link to this definition")

Return a list of all power-of-two integers contained in a flag _value_.
Added in version 3.11.

enum.bin(_num_ , _max_bits =None_)[¶](https://docs.python.org/3/library/enum.html#enum.bin "Link to this definition")

Like built-in `bin()`, except negative values are represented in two’s complement, and the leading bit always indicates sign (`0` implies positive, `1` implies negative).
Copy```
>>> import enum
>>> enum.bin(10)
'0b0 1010'
>>> enum.bin(~10)   # ~10 is -11
'0b1 0101'

```

Added in version 3.11.
* * *
## Notes[¶](https://docs.python.org/3/library/enum.html#notes "Link to this heading")
[`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum"), [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum"), and [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag")
> These three enum types are designed to be drop-in replacements for existing integer- and string-based values; as such, they have extra limitations:
>   * `__str__` uses the value and not the name of the enum member
>   * `__format__`, because it uses `__str__`, will also use the value of the enum member instead of its name
>

> If you do not need/want those limitations, you can either create your own base class by mixing in the `int` or `str` type yourself:
> Copy```
>>> from enum import Enum
>>> class MyIntEnum(int, Enum):
...     pass

```

> or you can reassign the appropriate [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str"), etc., in your enum:
> Copy```
>>> from enum import Enum, IntEnum
>>> class MyIntEnum(IntEnum):
...     __str__ = Enum.__str__

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`enum` — Support for enumerations](https://docs.python.org/3/library/enum.html)
    * [Module Contents](https://docs.python.org/3/library/enum.html#module-contents)
    * [Data Types](https://docs.python.org/3/library/enum.html#data-types)
      * [Supported `__dunder__` names](https://docs.python.org/3/library/enum.html#supported-dunder-names)
      * [Supported `_sunder_` names](https://docs.python.org/3/library/enum.html#supported-sunder-names)
    * [Utilities and Decorators](https://docs.python.org/3/library/enum.html#utilities-and-decorators)
    * [Notes](https://docs.python.org/3/library/enum.html#notes)


#### Previous topic
[`reprlib` — Alternate `repr()` implementation](https://docs.python.org/3/library/reprlib.html "previous chapter")
#### Next topic
[`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=enum+%E2%80%94+Support+for+enumerations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fenum.html&pagesource=library%2Fenum.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/graphlib.html "graphlib — Functionality to operate with graph-like structures") |
  * [previous](https://docs.python.org/3/library/reprlib.html "reprlib — Alternate repr\(\) implementation") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`enum` — Support for enumerations](https://docs.python.org/3/library/enum.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
