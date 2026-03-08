This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/contrib/#main-content)
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
[Documentation](https://docs.djangoproject.com/en/5.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/5.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/contrib/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/contrib/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/contrib/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/contrib/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/contrib/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/contrib/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/contrib/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/contrib/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/contrib/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/contrib/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/contrib/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/contrib/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/contrib/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/contrib/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/contrib/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/contrib/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/contrib/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/contrib/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/contrib/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/contrib/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/contrib/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/contrib/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/contrib/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/contrib/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/contrib/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/contrib/)


  * [](https://docs.djangoproject.com/en/5.0/ref/contrib/#top)


#  `contrib` packages[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#contrib-packages "Link to this heading")
Django aims to follow Python’s
This code lives in `contrib`, along with any dependencies those packages have.
Including `contrib` packages in `INSTALLED_APPS`
For most of these add-ons – specifically, the add-ons that include either models or template tags – you’ll need to add the package name (e.g., `'django.contrib.redirects'`) to your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) setting and rerun `manage.py migrate`.
  * [The Django admin site](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
  * [`django.contrib.auth`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/)
  * [The contenttypes framework](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/)
  * [The flatpages app](https://docs.djangoproject.com/en/5.0/ref/contrib/flatpages/)
  * [GeoDjango](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/)
  * [`django.contrib.humanize`](https://docs.djangoproject.com/en/5.0/ref/contrib/humanize/)
  * [The messages framework](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/)
  * [`django.contrib.postgres`](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/)
  * [The redirects app](https://docs.djangoproject.com/en/5.0/ref/contrib/redirects/)
  * [The sitemap framework](https://docs.djangoproject.com/en/5.0/ref/contrib/sitemaps/)
  * [The “sites” framework](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/)
  * [The `staticfiles` app](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/)
  * [The syndication feed framework](https://docs.djangoproject.com/en/5.0/ref/contrib/syndication/)


##  `admin`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#admin "Link to this heading")
The automatic Django administrative interface. For more information, see [Tutorial 2](https://docs.djangoproject.com/en/5.0/intro/tutorial02/) and the [admin documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/).
Requires the [auth](https://docs.djangoproject.com/en/5.0/ref/contrib/#auth) and [contenttypes](https://docs.djangoproject.com/en/5.0/ref/contrib/#contenttypes) contrib packages to be installed.
##  `auth`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#auth "Link to this heading")
Django’s authentication framework.
See [User authentication in Django](https://docs.djangoproject.com/en/5.0/topics/auth/).
##  `contenttypes`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#contenttypes "Link to this heading")
A light framework for hooking into “types” of content, where each installed Django model is a separate content type.
See the [contenttypes documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/).
##  `flatpages`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#flatpages "Link to this heading")
A framework for managing “flat” HTML content in a database.
See the [flatpages documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/flatpages/).
Requires the [sites](https://docs.djangoproject.com/en/5.0/ref/contrib/#sites) contrib package to be installed as well.
##  `gis`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#gis "Link to this heading")
A world-class geospatial framework built on top of Django, that enables storage, manipulation and display of spatial data.
See the [GeoDjango](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/) documentation for more.
##  `humanize`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#humanize "Link to this heading")
A set of Django template filters useful for adding a “human touch” to data.
See the [humanize documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/humanize/).
##  `messages`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#messages "Link to this heading")
A framework for storing and retrieving temporary cookie- or session-based messages
See the [messages documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/).
##  `postgres`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#postgres "Link to this heading")
A collection of PostgreSQL specific features.
See the [contrib.postgres documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/).
##  `redirects`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#redirects "Link to this heading")
A framework for managing redirects.
See the [redirects documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/redirects/).
##  `sessions`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#sessions "Link to this heading")
A framework for storing data in anonymous sessions.
See the [sessions documentation](https://docs.djangoproject.com/en/5.0/topics/http/sessions/).
##  `sites`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#sites "Link to this heading")
A light framework that lets you operate multiple websites off of the same database and Django installation. It gives you hooks for associating objects to one or more sites.
See the [sites documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/).
##  `sitemaps`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#sitemaps "Link to this heading")
A framework for generating Google sitemap XML files.
See the [sitemaps documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/sitemaps/).
##  `syndication`[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#syndication "Link to this heading")
A framework for generating syndication feeds, in RSS and Atom, quite easily.
See the [syndication documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/syndication/).
## Other add-ons[¶](https://docs.djangoproject.com/en/5.0/ref/contrib/#other-add-ons "Link to this heading")
If you have an idea for functionality to include in `contrib`, let us know! Code it up, and post it to the [django-users](https://docs.djangoproject.com/en/5.0/internals/mailing-lists/#django-users-mailing-list) mailing list.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/clickjacking/)
[The Django admin site ](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
[](https://docs.djangoproject.com/en/5.0/ref/contrib/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Baltimore Medical Malpractice Lawyers donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [`contrib` packages](https://docs.djangoproject.com/en/5.0/ref/contrib/)
    * [`admin`](https://docs.djangoproject.com/en/5.0/ref/contrib/#admin)
    * [`auth`](https://docs.djangoproject.com/en/5.0/ref/contrib/#auth)
    * [`contenttypes`](https://docs.djangoproject.com/en/5.0/ref/contrib/#contenttypes)
    * [`flatpages`](https://docs.djangoproject.com/en/5.0/ref/contrib/#flatpages)
    * [`gis`](https://docs.djangoproject.com/en/5.0/ref/contrib/#gis)
    * [`humanize`](https://docs.djangoproject.com/en/5.0/ref/contrib/#humanize)
    * [`messages`](https://docs.djangoproject.com/en/5.0/ref/contrib/#messages)
    * [`postgres`](https://docs.djangoproject.com/en/5.0/ref/contrib/#postgres)
    * [`redirects`](https://docs.djangoproject.com/en/5.0/ref/contrib/#redirects)
    * [`sessions`](https://docs.djangoproject.com/en/5.0/ref/contrib/#sessions)
    * [`sites`](https://docs.djangoproject.com/en/5.0/ref/contrib/#sites)
    * [`sitemaps`](https://docs.djangoproject.com/en/5.0/ref/contrib/#sitemaps)
    * [`syndication`](https://docs.djangoproject.com/en/5.0/ref/contrib/#syndication)
    * [Other add-ons](https://docs.djangoproject.com/en/5.0/ref/contrib/#other-add-ons)


### Browse
  * Prev: [Clickjacking Protection](https://docs.djangoproject.com/en/5.0/ref/clickjacking/)
  * Next: [The Django admin site](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * `contrib` packages


### Getting help

[FAQ](https://docs.djangoproject.com/en/5.0/faq/)
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
Offline (Django 5.0): [HTML](https://media.djangoproject.com/docs/django-docs-5.0-en.zip) |
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
