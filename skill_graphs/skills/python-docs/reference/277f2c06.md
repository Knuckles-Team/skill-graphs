## Available types[¶](https://docs.python.org/3/library/datetime.html#available-types "Link to this heading")

_class_ datetime.date

An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Attributes: [`year`](https://docs.python.org/3/library/datetime.html#datetime.date.year "datetime.date.year"), [`month`](https://docs.python.org/3/library/datetime.html#datetime.date.month "datetime.date.month"), and [`day`](https://docs.python.org/3/library/datetime.html#datetime.date.day "datetime.date.day").

_class_ datetime.time

An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. (There is no notion of “leap seconds” here.) Attributes: [`hour`](https://docs.python.org/3/library/datetime.html#datetime.time.hour "datetime.time.hour"), [`minute`](https://docs.python.org/3/library/datetime.html#datetime.time.minute "datetime.time.minute"), [`second`](https://docs.python.org/3/library/datetime.html#datetime.time.second "datetime.time.second"), [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond "datetime.time.microsecond"), and [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "datetime.time.tzinfo").

_class_ datetime.datetime

A combination of a date and a time. Attributes: [`year`](https://docs.python.org/3/library/datetime.html#datetime.datetime.year "datetime.datetime.year"), [`month`](https://docs.python.org/3/library/datetime.html#datetime.datetime.month "datetime.datetime.month"), [`day`](https://docs.python.org/3/library/datetime.html#datetime.datetime.day "datetime.datetime.day"), [`hour`](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour "datetime.datetime.hour"), [`minute`](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute "datetime.datetime.minute"), [`second`](https://docs.python.org/3/library/datetime.html#datetime.datetime.second "datetime.datetime.second"), [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond "datetime.datetime.microsecond"), and [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo").

_class_ datetime.timedelta

A duration expressing the difference between two [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") or [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") instances to microsecond resolution.

_class_ datetime.tzinfo

An abstract base class for time zone information objects. These are used by the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") classes to provide a customizable notion of time adjustment (for example, to account for time zone and/or daylight saving time).

_class_ datetime.timezone

A class that implements the [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") abstract base class as a fixed offset from the UTC.
Added in version 3.2.
Objects of these types are immutable.
Subclass relationships:
![timedelta, tzinfo, time, and date inherit from object; timezone inherits from tzinfo; and datetime inherits from date.](https://docs.python.org/3/_images/datetime-inheritance.svg)
### Common properties[¶](https://docs.python.org/3/library/datetime.html#common-properties "Link to this heading")
The [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date"), [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"), [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time"), and [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") types share these common features:
  * Objects of these types are immutable.
  * Objects of these types are [hashable](https://docs.python.org/3/glossary.html#term-hashable), meaning that they can be used as dictionary keys.
  * Objects of these types support efficient pickling via the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module.


### Determining if an object is aware or naive[¶](https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive "Link to this heading")
Objects of the [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") type are always naive.
An object of type [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") or [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") may be aware or naive.
A [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object `d` is aware if both of the following hold:
  1. `d.tzinfo` is not `None`
  2. `d.tzinfo.utcoffset(d)` does not return `None`


Otherwise, `d` is naive.
A [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object `t` is aware if both of the following hold:
  1. `t.tzinfo` is not `None`
  2. `t.tzinfo.utcoffset(None)` does not return `None`.


Otherwise, `t` is naive.
The distinction between aware and naive doesn’t apply to [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") objects.
