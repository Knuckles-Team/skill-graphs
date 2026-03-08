##  `django.utils.dateparse`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.dateparse "Link to this heading")
The functions defined in this module share the following properties:
  * They accept strings in ISO 8601 date/time formats (or some close alternatives) and return objects from the corresponding classes in Python’s
  * They raise
  * They return `None` if it isn’t well formatted at all.
  * They accept up to picosecond resolution in input, but they truncate it to microseconds, since that’s what Python supports.



parse_date(_value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/dateparse/#parse_date)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.dateparse.parse_date "Link to this definition")

Parses a string and returns a

parse_time(_value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/dateparse/#parse_time)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.dateparse.parse_time "Link to this definition")

Parses a string and returns a
UTC offsets aren’t supported; if `value` describes one, the result is `None`.

parse_datetime(_value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/dateparse/#parse_datetime)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.dateparse.parse_datetime "Link to this definition")

Parses a string and returns a
UTC offsets are supported; if `value` describes one, the result’s `tzinfo` attribute is a

parse_duration(_value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/dateparse/#parse_duration)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.dateparse.parse_duration "Link to this definition")

Parses a string and returns a
Expects data in the format `"DD HH:MM:SS.uuuuuu"`, `"DD HH:MM:SS,uuuuuu"`, or as specified by ISO 8601 (e.g. `P4DT1H15M20S` which is equivalent to `4 1:15:20`) or PostgreSQL’s day-time interval format (e.g. `3 days 04:05:06`).
