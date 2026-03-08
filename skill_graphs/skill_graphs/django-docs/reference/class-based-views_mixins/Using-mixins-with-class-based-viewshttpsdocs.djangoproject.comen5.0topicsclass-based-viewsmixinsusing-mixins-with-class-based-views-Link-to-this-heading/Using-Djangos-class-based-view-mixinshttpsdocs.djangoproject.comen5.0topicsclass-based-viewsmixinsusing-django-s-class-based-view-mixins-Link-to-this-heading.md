## Using Django’s class-based view mixins[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#using-django-s-class-based-view-mixins "Link to this heading")
Now we’ve seen how Django’s generic class-based views use the provided mixins, let’s look at other ways we can combine them. We’re still going to be combining them with either built-in class-based views, or other generic class-based views, but there are a range of rarer problems you can solve than are provided for by Django out of the box.
Warning
Not all mixins can be used together, and not all generic class based views can be used with all other mixins. Here we present a few examples that do work; if you want to bring together other functionality then you’ll have to consider interactions between attributes and methods that overlap between the different classes you’re using, and how
The reference documentation for Django’s [class-based views](https://docs.djangoproject.com/en/5.0/ref/class-based-views/) and [class-based view mixins](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins/) will help you in understanding which attributes and methods are likely to cause conflict between different classes and mixins.
If in doubt, it’s often better to back off and base your work on [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#View "View") or [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#TemplateView "TemplateView"), perhaps with [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin") and [`MultipleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin "django.views.generic.list.MultipleObjectMixin"). Although you will probably end up writing more code, it is more likely to be clearly understandable to someone else coming to it later, and with fewer interactions to worry about you will save yourself some thinking. (Of course, you can always dip into Django’s implementation of the generic class-based views for inspiration on how to tackle problems.)
### Using `SingleObjectMixin` with View[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#using-singleobjectmixin-with-view "Link to this heading")
If we want to write a class-based view that responds only to `POST`, we’ll subclass [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View "django.views.generic.base.View") and write a `post()` method in the subclass. However if we want our processing to work on a particular object, identified from the URL, we’ll want the functionality provided by [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin").
We’ll demonstrate this with the `Author` model we used in the [generic class-based views introduction](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/).
`views.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#id1 "Link to this code")
```
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from books.models import Author


class RecordInterestView(SingleObjectMixin, View):
    """Records the current user's interest in an author."""

    model = Author

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        # Look up the author we're interested in.
        self.object = self.get_object()
        # Actually record interest somehow here!

        return HttpResponseRedirect(
            reverse("author-detail", kwargs={"pk": self.object.pk})
        )

```

In practice you’d probably want to record the interest in a key-value store rather than in a relational database, so we’ve left that bit out. The only bit of the view that needs to worry about using [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin") is where we want to look up the author we’re interested in, which it does with a call to `self.get_object()`. Everything else is taken care of for us by the mixin.
We can hook this into our URLs easily enough:
`urls.py`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#id2 "Link to this code")
```
from django.urls import path
from books.views import RecordInterestView

urlpatterns = [
    # ...
    path(
        "author/<int:pk>/interest/",
        RecordInterestView.as_view(),
        name="author-interest",
    ),
]

```

Note the `pk` named group, which [`get_object()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object "django.views.generic.detail.SingleObjectMixin.get_object") uses to look up the `Author` instance. You could also use a slug, or any of the other features of [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin").
### Using `SingleObjectMixin` with `ListView`[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/#using-singleobjectmixin-with-listview "Link to this heading")
[`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView "django.views.generic.list.ListView") provides built-in pagination, but you might want to paginate a list of objects that are all linked (by a foreign key) to another object. In our publishing example, you might want to paginate through all the books by a particular publisher.
One way to do this is to combine [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#ListView "ListView") with [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin"), so that the queryset for the paginated list of books can hang off the publisher found as the single object. In order to do this, we need to have two different querysets:

`Book` queryset for use by [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView "django.views.generic.list.ListView")

Since we have access to the `Publisher` whose books we want to list, we override `get_queryset()` and use the `Publisher`’s [reverse foreign key manager](https://docs.djangoproject.com/en/5.0/topics/db/queries/#backwards-related-objects).

`Publisher` queryset for use in [`get_object()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object "django.views.generic.detail.SingleObjectMixin.get_object")

We’ll rely on the default implementation of `get_object()` to fetch the correct `Publisher` object. However, we need to explicitly pass a `queryset` argument because otherwise the default implementation of `get_object()` would call `get_queryset()` which we have overridden to return `Book` objects instead of `Publisher` ones.
Note
We have to think carefully about `get_context_data()`. Since both [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin") and [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#ListView "ListView") will put things in the context data under the value of `context_object_name` if it’s set, we’ll instead explicitly ensure the `Publisher` is in the context data. [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#ListView "ListView") will add in the suitable `page_obj` and `paginator` for us providing we remember to call `super()`.
Now we can write a new `PublisherDetailView`:
```
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from books.models import Publisher


class PublisherDetailView(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = "books/publisher_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Publisher.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publisher"] = self.object
        return context

    def get_queryset(self):
        return self.object.book_set.all()

```

Notice how we set `self.object` within `get()` so we can use it again later in `get_context_data()` and `get_queryset()`. If you don’t set `template_name`, the template will default to the normal [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#ListView "ListView") choice, which in this case would be `"books/book_list.html"` because it’s a list of books; [`ListView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/#ListView "ListView") knows nothing about [`SingleObjectMixin`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin "django.views.generic.detail.SingleObjectMixin"), so it doesn’t have any clue this view is anything to do with a `Publisher`.
The `paginate_by` is deliberately small in the example so you don’t have to create lots of books to see the pagination working! Here’s the template you’d want to use:
```
{% extends "base.html" %}

{% block content %}
    <h2>Publisher {{ publisher.name }}</h2>

    <ol>
      {% for book in page_obj %}
        <li>{{ book.title }}</li>
      {% endfor %}
    </ol>

    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
                <a href="?page={{ page_obj.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ page_obj.number }} of {{ paginator.num_pages }}.
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">next</a>
            {% endif %}
        </span>
    </div>
{% endblock %}

```
