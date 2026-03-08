## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Doniyor Jurabayev donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Making queries](https://docs.djangoproject.com/en/6.0/topics/db/queries/)
    * [Creating objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#creating-objects)
    * [Saving changes to objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#saving-changes-to-objects)
      * [Saving `ForeignKey` and `ManyToManyField` fields](https://docs.djangoproject.com/en/6.0/topics/db/queries/#saving-foreignkey-and-manytomanyfield-fields)
    * [Retrieving objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#retrieving-objects)
      * [Retrieving all objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#retrieving-all-objects)
      * [Retrieving specific objects with filters](https://docs.djangoproject.com/en/6.0/topics/db/queries/#retrieving-specific-objects-with-filters)
        * [Chaining filters](https://docs.djangoproject.com/en/6.0/topics/db/queries/#chaining-filters)
        * [Filtered `QuerySet`s are unique](https://docs.djangoproject.com/en/6.0/topics/db/queries/#filtered-querysets-are-unique)
        * [`QuerySet`s are lazy](https://docs.djangoproject.com/en/6.0/topics/db/queries/#querysets-are-lazy)
      * [Retrieving a single object with `get()`](https://docs.djangoproject.com/en/6.0/topics/db/queries/#retrieving-a-single-object-with-get)
      * [Other `QuerySet` methods](https://docs.djangoproject.com/en/6.0/topics/db/queries/#other-queryset-methods)
      * [Limiting `QuerySet`s](https://docs.djangoproject.com/en/6.0/topics/db/queries/#limiting-querysets)
      * [Field lookups](https://docs.djangoproject.com/en/6.0/topics/db/queries/#field-lookups)
      * [Lookups that span relationships](https://docs.djangoproject.com/en/6.0/topics/db/queries/#lookups-that-span-relationships)
        * [Spanning multi-valued relationships](https://docs.djangoproject.com/en/6.0/topics/db/queries/#spanning-multi-valued-relationships)
      * [Filters can reference fields on the model](https://docs.djangoproject.com/en/6.0/topics/db/queries/#filters-can-reference-fields-on-the-model)
      * [Expressions can reference transforms](https://docs.djangoproject.com/en/6.0/topics/db/queries/#expressions-can-reference-transforms)
      * [The `pk` lookup shortcut](https://docs.djangoproject.com/en/6.0/topics/db/queries/#the-pk-lookup-shortcut)
      * [Escaping percent signs and underscores in `LIKE` statements](https://docs.djangoproject.com/en/6.0/topics/db/queries/#escaping-percent-signs-and-underscores-in-like-statements)
      * [Caching and `QuerySet`s](https://docs.djangoproject.com/en/6.0/topics/db/queries/#caching-and-querysets)
        * [When `QuerySet`s are not cached](https://docs.djangoproject.com/en/6.0/topics/db/queries/#when-querysets-are-not-cached)
    * [Asynchronous queries](https://docs.djangoproject.com/en/6.0/topics/db/queries/#asynchronous-queries)
      * [Query iteration](https://docs.djangoproject.com/en/6.0/topics/db/queries/#query-iteration)
      * [`QuerySet` and manager methods](https://docs.djangoproject.com/en/6.0/topics/db/queries/#queryset-and-manager-methods)
      * [Transactions](https://docs.djangoproject.com/en/6.0/topics/db/queries/#transactions)
    * [Querying `JSONField`](https://docs.djangoproject.com/en/6.0/topics/db/queries/#querying-jsonfield)
      * [Storing and querying for `None`](https://docs.djangoproject.com/en/6.0/topics/db/queries/#storing-and-querying-for-none)
      * [Key, index, and path transforms](https://docs.djangoproject.com/en/6.0/topics/db/queries/#key-index-and-path-transforms)
        * [`KT()` expressions](https://docs.djangoproject.com/en/6.0/topics/db/queries/#module-django.db.models.fields.json)
      * [Containment and key lookups](https://docs.djangoproject.com/en/6.0/topics/db/queries/#containment-and-key-lookups)
        * [`contains`](https://docs.djangoproject.com/en/6.0/topics/db/queries/#contains)
        * [`contained_by`](https://docs.djangoproject.com/en/6.0/topics/db/queries/#contained-by)
        * [`has_key`](https://docs.djangoproject.com/en/6.0/topics/db/queries/#has-key)
        * [`has_keys`](https://docs.djangoproject.com/en/6.0/topics/db/queries/#has-keys)
        * [`has_any_keys`](https://docs.djangoproject.com/en/6.0/topics/db/queries/#has-any-keys)
    * [Complex lookups with `Q` objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#complex-lookups-with-q-objects)
    * [Comparing objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#comparing-objects)
    * [Deleting objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#deleting-objects)
    * [Copying model instances](https://docs.djangoproject.com/en/6.0/topics/db/queries/#copying-model-instances)
    * [Updating multiple objects at once](https://docs.djangoproject.com/en/6.0/topics/db/queries/#updating-multiple-objects-at-once)
    * [Related objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#related-objects)
      * [One-to-many relationships](https://docs.djangoproject.com/en/6.0/topics/db/queries/#one-to-many-relationships)
        * [Forward](https://docs.djangoproject.com/en/6.0/topics/db/queries/#forward)
        * [Following relationships “backward”](https://docs.djangoproject.com/en/6.0/topics/db/queries/#following-relationships-backward)
        * [Using a custom reverse manager](https://docs.djangoproject.com/en/6.0/topics/db/queries/#using-a-custom-reverse-manager)
        * [Additional methods to handle related objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#additional-methods-to-handle-related-objects)
      * [Many-to-many relationships](https://docs.djangoproject.com/en/6.0/topics/db/queries/#many-to-many-relationships)
        * [Filtering on many-to-many relationships](https://docs.djangoproject.com/en/6.0/topics/db/queries/#filtering-on-many-to-many-relationships)
      * [One-to-one relationships](https://docs.djangoproject.com/en/6.0/topics/db/queries/#one-to-one-relationships)
      * [How are the backward relationships possible?](https://docs.djangoproject.com/en/6.0/topics/db/queries/#how-are-the-backward-relationships-possible)
      * [Queries over related objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#queries-over-related-objects)
    * [Falling back to raw SQL](https://docs.djangoproject.com/en/6.0/topics/db/queries/#falling-back-to-raw-sql)


### Browse
  * Prev: [Models](https://docs.djangoproject.com/en/6.0/topics/db/models/)
  * Next: [Aggregation](https://docs.djangoproject.com/en/6.0/topics/db/aggregation/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [Using Django](https://docs.djangoproject.com/en/6.0/topics/)
      * [Models and databases](https://docs.djangoproject.com/en/6.0/topics/db/)
        * Making queries


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
