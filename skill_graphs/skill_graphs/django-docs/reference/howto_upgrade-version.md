This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/upgrade-version/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/upgrade-version/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/upgrade-version/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/upgrade-version/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/upgrade-version/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/upgrade-version/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/upgrade-version/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/upgrade-version/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/upgrade-version/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/upgrade-version/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/upgrade-version/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/upgrade-version/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/upgrade-version/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/upgrade-version/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/upgrade-version/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/upgrade-version/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/upgrade-version/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/upgrade-version/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/upgrade-version/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/upgrade-version/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/upgrade-version/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/upgrade-version/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/upgrade-version/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/upgrade-version/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/upgrade-version/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/upgrade-version/)


  * [](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#top)


# How to upgrade Django to a newer version[¶](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#how-to-upgrade-django-to-a-newer-version "Link to this heading")
While it can be a complex process at times, upgrading to the latest Django version has several benefits:
  * New features and improvements are added.
  * Bugs are fixed.
  * Older version of Django will eventually no longer receive security updates. (see [Supported versions](https://docs.djangoproject.com/en/5.0/internals/release-process/#supported-versions-policy)).
  * Upgrading as each new Django release is available makes future upgrades less painful by keeping your code base up to date.


Here are some things to consider to help make your upgrade process as smooth as possible.
## Required Reading[¶](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#required-reading "Link to this heading")
If it’s your first time doing an upgrade, it is useful to read the [guide on the different release processes](https://docs.djangoproject.com/en/5.0/internals/release-process/).
Afterward, you should familiarize yourself with the changes that were made in the new Django version(s):
  * Read the [release notes](https://docs.djangoproject.com/en/5.0/releases/) for each ‘final’ release from the one after your current Django version, up to and including the version to which you plan to upgrade.
  * Look at the [deprecation timeline](https://docs.djangoproject.com/en/5.0/internals/deprecation/) for the relevant versions.


Pay particular attention to backwards incompatible changes to get a clear idea of what will be needed for a successful upgrade.
If you’re upgrading through more than one feature version (e.g. 2.0 to 2.2), it’s usually easier to upgrade through each feature release incrementally (2.0 to 2.1 to 2.2) rather than to make all the changes for each feature release at once. For each feature release, use the latest patch release (e.g. for 2.1, use 2.1.15).
The same incremental upgrade approach is recommended when upgrading from one LTS to the next.
## Dependencies[¶](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#dependencies "Link to this heading")
In most cases it will be necessary to upgrade to the latest version of your Django-related dependencies as well. If the Django version was recently released or if some of your dependencies are not well-maintained, some of your dependencies may not yet support the new Django version. In these cases you may have to wait until new versions of your dependencies are released.
## Resolving deprecation warnings[¶](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#resolving-deprecation-warnings "Link to this heading")
Before upgrading, it’s a good idea to resolve any deprecation warnings raised by your project while using your current version of Django. Fixing these warnings before upgrading ensures that you’re informed about areas of the code that need altering.
In Python, deprecation warnings are silenced by default. You must turn them on using the `-Wa` Python command line option or the
/ 
```
$ python -Wa manage.py test

```

```
...\> py -Wa manage.py test

```

If you’re not using the Django test runner, you may need to also ensure that any console output is not captured which would hide deprecation warnings. For example, if you use
```
$ PYTHONWARNINGS=always pytest tests --capture=no

```

Resolve any deprecation warnings with your current version of Django before continuing the upgrade process.
Third party applications might use deprecated APIs in order to support multiple versions of Django, so deprecation warnings in packages you’ve installed don’t necessarily indicate a problem. If a package doesn’t support the latest version of Django, consider raising an issue or sending a pull request for it.
## Installation[¶](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#installation "Link to this heading")
Once you’re ready, it is time to [install the new Django version](https://docs.djangoproject.com/en/5.0/topics/install/). If you are using a
If you installed Django with `--upgrade` or `-U` flag:
/ 
```
$ python -m pip install -U Django

```

```
...\> py -m pip install -U Django

```

## Testing[¶](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#testing "Link to this heading")
When the new environment is set up, [run the full test suite](https://docs.djangoproject.com/en/5.0/topics/testing/overview/) for your application. Again, it’s useful to turn on deprecation warnings on so they’re shown in the test output (you can also use the flag if you test your app manually using `manage.py runserver`):
/ 
```
$ python -Wa manage.py test

```

```
...\> py -Wa manage.py test

```

After you have run the tests, fix any failures. While you have the release notes fresh in your mind, it may also be a good time to take advantage of new features in Django by refactoring your code to eliminate any deprecation warnings.
## Deployment[¶](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#deployment "Link to this heading")
When you are sufficiently confident your app works with the new version of Django, you’re ready to go ahead and [deploy](https://docs.djangoproject.com/en/5.0/howto/deployment/) your upgraded Django project.
If you are using caching provided by Django, you should consider clearing your cache after upgrading. Otherwise you may run into problems, for example, if you are caching pickled objects as these objects are not guaranteed to be pickle-compatible across Django versions. A past instance of incompatibility was caching pickled [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") objects, either directly or indirectly via the [`cache_page()`](https://docs.djangoproject.com/en/5.0/topics/cache/#django.views.decorators.cache.cache_page "django.views.decorators.cache.cache_page") decorator.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
[How to manage error reporting ](https://docs.djangoproject.com/en/5.0/howto/error-reporting/)
[](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Dominion Roofing Company, Inc. donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to upgrade Django to a newer version](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/)
    * [Required Reading](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#required-reading)
    * [Dependencies](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#dependencies)
    * [Resolving deprecation warnings](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#resolving-deprecation-warnings)
    * [Installation](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#installation)
    * [Testing](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#testing)
    * [Deployment](https://docs.djangoproject.com/en/5.0/howto/upgrade-version/#deployment)


### Browse
  * Prev: [Deployment checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
  * Next: [How to manage error reporting](https://docs.djangoproject.com/en/5.0/howto/error-reporting/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to upgrade Django to a newer version


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
