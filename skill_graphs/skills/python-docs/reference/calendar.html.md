[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`calendar` — General calendar-related functions](https://docs.python.org/3/library/calendar.html)
    * [Command-line usage](https://docs.python.org/3/library/calendar.html#command-line-usage)


#### Previous topic
[`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html "previous chapter")
#### Next topic
[`collections` — Container datatypes](https://docs.python.org/3/library/collections.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=calendar+%E2%80%94+General+calendar-related+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcalendar.html&pagesource=library%2Fcalendar.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/collections.html "collections — Container datatypes") |
  * [previous](https://docs.python.org/3/library/zoneinfo.html "zoneinfo — IANA time zone support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`calendar` — General calendar-related functions](https://docs.python.org/3/library/calendar.html)
  * |
  * Theme  Auto Light Dark |


#  `calendar` — General calendar-related functions[¶](https://docs.python.org/3/library/calendar.html#module-calendar "Link to this heading")
**Source code:**
* * *
This module allows you to output calendars like the Unix **cal** program, and provides additional useful functions related to the calendar. By default, these calendars have Monday as the first day of the week, and Sunday as the last (the European convention). Use [`setfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday "calendar.setfirstweekday") to set the first day of the week to Sunday (6) or to any other weekday. Parameters that specify dates are given as integers. For related functionality, see also the [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.") and [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") modules.
The functions and classes defined in this module use an idealized calendar, the current Gregorian calendar extended indefinitely in both directions. This matches the definition of the “proleptic Gregorian” calendar in Dershowitz and Reingold’s book “Calendrical Calculations”, where it’s the base calendar for all computations. Zero and negative years are interpreted as prescribed by the ISO 8601 standard. Year 0 is 1 BC, year -1 is 2 BC, and so on.

_class_ calendar.Calendar(_firstweekday =0_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar "Link to this definition")

Creates a `Calendar` object. _firstweekday_ is an integer specifying the first day of the week. [`MONDAY`](https://docs.python.org/3/library/calendar.html#calendar.MONDAY "calendar.MONDAY") is `0` (the default), [`SUNDAY`](https://docs.python.org/3/library/calendar.html#calendar.SUNDAY "calendar.SUNDAY") is `6`.
A `Calendar` object provides several methods that can be used for preparing the calendar data for formatting. This class doesn’t do any formatting itself. This is the job of subclasses.
`Calendar` instances have the following methods and attributes:

firstweekday[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.firstweekday "Link to this definition")

The first weekday as an integer (0–6).
This property can also be set and read using [`setfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.setfirstweekday "calendar.Calendar.setfirstweekday") and [`getfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.getfirstweekday "calendar.Calendar.getfirstweekday") respectively.

getfirstweekday()[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.getfirstweekday "Link to this definition")

Return an [`int`](https://docs.python.org/3/library/functions.html#int "int") for the current first weekday (0–6).
Identical to reading the [`firstweekday`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.firstweekday "calendar.Calendar.firstweekday") property.

setfirstweekday(_firstweekday_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.setfirstweekday "Link to this definition")

Set the first weekday to _firstweekday_ , passed as an [`int`](https://docs.python.org/3/library/functions.html#int "int") (0–6)
Identical to setting the [`firstweekday`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.firstweekday "calendar.Calendar.firstweekday") property.

iterweekdays()[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.iterweekdays "Link to this definition")

Return an iterator for the week day numbers that will be used for one week. The first value from the iterator will be the same as the value of the [`firstweekday`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.firstweekday "calendar.Calendar.firstweekday") property.

itermonthdates(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdates "Link to this definition")

Return an iterator for the month _month_ (1–12) in the year _year_. This iterator will return all days (as [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects) for the month and all days before the start of the month or after the end of the month that are required to get a complete week.

itermonthdays(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdays "Link to this definition")

Return an iterator for the month _month_ in the year _year_ similar to [`itermonthdates()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdates "calendar.Calendar.itermonthdates"), but not restricted by the [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") range. Days returned will simply be day of the month numbers. For the days outside of the specified month, the day number is `0`.

itermonthdays2(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdays2 "Link to this definition")

Return an iterator for the month _month_ in the year _year_ similar to [`itermonthdates()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdates "calendar.Calendar.itermonthdates"), but not restricted by the [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") range. Days returned will be tuples consisting of a day of the month number and a week day number.

itermonthdays3(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdays3 "Link to this definition")

Return an iterator for the month _month_ in the year _year_ similar to [`itermonthdates()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdates "calendar.Calendar.itermonthdates"), but not restricted by the [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") range. Days returned will be tuples consisting of a year, a month and a day of the month numbers.
Added in version 3.7.

itermonthdays4(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdays4 "Link to this definition")

Return an iterator for the month _month_ in the year _year_ similar to [`itermonthdates()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.itermonthdates "calendar.Calendar.itermonthdates"), but not restricted by the [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") range. Days returned will be tuples consisting of a year, a month, a day of the month, and a day of the week numbers.
Added in version 3.7.

monthdatescalendar(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.monthdatescalendar "Link to this definition")

Return a list of the weeks in the month _month_ of the _year_ as full weeks. Weeks are lists of seven [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects.

monthdays2calendar(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.monthdays2calendar "Link to this definition")

Return a list of the weeks in the month _month_ of the _year_ as full weeks. Weeks are lists of seven tuples of day numbers and weekday numbers.

monthdayscalendar(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.monthdayscalendar "Link to this definition")

Return a list of the weeks in the month _month_ of the _year_ as full weeks. Weeks are lists of seven day numbers.

yeardatescalendar(_year_ , _width =3_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.yeardatescalendar "Link to this definition")

Return the data for the specified year ready for formatting. The return value is a list of month rows. Each month row contains up to _width_ months (defaulting to 3). Each month contains between 4 and 6 weeks and each week contains 1–7 days. Days are [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects.

yeardays2calendar(_year_ , _width =3_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.yeardays2calendar "Link to this definition")

Return the data for the specified year ready for formatting (similar to [`yeardatescalendar()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.yeardatescalendar "calendar.Calendar.yeardatescalendar")). Entries in the week lists are tuples of day numbers and weekday numbers. Day numbers outside this month are zero.

yeardayscalendar(_year_ , _width =3_)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.yeardayscalendar "Link to this definition")

Return the data for the specified year ready for formatting (similar to [`yeardatescalendar()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.yeardatescalendar "calendar.Calendar.yeardatescalendar")). Entries in the week lists are day numbers. Day numbers outside this month are zero.

_class_ calendar.TextCalendar(_firstweekday =0_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar "Link to this definition")

This class can be used to generate plain text calendars.
`TextCalendar` instances have the following methods:

formatday(_theday_ , _weekday_ , _width_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatday "Link to this definition")

Return a string representing a single day formatted with the given _width_. If _theday_ is `0`, return a string of spaces of the specified width, representing an empty day. The _weekday_ parameter is unused.

formatweek(_theweek_ , _w =0_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatweek "Link to this definition")

Return a single week in a string with no newline. If _w_ is provided, it specifies the width of the date columns, which are centered. Depends on the first weekday as specified in the constructor or set by the [`setfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday "calendar.setfirstweekday") method.

formatweekday(_weekday_ , _width_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatweekday "Link to this definition")

Return a string representing the name of a single weekday formatted to the specified _width_. The _weekday_ parameter is an integer representing the day of the week, where `0` is Monday and `6` is Sunday.

formatweekheader(_width_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatweekheader "Link to this definition")

Return a string containing the header row of weekday names, formatted with the given _width_ for each column. The names depend on the locale settings and are padded to the specified width.

formatmonth(_theyear_ , _themonth_ , _w =0_, _l =0_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatmonth "Link to this definition")

Return a month’s calendar in a multi-line string. If _w_ is provided, it specifies the width of the date columns, which are centered. If _l_ is given, it specifies the number of lines that each week will use. Depends on the first weekday as specified in the constructor or set by the [`setfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday "calendar.setfirstweekday") method.

formatmonthname(_theyear_ , _themonth_ , _width =0_, _withyear =True_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatmonthname "Link to this definition")

Return a string representing the month’s name centered within the specified _width_. If _withyear_ is `True`, include the year in the output. The _theyear_ and _themonth_ parameters specify the year and month for the name to be formatted respectively.

prmonth(_theyear_ , _themonth_ , _w =0_, _l =0_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.prmonth "Link to this definition")

Print a month’s calendar as returned by [`formatmonth()`](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatmonth "calendar.TextCalendar.formatmonth").

formatyear(_theyear_ , _w =2_, _l =1_, _c =6_, _m =3_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatyear "Link to this definition")

Return a _m_ -column calendar for an entire year as a multi-line string. Optional parameters _w_ , _l_ , and _c_ are for date column width, lines per week, and number of spaces between month columns, respectively. Depends on the first weekday as specified in the constructor or set by the [`setfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday "calendar.setfirstweekday") method. The earliest year for which a calendar can be generated is platform-dependent.

pryear(_theyear_ , _w =2_, _l =1_, _c =6_, _m =3_)[¶](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.pryear "Link to this definition")

Print the calendar for an entire year as returned by [`formatyear()`](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatyear "calendar.TextCalendar.formatyear").

_class_ calendar.HTMLCalendar(_firstweekday =0_)[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar "Link to this definition")

This class can be used to generate HTML calendars.
`HTMLCalendar` instances have the following methods:

formatmonth(_theyear_ , _themonth_ , _withyear =True_)[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.formatmonth "Link to this definition")

Return a month’s calendar as an HTML table. If _withyear_ is true the year will be included in the header, otherwise just the month name will be used.

formatyear(_theyear_ , _width =3_)[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.formatyear "Link to this definition")

Return a year’s calendar as an HTML table. _width_ (defaulting to 3) specifies the number of months per row.

formatyearpage(_theyear_ , _width =3_, _css ='calendar.css'_, _encoding =None_)[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.formatyearpage "Link to this definition")

Return a year’s calendar as a complete HTML page. _width_ (defaulting to 3) specifies the number of months per row. _css_ is the name for the cascading style sheet to be used. [`None`](https://docs.python.org/3/library/constants.html#None "None") can be passed if no style sheet should be used. _encoding_ specifies the encoding to be used for the output (defaulting to the system default encoding).

formatmonthname(_theyear_ , _themonth_ , _withyear =True_)[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.formatmonthname "Link to this definition")

Return a month name as an HTML table row. If _withyear_ is true the year will be included in the row, otherwise just the month name will be used.
`HTMLCalendar` has the following attributes you can override to customize the CSS classes used by the calendar:

cssclasses[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.cssclasses "Link to this definition")

A list of CSS classes used for each weekday. The default class list is:
Copy```
cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

```

more styles can be added for each day:
Copy```
cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun red"]

```

Note that the length of this list must be seven items.

cssclass_noday[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.cssclass_noday "Link to this definition")

The CSS class for a weekday occurring in the previous or coming month.
Added in version 3.7.

cssclasses_weekday_head[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.cssclasses_weekday_head "Link to this definition")

A list of CSS classes used for weekday names in the header row. The default is the same as [`cssclasses`](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.cssclasses "calendar.HTMLCalendar.cssclasses").
Added in version 3.7.

cssclass_month_head[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.cssclass_month_head "Link to this definition")

The month’s head CSS class (used by [`formatmonthname()`](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.formatmonthname "calendar.HTMLCalendar.formatmonthname")). The default value is `"month"`.
Added in version 3.7.

cssclass_month[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.cssclass_month "Link to this definition")

The CSS class for the whole month’s table (used by [`formatmonth()`](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.formatmonth "calendar.HTMLCalendar.formatmonth")). The default value is `"month"`.
Added in version 3.7.

cssclass_year[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.cssclass_year "Link to this definition")

The CSS class for the whole year’s table of tables (used by [`formatyear()`](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.formatyear "calendar.HTMLCalendar.formatyear")). The default value is `"year"`.
Added in version 3.7.

cssclass_year_head[¶](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.cssclass_year_head "Link to this definition")

The CSS class for the table head for the whole year (used by [`formatyear()`](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar.formatyear "calendar.HTMLCalendar.formatyear")). The default value is `"year"`.
Added in version 3.7.
Note that although the naming for the above described class attributes is singular (e.g. `cssclass_month` `cssclass_noday`), one can replace the single CSS class with a space separated list of CSS classes, for example:
Copy```
"text-bold text-red"

```

Here is an example how `HTMLCalendar` can be customized:
Copy```
class CustomHTMLCal(calendar.HTMLCalendar):
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"

```


_class_ calendar.LocaleTextCalendar(_firstweekday =0_, _locale =None_)[¶](https://docs.python.org/3/library/calendar.html#calendar.LocaleTextCalendar "Link to this definition")

This subclass of [`TextCalendar`](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar "calendar.TextCalendar") can be passed a locale name in the constructor and will return month and weekday names in the specified locale.

_class_ calendar.LocaleHTMLCalendar(_firstweekday =0_, _locale =None_)[¶](https://docs.python.org/3/library/calendar.html#calendar.LocaleHTMLCalendar "Link to this definition")

This subclass of [`HTMLCalendar`](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar "calendar.HTMLCalendar") can be passed a locale name in the constructor and will return month and weekday names in the specified locale.
Note
The constructor, `formatweekday()` and `formatmonthname()` methods of these two classes temporarily change the `LC_TIME` locale to the given _locale_. Because the current locale is a process-wide setting, they are not thread-safe.
For simple text calendars this module provides the following functions.

calendar.setfirstweekday(_weekday_)[¶](https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday "Link to this definition")

Sets the weekday (`0` is Monday, `6` is Sunday) to start each week. The values [`MONDAY`](https://docs.python.org/3/library/calendar.html#calendar.MONDAY "calendar.MONDAY"), [`TUESDAY`](https://docs.python.org/3/library/calendar.html#calendar.TUESDAY "calendar.TUESDAY"), [`WEDNESDAY`](https://docs.python.org/3/library/calendar.html#calendar.WEDNESDAY "calendar.WEDNESDAY"), [`THURSDAY`](https://docs.python.org/3/library/calendar.html#calendar.THURSDAY "calendar.THURSDAY"), [`FRIDAY`](https://docs.python.org/3/library/calendar.html#calendar.FRIDAY "calendar.FRIDAY"), [`SATURDAY`](https://docs.python.org/3/library/calendar.html#calendar.SATURDAY "calendar.SATURDAY"), and [`SUNDAY`](https://docs.python.org/3/library/calendar.html#calendar.SUNDAY "calendar.SUNDAY") are provided for convenience. For example, to set the first weekday to Sunday:
Copy```
import calendar
calendar.setfirstweekday(calendar.SUNDAY)

```


calendar.firstweekday()[¶](https://docs.python.org/3/library/calendar.html#calendar.firstweekday "Link to this definition")

Returns the current setting for the weekday to start each week.

calendar.isleap(_year_)[¶](https://docs.python.org/3/library/calendar.html#calendar.isleap "Link to this definition")

Returns [`True`](https://docs.python.org/3/library/constants.html#True "True") if _year_ is a leap year, otherwise [`False`](https://docs.python.org/3/library/constants.html#False "False").

calendar.leapdays(_y1_ , _y2_)[¶](https://docs.python.org/3/library/calendar.html#calendar.leapdays "Link to this definition")

Returns the number of leap years in the range from _y1_ to _y2_ (exclusive), where _y1_ and _y2_ are years.
This function works for ranges spanning a century change.

calendar.weekday(_year_ , _month_ , _day_)[¶](https://docs.python.org/3/library/calendar.html#calendar.weekday "Link to this definition")

Returns the day of the week (`0` is Monday) for _year_ (`1970`–…), _month_ (`1`–`12`), _day_ (`1`–`31`).

calendar.weekheader(_n_)[¶](https://docs.python.org/3/library/calendar.html#calendar.weekheader "Link to this definition")

Return a header containing abbreviated weekday names. _n_ specifies the width in characters for one weekday.

calendar.monthrange(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.monthrange "Link to this definition")

Returns weekday of first day of the month and number of days in month, for the specified _year_ and _month_.

calendar.monthcalendar(_year_ , _month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.monthcalendar "Link to this definition")

Returns a matrix representing a month’s calendar. Each row represents a week; days outside of the month are represented by zeros. Each week begins with Monday unless set by [`setfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday "calendar.setfirstweekday").

calendar.prmonth(_theyear_ , _themonth_ , _w =0_, _l =0_)[¶](https://docs.python.org/3/library/calendar.html#calendar.prmonth "Link to this definition")

Prints a month’s calendar as returned by [`month()`](https://docs.python.org/3/library/calendar.html#calendar.month "calendar.month").

calendar.month(_theyear_ , _themonth_ , _w =0_, _l =0_)[¶](https://docs.python.org/3/library/calendar.html#calendar.month "Link to this definition")

Returns a month’s calendar in a multi-line string using the [`formatmonth()`](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatmonth "calendar.TextCalendar.formatmonth") of the [`TextCalendar`](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar "calendar.TextCalendar") class.

calendar.prcal(_year_ , _w =0_, _l =0_, _c =6_, _m =3_)[¶](https://docs.python.org/3/library/calendar.html#calendar.prcal "Link to this definition")

Prints the calendar for an entire year as returned by [`calendar()`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.").

calendar.calendar(_year_ , _w =2_, _l =1_, _c =6_, _m =3_)[¶](https://docs.python.org/3/library/calendar.html#calendar.calendar "Link to this definition")

Returns a 3-column calendar for an entire year as a multi-line string using the [`formatyear()`](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar.formatyear "calendar.TextCalendar.formatyear") of the [`TextCalendar`](https://docs.python.org/3/library/calendar.html#calendar.TextCalendar "calendar.TextCalendar") class.

calendar.timegm(_tuple_)[¶](https://docs.python.org/3/library/calendar.html#calendar.timegm "Link to this definition")

An unrelated but handy function that takes a time tuple such as returned by the [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime") function in the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") module, and returns the corresponding Unix timestamp value, assuming an epoch of 1970, and the POSIX encoding. In fact, `time.gmtime()` and `timegm()` are each others’ inverse.
The `calendar` module exports the following data attributes:

calendar.day_name[¶](https://docs.python.org/3/library/calendar.html#calendar.day_name "Link to this definition")

A sequence that represents the days of the week in the current locale, where Monday is day number 0.
Copy```
>>> import calendar
>>> list(calendar.day_name)
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

```


calendar.day_abbr[¶](https://docs.python.org/3/library/calendar.html#calendar.day_abbr "Link to this definition")

A sequence that represents the abbreviated days of the week in the current locale, where Mon is day number 0.
Copy```
>>> import calendar
>>> list(calendar.day_abbr)
['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

```


calendar.MONDAY[¶](https://docs.python.org/3/library/calendar.html#calendar.MONDAY "Link to this definition")


calendar.TUESDAY[¶](https://docs.python.org/3/library/calendar.html#calendar.TUESDAY "Link to this definition")


calendar.WEDNESDAY[¶](https://docs.python.org/3/library/calendar.html#calendar.WEDNESDAY "Link to this definition")


calendar.THURSDAY[¶](https://docs.python.org/3/library/calendar.html#calendar.THURSDAY "Link to this definition")


calendar.FRIDAY[¶](https://docs.python.org/3/library/calendar.html#calendar.FRIDAY "Link to this definition")


calendar.SATURDAY[¶](https://docs.python.org/3/library/calendar.html#calendar.SATURDAY "Link to this definition")


calendar.SUNDAY[¶](https://docs.python.org/3/library/calendar.html#calendar.SUNDAY "Link to this definition")

Aliases for the days of the week, where `MONDAY` is `0` and `SUNDAY` is `6`.
Added in version 3.12.

_class_ calendar.Day[¶](https://docs.python.org/3/library/calendar.html#calendar.Day "Link to this definition")

Enumeration defining days of the week as integer constants. The members of this enumeration are exported to the module scope as [`MONDAY`](https://docs.python.org/3/library/calendar.html#calendar.MONDAY "calendar.MONDAY") through [`SUNDAY`](https://docs.python.org/3/library/calendar.html#calendar.SUNDAY "calendar.SUNDAY").
Added in version 3.12.

calendar.month_name[¶](https://docs.python.org/3/library/calendar.html#calendar.month_name "Link to this definition")

A sequence that represents the months of the year in the current locale. This follows normal convention of January being month number 1, so it has a length of 13 and `month_name[0]` is the empty string.
Copy```
>>> import calendar
>>> list(calendar.month_name)
['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

```


calendar.month_abbr[¶](https://docs.python.org/3/library/calendar.html#calendar.month_abbr "Link to this definition")

A sequence that represents the abbreviated months of the year in the current locale. This follows normal convention of January being month number 1, so it has a length of 13 and `month_abbr[0]` is the empty string.
Copy```
>>> import calendar
>>> list(calendar.month_abbr)
['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

```


calendar.JANUARY[¶](https://docs.python.org/3/library/calendar.html#calendar.JANUARY "Link to this definition")


calendar.FEBRUARY[¶](https://docs.python.org/3/library/calendar.html#calendar.FEBRUARY "Link to this definition")


calendar.MARCH[¶](https://docs.python.org/3/library/calendar.html#calendar.MARCH "Link to this definition")


calendar.APRIL[¶](https://docs.python.org/3/library/calendar.html#calendar.APRIL "Link to this definition")


calendar.MAY[¶](https://docs.python.org/3/library/calendar.html#calendar.MAY "Link to this definition")


calendar.JUNE[¶](https://docs.python.org/3/library/calendar.html#calendar.JUNE "Link to this definition")


calendar.JULY[¶](https://docs.python.org/3/library/calendar.html#calendar.JULY "Link to this definition")


calendar.AUGUST[¶](https://docs.python.org/3/library/calendar.html#calendar.AUGUST "Link to this definition")


calendar.SEPTEMBER[¶](https://docs.python.org/3/library/calendar.html#calendar.SEPTEMBER "Link to this definition")


calendar.OCTOBER[¶](https://docs.python.org/3/library/calendar.html#calendar.OCTOBER "Link to this definition")


calendar.NOVEMBER[¶](https://docs.python.org/3/library/calendar.html#calendar.NOVEMBER "Link to this definition")


calendar.DECEMBER[¶](https://docs.python.org/3/library/calendar.html#calendar.DECEMBER "Link to this definition")

Aliases for the months of the year, where `JANUARY` is `1` and `DECEMBER` is `12`.
Added in version 3.12.

_class_ calendar.Month[¶](https://docs.python.org/3/library/calendar.html#calendar.Month "Link to this definition")

Enumeration defining months of the year as integer constants. The members of this enumeration are exported to the module scope as [`JANUARY`](https://docs.python.org/3/library/calendar.html#calendar.JANUARY "calendar.JANUARY") through [`DECEMBER`](https://docs.python.org/3/library/calendar.html#calendar.DECEMBER "calendar.DECEMBER").
Added in version 3.12.
The `calendar` module defines the following exceptions:

_exception_ calendar.IllegalMonthError(_month_)[¶](https://docs.python.org/3/library/calendar.html#calendar.IllegalMonthError "Link to this definition")

A subclass of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"), raised when the given month number is outside of the range 1-12 (inclusive).

month[¶](https://docs.python.org/3/library/calendar.html#calendar.IllegalMonthError.month "Link to this definition")

The invalid month number.

_exception_ calendar.IllegalWeekdayError(_weekday_)[¶](https://docs.python.org/3/library/calendar.html#calendar.IllegalWeekdayError "Link to this definition")

A subclass of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"), raised when the given weekday number is outside of the range 0-6 (inclusive).

weekday[¶](https://docs.python.org/3/library/calendar.html#calendar.IllegalWeekdayError.weekday "Link to this definition")

The invalid weekday number.
See also

Module [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")

Object-oriented interface to dates and times with similar functionality to the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") module.

Module [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.")

Low-level time related functions.
## Command-line usage[¶](https://docs.python.org/3/library/calendar.html#command-line-usage "Link to this heading")
Added in version 2.5.
The `calendar` module can be executed as a script from the command line to interactively print a calendar.
```
python -m calendar [-h] [-L LOCALE] [-e ENCODING] [-t {text,html}]
                   [-w WIDTH] [-l LINES] [-s SPACING] [-m MONTHS] [-c CSS]
                   [-f FIRST_WEEKDAY] [year] [month]

```

For example, to print a calendar for the year 2000:
Copy```
$ python -m calendar 2000
                                  2000

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6             1  2  3  4  5
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       6  7  8  9 10 11 12
10 11 12 13 14 15 16      14 15 16 17 18 19 20      13 14 15 16 17 18 19
17 18 19 20 21 22 23      21 22 23 24 25 26 27      20 21 22 23 24 25 26
24 25 26 27 28 29 30      28 29                     27 28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31

```

The following options are accepted:

--help, -h[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-help "Link to this definition")

Show the help message and exit.

--locale LOCALE, -L LOCALE[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-locale "Link to this definition")

The locale to use for month and weekday names. Defaults to English.

--encoding ENCODING, -e ENCODING[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-encoding "Link to this definition")

The encoding to use for output. [`--encoding`](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-encoding) is required if [`--locale`](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-locale) is set.

--type {text,html}, -t {text,html}[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-type "Link to this definition")

Print the calendar to the terminal as text, or as an HTML document.

--first-weekday FIRST_WEEKDAY, -f FIRST_WEEKDAY[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-first-weekday "Link to this definition")

The weekday to start each week. Must be a number between 0 (Monday) and 6 (Sunday). Defaults to 0.
Added in version 3.13.

year[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-arg-year "Link to this definition")

The year to print the calendar for. Defaults to the current year.

month[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-arg-month "Link to this definition")

The month of the specified [`year`](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-arg-year) to print the calendar for. Must be a number between 1 and 12, and may only be used in text mode. Defaults to printing a calendar for the full year.
_Text-mode options:_

--width WIDTH, -w WIDTH[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-width "Link to this definition")

The width of the date column in terminal columns. The date is printed centred in the column. Any value lower than 2 is ignored. Defaults to 2.

--lines LINES, -l LINES[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-lines "Link to this definition")

The number of lines for each week in terminal rows. The date is printed top-aligned. Any value lower than 1 is ignored. Defaults to 1.

--spacing SPACING, -s SPACING[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-spacing "Link to this definition")

The space between months in columns. Any value lower than 2 is ignored. Defaults to 6.

--months MONTHS, -m MONTHS[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-months "Link to this definition")

The number of months printed per row. Defaults to 3.
Changed in version 3.14: By default, today’s date is highlighted in color and can be [controlled using environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color).
_HTML-mode options:_

--css CSS, -c CSS[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-css "Link to this definition")

The path of a CSS stylesheet to use for the calendar. This must either be relative to the generated HTML, or an absolute HTTP or `file:///` URL.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`calendar` — General calendar-related functions](https://docs.python.org/3/library/calendar.html)
    * [Command-line usage](https://docs.python.org/3/library/calendar.html#command-line-usage)


#### Previous topic
[`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html "previous chapter")
#### Next topic
[`collections` — Container datatypes](https://docs.python.org/3/library/collections.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=calendar+%E2%80%94+General+calendar-related+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcalendar.html&pagesource=library%2Fcalendar.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/collections.html "collections — Container datatypes") |
  * [previous](https://docs.python.org/3/library/zoneinfo.html "zoneinfo — IANA time zone support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`calendar` — General calendar-related functions](https://docs.python.org/3/library/calendar.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
