## Updating multiple objects at once[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#updating-multiple-objects-at-once "Link to this heading")
Sometimes you want to set a field to a particular value for all the objects in a [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"). You can do this with the [`update()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.update "django.db.models.query.QuerySet.update") method. For example:
```
# Update all the headlines with pub_date in 2007.
Entry.objects.filter(pub_date__year=2007).update(headline="Everything is the same")

```

You can only set non-relation fields and [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") fields using this method. To update a non-relation field, provide the new value as a constant. To update [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") fields, set the new value to be the new model instance you want to point to. For example:
```
>>> b = Blog.objects.get(pk=1)

# Change every Entry so that it belongs to this Blog.
>>> Entry.objects.update(blog=b)

```

The `update()` method is applied instantly and returns the number of rows matched by the query (which may not be equal to the number of rows updated if some rows already have the new value). The only restriction on the [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") being updated is that it can only access one database table: the model’s main table. You can filter based on related fields, but you can only update columns in the model’s main table. Example:
```
>>> b = Blog.objects.get(pk=1)

# Update all the headlines belonging to this Blog.
>>> Entry.objects.filter(blog=b).update(headline="Everything is the same")

```

Be aware that the `update()` method is converted directly to an SQL statement. It is a bulk operation for direct updates. It doesn’t run any [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") methods on your models, or emit the `pre_save` or `post_save` signals (which are a consequence of calling [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save")), or honor the [`auto_now`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField.auto_now "django.db.models.DateField.auto_now") field option. If you want to save every item in a [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") and make sure that the [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") method is called on each instance, you don’t need any special function to handle that. Loop over them and call [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"):
```
for item in my_queryset:
    item.save()

```

Calls to update can also use [`F expressions`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.F "django.db.models.F") to update one field based on the value of another field in the model. This is especially useful for incrementing counters based upon their current value. For example, to increment the pingback count for every entry in the blog:
```
>>> Entry.objects.update(number_of_pingbacks=F("number_of_pingbacks") + 1)

```

However, unlike `F()` objects in filter and exclude clauses, you can’t introduce joins when you use `F()` objects in an update – you can only reference fields local to the model being updated. If you attempt to introduce a join with an `F()` object, a `FieldError` will be raised:
```
# This will raise a FieldError
>>> Entry.objects.update(headline=F("blog__name"))

```
