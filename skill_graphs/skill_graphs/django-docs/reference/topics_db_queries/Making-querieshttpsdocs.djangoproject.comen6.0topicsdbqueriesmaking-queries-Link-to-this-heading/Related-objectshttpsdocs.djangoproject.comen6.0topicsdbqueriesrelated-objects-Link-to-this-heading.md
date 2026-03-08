## Related objects[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#related-objects "Link to this heading")
When you define a relationship in a model (i.e., a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), [`OneToOneField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField"), or [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField")), instances of that model will have a convenient API to access the related object(s).
Using the models at the top of this page, for example, an `Entry` object `e` can get its associated `Blog` object by accessing the `blog` attribute: `e.blog`.
(Behind the scenes, this functionality is implemented by Python
Django also creates API accessors for the “other” side of the relationship – the link from the related model to the model that defines the relationship. For example, a `Blog` object `b` has access to a list of all related `Entry` objects via the `entry_set` attribute: `b.entry_set.all()`.
All examples in this section use the sample `Blog`, `Author` and `Entry` models defined at the top of this page.
### One-to-many relationships[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#one-to-many-relationships "Link to this heading")
#### Forward[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#forward "Link to this heading")
If a model has a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), instances of that model will have access to the related (foreign) object via an attribute of the model.
Example:
```
>>> e = Entry.objects.get(id=2)
>>> e.blog  # Returns the related Blog object.

```

You can get and set via a foreign-key attribute. As you may expect, changes to the foreign key aren’t saved to the database until you call [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"). Example:
```
>>> e = Entry.objects.get(id=2)
>>> e.blog = some_blog
>>> e.save()

```

If a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") field has `null=True` set (i.e., it allows `NULL` values), you can assign `None` to remove the relation. Example:
```
>>> e = Entry.objects.get(id=2)
>>> e.blog = None
>>> e.save()  # "UPDATE blog_entry SET blog_id = NULL ...;"

```

Forward access to one-to-many relationships is cached the first time the related object is accessed. Subsequent accesses to the foreign key on the same object instance are cached. Example:
```
>>> e = Entry.objects.get(id=2)
>>> print(e.blog)  # Hits the database to retrieve the associated Blog.
>>> print(e.blog)  # Doesn't hit the database; uses cached version.

```

Note that the [`select_related()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.select_related "django.db.models.query.QuerySet.select_related") [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") method recursively prepopulates the cache of all one-to-many relationships ahead of time. Example:
```
>>> e = Entry.objects.select_related().get(id=2)
>>> print(e.blog)  # Doesn't hit the database; uses cached version.
>>> print(e.blog)  # Doesn't hit the database; uses cached version.

```

#### Following relationships “backward”[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#following-relationships-backward "Link to this heading")
If a model has a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), instances of the foreign-key model will have access to a [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") that returns all instances of the first model. By default, this [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") is named `FOO_set`, where `FOO` is the source model name, lowercased. This [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") returns `QuerySet` instances, which can be filtered and manipulated as described in the “Retrieving objects” section above.
Example:
```
>>> b = Blog.objects.get(id=1)
>>> b.entry_set.all()  # Returns all Entry objects related to Blog.

# b.entry_set is a Manager that returns QuerySets.
>>> b.entry_set.filter(headline__contains="Lennon")
>>> b.entry_set.count()

```

You can override the `FOO_set` name by setting the [`related_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") parameter in the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") definition. For example, if the `Entry` model was altered to `blog = ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries')`, the above example code would look like this:
```
>>> b = Blog.objects.get(id=1)
>>> b.entries.all()  # Returns all Entry objects related to Blog.

# b.entries is a Manager that returns ``QuerySet`` instances.
>>> b.entries.filter(headline__contains="Lennon")
>>> b.entries.count()

```

#### Using a custom reverse manager[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#using-a-custom-reverse-manager "Link to this heading")
By default the [`RelatedManager`](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager "django.db.models.fields.related.RelatedManager") used for reverse relations is a subclass of the [default manager](https://docs.djangoproject.com/en/6.0/topics/db/managers/#manager-names) for that model. If you would like to specify a different manager for a given query you can use the following syntax:
```
from django.db import models


class Entry(models.Model):
    # ...
    objects = models.Manager()  # Default Manager
    entries = EntryManager()  # Custom Manager


b = Blog.objects.get(id=1)
b.entry_set(manager="entries").all()

```

If `EntryManager` performed default filtering in its `get_queryset()` method, that filtering would apply to the `all()` call.
Specifying a custom reverse manager also enables you to call its custom methods:
```
b.entry_set(manager="entries").is_published()

```

Interaction with prefetching
When calling [`prefetch_related()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.prefetch_related "django.db.models.query.QuerySet.prefetch_related") with a reverse relation, the default manager will be used. If you want to prefetch related objects using a custom reverse manager, use [`Prefetch()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.Prefetch "django.db.models.Prefetch"). For example:
```
from django.db.models import Prefetch

prefetch_manager = Prefetch("entry_set", queryset=Entry.entries.all())
Blog.objects.prefetch_related(prefetch_manager)

```

#### Additional methods to handle related objects[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#additional-methods-to-handle-related-objects "Link to this heading")
In addition to the [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") methods defined in “Retrieving objects” above, the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") has additional methods used to handle the set of related objects. A synopsis of each is below, and complete details can be found in the [related objects reference](https://docs.djangoproject.com/en/6.0/ref/models/relations/).

`add(obj1, obj2, ...)`

Adds the specified model objects to the related object set.

`create(**kwargs)`

Creates a new object, saves it and puts it in the related object set. Returns the newly created object.

`remove(obj1, obj2, ...)`

Removes the specified model objects from the related object set.

`clear()`

Removes all objects from the related object set.

`set(objs)`

Replace the set of related objects.
To assign the members of a related set, use the `set()` method with an iterable of object instances. For example, if `e1` and `e2` are `Entry` instances:
```
b = Blog.objects.get(id=1)
b.entry_set.set([e1, e2])

```

If the `clear()` method is available, any preexisting objects will be removed from the `entry_set` before all objects in the iterable (in this case, a list) are added to the set. If the `clear()` method is _not_ available, all objects in the iterable will be added without removing any existing elements.
Each “reverse” operation described in this section has an immediate effect on the database. Every addition, creation and deletion is immediately and automatically saved to the database.
### Many-to-many relationships[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#many-to-many-relationships "Link to this heading")
Both ends of a many-to-many relationship get automatic API access to the other end. The API works similar to a “backward” one-to-many relationship, above.
One difference is in the attribute naming: The model that defines the [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") uses the attribute name of that field itself, whereas the “reverse” model uses the lowercased model name of the original model, plus `'_set'` (just like reverse one-to-many relationships).
An example makes this easier to understand:
```
e = Entry.objects.get(id=3)
e.authors.all()  # Returns all Author objects for this Entry.
e.authors.count()
e.authors.filter(name__contains="John")

a = Author.objects.get(id=5)
a.entry_set.all()  # Returns all Entry objects for this Author.

```

Like [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") can specify [`related_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.related_name "django.db.models.ManyToManyField.related_name"). In the above example, if the [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") in `Entry` had specified `related_name='entries'`, then each `Author` instance would have an `entries` attribute instead of `entry_set`.
Another difference from one-to-many relationships is that in addition to model instances, the `add()`, `set()`, and `remove()` methods on many-to-many relationships accept primary key values. For example, if `e1` and `e2` are `Entry` instances, then these `set()` calls work identically:
```
a = Author.objects.get(id=5)
a.entry_set.set([e1, e2])
a.entry_set.set([e1.pk, e2.pk])

```

#### Filtering on many-to-many relationships[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#filtering-on-many-to-many-relationships "Link to this heading")
When calling `filter()` on a many-to-many relationship, be aware that the join between `Entry` and the intermediary model to `Author` is performed only once, resulting in a restrictive, or “sticky”, filter. Consider the following example:
```
>>> from datetime import date
>>> batucada = Blog.objects.create(name="Batucada Blog")
>>> e = Entry.objects.create(
...     blog=batucada,
...     headline="Supporting social movements with drums",
...     pub_date=date(2019, 6, 14),
... )

>>> gloria = Author.objects.create(name="Gloria")
>>> anna = Author.objects.create(name="Anna")
>>> e.authors.add(gloria, anna)

>>> anna.entry_set.filter(authors__name="Gloria")
<QuerySet []>

```

This filtered query is looking for blog entries that are co-authored by `anna` and `gloria`. You would expect it to return the entry `e`. However, the filter condition, which traverses the many-to-many relationship between `Entry` and `Author`, yields an empty `QuerySet`.
Since the join between `Entry` and the intermediary model to `Author` happens only once, no single object of the joined models - i.e., a relation between one author and one entry - can fulfill the query condition (entries that are co-authored by `anna` and `gloria`). You can circumvent this behavior by chaining two consecutive `filter()` calls, resulting in two separate joins and thus a more permissive filter:
```
>>> anna.entry_set.filter().filter(authors__name="Gloria")
<QuerySet [<Entry: Supporting social movements with drums>]>

```

exclude() is also sticky
Please note that for this example, [`exclude()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") behaves similarly to [`filter()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") despite being implemented differently. When traversing the many-to-many relationship, it does not exclude the entry `e` despite being co-authored by Gloria:
```
>>> anna.entry_set.exclude(authors__name="Gloria")
<QuerySet [<Entry: Supporting social movements with drums>]>

```

When chaining a second `exclude()` call, an empty `QuerySet` is returned, as expected:
```
>>> anna.entry_set.exclude().exclude(authors__name="Gloria")
<QuerySet []>

```

However, in other cases, [`exclude()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") behaves differently from [`filter()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"). See the [note](https://docs.djangoproject.com/en/6.0/topics/db/queries/#exclude-implementation) in the “Spanning multi-valued relationships” section above.
### One-to-one relationships[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#one-to-one-relationships "Link to this heading")
One-to-one relationships are very similar to many-to-one relationships. If you define a [`OneToOneField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField") on your model, instances of that model will have access to the related object via an attribute of the model.
For example:
```
class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    details = models.TextField()


ed = EntryDetail.objects.get(id=2)
ed.entry  # Returns the related Entry object.

```

The difference comes in “reverse” queries. The related model in a one-to-one relationship also has access to a [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") object, but that [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") represents a single object, rather than a collection of objects:
```
e = Entry.objects.get(id=2)
e.entrydetail  # returns the related EntryDetail object

```

If no object has been assigned to this relationship, Django will raise a `DoesNotExist` exception.
Instances can be assigned to the reverse relationship in the same way as you would assign the forward relationship:
```
e.entrydetail = ed

```

### How are the backward relationships possible?[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#how-are-the-backward-relationships-possible "Link to this heading")
Other object-relational mappers require you to define relationships on both sides. The Django developers believe this is a violation of the DRY (Don’t Repeat Yourself) principle, so Django only requires you to define the relationship on one end.
But how is this possible, given that a model class doesn’t know which other model classes are related to it until those other model classes are loaded?
The answer lies in the [`app registry`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.apps.apps "django.apps.apps"). When Django starts, it imports each application listed in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS), and then the `models` module inside each application. Whenever a new model class is created, Django adds backward-relationships to any related models. If the related models haven’t been imported yet, Django keeps tracks of the relationships and adds them when the related models eventually are imported.
For this reason, it’s particularly important that all the models you’re using be defined in applications listed in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS). Otherwise, backwards relations may not work properly.
### Queries over related objects[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#queries-over-related-objects "Link to this heading")
Queries involving related objects follow the same rules as queries involving normal value fields. When specifying the value for a query to match, you may use either an object instance itself, or the primary key value for the object.
For example, if you have a Blog object `b` with `id=5`, the following three queries would be identical:
```
Entry.objects.filter(blog=b)  # Query using object instance
Entry.objects.filter(blog=b.id)  # Query using id from instance
Entry.objects.filter(blog=5)  # Query using id directly

```
