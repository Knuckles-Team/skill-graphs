## Deleting objects[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#deleting-objects "Link to this heading")
The delete method, conveniently, is named [`delete()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete"). This method immediately deletes the object and returns the number of objects deleted and a dictionary with the number of deletions per object type. Example:
```
>>> e.delete()
(1, {'blog.Entry': 1})

```

You can also delete objects in bulk. Every [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") has a [`delete()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") method, which deletes all members of that [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet").
For example, this deletes all `Entry` objects with a `pub_date` year of 2005:
```
>>> Entry.objects.filter(pub_date__year=2005).delete()
(5, {'webapp.Entry': 5})

```

Keep in mind that this will, whenever possible, be executed purely in SQL, and so the `delete()` methods of individual object instances will not necessarily be called during the process. If you’ve provided a custom `delete()` method on a model class and want to ensure that it is called, you will need to “manually” delete instances of that model (e.g., by iterating over a [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") and calling `delete()` on each object individually) rather than using the bulk [`delete()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") method of a [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet").
When Django deletes an object, by default it emulates the behavior of the SQL constraint `ON DELETE CASCADE` – in other words, any objects which had foreign keys pointing at the object to be deleted will be deleted along with it. For example:
```
b = Blog.objects.get(pk=1)
# This will delete the Blog and all of its Entry objects.
b.delete()

```

This cascade behavior is customizable via the [`on_delete`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete") argument to the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey").
Note that [`delete()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") is the only [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") method that is not exposed on a [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") itself. This is a safety mechanism to prevent you from accidentally requesting `Entry.objects.delete()`, and deleting _all_ the entries. If you _do_ want to delete all the objects, then you have to explicitly request a complete query set:
```
Entry.objects.all().delete()

```
