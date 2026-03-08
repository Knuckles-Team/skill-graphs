[Skip to main content](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/intro/tutorial01/)
  * [sv](https://docs.djangoproject.com/sv/6.0/intro/tutorial01/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/intro/tutorial01/)
  * [pl](https://docs.djangoproject.com/pl/6.0/intro/tutorial01/)
  * [ko](https://docs.djangoproject.com/ko/6.0/intro/tutorial01/)
  * [ja](https://docs.djangoproject.com/ja/6.0/intro/tutorial01/)
  * [it](https://docs.djangoproject.com/it/6.0/intro/tutorial01/)
  * [id](https://docs.djangoproject.com/id/6.0/intro/tutorial01/)
  * [fr](https://docs.djangoproject.com/fr/6.0/intro/tutorial01/)
  * [es](https://docs.djangoproject.com/es/6.0/intro/tutorial01/)
  * [el](https://docs.djangoproject.com/el/6.0/intro/tutorial01/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/intro/tutorial01/)
  * [5.2](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
  * [5.1](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
  * [5.0](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
  * [4.2](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
  * [4.1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
  * [4.0](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
  * [3.2](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
  * [3.1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
  * [3.0](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
  * [2.2](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
  * [2.1](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
  * [2.0](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
  * [1.11](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
  * [1.10](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
  * [1.8](https://docs.djangoproject.com/en/1.8/intro/tutorial01/)


  * [](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#top)


# Writing your first Django app, part 1[¶](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#writing-your-first-django-app-part-1 "Link to this heading")
Let’s learn by example.
Throughout this tutorial, we’ll walk you through the creation of a basic poll application.
It’ll consist of two parts:
  * A public site that lets people view polls and vote in them.
  * An admin site that lets you add, change, and delete polls.


We’ll assume you have [Django installed](https://docs.djangoproject.com/en/6.0/intro/install/) already. You can tell Django is installed and which version by running the following command in a shell prompt (indicated by the $ prefix):
/ 
```
$ python -m django --version

```

```
...\> py -m django --version

```

If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.
This tutorial is written for Django 6.0, which supports Python 3.12 and later. If the Django version doesn’t match, you can refer to the tutorial for your version of Django by using the version switcher at the bottom right corner of this page, or update Django to the newest version. If you’re using an older version of Python, check [What Python version can I use with Django?](https://docs.djangoproject.com/en/6.0/faq/install/#faq-python-version-support) to find a compatible version of Django.
Where to get help:
If you’re having trouble going through this tutorial, please head over to the [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/) section of the FAQ.
## Creating a project[¶](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#creating-a-project "Link to this heading")
If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django [project](https://docs.djangoproject.com/en/6.0/glossary/#term-project) – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.
From the command line, `cd` into a directory where you’d like to store your code and run the following command to bootstrap a new Django project:
/ 
```
$ django-admin startproject mysite djangotutorial

```

```
...\> django-admin startproject mysite djangotutorial

```

This will create a directory `djangotutorial` with a project called `mysite` inside. The directory name doesn’t matter to Django; you can rename it to anything you like. If it didn’t work, see [Problems running django-admin](https://docs.djangoproject.com/en/6.0/faq/troubleshooting/#troubleshooting-django-admin).
Note
You’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like `django` (which will conflict with Django itself) or `test` (which conflicts with a built-in Python package).
Let’s look at what [`startproject`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) created:
```
djangotutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

```

These files are:
  * `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [django-admin and manage.py](https://docs.djangoproject.com/en/6.0/ref/django-admin/).
  * `mysite/`: A directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `mysite.urls`).
  * `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read
  * `mysite/settings.py`: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/6.0/topics/settings/) will tell you all about how settings work.
  * `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/6.0/topics/http/urls/).
  * `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/) for more details.
  * `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/) for more details.


## The development server[¶](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#the-development-server "Link to this heading")
Let’s verify your Django project works. Change into the `djangotutorial` directory, if you haven’t already, and run the following commands:
/ 
```
$ python manage.py runserver

```

```
...\> py manage.py runserver

```

You’ll see the following output on the command line:
```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are
applied. Run 'python manage.py migrate' to apply them.

March 06, 2026 - 15:50:53
Django version 6.0, using settings 'mysite.settings'
Starting development server at https://docs.djangoproject.com/en/[](https://docs.djangoproject.com/en/)6.0/howto/deployment/
```

Note
Ignore the warning about unapplied database migrations for now; we’ll deal with the database shortly.
Now that the server’s running, visit
You’ve started the Django development server, a lightweight web server written purely in Python. We’ve included this with Django so you can develop things rapidly, without having to deal with configuring a production server – such as Apache – until you’re ready for production.
Now’s a good time to note: **don’t** use this server in anything resembling a production environment. It’s intended only for use while developing. (We’re in the business of making web frameworks, not web servers.)
(To serve the site on a different port, see the [`runserver`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-runserver) reference.)
Automatic reloading of [`runserver`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-runserver)
The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.
## Creating the Polls app[¶](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#creating-the-polls-app "Link to this heading")
Now that your environment – a “project” – is set up, you’re set to start doing work.
Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.
Projects vs. apps
What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
Your apps can live anywhere in your `djangotutorial` folder.
To create your app, make sure you’re in the same directory as `manage.py` and type this command:
/ 
```
$ python manage.py startapp polls

```

```
...\> py manage.py startapp polls

```

That’ll create a directory `polls`, which is laid out like this:
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

```

This directory structure will house the poll application.
## Write your first view[¶](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#write-your-first-view "Link to this heading")
Let’s write the first view. Open the file `polls/views.py` and put the following Python code in it:
`polls/views.py`[¶](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#id1 "Link to this code")
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

```

This is the most basic view possible in Django. To access it in a browser, we need to map it to a URL - and for this we need to define a URL configuration, or “URLconf” for short. These URL configurations are defined inside each Django app, and they are Python files named `urls.py`.
To define a URLconf for the `polls` app, create a file `polls/urls.py` with the following content:
`polls/urls.py`[¶](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#id2 "Link to this code")
```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

```

Your app directory should now look like:
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py

```

The next step is to configure the root URLconf in the `mysite` project to include the URLconf defined in `polls.urls`. To do this, add an import for `django.urls.include` in `mysite/urls.py` and insert an [`include()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.include "django.urls.include") in the `urlpatterns` list, so you have:
`mysite/urls.py`[¶](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#id3 "Link to this code")
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

```

The [`path()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.path "django.urls.path") function expects at least two arguments: `route` and `view`. The [`include()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.include "django.urls.include") function allows referencing other URLconfs. Whenever Django encounters [`include()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.include "django.urls.include"), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
The idea behind [`include()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.include "django.urls.include") is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (`polls/urls.py`), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.
When to use [`include()`](https://docs.djangoproject.com/en/6.0/ref/urls/#django.urls.include "django.urls.include")
You should always use `include()` when you include other URL patterns. The only exception is `admin.site.urls`, which is a pre-built URLconf provided by Django for the default admin site.
You have now wired an `index` view into the URLconf. Verify it’s working with the following command:
/ 
```
$ python manage.py runserver

```

```
...\> py manage.py runserver

```

Go to _Hello, world. You’re at the polls index._ ”, which you defined in the `index` view.
Page not found?
If you get an error page here, check that you’re going to
When you’re comfortable with the basic request and response flow, read [part 2 of this tutorial](https://docs.djangoproject.com/en/6.0/intro/tutorial02/) to start working with the database.
Previous page and next page
[](https://docs.djangoproject.com/en/6.0/intro/install/)
[Writing your first Django app, part 2 ](https://docs.djangoproject.com/en/6.0/intro/tutorial02/)
[](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Portmoni donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Writing your first Django app, part 1](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)
    * [Creating a project](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#creating-a-project)
    * [The development server](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#the-development-server)
    * [Creating the Polls app](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#creating-the-polls-app)
    * [Write your first view](https://docs.djangoproject.com/en/6.0/intro/tutorial01/#write-your-first-view)


### Browse
  * Prev: [Quick install guide](https://docs.djangoproject.com/en/6.0/intro/install/)
  * Next: [Writing your first Django app, part 2](https://docs.djangoproject.com/en/6.0/intro/tutorial02/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [Getting started](https://docs.djangoproject.com/en/6.0/intro/)
      * Writing your first Django app, part 1


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
