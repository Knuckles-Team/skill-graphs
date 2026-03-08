## Using models[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#using-models "Link to this heading")
Once you have defined your models, you need to tell Django you’re going to _use_ those models. Do this by editing your settings file and changing the [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) setting to add the name of the module that contains your `models.py`.
For example, if the models for your application live in the module `myapp.models` (the package structure that is created for an application by the [`manage.py startapp`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startapp) script), [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) should read, in part:
```
INSTALLED_APPS = [
    # ...
    "myapp",
    # ...
]

```

When you add new apps to [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS), be sure to run [`manage.py migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate), optionally making migrations for them first with [`manage.py makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations).
