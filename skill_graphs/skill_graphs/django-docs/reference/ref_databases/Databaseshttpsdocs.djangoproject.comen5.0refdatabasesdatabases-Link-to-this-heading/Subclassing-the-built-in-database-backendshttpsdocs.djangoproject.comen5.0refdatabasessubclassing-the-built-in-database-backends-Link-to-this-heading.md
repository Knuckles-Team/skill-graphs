## Subclassing the built-in database backends[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#subclassing-the-built-in-database-backends "Link to this heading")
Django comes with built-in database backends. You may subclass an existing database backends to modify its behavior, features, or configuration.
Consider, for example, that you need to change a single database feature. First, you have to create a new directory with a `base` module in it. For example:
```
mysite/
    ...
    mydbengine/
        __init__.py
        base.py

```

The `base.py` module must contain a class named `DatabaseWrapper` that subclasses an existing engine from the `django.db.backends` module. Here’s an example of subclassing the PostgreSQL engine to change a feature class `allows_group_by_selected_pks_on_model`:
`mysite/mydbengine/base.py`[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#id18 "Link to this code")
```
from django.db.backends.postgresql import base, features


class DatabaseFeatures(features.DatabaseFeatures):
    def allows_group_by_selected_pks_on_model(self, model):
        return True


class DatabaseWrapper(base.DatabaseWrapper):
    features_class = DatabaseFeatures

```

Finally, you must specify a [`DATABASE-ENGINE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ENGINE) in your `settings.py` file:
```
DATABASES = {
    "default": {
        "ENGINE": "mydbengine",
        # ...
    },
}

```

You can see the current list of database engines by looking in
