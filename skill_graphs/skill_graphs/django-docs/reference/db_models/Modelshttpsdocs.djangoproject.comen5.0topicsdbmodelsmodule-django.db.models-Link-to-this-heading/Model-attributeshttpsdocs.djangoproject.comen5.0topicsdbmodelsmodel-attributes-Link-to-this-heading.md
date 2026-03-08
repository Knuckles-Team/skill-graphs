## Model attributes[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#model-attributes "Link to this heading")

`objects`

The most important attribute of a model is the [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager"). It’s the interface through which database query operations are provided to Django models and is used to [retrieve the instances](https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-objects) from the database. If no custom `Manager` is defined, the default name is [`objects`](https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.objects "django.db.models.Model.objects"). Managers are only accessible via model classes, not the model instances.
