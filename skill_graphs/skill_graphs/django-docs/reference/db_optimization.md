This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/db/optimization/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/db/optimization/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/db/optimization/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/db/optimization/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/db/optimization/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/db/optimization/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/db/optimization/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/db/optimization/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/db/optimization/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/db/optimization/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/db/optimization/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/db/optimization/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/db/optimization/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/db/optimization/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/db/optimization/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/db/optimization/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/db/optimization/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/db/optimization/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/db/optimization/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/db/optimization/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/db/optimization/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/db/optimization/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/db/optimization/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/db/optimization/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/db/optimization/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/db/optimization/)


  * [](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#top)


# Database access optimization[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#database-access-optimization "Link to this heading")
Django’s database layer provides various ways to help developers get the most out of their databases. This document gathers together links to the relevant documentation, and adds various tips, organized under a number of headings that outline the steps to take when attempting to optimize your database usage.
## Profile first[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#profile-first "Link to this heading")
As general programming practice, this goes without saying. Find out [what queries you are doing and what they are costing you](https://docs.djangoproject.com/en/5.0/faq/models/#faq-see-raw-sql-queries). Use [`QuerySet.explain()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.explain "django.db.models.query.QuerySet.explain") to understand how specific `QuerySet`s are executed by your database. You may also want to use an external project like
Remember that you may be optimizing for speed or memory or both, depending on your requirements. Sometimes optimizing for one will be detrimental to the other, but sometimes they will help each other. Also, work that is done by the database process might not have the same cost (to you) as the same amount of work done in your Python process. It is up to you to decide what your priorities are, where the balance must lie, and profile all of these as required since this will depend on your application and server.
With everything that follows, remember to profile after every change to ensure that the change is a benefit, and a big enough benefit given the decrease in readability of your code. **All** of the suggestions below come with the caveat that in your circumstances the general principle might not apply, or might even be reversed.
## Use standard DB optimization techniques[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-standard-db-optimization-techniques "Link to this heading")
…including:
  * _after_ you have determined from profiling what indexes should be added. Use [`Meta.indexes`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.indexes "django.db.models.Options.indexes") or [`Field.db_index`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.db_index "django.db.models.Field.db_index") to add these from Django. Consider adding indexes to fields that you frequently query using [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"), [`exclude()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude "django.db.models.query.QuerySet.exclude"), [`order_by()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.order_by "django.db.models.query.QuerySet.order_by"), etc. as indexes may help to speed up lookups. Note that determining the best indexes is a complex database-dependent topic that will depend on your particular application. The overhead of maintaining an index may outweigh any gains in query speed.


  * Appropriate use of field types.


We will assume you have done the things listed above. The rest of this document focuses on how to use Django in such a way that you are not doing unnecessary work. This document also does not address other optimization techniques that apply to all expensive operations, such as [general purpose caching](https://docs.djangoproject.com/en/5.0/topics/cache/).
## Understand `QuerySet`s[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#understand-querysets "Link to this heading")
Understanding [QuerySets](https://docs.djangoproject.com/en/5.0/ref/models/querysets/) is vital to getting good performance with simple code. In particular:
### Understand `QuerySet` evaluation[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#understand-queryset-evaluation "Link to this heading")
To avoid performance problems, it is important to understand:
  * that [QuerySets are lazy](https://docs.djangoproject.com/en/5.0/topics/db/queries/#querysets-are-lazy).
  * when [they are evaluated](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#when-querysets-are-evaluated).
  * how [the data is held in memory](https://docs.djangoproject.com/en/5.0/topics/db/queries/#caching-and-querysets).


### Understand cached attributes[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#understand-cached-attributes "Link to this heading")
As well as caching of the whole `QuerySet`, there is caching of the result of attributes on ORM objects. In general, attributes that are not callable will be cached. For example, assuming the [example blog models](https://docs.djangoproject.com/en/5.0/topics/db/queries/#queryset-model-example):
```
>>> entry = Entry.objects.get(id=1)
>>> entry.blog  # Blog object is retrieved at this point
>>> entry.blog  # cached version, no DB access

```

But in general, callable attributes cause DB lookups every time:
```
>>> entry = Entry.objects.get(id=1)
>>> entry.authors.all()  # query performed
>>> entry.authors.all()  # query performed again

```

Be careful when reading template code - the template system does not allow use of parentheses, but will call callables automatically, hiding the above distinction.
Be careful with your own custom properties - it is up to you to implement caching when required, for example using the [`cached_property`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.cached_property "django.utils.functional.cached_property") decorator.
### Use the `with` template tag[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-the-with-template-tag "Link to this heading")
To make use of the caching behavior of `QuerySet`, you may need to use the [`with`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-with) template tag.
### Use `iterator()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-iterator "Link to this heading")
When you have a lot of objects, the caching behavior of the `QuerySet` can cause a large amount of memory to be used. In this case, [`iterator()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.iterator "django.db.models.query.QuerySet.iterator") may help.
### Use `explain()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-explain "Link to this heading")
[`QuerySet.explain()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.explain "django.db.models.query.QuerySet.explain") gives you detailed information about how the database executes a query, including indexes and joins that are used. These details may help you find queries that could be rewritten more efficiently, or identify indexes that could be added to improve performance.
## Do database work in the database rather than in Python[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#do-database-work-in-the-database-rather-than-in-python "Link to this heading")
For instance:
  * At the most basic level, use [filter and exclude](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#queryset-api) to do filtering in the database.
  * Use [`F expressions`](https://docs.djangoproject.com/en/5.0/ref/models/expressions/#django.db.models.F "django.db.models.F") to filter based on other fields within the same model.
  * Use [annotate to do aggregation in the database](https://docs.djangoproject.com/en/5.0/topics/db/aggregation/).


If these aren’t enough to generate the SQL you need:
### Use `RawSQL`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-rawsql "Link to this heading")
A less portable but more powerful method is the [`RawSQL`](https://docs.djangoproject.com/en/5.0/ref/models/expressions/#django.db.models.expressions.RawSQL "django.db.models.expressions.RawSQL") expression, which allows some SQL to be explicitly added to the query. If that still isn’t powerful enough:
### Use raw SQL[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-raw-sql "Link to this heading")
Write your own [custom SQL to retrieve data or populate models](https://docs.djangoproject.com/en/5.0/topics/db/sql/). Use `django.db.connection.queries` to find out what Django is writing for you and start from there.
## Retrieve individual objects using a unique, indexed column[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#retrieve-individual-objects-using-a-unique-indexed-column "Link to this heading")
There are two reasons to use a column with [`unique`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.unique "django.db.models.Field.unique") or [`db_index`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.db_index "django.db.models.Field.db_index") when using [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") to retrieve individual objects. First, the query will be quicker because of the underlying database index. Also, the query could run much slower if multiple objects match the lookup; having a unique constraint on the column guarantees this will never happen.
So using the [example blog models](https://docs.djangoproject.com/en/5.0/topics/db/queries/#queryset-model-example):
```
>>> entry = Entry.objects.get(id=10)

```

will be quicker than:
```
>>> entry = Entry.objects.get(headline="News Item Title")

```

because `id` is indexed by the database and is guaranteed to be unique.
Doing the following is potentially quite slow:
```
>>> entry = Entry.objects.get(headline__startswith="News")

```

First of all, `headline` is not indexed, which will make the underlying database fetch slower.
Second, the lookup doesn’t guarantee that only one object will be returned. If the query matches more than one object, it will retrieve and transfer all of them from the database. This penalty could be substantial if hundreds or thousands of records are returned. The penalty will be compounded if the database lives on a separate server, where network overhead and latency also play a factor.
## Retrieve everything at once if you know you will need it[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#retrieve-everything-at-once-if-you-know-you-will-need-it "Link to this heading")
Hitting the database multiple times for different parts of a single ‘set’ of data that you will need all parts of is, in general, less efficient than retrieving it all in one query. This is particularly important if you have a query that is executed in a loop, and could therefore end up doing many database queries, when only one was needed. So:
### Use `QuerySet.select_related()` and `prefetch_related()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-select-related-and-prefetch-related "Link to this heading")
Understand [`select_related()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.select_related "django.db.models.query.QuerySet.select_related") and [`prefetch_related()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.prefetch_related "django.db.models.query.QuerySet.prefetch_related") thoroughly, and use them:
  * in [managers and default managers](https://docs.djangoproject.com/en/5.0/topics/db/managers/) where appropriate. Be aware when your manager is and is not used; sometimes this is tricky so don’t make assumptions.
  * in view code or other layers, possibly making use of [`prefetch_related_objects()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.prefetch_related_objects "django.db.models.prefetch_related_objects") where needed.


## Don’t retrieve things you don’t need[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#don-t-retrieve-things-you-don-t-need "Link to this heading")
### Use `QuerySet.values()` and `values_list()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-values-and-values-list "Link to this heading")
When you only want a `dict` or `list` of values, and don’t need ORM model objects, make appropriate usage of [`values()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.values "django.db.models.query.QuerySet.values"). These can be useful for replacing model objects in template code - as long as the dicts you supply have the same attributes as those used in the template, you are fine.
### Use `QuerySet.defer()` and `only()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-defer-and-only "Link to this heading")
Use [`defer()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.defer "django.db.models.query.QuerySet.defer") and [`only()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.only "django.db.models.query.QuerySet.only") if there are database columns you know that you won’t need (or won’t need in most cases) to avoid loading them. Note that if you _do_ use them, the ORM will have to go and get them in a separate query, making this a pessimization if you use it inappropriately.
Don’t be too aggressive in deferring fields without profiling as the database has to read most of the non-text, non-`VARCHAR` data from the disk for a single row in the results, even if it ends up only using a few columns. The `defer()` and `only()` methods are most useful when you can avoid loading a lot of text data or for fields that might take a lot of processing to convert back to Python. As always, profile first, then optimize.
### Use `QuerySet.contains(obj)`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-contains-obj "Link to this heading")
…if you only want to find out if `obj` is in the queryset, rather than `if obj in queryset`.
### Use `QuerySet.count()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-count "Link to this heading")
…if you only want the count, rather than doing `len(queryset)`.
### Use `QuerySet.exists()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-exists "Link to this heading")
…if you only want to find out if at least one result exists, rather than `if queryset`.
But:
### Don’t overuse `contains()`, `count()`, and `exists()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#don-t-overuse-contains-count-and-exists "Link to this heading")
If you are going to need other data from the QuerySet, evaluate it immediately.
For example, assuming a `Group` model that has a many-to-many relation to `User`, the following code is optimal:
```
members = group.members.all()

if display_group_members:
    if members:
        if current_user in members:
            print("You and", len(members) - 1, "other users are members of this group.")
        else:
            print("There are", len(members), "members in this group.")

        for member in members:
            print(member.username)
    else:
        print("There are no members in this group.")

```

It is optimal because:
  1. Since QuerySets are lazy, this does no database queries if `display_group_members` is `False`.
  2. Storing `group.members.all()` in the `members` variable allows its result cache to be reused.
  3. The line `if members:` causes `QuerySet.__bool__()` to be called, which causes the `group.members.all()` query to be run on the database. If there aren’t any results, it will return `False`, otherwise `True`.
  4. The line `if current_user in members:` checks if the user is in the result cache, so no additional database queries are issued.
  5. The use of `len(members)` calls `QuerySet.__len__()`, reusing the result cache, so again, no database queries are issued.
  6. The `for member` loop iterates over the result cache.


In total, this code does either one or zero database queries. The only deliberate optimization performed is using the `members` variable. Using `QuerySet.exists()` for the `if`, `QuerySet.contains()` for the `in`, or `QuerySet.count()` for the count would each cause additional queries.
### Use `QuerySet.update()` and `delete()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-update-and-delete "Link to this heading")
Rather than retrieve a load of objects, set some values, and save them individual, use a bulk SQL UPDATE statement, via [QuerySet.update()](https://docs.djangoproject.com/en/5.0/topics/db/queries/#topics-db-queries-update). Similarly, do [bulk deletes](https://docs.djangoproject.com/en/5.0/topics/db/queries/#topics-db-queries-delete) where possible.
Note, however, that these bulk update methods cannot call the `save()` or `delete()` methods of individual instances, which means that any custom behavior you have added for these methods will not be executed, including anything driven from the normal database object [signals](https://docs.djangoproject.com/en/5.0/ref/signals/).
### Use foreign key values directly[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-foreign-key-values-directly "Link to this heading")
If you only need a foreign key value, use the foreign key value that is already on the object you’ve got, rather than getting the whole related object and taking its primary key. i.e. do:
```
entry.blog_id

```

instead of:
```
entry.blog.id

```

### Don’t order results if you don’t care[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#don-t-order-results-if-you-don-t-care "Link to this heading")
Ordering is not free; each field to order by is an operation the database must perform. If a model has a default ordering ([`Meta.ordering`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.ordering "django.db.models.Options.ordering")) and you don’t need it, remove it on a `QuerySet` by calling [`order_by()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.order_by "django.db.models.query.QuerySet.order_by") with no parameters.
Adding an index to your database may help to improve ordering performance.
## Use bulk methods[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-bulk-methods "Link to this heading")
Use bulk methods to reduce the number of SQL statements.
### Create in bulk[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#create-in-bulk "Link to this heading")
When creating objects, where possible, use the [`bulk_create()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create "django.db.models.query.QuerySet.bulk_create") method to reduce the number of SQL queries. For example:
```
Entry.objects.bulk_create(
    [
        Entry(headline="This is a test"),
        Entry(headline="This is only a test"),
    ]
)

```

…is preferable to:
```
Entry.objects.create(headline="This is a test")
Entry.objects.create(headline="This is only a test")

```

Note that there are a number of [`caveats to this method`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create "django.db.models.query.QuerySet.bulk_create"), so make sure it’s appropriate for your use case.
### Update in bulk[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#update-in-bulk "Link to this heading")
When updating objects, where possible, use the [`bulk_update()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_update "django.db.models.query.QuerySet.bulk_update") method to reduce the number of SQL queries. Given a list or queryset of objects:
```
entries = Entry.objects.bulk_create(
    [
        Entry(headline="This is a test"),
        Entry(headline="This is only a test"),
    ]
)

```

The following example:
```
entries[0].headline = "This is not a test"
entries[1].headline = "This is no longer a test"
Entry.objects.bulk_update(entries, ["headline"])

```

…is preferable to:
```
entries[0].headline = "This is not a test"
entries[0].save()
entries[1].headline = "This is no longer a test"
entries[1].save()

```

Note that there are a number of [`caveats to this method`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_update "django.db.models.query.QuerySet.bulk_update"), so make sure it’s appropriate for your use case.
### Insert in bulk[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#insert-in-bulk "Link to this heading")
When inserting objects into [`ManyToManyFields`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"), use [`add()`](https://docs.djangoproject.com/en/5.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.add "django.db.models.fields.related.RelatedManager.add") with multiple objects to reduce the number of SQL queries. For example:
```
my_band.members.add(me, my_friend)

```

…is preferable to:
```
my_band.members.add(me)
my_band.members.add(my_friend)

```

…where `Bands` and `Artists` have a many-to-many relationship.
When inserting different pairs of objects into [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") or when the custom [`through`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField.through "django.db.models.ManyToManyField.through") table is defined, use [`bulk_create()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create "django.db.models.query.QuerySet.bulk_create") method to reduce the number of SQL queries. For example:
```
PizzaToppingRelationship = Pizza.toppings.through
PizzaToppingRelationship.objects.bulk_create(
    [
        PizzaToppingRelationship(pizza=my_pizza, topping=pepperoni),
        PizzaToppingRelationship(pizza=your_pizza, topping=pepperoni),
        PizzaToppingRelationship(pizza=your_pizza, topping=mushroom),
    ],
    ignore_conflicts=True,
)

```

…is preferable to:
```
my_pizza.toppings.add(pepperoni)
your_pizza.toppings.add(pepperoni, mushroom)

```

…where `Pizza` and `Topping` have a many-to-many relationship. Note that there are a number of [`caveats to this method`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create "django.db.models.query.QuerySet.bulk_create"), so make sure it’s appropriate for your use case.
### Remove in bulk[¶](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#remove-in-bulk "Link to this heading")
When removing objects from [`ManyToManyFields`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"), use [`remove()`](https://docs.djangoproject.com/en/5.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.remove "django.db.models.fields.related.RelatedManager.remove") with multiple objects to reduce the number of SQL queries. For example:
```
my_band.members.remove(me, my_friend)

```

…is preferable to:
```
my_band.members.remove(me)
my_band.members.remove(my_friend)

```

…where `Bands` and `Artists` have a many-to-many relationship.
When removing different pairs of objects from [`ManyToManyFields`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"), use [`delete()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") on a [`Q`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q") expression with multiple [`through`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField.through "django.db.models.ManyToManyField.through") model instances to reduce the number of SQL queries. For example:
```
from django.db.models import Q

PizzaToppingRelationship = Pizza.toppings.through
PizzaToppingRelationship.objects.filter(
    Q(pizza=my_pizza, topping=pepperoni)
    | Q(pizza=your_pizza, topping=pepperoni)
    | Q(pizza=your_pizza, topping=mushroom)
).delete()

```

…is preferable to:
```
my_pizza.toppings.remove(pepperoni)
your_pizza.toppings.remove(pepperoni, mushroom)

```

…where `Pizza` and `Topping` have a many-to-many relationship.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/db/tablespaces/)
[Database instrumentation ](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/)
[](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Krzysztof Szularz donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Database access optimization](https://docs.djangoproject.com/en/5.0/topics/db/optimization/)
    * [Profile first](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#profile-first)
    * [Use standard DB optimization techniques](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-standard-db-optimization-techniques)
    * [Understand `QuerySet`s](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#understand-querysets)
      * [Understand `QuerySet` evaluation](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#understand-queryset-evaluation)
      * [Understand cached attributes](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#understand-cached-attributes)
      * [Use the `with` template tag](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-the-with-template-tag)
      * [Use `iterator()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-iterator)
      * [Use `explain()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-explain)
    * [Do database work in the database rather than in Python](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#do-database-work-in-the-database-rather-than-in-python)
      * [Use `RawSQL`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-rawsql)
      * [Use raw SQL](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-raw-sql)
    * [Retrieve individual objects using a unique, indexed column](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#retrieve-individual-objects-using-a-unique-indexed-column)
    * [Retrieve everything at once if you know you will need it](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#retrieve-everything-at-once-if-you-know-you-will-need-it)
      * [Use `QuerySet.select_related()` and `prefetch_related()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-select-related-and-prefetch-related)
    * [Don’t retrieve things you don’t need](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#don-t-retrieve-things-you-don-t-need)
      * [Use `QuerySet.values()` and `values_list()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-values-and-values-list)
      * [Use `QuerySet.defer()` and `only()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-defer-and-only)
      * [Use `QuerySet.contains(obj)`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-contains-obj)
      * [Use `QuerySet.count()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-count)
      * [Use `QuerySet.exists()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-exists)
      * [Don’t overuse `contains()`, `count()`, and `exists()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#don-t-overuse-contains-count-and-exists)
      * [Use `QuerySet.update()` and `delete()`](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-queryset-update-and-delete)
      * [Use foreign key values directly](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-foreign-key-values-directly)
      * [Don’t order results if you don’t care](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#don-t-order-results-if-you-don-t-care)
    * [Use bulk methods](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#use-bulk-methods)
      * [Create in bulk](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#create-in-bulk)
      * [Update in bulk](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#update-in-bulk)
      * [Insert in bulk](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#insert-in-bulk)
      * [Remove in bulk](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#remove-in-bulk)


### Browse
  * Prev: [Tablespaces](https://docs.djangoproject.com/en/5.0/topics/db/tablespaces/)
  * Next: [Database instrumentation](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Models and databases](https://docs.djangoproject.com/en/5.0/topics/db/)
        * Database access optimization


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
