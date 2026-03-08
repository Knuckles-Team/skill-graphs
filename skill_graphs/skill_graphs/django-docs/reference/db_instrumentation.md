This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/db/instrumentation/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/db/instrumentation/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/db/instrumentation/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/db/instrumentation/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/db/instrumentation/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/db/instrumentation/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/db/instrumentation/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/db/instrumentation/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/db/instrumentation/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/db/instrumentation/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/db/instrumentation/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/db/instrumentation/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/db/instrumentation/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/db/instrumentation/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/db/instrumentation/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/db/instrumentation/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/db/instrumentation/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/db/instrumentation/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/db/instrumentation/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/db/instrumentation/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/db/instrumentation/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/db/instrumentation/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/db/instrumentation/)


  * [](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/#top)


# Database instrumentation[¶](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/#database-instrumentation "Link to this heading")
To help you understand and control the queries issued by your code, Django provides a hook for installing wrapper functions around the execution of database queries. For example, wrappers can count queries, measure query duration, log queries, or even prevent query execution (e.g. to make sure that no queries are issued while rendering a template with prefetched data).
The wrappers are modeled after [middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/) – they are callables which take another callable as one of their arguments. They call that callable to invoke the (possibly wrapped) database query, and they can do what they want around that call. They are, however, created and installed by user code, and so don’t need a separate factory like middleware do.
Installing a wrapper is done in a context manager – so the wrappers are temporary and specific to some flow in your code.
As mentioned above, an example of a wrapper is a query execution blocker. It could look like this:
```
def blocker(*args):
    raise Exception("No database access allowed here.")

```

And it would be used in a view to block queries from the template like so:
```
from django.db import connection
from django.shortcuts import render


def my_view(request):
    context = {...}  # Code to generate context with all data.
    template_name = ...
    with connection.execute_wrapper(blocker):
        return render(request, template_name, context)

```

The parameters sent to the wrappers are:
  * `execute` – a callable, which should be invoked with the rest of the parameters in order to execute the query.
  * `sql` – a `str`, the SQL query to be sent to the database.
  * `params` – a list/tuple of parameter values for the SQL command, or a list/tuple of lists/tuples if the wrapped call is `executemany()`.
  * `many` – a `bool` indicating whether the ultimately invoked call is `execute()` or `executemany()` (and whether `params` is expected to be a sequence of values, or a sequence of sequences of values).
  * `context` – a dictionary with further data about the context of invocation. This includes the connection and cursor.


Using the parameters, a slightly more complex version of the blocker could include the connection name in the error message:
```
def blocker(execute, sql, params, many, context):
    alias = context["connection"].alias
    raise Exception("Access to database '{}' blocked here".format(alias))

```

For a more complete example, a query logger could look like this:
```
import time


class QueryLogger:
    def __init__(self):
        self.queries = []

    def __call__(self, execute, sql, params, many, context):
        current_query = {"sql": sql, "params": params, "many": many}
        start = time.monotonic()
        try:
            result = execute(sql, params, many, context)
        except Exception as e:
            current_query["status"] = "error"
            current_query["exception"] = e
            raise
        else:
            current_query["status"] = "ok"
            return result
        finally:
            duration = time.monotonic() - start
            current_query["duration"] = duration
            self.queries.append(current_query)

```

To use this, you would create a logger object and install it as a wrapper:
```
from django.db import connection

ql = QueryLogger()
with connection.execute_wrapper(ql):
    do_queries()
# Now we can print the log.
print(ql.queries)

```

##  `connection.execute_wrapper()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/#connection-execute-wrapper "Link to this heading")

execute_wrapper(_wrapper_)[¶](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/#django.db.backends.base.DatabaseWrapper.execute_wrapper "Link to this definition")

Returns a context manager which, when entered, installs a wrapper around database query executions, and when exited, removes the wrapper. The wrapper is installed on the thread-local connection object.
`wrapper` is a callable taking five arguments. It is called for every query execution in the scope of the context manager, with arguments `execute`, `sql`, `params`, `many`, and `context` as described above. It’s expected to call `execute(sql, params, many, context)` and return the return value of that call.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/db/optimization/)
[Fixtures ](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/)
[](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Elements Interactive donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Database instrumentation](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/)
    * [`connection.execute_wrapper()`](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/#connection-execute-wrapper)


### Browse
  * Prev: [Database access optimization](https://docs.djangoproject.com/en/5.0/topics/db/optimization/)
  * Next: [Fixtures](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Models and databases](https://docs.djangoproject.com/en/5.0/topics/db/)
        * Database instrumentation


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
