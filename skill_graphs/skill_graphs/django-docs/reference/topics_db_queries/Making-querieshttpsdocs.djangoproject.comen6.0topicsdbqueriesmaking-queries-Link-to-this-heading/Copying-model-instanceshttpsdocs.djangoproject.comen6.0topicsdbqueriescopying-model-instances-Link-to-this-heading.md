## Copying model instances[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#copying-model-instances "Link to this heading")
Although there is no built-in method for copying model instances, it is possible to easily create new instance with all fields’ values copied. In the simplest case, you can set `pk` to `None` and [`_state.adding`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model._state "django.db.models.Model._state") to `True`. Using our blog example:
```
blog = Blog(name="My blog", tagline="Blogging is easy")
blog.save()  # blog.pk == 1

blog.pk = None
blog._state.adding = True
blog.save()  # blog.pk == 2

```

Things get more complicated if you use inheritance. Consider a subclass of `Blog`:
```
class ThemeBlog(Blog):
    theme = models.CharField(max_length=200)


django_blog = ThemeBlog(name="Django", tagline="Django is easy", theme="python")
django_blog.save()  # django_blog.pk == 3

```

Due to how inheritance works, you have to set both `pk` and `id` to `None`, and `_state.adding` to `True`:
```
django_blog.pk = None
django_blog.id = None
django_blog._state.adding = True
django_blog.save()  # django_blog.pk == 4

```

This process doesn’t copy relations that aren’t part of the model’s database table. For example, `Entry` has a `ManyToManyField` to `Author`. After duplicating an entry, you must set the many-to-many relations for the new entry:
```
entry = Entry.objects.all()[0]  # some previous entry
old_authors = entry.authors.all()
entry.pk = None
entry._state.adding = True
entry.save()
entry.authors.set(old_authors)

```

For a `OneToOneField`, you must duplicate the related object and assign it to the new object’s field to avoid violating the one-to-one unique constraint. For example, assuming `entry` is already duplicated as above:
```
detail = EntryDetail.objects.all()[0]
detail.pk = None
detail._state.adding = True
detail.entry = entry
detail.save()

```

Note that it is not possible to copy instances of models with deferred fields using this pattern unless values are assigned to them:
```
>>> blog = Blog.objects.defer("name")[0]
>>> blog.pk = None
>>> blog._state.adding = True
>>> blog.save()
Traceback (most recent call last):
    ...
AttributeError: Cannot retrieve deferred field 'name' from an unsaved model.
>>> blog.name = "Another Blog"
>>> blog.save()

```
