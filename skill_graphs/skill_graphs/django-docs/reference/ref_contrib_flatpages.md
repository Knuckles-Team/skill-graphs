[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/contrib/flatpages/)
  * [sv](https://docs.djangoproject.com/sv/6.0/ref/contrib/flatpages/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/contrib/flatpages/)
  * [pl](https://docs.djangoproject.com/pl/6.0/ref/contrib/flatpages/)
  * [ko](https://docs.djangoproject.com/ko/6.0/ref/contrib/flatpages/)
  * [ja](https://docs.djangoproject.com/ja/6.0/ref/contrib/flatpages/)
  * [it](https://docs.djangoproject.com/it/6.0/ref/contrib/flatpages/)
  * [id](https://docs.djangoproject.com/id/6.0/ref/contrib/flatpages/)
  * [fr](https://docs.djangoproject.com/fr/6.0/ref/contrib/flatpages/)
  * [es](https://docs.djangoproject.com/es/6.0/ref/contrib/flatpages/)
  * [el](https://docs.djangoproject.com/el/6.0/ref/contrib/flatpages/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/contrib/flatpages/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/contrib/flatpages/)
  * [5.0](https://docs.djangoproject.com/en/5.0/ref/contrib/flatpages/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/contrib/flatpages/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/contrib/flatpages/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/contrib/flatpages/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/contrib/flatpages/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/contrib/flatpages/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/contrib/flatpages/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/contrib/flatpages/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/contrib/flatpages/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/contrib/flatpages/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/contrib/flatpages/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/contrib/flatpages/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/contrib/flatpages/)


  * [](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#top)


# The flatpages app[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#module-django.contrib.flatpages "Link to this heading")
Django comes with an optional “flatpages” application. It lets you store “flat” HTML content in a database and handles the management for you via Django’s admin interface and a Python API.
A flatpage is an object with a URL, title and content. Use it for one-off, special-case pages, such as “About” or “Privacy Policy” pages, that you want to store in a database but for which you don’t want to develop a custom Django application.
A flatpage can use a custom template or a default, systemwide flatpage template. It can be associated with one, or multiple, sites.
The content field may optionally be left blank if you prefer to put your content in a custom template.
## Installation[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#installation "Link to this heading")
To install the flatpages app, follow these steps:
  1. Install the [`sites framework`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#module-django.contrib.sites "django.contrib.sites: Lets you operate multiple websites from the same database and Django project") by adding `'django.contrib.sites'` to your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) setting, if it’s not already in there.
Also make sure you’ve correctly set [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) to the ID of the site the settings file represents. This will usually be `1` (i.e. `SITE_ID = 1`), but if you’re using the sites framework to manage multiple sites, it could be the ID of a different site.
  2. Add `'django.contrib.flatpages'` to your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) setting.


Then either:
  1. Add an entry in your URLconf. For example:
```
urlpatterns = [
    path("pages/", include("django.contrib.flatpages.urls")),
]

```



or:
  1. Add `'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'` to your [`MIDDLEWARE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MIDDLEWARE) setting.
  2. Run the command [`manage.py migrate`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-migrate).


## How it works[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#how-it-works "Link to this heading")
`manage.py migrate` creates two tables in your database: `django_flatpage` and `django_flatpage_sites`. `django_flatpage` is a lookup table that maps a URL to a title and bunch of text content. `django_flatpage_sites` associates a flatpage with a site.
### Using the URLconf[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#using-the-urlconf "Link to this heading")
There are several ways to include the flatpages in your URLconf. You can dedicate a particular path to flatpages:
```
urlpatterns = [
    path("pages/", include("django.contrib.flatpages.urls")),
]

```

You can also set it up as a “catchall” pattern. In this case, it is important to place the pattern at the end of the other urlpatterns:
```
from django.contrib.flatpages import views

# Your other patterns here
urlpatterns += [
    re_path(r"^(?P<url>.*/)$", views.flatpage),
]

```

Warning
If you set [`APPEND_SLASH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-APPEND_SLASH) to `False`, you must remove the slash in the catchall pattern or flatpages without a trailing slash will not be matched.
Another common setup is to use flatpages for a limited set of known pages and to hardcode their URLs in the [URLconf](https://docs.djangoproject.com/en/6.0/topics/http/urls/):
```
from django.contrib.flatpages import views

urlpatterns += [
    path("about-us/", views.flatpage, kwargs={"url": "/about-us/"}, name="about"),
    path("license/", views.flatpage, kwargs={"url": "/license/"}, name="license"),
]

```

The `kwargs` argument sets the `url` value used for the `FlatPage` model lookup in the flatpage view.
The `name` argument allows the URL to be reversed in templates, for example using the [`url`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#std-templatetag-url) template tag.
### Using the middleware[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#using-the-middleware "Link to this heading")
The [`FlatpageFallbackMiddleware`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.middleware.FlatpageFallbackMiddleware "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware") can do all of the work.

_class_ FlatpageFallbackMiddleware[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.middleware.FlatpageFallbackMiddleware "Link to this definition")

Each time any Django application raises a 404 error, this middleware checks the flatpages database for the requested URL as a last resort. Specifically, it checks for a flatpage with the given URL with a site ID that corresponds to the [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) setting.
If it finds a match, it follows this algorithm:
  * If the flatpage has a custom template, it loads that template. Otherwise, it loads the template `flatpages/default.html`.
  * It passes that template a single context variable, `flatpage`, which is the flatpage object. It uses [`RequestContext`](https://docs.djangoproject.com/en/6.0/ref/templates/api/#django.template.RequestContext "django.template.RequestContext") in rendering the template.


The middleware will only add a trailing slash and redirect (by looking at the [`APPEND_SLASH`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-APPEND_SLASH) setting) if the resulting URL refers to a valid flatpage. Redirects are permanent (301 status code).
If it doesn’t find a match, the request continues to be processed as usual.
The middleware only gets activated for 404s – not for 500s or responses of any other status code.
Flatpages will not apply view middleware
Because the `FlatpageFallbackMiddleware` is applied only after URL resolution has failed and produced a 404, the response it returns will not apply any [view middleware](https://docs.djangoproject.com/en/6.0/topics/http/middleware/#view-middleware) methods. Only requests which are successfully routed to a view via normal URL resolution apply view middleware.
Note that the order of [`MIDDLEWARE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MIDDLEWARE) matters. Generally, you can put [`FlatpageFallbackMiddleware`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.middleware.FlatpageFallbackMiddleware "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware") at the end of the list. This means it will run first when processing the response, and ensures that any other response-processing middleware see the real flatpage response rather than the 404.
For more on middleware, read the [middleware docs](https://docs.djangoproject.com/en/6.0/topics/http/middleware/).
Ensure that your 404 template works
Note that the [`FlatpageFallbackMiddleware`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.middleware.FlatpageFallbackMiddleware "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware") only steps in once another view has successfully produced a 404 response. If another view or middleware class attempts to produce a 404 but ends up raising an exception instead, the response will become an HTTP 500 (“Internal Server Error”) and the [`FlatpageFallbackMiddleware`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.middleware.FlatpageFallbackMiddleware "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware") will not attempt to serve a flatpage.
## How to add, change and delete flatpages[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#how-to-add-change-and-delete-flatpages "Link to this heading")
Warning
Permissions to add or edit flatpages should be restricted to trusted users. Flatpages are defined by raw HTML and are **not sanitized** by Django. As a consequence, a malicious flatpage can lead to various security vulnerabilities, including permission escalation.
### Via the admin interface[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#via-the-admin-interface "Link to this heading")
If you’ve activated the automatic Django admin interface, you should see a “Flatpages” section on the admin index page. Edit flatpages as you edit any other object in the system.
The `FlatPage` model has an `enable_comments` field that isn’t used by `contrib.flatpages`, but that could be useful for your project or third-party apps. It doesn’t appear in the admin interface, but you can add it by registering a custom `ModelAdmin` for `FlatPage`:
```
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = [
        (None, {"fields": ["url", "title", "content", "sites"]}),
        (
            _("Advanced options"),
            {
                "classes": ["collapse"],
                "fields": [
                    "enable_comments",
                    "registration_required",
                    "template_name",
                ],
            },
        ),
    ]


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

```

### Via the Python API[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#via-the-python-api "Link to this heading")
Flatpages are represented by a standard [Django model](https://docs.djangoproject.com/en/6.0/topics/db/models/), [`FlatPage`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage "django.contrib.flatpages.models.FlatPage"). You can access flatpage objects via the [Django database API](https://docs.djangoproject.com/en/6.0/topics/db/queries/).
Check for duplicate flatpage URLs.
If you add or modify flatpages via your own code, you will likely want to check for duplicate flatpage URLs within the same site. The flatpage form used in the admin performs this validation check, and can be imported from `django.contrib.flatpages.forms.FlatpageForm` and used in your own views.
##  `FlatPage` model[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#flatpage-model "Link to this heading")

_class_ models.FlatPage[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage "Link to this definition")

### Fields[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#fields "Link to this heading")
[`FlatPage`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage "django.contrib.flatpages.models.FlatPage") objects have the following fields:

_class_ models.FlatPage


url[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage.url "Link to this definition")

Required. 100 characters or fewer. Indexed for faster lookups.

title[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage.title "Link to this definition")

Required. 200 characters or fewer.

content[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage.content "Link to this definition")

Optional ([`blank=True`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.blank "django.db.models.Field.blank")). [`TextField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.TextField "django.db.models.TextField") that typically, contains the HTML content of the page.

enable_comments[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage.enable_comments "Link to this definition")

Boolean. This field is not used by [`flatpages`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#module-django.contrib.flatpages "django.contrib.flatpages: A framework for managing simple ?flat? HTML content in a database.") by default and does not appear in the admin interface. Please see [flatpages admin interface section](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#flatpages-admin) for a detailed explanation.

template_name[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage.template_name "Link to this definition")

Optional ([`blank=True`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.blank "django.db.models.Field.blank")). 70 characters or fewer. Specifies the template used to render the page. Defaults to `flatpages/default.html` if not provided.

sites[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage.sites "Link to this definition")

Many-to-many relationship to [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site"), which determines the [sites](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/) the flatpage is available on.
### Methods[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#methods "Link to this heading")

_class_ models.FlatPage


get_absolute_url()[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage.get_absolute_url "Link to this definition")

Returns the relative URL path of the page based on the [`url`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage.url "django.contrib.flatpages.models.FlatPage.url") attribute.
## Flatpage templates[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#flatpage-templates "Link to this heading")
By default, flatpages are rendered via the template `flatpages/default.html`, but you can override that for a particular flatpage: in the admin, a collapsed fieldset titled “Advanced options” (clicking will expand it) contains a field for specifying a template name. If you’re creating a flatpage via the Python API you can set the template name as the field `template_name` on the `FlatPage` object.
Creating the `flatpages/default.html` template is your responsibility; in your template directory, create a `flatpages` directory containing a file `default.html`.
Flatpage templates are passed a single context variable, `flatpage`, which is the flatpage object.
Here’s a sample `flatpages/default.html` template:
```
<!DOCTYPE html>
<html lang="en">
<head>
<title>{{ flatpage.title }}</title>
</head>
<body>
{{ flatpage.content }}
</body>
</html>

```

Since you’re already entering raw HTML into the admin page for a flatpage, both `flatpage.title` and `flatpage.content` are marked as **not** requiring [automatic HTML escaping](https://docs.djangoproject.com/en/6.0/ref/templates/language/#automatic-html-escaping) in the template.
## Getting a list of [`FlatPage`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.models.FlatPage "django.contrib.flatpages.models.FlatPage") objects in your templates[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#getting-a-list-of-flatpage-objects-in-your-templates "Link to this heading")
The flatpages app provides a template tag that allows you to iterate over all of the available flatpages on the [current site](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#hooking-into-current-site-from-views).
Like all custom template tags, you’ll need to [load its custom tag library](https://docs.djangoproject.com/en/6.0/ref/templates/language/#loading-custom-template-libraries) before you can use it. After loading the library, you can retrieve all current flatpages via the [`get_flatpages`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#std-templatetag-get_flatpages) tag:
```
{% load flatpages %}
{% get_flatpages as flatpages %}
<ul>
    {% for page in flatpages %}
        <li><a href="{{ page.url }}">{{ page.title }}</a></li>
    {% endfor %}
</ul>

```

### Displaying `registration_required` flatpages[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#displaying-registration-required-flatpages "Link to this heading")
By default, the [`get_flatpages`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#std-templatetag-get_flatpages) template tag will only show flatpages that are marked `registration_required = False`. If you want to display registration-protected flatpages, you need to specify an authenticated user using a `for` clause.
For example:
```
{% get_flatpages for someuser as about_pages %}

```

If you provide an anonymous user, [`get_flatpages`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#std-templatetag-get_flatpages) will behave the same as if you hadn’t provided a user – i.e., it will only show you public flatpages.
### Limiting flatpages by base URL[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#limiting-flatpages-by-base-url "Link to this heading")
An optional argument, `starts_with`, can be applied to limit the returned pages to those beginning with a particular base URL. This argument may be passed as a string, or as a variable to be resolved from the context.
For example:
```
{% get_flatpages '/about/' as about_pages %}
{% get_flatpages about_prefix as about_pages %}
{% get_flatpages '/about/' for someuser as about_pages %}

```

## Integrating with [`django.contrib.sitemaps`](https://docs.djangoproject.com/en/6.0/ref/contrib/sitemaps/#module-django.contrib.sitemaps "django.contrib.sitemaps: A framework for generating Google sitemap XML files.")[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#integrating-with-django-contrib-sitemaps "Link to this heading")

_class_ FlatPageSitemap[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.sitemaps.FlatPageSitemap "Link to this definition")

The [`sitemaps.FlatPageSitemap`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.sitemaps.FlatPageSitemap "django.contrib.flatpages.sitemaps.FlatPageSitemap") class looks at all publicly visible [`flatpages`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#module-django.contrib.flatpages "django.contrib.flatpages: A framework for managing simple ?flat? HTML content in a database.") defined for the current [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) (see the [`sites documentation`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#module-django.contrib.sites "django.contrib.sites: Lets you operate multiple websites from the same database and Django project")) and creates an entry in the sitemap. These entries include only the [`location`](https://docs.djangoproject.com/en/6.0/ref/contrib/sitemaps/#django.contrib.sitemaps.Sitemap.location "django.contrib.sitemaps.Sitemap.location") attribute – not [`lastmod`](https://docs.djangoproject.com/en/6.0/ref/contrib/sitemaps/#django.contrib.sitemaps.Sitemap.lastmod "django.contrib.sitemaps.Sitemap.lastmod"), [`changefreq`](https://docs.djangoproject.com/en/6.0/ref/contrib/sitemaps/#django.contrib.sitemaps.Sitemap.changefreq "django.contrib.sitemaps.Sitemap.changefreq") or [`priority`](https://docs.djangoproject.com/en/6.0/ref/contrib/sitemaps/#django.contrib.sitemaps.Sitemap.priority "django.contrib.sitemaps.Sitemap.priority").
### Example[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#example "Link to this heading")
Here’s an example of a URLconf using [`FlatPageSitemap`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.sitemaps.FlatPageSitemap "django.contrib.flatpages.sitemaps.FlatPageSitemap"):
```
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path

urlpatterns = [
    # ...
    # the sitemap
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"flatpages": FlatPageSitemap}},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

```

Previous page and next page
[](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/)
[GeoDjango ](https://docs.djangoproject.com/en/6.0/ref/contrib/gis/)
[](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Ricardo Prado donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [The flatpages app](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/)
    * [Installation](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#installation)
    * [How it works](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#how-it-works)
      * [Using the URLconf](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#using-the-urlconf)
      * [Using the middleware](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#using-the-middleware)
    * [How to add, change and delete flatpages](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#how-to-add-change-and-delete-flatpages)
      * [Via the admin interface](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#via-the-admin-interface)
      * [Via the Python API](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#via-the-python-api)
    * [`FlatPage` model](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#flatpage-model)
      * [Fields](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#fields)
      * [Methods](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#methods)
    * [Flatpage templates](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#flatpage-templates)
    * [Getting a list of `FlatPage` objects in your templates](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#getting-a-list-of-flatpage-objects-in-your-templates)
      * [Displaying `registration_required` flatpages](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#displaying-registration-required-flatpages)
      * [Limiting flatpages by base URL](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#limiting-flatpages-by-base-url)
    * [Integrating with `django.contrib.sitemaps`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#integrating-with-django-contrib-sitemaps)
      * [Example](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#example)


### Browse
  * Prev: [The contenttypes framework](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/)
  * Next: [GeoDjango](https://docs.djangoproject.com/en/6.0/ref/contrib/gis/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
      * [`contrib` packages](https://docs.djangoproject.com/en/6.0/ref/contrib/)
        * The flatpages app


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
