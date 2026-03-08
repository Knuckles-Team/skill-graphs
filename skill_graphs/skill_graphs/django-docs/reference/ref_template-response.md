This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/template-response/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/template-response/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/template-response/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/template-response/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/template-response/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/template-response/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/template-response/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/template-response/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/template-response/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/template-response/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/template-response/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/template-response/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/template-response/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/template-response/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/template-response/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/template-response/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/template-response/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/template-response/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/template-response/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/template-response/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/template-response/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/template-response/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/template-response/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/template-response/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/template-response/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/template-response/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/template-response/)


  * [](https://docs.djangoproject.com/en/5.0/ref/template-response/#top)


#  `TemplateResponse` and `SimpleTemplateResponse`[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#module-django.template.response "Link to this heading")
Standard [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") objects are static structures. They are provided with a block of pre-rendered content at time of construction, and while that content can be modified, it isn’t in a form that makes it easy to perform modifications.
However, it can sometimes be beneficial to allow decorators or middleware to modify a response _after_ it has been constructed by the view. For example, you may want to change the template that is used, or put additional data into the context.
TemplateResponse provides a way to do just that. Unlike basic [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") objects, TemplateResponse objects retain the details of the template and context that was provided by the view to compute the response. The final output of the response is not computed until it is needed, later in the response process.
##  `SimpleTemplateResponse` objects[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#simpletemplateresponse-objects "Link to this heading")

_class_ SimpleTemplateResponse[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/response/#SimpleTemplateResponse)[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse "Link to this definition")

### Attributes[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#attributes "Link to this heading")

SimpleTemplateResponse.template_name[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.template_name "Link to this definition")

The name of the template to be rendered. Accepts a backend-dependent template object (such as those returned by [`get_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template")), the name of a template, or a list of template names.
Example: `['foo.html', 'path/to/bar.html']`

SimpleTemplateResponse.context_data[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.context_data "Link to this definition")

The context data to be used when rendering the template. It must be a
Example: `{'foo': 123}`

SimpleTemplateResponse.rendered_content[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.rendered_content "Link to this definition")

The current rendered value of the response content, using the current template and context data.

SimpleTemplateResponse.is_rendered[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.is_rendered "Link to this definition")

A boolean indicating whether the response content has been rendered.
### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#methods "Link to this heading")

SimpleTemplateResponse.__init__(_template_ , _context =None_, _content_type =None_, _status =None_, _charset =None_, _using =None_, _headers =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/response/#SimpleTemplateResponse.__init__)[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.__init__ "Link to this definition")

Instantiates a [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse") object with the given template, context, content type, HTTP status, and charset.

`template`

A backend-dependent template object (such as those returned by [`get_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template")), the name of a template, or a list of template names.

`context`

A

`content_type`

The value included in the HTTP `Content-Type` header, including the MIME type specification and the character set encoding. If `content_type` is specified, then its value is used. Otherwise, `'text/html'` is used.

`status`

The HTTP status code for the response.

`charset`

The charset in which the response will be encoded. If not given it will be extracted from `content_type`, and if that is unsuccessful, the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_CHARSET) setting will be used.

`using`

The [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-NAME) of a template engine to use for loading the template.

`headers`

A

SimpleTemplateResponse.resolve_context(_context_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/response/#SimpleTemplateResponse.resolve_context)[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.resolve_context "Link to this definition")

Preprocesses context data that will be used for rendering a template. Accepts a
Override this method in order to customize the context.

SimpleTemplateResponse.resolve_template(_template_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/response/#SimpleTemplateResponse.resolve_template)[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.resolve_template "Link to this definition")

Resolves the template instance to use for rendering. Accepts a backend-dependent template object (such as those returned by [`get_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template")), the name of a template, or a list of template names.
Returns the backend-dependent template object instance to be rendered.
Override this method in order to customize template loading.

SimpleTemplateResponse.add_post_render_callback()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/response/#SimpleTemplateResponse.add_post_render_callback)[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.add_post_render_callback "Link to this definition")

Add a callback that will be invoked after rendering has taken place. This hook can be used to defer certain processing operations (such as caching) until after rendering has occurred.
If the [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse") has already been rendered, the callback will be invoked immediately.
When called, callbacks will be passed a single argument – the rendered [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse") instance.
If the callback returns a value that is not `None`, this will be used as the response instead of the original response object (and will be passed to the next post rendering callback etc.)

SimpleTemplateResponse.render()[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.render "Link to this definition")

Sets `response.content` to the result obtained by [`SimpleTemplateResponse.rendered_content`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.rendered_content "django.template.response.SimpleTemplateResponse.rendered_content"), runs all post-rendering callbacks, and returns the resulting response object.
`render()` will only have an effect the first time it is called. On subsequent calls, it will return the result obtained from the first call.
##  `TemplateResponse` objects[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#templateresponse-objects "Link to this heading")

_class_ TemplateResponse[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/response/#TemplateResponse)[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "Link to this definition")

`TemplateResponse` is a subclass of [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse") that knows about the current [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest").
### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#id1 "Link to this heading")

TemplateResponse.__init__(_request_ , _template_ , _context =None_, _content_type =None_, _status =None_, _charset =None_, _using =None_, _headers =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/template/response/#TemplateResponse.__init__)[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse.__init__ "Link to this definition")

Instantiates a [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") object with the given request, template, context, content type, HTTP status, and charset.

`request`

An [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") instance.

`template`

A backend-dependent template object (such as those returned by [`get_template()`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.loader.get_template "django.template.loader.get_template")), the name of a template, or a list of template names.

`context`

A

`content_type`

The value included in the HTTP `Content-Type` header, including the MIME type specification and the character set encoding. If `content_type` is specified, then its value is used. Otherwise, `'text/html'` is used.

`status`

The HTTP status code for the response.

`charset`

The charset in which the response will be encoded. If not given it will be extracted from `content_type`, and if that is unsuccessful, the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_CHARSET) setting will be used.

`using`

The [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-NAME) of a template engine to use for loading the template.

`headers`

A
## The rendering process[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#the-rendering-process "Link to this heading")
Before a [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") instance can be returned to the client, it must be rendered. The rendering process takes the intermediate representation of template and context, and turns it into the final byte stream that can be served to the client.
There are three circumstances under which a `TemplateResponse` will be rendered:
  * When the `TemplateResponse` instance is explicitly rendered, using the [`SimpleTemplateResponse.render()`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.render "django.template.response.SimpleTemplateResponse.render") method.
  * When the content of the response is explicitly set by assigning `response.content`.
  * After passing through template response middleware, but before passing through response middleware.


A `TemplateResponse` can only be rendered once. The first call to [`SimpleTemplateResponse.render()`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.render "django.template.response.SimpleTemplateResponse.render") sets the content of the response; subsequent rendering calls do not change the response content.
However, when `response.content` is explicitly assigned, the change is always applied. If you want to force the content to be re-rendered, you can reevaluate the rendered content, and assign the content of the response manually:
```
# Set up a rendered TemplateResponse
>>> from django.template.response import TemplateResponse
>>> t = TemplateResponse(request, "original.html", {})
>>> t.render()
>>> print(t.content)
Original content

# Re-rendering doesn't change content
>>> t.template_name = "new.html"
>>> t.render()
>>> print(t.content)
Original content

# Assigning content does change, no render() call required
>>> t.content = t.rendered_content
>>> print(t.content)
New content

```

### Post-render callbacks[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#post-render-callbacks "Link to this heading")
Some operations – such as caching – cannot be performed on an unrendered template. They must be performed on a fully complete and rendered response.
If you’re using middleware, you can do that. Middleware provides multiple opportunities to process a response on exit from a view. If you put behavior in the response middleware, it’s guaranteed to execute after template rendering has taken place.
However, if you’re using a decorator, the same opportunities do not exist. Any behavior defined in a decorator is handled immediately.
To compensate for this (and any other analogous use cases), [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") allows you to register callbacks that will be invoked when rendering has completed. Using this callback, you can defer critical processing until a point where you can guarantee that rendered content will be available.
To define a post-render callback, define a function that takes a single argument – response – and register that function with the template response:
```
from django.template.response import TemplateResponse


def my_render_callback(response):
    # Do content-sensitive processing
    do_post_processing()


def my_view(request):
    # Create a response
    response = TemplateResponse(request, "mytemplate.html", {})
    # Register the callback
    response.add_post_render_callback(my_render_callback)
    # Return the response
    return response

```

`my_render_callback()` will be invoked after the `mytemplate.html` has been rendered, and will be provided the fully rendered [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") instance as an argument.
If the template has already been rendered, the callback will be invoked immediately.
## Using `TemplateResponse` and `SimpleTemplateResponse`[¶](https://docs.djangoproject.com/en/5.0/ref/template-response/#using-templateresponse-and-simpletemplateresponse "Link to this heading")
A [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") object can be used anywhere that a normal [`django.http.HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") can be used. It can also be used as an alternative to calling [`render()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.render "django.shortcuts.render").
For example, the following view returns a [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") with a template and a context containing a queryset:
```
from django.template.response import TemplateResponse


def blog_index(request):
    return TemplateResponse(
        request, "entry_list.html", {"entries": Entry.objects.all()}
    )

```

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/templates/api/)
[Unicode data ](https://docs.djangoproject.com/en/5.0/ref/unicode/)
[](https://docs.djangoproject.com/en/5.0/ref/template-response/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Tomonori Fujiwara donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [`TemplateResponse` and `SimpleTemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/)
    * [`SimpleTemplateResponse` objects](https://docs.djangoproject.com/en/5.0/ref/template-response/#simpletemplateresponse-objects)
      * [Attributes](https://docs.djangoproject.com/en/5.0/ref/template-response/#attributes)
      * [Methods](https://docs.djangoproject.com/en/5.0/ref/template-response/#methods)
    * [`TemplateResponse` objects](https://docs.djangoproject.com/en/5.0/ref/template-response/#templateresponse-objects)
      * [Methods](https://docs.djangoproject.com/en/5.0/ref/template-response/#id1)
    * [The rendering process](https://docs.djangoproject.com/en/5.0/ref/template-response/#the-rendering-process)
      * [Post-render callbacks](https://docs.djangoproject.com/en/5.0/ref/template-response/#post-render-callbacks)
    * [Using `TemplateResponse` and `SimpleTemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#using-templateresponse-and-simpletemplateresponse)


### Browse
  * Prev: [The Django template language: for Python programmers](https://docs.djangoproject.com/en/5.0/ref/templates/api/)
  * Next: [Unicode data](https://docs.djangoproject.com/en/5.0/ref/unicode/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * `TemplateResponse` and `SimpleTemplateResponse`


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
