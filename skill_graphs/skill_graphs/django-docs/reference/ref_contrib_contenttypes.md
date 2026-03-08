[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#main-content)
[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.
Menu Main navigation
  * [Overview](https://www.djangoproject.com/start/overview/)
  * [Download](https://www.djangoproject.com/download/)
  * [Documentation](https://docs.djangoproject.com/)
  * [News](https://www.djangoproject.com/weblog/)
  * [Issues](https://code.djangoproject.com/)
  * [Community](https://www.djangoproject.com/community/)
  * [Foundation](https://www.djangoproject.com/foundation/)
  * [♥ Donate](https://www.djangoproject.com/fundraising/)


Search Submit
Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
Toggle Light / Dark / Auto color theme
[Documentation](https://docs.djangoproject.com/en/6.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/6.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/contrib/contenttypes/)
  * [sv](https://docs.djangoproject.com/sv/6.0/ref/contrib/contenttypes/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/contrib/contenttypes/)
  * [pl](https://docs.djangoproject.com/pl/6.0/ref/contrib/contenttypes/)
  * [ko](https://docs.djangoproject.com/ko/6.0/ref/contrib/contenttypes/)
  * [ja](https://docs.djangoproject.com/ja/6.0/ref/contrib/contenttypes/)
  * [it](https://docs.djangoproject.com/it/6.0/ref/contrib/contenttypes/)
  * [id](https://docs.djangoproject.com/id/6.0/ref/contrib/contenttypes/)
  * [fr](https://docs.djangoproject.com/fr/6.0/ref/contrib/contenttypes/)
  * [es](https://docs.djangoproject.com/es/6.0/ref/contrib/contenttypes/)
  * [el](https://docs.djangoproject.com/el/6.0/ref/contrib/contenttypes/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/contrib/contenttypes/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/contrib/contenttypes/)
  * [5.0](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/contrib/contenttypes/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/contrib/contenttypes/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/contrib/contenttypes/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/contrib/contenttypes/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/contrib/contenttypes/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/contrib/contenttypes/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/contrib/contenttypes/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/contrib/contenttypes/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/)


  * [](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#top)


# The contenttypes framework[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes "Link to this heading")
Django includes a [`contenttypes`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes "django.contrib.contenttypes: Provides generic interface to installed models.") application that can track all of the models installed in your Django-powered project, providing a high-level, generic interface for working with your models.
## Overview[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#overview "Link to this heading")
At the heart of the contenttypes application is the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") model, which lives at `django.contrib.contenttypes.models.ContentType`. Instances of [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") represent and store information about the models installed in your project, and new instances of [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") are automatically created whenever new models are installed.
Instances of [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") have methods for returning the model classes they represent and for querying objects from those models. [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") also has a [custom manager](https://docs.djangoproject.com/en/6.0/topics/db/managers/#custom-managers) that adds methods for working with [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") and for obtaining instances of [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") for a particular model.
Relations between your models and [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") can also be used to enable “generic” relationships between an instance of one of your models and instances of any model you have installed.
## Installing the contenttypes framework[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#installing-the-contenttypes-framework "Link to this heading")
The contenttypes framework is included in the default [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) list created by `django-admin startproject`, but if you’ve removed it or if you manually set up your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) list, you can enable it by adding `'django.contrib.contenttypes'` to your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) setting.
It’s generally a good idea to have the contenttypes framework installed; several of Django’s other bundled applications require it:
  * The admin application uses it to log the history of each object added or changed through the admin interface.
  * Django’s [`authentication framework`](https://docs.djangoproject.com/en/6.0/topics/auth/#module-django.contrib.auth "django.contrib.auth: Django's authentication framework.") uses it to tie user permissions to specific models.


## The `ContentType` model[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#the-contenttype-model "Link to this heading")

_class_ ContentType[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "Link to this definition")

Each instance of [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") has two fields which, taken together, uniquely describe an installed model:

app_label[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.app_label "Link to this definition")

The name of the application the model is part of. This is taken from the [`app_label`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.app_label "django.contrib.contenttypes.models.ContentType.app_label") attribute of the model, and includes only the _last_ part of the application’s Python import path; `django.contrib.contenttypes`, for example, becomes an [`app_label`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.app_label "django.contrib.contenttypes.models.ContentType.app_label") of `contenttypes`.

model[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.model "Link to this definition")

The name of the model class.
Additionally, the following property is available:

name[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.name "Link to this definition")

The human-readable name of the content type. This is taken from the [`verbose_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.verbose_name "django.db.models.Field.verbose_name") attribute of the model.
Let’s look at an example to see how this works. If you already have the [`contenttypes`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes "django.contrib.contenttypes: Provides generic interface to installed models.") application installed, and then add [`the sites application`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#module-django.contrib.sites "django.contrib.sites: Lets you operate multiple websites from the same database and Django project") to your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) setting and run `manage.py migrate` to install it, the model [`django.contrib.sites.models.Site`](https://docs.djangoproject.com/en/6.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") will be installed into your database. Along with it a new instance of [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") will be created with the following values:
  * [`app_label`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.app_label "django.contrib.contenttypes.models.ContentType.app_label") will be set to `'sites'` (the last part of the Python path `django.contrib.sites`).
  * [`model`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.model "django.contrib.contenttypes.models.ContentType.model") will be set to `'site'`.


## Methods on `ContentType` instances[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#methods-on-contenttype-instances "Link to this heading")
Each [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") instance has methods that allow you to get from a [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") instance to the model it represents, or to retrieve objects from that model:

ContentType.get_object_for_this_type(_using =None_, _** kwargs_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.get_object_for_this_type "Link to this definition")

Takes a set of valid [lookup arguments](https://docs.djangoproject.com/en/6.0/topics/db/queries/#field-lookups-intro) for the model the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") represents, and does [`a get() lookup`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") on that model, returning the corresponding object. The `using` argument can be used to specify a different database than the default one.

ContentType.model_class()[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.model_class "Link to this definition")

Returns the model class represented by this [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") instance.
For example, we could look up the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") for the [`User`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.User "django.contrib.auth.models.User") model:
```
>>> from django.contrib.contenttypes.models import ContentType
>>> user_type = ContentType.objects.get(app_label="auth", model="user")
>>> user_type
<ContentType: user>

```

And then use it to query for a particular [`User`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.User "django.contrib.auth.models.User"), or to get access to the `User` model class:
```
>>> user_type.model_class()
<class 'django.contrib.auth.models.User'>
>>> user_type.get_object_for_this_type(username="Guido")
<User: Guido>

```

Together, [`get_object_for_this_type()`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.get_object_for_this_type "django.contrib.contenttypes.models.ContentType.get_object_for_this_type") and [`model_class()`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.model_class "django.contrib.contenttypes.models.ContentType.model_class") enable two extremely important use cases:
  1. Using these methods, you can write high-level generic code that performs queries on any installed model – instead of importing and using a single specific model class, you can pass an `app_label` and `model` into a [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") lookup at runtime, and then work with the model class or retrieve objects from it.
  2. You can relate another model to [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") as a way of tying instances of it to particular model classes, and use these methods to get access to those model classes.


Several of Django’s bundled applications make use of the latter technique. For example, [`the permissions system`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.Permission "django.contrib.auth.models.Permission") in Django’s authentication framework uses a [`Permission`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.Permission "django.contrib.auth.models.Permission") model with a foreign key to [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType"); this lets [`Permission`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.Permission "django.contrib.auth.models.Permission") represent concepts like “can add blog entry” or “can delete news story”.
### The `ContentTypeManager`[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#the-contenttypemanager "Link to this heading")

_class_ ContentTypeManager[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager "Link to this definition")

[`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") also has a custom manager, [`ContentTypeManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager "django.contrib.contenttypes.models.ContentTypeManager"), which adds the following methods:

clear_cache()[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager.clear_cache "Link to this definition")

Clears an internal cache used by [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") to keep track of models for which it has created [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") instances. You probably won’t need to call this method in application code yourself; Django will call it automatically when it’s needed.
You may need to clear the cache when testing, to reset between tests, or after preparing test state. For example:
```
class ContentTypesTests(TestCase):
    def setUp(self):
        ContentType.objects.clear_cache()
        self.addCleanup(ContentType.objects.clear_cache)

```


get_for_id(_id_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager.get_for_id "Link to this definition")

Lookup a [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") by ID. Since this method uses the same shared cache as [`get_for_model()`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager.get_for_model "django.contrib.contenttypes.models.ContentTypeManager.get_for_model"), it’s preferred to use this method over the usual `ContentType.objects.get(pk=id)`

get_for_model(_model_ , _for_concrete_model =True_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager.get_for_model "Link to this definition")

Takes either a model class or an instance of a model, and returns the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") instance representing that model. `for_concrete_model=False` allows fetching the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") of a proxy model.

get_for_models(_* models_, _for_concrete_models =True_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager.get_for_models "Link to this definition")

Takes a variadic number of model classes, and returns a dictionary mapping the model classes to the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") instances representing them. `for_concrete_models=False` allows fetching the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") of proxy models.

get_by_natural_key(_app_label_ , _model_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager.get_by_natural_key "Link to this definition")

Returns the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") instance uniquely identified by the given application label and model name. The primary purpose of this method is to allow [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") objects to be referenced via a [natural key](https://docs.djangoproject.com/en/6.0/topics/serialization/#topics-serialization-natural-keys) during deserialization.
The [`get_for_model()`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager.get_for_model "django.contrib.contenttypes.models.ContentTypeManager.get_for_model") method is especially useful when you know you need to work with a [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") but don’t want to go to the trouble of obtaining the model’s metadata to perform a manual lookup:
```
>>> from django.contrib.auth.models import User
>>> ContentType.objects.get_for_model(User)
<ContentType: user>

```

## Generic relations[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#generic-relations "Link to this heading")
Adding a foreign key from one of your own models to [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") allows your model to effectively tie itself to another model class, as in the example of the [`Permission`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.Permission "django.contrib.auth.models.Permission") model above. But it’s possible to go one step further and use [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") to enable truly generic (sometimes called “polymorphic”) relationships between models.
For example, it could be used for a tagging system like so:
```
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

```

A normal [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") can only “point to” one other model, which means that if the `TaggedItem` model used a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") it would have to choose one and only one model to store tags for. The contenttypes application provides a special field type (`GenericForeignKey`) which works around this and allows the relationship to be with any model:

_class_ GenericForeignKey[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "Link to this definition")

There are three parts to setting up a [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey"):
  1. Give your model a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") to [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType"). The usual name for this field is “content_type”.
  2. Give your model a field that can store primary key values from the models you’ll be relating to. For most models, this means a [`PositiveBigIntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PositiveBigIntegerField "django.db.models.PositiveBigIntegerField"). The usual name for this field is “object_id”.
  3. Give your model a [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey"), and pass it the names of the two fields described above. If these fields are named “content_type” and “object_id”, you can omit this – those are the default field names [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey") will look for.


Unlike for the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), a database index is _not_ automatically created on the [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey"), so it’s recommended that you use [`Meta.indexes`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.indexes "django.db.models.Options.indexes") to add your own multiple column index. This behavior [may change](https://code.djangoproject.com/ticket/23435) in the future.

for_concrete_model[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey.for_concrete_model "Link to this definition")

If `False`, the field will be able to reference proxy models. Default is `True`. This mirrors the `for_concrete_model` argument to [`get_for_model()`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentTypeManager.get_for_model "django.contrib.contenttypes.models.ContentTypeManager.get_for_model").
Primary key type compatibility
The “object_id” field doesn’t have to be the same type as the primary key fields on the related models, but their primary key values must be coercible to the same type as the “object_id” field by its [`get_db_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_value "django.db.models.Field.get_db_prep_value") method.
For example, if you want to allow generic relations to models with either [`IntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.IntegerField "django.db.models.IntegerField") or [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") primary key fields, you can use [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") for the “object_id” field on your model since integers can be coerced to strings by [`get_db_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_value "django.db.models.Field.get_db_prep_value").
For maximum flexibility you can use a [`TextField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.TextField "django.db.models.TextField") which doesn’t have a maximum length defined, however this may incur significant performance penalties depending on your database backend.
There is no one-size-fits-all solution for which field type is best. You should evaluate the models you expect to be pointing to and determine which solution will be most effective for your use case.
Serializing references to `ContentType` objects
If you’re serializing data (for example, when generating [`fixtures`](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures "django.test.TransactionTestCase.fixtures")) from a model that implements generic relations, you should probably be using a natural key to uniquely identify related [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") objects. See [natural keys](https://docs.djangoproject.com/en/6.0/topics/serialization/#topics-serialization-natural-keys) and [`dumpdata --natural-foreign`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#cmdoption-dumpdata-natural-foreign) for more information.
This will enable an API similar to the one used for a normal [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"); each `TaggedItem` will have a `content_object` field that returns the object it’s related to, and you can also assign to that field or use it when creating a `TaggedItem`:
```
>>> from django.contrib.auth.models import User
>>> guido = User.objects.get(username="Guido")
>>> t = TaggedItem(content_object=guido, tag="bdfl")
>>> t.save()
>>> t.content_object
<User: Guido>

```

If the related object is deleted, the `content_type` and `object_id` fields remain set to their original values and the `GenericForeignKey` returns `None`:
```
>>> guido.delete()
>>> t.content_object  # returns None

```

Due to the way [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey") is implemented, you cannot use such fields directly with filters (`filter()` and `exclude()`, for example) via the database API. Because a [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey") isn’t a normal field object, these examples will _not_ work:
```
# This will fail
>>> TaggedItem.objects.filter(content_object=guido)
# This will also fail
>>> TaggedItem.objects.get(content_object=guido)

```

Likewise, [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey")s do not appear in [`ModelForm`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm")s.
### Reverse generic relations[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#reverse-generic-relations "Link to this heading")

_class_ GenericRelation[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "Link to this definition")


related_query_name[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation.related_query_name "Link to this definition")

The relation on the related object back to this object doesn’t exist by default. Setting `related_query_name` creates a relation from the related object back to this one. This allows querying and filtering from the related object.
If you know which models you’ll be using most often, you can also add a “reverse” generic relationship to enable an additional API. For example:
```
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class Bookmark(models.Model):
    url = models.URLField()
    tags = GenericRelation(TaggedItem)

```

`Bookmark` instances will each have a `tags` attribute, which can be used to retrieve their associated `TaggedItems`:
```
>>> b = Bookmark(url="https://www.djangoproject.com/")
>>> b.save()
>>> t1 = TaggedItem(content_object=b, tag="django")
>>> t1.save()
>>> t2 = TaggedItem(content_object=b, tag="python")
>>> t2.save()
>>> b.tags.all()
<QuerySet [<TaggedItem: django>, <TaggedItem: python>]>

```

You can also use `add()`, `create()`, or `set()` to create relationships:
```
>>> t3 = TaggedItem(tag="Web development")
>>> b.tags.add(t3, bulk=False)
>>> b.tags.create(tag="Web framework")
<TaggedItem: Web framework>
>>> b.tags.all()
<QuerySet [<TaggedItem: django>, <TaggedItem: python>, <TaggedItem: Web development>, <TaggedItem: Web framework>]>
>>> b.tags.set([t1, t3])
>>> b.tags.all()
<QuerySet [<TaggedItem: django>, <TaggedItem: Web development>]>

```

The `remove()` call will bulk delete the specified model objects:
```
>>> b.tags.remove(t3)
>>> b.tags.all()
<QuerySet [<TaggedItem: django>]>
>>> TaggedItem.objects.all()
<QuerySet [<TaggedItem: django>]>

```

The `clear()` method can be used to bulk delete all related objects for an instance:
```
>>> b.tags.clear()
>>> b.tags.all()
<QuerySet []>
>>> TaggedItem.objects.all()
<QuerySet []>

```

Defining [`GenericRelation`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "django.contrib.contenttypes.fields.GenericRelation") with `related_query_name` set allows querying from the related object:
```
tags = GenericRelation(TaggedItem, related_query_name="bookmark")

```

This enables filtering, ordering, and other query operations on `Bookmark` from `TaggedItem`:
```
>>> # Get all tags belonging to bookmarks containing `django` in the url
>>> TaggedItem.objects.filter(bookmark__url__contains="django")
<QuerySet [<TaggedItem: django>, <TaggedItem: python>]>

```

If you don’t add the `related_query_name`, you can do the same types of lookups manually:
```
>>> bookmarks = Bookmark.objects.filter(url__contains="django")
>>> bookmark_type = ContentType.objects.get_for_model(Bookmark)
>>> TaggedItem.objects.filter(content_type__pk=bookmark_type.id, object_id__in=bookmarks)
<QuerySet [<TaggedItem: django>, <TaggedItem: python>]>

```

Just as [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey") accepts the names of the content-type and object-ID fields as arguments, so too does [`GenericRelation`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "django.contrib.contenttypes.fields.GenericRelation"); if the model which has the generic foreign key is using non-default names for those fields, you must pass the names of the fields when setting up a [`GenericRelation`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "django.contrib.contenttypes.fields.GenericRelation") to it. For example, if the `TaggedItem` model referred to above used fields named `content_type_fk` and `object_primary_key` to create its generic foreign key, then a [`GenericRelation`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "django.contrib.contenttypes.fields.GenericRelation") back to it would need to be defined like so:
```
tags = GenericRelation(
    TaggedItem,
    content_type_field="content_type_fk",
    object_id_field="object_primary_key",
)

```

Note also, that if you delete an object that has a [`GenericRelation`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "django.contrib.contenttypes.fields.GenericRelation"), any objects which have a [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey") pointing at it will be deleted as well. In the example above, this means that if a `Bookmark` object were deleted, any `TaggedItem` objects pointing at it would be deleted at the same time.
Unlike [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey") does not accept an [`on_delete`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete") argument to customize this behavior; if desired, you can avoid the cascade-deletion by not using [`GenericRelation`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "django.contrib.contenttypes.fields.GenericRelation"), and alternate behavior can be provided via the [`pre_delete`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.db.models.signals.pre_delete "django.db.models.signals.pre_delete") signal.
### Generic relations and aggregation[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#generic-relations-and-aggregation "Link to this heading")
[Django’s database aggregation API](https://docs.djangoproject.com/en/6.0/topics/db/aggregation/) works with a [`GenericRelation`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericRelation "django.contrib.contenttypes.fields.GenericRelation"). For example, you can find out how many tags all the bookmarks have:
```
>>> Bookmark.objects.aggregate(Count("tags"))
{'tags__count': 3}

```

### Generic relation in forms[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#generic-relation-in-forms "Link to this heading")
The [`django.contrib.contenttypes.forms`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes.forms "django.contrib.contenttypes.forms") module provides:
  * [`BaseGenericInlineFormSet`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.forms.BaseGenericInlineFormSet "django.contrib.contenttypes.forms.BaseGenericInlineFormSet")
  * A formset factory, [`generic_inlineformset_factory()`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.forms.generic_inlineformset_factory "django.contrib.contenttypes.forms.generic_inlineformset_factory"), for use with [`GenericForeignKey`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey "django.contrib.contenttypes.fields.GenericForeignKey").



_class_ BaseGenericInlineFormSet[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.forms.BaseGenericInlineFormSet "Link to this definition")


generic_inlineformset_factory(_model_ , _form =ModelForm_, _formset =BaseGenericInlineFormSet_, _ct_field ='content_type'_, _fk_field ='object_id'_, _fields =None_, _exclude =None_, _extra =3_, _can_order =False_, _can_delete =True_, _max_num =None_, _formfield_callback =None_, _validate_max =False_, _for_concrete_model =True_, _min_num =None_, _validate_min =False_, _absolute_max =None_, _can_delete_extra =True_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.forms.generic_inlineformset_factory "Link to this definition")

Returns a `GenericInlineFormSet` using [`modelformset_factory()`](https://docs.djangoproject.com/en/6.0/ref/forms/models/#django.forms.models.modelformset_factory "django.forms.models.modelformset_factory").
You must provide `ct_field` and `fk_field` if they are different from the defaults, `content_type` and `object_id` respectively. Other parameters are similar to those documented in [`modelformset_factory()`](https://docs.djangoproject.com/en/6.0/ref/forms/models/#django.forms.models.modelformset_factory "django.forms.models.modelformset_factory") and [`inlineformset_factory()`](https://docs.djangoproject.com/en/6.0/ref/forms/models/#django.forms.models.inlineformset_factory "django.forms.models.inlineformset_factory").
The `for_concrete_model` argument corresponds to the [`for_concrete_model`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey.for_concrete_model "django.contrib.contenttypes.fields.GenericForeignKey.for_concrete_model") argument on `GenericForeignKey`.
### Generic relations in admin[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#generic-relations-in-admin "Link to this heading")
The [`django.contrib.contenttypes.admin`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes.admin "django.contrib.contenttypes.admin") module provides [`GenericTabularInline`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericTabularInline "django.contrib.contenttypes.admin.GenericTabularInline") and [`GenericStackedInline`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericStackedInline "django.contrib.contenttypes.admin.GenericStackedInline") (subclasses of [`GenericInlineModelAdmin`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericInlineModelAdmin "django.contrib.contenttypes.admin.GenericInlineModelAdmin"))
These classes and functions enable the use of generic relations in forms and the admin. See the [model formset](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/) and [admin](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/#using-generic-relations-as-an-inline) documentation for more information.

_class_ GenericInlineModelAdmin[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericInlineModelAdmin "Link to this definition")

The [`GenericInlineModelAdmin`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericInlineModelAdmin "django.contrib.contenttypes.admin.GenericInlineModelAdmin") class inherits all properties from an [`InlineModelAdmin`](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin "django.contrib.admin.InlineModelAdmin") class. However, it adds a couple of its own for working with the generic relation:

ct_field[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericInlineModelAdmin.ct_field "Link to this definition")

The name of the [`ContentType`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType "django.contrib.contenttypes.models.ContentType") foreign key field on the model. Defaults to `content_type`.

ct_fk_field[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericInlineModelAdmin.ct_fk_field "Link to this definition")

The name of the integer field that represents the ID of the related object. Defaults to `object_id`.

_class_ GenericTabularInline[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericTabularInline "Link to this definition")


_class_ GenericStackedInline[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericStackedInline "Link to this definition")

Subclasses of [`GenericInlineModelAdmin`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.admin.GenericInlineModelAdmin "django.contrib.contenttypes.admin.GenericInlineModelAdmin") with stacked and tabular layouts, respectively.
###  `GenericPrefetch()`[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#genericprefetch "Link to this heading")

_class_ GenericPrefetch(_lookup_ , _querysets_ , _to_attr =None_)[¶](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#django.contrib.contenttypes.prefetch.GenericPrefetch "Link to this definition")

This lookup is similar to `Prefetch()` and it should only be used on `GenericForeignKey`. The `querysets` argument accepts a list of querysets, each for a different `ContentType`. This is useful for `GenericForeignKey` with non-homogeneous set of results.
```
>>> from django.contrib.contenttypes.prefetch import GenericPrefetch
>>> bookmark = Bookmark.objects.create(url="https://www.djangoproject.com/")
>>> animal = Animal.objects.create(name="lion", weight=100)
>>> TaggedItem.objects.create(tag="great", content_object=bookmark)
>>> TaggedItem.objects.create(tag="awesome", content_object=animal)
>>> prefetch = GenericPrefetch(
...     "content_object", [Bookmark.objects.all(), Animal.objects.only("name")]
... )
>>> TaggedItem.objects.prefetch_related(prefetch).all()
<QuerySet [<TaggedItem: Great>, <TaggedItem: Awesome>]>

```

Previous page and next page
[`django.contrib.auth`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/)
[The flatpages app ](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/)
[](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ David Winterbottom donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [The contenttypes framework](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/)
    * [Overview](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#overview)
    * [Installing the contenttypes framework](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#installing-the-contenttypes-framework)
    * [The `ContentType` model](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#the-contenttype-model)
    * [Methods on `ContentType` instances](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#methods-on-contenttype-instances)
      * [The `ContentTypeManager`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#the-contenttypemanager)
    * [Generic relations](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#generic-relations)
      * [Reverse generic relations](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#reverse-generic-relations)
      * [Generic relations and aggregation](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#generic-relations-and-aggregation)
      * [Generic relation in forms](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#generic-relation-in-forms)
      * [Generic relations in admin](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#generic-relations-in-admin)
      * [`GenericPrefetch()`](https://docs.djangoproject.com/en/6.0/ref/contrib/contenttypes/#genericprefetch)


### Browse
  * Prev: [`django.contrib.auth`](https://docs.djangoproject.com/en/6.0/ref/contrib/auth/)
  * Next: [The flatpages app](https://docs.djangoproject.com/en/6.0/ref/contrib/flatpages/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
      * [`contrib` packages](https://docs.djangoproject.com/en/6.0/ref/contrib/)
        * The contenttypes framework


### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
    Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
    Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.
### Download:
Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
Provided by
### Diamond and Platinum Members
  * **JetBrains**


  * **Sentry**


  * **Kraken Tech**


## Django Links
### Learn More
  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)


### Get Involved
  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)


### Get Help
  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)


### Follow Us
  * [News RSS](https://www.djangoproject.com/rss/weblog/)


### Support Us
  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)


[Django](https://www.djangoproject.com/)
  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by &


© 2005-2026 [ Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
