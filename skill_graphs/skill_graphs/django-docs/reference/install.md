This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/install/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/install/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/install/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/install/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/install/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/install/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/install/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/install/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/install/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/install/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/install/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/install/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/install/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/install/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/install/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/install/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/install/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/install/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/install/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/install/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/install/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/install/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/install/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/install/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/install/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/install/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/install/)


  * [](https://docs.djangoproject.com/en/5.0/topics/install/#top)


# How to install Django[¶](https://docs.djangoproject.com/en/5.0/topics/install/#how-to-install-django "Link to this heading")
This document will get you up and running with Django.
## Install Python[¶](https://docs.djangoproject.com/en/5.0/topics/install/#install-python "Link to this heading")
Django is a Python web framework. See [What Python version can I use with Django?](https://docs.djangoproject.com/en/5.0/faq/install/#faq-python-version-support) for details.
Get the latest version of Python at
Python on Windows
If you are just starting with Django and using Windows, you may find [How to install Django on Windows](https://docs.djangoproject.com/en/5.0/howto/windows/) useful.
## Install Apache and `mod_wsgi`[¶](https://docs.djangoproject.com/en/5.0/topics/install/#install-apache-and-mod-wsgi "Link to this heading")
If you just want to experiment with Django, skip ahead to the next section; Django includes a lightweight web server you can use for testing, so you won’t need to set up Apache until you’re ready to deploy Django in production.
If you want to use Django on a production site, use
See [How to use Django with mod_wsgi](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/modwsgi/) for information on how to configure mod_wsgi once you have it installed.
If you can’t use mod_wsgi for some reason, fear not: Django supports many other deployment options. One is [uWSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/uwsgi/); it works very well with
## Get your database running[¶](https://docs.djangoproject.com/en/5.0/topics/install/#get-your-database-running "Link to this heading")
If you plan to use Django’s database API functionality, you’ll need to make sure a database server is running. Django supports many different database servers and is officially supported with
If you are developing a small project or something you don’t plan to deploy in a production environment, SQLite is generally the best option as it doesn’t require running a separate server. However, SQLite has many differences from other databases, so if you are working on something substantial, it’s recommended to develop with the same database that you plan on using in production.
In addition to the officially supported databases, there are [backends provided by 3rd parties](https://docs.djangoproject.com/en/5.0/ref/databases/#third-party-notes) that allow you to use other databases with Django.
In addition to a database backend, you’ll need to make sure your Python database bindings are installed.
  * If you’re using PostgreSQL, you’ll need the [PostgreSQL notes](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes) for further details.
  * If you’re using MySQL or MariaDB, you’ll need a [DB API driver](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-db-api-drivers) like `mysqlclient`. See [notes for the MySQL backend](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-notes) for details.
  * If you’re using SQLite you might want to read the [SQLite backend notes](https://docs.djangoproject.com/en/5.0/ref/databases/#sqlite-notes).
  * If you’re using Oracle, you’ll need to install [notes for the Oracle backend](https://docs.djangoproject.com/en/5.0/ref/databases/#oracle-notes) for details regarding supported versions of both Oracle and `oracledb`.
  * If you’re using an unofficial 3rd party backend, please consult the documentation provided for any additional requirements.


If you plan to use Django’s `manage.py migrate` command to automatically create database tables for your models (after first installing Django and creating a project), you’ll need to ensure that Django has permission to create and alter tables in the database you’re using; if you plan to manually create the tables, you can grant Django `SELECT`, `INSERT`, `UPDATE` and `DELETE` permissions. After creating a database user with these permissions, you’ll specify the details in your project’s settings file, see [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) for details.
If you’re using Django’s [testing framework](https://docs.djangoproject.com/en/5.0/topics/testing/) to test database queries, Django will need permission to create a test database.
## Install the Django code[¶](https://docs.djangoproject.com/en/5.0/topics/install/#install-the-django-code "Link to this heading")
Installation instructions are slightly different depending on whether you’re installing a distribution-specific package, downloading the latest official release, or fetching the latest development version.
### Installing an official release with `pip`[¶](https://docs.djangoproject.com/en/5.0/topics/install/#installing-an-official-release-with-pip "Link to this heading")
This is the recommended way to install Django.
  1. Install `pip` installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.
  2. Take a look at [contributing tutorial](https://docs.djangoproject.com/en/5.0/intro/contributing/) walks through how to create a virtual environment.
  3. After you’ve created and activated a virtual environment, enter the command:
/ 
```
$ python -m pip install Django

```

```
...\> py -m pip install Django

```



### Installing a distribution-specific package[¶](https://docs.djangoproject.com/en/5.0/topics/install/#installing-a-distribution-specific-package "Link to this heading")
Check the [distribution specific notes](https://docs.djangoproject.com/en/5.0/misc/distributions/) to see if your platform/distribution provides official Django packages/installers. Distribution-provided packages will typically allow for automatic installation of dependencies and supported upgrade paths; however, these packages will rarely contain the latest release of Django.
### Installing the development version[¶](https://docs.djangoproject.com/en/5.0/topics/install/#installing-the-development-version "Link to this heading")
Tracking Django development
If you decide to use the latest development version of Django, you’ll want to pay close attention to [the development timeline](https://code.djangoproject.com/timeline), and you’ll want to keep an eye on the [release notes for the upcoming release](https://docs.djangoproject.com/en/5.0/releases/#development-release-notes). This will help you stay on top of any new features you might want to use, as well as any changes you’ll need to make to your code when updating your copy of Django. (For stable releases, any necessary changes are documented in the release notes.)
If you’d like to be able to update your Django code occasionally with the latest bug fixes and improvements, follow these instructions:
  1. Make sure that you have `git help` at a shell prompt to test this.)
  2. Check out Django’s main development branch like so:
/ 
```
$ git clone https://github.com/django/django.git

```

```
...\> git clone https://github.com/django/django.git

```

This will create a directory `django` in your current directory.
  3. Make sure that the Python interpreter can load Django’s code. The most convenient way to do this is to use a virtual environment and [contributing tutorial](https://docs.djangoproject.com/en/5.0/intro/contributing/) walks through how to create a virtual environment.
  4. After setting up and activating the virtual environment, run the following command:
/ 
```
$ python -m pip install -e django/

```

```
...\> py -m pip install -e django\

```

This will make Django’s code importable, and will also make the `django-admin` utility command available. In other words, you’re all set!


When you want to update your copy of the Django source code, run the command `git pull` from within the `django` directory. When you do this, Git will download any changes.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/)
[Models and databases ](https://docs.djangoproject.com/en/5.0/topics/db/)
[](https://docs.djangoproject.com/en/5.0/topics/install/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Unchained donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to install Django](https://docs.djangoproject.com/en/5.0/topics/install/)
    * [Install Python](https://docs.djangoproject.com/en/5.0/topics/install/#install-python)
    * [Install Apache and `mod_wsgi`](https://docs.djangoproject.com/en/5.0/topics/install/#install-apache-and-mod-wsgi)
    * [Get your database running](https://docs.djangoproject.com/en/5.0/topics/install/#get-your-database-running)
    * [Install the Django code](https://docs.djangoproject.com/en/5.0/topics/install/#install-the-django-code)
      * [Installing an official release with `pip`](https://docs.djangoproject.com/en/5.0/topics/install/#installing-an-official-release-with-pip)
      * [Installing a distribution-specific package](https://docs.djangoproject.com/en/5.0/topics/install/#installing-a-distribution-specific-package)
      * [Installing the development version](https://docs.djangoproject.com/en/5.0/topics/install/#installing-the-development-version)


### Browse
  * Prev: [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
  * Next: [Models and databases](https://docs.djangoproject.com/en/5.0/topics/db/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * How to install Django


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
