# Models[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#module-django.db.models "Link to this heading")
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
The basics:
  * Each model is a Python class that subclasses [`django.db.models.Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model").
  * Each attribute of the model represents a database field.
  * With all of this, Django gives you an automatically-generated database-access API; see [Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/).
