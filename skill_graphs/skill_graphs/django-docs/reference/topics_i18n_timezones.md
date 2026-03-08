[Skip to main content](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#main-content)
[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.
Menu Main navigation
  * [Overview](https://www.djangoproject.com/start/overview/)
  * [Download](https://www.djangoproject.com/download/)
  * [Documentation](https://docs.djangoproject.com/)
  * [News](https://www.djangoproject.com/weblog/)
  * [Issues](https://code.djangoproject.com/)
  * [Community](https://www.djangoproject.com/community/)
  * [Foundation](https://www.djangoproject.com/foundation/)
  * [♥ Donate](https://www.djangoproject.com/fundraising/)


Search Submit
Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
Toggle Light / Dark / Auto color theme
[Documentation](https://docs.djangoproject.com/en/6.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/6.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/topics/i18n/timezones/)
  * [sv](https://docs.djangoproject.com/sv/6.0/topics/i18n/timezones/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/topics/i18n/timezones/)
  * [pl](https://docs.djangoproject.com/pl/6.0/topics/i18n/timezones/)
  * [ko](https://docs.djangoproject.com/ko/6.0/topics/i18n/timezones/)
  * [ja](https://docs.djangoproject.com/ja/6.0/topics/i18n/timezones/)
  * [it](https://docs.djangoproject.com/it/6.0/topics/i18n/timezones/)
  * [id](https://docs.djangoproject.com/id/6.0/topics/i18n/timezones/)
  * [fr](https://docs.djangoproject.com/fr/6.0/topics/i18n/timezones/)
  * [es](https://docs.djangoproject.com/es/6.0/topics/i18n/timezones/)
  * [el](https://docs.djangoproject.com/el/6.0/topics/i18n/timezones/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/i18n/timezones/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/i18n/timezones/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/i18n/timezones/)
  * [5.0](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/i18n/timezones/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/i18n/timezones/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/i18n/timezones/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/i18n/timezones/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/i18n/timezones/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/i18n/timezones/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/i18n/timezones/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/i18n/timezones/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/i18n/timezones/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/i18n/timezones/)


  * [](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#top)


# Time zones[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zones "Link to this heading")
## Overview[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#overview "Link to this heading")
When support for time zones is enabled, Django stores datetime information in UTC in the database, uses time-zone-aware datetime objects internally, and converts them to the end user’s time zone in forms. Templates will use the [default time zone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-current-time-zone), but this can be updated to the end user’s time zone through the use of [filters and tags](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zones-in-templates).
This is handy if your users live in more than one time zone and you want to display datetime information according to each user’s wall clock.
Even if your website is available in only one time zone, it’s still good practice to store data in UTC in your database. The main reason is daylight saving time (DST). Many countries have a system of DST, where clocks are moved forward in spring and backward in autumn. If you’re working in local time, you’re likely to encounter errors twice a year, when the transitions happen. This probably doesn’t matter for your blog, but it’s a problem if you over bill or under bill your customers by one hour, twice a year, every year. The solution to this problem is to use UTC in the code and use local time only when interacting with end users.
Time zone support is enabled by default. To disable it, set [`USE_TZ = False`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) in your settings file.
Time zone support uses
If you’re wrestling with a particular problem, start with the [time zone FAQ](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zones-faq).
## Concepts[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#concepts "Link to this heading")
### Naive and aware datetime objects[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#naive-and-aware-datetime-objects "Link to this heading")
Python’s `tzinfo` attribute that can be used to store time zone information, represented as an instance of a subclass of **aware**. Otherwise, it’s **naive**.
You can use [`is_aware()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.is_aware "django.utils.timezone.is_aware") and [`is_naive()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.is_naive "django.utils.timezone.is_naive") to determine whether datetimes are aware or naive.
When time zone support is disabled, Django uses naive datetime objects in local time. This is sufficient for many use cases. In this mode, to obtain the current time, you would write:
```
import datetime

now = datetime.datetime.now()

```

When time zone support is enabled ([`USE_TZ=True`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ)), Django uses time-zone-aware datetime objects. If your code creates datetime objects, they should be aware too. In this mode, the example above becomes:
```
from django.utils import timezone

now = timezone.now()

```

Warning
Dealing with aware datetime objects isn’t always intuitive. For instance, the `tzinfo` argument of the standard datetime constructor doesn’t work reliably for time zones with DST. Using UTC is generally safe; if you’re using other time zones, you should review the
Note
Python’s `tzinfo` attribute, and PostgreSQL has a matching `time with time zone` type. However, as PostgreSQL’s docs put it, this type “exhibits properties which lead to questionable usefulness”.
Django only supports naive time objects and will raise an exception if you attempt to save an aware time object, as a timezone for a time with no associated date does not make sense.
### Interpretation of naive datetime objects[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#interpretation-of-naive-datetime-objects "Link to this heading")
When [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, Django still accepts naive datetime objects, in order to preserve backwards-compatibility. When the database layer receives one, it attempts to make it aware by interpreting it in the [default time zone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-current-time-zone) and raises a warning.
Unfortunately, during DST transitions, some datetimes don’t exist or are ambiguous. That’s why you should always create aware datetime objects when time zone support is enabled. (See the `fold` attribute to specify the offset that should apply to a datetime during a DST transition.)
In practice, this is rarely an issue. Django gives you aware datetime objects in the models and forms, and most often, new datetime objects are created from existing ones through [`timezone.now()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.now "django.utils.timezone.now") automatically does the right thing.
### Default time zone and current time zone[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-time-zone-and-current-time-zone "Link to this heading")
The **default time zone** is the time zone defined by the [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) setting.
The **current time zone** is the time zone that’s used for rendering.
You should set the current time zone to the end user’s actual time zone with [`activate()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.activate "django.utils.timezone.activate"). Otherwise, the default time zone is used.
Note
As explained in the documentation of [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE), Django sets environment variables so that its process runs in the default time zone. This happens regardless of the value of [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) and of the current time zone.
When [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, this is useful to preserve backwards-compatibility with applications that still rely on local time. However, [as explained above](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#naive-datetime-objects), this isn’t entirely reliable, and you should always work with aware datetimes in UTC in your own code. For instance, use `tz` parameter to
### Selecting the current time zone[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#selecting-the-current-time-zone "Link to this heading")
The current time zone is the equivalent of the current [locale](https://docs.djangoproject.com/en/6.0/topics/i18n/#term-locale-name) for translations. However, there’s no equivalent of the `Accept-Language` HTTP header that Django could use to determine the user’s time zone automatically. Instead, Django provides [time zone selection functions](https://docs.djangoproject.com/en/6.0/ref/utils/#time-zone-selection-functions). Use them to build the time zone selection logic that makes sense for you.
Most websites that care about time zones ask users in which time zone they live and store this information in the user’s profile. For anonymous users, they use the time zone of their primary audience or UTC.
Here’s an example that stores the current timezone in the session. (It skips error handling entirely for the sake of simplicity.)
Add the following middleware to [`MIDDLEWARE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MIDDLEWARE):
```
import zoneinfo

from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get("django_timezone")
        if tzname:
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)

```

Create a view that can set the current timezone:
```
from django.shortcuts import redirect, render

# Prepare a map of common locations to timezone choices you wish to offer.
common_timezones = {
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "New York": "America/New_York",
}


def set_timezone(request):
    if request.method == "POST":
        request.session["django_timezone"] = request.POST["timezone"]
        return redirect("/")
    else:
        return render(request, "template.html", {"timezones": common_timezones})

```

Include a form in `template.html` that will `POST` to this view:
```
{% load tz %}
{% get_current_timezone as TIME_ZONE %}
<form action="{% url 'set_timezone' %}" method="POST">
    {% csrf_token %}
    <label for="timezone">Time zone:</label>
    <select name="timezone">
        {% for city, tz in timezones.items %}
        <option value="{{ tz }}"{% if tz == TIME_ZONE %} selected{% endif %}>{{ city }}</option>
        {% endfor %}
    </select>
    <input type="submit" value="Set">
</form>

```

## Time zone aware input in forms[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zone-aware-input-in-forms "Link to this heading")
When you enable time zone support, Django interprets datetimes entered in forms in the [current time zone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-current-time-zone) and returns aware datetime objects in `cleaned_data`.
Converted datetimes that don’t exist or are ambiguous because they fall in a DST transition will be reported as invalid values.
## Time zone aware output in templates[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zone-aware-output-in-templates "Link to this heading")
When you enable time zone support, Django converts aware datetime objects to the [current time zone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-current-time-zone) when they’re rendered in templates. This behaves very much like [format localization](https://docs.djangoproject.com/en/6.0/topics/i18n/formatting/).
Warning
Django doesn’t convert naive datetime objects, because they could be ambiguous, and because your code should never produce naive datetimes when time zone support is enabled. However, you can force conversion with the template filters described below.
Conversion to local time isn’t always appropriate – you may be generating output for computers rather than for humans. The following filters and tags, provided by the `tz` template tag library, allow you to control the time zone conversions.
### Template tags[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#template-tags "Link to this heading")
####  `localtime`[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#localtime "Link to this heading")
Enables or disables conversion of aware datetime objects to the current time zone in the contained block.
This tag has exactly the same effects as the [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) setting as far as the template engine is concerned. It allows a more fine grained control of conversion.
To activate or deactivate conversion for a template block, use:
```
{% load tz %}

{% localtime on %}
    {{ value }}
{% endlocaltime %}

{% localtime off %}
    {{ value }}
{% endlocaltime %}

```

Note
The value of [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) isn’t respected inside of a `{% localtime %}` block.
####  `timezone`[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#timezone "Link to this heading")
Sets or unsets the current time zone in the contained block. When the current time zone is unset, the default time zone applies.
```
{% load tz %}

{% timezone "Europe/Paris" %}
    Paris time: {{ value }}
{% endtimezone %}

{% timezone None %}
    Server time: {{ value }}
{% endtimezone %}

```

####  `get_current_timezone`[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#get-current-timezone "Link to this heading")
You can get the name of the current time zone using the `get_current_timezone` tag:
```
{% get_current_timezone as TIME_ZONE %}

```

Alternatively, you can activate the [`tz()`](https://docs.djangoproject.com/en/6.0/ref/templates/api/#django.template.context_processors.tz "django.template.context_processors.tz") context processor and use the `TIME_ZONE` context variable.
### Template filters[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#template-filters "Link to this heading")
These filters accept both aware and naive datetimes. For conversion purposes, they assume that naive datetimes are in the default time zone. They always return aware datetimes.
####  `localtime`[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#std-templatefilter-localtime "Link to this heading")
Forces conversion of a single value to the current time zone.
For example:
```
{% load tz %}

{{ value|localtime }}

```

####  `utc`[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#utc "Link to this heading")
Forces conversion of a single value to UTC.
For example:
```
{% load tz %}

{{ value|utc }}

```

####  `timezone`[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#std-templatefilter-timezone "Link to this heading")
Forces conversion of a single value to an arbitrary timezone.
The argument must be an instance of a
For example:
```
{% load tz %}

{{ value|timezone:"Europe/Paris" }}

```

## Migration guide[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#migration-guide "Link to this heading")
Here’s how to migrate a project that was started before Django supported time zones.
### Database[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#database "Link to this heading")
#### PostgreSQL[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#postgresql "Link to this heading")
The PostgreSQL backend stores datetimes as `timestamp with time zone`. In practice, this means it converts datetimes from the connection’s time zone to UTC on storage, and from UTC to the connection’s time zone on retrieval.
As a consequence, if you’re using PostgreSQL, you can switch between `USE_TZ = False` and `USE_TZ = True` freely. The database connection’s time zone will be set to [`DATABASE-TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-TIME_ZONE) or `UTC` respectively, so that Django obtains correct datetimes in all cases. You don’t need to perform any data conversions.
Time zone settings
The [`time zone`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-TIME_ZONE) configured for the connection in the [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) setting is distinct from the general [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) setting.
#### Other databases[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#other-databases "Link to this heading")
Other backends store datetimes without time zone information. If you switch from `USE_TZ = False` to `USE_TZ = True`, you must convert your data from local time to UTC – which isn’t deterministic if your local time has DST.
### Code[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#code "Link to this heading")
The first step is to add [`USE_TZ = True`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) to your settings file. At this point, things should mostly work. If you create naive datetime objects in your code, Django makes them aware when necessary.
However, these conversions may fail around DST transitions, which means you aren’t getting the full benefits of time zone support yet. Also, you’re likely to run into a few problems because it’s impossible to compare a naive datetime with an aware datetime. Since Django now gives you aware datetimes, you’ll get exceptions wherever you compare a datetime that comes from a model or a form with a naive datetime that you’ve created in your code.
So the second step is to refactor your code wherever you instantiate datetime objects to make them aware. This can be done incrementally. [`django.utils.timezone`](https://docs.djangoproject.com/en/6.0/ref/utils/#module-django.utils.timezone "django.utils.timezone: Timezone support.") defines some handy helpers for compatibility code: [`now()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.now "django.utils.timezone.now"), [`is_aware()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.is_aware "django.utils.timezone.is_aware"), [`is_naive()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.is_naive "django.utils.timezone.is_naive"), [`make_aware()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.make_aware "django.utils.timezone.make_aware"), and [`make_naive()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.make_naive "django.utils.timezone.make_naive").
Finally, in order to help you locate code that needs upgrading, Django raises a warning when you attempt to save a naive datetime to the database:
```
RuntimeWarning: DateTimeField ModelName.field_name received a naive
datetime (2012-01-01 00:00:00) while time zone support is active.

```

During development, you can turn such warnings into exceptions and get a traceback by adding the following to your settings file:
```
import warnings

warnings.filterwarnings(
    "error",
    r"DateTimeField .* received a naive datetime",
    RuntimeWarning,
    r"django\.db\.models\.fields",
)

```

### Fixtures[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#fixtures "Link to this heading")
When serializing an aware datetime, the UTC offset is included, like this:
```
"2011-09-01T13:20:30+03:00"

```

While for a naive datetime, it isn’t:
```
"2011-09-01T13:20:30"

```

For models with [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField")s, this difference makes it impossible to write a fixture that works both with and without time zone support.
Fixtures generated with `USE_TZ = False`, or before Django 1.4, use the “naive” format. If your project contains such fixtures, after you enable time zone support, you’ll see
You can regenerate fixtures with [`loaddata`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-loaddata) then [`dumpdata`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-dumpdata). Or, if they’re small enough, you can edit them to add the UTC offset that matches your [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TIME_ZONE) to each serialized datetime.
## FAQ[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#faq "Link to this heading")
### Setup[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#setup "Link to this heading")
  1. **I don’t need multiple time zones. Should I enable time zone support?**
Yes. When time zone support is enabled, Django uses a more accurate model of local time. This shields you from subtle and unreproducible bugs around daylight saving time (DST) transitions.
When you enable time zone support, you’ll encounter some errors because you’re using naive datetimes where Django expects aware datetimes. Such errors show up when running tests. You’ll quickly learn how to avoid invalid operations.
On the other hand, bugs caused by the lack of time zone support are much harder to prevent, diagnose and fix. Anything that involves scheduled tasks or datetime arithmetic is a candidate for subtle bugs that will bite you only once or twice a year.
For these reasons, time zone support is enabled by default in new projects, and you should keep it unless you have a very good reason not to.
  2. **I’ve enabled time zone support. Am I safe?**
Maybe. You’re better protected from DST-related bugs, but you can still shoot yourself in the foot by carelessly turning naive datetimes into aware datetimes, and vice-versa.
If your application connects to other systems – for instance, if it queries a web service – make sure datetimes are properly specified. To transmit datetimes safely, their representation should include the UTC offset, or their values should be in UTC (or both!).
Finally, our calendar system contains interesting edge cases. For example, you can’t always subtract one year directly from a given date:
```
>>> import datetime
>>> def one_year_before(value):  # Wrong example.
...     return value.replace(year=value.year - 1)
...
>>> one_year_before(datetime.datetime(2012, 3, 1, 10, 0))
datetime.datetime(2011, 3, 1, 10, 0)
>>> one_year_before(datetime.datetime(2012, 2, 29, 10, 0))
Traceback (most recent call last):
...
ValueError: day is out of range for month

```

To implement such a function correctly, you must decide whether 2012-02-29 minus one year is 2011-02-28 or 2011-03-01, which depends on your business requirements.
  3. **How do I interact with a database that stores datetimes in local time?**
Set the [`TIME_ZONE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-TIME_ZONE) option to the appropriate time zone for this database in the [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) setting.
This is useful for connecting to a database that doesn’t support time zones and that isn’t managed by Django when [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`.


### Troubleshooting[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#troubleshooting "Link to this heading")
  1. **My application crashes with** `TypeError: can't compare offset-naive` `and offset-aware datetimes` **– what’s wrong?**
Let’s reproduce this error by comparing a naive and an aware datetime:
```
>>> from django.utils import timezone
>>> aware = timezone.now()
>>> naive = timezone.make_naive(aware)
>>> naive == aware
Traceback (most recent call last):
...
TypeError: can't compare offset-naive and offset-aware datetimes

```

If you encounter this error, most likely your code is comparing these two things:
     * a datetime provided by Django – for instance, a value read from a form or a model field. Since you enabled time zone support, it’s aware.
     * a datetime generated by your code, which is naive (or you wouldn’t be reading this).
Generally, the correct solution is to change your code to use an aware datetime instead.
If you’re writing a pluggable application that’s expected to work independently of the value of [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ), you may find [`django.utils.timezone.now()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.now "django.utils.timezone.now") useful. This function returns the current date and time as a naive datetime when `USE_TZ = False` and as an aware datetime when `USE_TZ = True`. You can add or subtract
  2. **I see lots of** `RuntimeWarning: DateTimeField received a naive datetime` `(YYYY-MM-DD HH:MM:SS)` `while time zone support is active` **– is that bad?**
When time zone support is enabled, the database layer expects to receive only aware datetimes from your code. This warning occurs when it receives a naive datetime. This indicates that you haven’t finished porting your code for time zone support. Please refer to the [migration guide](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zones-migration-guide) for tips on this process.
In the meantime, for backwards compatibility, the datetime is considered to be in the default time zone, which is generally what you expect.
  3. `now.date()` **is yesterday! (or tomorrow)**
If you’ve always used naive datetimes, you probably believe that you can convert a datetime to a date by calling its
None of this is true in a time zone aware environment:
```
>>> import datetime
>>> import zoneinfo
>>> paris_tz = zoneinfo.ZoneInfo("Europe/Paris")
>>> new_york_tz = zoneinfo.ZoneInfo("America/New_York")
>>> paris = datetime.datetime(2012, 3, 3, 1, 30, tzinfo=paris_tz)
# This is the correct way to convert between time zones.
>>> new_york = paris.astimezone(new_york_tz)
>>> paris == new_york, paris.date() == new_york.date()
(True, False)
>>> paris - new_york, paris.date() - new_york.date()
(datetime.timedelta(0), datetime.timedelta(1))
>>> paris
datetime.datetime(2012, 3, 3, 1, 30, tzinfo=zoneinfo.ZoneInfo(key='Europe/Paris'))
>>> new_york
datetime.datetime(2012, 3, 2, 19, 30, tzinfo=zoneinfo.ZoneInfo(key='America/New_York'))

```

As this example shows, the same datetime has a different date, depending on the time zone in which it is represented. But the real problem is more fundamental.
A datetime represents a **point in time**. It’s absolute: it doesn’t depend on anything. On the contrary, a date is a **calendaring concept**. It’s a period of time whose bounds depend on the time zone in which the date is considered. As you can see, these two concepts are fundamentally different, and converting a datetime to a date isn’t a deterministic operation.
What does this mean in practice?
Generally, you should avoid converting a [`date`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatefilter-date) template filter to only show the date part of a datetime. This filter will convert the datetime into the current time zone before formatting it, ensuring the results appear correctly.
If you really need to do the conversion yourself, you must ensure the datetime is converted to the appropriate time zone first. Usually, this will be the current timezone:
```
>>> from django.utils import timezone
>>> timezone.activate(zoneinfo.ZoneInfo("Asia/Singapore"))
# For this example, we set the time zone to Singapore, but here's how
# you would obtain the current time zone in the general case.
>>> current_tz = timezone.get_current_timezone()
>>> local = paris.astimezone(current_tz)
>>> local
datetime.datetime(2012, 3, 3, 8, 30, tzinfo=zoneinfo.ZoneInfo(key='Asia/Singapore'))
>>> local.date()
datetime.date(2012, 3, 3)

```

  4. **I get an error** “`Are time zone definitions for your database installed?`”
If you are using MySQL, see the [Time zone definitions](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-time-zone-definitions) section of the MySQL notes for instructions on loading time zone definitions.


### Usage[¶](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#usage "Link to this heading")
  1. **I have a string** `"2012-02-21 10:28:45"` **and I know it’s in the** `"Europe/Helsinki"` **time zone. How do I turn that into an aware datetime?**
Here you need to create the required `ZoneInfo` instance and attach it to the naïve datetime:
```
>>> import zoneinfo
>>> from django.utils.dateparse import parse_datetime
>>> naive = parse_datetime("2012-02-21 10:28:45")
>>> naive.replace(tzinfo=zoneinfo.ZoneInfo("Europe/Helsinki"))
datetime.datetime(2012, 2, 21, 10, 28, 45, tzinfo=zoneinfo.ZoneInfo(key='Europe/Helsinki'))

```

  2. **How can I obtain the local time in the current time zone?**
Well, the first question is, do you really need to?
You should only use local time when you’re interacting with humans, and the template layer provides [filters and tags](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zones-in-templates) to convert datetimes to the time zone of your choice.
Furthermore, Python knows how to compare aware datetimes, taking into account UTC offsets when necessary. It’s much easier (and possibly faster) to write all your model and view code in UTC. So, in most circumstances, the datetime in UTC returned by [`django.utils.timezone.now()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.now "django.utils.timezone.now") will be sufficient.
For the sake of completeness, though, if you really want the local time in the current time zone, here’s how you can obtain it:
```
>>> from django.utils import timezone
>>> timezone.localtime(timezone.now())
datetime.datetime(2012, 3, 3, 20, 10, 53, 873365, tzinfo=zoneinfo.ZoneInfo(key='Europe/Paris'))

```

In this example, the current time zone is `"Europe/Paris"`.
  3. **How can I see all available time zones?**

Previous page and next page
[](https://docs.djangoproject.com/en/6.0/topics/i18n/formatting/)
[Logging ](https://docs.djangoproject.com/en/6.0/topics/logging/)
[](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Online Casinon donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Time zones](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/)
    * [Overview](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#overview)
    * [Concepts](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#concepts)
      * [Naive and aware datetime objects](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#naive-and-aware-datetime-objects)
      * [Interpretation of naive datetime objects](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#interpretation-of-naive-datetime-objects)
      * [Default time zone and current time zone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-time-zone-and-current-time-zone)
      * [Selecting the current time zone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#selecting-the-current-time-zone)
    * [Time zone aware input in forms](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zone-aware-input-in-forms)
    * [Time zone aware output in templates](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#time-zone-aware-output-in-templates)
      * [Template tags](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#template-tags)
        * [`localtime`](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#localtime)
        * [`timezone`](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#timezone)
        * [`get_current_timezone`](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#get-current-timezone)
      * [Template filters](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#template-filters)
        * [`localtime`](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#std-templatefilter-localtime)
        * [`utc`](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#utc)
        * [`timezone`](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#std-templatefilter-timezone)
    * [Migration guide](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#migration-guide)
      * [Database](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#database)
        * [PostgreSQL](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#postgresql)
        * [Other databases](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#other-databases)
      * [Code](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#code)
      * [Fixtures](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#fixtures)
    * [FAQ](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#faq)
      * [Setup](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#setup)
      * [Troubleshooting](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#troubleshooting)
      * [Usage](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#usage)


### Browse
  * Prev: [Format localization](https://docs.djangoproject.com/en/6.0/topics/i18n/formatting/)
  * Next: [Logging](https://docs.djangoproject.com/en/6.0/topics/logging/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [Using Django](https://docs.djangoproject.com/en/6.0/topics/)
      * [Internationalization and localization](https://docs.djangoproject.com/en/6.0/topics/i18n/)
        * Time zones


### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
    Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
    Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.
### Download:
Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
Provided by
### Diamond and Platinum Members
  * **JetBrains**


  * **Sentry**


  * **Kraken Tech**


## Django Links
### Learn More
  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)


### Get Involved
  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)


### Get Help
  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)


### Follow Us
  * [News RSS](https://www.djangoproject.com/rss/weblog/)


### Support Us
  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)


[Django](https://www.djangoproject.com/)
  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by &


© 2005-2026 [ Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
