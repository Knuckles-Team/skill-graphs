This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/templates/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/templates/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/templates/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/templates/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/templates/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/templates/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/templates/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/templates/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/templates/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/templates/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/templates/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/templates/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/templates/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/templates/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/templates/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/templates/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/templates/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/templates/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/templates/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/templates/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/templates/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/templates/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/templates/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/templates/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/templates/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/templates/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/templates/)


  * [](https://docs.djangoproject.com/en/5.0/topics/templates/#top)


# Templates[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#module-django.template "Link to this heading")
Being a web framework, Django needs a convenient way to generate HTML dynamically. The most common approach relies on templates. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. For a hands-on example of creating HTML pages with templates, see [Tutorial 3](https://docs.djangoproject.com/en/5.0/intro/tutorial03/).
A Django project can be configured with one or several template engines (or even zero if you don’t use templates). Django ships built-in backends for its own template system, creatively called the Django template language (DTL), and for the popular alternative [Custom template backend](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/)
Django defines a standard API for loading and rendering templates regardless of the backend. Loading consists of finding the template for a given identifier and preprocessing it, usually compiling it to an in-memory representation. Rendering means interpolating the template with context data and returning the resulting string.
The [Django template language](https://docs.djangoproject.com/en/5.0/ref/templates/language/) is Django’s own template system. Until Django 1.8 it was the only built-in option available. It’s a good template library even though it’s fairly opinionated and sports a few idiosyncrasies. If you don’t have a pressing reason to choose another backend, you should use the DTL, especially if you’re writing a pluggable application and you intend to distribute templates. Django’s contrib apps that include templates, like [django.contrib.admin](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/), use the DTL.
For historical reasons, both the generic support for template engines and the implementation of the Django template language live in the `django.template` namespace.
Warning
The template system isn’t safe against untrusted template authors. For example, a site shouldn’t allow its users to provide their own templates, since template authors can do things like perform XSS attacks and access properties of template variables that may contain sensitive information.
## The Django template language[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#the-django-template-language "Link to this heading")
### Syntax[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#syntax "Link to this heading")
About this section
This is an overview of the Django template language’s syntax. For details see the [language syntax reference](https://docs.djangoproject.com/en/5.0/ref/templates/language/).
A Django template is a text document or a Python string marked-up using the Django template language. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.
A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags. Everything else is output as is.
The syntax of the Django template language involves four constructs.
#### Variables[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#variables "Link to this heading")
A variable outputs a value from the context, which is a dict-like object mapping keys to values.
Variables are surrounded by `{{` and `}}` like this:
```
My first name is {{ first_name }}. My last name is {{ last_name }}.

```

With a context of `{'first_name': 'John', 'last_name': 'Doe'}`, this template renders to:
```
My first name is John. My last name is Doe.

```

Dictionary lookup, attribute lookup and list-index lookups are implemented with a dot notation:
```
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}

```

If a variable resolves to a callable, the template system will call it with no arguments and use its result instead of the callable.
#### Tags[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#tags "Link to this heading")
Tags provide arbitrary logic in the rendering process.
This definition is deliberately vague. For example, a tag can output content, serve as a control structure e.g. an “if” statement or a “for” loop, grab content from a database, or even enable access to other template tags.
Tags are surrounded by `{%` and `%}` like this:
```
{% csrf_token %}

```

Most tags accept arguments:
```
{% cycle 'odd' 'even' %}

```

Some tags require beginning and ending tags:
```
{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}

```

A [reference of built-in tags](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#ref-templates-builtins-tags) is available as well as [instructions for writing custom tags](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#howto-writing-custom-template-tags).
#### Filters[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#filters "Link to this heading")
Filters transform the values of variables and tag arguments.
They look like this:
```
{{ django|title }}

```

With a context of `{'django': 'the web framework for perfectionists with deadlines'}`, this template renders to:
```
The Web Framework For Perfectionists With Deadlines

```

Some filters take an argument:
```
{{ my_date|date:"Y-m-d" }}

```

A [reference of built-in filters](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#ref-templates-builtins-filters) is available as well as [instructions for writing custom filters](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#howto-writing-custom-template-filters).
#### Comments[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#comments "Link to this heading")
Comments look like this:
```
{# this won't be rendered #}

```

A [`{% comment %}`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-comment) tag provides multi-line comments.
### Components[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#components "Link to this heading")
About this section
This is an overview of the Django template language’s APIs. For details see the [API reference](https://docs.djangoproject.com/en/5.0/ref/templates/api/).
#### Engine[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#engine "Link to this heading")
[`django.template.Engine`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Engine "django.template.Engine") encapsulates an instance of the Django template system. The main reason for instantiating an [`Engine`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Engine "django.template.Engine") directly is to use the Django template language outside of a Django project.
[`django.template.backends.django.DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") is a thin wrapper adapting [`django.template.Engine`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Engine "django.template.Engine") to Django’s template backend API.
#### Template[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#template "Link to this heading")
[`django.template.Template`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Template "django.template.Template") represents a compiled template. Templates are obtained with [`Engine.get_template()`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Engine.get_template "django.template.Engine.get_template") or [`Engine.from_string()`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Engine.from_string "django.template.Engine.from_string").
Likewise `django.template.backends.django.Template` is a thin wrapper adapting [`django.template.Template`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Template "django.template.Template") to the common template API.
#### Context[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#context "Link to this heading")
[`django.template.Context`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Context "django.template.Context") holds some metadata in addition to the context data. It is passed to [`Template.render()`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Template.render "django.template.Template.render") for rendering a template.
[`django.template.RequestContext`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.RequestContext "django.template.RequestContext") is a subclass of [`Context`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Context "django.template.Context") that stores the current [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") and runs template context processors.
The common API doesn’t have an equivalent concept. Context data is passed in a plain [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") is passed separately if needed.
#### Loaders[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#loaders "Link to this heading")
Template loaders are responsible for locating templates, loading them, and returning [`Template`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Template "django.template.Template") objects.
Django provides several [built-in template loaders](https://docs.djangoproject.com/en/5.0/ref/templates/api/#template-loaders) and supports [custom template loaders](https://docs.djangoproject.com/en/5.0/ref/templates/api/#custom-template-loaders).
#### Context processors[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#context-processors "Link to this heading")
Context processors are functions that receive the current [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") as an argument and return a
Their main use is to add common data shared by all templates to the context without repeating code in every view.
Django provides many [built-in context processors](https://docs.djangoproject.com/en/5.0/ref/templates/api/#context-processors), and you can implement your own additional context processors, too.
## Support for template engines[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#support-for-template-engines "Link to this heading")
### Configuration[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#configuration "Link to this heading")
Templates engines are configured with the [`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES) setting. It’s a list of configurations, one for each engine. The default value is empty. The `settings.py` generated by the [`startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) command defines a more useful value:
```
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            # ... some options here ...
        },
    },
]

```

[`BACKEND`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-BACKEND) is a dotted Python path to a template engine class implementing Django’s template backend API. The built-in backends are [`django.template.backends.django.DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") and [`django.template.backends.jinja2.Jinja2`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.jinja2.Jinja2 "django.template.backends.jinja2.Jinja2").
Since most engines load templates from files, the top-level configuration for each engine contains two common settings:
  * [`DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-DIRS) defines a list of directories where the engine should look for template source files, in search order.
  * [`APP_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-APP_DIRS) tells whether the engine should look for templates inside installed applications. Each backend defines a conventional name for the subdirectory inside applications where its templates should be stored.


While uncommon, it’s possible to configure several instances of the same backend with different options. In that case you should define a unique [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-NAME) for each engine.
[`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-OPTIONS) contains backend-specific settings.
### Usage[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#module-django.template.loader "Link to this heading")
The `django.template.loader` module defines two functions to load templates.

get_template(_template_name_ , _using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/loader/#get_template)[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.get_template "Link to this definition")

This function loads the template with the given name and returns a `Template` object.
The exact type of the return value depends on the backend that loaded the template. Each backend has its own `Template` class.
`get_template()` tries each template engine in order until one succeeds. If the template cannot be found, it raises [`TemplateDoesNotExist`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.TemplateDoesNotExist "django.template.TemplateDoesNotExist"). If the template is found but contains invalid syntax, it raises [`TemplateSyntaxError`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.TemplateSyntaxError "django.template.TemplateSyntaxError").
How templates are searched and loaded depends on each engine’s backend and configuration.
If you want to restrict the search to a particular template engine, pass the engine’s [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-NAME) in the `using` argument.

select_template(_template_name_list_ , _using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/loader/#select_template)[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.select_template "Link to this definition")

`select_template()` is just like `get_template()`, except it takes a list of template names. It tries each name in order and returns the first template that exists.
If loading a template fails, the following two exceptions, defined in `django.template`, may be raised:

_exception_ TemplateDoesNotExist(_msg_ , _tried =None_, _backend =None_, _chain =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/exceptions/#TemplateDoesNotExist)[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.TemplateDoesNotExist "Link to this definition")

This exception is raised when a template cannot be found. It accepts the following optional arguments for populating the [template postmortem](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#template-postmortem) on the debug page:

`backend`

The template backend instance from which the exception originated.

`tried`

A list of sources that were tried when finding the template. This is formatted as a list of tuples containing `(origin, status)`, where `origin` is an [origin-like](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#template-origin-api) object and `status` is a string with the reason the template wasn’t found.

`chain`

A list of intermediate [`TemplateDoesNotExist`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.TemplateDoesNotExist "django.template.TemplateDoesNotExist") exceptions raised when trying to load a template. This is used by functions, such as [`get_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template"), that try to load a given template from multiple engines.

_exception_ TemplateSyntaxError(_msg_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/exceptions/#TemplateSyntaxError)[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.TemplateSyntaxError "Link to this definition")

This exception is raised when a template was found but contains errors.
`Template` objects returned by `get_template()` and `select_template()` must provide a `render()` method with the following signature:

Template.render(_context =None_, _request =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.base.Template.render "Link to this definition")

Renders this template with a given context.
If `context` is provided, it must be a
If `request` is provided, it must be an [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest"). Then the engine must make it, as well as the CSRF token, available in the template. How this is achieved is up to each backend.
Here’s an example of the search algorithm. For this example the [`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES) setting is:
```
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "/home/html/example.com",
            "/home/html/default",
        ],
    },
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [
            "/home/html/jinja2",
        ],
    },
]

```

If you call `get_template('story_detail.html')`, here are the files Django will look for, in order:
  * `/home/html/example.com/story_detail.html` (`'django'` engine)
  * `/home/html/default/story_detail.html` (`'django'` engine)
  * `/home/html/jinja2/story_detail.html` (`'jinja2'` engine)


If you call `select_template(['story_253_detail.html', 'story_detail.html'])`, here’s what Django will look for:
  * `/home/html/example.com/story_253_detail.html` (`'django'` engine)
  * `/home/html/default/story_253_detail.html` (`'django'` engine)
  * `/home/html/jinja2/story_253_detail.html` (`'jinja2'` engine)
  * `/home/html/example.com/story_detail.html` (`'django'` engine)
  * `/home/html/default/story_detail.html` (`'django'` engine)
  * `/home/html/jinja2/story_detail.html` (`'jinja2'` engine)


When Django finds a template that exists, it stops looking.
Use `django.template.loader.select_template()` for more flexibility
You can use [`select_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.select_template "django.template.loader.select_template") for flexible template loading. For example, if you’ve written a news story and want some stories to have custom templates, use something like `select_template(['story_%s_detail.html' % story.id, 'story_detail.html'])`. That’ll allow you to use a custom template for an individual story, with a fallback template for stories that don’t have custom templates.
It’s possible – and preferable – to organize templates in subdirectories inside each directory containing templates. The convention is to make a subdirectory for each Django app, with subdirectories within those subdirectories as needed.
Do this for your own sanity. Storing all templates in the root level of a single directory gets messy.
To load a template that’s within a subdirectory, use a slash, like so:
```
get_template("news/story_detail.html")

```

Using the same [`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES) option as above, this will attempt to load the following templates:
  * `/home/html/example.com/news/story_detail.html` (`'django'` engine)
  * `/home/html/default/news/story_detail.html` (`'django'` engine)
  * `/home/html/jinja2/news/story_detail.html` (`'jinja2'` engine)


In addition, to cut down on the repetitive nature of loading and rendering templates, Django provides a shortcut function which automates the process.

render_to_string(_template_name_ , _context =None_, _request =None_, _using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/loader/#render_to_string)[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.render_to_string "Link to this definition")

`render_to_string()` loads a template like [`get_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template") and calls its `render()` method immediately. It takes the following arguments.

`template_name`

The name of the template to load and render. If it’s a list of template names, Django uses [`select_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.select_template "django.template.loader.select_template") instead of [`get_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template") to find the template.

`context`

A

`request`

An optional [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") that will be available during the template’s rendering process.

`using`

An optional template engine [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-NAME). The search for the template will be restricted to that engine.
Usage example:
```
from django.template.loader import render_to_string

rendered = render_to_string("my_template.html", {"foo": "bar"})

```

See also the [`render()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.render "django.shortcuts.render") shortcut which calls [`render_to_string()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.render_to_string "django.template.loader.render_to_string") and feeds the result into an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") suitable for returning from a view.
Finally, you can use configured engines directly:

engines[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.engines "Link to this definition")

Template engines are available in `django.template.engines`:
```
from django.template import engines

django_engine = engines["django"]
template = django_engine.from_string("Hello {{ name }}!")

```

The lookup key — `'django'` in this example — is the engine’s [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-NAME).
### Built-in backends[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#module-django.template.backends.django "Link to this heading")

_class_ DjangoTemplates[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/backends/django/#DjangoTemplates)[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "Link to this definition")

Set [`BACKEND`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-BACKEND) to `'django.template.backends.django.DjangoTemplates'` to configure a Django template engine.
When [`APP_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-APP_DIRS) is `True`, `DjangoTemplates` engines look for templates in the `templates` subdirectory of installed applications. This generic name was kept for backwards-compatibility.
`DjangoTemplates` engines accept the following [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-OPTIONS):
  * `'autoescape'`: a boolean that controls whether HTML autoescaping is enabled.
It defaults to `True`.
Warning
Only set it to `False` if you’re rendering non-HTML templates!
  * `'context_processors'`: a list of dotted Python paths to callables that are used to populate the context when a template is rendered with a request. These callables take a request object as their argument and return a
It defaults to an empty list.
See [`RequestContext`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.RequestContext "django.template.RequestContext") for more information.
  * `'debug'`: a boolean that turns on/off template debug mode. If it is `True`, the fancy error page will display a detailed report for any exception raised during template rendering. This report contains the relevant snippet of the template with the appropriate line highlighted.
It defaults to the value of the [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) setting.
  * `'loaders'`: a list of dotted Python paths to template loader classes. Each `Loader` class knows how to import templates from a particular source. Optionally, a tuple can be used instead of a string. The first item in the tuple should be the `Loader` class name, and subsequent items are passed to the `Loader` during initialization.
The default depends on the values of [`DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-DIRS) and [`APP_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-APP_DIRS).
See [Loader types](https://docs.djangoproject.com/en/5.0/ref/templates/api/#template-loaders) for details.
  * `'string_if_invalid'`: the output, as a string, that the template system should use for invalid (e.g. misspelled) variables.
It defaults to an empty string.
See [How invalid variables are handled](https://docs.djangoproject.com/en/5.0/ref/templates/api/#invalid-template-variables) for details.
  * `'file_charset'`: the charset used to read template files on disk.
It defaults to `'utf-8'`.
  * `'libraries'`: A dictionary of labels and dotted Python paths of template tag modules to register with the template engine. This can be used to add new libraries or provide alternate labels for existing ones. For example:
```
OPTIONS = {
    "libraries": {
        "myapp_tags": "path.to.myapp.tags",
        "admin.urls": "django.contrib.admin.templatetags.admin_urls",
    },
}

```

Libraries can be loaded by passing the corresponding dictionary key to the [`{% load %}`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-load) tag.
  * `'builtins'`: A list of dotted Python paths of template tag modules to add to [built-ins](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/). For example:
```
OPTIONS = {
    "builtins": ["myapp.builtins"],
}

```

Tags and filters from built-in libraries can be used without first calling the [`{% load %}`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-load) tag.



_class_ Jinja2[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/backends/jinja2/#Jinja2)[¶](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.jinja2.Jinja2 "Link to this definition")

Requires
/ 
```
$ python -m pip install Jinja2

```

```
...\> py -m pip install Jinja2

```

Set [`BACKEND`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-BACKEND) to `'django.template.backends.jinja2.Jinja2'` to configure a
When [`APP_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-APP_DIRS) is `True`, `Jinja2` engines look for templates in the `jinja2` subdirectory of installed applications.
The most important entry in [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-OPTIONS) is `'environment'`. It’s a dotted Python path to a callable returning a Jinja2 environment. It defaults to `'jinja2.Environment'`. Django invokes that callable and passes other options as keyword arguments. Furthermore, Django adds defaults that differ from Jinja2’s for a few options:
  * `'autoescape'`: `True`
  * `'loader'`: a loader configured for [`DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-DIRS) and [`APP_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-APP_DIRS)
  * `'auto_reload'`: `settings.DEBUG`
  * `'undefined'`: `DebugUndefined if settings.DEBUG else Undefined`


`Jinja2` engines also accept the following [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-OPTIONS):
  * `'context_processors'`: a list of dotted Python paths to callables that are used to populate the context when a template is rendered with a request. These callables take a request object as their argument and return a
It defaults to an empty list.
Using context processors with Jinja2 templates is discouraged.
Context processors are useful with Django templates because Django templates don’t support calling functions with arguments. Since Jinja2 doesn’t have that limitation, it’s recommended to put the function that you would use as a context processor in the global variables available to the template using `jinja2.Environment` as described below. You can then call that function in the template:
```
{{ function(request) }}

```

Some Django templates context processors return a fixed value. For Jinja2 templates, this layer of indirection isn’t necessary since you can add constants directly in `jinja2.Environment`.
The original use case for adding context processors for Jinja2 involved:
    * Making an expensive computation that depends on the request.
    * Needing the result in every template.
    * Using the result multiple times in each template.
Unless all of these conditions are met, passing a function to the template is more in line with the design of Jinja2.


The default configuration is purposefully kept to a minimum. If a template is rendered with a request (e.g. when using [`render()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.render "django.shortcuts.render")), the `Jinja2` backend adds the globals `request`, `csrf_input`, and `csrf_token` to the context. Apart from that, this backend doesn’t create a Django-flavored environment. It doesn’t know about Django filters and tags. In order to use Django-specific APIs, you must configure them into the environment.
For example, you can create `myproject/jinja2.py` with this content:
```
from django.templatetags.static import static
from django.urls import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
        }
    )
    return env

```

and set the `'environment'` option to `'myproject.jinja2.environment'`.
Then you could use the following constructs in Jinja2 templates:
```
<img src="{{ static('path/to/company-logo.png') }}" alt="Company Logo">

<a href="{{ url('admin:index') }}">Administration</a>

```

The concepts of tags and filters exist both in the Django template language and in Jinja2 but they’re used differently. Since Jinja2 supports passing arguments to callables in templates, many features that require a template tag or filter in Django templates can be achieved by calling a function in Jinja2 templates, as shown in the example above. Jinja2’s global namespace removes the need for template context processors. The Django template language doesn’t have an equivalent of Jinja2 tests.
Previous page and next page
[`Media` class)](https://docs.djangoproject.com/en/5.0/topics/forms/media/)
[Class-based views ](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
[](https://docs.djangoproject.com/en/5.0/topics/templates/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Nsukami Patrick donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Templates](https://docs.djangoproject.com/en/5.0/topics/templates/)
    * [The Django template language](https://docs.djangoproject.com/en/5.0/topics/templates/#the-django-template-language)
      * [Syntax](https://docs.djangoproject.com/en/5.0/topics/templates/#syntax)
        * [Variables](https://docs.djangoproject.com/en/5.0/topics/templates/#variables)
        * [Tags](https://docs.djangoproject.com/en/5.0/topics/templates/#tags)
        * [Filters](https://docs.djangoproject.com/en/5.0/topics/templates/#filters)
        * [Comments](https://docs.djangoproject.com/en/5.0/topics/templates/#comments)
      * [Components](https://docs.djangoproject.com/en/5.0/topics/templates/#components)
        * [Engine](https://docs.djangoproject.com/en/5.0/topics/templates/#engine)
        * [Template](https://docs.djangoproject.com/en/5.0/topics/templates/#template)
        * [Context](https://docs.djangoproject.com/en/5.0/topics/templates/#context)
        * [Loaders](https://docs.djangoproject.com/en/5.0/topics/templates/#loaders)
        * [Context processors](https://docs.djangoproject.com/en/5.0/topics/templates/#context-processors)
    * [Support for template engines](https://docs.djangoproject.com/en/5.0/topics/templates/#support-for-template-engines)
      * [Configuration](https://docs.djangoproject.com/en/5.0/topics/templates/#configuration)
      * [Usage](https://docs.djangoproject.com/en/5.0/topics/templates/#module-django.template.loader)
      * [Built-in backends](https://docs.djangoproject.com/en/5.0/topics/templates/#module-django.template.backends.django)


### Browse
  * Prev: [Form Assets (the `Media` class)](https://docs.djangoproject.com/en/5.0/topics/forms/media/)
  * Next: [Class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Templates


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
