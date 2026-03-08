This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/db/search/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/db/search/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/db/search/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/db/search/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/db/search/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/db/search/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/db/search/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/db/search/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/db/search/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/db/search/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/db/search/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/db/search/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/db/search/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/db/search/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/db/search/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/db/search/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/db/search/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/db/search/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/db/search/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/db/search/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/db/search/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/db/search/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/db/search/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/db/search/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/db/search/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/db/search/)


  * [](https://docs.djangoproject.com/en/5.0/topics/db/search/#top)


# Search[¶](https://docs.djangoproject.com/en/5.0/topics/db/search/#search "Link to this heading")
A common task for web applications is to search some data in the database with user input. In a simple case, this could be filtering a list of objects by a category. A more complex use case might require searching with weighting, categorization, highlighting, multiple languages, and so on. This document explains some of the possible use cases and the tools you can use.
We’ll refer to the same models used in [Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/).
## Use Cases[¶](https://docs.djangoproject.com/en/5.0/topics/db/search/#use-cases "Link to this heading")
### Standard textual queries[¶](https://docs.djangoproject.com/en/5.0/topics/db/search/#standard-textual-queries "Link to this heading")
Text-based fields have a selection of matching operations. For example, you may wish to allow lookup up an author like so:
```
>>> Author.objects.filter(name__contains="Terry")
[<Author: Terry Gilliam>, <Author: Terry Jones>]

```

This is a very fragile solution as it requires the user to know an exact substring of the author’s name. A better approach could be a case-insensitive match ([`icontains`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-icontains)), but this is only marginally better.
### A database’s more advanced comparison functions[¶](https://docs.djangoproject.com/en/5.0/topics/db/search/#a-database-s-more-advanced-comparison-functions "Link to this heading")
If you’re using PostgreSQL, Django provides [a selection of database specific tools](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/search/) to allow you to leverage more complex querying options. Other databases have different selections of tools, possibly via plugins or user-defined functions. Django doesn’t include any support for them at this time. We’ll use some examples from PostgreSQL to demonstrate the kind of functionality databases may have.
Searching in other databases
All of the searching tools provided by [`django.contrib.postgres`](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/#module-django.contrib.postgres "django.contrib.postgres: PostgreSQL-specific fields and features") are constructed entirely on public APIs such as [custom lookups](https://docs.djangoproject.com/en/5.0/ref/models/lookups/) and [database functions](https://docs.djangoproject.com/en/5.0/ref/models/database-functions/). Depending on your database, you should be able to construct queries to allow similar APIs. If there are specific things which cannot be achieved this way, please open a ticket.
In the above example, we determined that a case insensitive lookup would be more useful. When dealing with non-English names, a further improvement is to use [`unaccented comparison`](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/lookups/#std-fieldlookup-unaccent):
```
>>> Author.objects.filter(name__unaccent__icontains="Helen")
[<Author: Helen Mirren>, <Author: Helena Bonham Carter>, <Author: Hélène Joy>]

```

This shows another issue, where we are matching against a different spelling of the name. In this case we have an asymmetry though - a search for `Helen` will pick up `Helena` or `Hélène`, but not the reverse. Another option would be to use a [`trigram_similar`](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/lookups/#std-fieldlookup-trigram_similar) comparison, which compares sequences of letters.
For example:
```
>>> Author.objects.filter(name__unaccent__lower__trigram_similar="Hélène")
[<Author: Helen Mirren>, <Author: Hélène Joy>]

```

Now we have a different problem - the longer name of “Helena Bonham Carter” doesn’t show up as it is much longer. Trigram searches consider all combinations of three letters, and compares how many appear in both search and source strings. For the longer name, there are more combinations that don’t appear in the source string, so it is no longer considered a close match.
The correct choice of comparison functions here depends on your particular data set, for example the language(s) used and the type of text being searched. All of the examples we’ve seen are on short strings where the user is likely to enter something close (by varying definitions) to the source data.
### Document-based search[¶](https://docs.djangoproject.com/en/5.0/topics/db/search/#document-based-search "Link to this heading")
Standard database operations stop being a useful approach when you start considering large blocks of text. Whereas the examples above can be thought of as operations on a string of characters, full text search looks at the actual words. Depending on the system used, it’s likely to use some of the following ideas:
  * Ignoring “stop words” such as “a”, “the”, “and”.
  * Stemming words, so that “pony” and “ponies” are considered similar.
  * Weighting words based on different criteria such as how frequently they appear in the text, or the importance of the fields, such as the title or keywords, that they appear in.


There are many alternatives for using searching software, some of the most prominent are
#### PostgreSQL support[¶](https://docs.djangoproject.com/en/5.0/topics/db/search/#postgresql-support "Link to this heading")
PostgreSQL has its own full text search implementation built-in. While not as powerful as some other search engines, it has the advantage of being inside your database and so can easily be combined with other relational queries such as categorization.
The [`django.contrib.postgres`](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/#module-django.contrib.postgres "django.contrib.postgres: PostgreSQL-specific fields and features") module provides some helpers to make these queries. For example, a query might select all the blog entries which mention “cheese”:
```
>>> Entry.objects.filter(body_text__search="cheese")
[<Entry: Cheese on Toast recipes>, <Entry: Pizza recipes>]

```

You can also filter on a combination of fields and on related models:
```
>>> Entry.objects.annotate(
...     search=SearchVector("blog__tagline", "body_text"),
... ).filter(search="cheese")
[
    <Entry: Cheese on Toast recipes>,
    <Entry: Pizza Recipes>,
    <Entry: Dairy farming in Argentina>,
]

```

See the `contrib.postgres` [Full text search](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/search/) document for complete details.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/db/aggregation/)
[Managers ](https://docs.djangoproject.com/en/5.0/topics/db/managers/)
[](https://docs.djangoproject.com/en/5.0/topics/db/search/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Hamza Bawumia donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Search](https://docs.djangoproject.com/en/5.0/topics/db/search/)
    * [Use Cases](https://docs.djangoproject.com/en/5.0/topics/db/search/#use-cases)
      * [Standard textual queries](https://docs.djangoproject.com/en/5.0/topics/db/search/#standard-textual-queries)
      * [A database’s more advanced comparison functions](https://docs.djangoproject.com/en/5.0/topics/db/search/#a-database-s-more-advanced-comparison-functions)
      * [Document-based search](https://docs.djangoproject.com/en/5.0/topics/db/search/#document-based-search)
        * [PostgreSQL support](https://docs.djangoproject.com/en/5.0/topics/db/search/#postgresql-support)


### Browse
  * Prev: [Aggregation](https://docs.djangoproject.com/en/5.0/topics/db/aggregation/)
  * Next: [Managers](https://docs.djangoproject.com/en/5.0/topics/db/managers/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Models and databases](https://docs.djangoproject.com/en/5.0/topics/db/)
        * Search


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
