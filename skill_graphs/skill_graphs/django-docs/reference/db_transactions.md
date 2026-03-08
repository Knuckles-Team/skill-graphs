This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/db/transactions/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/db/transactions/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/db/transactions/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/db/transactions/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/db/transactions/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/db/transactions/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/db/transactions/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/db/transactions/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/db/transactions/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/db/transactions/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/db/transactions/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/db/transactions/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/db/transactions/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/db/transactions/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/db/transactions/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/db/transactions/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/db/transactions/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/db/transactions/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/db/transactions/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/db/transactions/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/db/transactions/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/db/transactions/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/db/transactions/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/db/transactions/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/db/transactions/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/db/transactions/)


  * [](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#top)


# Database transactions[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#module-django.db.transaction "Link to this heading")
Django gives you a few ways to control how database transactions are managed.
## Managing database transactions[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#managing-database-transactions "Link to this heading")
### Django’s default transaction behavior[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django-s-default-transaction-behavior "Link to this heading")
Django’s default behavior is to run in autocommit mode. Each query is immediately committed to the database, unless a transaction is active. [See below for details](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#autocommit-details).
Django uses transactions or savepoints automatically to guarantee the integrity of ORM operations that require multiple queries, especially [delete()](https://docs.djangoproject.com/en/5.0/topics/db/queries/#topics-db-queries-delete) and [update()](https://docs.djangoproject.com/en/5.0/topics/db/queries/#topics-db-queries-update) queries.
Django’s [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") class also wraps each test in a transaction for performance reasons.
### Tying transactions to HTTP requests[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#tying-transactions-to-http-requests "Link to this heading")
A common way to handle transactions on the web is to wrap each request in a transaction. Set [`ATOMIC_REQUESTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ATOMIC_REQUESTS) to `True` in the configuration of each database for which you want to enable this behavior.
It works like this. Before calling a view function, Django starts a transaction. If the response is produced without problems, Django commits the transaction. If the view produces an exception, Django rolls back the transaction.
You may perform subtransactions using savepoints in your view code, typically with the [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") context manager. However, at the end of the view, either all or none of the changes will be committed.
Warning
While the simplicity of this transaction model is appealing, it also makes it inefficient when traffic increases. Opening a transaction for every view has some overhead. The impact on performance depends on the query patterns of your application and on how well your database handles locking.
Per-request transactions and streaming responses
When a view returns a [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse"), reading the contents of the response will often execute code to generate the content. Since the view has already returned, such code runs outside of the transaction.
Generally speaking, it isn’t advisable to write to the database while generating a streaming response, since there’s no sensible way to handle errors after starting to send the response.
In practice, this feature wraps every view function in the [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") decorator described below.
Note that only the execution of your view is enclosed in the transactions. Middleware runs outside of the transaction, and so does the rendering of template responses.
When [`ATOMIC_REQUESTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ATOMIC_REQUESTS) is enabled, it’s still possible to prevent views from running in a transaction.

non_atomic_requests(_using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#non_atomic_requests)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.non_atomic_requests "Link to this definition")

This decorator will negate the effect of [`ATOMIC_REQUESTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ATOMIC_REQUESTS) for a given view:
```
from django.db import transaction


@transaction.non_atomic_requests
def my_view(request):
    do_stuff()


@transaction.non_atomic_requests(using="other")
def my_other_view(request):
    do_stuff_on_the_other_database()

```

It only works if it’s applied to the view itself.
### Controlling transactions explicitly[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#controlling-transactions-explicitly "Link to this heading")
Django provides a single API to control database transactions.

atomic(_using =None_, _savepoint =True_, _durable =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#atomic)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "Link to this definition")

Atomicity is the defining property of database transactions. `atomic` allows us to create a block of code within which the atomicity on the database is guaranteed. If the block of code is successfully completed, the changes are committed to the database. If there is an exception, the changes are rolled back.
`atomic` blocks can be nested. In this case, when an inner block completes successfully, its effects can still be rolled back if an exception is raised in the outer block at a later point.
It is sometimes useful to ensure an `atomic` block is always the outermost `atomic` block, ensuring that any database changes are committed when the block is exited without errors. This is known as durability and can be achieved by setting `durable=True`. If the `atomic` block is nested within another it raises a `RuntimeError`.
`atomic` is usable both as a
```
from django.db import transaction


@transaction.atomic
def viewfunc(request):
    # This code executes inside a transaction.
    do_stuff()

```

and as a
```
from django.db import transaction


def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()

    with transaction.atomic():
        # This code executes inside a transaction.
        do_more_stuff()

```

Wrapping `atomic` in a try/except block allows for natural handling of integrity errors:
```
from django.db import IntegrityError, transaction


@transaction.atomic
def viewfunc(request):
    create_parent()

    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()

    add_children()

```

In this example, even if `generate_relationships()` causes a database error by breaking an integrity constraint, you can execute queries in `add_children()`, and the changes from `create_parent()` are still there and bound to the same transaction. Note that any operations attempted in `generate_relationships()` will already have been rolled back safely when `handle_exception()` is called, so the exception handler can also operate on the database if necessary.
Avoid catching exceptions inside `atomic`!
When exiting an `atomic` block, Django looks at whether it’s exited normally or with an exception to determine whether to commit or roll back. If you catch and handle exceptions inside an `atomic` block, you may hide from Django the fact that a problem has happened. This can result in unexpected behavior.
This is mostly a concern for [`DatabaseError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.DatabaseError "django.db.DatabaseError") and its subclasses such as [`IntegrityError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError"). After such an error, the transaction is broken and Django will perform a rollback at the end of the `atomic` block. If you attempt to run database queries before the rollback happens, Django will raise a [`TransactionManagementError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.transaction.TransactionManagementError "django.db.transaction.TransactionManagementError"). You may also encounter this behavior when an ORM-related signal handler raises an exception.
The correct way to catch database errors is around an `atomic` block as shown above. If necessary, add an extra `atomic` block for this purpose. This pattern has another advantage: it delimits explicitly which operations will be rolled back if an exception occurs.
If you catch exceptions raised by raw SQL queries, Django’s behavior is unspecified and database-dependent.
You may need to manually revert app state when rolling back a transaction.
The values of a model’s fields won’t be reverted when a transaction rollback happens. This could lead to an inconsistent model state unless you manually restore the original field values.
For example, given `MyModel` with an `active` field, this snippet ensures that the `if obj.active` check at the end uses the correct value if updating `active` to `True` fails in the transaction:
```
from django.db import DatabaseError, transaction

obj = MyModel(active=False)
obj.active = True
try:
    with transaction.atomic():
        obj.save()
except DatabaseError:
    obj.active = False

if obj.active:
    ...

```

This also applies to any other mechanism that may hold app state, such as caching or global variables. For example, if the code proactively updates data in the cache after saving an object, it’s recommended to use [transaction.on_commit()](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#performing-actions-after-commit) instead, to defer cache alterations until the transaction is actually committed.
In order to guarantee atomicity, `atomic` disables some APIs. Attempting to commit, roll back, or change the autocommit state of the database connection within an `atomic` block will raise an exception.
`atomic` takes a `using` argument which should be the name of a database. If this argument isn’t provided, Django uses the `"default"` database.
Under the hood, Django’s transaction management code:
  * opens a transaction when entering the outermost `atomic` block;
  * creates a savepoint when entering an inner `atomic` block;
  * releases or rolls back to the savepoint when exiting an inner block;
  * commits or rolls back the transaction when exiting the outermost block.


You can disable the creation of savepoints for inner blocks by setting the `savepoint` argument to `False`. If an exception occurs, Django will perform the rollback when exiting the first parent block with a savepoint if there is one, and the outermost block otherwise. Atomicity is still guaranteed by the outer transaction. This option should only be used if the overhead of savepoints is noticeable. It has the drawback of breaking the error handling described above.
You may use `atomic` when autocommit is turned off. It will only use savepoints, even for the outermost block.
Performance considerations
Open transactions have a performance cost for your database server. To minimize this overhead, keep your transactions as short as possible. This is especially important if you’re using [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") in long-running processes, outside of Django’s request / response cycle.
## Autocommit[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#autocommit "Link to this heading")
### Why Django uses autocommit[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#why-django-uses-autocommit "Link to this heading")
In the SQL standards, each SQL query starts a transaction, unless one is already active. Such transactions must then be explicitly committed or rolled back.
This isn’t always convenient for application developers. To alleviate this problem, most databases provide an autocommit mode. When autocommit is turned on and no transaction is active, each SQL query gets wrapped in its own transaction. In other words, not only does each such query start a transaction, but the transaction also gets automatically committed or rolled back, depending on whether the query succeeded.
To avoid this, you can [deactivate the transaction management](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#deactivate-transaction-management), but it isn’t recommended.
### Deactivating transaction management[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#deactivating-transaction-management "Link to this heading")
You can totally disable Django’s transaction management for a given database by setting [`AUTOCOMMIT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-AUTOCOMMIT) to `False` in its configuration. If you do this, Django won’t enable autocommit, and won’t perform any commits. You’ll get the regular behavior of the underlying database library.
This requires you to commit explicitly every transaction, even those started by Django or by third-party libraries. Thus, this is best used in situations where you want to run your own transaction-controlling middleware or do something really strange.
## Performing actions after commit[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#performing-actions-after-commit "Link to this heading")
Sometimes you need to perform an action related to the current database transaction, but only if the transaction successfully commits. Examples might include a background task, an email notification, or a cache invalidation.
[`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") allows you to register callbacks that will be executed after the open transaction is successfully committed:

on_commit(_func_ , _using =None_, _robust =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#on_commit)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "Link to this definition")

Pass a function, or any callable, to [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit"):
```
from django.db import transaction


def send_welcome_email(): ...


transaction.on_commit(send_welcome_email)

```

Callbacks will not be passed any arguments, but you can bind them with
```
from functools import partial

for user in users:
    transaction.on_commit(partial(send_invite_email, user=user))

```

Callbacks are called after the open transaction is successfully committed. If the transaction is instead rolled back (typically when an unhandled exception is raised in an [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block), the callback will be discarded, and never called.
If you call `on_commit()` while there isn’t an open transaction, the callback will be executed immediately.
It’s sometimes useful to register callbacks that can fail. Passing `robust=True` allows the next callbacks to be executed even if the current one throws an exception. All errors derived from Python’s `Exception` class are caught and logged to the `django.db.backends.base` logger.
You can use [`TestCase.captureOnCommitCallbacks()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase.captureOnCommitCallbacks "django.test.TestCase.captureOnCommitCallbacks") to test callbacks registered with [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit").
Changed in Django 4.2:
The `robust` argument was added.
### Savepoints[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#savepoints "Link to this heading")
Savepoints (i.e. nested [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") blocks) are handled correctly. That is, an [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") callable registered after a savepoint (in a nested [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block) will be called after the outer transaction is committed, but not if a rollback to that savepoint or any previous savepoint occurred during the transaction:
```
with transaction.atomic():  # Outer atomic, start a new transaction
    transaction.on_commit(foo)

    with transaction.atomic():  # Inner atomic block, create a savepoint
        transaction.on_commit(bar)

# foo() and then bar() will be called when leaving the outermost block

```

On the other hand, when a savepoint is rolled back (due to an exception being raised), the inner callable will not be called:
```
with transaction.atomic():  # Outer atomic, start a new transaction
    transaction.on_commit(foo)

    try:
        with transaction.atomic():  # Inner atomic block, create a savepoint
            transaction.on_commit(bar)
            raise SomeError()  # Raising an exception - abort the savepoint
    except SomeError:
        pass

# foo() will be called, but not bar()

```

### Order of execution[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#order-of-execution "Link to this heading")
On-commit functions for a given transaction are executed in the order they were registered.
### Exception handling[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#exception-handling "Link to this heading")
If one on-commit function registered with `robust=False` within a given transaction raises an uncaught exception, no later registered functions in that same transaction will run. This is the same behavior as if you’d executed the functions sequentially yourself without [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit").
Changed in Django 4.2:
The `robust` argument was added.
### Timing of execution[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#timing-of-execution "Link to this heading")
Your callbacks are executed _after_ a successful commit, so a failure in a callback will not cause the transaction to roll back. They are executed conditionally upon the success of the transaction, but they are not _part_ of the transaction. For the intended use cases (mail notifications, background tasks, etc.), this should be fine. If it’s not (if your follow-up action is so critical that its failure should mean the failure of the transaction itself), then you don’t want to use the [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") hook. Instead, you may want
Callbacks are not run until autocommit is restored on the connection following the commit (because otherwise any queries done in a callback would open an implicit transaction, preventing the connection from going back into autocommit mode).
When in autocommit mode and outside of an [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block, the function will run immediately, not on commit.
On-commit functions only work with [autocommit mode](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#managing-autocommit) and the [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") (or [`ATOMIC_REQUESTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ATOMIC_REQUESTS)) transaction API. Calling [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") when autocommit is disabled and you are not within an atomic block will result in an error.
### Use in tests[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#use-in-tests "Link to this heading")
Django’s [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") class wraps each test in a transaction and rolls back that transaction after each test, in order to provide test isolation. This means that no transaction is ever actually committed, thus your [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") callbacks will never be run.
You can overcome this limitation by using [`TestCase.captureOnCommitCallbacks()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase.captureOnCommitCallbacks "django.test.TestCase.captureOnCommitCallbacks"). This captures your [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") callbacks in a list, allowing you to make assertions on them, or emulate the transaction committing by calling them.
Another way to overcome the limitation is to use [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") instead of [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase"). This will mean your transactions are committed, and the callbacks will run. However [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") flushes the database between tests, which is significantly slower than [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase")'s isolation.
### Why no rollback hook?[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#why-no-rollback-hook "Link to this heading")
A rollback hook is harder to implement robustly than a commit hook, since a variety of things can cause an implicit rollback.
For instance, if your database connection is dropped because your process was killed without a chance to shut down gracefully, your rollback hook will never run.
But there is a solution: instead of doing something during the atomic block (transaction) and then undoing it if the transaction fails, use [`on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") to delay doing it in the first place until after the transaction succeeds. It’s a lot easier to undo something you never did in the first place!
## Low-level APIs[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#low-level-apis "Link to this heading")
Warning
Always prefer [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") if possible at all. It accounts for the idiosyncrasies of each database and prevents invalid operations.
The low level APIs are only useful if you’re implementing your own transaction management.
### Autocommit[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#managing-autocommit "Link to this heading")
Django provides an API in the [`django.db.transaction`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#module-django.db.transaction "django.db.transaction") module to manage the autocommit state of each database connection.

get_autocommit(_using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#get_autocommit)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.get_autocommit "Link to this definition")


set_autocommit(_autocommit_ , _using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#set_autocommit)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.set_autocommit "Link to this definition")

These functions take a `using` argument which should be the name of a database. If it isn’t provided, Django uses the `"default"` database.
Autocommit is initially turned on. If you turn it off, it’s your responsibility to restore it.
Once you turn autocommit off, you get the default behavior of your database adapter, and Django won’t help you. Although that behavior is specified in
You must ensure that no transaction is active, usually by issuing a [`commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.commit "django.db.transaction.commit") or a [`rollback()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.rollback "django.db.transaction.rollback"), before turning autocommit back on.
Django will refuse to turn autocommit off when an [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block is active, because that would break atomicity.
### Transactions[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#transactions "Link to this heading")
A transaction is an atomic set of database queries. Even if your program crashes, the database guarantees that either all the changes will be applied, or none of them.
Django doesn’t provide an API to start a transaction. The expected way to start a transaction is to disable autocommit with [`set_autocommit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.set_autocommit "django.db.transaction.set_autocommit").
Once you’re in a transaction, you can choose either to apply the changes you’ve performed until this point with [`commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.commit "django.db.transaction.commit"), or to cancel them with [`rollback()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.rollback "django.db.transaction.rollback"). These functions are defined in [`django.db.transaction`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#module-django.db.transaction "django.db.transaction").

commit(_using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#commit)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.commit "Link to this definition")


rollback(_using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#rollback)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.rollback "Link to this definition")

These functions take a `using` argument which should be the name of a database. If it isn’t provided, Django uses the `"default"` database.
Django will refuse to commit or to rollback when an [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block is active, because that would break atomicity.
### Savepoints[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#topics-db-transactions-savepoints "Link to this heading")
A savepoint is a marker within a transaction that enables you to roll back part of a transaction, rather than the full transaction. Savepoints are available with the SQLite, PostgreSQL, Oracle, and MySQL (when using the InnoDB storage engine) backends. Other backends provide the savepoint functions, but they’re empty operations – they don’t actually do anything.
Savepoints aren’t especially useful if you are using autocommit, the default behavior of Django. However, once you open a transaction with [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic"), you build up a series of database operations awaiting a commit or rollback. If you issue a rollback, the entire transaction is rolled back. Savepoints provide the ability to perform a fine-grained rollback, rather than the full rollback that would be performed by `transaction.rollback()`.
When the [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") decorator is nested, it creates a savepoint to allow partial commit or rollback. You’re strongly encouraged to use [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") rather than the functions described below, but they’re still part of the public API, and there’s no plan to deprecate them.
Each of these functions takes a `using` argument which should be the name of a database for which the behavior applies. If no `using` argument is provided then the `"default"` database is used.
Savepoints are controlled by three functions in [`django.db.transaction`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#module-django.db.transaction "django.db.transaction"):

savepoint(_using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#savepoint)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.savepoint "Link to this definition")

Creates a new savepoint. This marks a point in the transaction that is known to be in a “good” state. Returns the savepoint ID (`sid`).

savepoint_commit(_sid_ , _using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#savepoint_commit)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.savepoint_commit "Link to this definition")

Releases savepoint `sid`. The changes performed since the savepoint was created become part of the transaction.

savepoint_rollback(_sid_ , _using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#savepoint_rollback)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.savepoint_rollback "Link to this definition")

Rolls back the transaction to savepoint `sid`.
These functions do nothing if savepoints aren’t supported or if the database is in autocommit mode.
In addition, there’s a utility function:

clean_savepoints(_using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#clean_savepoints)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.clean_savepoints "Link to this definition")

Resets the counter used to generate unique savepoint IDs.
The following example demonstrates the use of savepoints:
```
from django.db import transaction


# open a transaction
@transaction.atomic
def viewfunc(request):
    a.save()
    # transaction now contains a.save()

    sid = transaction.savepoint()

    b.save()
    # transaction now contains a.save() and b.save()

    if want_to_keep_b:
        transaction.savepoint_commit(sid)
        # open transaction still contains a.save() and b.save()
    else:
        transaction.savepoint_rollback(sid)
        # open transaction now contains only a.save()

```

Savepoints may be used to recover from a database error by performing a partial rollback. If you’re doing this inside an [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block, the entire block will still be rolled back, because it doesn’t know you’ve handled the situation at a lower level! To prevent this, you can control the rollback behavior with the following functions.

get_rollback(_using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#get_rollback)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.get_rollback "Link to this definition")


set_rollback(_rollback_ , _using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/transaction/#set_rollback)[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.set_rollback "Link to this definition")

Setting the rollback flag to `True` forces a rollback when exiting the innermost atomic block. This may be useful to trigger a rollback without raising an exception.
Setting it to `False` prevents such a rollback. Before doing that, make sure you’ve rolled back the transaction to a known-good savepoint within the current atomic block! Otherwise you’re breaking atomicity and data corruption may occur.
## Database-specific notes[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#database-specific-notes "Link to this heading")
### Savepoints in SQLite[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#savepoints-in-sqlite "Link to this heading")
While SQLite supports savepoints, a flaw in the design of the
When autocommit is enabled, savepoints don’t make sense. When it’s disabled, `SELECT`, `INSERT`, `UPDATE`, `DELETE` and `REPLACE`.) This bug has two consequences:
  * The low level APIs for savepoints are only usable inside a transaction i.e. inside an [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block.
  * It’s impossible to use [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") when autocommit is turned off.


### Transactions in MySQL[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#transactions-in-mysql "Link to this heading")
If you’re using MySQL, your tables may or may not support transactions; it depends on your MySQL version and the table types you’re using. (By “table types,” we mean something like “InnoDB” or “MyISAM”.) MySQL transaction peculiarities are outside the scope of this article, but the MySQL site has
If your MySQL setup does _not_ support transactions, then Django will always function in autocommit mode: statements will be executed and committed as soon as they’re called. If your MySQL setup _does_ support transactions, Django will handle transactions as explained in this document.
### Handling exceptions within PostgreSQL transactions[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#handling-exceptions-within-postgresql-transactions "Link to this heading")
Note
This section is relevant only if you’re implementing your own transaction management. This problem cannot occur in Django’s default mode and [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") handles it automatically.
Inside a transaction, when a call to a PostgreSQL cursor raises an exception (typically `IntegrityError`), all subsequent SQL in the same transaction will fail with the error “current transaction is aborted, queries ignored until end of transaction block”. While the basic use of `save()` is unlikely to raise an exception in PostgreSQL, there are more advanced usage patterns which might, such as saving objects with unique fields, saving using the `force_insert`/`force_update` flag, or invoking custom SQL.
There are several ways to recover from this sort of error.
#### Transaction rollback[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#transaction-rollback "Link to this heading")
The first option is to roll back the entire transaction. For example:
```
a.save()  # Succeeds, but may be undone by transaction rollback
try:
    b.save()  # Could throw exception
except IntegrityError:
    transaction.rollback()
c.save()  # Succeeds, but a.save() may have been undone

```

Calling `transaction.rollback()` rolls back the entire transaction. Any uncommitted database operations will be lost. In this example, the changes made by `a.save()` would be lost, even though that operation raised no error itself.
#### Savepoint rollback[¶](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#savepoint-rollback "Link to this heading")
You can use [savepoints](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#topics-db-transactions-savepoints) to control the extent of a rollback. Before performing a database operation that could fail, you can set or update the savepoint; that way, if the operation fails, you can roll back the single offending operation, rather than the entire transaction. For example:
```
a.save()  # Succeeds, and never undone by savepoint rollback
sid = transaction.savepoint()
try:
    b.save()  # Could throw exception
    transaction.savepoint_commit(sid)
except IntegrityError:
    transaction.savepoint_rollback(sid)
c.save()  # Succeeds, and a.save() is never undone

```

In this example, `a.save()` will not be undone in the case where `b.save()` raises an exception.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/db/sql/)
[Multiple databases ](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/)
[](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ FluxIndustries donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Database transactions](https://docs.djangoproject.com/en/5.0/topics/db/transactions/)
    * [Managing database transactions](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#managing-database-transactions)
      * [Django’s default transaction behavior](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django-s-default-transaction-behavior)
      * [Tying transactions to HTTP requests](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#tying-transactions-to-http-requests)
      * [Controlling transactions explicitly](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#controlling-transactions-explicitly)
    * [Autocommit](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#autocommit)
      * [Why Django uses autocommit](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#why-django-uses-autocommit)
      * [Deactivating transaction management](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#deactivating-transaction-management)
    * [Performing actions after commit](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#performing-actions-after-commit)
      * [Savepoints](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#savepoints)
      * [Order of execution](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#order-of-execution)
      * [Exception handling](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#exception-handling)
      * [Timing of execution](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#timing-of-execution)
      * [Use in tests](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#use-in-tests)
      * [Why no rollback hook?](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#why-no-rollback-hook)
    * [Low-level APIs](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#low-level-apis)
      * [Autocommit](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#managing-autocommit)
      * [Transactions](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#transactions)
      * [Savepoints](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#topics-db-transactions-savepoints)
    * [Database-specific notes](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#database-specific-notes)
      * [Savepoints in SQLite](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#savepoints-in-sqlite)
      * [Transactions in MySQL](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#transactions-in-mysql)
      * [Handling exceptions within PostgreSQL transactions](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#handling-exceptions-within-postgresql-transactions)
        * [Transaction rollback](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#transaction-rollback)
        * [Savepoint rollback](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#savepoint-rollback)


### Browse
  * Prev: [Performing raw SQL queries](https://docs.djangoproject.com/en/5.0/topics/db/sql/)
  * Next: [Multiple databases](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Models and databases](https://docs.djangoproject.com/en/5.0/topics/db/)
        * Database transactions


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
