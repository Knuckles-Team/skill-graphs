This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/performance/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/performance/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/performance/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/performance/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/performance/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/performance/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/performance/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/performance/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/performance/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/performance/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/performance/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/performance/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/performance/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/performance/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/performance/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/performance/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/performance/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/performance/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/performance/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/performance/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/performance/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/performance/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/performance/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/performance/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/performance/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/performance/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/performance/)


  * [](https://docs.djangoproject.com/en/5.0/topics/performance/#top)


# Performance and optimization[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#performance-and-optimization "Link to this heading")
This document provides an overview of techniques and tools that can help get your Django code running more efficiently - faster, and using fewer system resources.
## Introduction[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#introduction "Link to this heading")
Generally one’s first concern is to write code that _works_ , whose logic functions as required to produce the expected output. Sometimes, however, this will not be enough to make the code work as _efficiently_ as one would like.
In this case, what’s needed is something - and in practice, often a collection of things - to improve the code’s performance without, or only minimally, affecting its behavior.
## General approaches[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#general-approaches "Link to this heading")
### What are you optimizing _for_?[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#what-are-you-optimizing-for "Link to this heading")
It’s important to have a clear idea what you mean by ‘performance’. There is not just one metric of it.
Improved speed might be the most obvious aim for a program, but sometimes other performance improvements might be sought, such as lower memory consumption or fewer demands on the database or network.
Improvements in one area will often bring about improved performance in another, but not always; sometimes one can even be at the expense of another. For example, an improvement in a program’s speed might cause it to use more memory. Even worse, it can be self-defeating - if the speed improvement is so memory-hungry that the system starts to run out of memory, you’ll have done more harm than good.
There are other trade-offs to bear in mind. Your own time is a valuable resource, more precious than CPU time. Some improvements might be too difficult to be worth implementing, or might affect the portability or maintainability of the code. Not all performance improvements are worth the effort.
So, you need to know what performance improvements you are aiming for, and you also need to know that you have a good reason for aiming in that direction - and for that you need:
### Performance benchmarking[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#performance-benchmarking "Link to this heading")
It’s no good just guessing or assuming where the inefficiencies lie in your code.
#### Django tools[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#django-tools "Link to this heading")
Third-party panels are also available for the toolbar, that can (for example) report on cache performance and template rendering times.
#### Third-party services[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#third-party-services "Link to this heading")
There are a number of free services that will analyze and report on the performance of your site’s pages from the perspective of a remote HTTP client, in effect simulating the experience of an actual user.
These can’t report on the internals of your code, but can provide a useful insight into your site’s overall performance, including aspects that can’t be adequately measured from within Django environment. Examples include:
There are also several paid-for services that perform a similar analysis, including some that are Django-aware and can integrate with your codebase to profile its performance far more comprehensively.
### Get things right from the start[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#get-things-right-from-the-start "Link to this heading")
Some work in optimization involves tackling performance shortcomings, but some of the work can be built-in to what you’d do anyway, as part of the good practices you should adopt even before you start thinking about improving performance.
In this respect Python is an excellent language to work with, because solutions that look elegant and feel right usually are the best performing ones. As with most skills, learning what “looks right” takes practice, but one of the most useful guidelines is:
#### Work at the appropriate level[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#work-at-the-appropriate-level "Link to this heading")
Django offers many different ways of approaching things, but just because it’s possible to do something in a certain way doesn’t mean that it’s the most appropriate way to do it. For example, you might find that you could calculate the same thing - the number of items in a collection, perhaps - in a `QuerySet`, in Python, or in a template.
However, it will almost always be faster to do this work at lower rather than higher levels. At higher levels the system has to deal with objects through multiple levels of abstraction and layers of machinery.
That is, the database can typically do things faster than Python can, which can do them faster than the template language can:
```
# QuerySet operation on the database
# fast, because that's what databases are good at
my_bicycles.count()

# counting Python objects
# slower, because it requires a database query anyway, and processing
# of the Python objects
len(my_bicycles)

```

```
<!--
Django template filter
slower still, because it will have to count them in Python anyway,
and because of template language overheads
-->
{{ my_bicycles|length }}

```

Generally speaking, the most appropriate level for the job is the lowest-level one that it is comfortable to code for.
Note
The example above is merely illustrative.
Firstly, in a real-life case you need to consider what is happening before and after your count to work out what’s an optimal way of doing it _in that particular context_. The database optimization documents describes [a case where counting in the template would be better](https://docs.djangoproject.com/en/5.0/topics/db/optimization/#overuse-of-count-and-exists).
Secondly, there are other options to consider: in a real-life case, `{{ my_bicycles.count }}`, which invokes the `QuerySet` `count()` method directly from the template, might be the most appropriate choice.
## Caching[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#caching "Link to this heading")
Often it is expensive (that is, resource-hungry and slow) to compute a value, so there can be huge benefit in saving the value to a quickly accessible cache, ready for the next time it’s required.
It’s a sufficiently significant and powerful technique that Django includes a comprehensive caching framework, as well as other smaller pieces of caching functionality.
###  [The caching framework](https://docs.djangoproject.com/en/5.0/topics/cache/)[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#the-caching-framework "Link to this heading")
Django’s [caching framework](https://docs.djangoproject.com/en/5.0/topics/cache/) offers very significant opportunities for performance gains, by saving dynamic content so that it doesn’t need to be calculated for each request.
For convenience, Django offers different levels of cache granularity: you can cache the output of specific views, or only the pieces that are difficult to produce, or even an entire site.
Implementing caching should not be regarded as an alternative to improving code that’s performing poorly because it has been written badly. It’s one of the final steps toward producing well-performing code, not a shortcut.
###  [`cached_property`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.cached_property "django.utils.functional.cached_property")[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#cached-property "Link to this heading")
It’s common to have to call a class instance’s method more than once. If that function is expensive, then doing so can be wasteful.
Using the [`cached_property`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.cached_property "django.utils.functional.cached_property") decorator saves the value returned by a property; the next time the function is called on that instance, it will return the saved value rather than re-computing it. Note that this only works on methods that take `self` as their only argument and that it changes the method to a property.
Certain Django components also have their own caching functionality; these are discussed below in the sections related to those components.
## Understanding laziness[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#understanding-laziness "Link to this heading")
_Laziness_ is a strategy complementary to caching. Caching avoids recomputation by saving results; laziness delays computation until it’s actually required.
Laziness allows us to refer to things before they are instantiated, or even before it’s possible to instantiate them. This has numerous uses.
For example, [lazy translation](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#lazy-translations) can be used before the target language is even known, because it doesn’t take place until the translated string is actually required, such as in a rendered template.
Laziness is also a way to save effort by trying to avoid work in the first place. That is, one aspect of laziness is not doing anything until it has to be done, because it may not turn out to be necessary after all. Laziness can therefore have performance implications, and the more expensive the work concerned, the more there is to gain through laziness.
Python provides a number of tools for lazy evaluation, particularly through the
### Laziness in Django[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#laziness-in-django "Link to this heading")
Django is itself quite lazy. A good example of this can be found in the evaluation of `QuerySets`. [QuerySets are lazy](https://docs.djangoproject.com/en/5.0/topics/db/queries/#querysets-are-lazy). Thus a `QuerySet` can be created, passed around and combined with other `QuerySets`, without actually incurring any trips to the database to fetch the items it describes. What gets passed around is the `QuerySet` object, not the collection of items that - eventually - will be required from the database.
On the other hand, [certain operations will force the evaluation of a QuerySet](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#when-querysets-are-evaluated). Avoiding the premature evaluation of a `QuerySet` can save making an expensive and unnecessary trip to the database.
Django also offers a [`keep_lazy()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.keep_lazy "django.utils.functional.keep_lazy") decorator. This allows a function that has been called with a lazy argument to behave lazily itself, only being evaluated when it needs to be. Thus the lazy argument - which could be an expensive one - will not be called upon for evaluation until it’s strictly required.
## Databases[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#databases "Link to this heading")
### Database optimization[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#database-optimization "Link to this heading")
Django’s database layer provides various ways to help developers get the best performance from their databases. The [database optimization documentation](https://docs.djangoproject.com/en/5.0/topics/db/optimization/) gathers together links to the relevant documentation and adds various tips that outline the steps to take when attempting to optimize your database usage.
### Other database-related tips[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#other-database-related-tips "Link to this heading")
Enabling [Persistent connections](https://docs.djangoproject.com/en/5.0/ref/databases/#persistent-database-connections) can speed up connections to the database accounts for a significant part of the request processing time.
This helps a lot on virtualized hosts with limited network performance, for example.
## HTTP performance[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#http-performance "Link to this heading")
### Middleware[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#middleware "Link to this heading")
Django comes with a few helpful pieces of [middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/) that can help optimize your site’s performance. They include:
####  [`ConditionalGetMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.http.ConditionalGetMiddleware "django.middleware.http.ConditionalGetMiddleware")[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#conditionalgetmiddleware "Link to this heading")
Adds support for modern browsers to conditionally GET responses based on the `ETag` and `Last-Modified` headers. It also calculates and sets an ETag if needed.
####  [`GZipMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.gzip.GZipMiddleware "django.middleware.gzip.GZipMiddleware")[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#gzipmiddleware "Link to this heading")
Compresses responses for all modern browsers, saving bandwidth and transfer time. Note that GZipMiddleware is currently considered a security risk, and is vulnerable to attacks that nullify the protection provided by TLS/SSL. See the warning in [`GZipMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.gzip.GZipMiddleware "django.middleware.gzip.GZipMiddleware") for more information.
### Sessions[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#sessions "Link to this heading")
#### Using cached sessions[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#using-cached-sessions "Link to this heading")
[Using cached sessions](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#cached-sessions-backend) may be a way to increase performance by eliminating the need to load session data from a slower storage source like the database and instead storing frequently used session data in memory.
### Static files[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#static-files "Link to this heading")
Static files, which by definition are not dynamic, make an excellent target for optimization gains.
####  [`ManifestStaticFilesStorage`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.ManifestStaticFilesStorage "django.contrib.staticfiles.storage.ManifestStaticFilesStorage")[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#manifeststaticfilesstorage "Link to this heading")
By taking advantage of web browsers’ caching abilities, you can eliminate network hits entirely for a given file after the initial download.
[`ManifestStaticFilesStorage`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.ManifestStaticFilesStorage "django.contrib.staticfiles.storage.ManifestStaticFilesStorage") appends a content-dependent tag to the filenames of [static files](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/) to make it safe for browsers to cache them long-term without missing future changes - when a file changes, so will the tag, so browsers will reload the asset automatically.
#### “Minification”[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#minification "Link to this heading")
Several third-party Django tools and packages provide the ability to “minify” HTML, CSS, and JavaScript. They remove unnecessary whitespace, newlines, and comments, and shorten variable names, and thus reduce the size of the documents that your site publishes.
## Template performance[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#template-performance "Link to this heading")
Note that:
  * using `{% block %}` is faster than using `{% include %}`
  * heavily-fragmented templates, assembled from many small pieces, can affect performance


### The cached template loader[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#the-cached-template-loader "Link to this heading")
Enabling the [`cached template loader`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.loaders.cached.Loader "django.template.loaders.cached.Loader") often improves performance drastically, as it avoids compiling each template every time it needs to be rendered.
## Using different versions of available software[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#using-different-versions-of-available-software "Link to this heading")
It can sometimes be worth checking whether different and better-performing versions of the software that you’re using are available.
These techniques are targeted at more advanced users who want to push the boundaries of performance of an already well-optimized Django site.
However, they are not magic solutions to performance problems, and they’re unlikely to bring better than marginal gains to sites that don’t already do the more basic things the right way.
Note
It’s worth repeating: **reaching for alternatives to software you’re already using is never the first answer to performance problems**. When you reach this level of optimization, you need a formal benchmarking solution.
### Newer is often - but not always - better[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#newer-is-often-but-not-always-better "Link to this heading")
It’s fairly rare for a new release of well-maintained software to be less efficient, but the maintainers can’t anticipate every possible use-case - so while being aware that newer versions are likely to perform better, don’t assume that they always will.
This is true of Django itself. Successive releases have offered a number of improvements across the system, but you should still check the real-world performance of your application, because in some cases you may find that changes mean it performs worse rather than better.
Newer versions of Python, and also of Python packages, will often perform better too - but measure, rather than assume.
Note
Unless you’ve encountered an unusual performance problem in a particular version, you’ll generally find better features, reliability, and security in a new release and that these benefits are far more significant than any performance you might win or lose.
### Alternatives to Django’s template language[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#alternatives-to-django-s-template-language "Link to this heading")
For nearly all cases, Django’s built-in template language is perfectly adequate. However, if the bottlenecks in your Django project seem to lie in the template system and you have exhausted other opportunities to remedy this, a third-party alternative may be the answer.
Alternative template systems vary in the extent to which they share Django’s templating language.
Note
_If_ you experience performance issues in templates, the first thing to do is to understand exactly why. Using an alternative template system may prove faster, but the same gains may also be available without going to that trouble - for example, expensive processing and logic in your templates could be done more efficiently in your views.
### Alternative software implementations[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#alternative-software-implementations "Link to this heading")
It may be worth checking whether Python software you’re using has been provided in a different implementation that can execute the same code faster.
However: most performance problems in well-written Django sites aren’t at the Python execution level, but rather in inefficient database querying, caching, and templates. If you’re relying on poorly-written Python code, your performance problems are unlikely to be solved by having it execute faster.
Using an alternative implementation may introduce compatibility, deployment, portability, or maintenance issues. It goes without saying that before adopting a non-standard implementation you should ensure it provides sufficient performance gains for your application to outweigh the potential risks.
With these caveats in mind, you should be aware of:
#### [¶](https://docs.djangoproject.com/en/5.0/topics/performance/#id1 "Link to this heading")
A key aim of the PyPy project is
#### C implementations of Python libraries[¶](https://docs.djangoproject.com/en/5.0/topics/performance/#c-implementations-of-python-libraries "Link to this heading")
Some Python libraries are also implemented in C, and can be much faster. They aim to offer the same APIs. Note that compatibility issues and behavior differences are not unknown (and not always immediately evident).
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/security/)
[Serializing Django objects ](https://docs.djangoproject.com/en/5.0/topics/serialization/)
[](https://docs.djangoproject.com/en/5.0/topics/performance/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ arSensa Inc donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Performance and optimization](https://docs.djangoproject.com/en/5.0/topics/performance/)
    * [Introduction](https://docs.djangoproject.com/en/5.0/topics/performance/#introduction)
    * [General approaches](https://docs.djangoproject.com/en/5.0/topics/performance/#general-approaches)
      * [What are you optimizing _for_?](https://docs.djangoproject.com/en/5.0/topics/performance/#what-are-you-optimizing-for)
      * [Performance benchmarking](https://docs.djangoproject.com/en/5.0/topics/performance/#performance-benchmarking)
        * [Django tools](https://docs.djangoproject.com/en/5.0/topics/performance/#django-tools)
        * [Third-party services](https://docs.djangoproject.com/en/5.0/topics/performance/#third-party-services)
      * [Get things right from the start](https://docs.djangoproject.com/en/5.0/topics/performance/#get-things-right-from-the-start)
        * [Work at the appropriate level](https://docs.djangoproject.com/en/5.0/topics/performance/#work-at-the-appropriate-level)
    * [Caching](https://docs.djangoproject.com/en/5.0/topics/performance/#caching)
      * [The caching framework](https://docs.djangoproject.com/en/5.0/topics/performance/#the-caching-framework)
      * [`cached_property`](https://docs.djangoproject.com/en/5.0/topics/performance/#cached-property)
    * [Understanding laziness](https://docs.djangoproject.com/en/5.0/topics/performance/#understanding-laziness)
      * [Laziness in Django](https://docs.djangoproject.com/en/5.0/topics/performance/#laziness-in-django)
    * [Databases](https://docs.djangoproject.com/en/5.0/topics/performance/#databases)
      * [Database optimization](https://docs.djangoproject.com/en/5.0/topics/performance/#database-optimization)
      * [Other database-related tips](https://docs.djangoproject.com/en/5.0/topics/performance/#other-database-related-tips)
    * [HTTP performance](https://docs.djangoproject.com/en/5.0/topics/performance/#http-performance)
      * [Middleware](https://docs.djangoproject.com/en/5.0/topics/performance/#middleware)
        * [`ConditionalGetMiddleware`](https://docs.djangoproject.com/en/5.0/topics/performance/#conditionalgetmiddleware)
        * [`GZipMiddleware`](https://docs.djangoproject.com/en/5.0/topics/performance/#gzipmiddleware)
      * [Sessions](https://docs.djangoproject.com/en/5.0/topics/performance/#sessions)
        * [Using cached sessions](https://docs.djangoproject.com/en/5.0/topics/performance/#using-cached-sessions)
      * [Static files](https://docs.djangoproject.com/en/5.0/topics/performance/#static-files)
        * [`ManifestStaticFilesStorage`](https://docs.djangoproject.com/en/5.0/topics/performance/#manifeststaticfilesstorage)
        * [“Minification”](https://docs.djangoproject.com/en/5.0/topics/performance/#minification)
    * [Template performance](https://docs.djangoproject.com/en/5.0/topics/performance/#template-performance)
      * [The cached template loader](https://docs.djangoproject.com/en/5.0/topics/performance/#the-cached-template-loader)
    * [Using different versions of available software](https://docs.djangoproject.com/en/5.0/topics/performance/#using-different-versions-of-available-software)
      * [Newer is often - but not always - better](https://docs.djangoproject.com/en/5.0/topics/performance/#newer-is-often-but-not-always-better)
      * [Alternatives to Django’s template language](https://docs.djangoproject.com/en/5.0/topics/performance/#alternatives-to-django-s-template-language)
      * [Alternative software implementations](https://docs.djangoproject.com/en/5.0/topics/performance/#alternative-software-implementations)
        * [PyPy](https://docs.djangoproject.com/en/5.0/topics/performance/#id1)
        * [C implementations of Python libraries](https://docs.djangoproject.com/en/5.0/topics/performance/#c-implementations-of-python-libraries)


### Browse
  * Prev: [Security in Django](https://docs.djangoproject.com/en/5.0/topics/security/)
  * Next: [Serializing Django objects](https://docs.djangoproject.com/en/5.0/topics/serialization/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Performance and optimization


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
