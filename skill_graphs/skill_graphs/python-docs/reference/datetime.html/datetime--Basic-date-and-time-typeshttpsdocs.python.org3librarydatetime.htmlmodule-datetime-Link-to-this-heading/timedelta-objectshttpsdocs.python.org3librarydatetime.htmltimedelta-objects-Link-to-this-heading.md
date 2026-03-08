##  `timedelta` objects[¶](https://docs.python.org/3/library/datetime.html#timedelta-objects "Link to this heading")
A [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object represents a duration, the difference between two [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") or [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") instances.

_class_ datetime.timedelta(_days =0_, _seconds =0_, _microseconds =0_, _milliseconds =0_, _minutes =0_, _hours =0_, _weeks =0_)[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta "Link to this definition")

All arguments are optional and default to 0. Arguments may be integers or floats, and may be positive or negative.
Only _days_ , _seconds_ and _microseconds_ are stored internally. Arguments are converted to those units:
  * A millisecond is converted to 1000 microseconds.
  * A minute is converted to 60 seconds.
  * An hour is converted to 3600 seconds.
  * A week is converted to 7 days.


and days, seconds and microseconds are then normalized so that the representation is unique, with
  * `0 <= microseconds < 1000000`
  * `0 <= seconds < 3600*24` (the number of seconds in one day)
  * `-999999999 <= days <= 999999999`


The following example illustrates how any arguments besides _days_ , _seconds_ and _microseconds_ are “merged” and normalized into those three resulting attributes:
Copy```
>>> import datetime as dt
>>> delta = dt.timedelta(
...     days=50,
...     seconds=27,
...     microseconds=10,
...     milliseconds=29000,
...     minutes=5,
...     hours=8,
...     weeks=2
... )
>>> # Only days, seconds, and microseconds remain
>>> delta
datetime.timedelta(days=64, seconds=29156, microseconds=10)

```

Tip
`import datetime as dt` instead of `import datetime` or `from datetime import datetime` to avoid confusion between the module and the class. See
If any argument is a float and there are fractional microseconds, the fractional microseconds left over from all arguments are combined and their sum is rounded to the nearest microsecond using round-half-to-even tiebreaker. If no argument is a float, the conversion and normalization processes are exact (no information is lost).
If the normalized value of days lies outside the indicated range, [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") is raised.
Note that normalization of negative values may be surprising at first. For example:
Copy```
>>> import datetime as dt
>>> d = dt.timedelta(microseconds=-1)
>>> (d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)

```

Since the string representation of `timedelta` objects can be confusing, use the following recipe to produce a more readable format:
Copy```
>>> def pretty_timedelta(td):
...     if td.days >= 0:
...         return str(td)
...     return f'-({-td!s})'
...
>>> d = timedelta(hours=-1)
>>> str(d)  # not human-friendly
'-1 day, 23:00:00'
>>> pretty_timedelta(d)
'-(1:00:00)'

```

Class attributes:

timedelta.min[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.min "Link to this definition")

The most negative [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object, `timedelta(-999999999)`.

timedelta.max[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.max "Link to this definition")

The most positive [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object, `timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)`.

timedelta.resolution[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.resolution "Link to this definition")

The smallest possible difference between non-equal [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") objects, `timedelta(microseconds=1)`.
Note that, because of normalization, `timedelta.max` is greater than `-timedelta.min`. `-timedelta.max` is not representable as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object.
Instance attributes (read-only):

timedelta.days[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.days "Link to this definition")

Between -999,999,999 and 999,999,999 inclusive.

timedelta.seconds[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.seconds "Link to this definition")

Between 0 and 86,399 inclusive.
Caution
It is a somewhat common bug for code to unintentionally use this attribute when it is actually intended to get a [`total_seconds()`](https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds "datetime.timedelta.total_seconds") value instead:
Copy```
>>> import datetime as dt
>>> duration = dt.timedelta(seconds=11235813)
>>> duration.days, duration.seconds
(130, 3813)
>>> duration.total_seconds()
11235813.0

```


timedelta.microseconds[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.microseconds "Link to this definition")

Between 0 and 999,999 inclusive.
Supported operations:
Operation | Result
---|---
`t1 = t2 + t3` | Sum of `t2` and `t3`. Afterwards `t1 - t2 == t3` and `t1 - t3 == t2` are true. (1)
`t1 = t2 - t3` | Difference of `t2` and `t3`. Afterwards `t1 == t2 - t3` and `t2 == t1 + t3` are true. (1)(6)
`t1 = t2 * i or t1 = i * t2` | Delta multiplied by an integer. Afterwards `t1 // i == t2` is true, provided `i != 0`.
| In general, `t1  * i == t1 * (i-1) + t1` is true. (1)
`t1 = t2 * f or t1 = f * t2` | Delta multiplied by a float. The result is rounded to the nearest multiple of timedelta.resolution using round-half-to-even.
`f = t2 / t3` | Division (3) of overall duration `t2` by interval unit `t3`. Returns a [`float`](https://docs.python.org/3/library/functions.html#float "float") object.
`t1 = t2 / f or t1 = t2 / i` | Delta divided by a float or an int. The result is rounded to the nearest multiple of timedelta.resolution using round-half-to-even.
`t1 = t2 // i` or `t1 = t2 // t3` | The floor is computed and the remainder (if any) is thrown away. In the second case, an integer is returned. (3)
`t1 = t2 % t3` | The remainder is computed as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object. (3)
`q, r = divmod(t1, t2)` | Computes the quotient and the remainder: `q = t1 // t2` (3) and `r = t1 % t2`. `q` is an integer and `r` is a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object.
`+t1` | Returns a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object with the same value. (2)
`-t1` | Equivalent to `timedelta(-t1.days, -t1.seconds, -t1.microseconds)`, and to `t1 * -1`. (1)(4)
`abs(t)` | Equivalent to `+t` when `t.days >= 0`, and to `-t` when `t.days < 0`. (2)
`str(t)` | Returns a string in the form `[D day[s], ][H]H:MM:SS[.UUUUUU]`, where D is negative for negative `t`. (5)
`repr(t)` | Returns a string representation of the [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object as a constructor call with canonical attribute values.
Notes:
  1. This is exact but may overflow.
  2. This is exact and cannot overflow.
  3. Division by zero raises [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError "ZeroDivisionError").
  4. `-timedelta.max` is not representable as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object.
  5. String representations of [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") objects are normalized similarly to their internal representation. This leads to somewhat unusual results for negative timedeltas. For example:
Copy```
>>> timedelta(hours=-5)
datetime.timedelta(days=-1, seconds=68400)
>>> print(_)
-1 day, 19:00:00

```

  6. The expression `t2 - t3` will always be equal to the expression `t2 + (-t3)` except when t3 is equal to `timedelta.max`; in that case the former will produce a result while the latter will overflow.


In addition to the operations listed above, [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") objects support certain additions and subtractions with [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") and [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects (see below).
Changed in version 3.2: Floor division and true division of a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object by another `timedelta` object are now supported, as are remainder operations and the [`divmod()`](https://docs.python.org/3/library/functions.html#divmod "divmod") function. True division and multiplication of a `timedelta` object by a [`float`](https://docs.python.org/3/library/functions.html#float "float") object are now supported.
[`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") objects support equality and order comparisons.
In Boolean contexts, a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object is considered to be true if and only if it isn’t equal to `timedelta(0)`.
Instance methods:

timedelta.total_seconds()[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds "Link to this definition")

Return the total number of seconds contained in the duration. Equivalent to `td / timedelta(seconds=1)`. For interval units other than seconds, use the division form directly (for example, `td / timedelta(microseconds=1)`).
Note that for very large time intervals (greater than 270 years on most platforms) this method will lose microsecond accuracy.
Added in version 3.2.
### Examples of usage: `timedelta`[¶](https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta "Link to this heading")
An additional example of normalization:
Copy```
>>> # Components of another_year add up to exactly 365 days
>>> import datetime as dt
>>> year = dt.timedelta(days=365)
>>> another_year = dt.timedelta(weeks=40, days=84, hours=23,
...                             minutes=50, seconds=600)
>>> year == another_year
True
>>> year.total_seconds()
31536000.0

```

Examples of [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") arithmetic:
Copy```
>>> import datetime as dt
>>> year = dt.timedelta(days=365)
>>> ten_years = 10 * year
>>> ten_years
datetime.timedelta(days=3650)
>>> ten_years.days // 365
10
>>> nine_years = ten_years - year
>>> nine_years
datetime.timedelta(days=3285)
>>> three_years = nine_years // 3
>>> three_years, three_years.days // 365
(datetime.timedelta(days=1095), 3)

```

##  `date` objects[¶](https://docs.python.org/3/library/datetime.html#date-objects "Link to this heading")
A [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object represents a date (year, month and day) in an idealized calendar, the current Gregorian calendar indefinitely extended in both directions.
January 1 of year 1 is called day number 1, January 2 of year 1 is called day number 2, and so on. [[2]](https://docs.python.org/3/library/datetime.html#id5)

_class_ datetime.date(_year_ , _month_ , _day_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date "Link to this definition")

All arguments are required. Arguments must be integers, in the following ranges:
  * `MINYEAR <= year <= MAXYEAR`
  * `1 <= month <= 12`
  * `1 <= day <= number of days in the given month and year`


If an argument outside those ranges is given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
Other constructors, all class methods:

_classmethod_ date.today()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.today "Link to this definition")

Return the current local date.
This is equivalent to `date.fromtimestamp(time.time())`.

_classmethod_ date.fromtimestamp(_timestamp_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.fromtimestamp "Link to this definition")

Return the local date corresponding to the POSIX _timestamp_ , such as is returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time").
This may raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError"), if the timestamp is out of the range of values supported by the platform C `localtime()` function, and [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") on `localtime()` failure. It’s common for this to be restricted to years from 1970 through 2038. Note that on non-POSIX systems that include leap seconds in their notion of a timestamp, leap seconds are ignored by `fromtimestamp()`.
Changed in version 3.3: Raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the timestamp is out of the range of values supported by the platform C `localtime()` function. Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of `ValueError` on `localtime()` failure.

_classmethod_ date.fromordinal(_ordinal_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.fromordinal "Link to this definition")

Return the date corresponding to the proleptic Gregorian _ordinal_ , where January 1 of year 1 has ordinal 1.
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised unless `1 <= ordinal <= date.max.toordinal()`. For any date `d`, `date.fromordinal(d.toordinal()) == d`.

_classmethod_ date.fromisoformat(_date_string_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat "Link to this definition")

Return a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") corresponding to a _date_string_ given in any valid ISO 8601 format, with the following exceptions:
  1. Reduced precision dates are not currently supported (`YYYY-MM`, `YYYY`).
  2. Extended date representations are not currently supported (`±YYYYYY-MM-DD`).
  3. Ordinal dates are not currently supported (`YYYY-OOO`).


Examples:
Copy```
>>> import datetime as dt
>>> dt.date.fromisoformat('2019-12-04')
datetime.date(2019, 12, 4)
>>> dt.date.fromisoformat('20191204')
datetime.date(2019, 12, 4)
>>> dt.date.fromisoformat('2021-W01-1')
datetime.date(2021, 1, 4)

```

Added in version 3.7.
Changed in version 3.11: Previously, this method only supported the format `YYYY-MM-DD`.

_classmethod_ date.fromisocalendar(_year_ , _week_ , _day_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.fromisocalendar "Link to this definition")

Return a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") corresponding to the ISO calendar date specified by _year_ , _week_ and _day_. This is the inverse of the function [`date.isocalendar()`](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar "datetime.date.isocalendar").
Added in version 3.8.

_classmethod_ date.strptime(_date_string_ , _format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.strptime "Link to this definition")

Return a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") corresponding to _date_string_ , parsed according to _format_. This is equivalent to:
Copy```
date(*(time.strptime(date_string, format)[0:3]))

```

[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the date_string and format can’t be parsed by [`time.strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime") or if it returns a value which isn’t a time tuple. See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`date.fromisoformat()`](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat "datetime.date.fromisoformat").
Note
If _format_ specifies a day of month without a year a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") is emitted. This is to avoid a quadrennial leap year bug in code seeking to parse only a month and day as the default year used in absence of one in the format is not a leap year. Such _format_ values may raise an error as of Python 3.15. The workaround is to always include a year in your _format_. If parsing _date_string_ values that do not have a year, explicitly add a year that is a leap year before parsing:
Copy```
>>> import datetime as dt
>>> date_string = "02/29"
>>> when = dt.date.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
>>> when.strftime("%B %d")
'February 29'

```

Added in version 3.14.
Class attributes:

date.min[¶](https://docs.python.org/3/library/datetime.html#datetime.date.min "Link to this definition")

The earliest representable date, `date(MINYEAR, 1, 1)`.

date.max[¶](https://docs.python.org/3/library/datetime.html#datetime.date.max "Link to this definition")

The latest representable date, `date(MAXYEAR, 12, 31)`.

date.resolution[¶](https://docs.python.org/3/library/datetime.html#datetime.date.resolution "Link to this definition")

The smallest possible difference between non-equal date objects, `timedelta(days=1)`.
Instance attributes (read-only):

date.year[¶](https://docs.python.org/3/library/datetime.html#datetime.date.year "Link to this definition")

Between [`MINYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MINYEAR "datetime.MINYEAR") and [`MAXYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MAXYEAR "datetime.MAXYEAR") inclusive.

date.month[¶](https://docs.python.org/3/library/datetime.html#datetime.date.month "Link to this definition")

Between 1 and 12 inclusive.

date.day[¶](https://docs.python.org/3/library/datetime.html#datetime.date.day "Link to this definition")

Between 1 and the number of days in the given month of the given year.
Supported operations:
Operation | Result
---|---
`date2 = date1 + timedelta` | `date2` will be `timedelta.days` days after `date1`. (1)
`date2 = date1 - timedelta` | Computes `date2` such that `date2 + timedelta == date1`. (2)
`timedelta = date1 - date2` | (3)
`date1 == date2` `date1 != date2` | Equality comparison. (4)
`date1 < date2` `date1 > date2` `date1 <= date2` `date1 >= date2` | Order comparison. (5)
Notes:
  1. _date2_ is moved forward in time if `timedelta.days > 0`, or backward if `timedelta.days < 0`. Afterward `date2 - date1 == timedelta.days`. `timedelta.seconds` and `timedelta.microseconds` are ignored. [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") is raised if `date2.year` would be smaller than [`MINYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MINYEAR "datetime.MINYEAR") or larger than [`MAXYEAR`](https://docs.python.org/3/library/datetime.html#datetime.MAXYEAR "datetime.MAXYEAR").
  2. `timedelta.seconds` and `timedelta.microseconds` are ignored.
  3. This is exact, and cannot overflow. `timedelta.seconds` and `timedelta.microseconds` are 0, and `date2 + timedelta == date1` after.
  4. [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects are equal if they represent the same date.
`date` objects that are not also [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instances are never equal to `datetime` objects, even if they represent the same date.
  5. _date1_ is considered less than _date2_ when _date1_ precedes _date2_ in time. In other words, `date1 < date2` if and only if `date1.toordinal() < date2.toordinal()`.
Order comparison between a `date` object that is not also a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance and a `datetime` object raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").


Changed in version 3.13: Comparison between [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object and an instance of the [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") subclass that is not a `datetime` subclass no longer converts the latter to `date`, ignoring the time part and the time zone. The default behavior can be changed by overriding the special comparison methods in subclasses.
In Boolean contexts, all [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects are considered to be true.
Instance methods:

date.replace(_year =self.year_, _month =self.month_, _day =self.day_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.replace "Link to this definition")

Return a new [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object with the same values, but with specified parameters updated.
Example:
Copy```
>>> import datetime as dt
>>> d = dt.date(2002, 12, 31)
>>> d.replace(day=26)
datetime.date(2002, 12, 26)

```

The generic function [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace") also supports [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects.

date.timetuple()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.timetuple "Link to this definition")

Return a [`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time") such as returned by [`time.localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime").
The hours, minutes and seconds are 0, and the DST flag is -1.
`d.timetuple()` is equivalent to:
Copy```
time.struct_time((d.year, d.month, d.day, 0, 0, 0, d.weekday(), yday, -1))

```

where `yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1` is the day number within the current year starting with 1 for January 1st.

date.toordinal()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.toordinal "Link to this definition")

Return the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1. For any [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object `d`, `date.fromordinal(d.toordinal()) == d`.

date.weekday()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.weekday "Link to this definition")

Return the day of the week as an integer, where Monday is 0 and Sunday is 6. For example, `date(2002, 12, 4).weekday() == 2`, a Wednesday. See also [`isoweekday()`](https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday "datetime.date.isoweekday").

date.isoweekday()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday "Link to this definition")

Return the day of the week as an integer, where Monday is 1 and Sunday is 7. For example, `date(2002, 12, 4).isoweekday() == 3`, a Wednesday. See also [`weekday()`](https://docs.python.org/3/library/datetime.html#datetime.date.weekday "datetime.date.weekday"), [`isocalendar()`](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar "datetime.date.isocalendar").

date.isocalendar()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar "Link to this definition")

Return a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) object with three components: `year`, `week` and `weekday`.
The ISO calendar is a widely used variant of the Gregorian calendar. [[3]](https://docs.python.org/3/library/datetime.html#id6)
The ISO year consists of 52 or 53 full weeks, and where a week starts on a Monday and ends on a Sunday. The first week of an ISO year is the first (Gregorian) calendar week of a year containing a Thursday. This is called week number 1, and the ISO year of that Thursday is the same as its Gregorian year.
For example, 2004 begins on a Thursday, so the first week of ISO year 2004 begins on Monday, 29 Dec 2003 and ends on Sunday, 4 Jan 2004:
Copy```
>>> import datetime as dt
>>> dt.date(2003, 12, 29).isocalendar()
datetime.IsoCalendarDate(year=2004, week=1, weekday=1)
>>> dt.date(2004, 1, 4).isocalendar()
datetime.IsoCalendarDate(year=2004, week=1, weekday=7)

```

Changed in version 3.9: Result changed from a tuple to a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple).

date.isoformat()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.isoformat "Link to this definition")

Return a string representing the date in ISO 8601 format, `YYYY-MM-DD`:
Copy```
>>> import datetime as dt
>>> dt.date(2002, 12, 4).isoformat()
'2002-12-04'

```


date.__str__()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.__str__ "Link to this definition")

For a date `d`, `str(d)` is equivalent to `d.isoformat()`.

date.ctime()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.ctime "Link to this definition")

Return a string representing the date:
Copy```
>>> import datetime as dt
>>> dt.date(2002, 12, 4).ctime()
'Wed Dec  4 00:00:00 2002'

```

`d.ctime()` is equivalent to:
Copy```
time.ctime(time.mktime(d.timetuple()))

```

on platforms where the native C `ctime()` function (which [`time.ctime()`](https://docs.python.org/3/library/time.html#time.ctime "time.ctime") invokes, but which `date.ctime()` does not invoke) conforms to the C standard.

date.strftime(_format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.strftime "Link to this definition")

Return a string representing the date, controlled by an explicit format string. Format codes referring to hours, minutes or seconds will see 0 values. See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`date.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.date.isoformat "datetime.date.isoformat").

date.__format__(_format_)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.__format__ "Link to this definition")

Same as [`date.strftime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strftime "datetime.date.strftime"). This makes it possible to specify a format string for a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object in [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) and when using [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format"). See also [strftime() and strptime() behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) and [`date.isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.date.isoformat "datetime.date.isoformat").
### Examples of usage: `date`[¶](https://docs.python.org/3/library/datetime.html#examples-of-usage-date "Link to this heading")
Example of counting days to an event:
Copy```
>>> import time
>>> import datetime as dt
>>> today = dt.date.today()
>>> today
datetime.date(2007, 12, 5)
>>> today == dt.date.fromtimestamp(time.time())
True
>>> my_birthday = dt.date(today.year, 6, 24)
>>> if my_birthday < today:
...     my_birthday = my_birthday.replace(year=today.year + 1)
...
>>> my_birthday
datetime.date(2008, 6, 24)
>>> time_to_birthday = abs(my_birthday - today)
>>> time_to_birthday.days
202

```

More examples of working with [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date"):
Copy```
>>> import datetime as dt
>>> d = dt.date.fromordinal(730920) # 730920th day after 1. 1. 0001
>>> d
datetime.date(2002, 3, 11)

>>> # Methods related to formatting string output
>>> d.isoformat()
'2002-03-11'
>>> d.strftime("%d/%m/%y")
'11/03/02'
>>> d.strftime("%A %d. %B %Y")
'Monday 11. March 2002'
>>> d.ctime()
'Mon Mar 11 00:00:00 2002'
>>> 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
'The day is 11, the month is March.'

>>> # Methods for extracting 'components' under different calendars
>>> t = d.timetuple()
>>> for i in t:
...     print(i)
2002                # year
3                   # month
11                  # day
0
0
0
0                   # weekday (0 = Monday)
70                  # 70th day in the year
-1
>>> ic = d.isocalendar()
>>> for i in ic:
...     print(i)
2002                # ISO year
11                  # ISO week number
1                   # ISO day number ( 1 = Monday )

>>> # A date object is immutable; all operations produce a new object
>>> d.replace(year=2005)
datetime.date(2005, 3, 11)

```
