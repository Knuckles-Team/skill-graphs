## Inline formsets[¶](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#inline-formsets "Link to this heading")

_class_ models.BaseInlineFormSet[¶](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.models.BaseInlineFormSet "Link to this definition")

Inline formsets is a small abstraction layer on top of model formsets. These simplify the case of working with related objects via a foreign key. Suppose you have these two models:
```
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

```

If you want to create a formset that allows you to edit books belonging to a particular author, you could do this:
```
>>> from django.forms import inlineformset_factory
>>> BookFormSet = inlineformset_factory(Author, Book, fields=["title"])
>>> author = Author.objects.get(name="Mike Royko")
>>> formset = BookFormSet(instance=author)

```

`BookFormSet`’s [prefix](https://docs.djangoproject.com/en/6.0/topics/forms/formsets/#formset-prefix) is `'book_set'` (`<model name>_set` ). If `Book`’s `ForeignKey` to `Author` has a [`related_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name"), that’s used instead.
Note
[`inlineformset_factory()`](https://docs.djangoproject.com/en/6.0/ref/forms/models/#django.forms.models.inlineformset_factory "django.forms.models.inlineformset_factory") uses [`modelformset_factory()`](https://docs.djangoproject.com/en/6.0/ref/forms/models/#django.forms.models.modelformset_factory "django.forms.models.modelformset_factory") and marks `can_delete=True`.
See also
[Manually rendered can_delete and can_order](https://docs.djangoproject.com/en/6.0/topics/forms/formsets/#manually-rendered-can-delete-and-can-order).
### Overriding methods on an `InlineFormSet`[¶](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#overriding-methods-on-an-inlineformset "Link to this heading")
When overriding methods on `InlineFormSet`, you should subclass [`BaseInlineFormSet`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.models.BaseInlineFormSet "django.forms.models.BaseInlineFormSet") rather than [`BaseModelFormSet`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.models.BaseModelFormSet "django.forms.models.BaseModelFormSet").
For example, if you want to override `clean()`:
```
from django.forms import BaseInlineFormSet


class CustomInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        # example custom validation across forms in the formset
        for form in self.forms:
            # your custom formset validation
            ...

```

See also [Overriding clean() on a ModelFormSet](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#model-formsets-overriding-clean).
Then when you create your inline formset, pass in the optional argument `formset`:
```
>>> from django.forms import inlineformset_factory
>>> BookFormSet = inlineformset_factory(
...     Author, Book, fields=["title"], formset=CustomInlineFormSet
... )
>>> author = Author.objects.get(name="Mike Royko")
>>> formset = BookFormSet(instance=author)

```

### More than one foreign key to the same model[¶](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#more-than-one-foreign-key-to-the-same-model "Link to this heading")
If your model contains more than one foreign key to the same model, you’ll need to resolve the ambiguity manually using `fk_name`. For example, consider the following model:
```
class Friendship(models.Model):
    from_friend = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE,
        related_name="from_friends",
    )
    to_friend = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE,
        related_name="friends",
    )
    length_in_months = models.IntegerField()

```

To resolve this, you can use `fk_name` to [`inlineformset_factory()`](https://docs.djangoproject.com/en/6.0/ref/forms/models/#django.forms.models.inlineformset_factory "django.forms.models.inlineformset_factory"):
```
>>> FriendshipFormSet = inlineformset_factory(
...     Friend, Friendship, fk_name="from_friend", fields=["to_friend", "length_in_months"]
... )

```

### Using an inline formset in a view[¶](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#using-an-inline-formset-in-a-view "Link to this heading")
You may want to provide a view that allows a user to edit the related objects of a model. Here’s how you can do that:
```
def manage_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book, fields=["title"])
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(author.get_absolute_url())
    else:
        formset = BookInlineFormSet(instance=author)
    return render(request, "manage_books.html", {"formset": formset})

```

Notice how we pass `instance` in both the `POST` and `GET` cases.
### Specifying widgets to use in the inline form[¶](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#specifying-widgets-to-use-in-the-inline-form "Link to this heading")
`inlineformset_factory` uses `modelformset_factory` and passes most of its arguments to `modelformset_factory`. This means you can use the `widgets` parameter in much the same way as passing it to `modelformset_factory`. See [Specifying widgets to use in the form with widgets](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#specifying-widgets-to-use-in-the-form-with-widgets) above.
Previous page and next page
[](https://docs.djangoproject.com/en/6.0/topics/forms/formsets/)
[Form Assets (the `Media` class) ](https://docs.djangoproject.com/en/6.0/topics/forms/media/)
[](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#top)
