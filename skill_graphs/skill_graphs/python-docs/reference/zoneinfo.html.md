[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html)
    * [Using `ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#using-zoneinfo)
    * [Data sources](https://docs.python.org/3/library/zoneinfo.html#data-sources)
      * [Configuring the data sources](https://docs.python.org/3/library/zoneinfo.html#configuring-the-data-sources)
        * [Compile-time configuration](https://docs.python.org/3/library/zoneinfo.html#compile-time-configuration)
        * [Environment configuration](https://docs.python.org/3/library/zoneinfo.html#environment-configuration)
        * [Runtime configuration](https://docs.python.org/3/library/zoneinfo.html#runtime-configuration)
    * [The `ZoneInfo` class](https://docs.python.org/3/library/zoneinfo.html#the-zoneinfo-class)
      * [String representations](https://docs.python.org/3/library/zoneinfo.html#string-representations)
      * [Pickle serialization](https://docs.python.org/3/library/zoneinfo.html#pickle-serialization)
    * [Functions](https://docs.python.org/3/library/zoneinfo.html#functions)
    * [Globals](https://docs.python.org/3/library/zoneinfo.html#globals)
    * [Exceptions and warnings](https://docs.python.org/3/library/zoneinfo.html#exceptions-and-warnings)


#### Previous topic
[`datetime` — Basic date and time types](https://docs.python.org/3/library/datetime.html "previous chapter")
#### Next topic
[`calendar` — General calendar-related functions](https://docs.python.org/3/library/calendar.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zoneinfo+%E2%80%94+IANA+time+zone+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzoneinfo.html&pagesource=library%2Fzoneinfo.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/calendar.html "calendar — General calendar-related functions") |
  * [previous](https://docs.python.org/3/library/datetime.html "datetime — Basic date and time types") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html)
  * |
  * Theme  Auto Light Dark |


#  `zoneinfo` — IANA time zone support[¶](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo "Link to this heading")
Added in version 3.9.
**Source code:**
* * *
The `zoneinfo` module provides a concrete time zone implementation to support the IANA time zone database as originally specified in [**PEP 615**](https://peps.python.org/pep-0615/). By default, `zoneinfo` uses the system’s time zone data if available; if no system time zone data is available, the library will fall back to using the first-party
See also

Module: [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")

Provides the [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") and [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") types with which the [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") class is designed to be used.

Package

First-party package maintained by the CPython core developers to supply time zone data via PyPI.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
## Using `ZoneInfo`[¶](https://docs.python.org/3/library/zoneinfo.html#using-zoneinfo "Link to this heading")
[`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") is a concrete implementation of the [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") abstract base class, and is intended to be attached to `tzinfo`, either via the constructor, the [`datetime.replace`](https://docs.python.org/3/library/datetime.html#datetime.datetime.replace "datetime.datetime.replace") method or [`datetime.astimezone`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "datetime.datetime.astimezone"):
Copy```
>>> from zoneinfo import ZoneInfo
>>> from datetime import datetime, timedelta

>>> dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(dt)
2020-10-31 12:00:00-07:00

>>> dt.tzname()
'PDT'

```

Datetimes constructed in this way are compatible with datetime arithmetic and handle daylight saving time transitions with no further intervention:
Copy```
>>> dt_add = dt + timedelta(days=1)

>>> print(dt_add)
2020-11-01 12:00:00-08:00

>>> dt_add.tzname()
'PST'

```

These time zones also support the [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") attribute introduced in [**PEP 495**](https://peps.python.org/pep-0495/). During offset transitions which induce ambiguous times (such as a daylight saving time to standard time transition), the offset from _before_ the transition is used when `fold=0`, and the offset _after_ the transition is used when `fold=1`, for example:
Copy```
>>> dt = datetime(2020, 11, 1, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(dt)
2020-11-01 01:00:00-07:00

>>> print(dt.replace(fold=1))
2020-11-01 01:00:00-08:00

```

When converting from another time zone, the fold will be set to the correct value:
Copy```
>>> from datetime import timezone
>>> LOS_ANGELES = ZoneInfo("America/Los_Angeles")
>>> dt_utc = datetime(2020, 11, 1, 8, tzinfo=timezone.utc)

>>> # Before the PDT -> PST transition
>>> print(dt_utc.astimezone(LOS_ANGELES))
2020-11-01 01:00:00-07:00

>>> # After the PDT -> PST transition
>>> print((dt_utc + timedelta(hours=1)).astimezone(LOS_ANGELES))
2020-11-01 01:00:00-08:00

```

## Data sources[¶](https://docs.python.org/3/library/zoneinfo.html#data-sources "Link to this heading")
The `zoneinfo` module does not directly provide time zone data, and instead pulls time zone information from the system time zone database or the first-party PyPI package [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") will raise [`ZoneInfoNotFoundError`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfoNotFoundError "zoneinfo.ZoneInfoNotFoundError").
### Configuring the data sources[¶](https://docs.python.org/3/library/zoneinfo.html#configuring-the-data-sources "Link to this heading")
When `ZoneInfo(key)` is called, the constructor first searches the directories specified in [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") for a file matching `key`, and on failure looks for a match in the tzdata package. This behavior can be configured in three ways:
  1. The default [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") when not otherwise specified can be configured at [compile time](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-compile-time-config).
  2. [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") can be configured using [an environment variable](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-environment-var).
  3. At [runtime](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-runtime-config), the search path can be manipulated using the [`reset_tzpath()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "zoneinfo.reset_tzpath") function.


#### Compile-time configuration[¶](https://docs.python.org/3/library/zoneinfo.html#compile-time-configuration "Link to this heading")
The default [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") includes several common deployment locations for the time zone database (except on Windows, where there are no “well-known” locations for time zone data). On POSIX systems, downstream distributors and those building Python from source who know where their system time zone data is deployed may change the default time zone path by specifying the compile-time option `TZPATH` (or, more likely, the [`configure flag --with-tzpath`](https://docs.python.org/3/using/configure.html#cmdoption-with-tzpath)), which should be a string delimited by [`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep").
On all platforms, the configured value is available as the `TZPATH` key in [`sysconfig.get_config_var()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_var "sysconfig.get_config_var").
#### Environment configuration[¶](https://docs.python.org/3/library/zoneinfo.html#environment-configuration "Link to this heading")
When initializing [`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH") (either at import time or whenever [`reset_tzpath()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "zoneinfo.reset_tzpath") is called with no arguments), the `zoneinfo` module will use the environment variable `PYTHONTZPATH`, if it exists, to set the search path.

PYTHONTZPATH[¶](https://docs.python.org/3/library/zoneinfo.html#envvar-PYTHONTZPATH "Link to this definition")

This is an [`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep")-separated string containing the time zone search path to use. It must consist of only absolute rather than relative paths. Relative components specified in `PYTHONTZPATH` will not be used, but otherwise the behavior when a relative path is specified is implementation-defined; CPython will raise [`InvalidTZPathWarning`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.InvalidTZPathWarning "zoneinfo.InvalidTZPathWarning"), but other implementations are free to silently ignore the erroneous component or raise an exception.
To set the system to ignore the system data and use the tzdata package instead, set `PYTHONTZPATH=""`.
#### Runtime configuration[¶](https://docs.python.org/3/library/zoneinfo.html#runtime-configuration "Link to this heading")
The TZ search path can also be configured at runtime using the [`reset_tzpath()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "zoneinfo.reset_tzpath") function. This is generally not an advisable operation, though it is reasonable to use it in test functions that require the use of a specific time zone path (or require disabling access to the system time zones).
## The `ZoneInfo` class[¶](https://docs.python.org/3/library/zoneinfo.html#the-zoneinfo-class "Link to this heading")

_class_ zoneinfo.ZoneInfo(_key_)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "Link to this definition")

A concrete [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass that represents an IANA time zone specified by the string `key`. Calls to the primary constructor will always return objects that compare identically; put another way, barring cache invalidation via [`ZoneInfo.clear_cache()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.clear_cache "zoneinfo.ZoneInfo.clear_cache"), for all values of `key`, the following assertion will always be true:
Copy```
a = ZoneInfo(key)
b = ZoneInfo(key)
assert a is b

```

`key` must be in the form of a relative, normalized POSIX path, with no up-level references. The constructor will raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if a non-conforming key is passed.
If no file matching `key` is found, the constructor will raise [`ZoneInfoNotFoundError`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfoNotFoundError "zoneinfo.ZoneInfoNotFoundError").
The `ZoneInfo` class has two alternate constructors:

_classmethod_ ZoneInfo.from_file(_file_obj_ , _/_ , _key =None_)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.from_file "Link to this definition")

Constructs a `ZoneInfo` object from a file-like object returning bytes (e.g. a file opened in binary mode or an [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") object). Unlike the primary constructor, this always constructs a new object.
The `key` parameter sets the name of the zone for the purposes of [`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__") and [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__").
Objects created via this constructor cannot be pickled (see [pickling](https://docs.python.org/3/library/zoneinfo.html#pickling)).
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the data read from _file_obj_ is not a valid TZif file.

_classmethod_ ZoneInfo.no_cache(_key_)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.no_cache "Link to this definition")

An alternate constructor that bypasses the constructor’s cache. It is identical to the primary constructor, but returns a new object on each call. This is most likely to be useful for testing or demonstration purposes, but it can also be used to create a system with a different cache invalidation strategy.
Objects created via this constructor will also bypass the cache of a deserializing process when unpickled.
Caution
Using this constructor may change the semantics of your datetimes in surprising ways, only use it if you know that you need to.
The following class methods are also available:

_classmethod_ ZoneInfo.clear_cache(_*_ , _only_keys =None_)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.clear_cache "Link to this definition")

A method for invalidating the cache on the `ZoneInfo` class. If no arguments are passed, all caches are invalidated and the next call to the primary constructor for each key will return a new instance.
If an iterable of key names is passed to the `only_keys` parameter, only the specified keys will be removed from the cache. Keys passed to `only_keys` but not found in the cache are ignored.
Warning
Invoking this function may change the semantics of datetimes using `ZoneInfo` in surprising ways; this modifies module state and thus may have wide-ranging effects. Only use it if you know that you need to.
The class has one attribute:

ZoneInfo.key[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.key "Link to this definition")

This is a read-only [attribute](https://docs.python.org/3/glossary.html#term-attribute) that returns the value of `key` passed to the constructor, which should be a lookup key in the IANA time zone database (e.g. `America/New_York`, `Europe/Paris` or `Asia/Tokyo`).
For zones constructed from file without specifying a `key` parameter, this will be set to `None`.
Note
Although it is a somewhat common practice to expose these to end users, these values are designed to be primary keys for representing the relevant zones and not necessarily user-facing elements. Projects like CLDR (the Unicode Common Locale Data Repository) can be used to get more user-friendly strings from these keys.
### String representations[¶](https://docs.python.org/3/library/zoneinfo.html#string-representations "Link to this heading")
The string representation returned when calling [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") on a [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") object defaults to using the [`ZoneInfo.key`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.key "zoneinfo.ZoneInfo.key") attribute (see the note on usage in the attribute documentation):
Copy```
>>> zone = ZoneInfo("Pacific/Kwajalein")
>>> str(zone)
'Pacific/Kwajalein'

>>> dt = datetime(2020, 4, 1, 3, 15, tzinfo=zone)
>>> f"{dt.isoformat()} [{dt.tzinfo}]"
'2020-04-01T03:15:00+12:00 [Pacific/Kwajalein]'

```

For objects constructed from a file without specifying a `key` parameter, `str` falls back to calling [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr"). `ZoneInfo`’s `repr` is implementation-defined and not necessarily stable between versions, but it is guaranteed not to be a valid `ZoneInfo` key.
### Pickle serialization[¶](https://docs.python.org/3/library/zoneinfo.html#pickle-serialization "Link to this heading")
Rather than serializing all transition data, `ZoneInfo` objects are serialized by key, and `ZoneInfo` objects constructed from files (even those with a value for `key` specified) cannot be pickled.
The behavior of a `ZoneInfo` file depends on how it was constructed:
  1. `ZoneInfo(key)`: When constructed with the primary constructor, a `ZoneInfo` object is serialized by key, and when deserialized, the deserializing process uses the primary and thus it is expected that these are the same object as other references to the same time zone. For example, if `europe_berlin_pkl` is a string containing a pickle constructed from `ZoneInfo("Europe/Berlin")`, one would expect the following behavior:
Copy```
>>> a = ZoneInfo("Europe/Berlin")
>>> b = pickle.loads(europe_berlin_pkl)
>>> a is b
True

```

  2. `ZoneInfo.no_cache(key)`: When constructed from the cache-bypassing constructor, the `ZoneInfo` object is also serialized by key, but when deserialized, the deserializing process uses the cache bypassing constructor. If `europe_berlin_pkl_nc` is a string containing a pickle constructed from `ZoneInfo.no_cache("Europe/Berlin")`, one would expect the following behavior:
Copy```
>>> a = ZoneInfo("Europe/Berlin")
>>> b = pickle.loads(europe_berlin_pkl_nc)
>>> a is b
False

```

  3. `ZoneInfo.from_file(file_obj, /, key=None)`: When constructed from a file, the `ZoneInfo` object raises an exception on pickling. If an end user wants to pickle a `ZoneInfo` constructed from a file, it is recommended that they use a wrapper type or a custom serialization function: either serializing by key or storing the contents of the file object and serializing that.


This method of serialization requires that the time zone data for the required key be available on both the serializing and deserializing side, similar to the way that references to classes and functions are expected to exist in both the serializing and deserializing environments. It also means that no guarantees are made about the consistency of results when unpickling a `ZoneInfo` pickled in an environment with a different version of the time zone data.
## Functions[¶](https://docs.python.org/3/library/zoneinfo.html#functions "Link to this heading")

zoneinfo.available_timezones()[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.available_timezones "Link to this definition")

Get a set containing all the valid keys for IANA time zones available anywhere on the time zone path. This is recalculated on every call to the function.
This function only includes canonical zone names and does not include “special” zones such as those under the `posix/` and `right/` directories, or the `posixrules` zone.
Caution
This function may open a large number of files, as the best way to determine if a file on the time zone path is a valid time zone is to read the “magic string” at the beginning.
Note
These values are not designed to be exposed to end-users; for user facing elements, applications should use something like CLDR (the Unicode Common Locale Data Repository) to get more user-friendly strings. See also the cautionary note on [`ZoneInfo.key`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.key "zoneinfo.ZoneInfo.key").

zoneinfo.reset_tzpath(_to =None_)[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "Link to this definition")

Sets or resets the time zone search path ([`TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH")) for the module. When called with no arguments, `TZPATH` is set to the default value.
Calling `reset_tzpath` will not invalidate the [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") cache, and so calls to the primary `ZoneInfo` constructor will only use the new `TZPATH` in the case of a cache miss.
The `to` parameter must be a [sequence](https://docs.python.org/3/glossary.html#term-sequence) of strings or [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike") and not a string, all of which must be absolute paths. [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised if something other than an absolute path is passed.
## Globals[¶](https://docs.python.org/3/library/zoneinfo.html#globals "Link to this heading")

zoneinfo.TZPATH[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "Link to this definition")

A read-only sequence representing the time zone search path – when constructing a `ZoneInfo` from a key, the key is joined to each entry in the `TZPATH`, and the first file found is used.
`TZPATH` may contain only absolute paths, never relative paths, regardless of how it is configured.
The object that `zoneinfo.TZPATH` points to may change in response to a call to [`reset_tzpath()`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.reset_tzpath "zoneinfo.reset_tzpath"), so it is recommended to use `zoneinfo.TZPATH` rather than importing `TZPATH` from `zoneinfo` or assigning a long-lived variable to `zoneinfo.TZPATH`.
For more information on configuring the time zone search path, see [Configuring the data sources](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-configuration).
## Exceptions and warnings[¶](https://docs.python.org/3/library/zoneinfo.html#exceptions-and-warnings "Link to this heading")

_exception_ zoneinfo.ZoneInfoNotFoundError[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfoNotFoundError "Link to this definition")

Raised when construction of a [`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") object fails because the specified key could not be found on the system. This is a subclass of [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError").

_exception_ zoneinfo.InvalidTZPathWarning[¶](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.InvalidTZPathWarning "Link to this definition")

Raised when [`PYTHONTZPATH`](https://docs.python.org/3/library/zoneinfo.html#envvar-PYTHONTZPATH) contains an invalid component that will be filtered out, such as a relative path.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html)
    * [Using `ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#using-zoneinfo)
    * [Data sources](https://docs.python.org/3/library/zoneinfo.html#data-sources)
      * [Configuring the data sources](https://docs.python.org/3/library/zoneinfo.html#configuring-the-data-sources)
        * [Compile-time configuration](https://docs.python.org/3/library/zoneinfo.html#compile-time-configuration)
        * [Environment configuration](https://docs.python.org/3/library/zoneinfo.html#environment-configuration)
        * [Runtime configuration](https://docs.python.org/3/library/zoneinfo.html#runtime-configuration)
    * [The `ZoneInfo` class](https://docs.python.org/3/library/zoneinfo.html#the-zoneinfo-class)
      * [String representations](https://docs.python.org/3/library/zoneinfo.html#string-representations)
      * [Pickle serialization](https://docs.python.org/3/library/zoneinfo.html#pickle-serialization)
    * [Functions](https://docs.python.org/3/library/zoneinfo.html#functions)
    * [Globals](https://docs.python.org/3/library/zoneinfo.html#globals)
    * [Exceptions and warnings](https://docs.python.org/3/library/zoneinfo.html#exceptions-and-warnings)


#### Previous topic
[`datetime` — Basic date and time types](https://docs.python.org/3/library/datetime.html "previous chapter")
#### Next topic
[`calendar` — General calendar-related functions](https://docs.python.org/3/library/calendar.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=zoneinfo+%E2%80%94+IANA+time+zone+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzoneinfo.html&pagesource=library%2Fzoneinfo.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/calendar.html "calendar — General calendar-related functions") |
  * [previous](https://docs.python.org/3/library/datetime.html "datetime — Basic date and time types") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)
