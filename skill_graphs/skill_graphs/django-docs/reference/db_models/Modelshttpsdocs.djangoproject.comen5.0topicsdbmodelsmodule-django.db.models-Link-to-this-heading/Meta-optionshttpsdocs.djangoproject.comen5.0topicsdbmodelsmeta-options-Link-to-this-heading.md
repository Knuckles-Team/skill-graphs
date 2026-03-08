##  `Meta` options[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options "Link to this heading")
Give your model metadata by using an inner `class Meta`, like so:
```
from django.db import models


class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"

```

Model metadata is “anything that’s not a field”, such as ordering options ([`ordering`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.ordering "django.db.models.Options.ordering")), database table name ([`db_table`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.db_table "django.db.models.Options.db_table")), or human-readable singular and plural names ([`verbose_name`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.verbose_name "django.db.models.Options.verbose_name") and [`verbose_name_plural`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.verbose_name_plural "django.db.models.Options.verbose_name_plural")). None are required, and adding `class Meta` to a model is completely optional.
A complete list of all possible `Meta` options can be found in the [model option reference](https://docs.djangoproject.com/en/5.0/ref/models/options/).
