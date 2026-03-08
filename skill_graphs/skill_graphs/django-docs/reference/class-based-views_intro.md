This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/class-based-views/intro/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/class-based-views/intro/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/class-based-views/intro/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/class-based-views/intro/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/class-based-views/intro/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/class-based-views/intro/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/class-based-views/intro/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/class-based-views/intro/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/class-based-views/intro/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/class-based-views/intro/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/class-based-views/intro/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/class-based-views/intro/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/class-based-views/intro/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/class-based-views/intro/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/class-based-views/intro/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/class-based-views/intro/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/class-based-views/intro/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/class-based-views/intro/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/class-based-views/intro/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/class-based-views/intro/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/class-based-views/intro/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/)


  * [](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#top)


# Introduction to class-based views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#introduction-to-class-based-views "Link to this heading")
Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences and advantages when compared to function-based views:
  * Organization of code related to specific HTTP methods (`GET`, `POST`, etc.) can be addressed by separate methods instead of conditional branching.
  * Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.


## The relationship and history of generic views, class-based views, and class-based generic views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#the-relationship-and-history-of-generic-views-class-based-views-and-class-based-generic-views "Link to this heading")
In the beginning there was only the view function contract, Django passed your function an [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") and expected back an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse"). This was the extent of what Django provided.
Early on it was recognized that there were common idioms and patterns found in view development. Function-based generic views were introduced to abstract these patterns and ease view development for the common cases.
The problem with function-based generic views is that while they covered the simple cases well, there was no way to extend or customize them beyond some configuration options, limiting their usefulness in many real-world applications.
Class-based generic views were created with the same objective as function-based generic views, to make view development easier. However, the way the solution is implemented, through the use of mixins, provides a toolkit that results in class-based generic views being more extensible and flexible than their function-based counterparts.
If you have tried function based generic views in the past and found them lacking, you should not think of class-based generic views as a class-based equivalent, but rather as a fresh approach to solving the original problems that generic views were meant to solve.
The toolkit of base classes and mixins that Django uses to build class-based generic views are built for maximum flexibility, and as such have many hooks in the form of default method implementations and attributes that you are unlikely to be concerned with in the simplest use cases. For example, instead of limiting you to a class-based attribute for `form_class`, the implementation uses a `get_form` method, which calls a `get_form_class` method, which in its default implementation returns the `form_class` attribute of the class. This gives you several options for specifying what form to use, from an attribute, to a fully dynamic, callable hook. These options seem to add hollow complexity for simple situations, but without them, more advanced designs would be limited.
## Using class-based views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-class-based-views "Link to this heading")
At its core, a class-based view allows you to respond to different HTTP request methods with different class instance methods, instead of with conditionally branching code inside a single view function.
So where the code to handle HTTP `GET` in a view function would look something like:
```
from django.http import HttpResponse


def my_view(request):
    if request.method == "GET":
        # <view logic>
        return HttpResponse("result")

```

In a class-based view, this would become:
```
from django.http import HttpResponse
from django.views import View


class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse("result")

```

Because Django’s URL resolver expects to send the request and associated arguments to a callable function, not a class, class-based views have an [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") class method which returns a function that can be called when a request arrives for a URL matching the associated pattern. The function creates an instance of the class, calls [`setup()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup") to initialize its attributes, and then calls its [`dispatch()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch") method. `dispatch` looks at the request to determine whether it is a `GET`, `POST`, etc, and relays the request to a matching method if one is defined, or raises [`HttpResponseNotAllowed`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotAllowed "django.http.HttpResponseNotAllowed") if not:
```
# urls.py
from django.urls import path
from myapp.views import MyView

urlpatterns = [
    path("about/", MyView.as_view()),
]

```

It is worth noting that what your method returns is identical to what you return from a function-based view, namely some form of [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse"). This means that [http shortcuts](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/) or [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") objects are valid to use inside a class-based view.
While a minimal class-based view does not require any class attributes to perform its job, class attributes are useful in many class-based designs, and there are two ways to configure or set class attributes.
The first is the standard Python way of subclassing and overriding attributes and methods in the subclass. So that if your parent class had an attribute `greeting` like this:
```
from django.http import HttpResponse
from django.views import View


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)

```

You can override that in a subclass:
```
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"

```

Another option is to configure class attributes as keyword arguments to the [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") call in the URLconf:
```
urlpatterns = [
    path("about/", GreetingView.as_view(greeting="G'day")),
]

```

Note
While your class is instantiated for each request dispatched to it, class attributes set through the [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") entry point are configured only once at the time your URLs are imported.
## Using mixins[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-mixins "Link to this heading")
Mixins are a form of multiple inheritance where behaviors and attributes of multiple parent classes can be combined.
For example, in the generic class-based views there is a mixin called [`TemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin "django.views.generic.base.TemplateResponseMixin") whose primary purpose is to define the method [`render_to_response()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response"). When combined with the behavior of the [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View "django.views.generic.base.View") base class, the result is a [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.TemplateView "django.views.generic.base.TemplateView") class that will dispatch requests to the appropriate matching methods (a behavior defined in the `View` base class), and that has a [`render_to_response()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response") method that uses a [`template_name`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") attribute to return a [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") object (a behavior defined in the `TemplateResponseMixin`).
Mixins are an excellent way of reusing code across multiple classes, but they come with some cost. The more your code is scattered among mixins, the harder it will be to read a child class and know what exactly it is doing, and the harder it will be to know which methods from which mixins to override if you are subclassing something that has a deep inheritance tree.
Note also that you can only inherit from one generic view - that is, only one parent class may inherit from [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View "django.views.generic.base.View") and the rest (if any) should be mixins. Trying to inherit from more than one class that inherits from `View` - for example, trying to use a form at the top of a list and combining [`ProcessFormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ProcessFormView "django.views.generic.edit.ProcessFormView") and [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView "django.views.generic.list.ListView") - won’t work as expected.
## Handling forms with class-based views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-forms-with-class-based-views "Link to this heading")
A basic function-based view that handles forms may look something like this:
```
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm


def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect("/success/")
    else:
        form = MyForm(initial={"key": "value"})

    return render(request, "form_template.html", {"form": form})

```

A similar class-based view might look like:
```
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import MyForm


class MyFormView(View):
    form_class = MyForm
    initial = {"key": "value"}
    template_name = "form_template.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect("/success/")

        return render(request, self.template_name, {"form": form})

```

This is a minimal case, but you can see that you would then have the option of customizing this view by overriding any of the class attributes, e.g. `form_class`, via URLconf configuration, or subclassing and overriding one or more of the methods (or both!).
## Decorating class-based views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#decorating-class-based-views "Link to this heading")
The extension of class-based views isn’t limited to using mixins. You can also use decorators. Since class-based views aren’t functions, decorating them works differently depending on if you’re using `as_view()` or creating a subclass.
### Decorating in URLconf[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#decorating-in-urlconf "Link to this heading")
You can adjust class-based views by decorating the result of the [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") method. The easiest place to do this is in the URLconf where you deploy your view:
```
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from .views import VoteView

urlpatterns = [
    path("about/", login_required(TemplateView.as_view(template_name="secret.html"))),
    path("vote/", permission_required("polls.can_vote")(VoteView.as_view())),
]

```

This approach applies the decorator on a per-instance basis. If you want every instance of a view to be decorated, you need to take a different approach.
### Decorating the class[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#decorating-the-class "Link to this heading")
To decorate every instance of a class-based view, you need to decorate the class definition itself. To do this you apply the decorator to the [`dispatch()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch") method of the class.
A method on a class isn’t quite the same as a standalone function, so you can’t just apply a function decorator to the method – you need to transform it into a method decorator first. The `method_decorator` decorator transforms a function decorator into a method decorator so that it can be used on an instance method. For example:
```
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class ProtectedView(TemplateView):
    template_name = "secret.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

```

Or, more succinctly, you can decorate the class instead and pass the name of the method to be decorated as the keyword argument `name`:
```
@method_decorator(login_required, name="dispatch")
class ProtectedView(TemplateView):
    template_name = "secret.html"

```

If you have a set of common decorators used in several places, you can define a list or tuple of decorators and use this instead of invoking `method_decorator()` multiple times. These two classes are equivalent:
```
decorators = [never_cache, login_required]


@method_decorator(decorators, name="dispatch")
class ProtectedView(TemplateView):
    template_name = "secret.html"


@method_decorator(never_cache, name="dispatch")
@method_decorator(login_required, name="dispatch")
class ProtectedView(TemplateView):
    template_name = "secret.html"

```

The decorators will process a request in the order they are passed to the decorator. In the example, `never_cache()` will process the request before `login_required()`.
In this example, every instance of `ProtectedView` will have login protection. These examples use `login_required`, however, the same behavior can be obtained by using [`LoginRequiredMixin`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.mixins.LoginRequiredMixin "django.contrib.auth.mixins.LoginRequiredMixin").
Note
`method_decorator` passes `*args` and `**kwargs` as parameters to the decorated method on the class. If your method does not accept a compatible set of parameters it will raise a `TypeError` exception.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
[Built-in class-based generic views ](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/)
[](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Nick Efford donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Introduction to class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/)
    * [The relationship and history of generic views, class-based views, and class-based generic views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#the-relationship-and-history-of-generic-views-class-based-views-and-class-based-generic-views)
    * [Using class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-class-based-views)
    * [Using mixins](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-mixins)
    * [Handling forms with class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-forms-with-class-based-views)
    * [Decorating class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#decorating-class-based-views)
      * [Decorating in URLconf](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#decorating-in-urlconf)
      * [Decorating the class](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#decorating-the-class)


### Browse
  * Prev: [Class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
  * Next: [Built-in class-based generic views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
        * Introduction to class-based views


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
