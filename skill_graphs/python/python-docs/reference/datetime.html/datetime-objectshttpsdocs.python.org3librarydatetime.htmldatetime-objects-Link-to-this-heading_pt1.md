##  `datetime` objects[¶](https://docs.python.org/3/library/datetime.html#datetime-objects "Link to this heading")
A [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object is a single object containing all the information from a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object and a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object.
Like a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object, [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") assumes the current Gregorian calendar extended in both directions; like a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object, `datetime` assumes there are exactly 3600*24 seconds in every day.
Constructor:

_class_ datetime.datetime(_year_ , _month_ , _day_ , _hour =0_, _minute =0_, _second =0_, _microsecond =0_, _tzinfo =None_, _*_ , _fold =0_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime "Link to this definition")

The _year_ , _month_ and _day_ arguments are required. _tzinfo_ may be `None`, or an instance of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass. The remaining arguments must be integers in the following ranges:
  * `MINYEAR <= year <= MAXYEAR`,
  * `1 <= month <= 12`,
  * `1 <= day <= number of days in the given month and year`,
  * `0 <= hour < 24`,
  * `0 <= minute < 60`,
  * `0 <= second < 60`,
  * `0 <= microsecond < 1000000`,
  * `fold in [0, 1]`.


If an argument outside those ranges is given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
Changed in version 3.6: Added the _fold_ parameter.
Other constructors, all class methods:

_classmethod_ datetime.today()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.today "Link to this definition")

Return the current local date and time, with [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") `None`.
Equivalent to:
Copy```
datetime.fromtimestamp(time.time())

```

See also [`now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now"), [`fromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp "datetime.datetime.fromtimestamp").
This method is functionally equivalent to [`now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now"), but without a `tz` parameter.

_classmethod_ datetime.now(_tz =None_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "Link to this definition")

Return the current local date and time.
If optional argument _tz_ is `None` or not specified, this is like [`today()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.today "datetime.datetime.today"), but, if possible, supplies more precision than can be gotten from going through a [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time") timestamp (for example, this may be possible on platforms supplying the C `gettimeofday()` function).
If _tz_ is not `None`, it must be an instance of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass, and the current date and time are converted to _tz_ ’s time zone.
This function is preferred over [`today()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.today "datetime.datetime.today") and [`utcnow()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow "datetime.datetime.utcnow").
Note
Subsequent calls to `datetime.now()` may return the same instant depending on the precision of the underlying clock.

_classmethod_ datetime.utcnow()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow "Link to this definition")

Return the current UTC date and time, with [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") `None`.
This is like [`now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now"), but returns the current UTC date and time, as a naive [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object. An aware current UTC datetime can be obtained by calling `datetime.now(timezone.utc)`. See also `now()`.
Warning
Because naive `datetime` objects are treated by many `datetime` methods as local times, it is preferred to use aware datetimes to represent times in UTC. As such, the recommended way to create an object representing the current time in UTC is by calling `datetime.now(timezone.utc)`.
Deprecated since version 3.12: Use [`datetime.now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now") with [`UTC`](https://docs.python.org/3/library/datetime.html#datetime.UTC "datetime.UTC") instead.

_classmethod_ datetime.fromtimestamp(_timestamp_ , _tz =None_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp "Link to this definition")

Return the local date and time corresponding to the POSIX timestamp, such as is returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time"). If optional argument _tz_ is `None` or not specified, the timestamp is converted to the platform’s local date and time, and the returned [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object is naive.
If _tz_ is not `None`, it must be an instance of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass, and the timestamp is converted to _tz_ ’s time zone.
`fromtimestamp()` may raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError"), if the timestamp is out of the range of values supported by the platform C `localtime()` or `gmtime()` functions, and [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") on `localtime()` or `gmtime()` failure. It’s common for this to be restricted to years in 1970 through 2038. Note that on non-POSIX systems that include leap seconds in their notion of a timestamp, leap seconds are ignored by `fromtimestamp()`, and then it’s possible to have two timestamps differing by a second that yield identical [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects. This method is preferred over [`utcfromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp "datetime.datetime.utcfromtimestamp").
Changed in version 3.3: Raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the timestamp is out of the range of values supported by the platform C `localtime()` or `gmtime()` functions. Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of `ValueError` on `localtime()` or `gmtime()` failure.
Changed in version 3.6: `fromtimestamp()` may return instances with [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") set to 1.

_classmethod_ datetime.utcfromtimestamp(_timestamp_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp "Link to this definition")

Return the UTC [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") corresponding to the POSIX timestamp, with [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") `None`. (The resulting object is naive.)
This may raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError"), if the timestamp is out of the range of values supported by the platform C `gmtime()` function, and [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") on `gmtime()` failure. It’s common for this to be restricted to years in 1970 through 2038.
To get an aware [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object, call [`fromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp "datetime.datetime.fromtimestamp"):
Copy```
datetime.fromtimestamp(timestamp, timezone.utc)

```

On the POSIX compliant platforms, it is equivalent to the following expression:
Copy```
datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=timestamp)

```

except the latter formula always supports the full years range: between [`MINYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MINYEAR "datetime.MINYEAR") and [`MAXYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MAXYEAR "datetime.MAXYEAR") inclusive.
Warning
Because naive `datetime` objects are treated by many `datetime` methods as local times, it is preferred to use aware datetimes to represent times in UTC. As such, the recommended way to create an object representing a specific timestamp in UTC is by calling `datetime.fromtimestamp(timestamp, tz=timezone.utc)`.
Changed in version 3.3: Raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the timestamp is out of the range of values supported by the platform C `gmtime()` function. Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of `ValueError` on `gmtime()` failure.
Changed in version 3.15: Accepts any real number as _timestamp_ , not only integer or float.
Deprecated since version 3.12: Use [`datetime.fromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp "datetime.datetime.fromtimestamp") with [`UTC`](https://docs.python.org/3/library/datetime.html#datetime.UTC "datetime.UTC") instead.

_classmethod_ datetime.fromordinal(_ordinal_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromordinal "Link to this definition")

Return the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") corresponding to the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1. [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised unless `1 <= ordinal <= datetime.max.toordinal()`. The hour, minute, second and microsecond of the result are all 0, and [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") is `None`.

_classmethod_ datetime.combine(_date_ , _time_ , _tzinfo =time.tzinfo_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.combine "Link to this definition")

Return a new [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object whose date components are equal to the given [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object’s, and whose time components are equal to the given [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object’s. If the _tzinfo_ argument is provided, its value is used to set the [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attribute of the result, otherwise the [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "datetime.time.tzinfo") attribute of the _time_ argument is used. If the _date_ argument is a `datetime` object, its time components and `tzinfo` attributes are ignored.
For any [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object `d`, `d == datetime.combine(d.date(), d.time(), d.tzinfo)`.
Changed in version 3.6: Added the _tzinfo_ argument.

_classmethod_ datetime.fromisoformat(_date_string_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat "Link to this definition")

Return a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") corresponding to a _date_string_ in any valid ISO 8601 format, with the following exceptions:
  1. Time zone offsets may have fractional seconds.
  2. The `T` separator may be replaced by any single unicode character.
  3. Fractional hours and minutes are not supported.
  4. Reduced precision dates are not currently supported (`YYYY-MM`, `YYYY`).
  5. Extended date representations are not currently supported (`±YYYYYY-MM-DD`).
  6. Ordinal dates are not currently supported (`YYYY-OOO`).


Examples:
Copy```
>>> import datetime as dt
>>> dt.datetime.fromisoformat('2011-11-04')
datetime.datetime(2011, 11, 4, 0, 0)
>>> dt.datetime.fromisoformat('20111104')
datetime.datetime(2011, 11, 4, 0, 0)
>>> dt.datetime.fromisoformat('2011-11-04T00:05:23')
datetime.datetime(2011, 11, 4, 0, 5, 23)
>>> dt.datetime.fromisoformat('2011-11-04T00:05:23Z')
datetime.datetime(2011, 11, 4, 0, 5, 23, tzinfo=datetime.timezone.utc)
>>> dt.datetime.fromisoformat('20111104T000523')
datetime.datetime(2011, 11, 4, 0, 5, 23)
>>> dt.datetime.fromisoformat('2011-W01-2T00:05:23.283')
datetime.datetime(2011, 1, 4, 0, 5, 23, 283000)
>>> dt.datetime.fromisoformat('2011-11-04 00:05:23.283')
datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
>>> dt.datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
datetime.datetime(2011, 11, 4, 0, 5, 23, 283000, tzinfo=datetime.timezone.utc)
>>> dt.datetime.fromisoformat('2011-11-04T00:05:23+04:00')
datetime.datetime(2011, 11, 4, 0, 5, 23,
    tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))

```

Added in version 3.7.
Changed in version 3.11: Previously, this method only supported formats that could be emitted by [`date.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.date.isoformat "datetime.date.isoformat") or [`datetime.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat "datetime.datetime.isoformat").

_classmethod_ datetime.fromisocalendar(_year_ , _week_ , _day_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisocalendar "Link to this definition")

Return a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") corresponding to the ISO calendar date specified by _year_ , _week_ and _day_. The non-date components of the datetime are populated with their normal default values. This is the inverse of the function [`datetime.isocalendar()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isocalendar "datetime.datetime.isocalendar").
Added in version 3.8.

_classmethod_ datetime.strptime(_date_string_ , _format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "Link to this definition")

Return a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") corresponding to _date_string_ , parsed according to _format_.
If _format_ does not contain microseconds or time zone information, this is equivalent to:
Copy```
datetime(*(time.strptime(date_string, format)[0:6]))

```

[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the date_string and format can’t be parsed by [`time.strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime") or if it returns a value which isn’t a time tuple. See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`datetime.fromisoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat "datetime.datetime.fromisoformat").
Changed in version 3.13: If _format_ specifies a day of month without a year a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") is now emitted. This is to avoid a quadrennial leap year bug in code seeking to parse only a month and day as the default year used in absence of one in the format is not a leap year. Such _format_ values may raise an error as of Python 3.15. The workaround is to always include a year in your _format_. If parsing _date_string_ values that do not have a year, explicitly add a year that is a leap year before parsing:
Copy```
>>> import datetime as dt
>>> date_string = "02/29"
>>> when = dt.datetime.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
>>> when.strftime("%B %d")
'February 29'

```

Class attributes:

datetime.min[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.min "Link to this definition")

The earliest representable [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"), `datetime(MINYEAR, 1, 1, tzinfo=None)`.

datetime.max[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.max "Link to this definition")

The latest representable [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"), `datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=None)`.

datetime.resolution[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.resolution "Link to this definition")

The smallest possible difference between non-equal [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects, `timedelta(microseconds=1)`.
Instance attributes (read-only):

datetime.year[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.year "Link to this definition")

Between [`MINYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MINYEAR "datetime.MINYEAR") and [`MAXYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MAXYEAR "datetime.MAXYEAR") inclusive.

datetime.month[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.month "Link to this definition")

Between 1 and 12 inclusive.

datetime.day[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.day "Link to this definition")

Between 1 and the number of days in the given month of the given year.

datetime.hour[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour "Link to this definition")

In `range(24)`.

datetime.minute[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute "Link to this definition")

In `range(60)`.

datetime.second[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.second "Link to this definition")

In `range(60)`.

datetime.microsecond[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond "Link to this definition")

In `range(1000000)`.

datetime.tzinfo[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "Link to this definition")

The object passed as the _tzinfo_ argument to the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") constructor, or `None` if none was passed.

datetime.fold[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "Link to this definition")

In `[0, 1]`. Used to disambiguate wall times during a repeated interval. (A repeated interval occurs when clocks are rolled back at the end of daylight saving time or when the UTC offset for the current zone is decreased for political reasons.) The values 0 and 1 represent, respectively, the earlier and later of the two moments with the same wall time representation.
Added in version 3.6.
Supported operations:
Operation | Result
---|---
`datetime2 = datetime1 + timedelta` | (1)
`datetime2 = datetime1 - timedelta` | (2)
`timedelta = datetime1 - datetime2` | (3)
`datetime1 == datetime2` `datetime1 != datetime2` | Equality comparison. (4)
`datetime1 < datetime2` `datetime1 > datetime2` `datetime1 <= datetime2` `datetime1 >= datetime2` | Order comparison. (5)
  1. `datetime2` is a duration of `timedelta` removed from `datetime1`, moving forward in time if `timedelta.days > 0`, or backward if `timedelta.days < 0`. The result has the same [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attribute as the input datetime, and `datetime2 - datetime1 == timedelta` after. [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") is raised if `datetime2.year` would be smaller than [`MINYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MINYEAR "datetime.MINYEAR") or larger than [`MAXYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MAXYEAR "datetime.MAXYEAR"). Note that no time zone adjustments are done even if the input is an aware object.
  2. Computes the `datetime2` such that `datetime2 + timedelta == datetime1`. As for addition, the result has the same [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attribute as the input datetime, and no time zone adjustments are done even if the input is aware.
  3. Subtraction of a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") from a `datetime` is defined only if both operands are naive, or if both are aware. If one is aware and the other is naive, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised.
If both are naive, or both are aware and have the same [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attribute, the `tzinfo` attributes are ignored, and the result is a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object `t` such that `datetime2 + t == datetime1`. No time zone adjustments are done in this case.
If both are aware and have different [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attributes, `a-b` acts as if `a` and `b` were first converted to naive UTC datetimes. The result is `(a.replace(tzinfo=None) - a.utcoffset()) - (b.replace(tzinfo=None) - b.utcoffset())` except that the implementation never overflows.
  4. [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects are equal if they represent the same date and time, taking into account the time zone.
Naive and aware `datetime` objects are never equal.
If both comparands are aware, and have the same `tzinfo` attribute, the `tzinfo` and [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") attributes are ignored and the base datetimes are compared. If both comparands are aware and have different [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attributes, the comparison acts as comparands were first converted to UTC datetimes except that the implementation never overflows. `datetime` instances in a repeated interval are never equal to `datetime` instances in other time zone.
  5. _datetime1_ is considered less than _datetime2_ when _datetime1_ precedes _datetime2_ in time, taking into account the time zone.
Order comparison between naive and aware [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
If both comparands are aware, and have the same `tzinfo` attribute, the `tzinfo` and [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") attributes are ignored and the base datetimes are compared. If both comparands are aware and have different [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") attributes, the comparison acts as comparands were first converted to UTC datetimes except that the implementation never overflows.


Changed in version 3.3: Equality comparisons between aware and naive [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instances don’t raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
Changed in version 3.13: Comparison between [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object and an instance of the [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") subclass that is not a `datetime` subclass no longer converts the latter to `date`, ignoring the time part and the time zone. The default behavior can be changed by overriding the special comparison methods in subclasses.
Instance methods:

datetime.date()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.date "Link to this definition")
