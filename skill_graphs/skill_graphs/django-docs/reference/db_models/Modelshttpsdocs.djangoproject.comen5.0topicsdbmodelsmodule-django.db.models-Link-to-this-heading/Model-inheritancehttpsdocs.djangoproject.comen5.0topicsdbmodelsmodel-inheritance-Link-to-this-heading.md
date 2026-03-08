## Model inheritance[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance "Link to this heading")
Model inheritance in Django works almost identically to the way normal class inheritance works in Python, but the basics at the beginning of the page should still be followed. That means the base class should subclass [`django.db.models.Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model").
The only decision you have to make is whether you want the parent models to be models in their own right (with their own database tables), or if the parents are just holders of common information that will only be visible through the child models.
There are three styles of inheritance that are possible in Django.
  1. Often, you will just want to use the parent class to hold information that you don’t want to have to type out for each child model. This class isn’t going to ever be used in isolation, so [Abstract base classes](https://docs.djangoproject.com/en/5.0/topics/db/models/#abstract-base-classes) are what you’re after.
  2. If you’re subclassing an existing model (perhaps something from another application entirely) and want each model to have its own database table, [Multi-table inheritance](https://docs.djangoproject.com/en/5.0/topics/db/models/#multi-table-inheritance) is the way to go.
  3. Finally, if you only want to modify the Python-level behavior of a model, without changing the models fields in any way, you can use [Proxy models](https://docs.djangoproject.com/en/5.0/topics/db/models/#proxy-models).


### Abstract base classes[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#abstract-base-classes "Link to this heading")
Abstract base classes are useful when you want to put some common information into a number of other models. You write your base class and put `abstract=True` in the [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) class. This model will then not be used to create any database table. Instead, when it is used as a base class for other models, its fields will be added to those of the child class.
An example:
```
from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

```

The `Student` model will have three fields: `name`, `age` and `home_group`. The `CommonInfo` model cannot be used as a normal Django model, since it is an abstract base class. It does not generate a database table or have a manager, and cannot be instantiated or saved directly.
Fields inherited from abstract base classes can be overridden with another field or value, or be removed with `None`.
For many uses, this type of model inheritance will be exactly what you want. It provides a way to factor out common information at the Python level, while still only creating one database table per child model at the database level.
####  `Meta` inheritance[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-inheritance "Link to this heading")
When an abstract base class is created, Django makes any [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) inner class you declared in the base class available as an attribute. If a child class does not declare its own [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) class, it will inherit the parent’s [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options). If the child wants to extend the parent’s [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) class, it can subclass it. For example:
```
from django.db import models


class CommonInfo(models.Model):
    # ...
    class Meta:
        abstract = True
        ordering = ["name"]


class Student(CommonInfo):
    # ...
    class Meta(CommonInfo.Meta):
        db_table = "student_info"

```

Django does make one adjustment to the [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) class of an abstract base class: before installing the [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) attribute, it sets `abstract=False`. This means that children of abstract base classes don’t automatically become abstract classes themselves. To make an abstract base class that inherits from another abstract base class, you need to explicitly set `abstract=True` on the child.
Some attributes won’t make sense to include in the [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) class of an abstract base class. For example, including `db_table` would mean that all the child classes (the ones that don’t specify their own [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options)) would use the same database table, which is almost certainly not what you want.
Due to the way Python inheritance works, if a child class inherits from multiple abstract base classes, only the [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) options from the first listed class will be inherited by default. To inherit [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) options from multiple abstract base classes, you must explicitly declare the [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) inheritance. For example:
```
from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ["name"]


class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False


class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass

```

#### Be careful with `related_name` and `related_query_name`[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#be-careful-with-related-name-and-related-query-name "Link to this heading")
If you are using [`related_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") or [`related_query_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name") on a `ForeignKey` or `ManyToManyField`, you must always specify a _unique_ reverse name and query name for the field. This would normally cause a problem in abstract base classes, since the fields on this class are included into each of the child classes, with exactly the same values for the attributes (including [`related_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") and [`related_query_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name")) each time.
To work around this problem, when you are using [`related_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") or [`related_query_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name") in an abstract base class (only), part of the value should contain `'%(app_label)s'` and `'%(class)s'`.
  * `'%(class)s'` is replaced by the lowercased name of the child class that the field is used in.
  * `'%(app_label)s'` is replaced by the lowercased name of the app the child class is contained within. Each installed application name must be unique and the model class names within each app must also be unique, therefore the resulting name will end up being different.


For example, given an app `common/models.py`:
```
from django.db import models


class Base(models.Model):
    m2m = models.ManyToManyField(
        OtherModel,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass

```

Along with another app `rare/models.py`:
```
from common.models import Base


class ChildB(Base):
    pass

```

The reverse name of the `common.ChildA.m2m` field will be `common_childa_related` and the reverse query name will be `common_childas`. The reverse name of the `common.ChildB.m2m` field will be `common_childb_related` and the reverse query name will be `common_childbs`. Finally, the reverse name of the `rare.ChildB.m2m` field will be `rare_childb_related` and the reverse query name will be `rare_childbs`. It’s up to you how you use the `'%(class)s'` and `'%(app_label)s'` portion to construct your related name or related query name but if you forget to use it, Django will raise errors when you perform system checks (or run [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate)).
If you don’t specify a [`related_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") attribute for a field in an abstract base class, the default reverse name will be the name of the child class followed by `'_set'`, just as it normally would be if you’d declared the field directly on the child class. For example, in the above code, if the [`related_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") attribute was omitted, the reverse name for the `m2m` field would be `childa_set` in the `ChildA` case and `childb_set` for the `ChildB` field.
### Multi-table inheritance[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#multi-table-inheritance "Link to this heading")
The second type of model inheritance supported by Django is when each model in the hierarchy is a model all by itself. Each model corresponds to its own database table and can be queried and created individually. The inheritance relationship introduces links between the child model and each of its parents (via an automatically-created [`OneToOneField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField")). For example:
```
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

```

All of the fields of `Place` will also be available in `Restaurant`, although the data will reside in a different database table. So these are both possible:
```
>>> Place.objects.filter(name="Bob's Cafe")
>>> Restaurant.objects.filter(name="Bob's Cafe")

```

If you have a `Place` that is also a `Restaurant`, you can get from the `Place` object to the `Restaurant` object by using the lowercase version of the model name:
```
>>> p = Place.objects.get(id=12)
# If p is a Restaurant object, this will give the child class:
>>> p.restaurant
<Restaurant: ...>

```

However, if `p` in the above example was _not_ a `Restaurant` (it had been created directly as a `Place` object or was the parent of some other class), referring to `p.restaurant` would raise a `Restaurant.DoesNotExist` exception.
The automatically-created [`OneToOneField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField") on `Restaurant` that links it to `Place` looks like this:
```
place_ptr = models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    parent_link=True,
    primary_key=True,
)

```

You can override that field by declaring your own [`OneToOneField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField") with [`parent_link=True`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField.parent_link "django.db.models.OneToOneField.parent_link") on `Restaurant`.
####  `Meta` and multi-table inheritance[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-and-multi-table-inheritance "Link to this heading")
In the multi-table inheritance situation, it doesn’t make sense for a child class to inherit from its parent’s [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) class. All the [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) options have already been applied to the parent class and applying them again would normally only lead to contradictory behavior (this is in contrast with the abstract base class case, where the base class doesn’t exist in its own right).
So a child model does not have access to its parent’s [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) class. However, there are a few limited cases where the child inherits behavior from the parent: if the child does not specify an [`ordering`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.ordering "django.db.models.Options.ordering") attribute or a [`get_latest_by`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.get_latest_by "django.db.models.Options.get_latest_by") attribute, it will inherit these from its parent.
If the parent has an ordering and you don’t want the child to have any natural ordering, you can explicitly disable it:
```
class ChildModel(ParentModel):
    # ...
    class Meta:
        # Remove parent's ordering effect
        ordering = []

```

#### Inheritance and reverse relations[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#inheritance-and-reverse-relations "Link to this heading")
Because multi-table inheritance uses an implicit [`OneToOneField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField") to link the child and the parent, it’s possible to move from the parent down to the child, as in the above example. However, this uses up the name that is the default [`related_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") value for [`ForeignKey`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") and [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") relations. If you are putting those types of relations on a subclass of the parent model, you **must** specify the [`related_name`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") attribute on each such field. If you forget, Django will raise a validation error.
For example, using the above `Place` class again, let’s create another subclass with a [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"):
```
class Supplier(Place):
    customers = models.ManyToManyField(Place)

```

This results in the error:
```
Reverse query name for 'Supplier.customers' clashes with reverse query
name for 'Supplier.place_ptr'.

HINT: Add or change a related_name argument to the definition for
'Supplier.customers' or 'Supplier.place_ptr'.

```

Adding `related_name` to the `customers` field as follows would resolve the error: `models.ManyToManyField(Place, related_name='provider')`.
#### Specifying the parent link field[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#specifying-the-parent-link-field "Link to this heading")
As mentioned, Django will automatically create a [`OneToOneField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField") linking your child class back to any non-abstract parent models. If you want to control the name of the attribute linking back to the parent, you can create your own [`OneToOneField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField") and set [`parent_link=True`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField.parent_link "django.db.models.OneToOneField.parent_link") to indicate that your field is the link back to the parent class.
### Proxy models[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#proxy-models "Link to this heading")
When using [multi-table inheritance](https://docs.djangoproject.com/en/5.0/topics/db/models/#multi-table-inheritance), a new database table is created for each subclass of a model. This is usually the desired behavior, since the subclass needs a place to store any additional data fields that are not present on the base class. Sometimes, however, you only want to change the Python behavior of a model – perhaps to change the default manager, or add a new method.
This is what proxy model inheritance is for: creating a _proxy_ for the original model. You can create, delete and update instances of the proxy model and all the data will be saved as if you were using the original (non-proxied) model. The difference is that you can change things like the default model ordering or the default manager in the proxy, without having to alter the original.
Proxy models are declared like normal models. You tell Django that it’s a proxy model by setting the [`proxy`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.proxy "django.db.models.Options.proxy") attribute of the `Meta` class to `True`.
For example, suppose you want to add a method to the `Person` model. You can do it like this:
```
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass

```

The `MyPerson` class operates on the same database table as its parent `Person` class. In particular, any new instances of `Person` will also be accessible through `MyPerson`, and vice-versa:
```
>>> p = Person.objects.create(first_name="foobar")
>>> MyPerson.objects.get(first_name="foobar")
<MyPerson: foobar>

```

You could also use a proxy model to define a different default ordering on a model. You might not always want to order the `Person` model, but regularly order by the `last_name` attribute when you use the proxy:
```
class OrderedPerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True

```

Now normal `Person` queries will be unordered and `OrderedPerson` queries will be ordered by `last_name`.
Proxy models inherit `Meta` attributes [in the same way as regular models](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-and-multi-table-inheritance).
####  `QuerySet`s still return the model that was requested[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#querysets-still-return-the-model-that-was-requested "Link to this heading")
There is no way to have Django return, say, a `MyPerson` object whenever you query for `Person` objects. A queryset for `Person` objects will return those types of objects. The whole point of proxy objects is that code relying on the original `Person` will use those and your own code can use the extensions you included (that no other code is relying on anyway). It is not a way to replace the `Person` (or any other) model everywhere with something of your own creation.
#### Base class restrictions[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#base-class-restrictions "Link to this heading")
A proxy model must inherit from exactly one non-abstract model class. You can’t inherit from multiple non-abstract models as the proxy model doesn’t provide any connection between the rows in the different database tables. A proxy model can inherit from any number of abstract model classes, providing they do _not_ define any model fields. A proxy model may also inherit from any number of proxy models that share a common non-abstract parent class.
#### Proxy model managers[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#proxy-model-managers "Link to this heading")
If you don’t specify any model managers on a proxy model, it inherits the managers from its model parents. If you define a manager on the proxy model, it will become the default, although any managers defined on the parent classes will still be available.
Continuing our example from above, you could change the default manager used when you query the `Person` model like this:
```
from django.db import models


class NewManager(models.Manager):
    # ...
    pass


class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True

```

If you wanted to add a new manager to the Proxy, without replacing the existing default, you can use the techniques described in the [custom manager](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers-and-inheritance) documentation: create a base class containing the new managers and inherit that after the primary base class:
```
# Create an abstract class for the new manager.
class ExtraManagers(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True


class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True

```

You probably won’t need to do this very often, but, when you do, it’s possible.
#### Differences between proxy inheritance and unmanaged models[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#differences-between-proxy-inheritance-and-unmanaged-models "Link to this heading")
Proxy model inheritance might look fairly similar to creating an unmanaged model, using the [`managed`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.managed "django.db.models.Options.managed") attribute on a model’s `Meta` class.
With careful setting of [`Meta.db_table`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.db_table "django.db.models.Options.db_table") you could create an unmanaged model that shadows an existing model and adds Python methods to it. However, that would be very repetitive and fragile as you need to keep both copies synchronized if you make any changes.
On the other hand, proxy models are intended to behave exactly like the model they are proxying for. They are always in sync with the parent model since they directly inherit its fields and managers.
The general rules are:
  1. If you are mirroring an existing model or database table and don’t want all the original database table columns, use `Meta.managed=False`. That option is normally useful for modeling database views and tables not under the control of Django.
  2. If you are wanting to change the Python-only behavior of a model, but keep all the same fields as in the original, use `Meta.proxy=True`. This sets things up so that the proxy model is an exact copy of the storage structure of the original model when data is saved.


### Multiple inheritance[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#multiple-inheritance "Link to this heading")
Just as with Python’s subclassing, it’s possible for a Django model to inherit from multiple parent models. Keep in mind that normal Python name resolution rules apply. The first base class that a particular name (e.g. [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options)) appears in will be the one that is used; for example, this means that if multiple parents contain a [Meta](https://docs.djangoproject.com/en/5.0/topics/db/models/#meta-options) class, only the first one is going to be used, and all others will be ignored.
Generally, you won’t need to inherit from multiple parents. The main use-case where this is useful is for “mix-in” classes: adding a particular extra field or method to every class that inherits the mix-in. Try to keep your inheritance hierarchies as simple and straightforward as possible so that you won’t have to struggle to work out where a particular piece of information is coming from.
Note that inheriting from multiple models that have a common `id` primary key field will raise an error. To properly use multiple inheritance, you can use an explicit [`AutoField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField") in the base models:
```
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    ...


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ...


class BookReview(Book, Article):
    pass

```

Or use a common ancestor to hold the [`AutoField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField"). This requires using an explicit [`OneToOneField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField") from each parent model to the common ancestor to avoid a clash between the fields that are automatically generated and inherited by the child:
```
class Piece(models.Model):
    pass


class Article(Piece):
    article_piece = models.OneToOneField(
        Piece, on_delete=models.CASCADE, parent_link=True
    )
    ...


class Book(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)
    ...


class BookReview(Book, Article):
    pass

```

### Field name “hiding” is not permitted[¶](https://docs.djangoproject.com/en/5.0/topics/db/models/#field-name-hiding-is-not-permitted "Link to this heading")
In normal Python class inheritance, it is permissible for a child class to override any attribute from the parent class. In Django, this isn’t usually permitted for model fields. If a non-abstract model base class has a field called `author`, you can’t create another model field or define an attribute called `author` in any class that inherits from that base class.
This restriction doesn’t apply to model fields inherited from an abstract model. Such fields may be overridden with another field or value, or be removed by setting `field_name = None`.
Warning
Model managers are inherited from abstract base classes. Overriding an inherited field which is referenced by an inherited [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") may cause subtle bugs. See [custom managers and model inheritance](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers-and-inheritance).
Note
Some fields define extra attributes on the model, e.g. a [`ForeignKey`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") defines an extra attribute with `_id` appended to the field name, as well as `related_name` and `related_query_name` on the foreign model.
These extra attributes cannot be overridden unless the field that defines it is changed or removed so that it no longer defines the extra attribute.
Overriding fields in a parent model leads to difficulties in areas such as initializing new instances (specifying which field is being initialized in `Model.__init__`) and serialization. These are features which normal Python class inheritance doesn’t have to deal with in quite the same way, so the difference between Django model inheritance and Python class inheritance isn’t arbitrary.
This restriction only applies to attributes which are [`Field`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field "django.db.models.Field") instances. Normal Python attributes can be overridden if you wish. It also only applies to the name of the attribute as Python sees it: if you are manually specifying the database column name, you can have the same column name appearing in both a child and an ancestor model for multi-table inheritance (they are columns in two different database tables).
Django will raise a [`FieldError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.FieldError "django.core.exceptions.FieldError") if you override any model field in any ancestor model.
Note that because of the way fields are resolved during class definition, model fields inherited from multiple abstract parent models are resolved in a strict depth-first order. This contrasts with standard Python MRO, which is resolved breadth-first in cases of diamond shaped inheritance. This difference only affects complex model hierarchies, which (as per the advice above) you should try to avoid.
