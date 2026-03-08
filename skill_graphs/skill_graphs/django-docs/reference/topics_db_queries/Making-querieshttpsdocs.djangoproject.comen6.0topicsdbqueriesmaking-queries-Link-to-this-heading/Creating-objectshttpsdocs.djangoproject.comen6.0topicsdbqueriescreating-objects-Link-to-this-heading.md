## Creating objects[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#creating-objects "Link to this heading")
To represent database-table data in Python objects, Django uses an intuitive system: A model class represents a database table, and an instance of that class represents a particular record in the database table.
To create an object, instantiate it using keyword arguments to the model class, then call [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") to save it to the database.
Assuming models live in a `models.py` file inside a `blog` Django app, here is an example:
```
>>> from blog.models import Blog
>>> b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
>>> b.save()

```

This performs an `INSERT` SQL statement behind the scenes. Django doesn’t hit the database until you explicitly call [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save").
The [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") method has no return value.
See also
[`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") takes a number of advanced options not described here. See the documentation for [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") for complete details.
To create and save an object in a single step, use the [`create()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.create "django.db.models.query.QuerySet.create") method.
