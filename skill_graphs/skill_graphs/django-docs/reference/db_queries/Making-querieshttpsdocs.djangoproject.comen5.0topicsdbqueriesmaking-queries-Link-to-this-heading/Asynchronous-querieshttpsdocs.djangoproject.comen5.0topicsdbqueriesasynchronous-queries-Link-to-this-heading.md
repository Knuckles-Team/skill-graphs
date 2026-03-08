## Asynchronous queries[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#asynchronous-queries "Link to this heading")
If you are writing asynchronous views or code, you cannot use the ORM for queries in quite the way we have described above, as you cannot call _blocking_ synchronous code from asynchronous code - it will block up the event loop (or, more likely, Django will notice and raise a `SynchronousOnlyOperation` to stop that from happening).
Fortunately, you can do many queries using Django’s asynchronous query APIs. Every method that might block - such as `get()` or `delete()` - has an asynchronous variant (`aget()` or `adelete()`), and when you iterate over results, you can use asynchronous iteration (`async for`) instead.
### Query iteration[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#query-iteration "Link to this heading")
The default way of iterating over a query - with `for` - will result in a blocking database query behind the scenes as Django loads the results at iteration time. To fix this, you can swap to `async for`:
```
async for entry in Authors.objects.filter(name__startswith="A"):
    ...

```

Be aware that you also can’t do other things that might iterate over the queryset, such as wrapping `list()` around it to force its evaluation (you can use `async for` in a comprehension, if you want it).
Because `QuerySet` methods like `filter()` and `exclude()` do not actually run the query - they set up the queryset to run when it’s iterated over - you can use those freely in asynchronous code. For a guide to which methods can keep being used like this, and which have asynchronous versions, read the next section.
###  `QuerySet` and manager methods[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#queryset-and-manager-methods "Link to this heading")
Some methods on managers and querysets - like `get()` and `first()` - force execution of the queryset and are blocking. Some, like `filter()` and `exclude()`, don’t force execution and so are safe to run from asynchronous code. But how are you supposed to tell the difference?
While you could poke around and see if there is an `a`-prefixed version of the method (for example, we have `aget()` but not `afilter()`), there is a more logical way - look up what kind of method it is in the [QuerySet reference](https://docs.djangoproject.com/en/5.0/ref/models/querysets/).
In there, you’ll find the methods on QuerySets grouped into two sections:
  * _Methods that return new querysets_ : These are the non-blocking ones, and don’t have asynchronous versions. You’re free to use these in any situation, though read the notes on `defer()` and `only()` before you use them.
  * _Methods that do not return querysets_ : These are the blocking ones, and have asynchronous versions - the asynchronous name for each is noted in its documentation, though our standard pattern is to add an `a` prefix.


Using this distinction, you can work out when you need to use asynchronous versions, and when you don’t. For example, here’s a valid asynchronous query:
```
user = await User.objects.filter(username=my_input).afirst()

```

`filter()` returns a queryset, and so it’s fine to keep chaining it inside an asynchronous environment, whereas `first()` evaluates and returns a model instance - thus, we change to `afirst()`, and use `await` at the front of the whole expression in order to call it in an asynchronous-friendly way.
Note
If you forget to put the `await` part in, you may see errors like _“coroutine object has no attribute x”_ or _“ <coroutine …>”_ strings in place of your model instances. If you ever see these, you are missing an `await` somewhere to turn that coroutine into a real value.
### Transactions[¶](https://docs.djangoproject.com/en/5.0/topics/db/queries/#transactions "Link to this heading")
Transactions are **not** currently supported with asynchronous queries and updates. You will find that trying to use one raises `SynchronousOnlyOperation`.
If you wish to use a transaction, we suggest you write your ORM code inside a separate, synchronous function and then call that using `sync_to_async` - see [Asynchronous support](https://docs.djangoproject.com/en/5.0/topics/async/) for more.
