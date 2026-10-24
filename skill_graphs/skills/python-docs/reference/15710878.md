
Return [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object with same year, month and day.

datetime.time()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.time "Link to this definition")

Return [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object with same hour, minute, second, microsecond and fold. [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") is `None`. See also method [`timetz()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetz "datetime.datetime.timetz").
Changed in version 3.6: The fold value is copied to the returned [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object.

datetime.timetz()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetz "Link to this definition")

Return [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object with same hour, minute, second, microsecond, fold, and tzinfo attributes. See also method [`time()`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.").
Changed in version 3.6: The fold value is copied to the returned [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object.

datetime.replace(_year =self.year_, _month =self.month_, _day =self.day_, _hour =self.hour_, _minute =self.minute_, _second =self.second_, _microsecond =self.microsecond_, _tzinfo =self.tzinfo_, _*_ , _fold =0_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.replace "Link to this definition")

Return a new [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.") object with the same attributes, but with specified parameters updated. Note that `tzinfo=None` can be specified to create a naive datetime from an aware datetime with no conversion of date and time data.
[`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects are also supported by generic function [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace").
Changed in version 3.6: Added the _fold_ parameter.

datetime.astimezone(_tz =None_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "Link to this definition")

Return a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object with new [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attribute _tz_ , adjusting the date and time data so the result is the same UTC time as _self_ , but in _tz_ ’s local time.
If provided, _tz_ must be an instance of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass, and its [`utcoffset()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcoffset "datetime.datetime.utcoffset") and [`dst()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.dst "datetime.datetime.dst") methods must not return `None`. If _self_ is naive, it is presumed to represent time in the system time zone.
If called without arguments (or with `tz=None`) the system local time zone is assumed for the target time zone. The `.tzinfo` attribute of the converted datetime instance will be set to an instance of [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") with the zone name and offset obtained from the OS.
If `self.tzinfo` is _tz_ , `self.astimezone(tz)` is equal to _self_ : no adjustment of date or time data is performed. Else the result is local time in the time zone _tz_ , representing the same UTC time as _self_ : after `astz = dt.astimezone(tz)`, `astz - astz.utcoffset()` will have the same date and time data as `dt - dt.utcoffset()`.
If you merely want to attach a [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") object _tz_ to a datetime _dt_ without adjustment of date and time data, use `dt.replace(tzinfo=tz)`. If you merely want to remove the `timezone` object from an aware datetime _dt_ without conversion of date and time data, use `dt.replace(tzinfo=None)`.
Note that the default [`tzinfo.fromutc()`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.fromutc "datetime.tzinfo.fromutc") method can be overridden in a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass to affect the result returned by `astimezone()`. Ignoring error cases, `astimezone()` acts like:
Copy```
def astimezone(self, tz):
    if self.tzinfo is tz:
        return self
    # Convert self to UTC, and attach the new timezone object.
    utc = (self - self.utcoffset()).replace(tzinfo=tz)
    # Convert from UTC to tz's local time.
    return tz.fromutc(utc)

```

Changed in version 3.3: _tz_ now can be omitted.
Changed in version 3.6: The `astimezone()` method can now be called on naive instances that are presumed to represent system local time.

datetime.utcoffset()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcoffset "Link to this definition")

If [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") is `None`, returns `None`, else returns `self.tzinfo.utcoffset(self)`, and raises an exception if the latter doesn’t return `None` or a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object with magnitude less than one day.
Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.

datetime.dst()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.dst "Link to this definition")

If [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") is `None`, returns `None`, else returns `self.tzinfo.dst(self)`, and raises an exception if the latter doesn’t return `None` or a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object with magnitude less than one day.
Changed in version 3.7: The DST offset is not restricted to a whole number of minutes.

datetime.tzname()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzname "Link to this definition")

If [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") is `None`, returns `None`, else returns `self.tzinfo.tzname(self)`, raises an exception if the latter doesn’t return `None` or a string object,

datetime.timetuple()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetuple "Link to this definition")

Return a [`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time") such as returned by [`time.localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime").
`d.timetuple()` is equivalent to:
Copy```
time.struct_time((d.year, d.month, d.day,
                  d.hour, d.minute, d.second,
                  d.weekday(), yday, dst))

```

where `yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1` is the day number within the current year starting with 1 for January 1st. The [`tm_isdst`](https://docs.python.org/3/library/time.html#time.struct_time.tm_isdst "time.struct_time.tm_isdst") flag of the result is set according to the [`dst()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.dst "datetime.datetime.dst") method: [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") is `None` or `dst()` returns `None`, `tm_isdst` is set to `-1`; else if `dst()` returns a non-zero value, `tm_isdst` is set to 1; else `tm_isdst` is set to 0.

datetime.utctimetuple()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.utctimetuple "Link to this definition")

If [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance `d` is naive, this is the same as `d.timetuple()` except that [`tm_isdst`](https://docs.python.org/3/library/time.html#time.struct_time.tm_isdst "time.struct_time.tm_isdst") is forced to 0 regardless of what `d.dst()` returns. DST is never in effect for a UTC time.
If `d` is aware, `d` is normalized to UTC time, by subtracting `d.utcoffset()`, and a [`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time") for the normalized time is returned. `tm_isdst` is forced to 0. Note that an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") may be raised if `d.year` was `MINYEAR` or `MAXYEAR` and UTC adjustment spills over a year boundary.
Warning
Because naive `datetime` objects are treated by many `datetime` methods as local times, it is preferred to use aware datetimes to represent times in UTC; as a result, using `datetime.utctimetuple()` may give misleading results. If you have a naive `datetime` representing UTC, use `datetime.replace(tzinfo=timezone.utc)` to make it aware, at which point you can use [`datetime.timetuple()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetuple "datetime.datetime.timetuple").

datetime.toordinal()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.toordinal "Link to this definition")

Return the proleptic Gregorian ordinal of the date. The same as `self.date().toordinal()`.

datetime.timestamp()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp "Link to this definition")

Return POSIX timestamp corresponding to the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance. The return value is a [`float`](https://docs.python.org/3/library/functions.html#float "float") similar to that returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time").
Naive [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instances are assumed to represent local time and this method relies on the platform C `mktime()` function to perform the conversion. Since `datetime` supports wider range of values than `mktime()` on many platforms, this method may raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") or [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") for times far in the past or far in the future.
For aware [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instances, the return value is computed as:
Copy```
(dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()

```

Note
There is no method to obtain the POSIX timestamp directly from a naive [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance representing UTC time. If your application uses this convention and your system time zone is not set to UTC, you can obtain the POSIX timestamp by supplying `tzinfo=timezone.utc`:
Copy```
timestamp = dt.replace(tzinfo=timezone.utc).timestamp()

```

or by calculating the timestamp directly:
Copy```
timestamp = (dt - datetime(1970, 1, 1)) / timedelta(seconds=1)

```

Added in version 3.3.
Changed in version 3.6: The `timestamp()` method uses the [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") attribute to disambiguate the times during a repeated interval.

datetime.weekday()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday "Link to this definition")

Return the day of the week as an integer, where Monday is 0 and Sunday is 6. The same as `self.date().weekday()`. See also [`isoweekday()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoweekday "datetime.datetime.isoweekday").

datetime.isoweekday()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoweekday "Link to this definition")

Return the day of the week as an integer, where Monday is 1 and Sunday is 7. The same as `self.date().isoweekday()`. See also [`weekday()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday "datetime.datetime.weekday"), [`isocalendar()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isocalendar "datetime.datetime.isocalendar").

datetime.isocalendar()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.isocalendar "Link to this definition")

Return a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) with three components: `year`, `week` and `weekday`. The same as `self.date().isocalendar()`.

datetime.isoformat(_sep ='T'_, _timespec ='auto'_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat "Link to this definition")

Return a string representing the date and time in ISO 8601 format:
  * `YYYY-MM-DDTHH:MM:SS.ffffff`, if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond "datetime.datetime.microsecond") is not 0
  * `YYYY-MM-DDTHH:MM:SS`, if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond "datetime.datetime.microsecond") is 0


If [`utcoffset()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcoffset "datetime.datetime.utcoffset") does not return `None`, a string is appended, giving the UTC offset:
  * `YYYY-MM-DDTHH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]`, if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond "datetime.datetime.microsecond") is not 0
  * `YYYY-MM-DDTHH:MM:SS+HH:MM[:SS[.ffffff]]`, if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond "datetime.datetime.microsecond") is 0


Examples:
Copy```
>>> import datetime as dt
>>> dt.datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat()
'2019-05-18T15:17:08.132263'
>>> dt.datetime(2019, 5, 18, 15, 17, tzinfo=dt.timezone.utc).isoformat()
'2019-05-18T15:17:00+00:00'

```

The optional argument _sep_ (default `'T'`) is a one-character separator, placed between the date and time portions of the result. For example:
Copy```
>>> import datetime as dt
>>> class TZ(dt.tzinfo):
...     """A time zone with an arbitrary, constant -06:39 offset."""
...     def utcoffset(self, when):
...         return dt.timedelta(hours=-6, minutes=-39)
...
>>> dt.datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
'2002-12-25 00:00:00-06:39'
>>> dt.datetime(2009, 11, 27, microsecond=100, tzinfo=TZ()).isoformat()
'2009-11-27T00:00:00.000100-06:39'

```

The optional argument _timespec_ specifies the number of additional components of the time to include (the default is `'auto'`). It can be one of the following:
  * `'auto'`: Same as `'seconds'` if [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond "datetime.datetime.microsecond") is 0, same as `'microseconds'` otherwise.
  * `'hours'`: Include the [`hour`](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour "datetime.datetime.hour") in the two-digit `HH` format.
  * `'minutes'`: Include [`hour`](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour "datetime.datetime.hour") and [`minute`](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute "datetime.datetime.minute") in `HH:MM` format.
  * `'seconds'`: Include [`hour`](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour "datetime.datetime.hour"), [`minute`](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute "datetime.datetime.minute"), and [`second`](https://docs.python.org/3/library/datetime.html#datetime.datetime.second "datetime.datetime.second") in `HH:MM:SS` format.
  * `'milliseconds'`: Include full time, but truncate fractional second part to milliseconds. `HH:MM:SS.sss` format.
  * `'microseconds'`: Include full time in `HH:MM:SS.ffffff` format.


Note
Excluded time components are truncated, not rounded.
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised on an invalid _timespec_ argument:
Copy```
>>> import datetime as dt
>>> dt.datetime.now().isoformat(timespec='minutes')
'2002-12-25T00:00'
>>> my_datetime = dt.datetime(2015, 1, 1, 12, 30, 59, 0)
>>> my_datetime.isoformat(timespec='microseconds')
'2015-01-01T12:30:59.000000'

```

Changed in version 3.6: Added the _timespec_ parameter.

datetime.__str__()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.__str__ "Link to this definition")

For a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance `d`, `str(d)` is equivalent to `d.isoformat(' ')`.

datetime.ctime()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.ctime "Link to this definition")

Return a string representing the date and time:
Copy```
>>> import datetime as dt
>>> dt.datetime(2002, 12, 4, 20, 30, 40).ctime()
'Wed Dec  4 20:30:40 2002'

```

The output string will _not_ include time zone information, regardless of whether the input is aware or naive.
`d.ctime()` is equivalent to:
Copy```
time.ctime(time.mktime(d.timetuple()))

```

on platforms where the native C `ctime()` function (which [`time.ctime()`](https://docs.python.org/3/library/time.html#time.ctime "time.ctime") invokes, but which `datetime.ctime()` does not invoke) conforms to the C standard.

datetime.strftime(_format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "Link to this definition")

Return a string representing the date and time, controlled by an explicit format string. See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`datetime.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat "datetime.datetime.isoformat").

datetime.__format__(_format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.__format__ "Link to this definition")

Same as [`datetime.strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime"). This makes it possible to specify a format string for a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object in [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) and when using [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format"). See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`datetime.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat "datetime.datetime.isoformat").
### Examples of usage: `datetime`[¶](https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime "Link to this heading")
Examples of working with [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects:
Copy```
>>> import datetime as dt

>>> # Using datetime.combine()
>>> d = dt.date(2005, 7, 14)
>>> t = dt.time(12, 30)
>>> dt.datetime.combine(d, t)
datetime.datetime(2005, 7, 14, 12, 30)

>>> # Using datetime.now()
>>> dt.datetime.now()
datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
>>> dt.datetime.now(dt.timezone.utc)
datetime.datetime(2007, 12, 6, 15, 29, 43, 79060, tzinfo=datetime.timezone.utc)

>>> # Using datetime.strptime()
>>> my_datetime = dt.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
>>> my_datetime
datetime.datetime(2006, 11, 21, 16, 30)

>>> # Using datetime.timetuple() to get tuple of all attributes
>>> tt = my_datetime.timetuple()
>>> for it in tt:
...     print(it)
...
2006    # year
11      # month
21      # day
16      # hour
30      # minute
0       # second
1       # weekday (0 = Monday)
325     # number of days since 1st January
-1      # dst - method tzinfo.dst() returned None

>>> # Date in ISO format
>>> ic = my_datetime.isocalendar()
>>> for it in ic:
...     print(it)
...
2006    # ISO year
47      # ISO week
2       # ISO weekday

>>> # Formatting a datetime
>>> my_datetime.strftime("%A, %d. %B %Y %I:%M%p")
'Tuesday, 21. November 2006 04:30PM'
>>> 'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(my_datetime, "day", "month", "time")
'The day is 21, the month is November, the time is 04:30PM.'

```

The example below defines a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass capturing time zone information for Kabul, Afghanistan, which used +4 UTC until 1945 and then +4:30 UTC thereafter:
Copy```
import datetime as dt

class KabulTz(dt.tzinfo):
    # Kabul used +4 until 1945, when they moved to +4:30
    UTC_MOVE_DATE = dt.datetime(1944, 12, 31, 20, tzinfo=dt.timezone.utc)

    def utcoffset(self, when):
        if when.year < 1945:
            return dt.timedelta(hours=4)
        elif (1945, 1, 1, 0, 0) <= when.timetuple()[:5] < (1945, 1, 1, 0, 30):
            # An ambiguous ("imaginary") half-hour range representing
            # a 'fold' in time due to the shift from +4 to +4:30.
            # If when falls in the imaginary range, use fold to decide how
            # to resolve. See PEP 495.
            return dt.timedelta(hours=4, minutes=(30 if when.fold else 0))
        else:
            return dt.timedelta(hours=4, minutes=30)

    def fromutc(self, when):
        # Follow same validations as in datetime.tzinfo
        if not isinstance(when, dt.datetime):
            raise TypeError("fromutc() requires a datetime argument")
        if when.tzinfo is not self:
            raise ValueError("when.tzinfo is not self")

        # A custom implementation is required for fromutc as
        # the input to this function is a datetime with utc values
        # but with a tzinfo set to self.
        # See datetime.astimezone or fromtimestamp.
        if when.replace(tzinfo=dt.timezone.utc) >= self.UTC_MOVE_DATE:
            return when + dt.timedelta(hours=4, minutes=30)
        else:
            return when + dt.timedelta(hours=4)

    def dst(self, when):
        # Kabul does not observe daylight saving time.
        return dt.timedelta(0)

    def tzname(self, when):
        if when >= self.UTC_MOVE_DATE:
            return "+04:30"
        return "+04"

```

Usage of `KabulTz` from above:
Copy```
>>> tz1 = KabulTz()

>>> # Datetime before the change
>>> dt1 = dt.datetime(1900, 11, 21, 16, 30, tzinfo=tz1)
>>> print(dt1.utcoffset())
4:00:00

>>> # Datetime after the change
>>> dt2 = dt.datetime(2006, 6, 14, 13, 0, tzinfo=tz1)
>>> print(dt2.utcoffset())
4:30:00

>>> # Convert datetime to another time zone
>>> dt3 = dt2.astimezone(dt.timezone.utc)
>>> dt3
datetime.datetime(2006, 6, 14, 8, 30, tzinfo=datetime.timezone.utc)
>>> dt2
datetime.datetime(2006, 6, 14, 13, 0, tzinfo=KabulTz())
>>> dt2 == dt3
True

```

##  `time` objects[¶](https://docs.python.org/3/library/datetime.html#time-objects "Link to this heading")
A [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object represents a (local) time of day, independent of any particular day, and subject to adjustment via a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") object.

_class_ datetime.time(_hour =0_, _minute =0_, _second =0_, _microsecond =0_, _tzinfo =None_, _*_ , _fold =0_)[¶](https://docs.python.org/3/library/datetime.html#datetime.time "Link to this definition")

All arguments are optional. _tzinfo_ may be `None`, or an instance of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass. The remaining arguments must be integers in the following ranges:
  * `0 <= hour < 24`,
  * `0 <= minute < 60`,
  * `0 <= second < 60`,
  * `0 <= microsecond < 1000000`,
  * `fold in [0, 1]`.


If an argument outside those ranges is given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. All default to 0 except _tzinfo_ , which defaults to `None`.
Class attributes:

time.min[¶](https://docs.python.org/3/library/datetime.html#datetime.time.min "Link to this definition")

The earliest representable [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time"), `time(0, 0, 0, 0)`.

time.max[¶](https://docs.python.org/3/library/datetime.html#datetime.time.max "Link to this definition")

The latest representable [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time"), `time(23, 59, 59, 999999)`.

time.resolution[¶](https://docs.python.org/3/library/datetime.html#datetime.time.resolution "Link to this definition")

The smallest possible difference between non-equal [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects, `timedelta(microseconds=1)`, although note that arithmetic on `time` objects is not supported.
