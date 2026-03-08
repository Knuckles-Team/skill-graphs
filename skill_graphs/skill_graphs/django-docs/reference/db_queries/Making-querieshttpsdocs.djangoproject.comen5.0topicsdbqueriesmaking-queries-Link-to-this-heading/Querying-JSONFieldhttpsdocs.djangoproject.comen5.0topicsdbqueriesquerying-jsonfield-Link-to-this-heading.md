## Querying `JSONField`[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#querying-jsonfield "Link to this heading")
Lookups implementation is different in [`JSONField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.JSONField "django.db.models.JSONField"), mainly due to the existence of key transformations. To demonstrate, we will use the following example model:
```
from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name

```

### Storing and querying for `None`[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#storing-and-querying-for-none "Link to this heading")
As with other fields, storing `None` as the field’s value will store it as SQL `NULL`. While not recommended, it is possible to store JSON scalar `null` instead of SQL `NULL` by using [`Value(None, JSONField())`](https://docs.djangoproject.com/en/5.0/ref/models/expressions/#django.db.models.Value "django.db.models.Value").
Whichever of the values is stored, when retrieved from the database, the Python representation of the JSON scalar `null` is the same as SQL `NULL`, i.e. `None`. Therefore, it can be hard to distinguish between them.
This only applies to `None` as the top-level value of the field. If `None` is inside a `null`.
When querying, `None` value will always be interpreted as JSON `null`. To query for SQL `NULL`, use [`isnull`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-isnull):
```
>>> Dog.objects.create(name="Max", data=None)  # SQL NULL.
<Dog: Max>
>>> Dog.objects.create(name="Archie", data=Value(None, JSONField()))  # JSON null.
<Dog: Archie>
>>> Dog.objects.filter(data=None)
<QuerySet [<Dog: Archie>]>
>>> Dog.objects.filter(data=Value(None, JSONField()))
<QuerySet [<Dog: Archie>]>
>>> Dog.objects.filter(data__isnull=True)
<QuerySet [<Dog: Max>]>
>>> Dog.objects.filter(data__isnull=False)
<QuerySet [<Dog: Archie>]>

```

Unless you are sure you wish to work with SQL `NULL` values, consider setting `null=False` and providing a suitable default for empty values, such as `default=dict`.
Note
Storing JSON scalar `null` does not violate [`null=False`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null").
Changed in Django 4.2:
Support for expressing JSON `null` using `Value(None, JSONField())` was added.
Deprecated since version 4.2: Passing `Value("null")` to express JSON `null` is deprecated.
### Key, index, and path transforms[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#key-index-and-path-transforms "Link to this heading")
To query based on a given dictionary key, use that key as the lookup name:
```
>>> Dog.objects.create(
...     name="Rufus",
...     data={
...         "breed": "labrador",
...         "owner": {
...             "name": "Bob",
...             "other_pets": [
...                 {
...                     "name": "Fishy",
...                 }
...             ],
...         },
...     },
... )
<Dog: Rufus>
>>> Dog.objects.create(name="Meg", data={"breed": "collie", "owner": None})
<Dog: Meg>
>>> Dog.objects.filter(data__breed="collie")
<QuerySet [<Dog: Meg>]>

```

Multiple keys can be chained together to form a path lookup:
```
>>> Dog.objects.filter(data__owner__name="Bob")
<QuerySet [<Dog: Rufus>]>

```

If the key is an integer, it will be interpreted as an index transform in an array:
```
>>> Dog.objects.filter(data__owner__other_pets__0__name="Fishy")
<QuerySet [<Dog: Rufus>]>

```

If the key you wish to query by clashes with the name of another lookup, use the [`contains`](https://docs.djangoproject.com/en/5.0/topics/db/queries/#std-fieldlookup-jsonfield.contains) lookup instead.
To query for missing keys, use the `isnull` lookup:
```
>>> Dog.objects.create(name="Shep", data={"breed": "collie"})
<Dog: Shep>
>>> Dog.objects.filter(data__owner__isnull=True)
<QuerySet [<Dog: Shep>]>

```

Note
The lookup examples given above implicitly use the [`exact`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-exact) lookup. Key, index, and path transforms can also be chained with: [`icontains`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-icontains), [`endswith`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-endswith), [`iendswith`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-iendswith), [`iexact`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-iexact), [`regex`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-regex), [`iregex`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-iregex), [`startswith`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-startswith), [`istartswith`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-istartswith), [`lt`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-lt), [`lte`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-lte), [`gt`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-gt), and [`gte`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-gte), as well as with [Containment and key lookups](https://docs.djangoproject.com/en/5.0/topics/db/queries/#containment-and-key-lookups).
####  `KT()` expressions[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#kt-expressions "Link to this heading")
New in Django 4.2.

_class_ KT(_lookup_)[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#django.db.models.fields.json.KT "Link to this definition")

Represents the text value of a key, index, or path transform of [`JSONField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.JSONField "django.db.models.JSONField"). You can use the double underscore notation in `lookup` to chain dictionary key and index transforms.
For example:
```
>>> from django.db.models.fields.json import KT
>>> Dog.objects.create(
...     name="Shep",
...     data={
...         "owner": {"name": "Bob"},
...         "breed": ["collie", "lhasa apso"],
...     },
... )
<Dog: Shep>
>>> Dogs.objects.annotate(
...     first_breed=KT("data__breed__1"), owner_name=KT("data__owner__name")
... ).filter(first_breed__startswith="lhasa", owner_name="Bob")
<QuerySet [<Dog: Shep>]>

```

