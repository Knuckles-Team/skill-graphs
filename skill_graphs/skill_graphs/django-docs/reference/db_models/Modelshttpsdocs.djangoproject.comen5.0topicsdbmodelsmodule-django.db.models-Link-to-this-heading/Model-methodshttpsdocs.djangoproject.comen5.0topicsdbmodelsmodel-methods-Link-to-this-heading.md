## Model methods[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#model-methods "Link to this heading")
Define custom methods on a model to add custom “row-level” functionality to your objects. Whereas [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") methods are intended to do “table-wide” things, model methods should act on a particular model instance.
This is a valuable technique for keeping business logic in one place – the model.
For example, this model has a few custom methods:
```
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime

        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"

```

The last method in this example is a [property](https://docs.djangoproject.com/en/5.0/glossary/#term-property).
The [model instance reference](https://docs.djangoproject.com/en/5.0/ref/models/instances/) has a complete list of [methods automatically given to each model](https://docs.djangoproject.com/en/5.0/ref/models/instances/#model-instance-methods). You can override most of these – see [overriding predefined model methods](https://docs.djangoproject.com/en/5.0/topics/db/models/#overriding-predefined-model-methods), below – but there are a couple that you’ll almost always want to define:

[`__str__()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.__str__ "django.db.models.Model.__str__")

A Python “magic method” that returns a string representation of any object. This is what Python and Django will use whenever a model instance needs to be coerced and displayed as a plain string. Most notably, this happens when you display an object in an interactive console or in the admin.
You’ll always want to define this method; the default isn’t very helpful at all.

[`get_absolute_url()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.get_absolute_url "django.db.models.Model.get_absolute_url")

This tells Django how to calculate the URL for an object. Django uses this in its admin interface, and any time it needs to figure out a URL for an object.
Any object that has a URL that uniquely identifies it should define this method.
### Overriding predefined model methods[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#overriding-predefined-model-methods "Link to this heading")
There’s another set of [model methods](https://docs.djangoproject.com/en/5.0/ref/models/instances/#model-instance-methods) that encapsulate a bunch of database behavior that you’ll want to customize. In particular you’ll often want to change the way [`save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") and [`delete()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete") work.
You’re free to override these methods (and any other model method) to alter behavior.
A classic use-case for overriding the built-in methods is if you want something to happen whenever you save an object. For example (see [`save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") for documentation of the parameters it accepts):
```
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something_else()

```

You can also prevent saving:
```
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return  # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.

```

It’s important to remember to call the superclass method – that’s that `super().save(*args, **kwargs)` business – to ensure that the object still gets saved into the database. If you forget to call the superclass method, the default behavior won’t happen and the database won’t get touched.
It’s also important that you pass through the arguments that can be passed to the model method – that’s what the `*args, **kwargs` bit does. Django will, from time to time, extend the capabilities of built-in model methods, adding new arguments. If you use `*args, **kwargs` in your method definitions, you are guaranteed that your code will automatically support those arguments when they are added.
If you wish to update a field value in the [`save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") method, you may also want to have this field added to the `update_fields` keyword argument. This will ensure the field is saved when `update_fields` is specified. For example:
```
from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.TextField()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        if update_fields is not None and "name" in update_fields:
            update_fields = {"slug"}.union(update_fields)
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

```

See [Specifying which fields to save](https://docs.djangoproject.com/en/5.0/ref/models/instances/#ref-models-update-fields) for more details.
Overridden model methods are not called on bulk operations
Note that the [`delete()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete") method for an object is not necessarily called when [deleting objects in bulk using a QuerySet](https://docs.djangoproject.com/en/5.0/topics/db/queries/#topics-db-queries-delete) or as a result of a [`cascading delete`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete"). To ensure customized delete logic gets executed, you can use [`pre_delete`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_delete "django.db.models.signals.pre_delete") and/or [`post_delete`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_delete "django.db.models.signals.post_delete") signals.
Unfortunately, there isn’t a workaround when [`creating`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create "django.db.models.query.QuerySet.bulk_create") or [`updating`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.update "django.db.models.query.QuerySet.update") objects in bulk, since none of [`save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"), [`pre_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_save "django.db.models.signals.pre_save"), and [`post_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_save "django.db.models.signals.post_save") are called.
### Executing custom SQL[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#executing-custom-sql "Link to this heading")
Another common pattern is writing custom SQL statements in model methods and module-level methods. For more details on using raw SQL, see the documentation on [using raw SQL](https://docs.djangoproject.com/en/5.0/topics/db/sql/).
