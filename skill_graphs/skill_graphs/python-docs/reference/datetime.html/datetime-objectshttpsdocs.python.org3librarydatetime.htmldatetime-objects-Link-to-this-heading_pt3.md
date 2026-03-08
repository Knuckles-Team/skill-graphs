Instance attributes (read-only):

time.hour[¶](https://docs.python.org/3/library/datetime.html#datetime.time.hour "Link to this definition")

In `range(24)`.

time.minute[¶](https://docs.python.org/3/library/datetime.html#datetime.time.minute "Link to this definition")

In `range(60)`.

time.second[¶](https://docs.python.org/3/library/datetime.html#datetime.time.second "Link to this definition")

In `range(60)`.

time.microsecond[¶](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond "Link to this definition")

In `range(1000000)`.

time.tzinfo[¶](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "Link to this definition")

The object passed as the tzinfo argument to the [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") constructor, or `None` if none was passed.

time.fold[¶](https://docs.python.org/3/library/datetime.html#datetime.time.fold "Link to this definition")

In `[0, 1]`. Used to disambiguate wall times during a repeated interval. (A repeated interval occurs when clocks are rolled back at the end of daylight saving time or when the UTC offset for the current zone is decreased for political reasons.) The values 0 and 1 represent, respectively, the earlier and later of the two moments with the same wall time representation.
Added in version 3.6.
[`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects support equality and order comparisons, where `a` is considered less than `b` when `a` precedes `b` in time.
Naive and aware `time` objects are never equal. Order comparison between naive and aware `time` objects raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
If both comparands are aware, and have the same [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "datetime.time.tzinfo") attribute, the `tzinfo` and `fold` attributes are ignored and the base times are compared. If both comparands are aware and have different `tzinfo` attributes, the comparands are first adjusted by subtracting their UTC offsets (obtained from `self.utcoffset()`).
Changed in version 3.3: Equality comparisons between aware and naive [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") instances don’t raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
In Boolean contexts, a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object is always considered to be true.
Changed in version 3.5: Before Python 3.5, a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object was considered to be false if it represented midnight in UTC. This behavior was considered obscure and error-prone and has been removed in Python 3.5. See [bpo-13936](https://bugs.python.org/issue?@action=redirect&bpo=13936) for more information.
Other constructors:

_classmethod_ time.fromisoformat(_time_string_)[¶](https://docs.python.org/3/library/datetime.html#datetime.time.fromisoformat "Link to this definition")

Return a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") corresponding to a _time_string_ in any valid ISO 8601 format, with the following exceptions:
  1. Time zone offsets may have fractional seconds.
  2. The leading `T`, normally required in cases where there may be ambiguity between a date and a time, is not required.
  3. Fractional seconds may have any number of digits (anything beyond 6 will be truncated).
  4. Fractional hours and minutes are not supported.


Examples:
Copy```
>>> import datetime as dt
>>> dt.time.fromisoformat('04:23:01')
datetime.time(4, 23, 1)
>>> dt.time.fromisoformat('T04:23:01')
datetime.time(4, 23, 1)
>>> dt.time.fromisoformat('T042301')
datetime.time(4, 23, 1)
>>> dt.time.fromisoformat('04:23:01.000384')
datetime.time(4, 23, 1, 384)
>>> dt.time.fromisoformat('04:23:01,000384')
datetime.time(4, 23, 1, 384)
>>> dt.time.fromisoformat('04:23:01+04:00')
datetime.time(4, 23, 1, tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))
>>> dt.time.fromisoformat('04:23:01Z')
datetime.time(4, 23, 1, tzinfo=datetime.timezone.utc)
>>> dt.time.fromisoformat('04:23:01+00:00')
datetime.time(4, 23, 1, tzinfo=datetime.timezone.utc)

```

Added in version 3.7.
Changed in version 3.11: Previously, this method only supported formats that could be emitted by [`time.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.time.isoformat "datetime.time.isoformat").

_classmethod_ time.strptime(_date_string_ , _format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.time.strptime "Link to this definition")

Return a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") corresponding to _date_string_ , parsed according to _format_.
If _format_ does not contain microseconds or timezone information, this is equivalent to:
Copy```
time(*(time.strptime(date_string, format)[3:6]))

```

[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the _date_string_ and _format_ cannot be parsed by [`time.strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime") or if it returns a value which is not a time tuple. See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`time.fromisoformat()`](https://docs.python.org/3/library/datetime.html#datetime.time.fromisoformat "datetime.time.fromisoformat").
Added in version 3.14.
Instance methods:

time.replace(_hour =self.hour_, _minute =self.minute_, _second =self.second_, _microsecond =self.microsecond_, _tzinfo =self.tzinfo_, _*_ , _fold =0_)[¶](https://docs.python.org/3/library/datetime.html#datetime.time.replace "Link to this definition")

Return a new [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") with the same values, but with specified parameters updated. Note that `tzinfo=None` can be specified to create a naive `time` from an aware `time`, without conversion of the time data.
[`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects are also supported by generic function [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace").
Changed in version 3.6: Added the _fold_ parameter.

time.isoformat(_timespec ='auto'_)[¶](https://docs.python.org/3/library/datetime.html#datetime.time.isoformat "Link to this definition")

Return a string representing the time in ISO 8601 format, one of:
  * `HH:MM:SS.ffffff`, if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond "datetime.time.microsecond") is not 0
  * `HH:MM:SS`, if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond "datetime.time.microsecond") is 0
  * `HH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]`, if [`utcoffset()`](https://docs.python.org/3/library/datetime.html#datetime.time.utcoffset "datetime.time.utcoffset") does not return `None`
  * `HH:MM:SS+HH:MM[:SS[.ffffff]]`, if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond "datetime.time.microsecond") is 0 and [`utcoffset()`](https://docs.python.org/3/library/datetime.html#datetime.time.utcoffset "datetime.time.utcoffset") does not return `None`


The optional argument _timespec_ specifies the number of additional components of the time to include (the default is `'auto'`). It can be one of the following:
  * `'auto'`: Same as `'seconds'` if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond "datetime.time.microsecond") is 0, same as `'microseconds'` otherwise.
  * `'hours'`: Include the [`hour`](https://docs.python.org/3/library/datetime.html#datetime.time.hour "datetime.time.hour") in the two-digit `HH` format.
  * `'minutes'`: Include [`hour`](https://docs.python.org/3/library/datetime.html#datetime.time.hour "datetime.time.hour") and [`minute`](https://docs.python.org/3/library/datetime.html#datetime.time.minute "datetime.time.minute") in `HH:MM` format.
  * `'seconds'`: Include [`hour`](https://docs.python.org/3/library/datetime.html#datetime.time.hour "datetime.time.hour"), [`minute`](https://docs.python.org/3/library/datetime.html#datetime.time.minute "datetime.time.minute"), and [`second`](https://docs.python.org/3/library/datetime.html#datetime.time.second "datetime.time.second") in `HH:MM:SS` format.
  * `'milliseconds'`: Include full time, but truncate fractional second part to milliseconds. `HH:MM:SS.sss` format.
  * `'microseconds'`: Include full time in `HH:MM:SS.ffffff` format.


Note
Excluded time components are truncated, not rounded.
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised on an invalid _timespec_ argument.
Example:
Copy```
>>> import datetime as dt
>>> dt.time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')
'12:34'
>>> my_time = dt.time(hour=12, minute=34, second=56, microsecond=0)
>>> my_time.isoformat(timespec='microseconds')
'12:34:56.000000'
>>> my_time.isoformat(timespec='auto')
'12:34:56'

```

Changed in version 3.6: Added the _timespec_ parameter.

time.__str__()[¶](https://docs.python.org/3/library/datetime.html#datetime.time.__str__ "Link to this definition")

For a time `t`, `str(t)` is equivalent to `t.isoformat()`.

time.strftime(_format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.time.strftime "Link to this definition")

Return a string representing the time, controlled by an explicit format string. See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`time.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.time.isoformat "datetime.time.isoformat").

time.__format__(_format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.time.__format__ "Link to this definition")

Same as [`time.strftime()`](https://docs.python.org/3/library/datetime.html#datetime.time.strftime "datetime.time.strftime"). This makes it possible to specify a format string for a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object in [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) and when using [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format"). See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`time.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.time.isoformat "datetime.time.isoformat").

time.utcoffset()[¶](https://docs.python.org/3/library/datetime.html#datetime.time.utcoffset "Link to this definition")

If [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "datetime.time.tzinfo") is `None`, returns `None`, else returns `self.tzinfo.utcoffset(None)`, and raises an exception if the latter doesn’t return `None` or a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object with magnitude less than one day.
Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.

time.dst()[¶](https://docs.python.org/3/library/datetime.html#datetime.time.dst "Link to this definition")

If [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "datetime.time.tzinfo") is `None`, returns `None`, else returns `self.tzinfo.dst(None)`, and raises an exception if the latter doesn’t return `None`, or a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object with magnitude less than one day.
Changed in version 3.7: The DST offset is not restricted to a whole number of minutes.

time.tzname()[¶](https://docs.python.org/3/library/datetime.html#datetime.time.tzname "Link to this definition")

If [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "datetime.time.tzinfo") is `None`, returns `None`, else returns `self.tzinfo.tzname(None)`, or raises an exception if the latter doesn’t return `None` or a string object.
### Examples of usage: `time`[¶](https://docs.python.org/3/library/datetime.html#examples-of-usage-time "Link to this heading")
Examples of working with a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object:
Copy```
>>> import datetime as dt
>>> class TZ1(dt.tzinfo):
...     def utcoffset(self, when):
...         return dt.timedelta(hours=1)
...     def dst(self, when):
...         return dt.timedelta(0)
...     def tzname(self, when):
...         return "+01:00"
...     def  __repr__(self):
...         return f"{self.__class__.__name__}()"
...
>>> t = dt.time(12, 10, 30, tzinfo=TZ1())
>>> t
datetime.time(12, 10, 30, tzinfo=TZ1())
>>> t.isoformat()
'12:10:30+01:00'
>>> t.dst()
datetime.timedelta(0)
>>> t.tzname()
'+01:00'
>>> t.strftime("%H:%M:%S %Z")
'12:10:30 +01:00'
>>> 'The {} is {:%H:%M}.'.format("time", t)
'The time is 12:10.'

```

##  `tzinfo` objects[¶](https://docs.python.org/3/library/datetime.html#tzinfo-objects "Link to this heading")

_class_ datetime.tzinfo[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "Link to this definition")

This is an [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class), meaning that this class should not be instantiated directly. Define a subclass of `tzinfo` to capture information about a particular time zone.
An instance of (a concrete subclass of) `tzinfo` can be passed to the constructors for [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects. The latter objects view their attributes as being in local time, and the `tzinfo` object supports methods revealing offset of local time from UTC, the name of the time zone, and DST offset, all relative to a date or time object passed to them.
You need to derive a concrete subclass, and (at least) supply implementations of the standard `tzinfo` methods needed by the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") methods you use. The `datetime` module provides [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone"), a simple concrete subclass of `tzinfo` which can represent time zones with fixed offset from UTC such as UTC itself or North American EST and EDT.
Special requirement for pickling: A `tzinfo` subclass must have an [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__") method that can be called with no arguments, otherwise it can be pickled but possibly not unpickled again. This is a technical requirement that may be relaxed in the future.
A concrete subclass of `tzinfo` may need to implement the following methods. Exactly which methods are needed depends on the uses made of aware `datetime` objects. If in doubt, simply implement all of them.

tzinfo.utcoffset(_dt_)[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.utcoffset "Link to this definition")

Return offset of local time from UTC, as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object that is positive east of UTC. If local time is west of UTC, this should be negative.
This represents the _total_ offset from UTC; for example, if a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") object represents both time zone and DST adjustments, `utcoffset()` should return their sum. If the UTC offset isn’t known, return `None`. Else the value returned must be a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object strictly between `-timedelta(hours=24)` and `timedelta(hours=24)` (the magnitude of the offset must be less than one day). Most implementations of `utcoffset()` will probably look like one of these two:
Copy```
return CONSTANT                 # fixed-offset class
return CONSTANT + self.dst(dt)  # daylight-aware class

```

If `utcoffset()` does not return `None`, [`dst()`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.dst "datetime.tzinfo.dst") should not return `None` either.
The default implementation of `utcoffset()` raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").
Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.

tzinfo.dst(_dt_)[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.dst "Link to this definition")

Return the daylight saving time (DST) adjustment, as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object or `None` if DST information isn’t known.
Return `timedelta(0)` if DST is not in effect. If DST is in effect, return the offset as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object (see [`utcoffset()`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.utcoffset "datetime.tzinfo.utcoffset") for details). Note that DST offset, if applicable, has already been added to the UTC offset returned by `utcoffset()`, so there’s no need to consult `dst()` unless you’re interested in obtaining DST info separately. For example, [`datetime.timetuple()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetuple "datetime.datetime.timetuple") calls its [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attribute’s `dst()` method to determine how the [`tm_isdst`](https://docs.python.org/3/library/time.html#time.struct_time.tm_isdst "time.struct_time.tm_isdst") flag should be set, and [`tzinfo.fromutc()`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.fromutc "datetime.tzinfo.fromutc") calls `dst()` to account for DST changes when crossing time zones.
An instance _tz_ of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass that models both standard and daylight times must be consistent in this sense:
`tz.utcoffset(dt) - tz.dst(dt)`
must return the same result for every [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") _dt_ with `dt.tzinfo == tz`. For sane [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclasses, this expression yields the time zone’s “standard offset”, which should not depend on the date or the time, but only on geographic location. The implementation of [`datetime.astimezone()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "datetime.datetime.astimezone") relies on this, but cannot detect violations; it’s the programmer’s responsibility to ensure it. If a `tzinfo` subclass cannot guarantee this, it may be able to override the default implementation of [`tzinfo.fromutc()`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.fromutc "datetime.tzinfo.fromutc") to work correctly with `astimezone()` regardless.
Most implementations of `dst()` will probably look like one of these two:
Copy```
import datetime as dt

def dst(self, when):
    # a fixed-offset class:  doesn't account for DST
    return dt.timedelta(0)

```

or:
Copy```
import datetime as dt

def dst(self, when):
    # Code to set dston and dstoff to the time zone's DST
    # transition times based on the input when.year, and expressed
    # in standard local time.

    if dston <= when.replace(tzinfo=None) < dstoff:
        return dt.timedelta(hours=1)
    else:
        return dt.timedelta(0)

```

The default implementation of `dst()` raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").
Changed in version 3.7: The DST offset is not restricted to a whole number of minutes.

tzinfo.tzname(_dt_)[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.tzname "Link to this definition")

Return the time zone name corresponding to the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object _dt_ , as a string. Nothing about string names is defined by the `datetime` module, and there’s no requirement that it mean anything in particular. For example, `"GMT"`, `"UTC"`, `"-500"`, `"-5:00"`, `"EDT"`, `"US/Eastern"`, `"America/New York"` are all valid replies. Return `None` if a string name isn’t known. Note that this is a method rather than a fixed string primarily because some [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclasses will wish to return different names depending on the specific value of _dt_ passed, especially if the `tzinfo` class is accounting for daylight time.
The default implementation of `tzname()` raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").
These methods are called by a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") or [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object, in response to their methods of the same names. A `datetime` object passes itself as the argument, and a `time` object passes `None` as the argument. A [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass’s methods should therefore be prepared to accept a _dt_ argument of `None`, or of class `datetime`.
When `None` is passed, it’s up to the class designer to decide the best response. For example, returning `None` is appropriate if the class wishes to say that time objects don’t participate in the [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") protocols. It may be more useful for `utcoffset(None)` to return the standard UTC offset, as there is no other convention for discovering the standard offset.
When a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object is passed in response to a `datetime` method, `dt.tzinfo` is the same object as _self_. [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") methods can rely on this, unless user code calls `tzinfo` methods directly. The intent is that the `tzinfo` methods interpret _dt_ as being in local time, and not need worry about objects in other time zones.
There is one more [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") method that a subclass may wish to override:

tzinfo.fromutc(_dt_)[¶](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.fromutc "Link to this definition")

This is called from the default [`datetime.astimezone()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "datetime.datetime.astimezone") implementation. When called from that, `dt.tzinfo` is _self_ , and _dt_ ’s date and time data are to be viewed as expressing a UTC time. The purpose of `fromutc()` is to adjust the date and time data, returning an equivalent datetime in _self_ ’s local time.
Most [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclasses should be able to inherit the default `fromutc()` implementation without problems. It’s strong enough to handle fixed-offset time zones, and time zones accounting for both standard and daylight time, and the latter even if the DST transition times differ in different years. An example of a time zone the default `fromutc()` implementation may not handle correctly in all cases is one where the standard offset (from UTC) depends on the specific date and time passed, which can happen for political reasons. The default implementations of [`astimezone()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "datetime.datetime.astimezone") and `fromutc()` may not produce the result you want if the result is one of the hours straddling the moment the standard offset changes.
Skipping code for error cases, the default `fromutc()` implementation acts like:
Copy```
import datetime as dt

def fromutc(self, when):
    # raise ValueError error if when.tzinfo is not self
    dtoff = when.utcoffset()
    dtdst = when.dst()
    # raise ValueError if dtoff is None or dtdst is None
    delta = dtoff - dtdst  # this is self's standard offset
    if delta:
        when += delta   # convert to standard local time
        dtdst = when.dst()
        # raise ValueError if dtdst is None
    if dtdst:
        return when + dtdst
    else:
        return when

```

In the following [`tzinfo_examples.py`](https://docs.python.org/3/_downloads/6dc1f3f4f0e6ca13cb42ddf4d6cbc8af/tzinfo_examples.py) file there are some examples of [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") classes:
