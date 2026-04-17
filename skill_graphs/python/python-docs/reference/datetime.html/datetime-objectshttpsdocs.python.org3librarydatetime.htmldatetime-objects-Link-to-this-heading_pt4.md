Copy```
import datetime as dt

# A class capturing the platform's idea of local time.
# (May result in wrong values on historical times in
#  timezones where UTC offset and/or the DST rules had
#  changed in the past.)
import time

ZERO = dt.timedelta(0)
HOUR = dt.timedelta(hours=1)
SECOND = dt.timedelta(seconds=1)

STDOFFSET = dt.timedelta(seconds=-time.timezone)
if time.daylight:
    DSTOFFSET = dt.timedelta(seconds=-time.altzone)
else:
    DSTOFFSET = STDOFFSET

DSTDIFF = DSTOFFSET - STDOFFSET


class LocalTimezone(dt.tzinfo):

    def fromutc(self, when):
        assert when.tzinfo is self
        stamp = (when - dt.datetime(1970, 1, 1, tzinfo=self)) // SECOND
        args = time.localtime(stamp)[:6]
        dst_diff = DSTDIFF // SECOND
        # Detect fold
        fold = (args == time.localtime(stamp - dst_diff))
        return dt.datetime(*args, microsecond=when.microsecond,
                           tzinfo=self, fold=fold)

    def utcoffset(self, when):
        if self._isdst(when):
            return DSTOFFSET
        else:
            return STDOFFSET

    def dst(self, when):
        if self._isdst(when):
            return DSTDIFF
        else:
            return ZERO

    def tzname(self, when):
        return time.tzname[self._isdst(when)]

    def _isdst(self, when):
        tt = (when.year, when.month, when.day,
              when.hour, when.minute, when.second,
              when.weekday(), 0, 0)
        stamp = time.mktime(tt)
        tt = time.localtime(stamp)
        return tt.tm_isdst > 0


Local = LocalTimezone()


# A complete implementation of current DST rules for major US time zones.

def first_sunday_on_or_after(when):
    days_to_go = 6 - when.weekday()
    if days_to_go:
        when += dt.timedelta(days_to_go)
    return when


# US DST Rules
#
# This is a simplified (i.e., wrong for a few cases) set of rules for US
# DST start and end times. For a complete and up-to-date set of DST rules
# and timezone definitions, visit the Olson Database (or try pytz):
# http://www.twinsun.com/tz/tz-link.htm
# https://sourceforge.net/projects/pytz/ (might not be up-to-date)
#
# In the US, since 2007, DST starts at 2am (standard time) on the second
# Sunday in March, which is the first Sunday on or after Mar 8.
DSTSTART_2007 = dt.datetime(1, 3, 8, 2)
# and ends at 2am (DST time) on the first Sunday of Nov.
DSTEND_2007 = dt.datetime(1, 11, 1, 2)
# From 1987 to 2006, DST used to start at 2am (standard time) on the first
# Sunday in April and to end at 2am (DST time) on the last
# Sunday of October, which is the first Sunday on or after Oct 25.
DSTSTART_1987_2006 = dt.datetime(1, 4, 1, 2)
DSTEND_1987_2006 = dt.datetime(1, 10, 25, 2)
# From 1967 to 1986, DST used to start at 2am (standard time) on the last
# Sunday in April (the one on or after April 24) and to end at 2am (DST time)
# on the last Sunday of October, which is the first Sunday
# on or after Oct 25.
DSTSTART_1967_1986 = dt.datetime(1, 4, 24, 2)
DSTEND_1967_1986 = DSTEND_1987_2006


def us_dst_range(year):
    # Find start and end times for US DST. For years before 1967, return
    # start = end for no DST.
    if 2006 < year:
        dststart, dstend = DSTSTART_2007, DSTEND_2007
    elif 1986 < year < 2007:
        dststart, dstend = DSTSTART_1987_2006, DSTEND_1987_2006
    elif 1966 < year < 1987:
        dststart, dstend = DSTSTART_1967_1986, DSTEND_1967_1986
    else:
        return (dt.datetime(year, 1, 1), ) * 2

    start = first_sunday_on_or_after(dststart.replace(year=year))
    end = first_sunday_on_or_after(dstend.replace(year=year))
    return start, end


class USTimeZone(dt.tzinfo):

    def __init__(self, hours, reprname, stdname, dstname):
        self.stdoffset = dt.timedelta(hours=hours)
        self.reprname = reprname
        self.stdname = stdname
        self.dstname = dstname

    def __repr__(self):
        return self.reprname

    def tzname(self, when):
        if self.dst(when):
            return self.dstname
        else:
            return self.stdname

    def utcoffset(self, when):
        return self.stdoffset + self.dst(when)

    def dst(self, when):
        if when is None or when.tzinfo is None:
            # An exception may be sensible here, in one or both cases.
            # It depends on how you want to treat them.  The default
            # fromutc() implementation (called by the default astimezone()
            # implementation) passes a datetime with when.tzinfo is self.
            return ZERO
        assert when.tzinfo is self
        start, end = us_dst_range(when.year)
        # Can't compare naive to aware objects, so strip the timezone from
        # when first.
        when = when.replace(tzinfo=None)
        if start + HOUR <= when < end - HOUR:
            # DST is in effect.
            return HOUR
        if end - HOUR <= when < end:
            # Fold (an ambiguous hour): use when.fold to disambiguate.
            return ZERO if when.fold else HOUR
        if start <= when < start + HOUR:
            # Gap (a non-existent hour): reverse the fold rule.
            return HOUR if when.fold else ZERO
        # DST is off.
        return ZERO

    def fromutc(self, when):
        assert when.tzinfo is self
        start, end = us_dst_range(when.year)
        start = start.replace(tzinfo=self)
        end = end.replace(tzinfo=self)
        std_time = when + self.stdoffset
        dst_time = std_time + HOUR
        if end <= dst_time < end + HOUR:
            # Repeated hour
            return std_time.replace(fold=1)
        if std_time < start or dst_time >= end:
            # Standard time
            return std_time
        if start <= std_time < end - HOUR:
            # Daylight saving time
            return dst_time


Eastern  = USTimeZone(-5, "Eastern",  "EST", "EDT")
Central  = USTimeZone(-6, "Central",  "CST", "CDT")
Mountain = USTimeZone(-7, "Mountain", "MST", "MDT")
Pacific  = USTimeZone(-8, "Pacific",  "PST", "PDT")

```

Note that there are unavoidable subtleties twice per year in a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass accounting for both standard and daylight time, at the DST transition points. For concreteness, consider US Eastern (UTC -0500), where EDT begins the minute after 1:59 (EST) on the second Sunday in March, and ends the minute after 1:59 (EDT) on the first Sunday in November:
Copy```
  UTC   3:MM  4:MM  5:MM  6:MM  7:MM  8:MM
  EST  22:MM 23:MM  0:MM  1:MM  2:MM  3:MM
  EDT  23:MM  0:MM  1:MM  2:MM  3:MM  4:MM

start  22:MM 23:MM  0:MM  1:MM  3:MM  4:MM

  end  23:MM  0:MM  1:MM  1:MM  2:MM  3:MM

```

When DST starts (the “start” line), the local wall clock leaps from 1:59 to 3:00. A wall time of the form 2:MM doesn’t really make sense on that day, so `astimezone(Eastern)` won’t deliver a result with `hour == 2` on the day DST begins. For example, at the Spring forward transition of 2016, we get:
Copy```
>>> import datetime as dt
>>> from tzinfo_examples import HOUR, Eastern
>>> u0 = dt.datetime(2016, 3, 13, 5, tzinfo=dt.timezone.utc)
>>> for i in range(4):
...     u = u0 + i*HOUR
...     t = u.astimezone(Eastern)
...     print(u.time(), 'UTC =', t.time(), t.tzname())
...
05:00:00 UTC = 00:00:00 EST
06:00:00 UTC = 01:00:00 EST
07:00:00 UTC = 03:00:00 EDT
08:00:00 UTC = 04:00:00 EDT

```

When DST ends (the “end” line), there’s a potentially worse problem: there’s an hour that can’t be spelled unambiguously in local wall time: the last hour of daylight time. In Eastern, that’s times of the form 5:MM UTC on the day daylight time ends. The local wall clock leaps from 1:59 (daylight time) back to 1:00 (standard time) again. Local times of the form 1:MM are ambiguous. [`astimezone()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "datetime.datetime.astimezone") mimics the local clock’s behavior by mapping two adjacent UTC hours into the same local hour then. In the Eastern example, UTC times of the form 5:MM and 6:MM both map to 1:MM when converted to Eastern, but earlier times have the [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") attribute set to 0 and the later times have it set to 1. For example, at the Fall back transition of 2016, we get:
Copy```
>>> import datetime as dt
>>> from tzinfo_examples import HOUR, Eastern
>>> u0 = dt.datetime(2016, 11, 6, 4, tzinfo=dt.timezone.utc)
>>> for i in range(4):
...     u = u0 + i*HOUR
...     t = u.astimezone(Eastern)
...     print(u.time(), 'UTC =', t.time(), t.tzname(), t.fold)
...
04:00:00 UTC = 00:00:00 EDT 0
05:00:00 UTC = 01:00:00 EDT 0
06:00:00 UTC = 01:00:00 EST 1
07:00:00 UTC = 02:00:00 EST 0

```

Note that the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instances that differ only by the value of the [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") attribute are considered equal in comparisons.
Applications that can’t bear wall-time ambiguities should explicitly check the value of the [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") attribute or avoid using hybrid [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclasses; there are no ambiguities when using [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone"), or any other fixed-offset `tzinfo` subclass (such as a class representing only EST (fixed offset -5 hours), or only EDT (fixed offset -4 hours)).
See also
>

[`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo "zoneinfo: IANA time zone support")

> The `datetime` module has a basic [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") class (for handling arbitrary fixed offsets from UTC) and its [`timezone.utc`](https://docs.python.org/3/library/datetime.html#datetime.timezone.utc "datetime.timezone.utc") attribute (a UTC `timezone` instance).
> `zoneinfo` brings the _IANA time zone database_ (also known as the Olson database) to Python, and its usage is recommended.
The Time Zone Database (often called tz, tzdata or zoneinfo) contains code and data that represent the history of local time for many representative locations around the globe. It is updated periodically to reflect changes made by political bodies to time zone boundaries, UTC offsets, and daylight-saving rules.
##  `timezone` objects[¶](https://docs.python.org/3/library/datetime.html#timezone-objects "Link to this heading")
The [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") class is a subclass of [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo"), each instance of which represents a time zone defined by a fixed offset from UTC.
Objects of this class cannot be used to represent time zone information in the locations where different offsets are used in different days of the year or where historical changes have been made to civil time.

_class_ datetime.timezone(_offset_ , _name =None_)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone "Link to this definition")

The _offset_ argument must be specified as a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object representing the difference between the local time and UTC. It must be strictly between `-timedelta(hours=24)` and `timedelta(hours=24)`, otherwise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
The _name_ argument is optional. If specified it must be a string that will be used as the value returned by the [`datetime.tzname()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzname "datetime.datetime.tzname") method.
Added in version 3.2.
Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.

timezone.utcoffset(_dt_)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.utcoffset "Link to this definition")

Return the fixed value specified when the [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") instance is constructed.
The _dt_ argument is ignored. The return value is a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") instance equal to the difference between the local time and UTC.
Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.

timezone.tzname(_dt_)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.tzname "Link to this definition")

Return the fixed value specified when the [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") instance is constructed.
If _name_ is not provided in the constructor, the name returned by `tzname(dt)` is generated from the value of the `offset` as follows. If _offset_ is `timedelta(0)`, the name is “UTC”, otherwise it is a string in the format `UTC±HH:MM`, where ± is the sign of `offset`, HH and MM are two digits of `offset.hours` and `offset.minutes` respectively.
Changed in version 3.6: Name generated from `offset=timedelta(0)` is now plain `'UTC'`, not `'UTC+00:00'`.

timezone.dst(_dt_)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.dst "Link to this definition")

Always returns `None`.

timezone.fromutc(_dt_)[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.fromutc "Link to this definition")

Return `dt + offset`. The _dt_ argument must be an aware [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance, with `tzinfo` set to `self`.
Class attributes:

timezone.utc[¶](https://docs.python.org/3/library/datetime.html#datetime.timezone.utc "Link to this definition")

The UTC time zone, `timezone(timedelta(0))`.
##  `strftime()` and `strptime()` behavior[¶](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior "Link to this heading")
[`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date"), [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"), and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects all support a `strftime(format)` method, to create a string representing the time under the control of an explicit format string.
Conversely, the [`date.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strptime "datetime.date.strptime"), [`datetime.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") and [`time.strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime") class methods create an object from a string representing the time and a corresponding format string.
The table below provides a high-level comparison of [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime") versus [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime"):
| `strftime` | `strptime`
---|---|---
Usage | Convert object to a string according to a given format | Parse a string into an object given a corresponding format
Type of method | Instance method | Class method
Signature | `strftime(format)` | `strptime(date_string, format)`
###  `strftime()` and `strptime()` format codes[¶](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes "Link to this heading")
These methods accept format codes that can be used to parse and format dates:
Copy```
>>> import datetime as dt
>>> dt.datetime.strptime('31/01/22 23:59:59.999999',
...                      '%d/%m/%y %H:%M:%S.%f')
datetime.datetime(2022, 1, 31, 23, 59, 59, 999999)
>>> _.strftime('%a %d %b %Y, %I:%M%p')
'Mon 31 Jan 2022, 11:59PM'

```

The following is a list of all the format codes that the 1989 C standard requires, and these work on all platforms with a standard C implementation.
Directive | Meaning | Example | Notes
---|---|---|---
`%a` | Weekday as locale’s abbreviated name. |  Sun, Mon, …, Sat (en_US); So, Mo, …, Sa (de_DE) | (1)
`%A` | Weekday as locale’s full name. |  Sunday, Monday, …, Saturday (en_US); Sonntag, Montag, …, Samstag (de_DE) | (1)
`%w` | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday. | 0, 1, …, 6 |
`%d` | Day of the month as a zero-padded decimal number. | 01, 02, …, 31 | (9)
`%b` | Month as locale’s abbreviated name. |  Jan, Feb, …, Dec (en_US); Jan, Feb, …, Dez (de_DE) | (1)
`%B` | Month as locale’s full name. |  January, February, …, December (en_US); January, February, …, December (de_DE) | (1)
`%m` | Month as a zero-padded decimal number. | 01, 02, …, 12 | (9)
`%y` | Year without century as a zero-padded decimal number. | 00, 01, …, 99 | (9)
`%Y` | Year with century as a decimal number. | 0001, 0002, …, 2013, 2014, …, 9998, 9999 | (2)
`%H` | Hour (24-hour clock) as a zero-padded decimal number. | 00, 01, …, 23 | (9)
`%I` | Hour (12-hour clock) as a zero-padded decimal number. | 01, 02, …, 12 | (9)
`%p` | Locale’s equivalent of either AM or PM. |  AM, PM (en_US); am, pm (de_DE) | (1), (3)
`%M` | Minute as a zero-padded decimal number. | 00, 01, …, 59 | (9)
`%S` | Second as a zero-padded decimal number. | 00, 01, …, 59 | (4), (9)
`%f` | Microsecond as a decimal number, zero-padded to 6 digits. | 000000, 000001, …, 999999 | (5)
`%z` | UTC offset in the form `±HHMM[SS[.ffffff]]` (empty string if the object is naive). | (empty), +0000, -0400, +1030, +063415, -030712.345216 | (6)
`%Z` | Time zone name (empty string if the object is naive). | (empty), UTC, GMT | (6)
`%j` | Day of the year as a zero-padded decimal number. | 001, 002, …, 366 | (9)
`%U` | Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. | 00, 01, …, 53 | (7), (9)
`%W` | Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0. | 00, 01, …, 53 | (7), (9)
`%c` | Locale’s appropriate date and time representation. |  Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE) | (1)
`%x` | Locale’s appropriate date representation. |  08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE) | (1)
`%X` | Locale’s appropriate time representation. |  21:30:00 (en_US); 21:30:00 (de_DE) | (1)
`%%` | A literal `'%'` character. | % |
Several additional directives not required by the C89 standard are included for convenience. These parameters all correspond to ISO 8601 date values.
Directive | Meaning | Example | Notes
---|---|---|---
`%G` | ISO 8601 year with century representing the year that contains the greater part of the ISO week (`%V`). | 0001, 0002, …, 2013, 2014, …, 9998, 9999 | (8)
`%u` | ISO 8601 weekday as a decimal number where 1 is Monday. | 1, 2, …, 7 |
`%V` | ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4. | 01, 02, …, 53 | (8), (9)
`%:z` | UTC offset in the form `±HH:MM[:SS[.ffffff]]` (empty string if the object is naive). | (empty), +00:00, -04:00, +10:30, +06:34:15, -03:07:12.345216 | (6)
These may not be available on all platforms when used with the [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime") method. The ISO 8601 year and ISO 8601 week directives are not interchangeable with the year and week number directives above. Calling [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") with incomplete or ambiguous ISO 8601 directives will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
The full set of format codes supported varies across platforms, because Python calls the platform C library’s `strftime()` function, and platform variations are common. To see the full set of format codes supported on your platform, consult the
Added in version 3.6: `%G`, `%u` and `%V` were added.
Added in version 3.12: `%:z` was added.
### Technical detail[¶](https://docs.python.org/3/library/datetime.html#technical-detail "Link to this heading")
Broadly speaking, `d.strftime(fmt)` acts like the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") module’s `time.strftime(fmt, d.timetuple())` although not all objects support a [`timetuple()`](https://docs.python.org/3/library/datetime.html#datetime.date.timetuple "datetime.date.timetuple") method.
For the [`datetime.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") and [`date.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strptime "datetime.date.strptime") class methods, the default value is `1900-01-01T00:00:00.000`: any components not specified in the format string will be pulled from the default value.
Note
Format strings without separators can be ambiguous for parsing. For example, with `%Y%m%d`, the string `2026111` may be parsed either as `2026-11-01` or as `2026-01-11`. Use separators to ensure the input is parsed as intended.
Note
When used to parse partial dates lacking a year, [`datetime.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") and [`date.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strptime "datetime.date.strptime") will raise when encountering February 29 because the default year of 1900 is _not_ a leap year. Always add a default leap year to partial date strings before parsing.
Copy```
>>> import datetime as dt
>>> value = "2/29"
>>> dt.datetime.strptime(value, "%m/%d")
Traceback (most recent call last):
...
ValueError: day 29 must be in range 1..28 for month 2 in year 1900
>>> dt.datetime.strptime(f"1904 {value}", "%Y %m/%d")
datetime.datetime(1904, 2, 29, 0, 0)

```

Using `datetime.strptime(date_string, format)` is equivalent to:
Copy```
datetime(*(time.strptime(date_string, format)[0:6]))

```

except when the format includes sub-second components or time zone offset information, which are supported in `datetime.strptime` but are discarded by `time.strptime`.
For [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects, the format codes for year, month, and day should not be used, as `time` objects have no such values. If they’re used anyway, 1900 is substituted for the year, and 1 for the month and day.
For [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects, the format codes for hours, minutes, seconds, and microseconds should not be used, as `date` objects have no such values. If they’re used anyway, 0 is substituted for them.
For the same reason, handling of format strings containing Unicode code points that can’t be represented in the charset of the current locale is also platform-dependent. On some platforms such code points are preserved intact in the output, while on others `strftime` may raise [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError") or return an empty string instead.
Notes:
  1. Because the format depends on the current locale, care should be taken when making assumptions about the output value. Field orderings will vary (for example, “month/day/year” versus “day/month/year”), and the output may contain non-ASCII characters.
  2. The [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") method can parse years in the full [1, 9999] range, but years < 1000 must be zero-filled to 4-digit width.
Changed in version 3.2: In previous versions, [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime") method was restricted to years >= 1900.
Changed in version 3.3: In version 3.2, [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime") method was restricted to years >= 1000.
  3. When used with the [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") method, the `%p` directive only affects the output hour field if the `%I` directive is used to parse the hour.
  4. Unlike the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") module, the `datetime` module does not support leap seconds.
  5. When used with the [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") method, the `%f` directive accepts from one to six digits and zero pads on the right. `%f` is an extension to the set of format characters in the C standard (but implemented separately in datetime objects, and therefore always available).
