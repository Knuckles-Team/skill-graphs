## Retrieving objects[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-objects "Link to this heading")
To retrieve objects from your database, construct a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") via a [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") on your model class.
A [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") represents a collection of objects from your database. It can have zero, one or many _filters_. Filters narrow down the query results based on the given parameters. In SQL terms, a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") equates to a `SELECT` statement, and a filter is a limiting clause such as `WHERE` or `LIMIT`.
You get a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") by using your model’s [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager"). Each model has at least one [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager"), and it’s called [`objects`](https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.objects "django.db.models.Model.objects") by default. Access it directly via the model class, like so:
```
>>> Blog.objects
<django.db.models.manager.Manager object at ...>
>>> b = Blog(name="Foo", tagline="Bar")
>>> b.objects
Traceback:
    ...
AttributeError: "Manager isn't accessible via Blog instances."

```

Note
`Managers` are accessible only via model classes, rather than from model instances, to enforce a separation between “table-level” operations and “record-level” operations.
The [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") is the main source of `QuerySets` for a model. For example, `Blog.objects.all()` returns a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") that contains all `Blog` objects in the database.
### Retrieving all objects[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-all-objects "Link to this heading")
The simplest way to retrieve objects from a table is to get all of them. To do this, use the [`all()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.all "django.db.models.query.QuerySet.all") method on a [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager"):
```
>>> all_entries = Entry.objects.all()

```

The [`all()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.all "django.db.models.query.QuerySet.all") method returns a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") of all the objects in the database.
### Retrieving specific objects with filters[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-specific-objects-with-filters "Link to this heading")
The [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") returned by [`all()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.all "django.db.models.query.QuerySet.all") describes all objects in the database table. Usually, though, you’ll need to select only a subset of the complete set of objects.
To create such a subset, you refine the initial [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), adding filter conditions. The two most common ways to refine a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") are:

`filter(**kwargs)`

Returns a new [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing objects that match the given lookup parameters.

`exclude(**kwargs)`

Returns a new [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing objects that do _not_ match the given lookup parameters.
The lookup parameters (`**kwargs` in the above function definitions) should be in the format described in [Field lookups](https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups) below.
For example, to get a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") of blog entries from the year 2006, use [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") like so:
```
Entry.objects.filter(pub_date__year=2006)

```

With the default manager class, it is the same as:
```
Entry.objects.all().filter(pub_date__year=2006)

```

#### Chaining filters[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#chaining-filters "Link to this heading")
The result of refining a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is itself a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), so it’s possible to chain refinements together. For example:
```
>>> Entry.objects.filter(headline__startswith="What").exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(pub_date__gte=datetime.date(2005, 1, 30))

```

This takes the initial [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") of all entries in the database, adds a filter, then an exclusion, then another filter. The final result is a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing all entries with a headline that starts with “What”, that were published between January 30, 2005, and the current day.
#### Filtered `QuerySet`s are unique[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#filtered-querysets-are-unique "Link to this heading")
Each time you refine a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), you get a brand-new [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") that is in no way bound to the previous [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"). Each refinement creates a separate and distinct [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") that can be stored, used and reused.
Example:
```
>>> q1 = Entry.objects.filter(headline__startswith="What")
>>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
>>> q3 = q1.filter(pub_date__gte=datetime.date.today())

```

These three `QuerySets` are separate. The first is a base [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing all entries that contain a headline starting with “What”. The second is a subset of the first, with an additional criteria that excludes records whose `pub_date` is today or in the future. The third is a subset of the first, with an additional criteria that selects only the records whose `pub_date` is today or in the future. The initial [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") (`q1`) is unaffected by the refinement process.
####  `QuerySet`s are lazy[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#querysets-are-lazy "Link to this heading")
`QuerySets` are lazy – the act of creating a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") doesn’t involve any database activity. You can stack filters together all day long, and Django won’t actually run the query until the [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is _evaluated_. Take a look at this example:
```
>>> q = Entry.objects.filter(headline__startswith="What")
>>> q = q.filter(pub_date__lte=datetime.date.today())
>>> q = q.exclude(body_text__icontains="food")
>>> print(q)

```

Though this looks like three database hits, in fact it hits the database only once, at the last line (`print(q)`). In general, the results of a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") aren’t fetched from the database until you “ask” for them. When you do, the [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is _evaluated_ by accessing the database. For more details on exactly when evaluation takes place, see [When QuerySets are evaluated](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#when-querysets-are-evaluated).
### Retrieving a single object with `get()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-a-single-object-with-get "Link to this heading")
[`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") will always give you a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), even if only a single object matches the query - in this case, it will be a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") containing a single element.
If you know there is only one object that matches your query, you can use the [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") method on a [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") which returns the object directly:
```
>>> one_entry = Entry.objects.get(pk=1)

```

You can use any query expression with [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get"), just like with [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") - again, see [Field lookups](https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups) below.
Note that there is a difference between using [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get"), and using [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") with a slice of `[0]`. If there are no results that match the query, [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") will raise a `DoesNotExist` exception. This exception is an attribute of the model class that the query is being performed on - so in the code above, if there is no `Entry` object with a primary key of 1, Django will raise `Entry.DoesNotExist`.
Similarly, Django will complain if more than one item matches the [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") query. In this case, it will raise [`MultipleObjectsReturned`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.MultipleObjectsReturned "django.core.exceptions.MultipleObjectsReturned"), which again is an attribute of the model class itself.
### Other `QuerySet` methods[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#other-queryset-methods "Link to this heading")
Most of the time you’ll use [`all()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.all "django.db.models.query.QuerySet.all"), [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get"), [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") and [`exclude()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") when you need to look up objects from the database. However, that’s far from all there is; see the [QuerySet API Reference](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#queryset-api) for a complete list of all the various [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") methods.
### Limiting `QuerySet`s[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#limiting-querysets "Link to this heading")
Use a subset of Python’s array-slicing syntax to limit your [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") to a certain number of results. This is the equivalent of SQL’s `LIMIT` and `OFFSET` clauses.
For example, this returns the first 5 objects (`LIMIT 5`):
```
>>> Entry.objects.all()[:5]

```

This returns the sixth through tenth objects (`OFFSET 5 LIMIT 5`):
```
>>> Entry.objects.all()[5:10]

```

Negative indexing (i.e. `Entry.objects.all()[-1]`) is not supported.
Generally, slicing a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") returns a new [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") – it doesn’t evaluate the query. An exception is if you use the “step” parameter of Python slice syntax. For example, this would actually execute the query in order to return a list of every _second_ object of the first 10:
```
>>> Entry.objects.all()[:10:2]

```

Further filtering or ordering of a sliced queryset is prohibited due to the ambiguous nature of how that might work.
To retrieve a _single_ object rather than a list (e.g. `SELECT foo FROM bar LIMIT 1`), use an index instead of a slice. For example, this returns the first `Entry` in the database, after ordering entries alphabetically by headline:
```
>>> Entry.objects.order_by("headline")[0]

```

This is roughly equivalent to:
```
>>> Entry.objects.order_by("headline")[0:1].get()

```

Note, however, that the first of these will raise `IndexError` while the second will raise `DoesNotExist` if no objects match the given criteria. See [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") for more details.
### Field lookups[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups "Link to this heading")
Field lookups are how you specify the meat of an SQL `WHERE` clause. They’re specified as keyword arguments to the [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") methods [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"), [`exclude()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") and [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get").
Basic lookups keyword arguments take the form `field__lookuptype=value`. (That’s a double-underscore). For example:
```
>>> Entry.objects.filter(pub_date__lte="2006-01-01")

```

translates (roughly) into the following SQL:
```
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';

```

How this is possible
Python has the ability to define functions that accept arbitrary name-value arguments whose names and values are evaluated at runtime. For more information, see
The field specified in a lookup has to be the name of a model field. There’s one exception though, in case of a [`ForeignKey`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") you can specify the field name suffixed with `_id`. In this case, the value parameter is expected to contain the raw value of the foreign model’s primary key. For example:
```
>>> Entry.objects.filter(blog_id=4)

```

If you pass an invalid keyword argument, a lookup function will raise `TypeError`.
The database API supports about two dozen lookup types; a complete reference can be found in the [field lookup reference](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#field-lookups). To give you a taste of what’s available, here’s some of the more common lookups you’ll probably use:

[`exact`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-exact)

An “exact” match. For example:
```
>>> Entry.objects.get(headline__exact="Cat bites dog")

```

Would generate SQL along these lines:
```
SELECT ... WHERE headline = 'Cat bites dog';

```

If you don’t provide a lookup type – that is, if your keyword argument doesn’t contain a double underscore – the lookup type is assumed to be `exact`.
For example, the following two statements are equivalent:
```
>>> Blog.objects.get(id__exact=14)  # Explicit form
>>> Blog.objects.get(id=14)  # __exact is implied

```

This is for convenience, because `exact` lookups are the common case.

[`iexact`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-iexact)

A case-insensitive match. So, the query:
```
>>> Blog.objects.get(name__iexact="beatles blog")

```

Would match a `Blog` titled `"Beatles Blog"`, `"beatles blog"`, or even `"BeAtlES blOG"`.

[`contains`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-contains)

Case-sensitive containment test. For example:
```
Entry.objects.get(headline__contains="Lennon")

```

Roughly translates to this SQL:
```
SELECT ... WHERE headline LIKE '%Lennon%';

```

Note this will match the headline `'Today Lennon honored'` but not `'today lennon honored'`.
There’s also a case-insensitive version, [`icontains`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-icontains).

[`startswith`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-startswith), [`endswith`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-endswith)

Starts-with and ends-with search, respectively. There are also case-insensitive versions called [`istartswith`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-istartswith) and [`iendswith`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-iendswith).
Again, this only scratches the surface. A complete reference can be found in the [field lookup reference](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#field-lookups).
### Lookups that span relationships[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#lookups-that-span-relationships "Link to this heading")
Django offers a powerful and intuitive way to “follow” relationships in lookups, taking care of the SQL `JOIN`s for you automatically, behind the scenes. To span a relationship, use the field name of related fields across models, separated by double underscores, until you get to the field you want.
This example retrieves all `Entry` objects with a `Blog` whose `name` is `'Beatles Blog'`:
```
>>> Entry.objects.filter(blog__name="Beatles Blog")

```

This spanning can be as deep as you’d like.
It works backwards, too. While it [`can be customized`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name"), by default you refer to a “reverse” relationship in a lookup using the lowercase name of the model.
This example retrieves all `Blog` objects which have at least one `Entry` whose `headline` contains `'Lennon'`:
```
>>> Blog.objects.filter(entry__headline__contains="Lennon")

```

If you are filtering across multiple relationships and one of the intermediate models doesn’t have a value that meets the filter condition, Django will treat it as if there is an empty (all values are `NULL`), but valid, object there. All this means is that no error will be raised. For example, in this filter:
```
Blog.objects.filter(entry__authors__name="Lennon")

```

(if there was a related `Author` model), if there was no `author` associated with an entry, it would be treated as if there was also no `name` attached, rather than raising an error because of the missing `author`. Usually this is exactly what you want to have happen. The only case where it might be confusing is if you are using [`isnull`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-isnull). Thus:
```
Blog.objects.filter(entry__authors__name__isnull=True)

```

will return `Blog` objects that have an empty `name` on the `author` and also those which have an empty `author` on the `entry`. If you don’t want those latter objects, you could write:
```
Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)

```

#### Spanning multi-valued relationships[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#spanning-multi-valued-relationships "Link to this heading")
When spanning a [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") or a reverse [`ForeignKey`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") (such as from `Blog` to `Entry`), filtering on multiple attributes raises the question of whether to require each attribute to coincide in the same related object. We might seek blogs that have an entry from 2008 with _“Lennon”_ in its headline, or we might seek blogs that merely have any entry from 2008 as well as some newer or older entry with _“Lennon”_ in its headline.
To select all blogs containing at least one entry from 2008 having _“Lennon”_ in its headline (the same entry satisfying both conditions), we would write:
```
Blog.objects.filter(entry__headline__contains="Lennon", entry__pub_date__year=2008)

```

Otherwise, to perform a more permissive query selecting any blogs with merely _some_ entry with _“Lennon”_ in its headline and _some_ entry from 2008, we would write:
```
Blog.objects.filter(entry__headline__contains="Lennon").filter(
    entry__pub_date__year=2008
)

```

Suppose there is only one blog that has both entries containing _“Lennon”_ and entries from 2008, but that none of the entries from 2008 contained _“Lennon”_. The first query would not return any blogs, but the second query would return that one blog. (This is because the entries selected by the second filter may or may not be the same as the entries in the first filter. We are filtering the `Blog` items with each filter statement, not the `Entry` items.) In short, if each condition needs to match the same related object, then each should be contained in a single [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") call.
Note
As the second (more permissive) query chains multiple filters, it performs multiple joins to the primary model, potentially yielding duplicates.
```
>>> from datetime import date
>>> beatles = Blog.objects.create(name="Beatles Blog")
>>> pop = Blog.objects.create(name="Pop Music Blog")
>>> Entry.objects.create(
...     blog=beatles,
...     headline="New Lennon Biography",
...     pub_date=date(2008, 6, 1),
... )
<Entry: New Lennon Biography>
>>> Entry.objects.create(
...     blog=beatles,
...     headline="New Lennon Biography in Paperback",
...     pub_date=date(2009, 6, 1),
... )
<Entry: New Lennon Biography in Paperback>
>>> Entry.objects.create(
...     blog=pop,
...     headline="Best Albums of 2008",
...     pub_date=date(2008, 12, 15),
... )
<Entry: Best Albums of 2008>
>>> Entry.objects.create(
...     blog=pop,
...     headline="Lennon Would Have Loved Hip Hop",
...     pub_date=date(2020, 4, 1),
... )
<Entry: Lennon Would Have Loved Hip Hop>
>>> Blog.objects.filter(
...     entry__headline__contains="Lennon",
...     entry__pub_date__year=2008,
... )
<QuerySet [<Blog: Beatles Blog>]>
>>> Blog.objects.filter(
...     entry__headline__contains="Lennon",
... ).filter(
...     entry__pub_date__year=2008,
... )
<QuerySet [<Blog: Beatles Blog>, <Blog: Beatles Blog>, <Blog: Pop Music Blog]>

```

Note
The behavior of [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") for queries that span multi-value relationships, as described above, is not implemented equivalently for [`exclude()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude"). Instead, the conditions in a single [`exclude()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude") call will not necessarily refer to the same item.
For example, the following query would exclude blogs that contain _both_ entries with _“Lennon”_ in the headline _and_ entries published in 2008:
```
Blog.objects.exclude(
    entry__headline__contains="Lennon",
    entry__pub_date__year=2008,
)

```

However, unlike the behavior when using [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"), this will not limit blogs based on entries that satisfy both conditions. In order to do that, i.e. to select all blogs that do not contain entries published with _“Lennon”_ that were published in 2008, you need to make two queries:
```
Blog.objects.exclude(
    entry__in=Entry.objects.filter(
        headline__contains="Lennon",
        pub_date__year=2008,
    ),
)

```

### Filters can reference fields on the model[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#filters-can-reference-fields-on-the-model "Link to this heading")
In the examples given so far, we have constructed filters that compare the value of a model field with a constant. But what if you want to compare the value of a model field with another field on the same model?
Django provides [`F expressions`](https://docs.djangoproject.com/en/5.0/ref/models/expressions/#django.db.models.F "django.db.models.F") to allow such comparisons. Instances of `F()` act as a reference to a model field within a query. These references can then be used in query filters to compare the values of two different fields on the same model instance.
For example, to find a list of all blog entries that have had more comments than pingbacks, we construct an `F()` object to reference the pingback count, and use that `F()` object in the query:
```
>>> from django.db.models import F
>>> Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks"))

```

Django supports the use of addition, subtraction, multiplication, division, modulo, and power arithmetic with `F()` objects, both with constants and with other `F()` objects. To find all the blog entries with more than _twice_ as many comments as pingbacks, we modify the query:
```
>>> Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks") * 2)

```

To find all the entries where the rating of the entry is less than the sum of the pingback count and comment count, we would issue the query:
```
>>> Entry.objects.filter(rating__lt=F("number_of_comments") + F("number_of_pingbacks"))

```

You can also use the double underscore notation to span relationships in an `F()` object. An `F()` object with a double underscore will introduce any joins needed to access the related object. For example, to retrieve all the entries where the author’s name is the same as the blog name, we could issue the query:
```
>>> Entry.objects.filter(authors__name=F("blog__name"))

```

For date and date/time fields, you can add or subtract a
```
>>> from datetime import timedelta
>>> Entry.objects.filter(mod_date__gt=F("pub_date") + timedelta(days=3))

```

The `F()` objects support bitwise operations by `.bitand()`, `.bitor()`, `.bitxor()`, `.bitrightshift()`, and `.bitleftshift()`. For example:
```
>>> F("somefield").bitand(16)

```

Oracle
Oracle doesn’t support bitwise XOR operation.
### Expressions can reference transforms[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#expressions-can-reference-transforms "Link to this heading")
Django supports using transforms in expressions.
For example, to find all `Entry` objects published in the same year as they were last modified:
```
>>> from django.db.models import F
>>> Entry.objects.filter(pub_date__year=F("mod_date__year"))

```

To find the earliest year an entry was published, we can issue the query:
```
>>> from django.db.models import Min
>>> Entry.objects.aggregate(first_published_year=Min("pub_date__year"))

```

This example finds the value of the highest rated entry and the total number of comments on all entries for each year:
```
>>> from django.db.models import OuterRef, Subquery, Sum
>>> Entry.objects.values("pub_date__year").annotate(
...     top_rating=Subquery(
...         Entry.objects.filter(
...             pub_date__year=OuterRef("pub_date__year"),
...         )
...         .order_by("-rating")
...         .values("rating")[:1]
...     ),
...     total_comments=Sum("number_of_comments"),
... )

```

### The `pk` lookup shortcut[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#the-pk-lookup-shortcut "Link to this heading")
For convenience, Django provides a `pk` lookup shortcut, which stands for “primary key”.
In the example `Blog` model, the primary key is the `id` field, so these three statements are equivalent:
```
>>> Blog.objects.get(id__exact=14)  # Explicit form
>>> Blog.objects.get(id=14)  # __exact is implied
>>> Blog.objects.get(pk=14)  # pk implies id__exact

```

The use of `pk` isn’t limited to `__exact` queries – any query term can be combined with `pk` to perform a query on the primary key of a model:
```
# Get blogs entries with id 1, 4 and 7
>>> Blog.objects.filter(pk__in=[1, 4, 7])

# Get all blog entries with id > 14
>>> Blog.objects.filter(pk__gt=14)

```

`pk` lookups also work across joins. For example, these three statements are equivalent:
```
>>> Entry.objects.filter(blog__id__exact=3)  # Explicit form
>>> Entry.objects.filter(blog__id=3)  # __exact is implied
>>> Entry.objects.filter(blog__pk=3)  # __pk implies __id__exact

```

### Escaping percent signs and underscores in `LIKE` statements[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#escaping-percent-signs-and-underscores-in-like-statements "Link to this heading")
The field lookups that equate to `LIKE` SQL statements (`iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith` and `iendswith`) will automatically escape the two special characters used in `LIKE` statements – the percent sign and the underscore. (In a `LIKE` statement, the percent sign signifies a multiple-character wildcard and the underscore signifies a single-character wildcard.)
This means things should work intuitively, so the abstraction doesn’t leak. For example, to retrieve all the entries that contain a percent sign, use the percent sign as any other character:
```
>>> Entry.objects.filter(headline__contains="%")

```

Django takes care of the quoting for you; the resulting SQL will look something like this:
```
SELECT ... WHERE headline LIKE '%\%%';

```

Same goes for underscores. Both percentage signs and underscores are handled for you transparently.
### Caching and `QuerySet`s[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#caching-and-querysets "Link to this heading")
Each [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") contains a cache to minimize database access. Understanding how it works will allow you to write the most efficient code.
In a newly created [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet"), the cache is empty. The first time a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is evaluated – and, hence, a database query happens – Django saves the query results in the [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet")’s cache and returns the results that have been explicitly requested (e.g., the next element, if the [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") is being iterated over). Subsequent evaluations of the [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") reuse the cached results.
Keep this caching behavior in mind, because it may bite you if you don’t use your [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet")s correctly. For example, the following will create two [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet")s, evaluate them, and throw them away:
```
>>> print([e.headline for e in Entry.objects.all()])
>>> print([e.pub_date for e in Entry.objects.all()])

```

That means the same database query will be executed twice, effectively doubling your database load. Also, there’s a possibility the two lists may not include the same database records, because an `Entry` may have been added or deleted in the split second between the two requests.
To avoid this problem, save the [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") and reuse it:
```
>>> queryset = Entry.objects.all()
>>> print([p.headline for p in queryset])  # Evaluate the query set.
>>> print([p.pub_date for p in queryset])  # Reuse the cache from the evaluation.

```

#### When `QuerySet`s are not cached[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#when-querysets-are-not-cached "Link to this heading")
Querysets do not always cache their results. When evaluating only _part_ of the queryset, the cache is checked, but if it is not populated then the items returned by the subsequent query are not cached. Specifically, this means that [limiting the queryset](https://docs.djangoproject.com/en/5.0/topics/db/queries/#limiting-querysets) using an array slice or an index will not populate the cache.
For example, repeatedly getting a certain index in a queryset object will query the database each time:
```
>>> queryset = Entry.objects.all()
>>> print(queryset[5])  # Queries the database
>>> print(queryset[5])  # Queries the database again

```

However, if the entire queryset has already been evaluated, the cache will be checked instead:
```
>>> queryset = Entry.objects.all()
>>> [entry for entry in queryset]  # Queries the database
>>> print(queryset[5])  # Uses cache
>>> print(queryset[5])  # Uses cache

```

Here are some examples of other actions that will result in the entire queryset being evaluated and therefore populate the cache:
```
>>> [entry for entry in queryset]
>>> bool(queryset)
>>> entry in queryset
>>> list(queryset)

```

Note
Simply printing the queryset will not populate the cache. This is because the call to `__repr__()` only returns a slice of the entire queryset.
