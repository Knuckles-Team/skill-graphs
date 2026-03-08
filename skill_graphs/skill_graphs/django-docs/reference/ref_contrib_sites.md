[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/contrib/sites/)
  * [sv](https://docs.djangoproject.com/sv/6.0/ref/contrib/sites/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/contrib/sites/)
  * [pl](https://docs.djangoproject.com/pl/6.0/ref/contrib/sites/)
  * [ko](https://docs.djangoproject.com/ko/6.0/ref/contrib/sites/)
  * [ja](https://docs.djangoproject.com/ja/6.0/ref/contrib/sites/)
  * [it](https://docs.djangoproject.com/it/6.0/ref/contrib/sites/)
  * [id](https://docs.djangoproject.com/id/6.0/ref/contrib/sites/)
  * [fr](https://docs.djangoproject.com/fr/6.0/ref/contrib/sites/)
  * [es](https://docs.djangoproject.com/es/6.0/ref/contrib/sites/)
  * [el](https://docs.djangoproject.com/el/6.0/ref/contrib/sites/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/contrib/sites/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/contrib/sites/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/contrib/sites/)
  * [5.0](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/contrib/sites/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/contrib/sites/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/contrib/sites/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/contrib/sites/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/contrib/sites/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/contrib/sites/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/contrib/sites/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/contrib/sites/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/contrib/sites/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/contrib/sites/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/contrib/sites/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/contrib/sites/)


  * [](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#top)


# The “sites” framework[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#module-django.contrib.sites "Link to this heading")
Django comes with an optional “sites” framework. It’s a hook for associating objects and functionality to particular websites, and it’s a holding place for the domain names and “verbose” names of your Django-powered sites.
Use it if your single Django installation powers more than one site and you need to differentiate between those sites in some way.
The sites framework is mainly based on this model:

_class_ models.Site[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "Link to this definition")

A model for storing the `domain` and `name` attributes of a website.

domain[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site.domain "Link to this definition")

The fully qualified domain name associated with the website. For example, `www.example.com`.

name[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site.name "Link to this definition")

A human-readable “verbose” name for the website.
The [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) setting specifies the database ID of the [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") object associated with that particular settings file. If the setting is omitted, the [`get_current_site()`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.shortcuts.get_current_site "django.contrib.sites.shortcuts.get_current_site") function will try to get the current site by comparing the [`domain`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site.domain "django.contrib.sites.models.Site.domain") with the host name from the [`request.get_host()`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host") method.
How you use this is up to you, but Django uses it in a couple of ways automatically via a couple of conventions.
## Example usage[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#example-usage "Link to this heading")
Why would you use sites? It’s best explained through examples.
### Associating content with multiple sites[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#associating-content-with-multiple-sites "Link to this heading")
The _both_ sites.
The naive way of solving the problem would be to require site producers to publish the same story twice: once for LJWorld.com and again for Lawrence.com. But that’s inefficient for site producers, and it’s redundant to store multiple copies of the same story in the database.
A better solution removes the content duplication: Both sites use the same article database, and an article is associated with one or more sites. In Django model terminology, that’s represented by a [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") in the `Article` model:
```
from django.contrib.sites.models import Site
from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=200)
    # ...
    sites = models.ManyToManyField(Site)

```

This accomplishes several things quite nicely:
  * It lets the site producers edit all content – on both sites – in a single interface (the Django admin).
  * It means the same story doesn’t have to be published twice in the database; it only has a single record in the database.
  * It lets the site developers use the same Django view code for both sites. The view code that displays a given story checks to make sure the requested story is on the current site. It looks something like this:
```
from django.contrib.sites.shortcuts import get_current_site


def article_detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id, sites__id=get_current_site(request).id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist on this site")
    # ...

```



### Associating content with a single site[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#associating-content-with-a-single-site "Link to this heading")
Similarly, you can associate a model to the [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") model in a many-to-one relationship, using [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey").
For example, if an article is only allowed on a single site, you’d use a model like this:
```
from django.contrib.sites.models import Site
from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=200)
    # ...
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

```

This has the same benefits as described in the last section.
### Hooking into the current site from views[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#hooking-into-the-current-site-from-views "Link to this heading")
You can use the sites framework in your Django views to do particular things based on the site in which the view is being called. For example:
```
from django.conf import settings


def my_view(request):
    if settings.SITE_ID == 3:
        # Do something.
        pass
    else:
        # Do something else.
        pass

```

It’s fragile to hardcode the site IDs like that, in case they change. The cleaner way of accomplishing the same thing is to check the current site’s domain:
```
from django.contrib.sites.shortcuts import get_current_site


def my_view(request):
    current_site = get_current_site(request)
    if current_site.domain == "foo.com":
        # Do something
        pass
    else:
        # Do something else.
        pass

```

This has also the advantage of checking if the sites framework is installed, and return a [`RequestSite`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite "django.contrib.sites.requests.RequestSite") instance if it is not.
If you don’t have access to the request object, you can use the `get_current()` method of the [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") model’s manager. You should then ensure that your settings file does contain the [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) setting. This example is equivalent to the previous one:
```
from django.contrib.sites.models import Site


def my_function_without_request():
    current_site = Site.objects.get_current()
    if current_site.domain == "foo.com":
        # Do something
        pass
    else:
        # Do something else.
        pass

```

### Getting the current domain for display[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#getting-the-current-domain-for-display "Link to this heading")
LJWorld.com and Lawrence.com both have email alert functionality, which lets readers sign up to get notifications when news happens. It’s pretty basic: A reader signs up on a web form and immediately gets an email saying, “Thanks for your subscription.”
It’d be inefficient and redundant to implement this sign up processing code twice, so the sites use the same code behind the scenes. But the “thank you for signing up” notice needs to be different for each site. By using [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") objects, we can abstract the “thank you” notice to use the values of the current site’s [`name`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site.name "django.contrib.sites.models.Site.name") and [`domain`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site.domain "django.contrib.sites.models.Site.domain").
Here’s an example of what the form-handling view looks like:
```
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail


def register_for_newsletter(request):
    # Check form values, etc., and subscribe the user.
    # ...

    current_site = get_current_site(request)
    send_mail(
        "Thanks for subscribing to %s alerts" % current_site.name,
        "Thanks for your subscription. We appreciate it.\n\n-The %s team."
        % (current_site.name,),
        "editor@%s" % current_site.domain,
        [user.email],
    )

    # ...

```

On Lawrence.com, this email has the subject line “Thanks for subscribing to lawrence.com alerts.” On LJWorld.com, the email has the subject “Thanks for subscribing to LJWorld.com alerts.” Same goes for the email’s message body.
Note that an even more flexible (but more heavyweight) way of doing this would be to use Django’s template system. Assuming Lawrence.com and LJWorld.com have different template directories ([`DIRS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES-DIRS)), you could farm out to the template system like so:
```
from django.core.mail import send_mail
from django.template import loader


def register_for_newsletter(request):
    # Check form values, etc., and subscribe the user.
    # ...

    subject = loader.get_template("alerts/subject.txt").render({})
    message = loader.get_template("alerts/message.txt").render({})
    send_mail(subject, message, "editor@ljworld.com", [user.email])

    # ...

```

In this case, you’d have to create `subject.txt` and `message.txt` template files for both the LJWorld.com and Lawrence.com template directories. That gives you more flexibility, but it’s also more complex.
It’s a good idea to exploit the [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") objects as much as possible, to remove unneeded complexity and redundancy.
### Getting the current domain for full URLs[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#getting-the-current-domain-for-full-urls "Link to this heading")
Django’s `get_absolute_url()` convention is nice for getting your objects’ URL without the domain name, but in some cases you might want to display the full URL – with `https://` and the domain and everything – for an object. To do this, you can use the sites framework. An example:
```
>>> from django.contrib.sites.models import Site
>>> obj = MyModel.objects.get(id=3)
>>> obj.get_absolute_url()
'/mymodel/objects/3/'
>>> Site.objects.get_current().domain
'example.com'
>>> "https://%s%s" % (Site.objects.get_current().domain, obj.get_absolute_url())
'https://example.com/mymodel/objects/3/'

```

## Enabling the sites framework[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#enabling-the-sites-framework "Link to this heading")
To enable the sites framework, follow these steps:
  1. Add `'django.contrib.sites'` to your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) setting.
  2. Define a [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) setting:
```
SITE_ID = 1

```

  3. Run [`migrate`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-migrate).


`django.contrib.sites` registers a [`post_migrate`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.db.models.signals.post_migrate "django.db.models.signals.post_migrate") signal handler which creates a default site named `example.com` with the domain `example.com`. This site will also be created after Django creates the test database. To set the correct name and domain for your project, you can use a [data migration](https://docs.djangoproject.com/en/6.0/topics/migrations/#data-migrations).
In order to serve different sites in production, you’d create a separate settings file with each `SITE_ID` (perhaps importing from a common settings file to avoid duplicating shared settings) and then specify the appropriate [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/6.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) for each site.
## Caching the current `Site` object[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#caching-the-current-site-object "Link to this heading")
As the current site is stored in the database, each call to `Site.objects.get_current()` could result in a database query. But Django is a little cleverer than that: on the first request, the current site is cached, and any subsequent call returns the cached data instead of hitting the database.
If for any reason you want to force a database query, you can tell Django to clear the cache using `Site.objects.clear_cache()`:
```
# First call; current site fetched from database.
current_site = Site.objects.get_current()
# ...

# Second call; current site fetched from cache.
current_site = Site.objects.get_current()
# ...

# Force a database query for the third call.
Site.objects.clear_cache()
current_site = Site.objects.get_current()

```

## The `CurrentSiteManager`[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#the-currentsitemanager "Link to this heading")

_class_ managers.CurrentSiteManager[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "Link to this definition")

If [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") plays a key role in your application, consider using the helpful [`CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager") in your model(s). It’s a model [manager](https://docs.djangoproject.com/en/6.0/topics/db/managers/) that automatically filters its queries to include only objects associated with the current [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site").
Mandatory [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID)
The `CurrentSiteManager` is only usable when the [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) setting is defined in your settings.
Use [`CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager") by adding it to your model explicitly. For example:
```
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models


class Photo(models.Model):
    photo = models.FileField(upload_to="photos")
    photographer_name = models.CharField(max_length=100)
    pub_date = models.DateField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager()

```

With this model, `Photo.objects.all()` will return all `Photo` objects in the database, but `Photo.on_site.all()` will return only the `Photo` objects associated with the current site, according to the [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) setting.
Put another way, these two statements are equivalent:
```
Photo.objects.filter(site=settings.SITE_ID)
Photo.on_site.all()

```

How did [`CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager") know which field of `Photo` was the [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site")? By default, [`CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager") looks for a either a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") called `site` or a [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") called `sites` to filter on. If you use a field named something other than `site` or `sites` to identify which [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") objects your object is related to, then you need to explicitly pass the custom field name as a parameter to [`CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager") on your model. The following model, which has a field called `publish_on`, demonstrates this:
```
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models


class Photo(models.Model):
    photo = models.FileField(upload_to="photos")
    photographer_name = models.CharField(max_length=100)
    pub_date = models.DateField()
    publish_on = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = models.Manager()
    on_site = CurrentSiteManager("publish_on")

```

If you attempt to use [`CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager") and pass a field name that doesn’t exist, Django will raise a `ValueError`.
Finally, note that you’ll probably want to keep a normal (non-site-specific) `Manager` on your model, even if you use [`CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager"). As explained in the [manager documentation](https://docs.djangoproject.com/en/6.0/topics/db/managers/), if you define a manager manually, then Django won’t create the automatic `objects = models.Manager()` manager for you. Also note that certain parts of Django – namely, the Django admin site and generic views – use whichever manager is defined _first_ in the model, so if you want your admin site to have access to all objects (not just site-specific ones), put `objects = models.Manager()` in your model, before you define [`CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.managers.CurrentSiteManager "django.contrib.sites.managers.CurrentSiteManager").
## Site middleware[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#site-middleware "Link to this heading")
If you often use this pattern:
```
from django.contrib.sites.models import Site


def my_view(request):
    site = Site.objects.get_current()
    ...

```

To avoid repetitions, add [`django.contrib.sites.middleware.CurrentSiteMiddleware`](https://docs.djangoproject.com/en/6.0/ref/middleware/#django.contrib.sites.middleware.CurrentSiteMiddleware "django.contrib.sites.middleware.CurrentSiteMiddleware") to [`MIDDLEWARE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MIDDLEWARE). The middleware sets the `site` attribute on every request object, so you can use `request.site` to get the current site.
## How Django uses the sites framework[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#how-django-uses-the-sites-framework "Link to this heading")
Although it’s not required that you use the sites framework, it’s strongly encouraged, because Django takes advantage of it in a few places. Even if your Django installation is powering only a single site, you should take the two seconds to create the site object with your `domain` and `name`, and point to its ID in your [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) setting.
Here’s how Django uses the sites framework:
  * In the [`redirects framework`](https://docs.djangoproject.com/en/6.0/ref/contrib/redirects/#module-django.contrib.redirects "django.contrib.redirects: A framework for managing redirects."), each redirect object is associated with a particular site. When Django searches for a redirect, it takes into account the current site.
  * In the [`flatpages framework`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#module-django.contrib.flatpages "django.contrib.flatpages: A framework for managing simple ?flat? HTML content in a database."), each flatpage is associated with a particular site. When a flatpage is created, you specify its [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site"), and the [`FlatpageFallbackMiddleware`](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/#django.contrib.flatpages.middleware.FlatpageFallbackMiddleware "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware") checks the current site in retrieving flatpages to display.
  * In the [`syndication framework`](https://docs.djangoproject.com/en/6.0/ref/contrib/syndication/#module-django.contrib.syndication "django.contrib.syndication: A framework for generating syndication feeds, in RSS and Atom, quite easily."), the templates for `title` and `description` automatically have access to a variable `{{ site }}`, which is the [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") object representing the current site. Also, the hook for providing item URLs will use the `domain` from the current [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") object if you don’t specify a fully-qualified domain.
  * In the [`authentication framework`](https://docs.djangoproject.com/en/6.0/topics/auth/#module-django.contrib.auth "django.contrib.auth: Django's authentication framework."), [`django.contrib.auth.views.LoginView`](https://docs.djangoproject.com/en/6.0/topics/auth/default/#django.contrib.auth.views.LoginView "django.contrib.auth.views.LoginView") passes the current [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") name to the template as `{{ site_name }}`.
  * The shortcut view (`django.contrib.contenttypes.views.shortcut`) uses the domain of the current [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") object when calculating an object’s URL.
  * In the admin framework, the “view on site” link uses the current [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") to work out the domain for the site that it will redirect to.


##  `RequestSite` objects[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#requestsite-objects "Link to this heading")
Some [django.contrib](https://docs.djangoproject.com/en/6.0/ref/contrib/) applications take advantage of the sites framework but are architected in a way that doesn’t _require_ the sites framework to be installed in your database. (Some people don’t want to, or just aren’t _able_ to install the extra database table that the sites framework requires.) For those cases, the framework provides a [`django.contrib.sites.requests.RequestSite`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite "django.contrib.sites.requests.RequestSite") class, which can be used as a fallback when the database-backed sites framework is not available.

_class_ requests.RequestSite[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite "Link to this definition")

A class that shares the primary interface of [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") (i.e., it has `domain` and `name` attributes) but gets its data from a Django [`HttpRequest`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object rather than from a database.

__init__(_request_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite.__init__ "Link to this definition")

Sets the `name` and `domain` attributes to the value of [`get_host()`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host").
A [`RequestSite`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite "django.contrib.sites.requests.RequestSite") object has a similar interface to a normal [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") object, except its [`__init__()`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite.__init__ "django.contrib.sites.requests.RequestSite.__init__") method takes an [`HttpRequest`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object. It’s able to deduce the `domain` and `name` by looking at the request’s domain. It has `save()` and `delete()` methods to match the interface of [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site"), but the methods raise
##  `get_current_site` shortcut[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#get-current-site-shortcut "Link to this heading")
Finally, to avoid repetitive fallback code, the framework provides a [`django.contrib.sites.shortcuts.get_current_site()`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.shortcuts.get_current_site "django.contrib.sites.shortcuts.get_current_site") function.

shortcuts.get_current_site(_request_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.shortcuts.get_current_site "Link to this definition")

A function that checks if `django.contrib.sites` is installed and returns either the current [`Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") object or a [`RequestSite`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite "django.contrib.sites.requests.RequestSite") object based on the request. It looks up the current site based on [`request.get_host()`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host") if the [`SITE_ID`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-SITE_ID) setting is not defined.
Both a domain and a port may be returned by [`request.get_host()`](https://docs.djangoproject.com/en/6.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host") when the Host header has a port explicitly specified, e.g. `example.com:80`. In such cases, if the lookup fails because the host does not match a record in the database, the port is stripped and the lookup is retried with the domain part only. This does not apply to [`RequestSite`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite "django.contrib.sites.requests.RequestSite") which will always use the unmodified host. Previous page and next page
[](https://docs.djangoproject.com/en/6.0/ref/contrib/sitemaps/)
[The `staticfiles` app ](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/)
[](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ West Palm Beach Employment Attorney donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [The “sites” framework](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/)
    * [Example usage](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#example-usage)
      * [Associating content with multiple sites](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#associating-content-with-multiple-sites)
      * [Associating content with a single site](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#associating-content-with-a-single-site)
      * [Hooking into the current site from views](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#hooking-into-the-current-site-from-views)
      * [Getting the current domain for display](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#getting-the-current-domain-for-display)
      * [Getting the current domain for full URLs](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#getting-the-current-domain-for-full-urls)
    * [Enabling the sites framework](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#enabling-the-sites-framework)
    * [Caching the current `Site` object](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#caching-the-current-site-object)
    * [The `CurrentSiteManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#the-currentsitemanager)
    * [Site middleware](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#site-middleware)
    * [How Django uses the sites framework](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#how-django-uses-the-sites-framework)
    * [`RequestSite` objects](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#requestsite-objects)
    * [`get_current_site` shortcut](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#get-current-site-shortcut)


### Browse
  * Prev: [The sitemap framework](https://docs.djangoproject.com/en/6.0/ref/contrib/sitemaps/)
  * Next: [The `staticfiles` app](https://docs.djangoproject.com/en/6.0/ref/contrib/staticfiles/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
      * [`contrib` packages](https://docs.djangoproject.com/en/6.0/ref/contrib/)
        * The “sites” framework


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
