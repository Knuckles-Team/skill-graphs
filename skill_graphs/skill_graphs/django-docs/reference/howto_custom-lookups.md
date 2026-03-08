This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#main-content)
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
[Documentation](https://docs.djangoproject.com/en/5.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/5.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/custom-lookups/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/custom-lookups/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/custom-lookups/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/custom-lookups/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/custom-lookups/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/custom-lookups/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/custom-lookups/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/custom-lookups/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/custom-lookups/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/custom-lookups/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/custom-lookups/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/custom-lookups/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/custom-lookups/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/custom-lookups/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/custom-lookups/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/custom-lookups/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/custom-lookups/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/custom-lookups/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/custom-lookups/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/custom-lookups/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/custom-lookups/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/custom-lookups/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/custom-lookups/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/custom-lookups/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/custom-lookups/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/custom-lookups/)


  * [](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#top)


# How to write custom lookups[¶](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#how-to-write-custom-lookups "Link to this heading")
Django offers a wide variety of [built-in lookups](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#field-lookups) for filtering (for example, `exact` and `icontains`). This documentation explains how to write custom lookups and how to alter the working of existing lookups. For the API references of lookups, see the [Lookup API reference](https://docs.djangoproject.com/en/5.0/ref/models/lookups/).
## A lookup example[¶](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#a-lookup-example "Link to this heading")
Let’s start with a small custom lookup. We will write a custom lookup `ne` which works opposite to `exact`. `Author.objects.filter(name__ne='Jack')` will translate to the SQL:
```
"author"."name" <> 'Jack'

```

This SQL is backend independent, so we don’t need to worry about different databases.
There are two steps to making this work. Firstly we need to implement the lookup, then we need to tell Django about it:
```
from django.db.models import Lookup


class NotEqual(Lookup):
    lookup_name = "ne"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return "%s <> %s" % (lhs, rhs), params

```

To register the `NotEqual` lookup we will need to call `register_lookup` on the field class we want the lookup to be available for. In this case, the lookup makes sense on all `Field` subclasses, so we register it with `Field` directly:
```
from django.db.models import Field

Field.register_lookup(NotEqual)

```

Lookup registration can also be done using a decorator pattern:
```
from django.db.models import Field


@Field.register_lookup
class NotEqualLookup(Lookup): ...

```

We can now use `foo__ne` for any field `foo`. You will need to ensure that this registration happens before you try to create any querysets using it. You could place the implementation in a `models.py` file, or register the lookup in the `ready()` method of an `AppConfig`.
Taking a closer look at the implementation, the first required attribute is `lookup_name`. This allows the ORM to understand how to interpret `name__ne` and use `NotEqual` to generate the SQL. By convention, these names are always lowercase strings containing only letters, but the only hard requirement is that it must not contain the string `__`.
We then need to define the `as_sql` method. This takes a `SQLCompiler` object, called `compiler`, and the active database connection. `SQLCompiler` objects are not documented, but the only thing we need to know about them is that they have a `compile()` method which returns a tuple containing an SQL string, and the parameters to be interpolated into that string. In most cases, you don’t need to use it directly and can pass it on to `process_lhs()` and `process_rhs()`.
A `Lookup` works against two values, `lhs` and `rhs`, standing for left-hand side and right-hand side. The left-hand side is usually a field reference, but it can be anything implementing the [query expression API](https://docs.djangoproject.com/en/5.0/ref/models/lookups/#query-expression). The right-hand is the value given by the user. In the example `Author.objects.filter(name__ne='Jack')`, the left-hand side is a reference to the `name` field of the `Author` model, and `'Jack'` is the right-hand side.
We call `process_lhs` and `process_rhs` to convert them into the values we need for SQL using the `compiler` object described before. These methods return tuples containing some SQL and the parameters to be interpolated into that SQL, just as we need to return from our `as_sql` method. In the above example, `process_lhs` returns `('"author"."name"', [])` and `process_rhs` returns `('"%s"', ['Jack'])`. In this example there were no parameters for the left hand side, but this would depend on the object we have, so we still need to include them in the parameters we return.
Finally we combine the parts into an SQL expression with `<>`, and supply all the parameters for the query. We then return a tuple containing the generated SQL string and the parameters.
## A transformer example[¶](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#a-transformer-example "Link to this heading")
The custom lookup above is great, but in some cases you may want to be able to chain lookups together. For example, let’s suppose we are building an application where we want to make use of the `abs()` operator. We have an `Experiment` model which records a start value, end value, and the change (start - end). We would like to find all experiments where the change was equal to a certain amount (`Experiment.objects.filter(change__abs=27)`), or where it did not exceed a certain amount (`Experiment.objects.filter(change__abs__lt=27)`).
Note
This example is somewhat contrived, but it nicely demonstrates the range of functionality which is possible in a database backend independent manner, and without duplicating functionality already in Django.
We will start by writing an `AbsoluteValue` transformer. This will use the SQL function `ABS()` to transform the value before comparison:
```
from django.db.models import Transform


class AbsoluteValue(Transform):
    lookup_name = "abs"
    function = "ABS"

```

Next, let’s register it for `IntegerField`:
```
from django.db.models import IntegerField

IntegerField.register_lookup(AbsoluteValue)

```

We can now run the queries we had before. `Experiment.objects.filter(change__abs=27)` will generate the following SQL:
```
SELECT ... WHERE ABS("experiments"."change") = 27

```

By using `Transform` instead of `Lookup` it means we are able to chain further lookups afterward. So `Experiment.objects.filter(change__abs__lt=27)` will generate the following SQL:
```
SELECT ... WHERE ABS("experiments"."change") < 27

```

Note that in case there is no other lookup specified, Django interprets `change__abs=27` as `change__abs__exact=27`.
This also allows the result to be used in `ORDER BY` and `DISTINCT ON` clauses. For example `Experiment.objects.order_by('change__abs')` generates:
```
SELECT ... ORDER BY ABS("experiments"."change") ASC

```

And on databases that support distinct on fields (such as PostgreSQL), `Experiment.objects.distinct('change__abs')` generates:
```
SELECT ... DISTINCT ON ABS("experiments"."change")

```

When looking for which lookups are allowable after the `Transform` has been applied, Django uses the `output_field` attribute. We didn’t need to specify this here as it didn’t change, but supposing we were applying `AbsoluteValue` to some field which represents a more complex type (for example a point relative to an origin, or a complex number) then we may have wanted to specify that the transform returns a `FloatField` type for further lookups. This can be done by adding an `output_field` attribute to the transform:
```
from django.db.models import FloatField, Transform


class AbsoluteValue(Transform):
    lookup_name = "abs"
    function = "ABS"

    @property
    def output_field(self):
        return FloatField()

```

This ensures that further lookups like `abs__lte` behave as they would for a `FloatField`.
## Writing an efficient `abs__lt` lookup[¶](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#writing-an-efficient-abs-lt-lookup "Link to this heading")
When using the above written `abs` lookup, the SQL produced will not use indexes efficiently in some cases. In particular, when we use `change__abs__lt=27`, this is equivalent to `change__gt=-27` AND `change__lt=27`. (For the `lte` case we could use the SQL `BETWEEN`).
So we would like `Experiment.objects.filter(change__abs__lt=27)` to generate the following SQL:
```
SELECT .. WHERE "experiments"."change" < 27 AND "experiments"."change" > -27

```

The implementation is:
```
from django.db.models import Lookup


class AbsoluteValueLessThan(Lookup):
    lookup_name = "lt"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = compiler.compile(self.lhs.lhs)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params + lhs_params + rhs_params
        return "%s < %s AND %s > -%s" % (lhs, rhs, lhs, rhs), params


AbsoluteValue.register_lookup(AbsoluteValueLessThan)

```

There are a couple of notable things going on. First, `AbsoluteValueLessThan` isn’t calling `process_lhs()`. Instead it skips the transformation of the `lhs` done by `AbsoluteValue` and uses the original `lhs`. That is, we want to get `"experiments"."change"` not `ABS("experiments"."change")`. Referring directly to `self.lhs.lhs` is safe as `AbsoluteValueLessThan` can be accessed only from the `AbsoluteValue` lookup, that is the `lhs` is always an instance of `AbsoluteValue`.
Notice also that as both sides are used multiple times in the query the params need to contain `lhs_params` and `rhs_params` multiple times.
The final query does the inversion (`27` to `-27`) directly in the database. The reason for doing this is that if the `self.rhs` is something else than a plain integer value (for example an `F()` reference) we can’t do the transformations in Python.
Note
In fact, most lookups with `__abs` could be implemented as range queries like this, and on most database backends it is likely to be more sensible to do so as you can make use of the indexes. However with PostgreSQL you may want to add an index on `abs(change)` which would allow these queries to be very efficient.
## A bilateral transformer example[¶](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#a-bilateral-transformer-example "Link to this heading")
The `AbsoluteValue` example we discussed previously is a transformation which applies to the left-hand side of the lookup. There may be some cases where you want the transformation to be applied to both the left-hand side and the right-hand side. For instance, if you want to filter a queryset based on the equality of the left and right-hand side insensitively to some SQL function.
Let’s examine case-insensitive transformations here. This transformation isn’t very useful in practice as Django already comes with a bunch of built-in case-insensitive lookups, but it will be a nice demonstration of bilateral transformations in a database-agnostic way.
We define an `UpperCase` transformer which uses the SQL function `UPPER()` to transform the values before comparison. We define [`bilateral = True`](https://docs.djangoproject.com/en/5.0/ref/models/lookups/#django.db.models.Transform.bilateral "django.db.models.Transform.bilateral") to indicate that this transformation should apply to both `lhs` and `rhs`:
```
from django.db.models import Transform


class UpperCase(Transform):
    lookup_name = "upper"
    function = "UPPER"
    bilateral = True

```

Next, let’s register it:
```
from django.db.models import CharField, TextField

CharField.register_lookup(UpperCase)
TextField.register_lookup(UpperCase)

```

Now, the queryset `Author.objects.filter(name__upper="doe")` will generate a case insensitive query like this:
```
SELECT ... WHERE UPPER("author"."name") = UPPER('doe')

```

## Writing alternative implementations for existing lookups[¶](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#writing-alternative-implementations-for-existing-lookups "Link to this heading")
Sometimes different database vendors require different SQL for the same operation. For this example we will rewrite a custom implementation for MySQL for the NotEqual operator. Instead of `<>` we will be using `!=` operator. (Note that in reality almost all databases support both, including all the official databases supported by Django).
We can change the behavior on a specific backend by creating a subclass of `NotEqual` with an `as_mysql` method:
```
class MySQLNotEqual(NotEqual):
    def as_mysql(self, compiler, connection, **extra_context):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return "%s != %s" % (lhs, rhs), params


Field.register_lookup(MySQLNotEqual)

```

We can then register it with `Field`. It takes the place of the original `NotEqual` class as it has the same `lookup_name`.
When compiling a query, Django first looks for `as_%s % connection.vendor` methods, and then falls back to `as_sql`. The vendor names for the in-built backends are `sqlite`, `postgresql`, `oracle` and `mysql`.
## How Django determines the lookups and transforms which are used[¶](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#how-django-determines-the-lookups-and-transforms-which-are-used "Link to this heading")
In some cases you may wish to dynamically change which `Transform` or `Lookup` is returned based on the name passed in, rather than fixing it. As an example, you could have a field which stores coordinates or an arbitrary dimension, and wish to allow a syntax like `.filter(coords__x7=4)` to return the objects where the 7th coordinate has value 4. In order to do this, you would override `get_lookup` with something like:
```
class CoordinatesField(Field):
    def get_lookup(self, lookup_name):
        if lookup_name.startswith("x"):
            try:
                dimension = int(lookup_name.removeprefix("x"))
            except ValueError:
                pass
            else:
                return get_coordinate_lookup(dimension)
        return super().get_lookup(lookup_name)

```

You would then define `get_coordinate_lookup` appropriately to return a `Lookup` subclass which handles the relevant value of `dimension`.
There is a similarly named method called `get_transform()`. `get_lookup()` should always return a `Lookup` subclass, and `get_transform()` a `Transform` subclass. It is important to remember that `Transform` objects can be further filtered on, and `Lookup` objects cannot.
When filtering, if there is only one lookup name remaining to be resolved, we will look for a `Lookup`. If there are multiple names, it will look for a `Transform`. In the situation where there is only one name and a `Lookup` is not found, we look for a `Transform` and then the `exact` lookup on that `Transform`. All call sequences always end with a `Lookup`. To clarify:
  * `.filter(myfield__mylookup)` will call `myfield.get_lookup('mylookup')`.
  * `.filter(myfield__mytransform__mylookup)` will call `myfield.get_transform('mytransform')`, and then `mytransform.get_lookup('mylookup')`.
  * `.filter(myfield__mytransform)` will first call `myfield.get_lookup('mytransform')`, which will fail, so it will fall back to calling `myfield.get_transform('mytransform')` and then `mytransform.get_lookup('exact')`.

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/custom-model-fields/)
[How to implement a custom template backend ](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/)
[](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Landscape donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to write custom lookups](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/)
    * [A lookup example](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#a-lookup-example)
    * [A transformer example](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#a-transformer-example)
    * [Writing an efficient `abs__lt` lookup](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#writing-an-efficient-abs-lt-lookup)
    * [A bilateral transformer example](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#a-bilateral-transformer-example)
    * [Writing alternative implementations for existing lookups](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#writing-alternative-implementations-for-existing-lookups)
    * [How Django determines the lookups and transforms which are used](https://docs.djangoproject.com/en/5.0/howto/custom-lookups/#how-django-determines-the-lookups-and-transforms-which-are-used)


### Browse
  * Prev: [How to create custom model fields](https://docs.djangoproject.com/en/5.0/howto/custom-model-fields/)
  * Next: [How to implement a custom template backend](https://docs.djangoproject.com/en/5.0/howto/custom-template-backend/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to write custom lookups


### Getting help

[FAQ](https://docs.djangoproject.com/en/5.0/faq/)
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
Offline (Django 5.0): [HTML](https://media.djangoproject.com/docs/django-docs-5.0-en.zip) |
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
