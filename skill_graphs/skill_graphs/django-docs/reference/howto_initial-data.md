This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/initial-data/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/initial-data/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/initial-data/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/initial-data/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/initial-data/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/initial-data/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/initial-data/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/initial-data/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/initial-data/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/initial-data/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/initial-data/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/initial-data/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/initial-data/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/initial-data/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/initial-data/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/initial-data/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/initial-data/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/initial-data/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/initial-data/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/initial-data/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/initial-data/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/initial-data/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/initial-data/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/initial-data/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/initial-data/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/initial-data/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/initial-data/)


  * [](https://docs.djangoproject.com/en/5.0/howto/initial-data/#top)


# How to provide initial data for models[¶](https://docs.djangoproject.com/en/5.0/howto/initial-data/#how-to-provide-initial-data-for-models "Link to this heading")
It’s sometimes useful to prepopulate your database with hard-coded data when you’re first setting up an app. You can provide initial data with migrations or fixtures.
## Provide initial data with migrations[¶](https://docs.djangoproject.com/en/5.0/howto/initial-data/#provide-initial-data-with-migrations "Link to this heading")
To automatically load initial data for an app, create a [data migration](https://docs.djangoproject.com/en/5.0/topics/migrations/#data-migrations). Migrations are run when setting up the test database, so the data will be available there, subject to [some limitations](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#test-case-serialized-rollback).
## Provide data with fixtures[¶](https://docs.djangoproject.com/en/5.0/howto/initial-data/#provide-data-with-fixtures "Link to this heading")
You can also provide data using [fixtures](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation), however, this data isn’t loaded automatically, except if you use [`TransactionTestCase.fixtures`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures "django.test.TransactionTestCase.fixtures").
A fixture is a collection of data that Django knows how to import into a database. The most straightforward way of creating a fixture if you’ve already got some data is to use the [`manage.py dumpdata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dumpdata) command. Or, you can write fixtures by hand; fixtures can be written as JSON, XML or YAML (with [serialization documentation](https://docs.djangoproject.com/en/5.0/topics/serialization/) has more details about each of these supported [serialization formats](https://docs.djangoproject.com/en/5.0/topics/serialization/#serialization-formats).
As an example, though, here’s what a fixture for a `Person` model might look like in JSON:
```
[
  {
    "model": "myapp.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapp.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]

```

And here’s that same fixture as YAML:
```
- model: myapp.person
  pk: 1
  fields:
    first_name: John
    last_name: Lennon
- model: myapp.person
  pk: 2
  fields:
    first_name: Paul
    last_name: McCartney

```

You’ll store this data in a `fixtures` directory inside your app.
You can load data by calling [`manage.py loaddata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-loaddata) `<fixturename>`, where `<fixturename>` is the name of the fixture file you’ve created. Each time you run [`loaddata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-loaddata), the data will be read from the fixture and reloaded into the database. Note this means that if you change one of the rows created by a fixture and then run [`loaddata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-loaddata) again, you’ll wipe out any changes you’ve made.
### Tell Django where to look for fixture files[¶](https://docs.djangoproject.com/en/5.0/howto/initial-data/#tell-django-where-to-look-for-fixture-files "Link to this heading")
By default, Django looks for fixtures in the `fixtures` directory inside each app for, so the command `loaddata sample` will find the file `my_app/fixtures/sample.json`. This works with relative paths as well, so `loaddata my_app/sample` will find the file `my_app/fixtures/my_app/sample.json`.
Django also looks for fixtures in the list of directories provided in the [`FIXTURE_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FIXTURE_DIRS) setting.
To completely prevent default search form happening, use an absolute path to specify the location of your fixture file, e.g. `loaddata /path/to/sample`.
Namespace your fixture files
Django will use the first fixture file it finds whose name matches, so if you have fixture files with the same name in different applications, you will be unable to distinguish between them in your `loaddata` commands. The easiest way to avoid this problem is by _namespacing_ your fixture files. That is, by putting them inside a directory named for their application, as in the relative path example above.
See also
Fixtures are also used by the [testing framework](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#topics-testing-fixtures) to help set up a consistent test environment.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/error-reporting/)
[How to integrate Django with a legacy database ](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/)
[](https://docs.djangoproject.com/en/5.0/howto/initial-data/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ JUJ8EjxYaGvH donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to provide initial data for models](https://docs.djangoproject.com/en/5.0/howto/initial-data/)
    * [Provide initial data with migrations](https://docs.djangoproject.com/en/5.0/howto/initial-data/#provide-initial-data-with-migrations)
    * [Provide data with fixtures](https://docs.djangoproject.com/en/5.0/howto/initial-data/#provide-data-with-fixtures)
      * [Tell Django where to look for fixture files](https://docs.djangoproject.com/en/5.0/howto/initial-data/#tell-django-where-to-look-for-fixture-files)


### Browse
  * Prev: [How to manage error reporting](https://docs.djangoproject.com/en/5.0/howto/error-reporting/)
  * Next: [How to integrate Django with a legacy database](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to provide initial data for models


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
