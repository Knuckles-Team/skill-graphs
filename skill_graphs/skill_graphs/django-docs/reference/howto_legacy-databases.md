This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/legacy-databases/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/legacy-databases/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/legacy-databases/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/legacy-databases/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/legacy-databases/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/legacy-databases/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/legacy-databases/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/legacy-databases/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/legacy-databases/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/legacy-databases/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/legacy-databases/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/legacy-databases/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/legacy-databases/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/legacy-databases/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/legacy-databases/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/legacy-databases/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/legacy-databases/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/legacy-databases/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/legacy-databases/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/legacy-databases/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/legacy-databases/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/legacy-databases/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/legacy-databases/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/legacy-databases/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/legacy-databases/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/legacy-databases/)


  * [](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#top)


# How to integrate Django with a legacy database[¶](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#how-to-integrate-django-with-a-legacy-database "Link to this heading")
While Django is best suited for developing new applications, it’s quite possible to integrate it into legacy databases. Django includes a couple of utilities to automate as much of this process as possible.
This document assumes you know the Django basics, as covered in the [tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/).
Once you’ve got Django set up, you’ll follow this general process to integrate with an existing database.
## Give Django your database parameters[¶](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#give-django-your-database-parameters "Link to this heading")
You’ll need to tell Django what your database connection parameters are, and what the name of the database is. Do that by editing the [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) setting and assigning values to the following keys for the `'default'` connection:
  * [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NAME)
  * [`ENGINE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ENGINE)
  * [`USER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USER)
  * [`PASSWORD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PASSWORD)
  * [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST)
  * [`PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PORT)


## Auto-generate the models[¶](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#auto-generate-the-models "Link to this heading")
Django comes with a utility called [`inspectdb`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-inspectdb) that can create models by introspecting an existing database. You can view the output by running this command:
```
$ python manage.py inspectdb

```

Save this as a file by using standard Unix output redirection:
```
$ python manage.py inspectdb > models.py

```

This feature is meant as a shortcut, not as definitive model generation. See the [`documentation of inspectdb`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-inspectdb) for more information.
Once you’ve cleaned up your models, name the file `models.py` and put it in the Python package that holds your app. Then add the app to your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) setting.
By default, [`inspectdb`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-inspectdb) creates unmanaged models. That is, `managed = False` in the model’s `Meta` class tells Django not to manage each table’s creation, modification, and deletion:
```
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = "CENSUS_PERSONS"

```

If you do want to allow Django to manage the table’s lifecycle, you’ll need to change the [`managed`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.managed "django.db.models.Options.managed") option above to `True` (or remove it because `True` is its default value).
## Install the core Django tables[¶](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#install-the-core-django-tables "Link to this heading")
Next, run the [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate) command to install any extra needed database records such as admin permissions and content types:
```
$ python manage.py migrate

```

## Test and tweak[¶](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#test-and-tweak "Link to this heading")
Those are the basic steps – from here you’ll want to tweak the models Django generated until they work the way you’d like. Try accessing your data via the Django database API, and try editing objects via Django’s admin site, and edit the models file accordingly.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/initial-data/)
[How to configure and use logging ](https://docs.djangoproject.com/en/5.0/howto/logging/)
[](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Schwartz Kalina, PLLC donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to integrate Django with a legacy database](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/)
    * [Give Django your database parameters](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#give-django-your-database-parameters)
    * [Auto-generate the models](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#auto-generate-the-models)
    * [Install the core Django tables](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#install-the-core-django-tables)
    * [Test and tweak](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/#test-and-tweak)


### Browse
  * Prev: [How to provide initial data for models](https://docs.djangoproject.com/en/5.0/howto/initial-data/)
  * Next: [How to configure and use logging](https://docs.djangoproject.com/en/5.0/howto/logging/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to integrate Django with a legacy database


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
