This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/class-based-views/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/class-based-views/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/class-based-views/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/class-based-views/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/class-based-views/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/class-based-views/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/class-based-views/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/class-based-views/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/class-based-views/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/class-based-views/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/class-based-views/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/class-based-views/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/class-based-views/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/class-based-views/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/class-based-views/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/class-based-views/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/class-based-views/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/class-based-views/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/class-based-views/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/class-based-views/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/class-based-views/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/class-based-views/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/class-based-views/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/class-based-views/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/class-based-views/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/class-based-views/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/class-based-views/)


  * [](https://docs.djangoproject.com/en/5.0/ref/class-based-views/#top)


# Built-in class-based views API[¶](https://docs.djangoproject.com/en/5.0/ref/class-based-views/#built-in-class-based-views-api "Link to this heading")
Class-based views API reference. For introductory material, see the [Class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/) topic guide.
  * [Base views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/)
    * [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#view)
    * [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview)
    * [`RedirectView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#redirectview)
  * [Generic display views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/)
    * [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#detailview)
    * [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview)
  * [Generic editing views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/)
    * [`FormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#formview)
    * [`CreateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#createview)
    * [`UpdateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#updateview)
    * [`DeleteView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#deleteview)
  * [Generic date views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-date-based/)
    * [`ArchiveIndexView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-date-based/#archiveindexview)
    * [`YearArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-date-based/#yeararchiveview)
    * [`MonthArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-date-based/#montharchiveview)
    * [`WeekArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-date-based/#weekarchiveview)
    * [`DayArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-date-based/#dayarchiveview)
    * [`TodayArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-date-based/#todayarchiveview)
    * [`DateDetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-date-based/#datedetailview)
  * [Class-based views mixins](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins/)
    * [Simple mixins](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/)
      * [`ContextMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#contextmixin)
      * [`TemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#templateresponsemixin)
    * [Single object mixins](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/)
      * [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#singleobjectmixin)
      * [`SingleObjectTemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#singleobjecttemplateresponsemixin)
    * [Multiple object mixins](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-multiple-object/)
      * [`MultipleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-multiple-object/#multipleobjectmixin)
      * [`MultipleObjectTemplateResponseMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-multiple-object/#multipleobjecttemplateresponsemixin)
    * [Editing mixins](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/)
      * [`FormMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#formmixin)
      * [`ModelFormMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#modelformmixin)
      * [`ProcessFormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#processformview)
      * [`DeletionMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#deletionmixin)
    * [Date-based mixins](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-date-based/)
      * [`YearMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-date-based/#yearmixin)
      * [`MonthMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-date-based/#monthmixin)
      * [`DayMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-date-based/#daymixin)
      * [`WeekMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-date-based/#weekmixin)
      * [`DateMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-date-based/#datemixin)
      * [`BaseDateListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-date-based/#basedatelistview)
  * [Class-based generic views - flattened index](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/)
    * [Simple generic views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#simple-generic-views)
      * [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#view)
      * [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#templateview)
      * [`RedirectView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#redirectview)
    * [Detail Views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#detail-views)
      * [`DetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#detailview)
    * [List Views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#list-views)
      * [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#listview)
    * [Editing views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#editing-views)
      * [`FormView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#formview)
      * [`CreateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#createview)
      * [`UpdateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#updateview)
      * [`DeleteView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#deleteview)
    * [Date-based views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#date-based-views)
      * [`ArchiveIndexView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#archiveindexview)
      * [`YearArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#yeararchiveview)
      * [`MonthArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#montharchiveview)
      * [`WeekArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#weekarchiveview)
      * [`DayArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#dayarchiveview)
      * [`TodayArchiveView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#todayarchiveview)
      * [`DateDetailView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#datedetailview)


## Specification[¶](https://docs.djangoproject.com/en/5.0/ref/class-based-views/#specification "Link to this heading")
Each request served by a class-based view has an independent state; therefore, it is safe to store state variables on the instance (i.e., `self.foo = 3` is a thread-safe operation).
A class-based view is deployed into a URL pattern using the [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") classmethod:
```
urlpatterns = [
    path("view/", MyView.as_view(size=42)),
]

```

Thread safety with view arguments
Arguments passed to a view are shared between every instance of a view. This means that you shouldn’t use a list, dictionary, or any other mutable object as an argument to a view. If you do and the shared object is modified, the actions of one user visiting your view could have an effect on subsequent users visiting the same view.
Arguments passed into [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") will be assigned onto the instance that is used to service a request. Using the previous example, this means that every request on `MyView` is able to use `self.size`. Arguments must correspond to attributes that already exist on the class (return `True` on a `hasattr` check).
## Base vs Generic views[¶](https://docs.djangoproject.com/en/5.0/ref/class-based-views/#base-vs-generic-views "Link to this heading")
Base class-based views can be thought of as _parent_ views, which can be used by themselves or inherited from. They may not provide all the capabilities required for projects, in which case there are Mixins which extend what base views can do.
Django’s generic views are built off of those base views, and were developed as a shortcut for common usage patterns such as displaying the details of an object. They take certain common idioms and patterns found in view development and abstract them so that you can quickly write common views of data without having to repeat yourself.
Most generic views require the `queryset` key, which is a `QuerySet` instance; see [Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/) for more information about `QuerySet` objects.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/checks/)
[Base views ](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/)
[](https://docs.djangoproject.com/en/5.0/ref/class-based-views/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Perlet & Shiner, P.A. donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Built-in class-based views API](https://docs.djangoproject.com/en/5.0/ref/class-based-views/)
    * [Specification](https://docs.djangoproject.com/en/5.0/ref/class-based-views/#specification)
    * [Base vs Generic views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/#base-vs-generic-views)


### Browse
  * Prev: [System check framework](https://docs.djangoproject.com/en/5.0/ref/checks/)
  * Next: [Base views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Built-in class-based views API


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
