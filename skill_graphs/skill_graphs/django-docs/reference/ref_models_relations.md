[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/models/relations/#main-content)
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
[Documentation](https://docs.djangoproject.com/en/6.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/6.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/models/relations/)
  * [sv](https://docs.djangoproject.com/sv/6.0/ref/models/relations/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/models/relations/)
  * [pl](https://docs.djangoproject.com/pl/6.0/ref/models/relations/)
  * [ko](https://docs.djangoproject.com/ko/6.0/ref/models/relations/)
  * [ja](https://docs.djangoproject.com/ja/6.0/ref/models/relations/)
  * [it](https://docs.djangoproject.com/it/6.0/ref/models/relations/)
  * [id](https://docs.djangoproject.com/id/6.0/ref/models/relations/)
  * [fr](https://docs.djangoproject.com/fr/6.0/ref/models/relations/)
  * [es](https://docs.djangoproject.com/es/6.0/ref/models/relations/)
  * [el](https://docs.djangoproject.com/el/6.0/ref/models/relations/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/models/relations/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/models/relations/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/models/relations/)
  * [5.0](https://docs.djangoproject.com/en/5.0/ref/models/relations/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/models/relations/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/models/relations/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/models/relations/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/models/relations/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/models/relations/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/models/relations/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/models/relations/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/models/relations/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/models/relations/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/models/relations/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/models/relations/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/models/relations/)


  * [](https://docs.djangoproject.com/en/6.0/ref/models/relations/#top)


# Related objects reference[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#related-objects-reference "Link to this heading")

_class_ RelatedManager[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager "Link to this definition")

A “related manager” is a manager used in a one-to-many or many-to-many related context. This happens in two cases:
  * The “other side” of a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") relation. That is:
```
from django.db import models


class Blog(models.Model):
    # ...
    pass


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

```

In the above example, the methods below will be available on the manager `blog.entry_set`.
  * Both sides of a [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") relation
```
class Topping(models.Model):
    # ...
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)

```

In this example, the methods below will be available both on `topping.pizza_set` and on `pizza.toppings`.



add(_* objs_, _bulk =True_, _through_defaults =None_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.add "Link to this definition")


aadd(_* objs_, _bulk =True_, _through_defaults =None_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.aadd "Link to this definition")

_Asynchronous version_ : `aadd`
Adds the specified model objects to the related object set.
Example:
```
>>> b = Blog.objects.get(id=1)
>>> e = Entry.objects.get(id=234)
>>> b.entry_set.add(e)  # Associates Entry e with Blog b.

```

In the example above, in the case of a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") relationship, [`QuerySet.update()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.update "django.db.models.query.QuerySet.update") is used to perform the update. This requires the objects to already be saved.
You can use the `bulk=False` argument to instead have the related manager perform the update by calling `e.save()`.
Using `add()` with a many-to-many relationship, however, will not call any `save()` methods (the `bulk` argument doesn’t exist), but rather create the relationships using [`QuerySet.bulk_create()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create "django.db.models.query.QuerySet.bulk_create"). If you need to execute some custom logic when a relationship is created, listen to the [`m2m_changed`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.db.models.signals.m2m_changed "django.db.models.signals.m2m_changed") signal, which will trigger `pre_add` and `post_add` actions.
Using `add()` on a relation that already exists won’t duplicate the relation, but it will still trigger signals.
For many-to-many relationships `add()` accepts either model instances or field values, normally primary keys, as the `*objs` argument.
Use the `through_defaults` argument to specify values for the new [intermediate model](https://docs.djangoproject.com/en/6.0/topics/db/models/#intermediary-manytomany) instance(s), if needed. You can use callables as values in the `through_defaults` dictionary and they will be evaluated once before creating any intermediate instance(s).

create(_through_defaults =None_, _** kwargs_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.create "Link to this definition")


acreate(_through_defaults =None_, _** kwargs_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.acreate "Link to this definition")

_Asynchronous version_ : `acreate`
Creates a new object, saves it and puts it in the related object set. Returns the newly created object:
```
>>> b = Blog.objects.get(id=1)
>>> e = b.entry_set.create(
...     headline="Hello", body_text="Hi", pub_date=datetime.date(2005, 1, 1)
... )

# No need to call e.save() at this point -- it's already been saved.

```

This is equivalent to (but simpler than):
```
>>> b = Blog.objects.get(id=1)
>>> e = Entry(blog=b, headline="Hello", body_text="Hi", pub_date=datetime.date(2005, 1, 1))
>>> e.save(force_insert=True)

```

Note that there’s no need to specify the keyword argument of the model that defines the relationship. In the above example, we don’t pass the parameter `blog` to `create()`. Django figures out that the new `Entry` object’s `blog` field should be set to `b`.
Use the `through_defaults` argument to specify values for the new [intermediate model](https://docs.djangoproject.com/en/6.0/topics/db/models/#intermediary-manytomany) instance, if needed. You can use callables as values in the `through_defaults` dictionary.

remove(_* objs_, _bulk =True_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.remove "Link to this definition")


aremove(_* objs_, _bulk =True_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.aremove "Link to this definition")

_Asynchronous version_ : `aremove`
Removes the specified model objects from the related object set:
```
>>> b = Blog.objects.get(id=1)
>>> e = Entry.objects.get(id=234)
>>> b.entry_set.remove(e)  # Disassociates Entry e from Blog b.

```

Similar to [`add()`](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.add "django.db.models.fields.related.RelatedManager.add"), `e.save()` is called in the example above to perform the update. Using `remove()` with a many-to-many relationship, however, will delete the relationships using [`QuerySet.delete()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") which means no model `save()` methods are called; listen to the [`m2m_changed`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.db.models.signals.m2m_changed "django.db.models.signals.m2m_changed") signal if you wish to execute custom code when a relationship is deleted.
For many-to-many relationships `remove()` accepts either model instances or field values, normally primary keys, as the `*objs` argument.
For [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") objects, this method only exists if `null=True`. If the related field can’t be set to `None` (`NULL`), then an object can’t be removed from a relation without being added to another. In the above example, removing `e` from `b.entry_set()` is equivalent to doing `e.blog = None`, and because the `blog` [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") doesn’t have `null=True`, this is invalid.
For [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") objects, this method accepts a `bulk` argument to control how to perform the operation. If `True` (the default), `QuerySet.update()` is used. If `bulk=False`, the `save()` method of each individual model instance is called instead. This triggers the [`pre_save`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.db.models.signals.pre_save "django.db.models.signals.pre_save") and [`post_save`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.db.models.signals.post_save "django.db.models.signals.post_save") signals and comes at the expense of performance.
For many-to-many relationships, the `bulk` keyword argument doesn’t exist.

clear(_bulk =True_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.clear "Link to this definition")


aclear(_bulk =True_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.aclear "Link to this definition")

_Asynchronous version_ : `aclear`
Removes all objects from the related object set:
```
>>> b = Blog.objects.get(id=1)
>>> b.entry_set.clear()

```

Note this doesn’t delete the related objects – it just disassociates them.
Just like `remove()`, `clear()` is only available on [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey")s where `null=True` and it also accepts the `bulk` keyword argument.
For many-to-many relationships, the `bulk` keyword argument doesn’t exist.

set(_objs_ , _bulk =True_, _clear =False_, _through_defaults =None_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.set "Link to this definition")


aset(_objs_ , _bulk =True_, _clear =False_, _through_defaults =None_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.aset "Link to this definition")

_Asynchronous version_ : `aset`
Replace the set of related objects:
```
>>> new_list = [obj1, obj2, obj3]
>>> e.related_set.set(new_list)

```

This method accepts a `clear` argument to control how to perform the operation. If `False` (the default), the elements missing from the new set are removed using `remove()` and only the new ones are added. If `clear=True`, the `clear()` method is called instead and the whole set is added at once.
For [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") objects, the `bulk` argument is passed on to [`add()`](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.add "django.db.models.fields.related.RelatedManager.add") and [`remove()`](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.remove "django.db.models.fields.related.RelatedManager.remove").
For many-to-many relationships, the `bulk` keyword argument doesn’t exist.
Note that since `set()` is a compound operation, it is subject to race conditions. For instance, new objects may be added to the database in between the call to `clear()` and the call to `add()`.
For many-to-many relationships `set()` accepts a list of either model instances or field values, normally primary keys, as the `objs` argument.
Use the `through_defaults` argument to specify values for the new [intermediate model](https://docs.djangoproject.com/en/6.0/topics/db/models/#intermediary-manytomany) instance(s), if needed. You can use callables as values in the `through_defaults` dictionary and they will be evaluated once before creating any intermediate instance(s).
Note
Note that `add()`, `aadd()`, `create()`, `acreate()`, `remove()`, `aremove()`, `clear()`, `aclear()`, `set()`, and `aset()` all apply database changes immediately for all types of related fields. In other words, there is no need to call `save()`/`asave()` on either end of the relationship.
If you use [`prefetch_related()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.prefetch_related "django.db.models.query.QuerySet.prefetch_related"), the `add()`, `aadd()`, `remove()`, `aremove()`, `clear()`, `aclear()`, `set()`, and `aset()` methods clear the prefetched cache. Previous page and next page
[`_meta` API](https://docs.djangoproject.com/en/6.0/ref/models/meta/)
[Model class reference ](https://docs.djangoproject.com/en/6.0/ref/models/class/)
[](https://docs.djangoproject.com/en/6.0/ref/models/relations/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ haudoing donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Related objects reference](https://docs.djangoproject.com/en/6.0/ref/models/relations/)


### Browse
  * Prev: [Model `_meta` API](https://docs.djangoproject.com/en/6.0/ref/models/meta/)
  * Next: [Model class reference](https://docs.djangoproject.com/en/6.0/ref/models/class/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
      * [Models](https://docs.djangoproject.com/en/6.0/ref/models/)
        * Related objects reference


### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
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
Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
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
