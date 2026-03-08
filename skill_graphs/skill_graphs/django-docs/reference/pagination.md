This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/pagination/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/pagination/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/pagination/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/pagination/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/pagination/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/pagination/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/pagination/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/pagination/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/pagination/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/pagination/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/pagination/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/pagination/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/pagination/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/pagination/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/pagination/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/pagination/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/pagination/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/pagination/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/pagination/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/pagination/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/pagination/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/pagination/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/pagination/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/pagination/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/pagination/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/pagination/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/pagination/)


  * [](https://docs.djangoproject.com/en/5.0/topics/pagination/#top)


# Pagination[¶](https://docs.djangoproject.com/en/5.0/topics/pagination/#pagination "Link to this heading")
Django provides high-level and low-level ways to help you manage paginated data – that is, data that’s split across several pages, with “Previous/Next” links.
## The `Paginator` class[¶](https://docs.djangoproject.com/en/5.0/topics/pagination/#the-paginator-class "Link to this heading")
Under the hood, all methods of pagination use the [`Paginator`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator "django.core.paginator.Paginator") class. It does all the heavy lifting of actually splitting a `QuerySet` into [`Page`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Page "django.core.paginator.Page") objects.
## Example[¶](https://docs.djangoproject.com/en/5.0/topics/pagination/#example "Link to this heading")
Give [`Paginator`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator "django.core.paginator.Paginator") a list of objects, plus the number of items you’d like to have on each page, and it gives you methods for accessing the items for each page:
```
>>> from django.core.paginator import Paginator
>>> objects = ["john", "paul", "george", "ringo"]
>>> p = Paginator(objects, 2)

>>> p.count
4
>>> p.num_pages
2
>>> type(p.page_range)
<class 'range_iterator'>
>>> p.page_range
range(1, 3)

>>> page1 = p.page(1)
>>> page1
<Page 1 of 2>
>>> page1.object_list
['john', 'paul']

>>> page2 = p.page(2)
>>> page2.object_list
['george', 'ringo']
>>> page2.has_next()
False
>>> page2.has_previous()
True
>>> page2.has_other_pages()
True
>>> page2.next_page_number()
Traceback (most recent call last):
...
EmptyPage: That page contains no results
>>> page2.previous_page_number()
1
>>> page2.start_index()  # The 1-based index of the first item on this page
3
>>> page2.end_index()  # The 1-based index of the last item on this page
4

>>> p.page(0)
Traceback (most recent call last):
...
EmptyPage: That page number is less than 1
>>> p.page(3)
Traceback (most recent call last):
...
EmptyPage: That page contains no results

```

Note
Note that you can give `Paginator` a list/tuple, a Django `QuerySet`, or any other object with a `count()` or `__len__()` method. When determining the number of objects contained in the passed object, `Paginator` will first try calling `count()`, then fallback to using `len()` if the passed object has no `count()` method. This allows objects such as Django’s `QuerySet` to use a more efficient `count()` method when available.
## Paginating a `ListView`[¶](https://docs.djangoproject.com/en/5.0/topics/pagination/#paginating-a-listview "Link to this heading")
[`django.views.generic.list.ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView "django.views.generic.list.ListView") provides a builtin way to paginate the displayed list. You can do this by adding a [`paginate_by`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_by "django.views.generic.list.MultipleObjectMixin.paginate_by") attribute to your view class, for example:
```
from django.views.generic import ListView

from myapp.models import Contact


class ContactListView(ListView):
    paginate_by = 2
    model = Contact

```

This limits the number of objects per page and adds a `paginator` and `page_obj` to the `context`. To allow your users to navigate between pages, add links to the next and previous page, in your template like this:
```
{% for contact in page_obj %}
    {# Each "contact" is a Contact model object. #}
    {{ contact.full_name|upper }}<br>
    ...
{% endfor %}

<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>

```

## Using `Paginator` in a view function[¶](https://docs.djangoproject.com/en/5.0/topics/pagination/#using-paginator-in-a-view-function "Link to this heading")
Here’s an example using [`Paginator`](https://docs.djangoproject.com/en/5.0/ref/paginator/#django.core.paginator.Paginator "django.core.paginator.Paginator") in a view function to paginate a queryset:
```
from django.core.paginator import Paginator
from django.shortcuts import render

from myapp.models import Contact


def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})

```

In the template `list.html`, you can include navigation between pages in the same way as in the template for the `ListView` above.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/logging/)
[Security in Django ](https://docs.djangoproject.com/en/5.0/topics/security/)
[](https://docs.djangoproject.com/en/5.0/topics/pagination/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Oscar Gillberg donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Pagination](https://docs.djangoproject.com/en/5.0/topics/pagination/)
    * [The `Paginator` class](https://docs.djangoproject.com/en/5.0/topics/pagination/#the-paginator-class)
    * [Example](https://docs.djangoproject.com/en/5.0/topics/pagination/#example)
    * [Paginating a `ListView`](https://docs.djangoproject.com/en/5.0/topics/pagination/#paginating-a-listview)
    * [Using `Paginator` in a view function](https://docs.djangoproject.com/en/5.0/topics/pagination/#using-paginator-in-a-view-function)


### Browse
  * Prev: [Logging](https://docs.djangoproject.com/en/5.0/topics/logging/)
  * Next: [Security in Django](https://docs.djangoproject.com/en/5.0/topics/security/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Pagination


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
