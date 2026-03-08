##  `django.utils.timezone`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.timezone "Link to this heading")

get_fixed_timezone(_offset_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#get_fixed_timezone)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.get_fixed_timezone "Link to this definition")

Returns a
`offset` is a

get_default_timezone()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#get_default_timezone)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.get_default_timezone "Link to this definition")

Returns a [default time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).

get_default_timezone_name()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#get_default_timezone_name)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.get_default_timezone_name "Link to this definition")

Returns the name of the [default time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).

get_current_timezone()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#get_current_timezone)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.get_current_timezone "Link to this definition")

Returns a [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).

get_current_timezone_name()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#get_current_timezone_name)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.get_current_timezone_name "Link to this definition")

Returns the name of the [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).

activate(_timezone_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#activate)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.activate "Link to this definition")

Sets the [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone). The `timezone` argument must be an instance of a

deactivate()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#deactivate)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.deactivate "Link to this definition")

Unsets the [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).

override(_timezone_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#override)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.override "Link to this definition")

This is a Python context manager that sets the [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone) on entry with [`activate()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.activate "django.utils.timezone.activate"), and restores the previously active time zone on exit. If the `timezone` argument is `None`, the [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone) is unset on entry with [`deactivate()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.deactivate "django.utils.timezone.deactivate") instead.
`override` is also usable as a function decorator.

localtime(_value =None_, _timezone =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#localtime)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.localtime "Link to this definition")

Converts an aware [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).
When `value` is omitted, it defaults to [`now()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.now "django.utils.timezone.now").
This function doesn’t work on naive datetimes; use [`make_aware()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.make_aware "django.utils.timezone.make_aware") instead.

localdate(_value =None_, _timezone =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#localdate)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.localdate "Link to this definition")

Uses [`localtime()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.localtime "django.utils.timezone.localtime") to convert an aware [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).
When `value` is omitted, it defaults to [`now()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.now "django.utils.timezone.now").
This function doesn’t work on naive datetimes.

now()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#now)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.now "Link to this definition")

Returns a [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ):
  * If [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is `False`, this will be a [naive](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#naive-vs-aware-datetimes) datetime (i.e. a datetime without an associated timezone) that represents the current time in the system’s local timezone.
  * If [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is `True`, this will be an [aware](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#naive-vs-aware-datetimes) datetime representing the current time in UTC. Note that [`now()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.now "django.utils.timezone.now") will always return times in UTC regardless of the value of [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE); you can use [`localtime()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.localtime "django.utils.timezone.localtime") to get the time in the current time zone.



is_aware(_value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#is_aware)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.is_aware "Link to this definition")

Returns `True` if `value` is aware, `False` if it is naive. This function assumes that `value` is a

is_naive(_value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#is_naive)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.is_naive "Link to this definition")

Returns `True` if `value` is naive, `False` if it is aware. This function assumes that `value` is a

make_aware(_value_ , _timezone =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#make_aware)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.make_aware "Link to this definition")

Returns an aware `value` in `timezone`, `value` being a naive `timezone` is set to `None`, it defaults to the [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).

make_naive(_value_ , _timezone =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/timezone/#make_naive)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.timezone.make_naive "Link to this definition")

Returns a naive `timezone` the same point in time as `value`, `value` being an aware `timezone` is set to `None`, it defaults to the [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone).
