This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/paginator/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/paginator/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/paginator/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/paginator/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/paginator/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/paginator/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/paginator/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/paginator/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/paginator/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/paginator/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/paginator/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/paginator/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/paginator/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/paginator/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/paginator/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/paginator/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/paginator/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/paginator/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/paginator/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/paginator/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/paginator/)


  * [](https://docs.djangoproject.com/en/5.0/ref/paginator/#top)


# Paginator[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#paginator "Link to this heading")
Django provides a few classes that help you manage paginated data – that is, data that’s split across several pages, with “Previous/Next” links. These classes live in
For examples, see the [Pagination topic guide](https://docs.djangoproject.com/en/5.0/topics/pagination/).
##  `Paginator` class[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#paginator-class "Link to this heading")

_class_ Paginator(_object_list_ , _per_page_ , _orphans =0_, _allow_empty_first_page =True_, _error_messages =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Paginator)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator "Link to this definition")

A paginator acts like a sequence of [`Page`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page "django.core.paginator.Page") when using `len()` or iterating it directly.

Paginator.object_list[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.object_list "Link to this definition")

Required. A list, tuple, `QuerySet`, or other sliceable object with a `count()` or `__len__()` method. For consistent pagination, `QuerySet`s should be ordered, e.g. with an [`order_by()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.order_by "django.db.models.query.QuerySet.order_by") clause or with a default [`ordering`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.ordering "django.db.models.Options.ordering") on the model.
Performance issues paginating large `QuerySet`s
If you’re using a `QuerySet` with a very large number of items, requesting high page numbers might be slow on some databases, because the resulting `LIMIT`/`OFFSET` query needs to count the number of `OFFSET` records which takes longer as the page number gets higher.

Paginator.per_page[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.per_page "Link to this definition")

Required. The maximum number of items to include on a page, not including orphans (see the [`orphans`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.orphans "django.core.paginator.Paginator.orphans") optional argument below).

Paginator.orphans[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.orphans "Link to this definition")

Optional. Use this when you don’t want to have a last page with very few items. If the last page would normally have a number of items less than or equal to `orphans`, then those items will be added to the previous page (which becomes the last page) instead of leaving the items on a page by themselves. For example, with 23 items, `per_page=10`, and `orphans=3`, there will be two pages; the first page with 10 items and the second (and last) page with 13 items. `orphans` defaults to zero, which means pages are never combined and the last page may have one item.

Paginator.allow_empty_first_page[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.allow_empty_first_page "Link to this definition")

Optional. Whether or not the first page is allowed to be empty. If `False` and `object_list` is empty, then an `EmptyPage` error will be raised.

Paginator.error_messages[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.error_messages "Link to this definition")

New in Django 5.0.
The `error_messages` argument lets you override the default messages that the paginator will raise. Pass in a dictionary with keys matching the error messages you want to override. Available error message keys are: `invalid_page`, `min_page`, and `no_results`.
For example, here is the default error message:
```
>>> from django.core.paginator import Paginator
>>> paginator = Paginator([1, 2, 3], 2)
>>> paginator.page(5)
Traceback (most recent call last):
  ...
EmptyPage: That page contains no results

```

And here is a custom error message:
```
>>> paginator = Paginator(
...     [1, 2, 3],
...     2,
...     error_messages={"no_results": "Page does not exist"},
... )
>>> paginator.page(5)
Traceback (most recent call last):
  ...
EmptyPage: Page does not exist

```

### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#methods "Link to this heading")

Paginator.get_page(_number_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Paginator.get_page)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.get_page "Link to this definition")

Returns a [`Page`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page "django.core.paginator.Page") object with the given 1-based index, while also handling out of range and invalid page numbers.
If the page isn’t a number, it returns the first page. If the page number is negative or greater than the number of pages, it returns the last page.
Raises an [`EmptyPage`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.EmptyPage "django.core.paginator.EmptyPage") exception only if you specify `Paginator(..., allow_empty_first_page=False)` and the `object_list` is empty.

Paginator.page(_number_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Paginator.page)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.page "Link to this definition")

Returns a [`Page`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page "django.core.paginator.Page") object with the given 1-based index. Raises [`PageNotAnInteger`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.PageNotAnInteger "django.core.paginator.PageNotAnInteger") if the `number` cannot be converted to an integer by calling `int()`. Raises [`EmptyPage`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.EmptyPage "django.core.paginator.EmptyPage") if the given page number doesn’t exist.

Paginator.get_elided_page_range(_number_ , _*_ , _on_each_side =3_, _on_ends =2_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Paginator.get_elided_page_range)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.get_elided_page_range "Link to this definition")

Returns a 1-based list of page numbers similar to [`Paginator.page_range`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.page_range "django.core.paginator.Paginator.page_range"), but may add an ellipsis to either or both sides of the current page number when [`Paginator.num_pages`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.num_pages "django.core.paginator.Paginator.num_pages") is large.
The number of pages to include on each side of the current page number is determined by the `on_each_side` argument which defaults to 3.
The number of pages to include at the beginning and end of page range is determined by the `on_ends` argument which defaults to 2.
For example, with the default values for `on_each_side` and `on_ends`, if the current page is 10 and there are 50 pages, the page range will be `[1, 2, '…', 7, 8, 9, 10, 11, 12, 13, '…', 49, 50]`. This will result in pages 7, 8, and 9 to the left of and 11, 12, and 13 to the right of the current page as well as pages 1 and 2 at the start and 49 and 50 at the end.
Raises [`InvalidPage`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.InvalidPage "django.core.paginator.InvalidPage") if the given page number doesn’t exist.
### Attributes[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#attributes "Link to this heading")

Paginator.ELLIPSIS[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.ELLIPSIS "Link to this definition")

A translatable string used as a substitute for elided page numbers in the page range returned by [`get_elided_page_range()`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.get_elided_page_range "django.core.paginator.Paginator.get_elided_page_range"). Default is `'…'`.

Paginator.count[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.count "Link to this definition")

The total number of objects, across all pages.
Note
When determining the number of objects contained in `object_list`, `Paginator` will first try calling `object_list.count()`. If `object_list` has no `count()` method, then `Paginator` will fall back to using `len(object_list)`. This allows objects, such as `QuerySet`, to use a more efficient `count()` method when available.

Paginator.num_pages[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.num_pages "Link to this definition")

The total number of pages.

Paginator.page_range[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.page_range "Link to this definition")

A 1-based range iterator of page numbers, e.g. yielding `[1, 2, 3, 4]`.
##  `Page` class[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#page-class "Link to this heading")
You usually won’t construct `Page` objects by hand – you’ll get them by iterating [`Paginator`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator "django.core.paginator.Paginator"), or by using [`Paginator.page()`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.page "django.core.paginator.Paginator.page").

_class_ Page(_object_list_ , _number_ , _paginator_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Page)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page "Link to this definition")

A page acts like a sequence of [`Page.object_list`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.object_list "django.core.paginator.Page.object_list") when using `len()` or iterating it directly.
### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#id1 "Link to this heading")

Page.has_next()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Page.has_next)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.has_next "Link to this definition")

Returns `True` if there’s a next page.

Page.has_previous()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Page.has_previous)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.has_previous "Link to this definition")

Returns `True` if there’s a previous page.

Page.has_other_pages()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Page.has_other_pages)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.has_other_pages "Link to this definition")

Returns `True` if there’s a next **or** previous page.

Page.next_page_number()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Page.next_page_number)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.next_page_number "Link to this definition")

Returns the next page number. Raises [`InvalidPage`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.InvalidPage "django.core.paginator.InvalidPage") if next page doesn’t exist.

Page.previous_page_number()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Page.previous_page_number)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.previous_page_number "Link to this definition")

Returns the previous page number. Raises [`InvalidPage`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.InvalidPage "django.core.paginator.InvalidPage") if previous page doesn’t exist.

Page.start_index()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Page.start_index)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.start_index "Link to this definition")

Returns the 1-based index of the first object on the page, relative to all of the objects in the paginator’s list. For example, when paginating a list of 5 objects with 2 objects per page, the second page’s [`start_index()`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.start_index "django.core.paginator.Page.start_index") would return `3`.

Page.end_index()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#Page.end_index)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.end_index "Link to this definition")

Returns the 1-based index of the last object on the page, relative to all of the objects in the paginator’s list. For example, when paginating a list of 5 objects with 2 objects per page, the second page’s [`end_index()`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.end_index "django.core.paginator.Page.end_index") would return `4`.
### Attributes[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#id2 "Link to this heading")

Page.object_list[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.object_list "Link to this definition")

The list of objects on this page.

Page.number[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.number "Link to this definition")

The 1-based page number for this page.

Page.paginator[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page.paginator "Link to this definition")

The associated [`Paginator`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator "django.core.paginator.Paginator") object.
## Exceptions[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#exceptions "Link to this heading")

_exception_ InvalidPage[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#InvalidPage)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.InvalidPage "Link to this definition")

A base class for exceptions raised when a paginator is passed an invalid page number.
The [`Paginator.page()`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.page "django.core.paginator.Paginator.page") method raises an exception if the requested page is invalid (i.e. not an integer) or contains no objects. Generally, it’s enough to catch the `InvalidPage` exception, but if you’d like more granularity, you can catch either of the following exceptions:

_exception_ PageNotAnInteger[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#PageNotAnInteger)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.PageNotAnInteger "Link to this definition")

Raised when [`page()`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.page "django.core.paginator.Paginator.page") is given a value that isn’t an integer.

_exception_ EmptyPage[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/paginator/#EmptyPage)[¶](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.EmptyPage "Link to this definition")

Raised when [`page()`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator.page "django.core.paginator.Paginator.page") is given a valid value but no objects exist on that page.
Both of the exceptions are subclasses of [`InvalidPage`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.InvalidPage "django.core.paginator.InvalidPage"), so you can handle them both with `except InvalidPage`.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/models/database-functions/)
[Request and response objects ](https://docs.djangoproject.com/en/5.0/ref/request-response/)
[](https://docs.djangoproject.com/en/5.0/ref/paginator/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ pynur donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Paginator](https://docs.djangoproject.com/en/5.0/ref/paginator/)
    * [`Paginator` class](https://docs.djangoproject.com/en/5.0/ref/paginator/#paginator-class)
      * [Methods](https://docs.djangoproject.com/en/5.0/ref/paginator/#methods)
      * [Attributes](https://docs.djangoproject.com/en/5.0/ref/paginator/#attributes)
    * [`Page` class](https://docs.djangoproject.com/en/5.0/ref/paginator/#page-class)
      * [Methods](https://docs.djangoproject.com/en/5.0/ref/paginator/#id1)
      * [Attributes](https://docs.djangoproject.com/en/5.0/ref/paginator/#id2)
    * [Exceptions](https://docs.djangoproject.com/en/5.0/ref/paginator/#exceptions)


### Browse
  * Prev: [Database Functions](https://docs.djangoproject.com/en/5.0/ref/models/database-functions/)
  * Next: [Request and response objects](https://docs.djangoproject.com/en/5.0/ref/request-response/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Paginator


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
