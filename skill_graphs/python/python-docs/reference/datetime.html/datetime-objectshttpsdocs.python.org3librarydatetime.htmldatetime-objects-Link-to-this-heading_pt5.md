  6. For a naive object, the `%z`, `%:z` and `%Z` format codes are replaced by empty strings.
For an aware object:

`%z`

[`utcoffset()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcoffset "datetime.datetime.utcoffset") is transformed into a string of the form `±HHMM[SS[.ffffff]]`, where `HH` is a 2-digit string giving the number of UTC offset hours, `MM` is a 2-digit string giving the number of UTC offset minutes, `SS` is a 2-digit string giving the number of UTC offset seconds and `ffffff` is a 6-digit string giving the number of UTC offset microseconds. The `ffffff` part is omitted when the offset is a whole number of seconds and both the `ffffff` and the `SS` part is omitted when the offset is a whole number of minutes. For example, if `utcoffset()` returns `timedelta(hours=-3, minutes=-30)`, `%z` is replaced with the string `'-0330'`.
Changed in version 3.7: The UTC offset is not restricted to a whole number of minutes.
Changed in version 3.7: When the `%z` directive is provided to the [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") method, the UTC offsets can have a colon as a separator between hours, minutes and seconds. For example, `'+01:00:00'` will be parsed as an offset of one hour. In addition, providing `'Z'` is identical to `'+00:00'`.

`%:z`

Behaves exactly as `%z`, but has a colon separator added between hours, minutes and seconds.

`%Z`

In [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime"), `%Z` is replaced by an empty string if [`tzname()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzname "datetime.datetime.tzname") returns `None`; otherwise `%Z` is replaced by the returned value, which must be a string.
[`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") only accepts certain values for `%Z`:
    1. any value in `time.tzname` for your machine’s locale
    2. the hard-coded values `UTC` and `GMT`
So someone living in Japan may have `JST`, `UTC`, and `GMT` as valid values, but probably not `EST`. It will raise `ValueError` for invalid values.
Changed in version 3.2: When the `%z` directive is provided to the [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") method, an aware [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object will be produced. The `tzinfo` of the result will be set to a [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") instance.
  7. When used with the [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") method, `%U` and `%W` are only used in calculations when the day of the week and the calendar year (`%Y`) are specified.
  8. Similar to `%U` and `%W`, `%V` is only used in calculations when the day of the week and the ISO year (`%G`) are specified in a [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") format string. Also note that `%G` and `%Y` are not interchangeable.
  9. When used with the [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") method, the leading zero is optional for formats `%d`, `%m`, `%H`, `%I`, `%M`, `%S`, `%j`, `%U`, `%W`, and `%V`. Format `%y` does require a leading zero.
  10. When parsing a month and day using [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime"), always include a year in the format. If the value you need to parse lacks a year, append an explicit dummy leap year. Otherwise your code will raise an exception when it encounters leap day because the default year used by the parser (1900) is not a leap year. Users run into that bug every leap year.
Copy```
>>> month_day = "02/29"
>>> dt.datetime.strptime(f"{month_day};1984", "%m/%d;%Y")  # No leap year bug.
datetime.datetime(1984, 2, 29, 0, 0)

```

Deprecated since version 3.13, will be removed in version 3.15: [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") calls using a format string containing a day of month without a year now emit a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). In 3.15 or later we may change this into an error or change the default year to a leap year. See


Footnotes
[[1](https://docs.python.org/3/library/datetime.html#id1)]
If, that is, we ignore the effects of relativity.
[[2](https://docs.python.org/3/library/datetime.html#id2)]
This matches the definition of the “proleptic Gregorian” calendar in Dershowitz and Reingold’s book _Calendrical Calculations_ , where it’s the base calendar for all computations. See the book for algorithms for converting between proleptic Gregorian ordinals and many other calendar systems.
[[3](https://docs.python.org/3/library/datetime.html#id3)]
See R. H. van Gent’s
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`datetime` — Basic date and time types](https://docs.python.org/3/library/datetime.html)
    * [Aware and naive objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects)
    * [Constants](https://docs.python.org/3/library/datetime.html#constants)
    * [Available types](https://docs.python.org/3/library/datetime.html#available-types)
      * [Common properties](https://docs.python.org/3/library/datetime.html#common-properties)
      * [Determining if an object is aware or naive](https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive)
    * [`timedelta` objects](https://docs.python.org/3/library/datetime.html#timedelta-objects)
      * [Examples of usage: `timedelta`](https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta)
    * [`date` objects](https://docs.python.org/3/library/datetime.html#date-objects)
      * [Examples of usage: `date`](https://docs.python.org/3/library/datetime.html#examples-of-usage-date)
    * [`datetime` objects](https://docs.python.org/3/library/datetime.html#datetime-objects)
      * [Examples of usage: `datetime`](https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime)
    * [`time` objects](https://docs.python.org/3/library/datetime.html#time-objects)
      * [Examples of usage: `time`](https://docs.python.org/3/library/datetime.html#examples-of-usage-time)
    * [`tzinfo` objects](https://docs.python.org/3/library/datetime.html#tzinfo-objects)
    * [`timezone` objects](https://docs.python.org/3/library/datetime.html#timezone-objects)
    * [`strftime()` and `strptime()` behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
      * [`strftime()` and `strptime()` format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
      * [Technical detail](https://docs.python.org/3/library/datetime.html#technical-detail)


#### Previous topic
[Data Types](https://docs.python.org/3/library/datatypes.html "previous chapter")
#### Next topic
[`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=datetime+%E2%80%94+Basic+date+and+time+types&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdatetime.html&pagesource=library%2Fdatetime.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/zoneinfo.html "zoneinfo — IANA time zone support") |
  * [previous](https://docs.python.org/3/library/datatypes.html "Data Types") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Types](https://docs.python.org/3/library/datatypes.html) »
  * [`datetime` — Basic date and time types](https://docs.python.org/3/library/datetime.html#time-objects)
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
