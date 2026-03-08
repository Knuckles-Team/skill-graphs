This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/custom-template-backend/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/custom-template-backend/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/custom-template-backend/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/custom-template-backend/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/custom-template-backend/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/custom-template-backend/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/custom-template-backend/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/custom-template-backend/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/custom-template-backend/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/custom-template-backend/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/custom-template-backend/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/custom-template-backend/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/custom-template-backend/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/custom-template-backend/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/custom-template-backend/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/custom-template-backend/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/custom-template-backend/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/custom-template-backend/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/custom-template-backend/)


  * [](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#top)


# How to implement a custom template backend[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#how-to-implement-a-custom-template-backend "Link to this heading")
## Custom backends[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#custom-backends "Link to this heading")
Here’s how to implement a custom template backend in order to use another template system. A template backend is a class that inherits `django.template.backends.base.BaseEngine`. It must implement `get_template()` and optionally `from_string()`. Here’s an example for a fictional `foobar` template library:
```
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy

import foobar


class FooBar(BaseEngine):
    # Name of the subdirectory containing the templates for this engine
    # inside an installed application.
    app_dirname = "foobar"

    def __init__(self, params):
        params = params.copy()
        options = params.pop("OPTIONS").copy()
        super().__init__(params)

        self.engine = foobar.Engine(**options)

    def from_string(self, template_code):
        try:
            return Template(self.engine.from_string(template_code))
        except foobar.TemplateCompilationFailed as exc:
            raise TemplateSyntaxError(exc.args)

    def get_template(self, template_name):
        try:
            return Template(self.engine.get_template(template_name))
        except foobar.TemplateNotFound as exc:
            raise TemplateDoesNotExist(exc.args, backend=self)
        except foobar.TemplateCompilationFailed as exc:
            raise TemplateSyntaxError(exc.args)


class Template:
    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context["request"] = request
            context["csrf_input"] = csrf_input_lazy(request)
            context["csrf_token"] = csrf_token_lazy(request)
        return self.template.render(context)

```

See
## Debug integration for custom engines[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#debug-integration-for-custom-engines "Link to this heading")
The Django debug page has hooks to provide detailed information when a template error arises. Custom template engines can use these hooks to enhance the traceback information that appears to users. The following hooks are available:
### Template postmortem[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#template-postmortem "Link to this heading")
The postmortem appears when [`TemplateDoesNotExist`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.TemplateDoesNotExist "django.template.TemplateDoesNotExist") is raised. It lists the template engines and loaders that were used when trying to find a given template. For example, if two Django engines are configured, the postmortem will appear like:
![../../_images/postmortem.png](https://docs.djangoproject.com/en/5.0/_images/postmortem.png)
Custom engines can populate the postmortem by passing the `backend` and `tried` arguments when raising [`TemplateDoesNotExist`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.TemplateDoesNotExist "django.template.TemplateDoesNotExist"). Backends that use the postmortem [should specify an origin](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#template-origin-api) on the template object.
### Contextual line information[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#contextual-line-information "Link to this heading")
If an error happens during template parsing or rendering, Django can display the line the error happened on. For example:
![../../_images/template-lines.png](https://docs.djangoproject.com/en/5.0/_images/template-lines.png)
Custom engines can populate this information by setting a `template_debug` attribute on exceptions raised during parsing and rendering. This attribute is a
  * `'name'`: The name of the template in which the exception occurred.
  * `'message'`: The exception message.
  * `'source_lines'`: The lines before, after, and including the line the exception occurred on. This is for context, so it shouldn’t contain more than 20 lines or so.
  * `'line'`: The line number on which the exception occurred.
  * `'before'`: The content on the error line before the token that raised the error.
  * `'during'`: The token that raised the error.
  * `'after'`: The content on the error line after the token that raised the error.
  * `'total'`: The number of lines in `source_lines`.
  * `'top'`: The line number where `source_lines` starts.
  * `'bottom'`: The line number where `source_lines` ends.


Given the above template error, `template_debug` would look like:
```
{
    "name": "/path/to/template.html",
    "message": "Invalid block tag: 'syntax'",
    "source_lines": [
        (1, "some\n"),
        (2, "lines\n"),
        (3, "before\n"),
        (4, "Hello {% syntax error %} {{ world }}\n"),
        (5, "some\n"),
        (6, "lines\n"),
        (7, "after\n"),
        (8, ""),
    ],
    "line": 4,
    "before": "Hello ",
    "during": "{% syntax error %}",
    "after": " {{ world }}\n",
    "total": 9,
    "bottom": 9,
    "top": 1,
}

```

### Origin API and 3rd-party integration[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#origin-api-and-3rd-party-integration "Link to this heading")
Django templates have an [`Origin`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.base.Origin "django.template.base.Origin") object available through the `template.origin` attribute. This enables debug information to be displayed in the [template postmortem](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#template-postmortem), as well as in 3rd-party libraries, like the
Custom engines can provide their own `template.origin` information by creating an object that specifies the following attributes:
  * `'name'`: The full path to the template.
  * `'template_name'`: The relative path to the template as passed into the template loading methods.
  * `'loader_name'`: An optional string identifying the function or class used to load the template, e.g. `django.template.loaders.filesystem.Loader`.

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/)
[How to create custom template tags and filters ](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/)
[](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Abdulaziz AlMalki donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to implement a custom template backend](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/)
    * [Custom backends](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#custom-backends)
    * [Debug integration for custom engines](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#debug-integration-for-custom-engines)
      * [Template postmortem](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#template-postmortem)
      * [Contextual line information](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#contextual-line-information)
      * [Origin API and 3rd-party integration](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/#origin-api-and-3rd-party-integration)


### Browse
  * Prev: [How to write custom lookups](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/)
  * Next: [How to create custom template tags and filters](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to implement a custom template backend


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
