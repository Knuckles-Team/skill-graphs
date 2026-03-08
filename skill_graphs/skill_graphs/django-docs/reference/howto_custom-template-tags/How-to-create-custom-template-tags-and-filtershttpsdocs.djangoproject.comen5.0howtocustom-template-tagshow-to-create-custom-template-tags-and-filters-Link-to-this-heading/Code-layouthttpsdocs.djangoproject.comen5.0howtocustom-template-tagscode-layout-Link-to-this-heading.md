## Code layout[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#code-layout "Link to this heading")
The most common place to specify custom template tags and filters is inside a Django app. If they relate to an existing app, it makes sense to bundle them there; otherwise, they can be added to a new app. When a Django app is added to [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS), any tags it defines in the conventional location described below are automatically made available to load within templates.
The app should contain a `templatetags` directory, at the same level as `models.py`, `views.py`, etc. If this doesn’t already exist, create it - don’t forget the `__init__.py` file to ensure the directory is treated as a Python package.
Development server won’t automatically restart
After adding the `templatetags` module, you will need to restart your server before you can use the tags or filters in templates.
Your custom tags and filters will live in a module inside the `templatetags` directory. The name of the module file is the name you’ll use to load the tags later, so be careful to pick a name that won’t clash with custom tags and filters in another app.
For example, if your custom tags/filters are in a file called `poll_extras.py`, your app layout might look like this:
```
polls/
    __init__.py
    models.py
    templatetags/
        __init__.py
        poll_extras.py
    views.py

```

And in your template you would use the following:
```
{% load poll_extras %}

```

The app that contains the custom tags must be in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) in order for the [`{% load %}`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-load) tag to work. This is a security feature: It allows you to host Python code for many template libraries on a single host machine without enabling access to all of them for every Django installation.
There’s no limit on how many modules you put in the `templatetags` package. Just keep in mind that a [`{% load %}`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-load) statement will load tags/filters for the given Python module name, not the name of the app.
To be a valid tag library, the module must contain a module-level variable named `register` that is a `template.Library` instance, in which all the tags and filters are registered. So, near the top of your module, put the following:
```
from django import template

register = template.Library()

```

Alternatively, template tag modules can be registered through the `'libraries'` argument to [`DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates"). This is useful if you want to use a different label from the template tag module name when loading template tags. It also enables you to register tags without installing an application.
Behind the scenes
For a ton of examples, read the source code for Django’s default filters and tags. They’re in
For more information on the [`load`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-load) tag, read its documentation.