Note
Due to the way in which key-path queries work, [`exclude()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") and [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") are not guaranteed to produce exhaustive sets. If you want to include objects that do not have the path, add the `isnull` lookup.
Warning
Since any string could be a key in a JSON object, any lookup other than those listed below will be interpreted as a key lookup. No errors are raised. Be extra careful for typing mistakes, and always check your queries work as you intend.
MariaDB and Oracle users
Using [`order_by()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.order_by "django.db.models.query.QuerySet.order_by") on key, index, or path transforms will sort the objects using the string representation of the values. This is because MariaDB and Oracle Database do not provide a function that converts JSON values into their equivalent SQL values.
Oracle users
On Oracle Database, using `None` as the lookup value in an [`exclude()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") query will return objects that do not have `null` as the value at the given path, including objects that do not have the path. On other database backends, the query will return objects that have the path and the value is not `null`.
PostgreSQL users
On PostgreSQL, if only one key or index is used, the SQL operator `->` is used. If multiple operators are used then the `#>` operator is used.
SQLite users
On SQLite, `"true"`, `"false"`, and `"null"` string values will always be interpreted as `True`, `False`, and JSON `null` respectively.
### Containment and key lookups[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#containment-and-key-lookups "Link to this heading")
####  `contains`[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#contains "Link to this heading")
The [`contains`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-contains) lookup is overridden on `JSONField`. The returned objects are those where the given `dict` of key-value pairs are all contained in the top-level of the field. For example:
```
>>> Dog.objects.create(name="Rufus", data={"breed": "labrador", "owner": "Bob"})
<Dog: Rufus>
>>> Dog.objects.create(name="Meg", data={"breed": "collie", "owner": "Bob"})
<Dog: Meg>
>>> Dog.objects.create(name="Fred", data={})
<Dog: Fred>
>>> Dog.objects.filter(data__contains={"owner": "Bob"})
<QuerySet [<Dog: Rufus>, <Dog: Meg>]>
>>> Dog.objects.filter(data__contains={"breed": "collie"})
<QuerySet [<Dog: Meg>]>

```

Oracle and SQLite
`contains` is not supported on Oracle and SQLite.
####  `contained_by`[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#contained-by "Link to this heading")
This is the inverse of the [`contains`](https://docs.djangoproject.com/en/5.0/topics/db/queries/#std-fieldlookup-jsonfield.contains) lookup - the objects returned will be those where the key-value pairs on the object are a subset of those in the value passed. For example:
```
>>> Dog.objects.create(name="Rufus", data={"breed": "labrador", "owner": "Bob"})
<Dog: Rufus>
>>> Dog.objects.create(name="Meg", data={"breed": "collie", "owner": "Bob"})
<Dog: Meg>
>>> Dog.objects.create(name="Fred", data={})
<Dog: Fred>
>>> Dog.objects.filter(data__contained_by={"breed": "collie", "owner": "Bob"})
<QuerySet [<Dog: Meg>, <Dog: Fred>]>
>>> Dog.objects.filter(data__contained_by={"breed": "collie"})
<QuerySet [<Dog: Fred>]>

```

Oracle and SQLite
`contained_by` is not supported on Oracle and SQLite.
####  `has_key`[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#has-key "Link to this heading")
Returns objects where the given key is in the top-level of the data. For example:
```
>>> Dog.objects.create(name="Rufus", data={"breed": "labrador"})
<Dog: Rufus>
>>> Dog.objects.create(name="Meg", data={"breed": "collie", "owner": "Bob"})
<Dog: Meg>
>>> Dog.objects.filter(data__has_key="owner")
<QuerySet [<Dog: Meg>]>

```

####  `has_keys`[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#has-keys "Link to this heading")
Returns objects where all of the given keys are in the top-level of the data. For example:
```
>>> Dog.objects.create(name="Rufus", data={"breed": "labrador"})
<Dog: Rufus>
>>> Dog.objects.create(name="Meg", data={"breed": "collie", "owner": "Bob"})
<Dog: Meg>
>>> Dog.objects.filter(data__has_keys=["breed", "owner"])
<QuerySet [<Dog: Meg>]>

```

####  `has_any_keys`[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#has-any-keys "Link to this heading")
Returns objects where any of the given keys are in the top-level of the data. For example:
```
>>> Dog.objects.create(name="Rufus", data={"breed": "labrador"})
<Dog: Rufus>
>>> Dog.objects.create(name="Meg", data={"owner": "Bob"})
<Dog: Meg>
>>> Dog.objects.filter(data__has_any_keys=["owner", "breed"])
<QuerySet [<Dog: Rufus>, <Dog: Meg>]>

```
