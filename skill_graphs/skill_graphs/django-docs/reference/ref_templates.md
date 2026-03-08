This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/templates/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/templates/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/templates/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/templates/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/templates/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/templates/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/templates/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/templates/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/templates/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/templates/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/templates/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/templates/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/templates/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/templates/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/templates/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/templates/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/templates/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/templates/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/templates/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/templates/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/templates/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/templates/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/templates/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/templates/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/templates/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/templates/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/templates/)


  * [](https://docs.djangoproject.com/en/5.0/ref/templates/#top)


# Templates[¶](https://docs.djangoproject.com/en/5.0/ref/templates/#templates "Link to this heading")
Django’s template engine provides a powerful mini-language for defining the user-facing layer of your application, encouraging a clean separation of application and presentation logic. Templates can be maintained by anyone with an understanding of HTML; no knowledge of Python is required. For introductory material, see [Templates](https://docs.djangoproject.com/en/5.0/topics/templates/) topic guide.
  * [The Django template language](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
    * [Templates](https://docs.djangoproject.com/en/5.0/ref/templates/language/#templates)
    * [Variables](https://docs.djangoproject.com/en/5.0/ref/templates/language/#variables)
    * [Filters](https://docs.djangoproject.com/en/5.0/ref/templates/language/#filters)
    * [Tags](https://docs.djangoproject.com/en/5.0/ref/templates/language/#tags)
    * [Comments](https://docs.djangoproject.com/en/5.0/ref/templates/language/#comments)
    * [Template inheritance](https://docs.djangoproject.com/en/5.0/ref/templates/language/#template-inheritance)
    * [Automatic HTML escaping](https://docs.djangoproject.com/en/5.0/ref/templates/language/#automatic-html-escaping)
    * [Accessing method calls](https://docs.djangoproject.com/en/5.0/ref/templates/language/#accessing-method-calls)
    * [Custom tag and filter libraries](https://docs.djangoproject.com/en/5.0/ref/templates/language/#custom-tag-and-filter-libraries)
  * [Built-in template tags and filters](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)
    * [Built-in tag reference](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#built-in-tag-reference)
    * [Built-in filter reference](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#built-in-filter-reference)
    * [Internationalization tags and filters](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#internationalization-tags-and-filters)
    * [Other tags and filters libraries](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#other-tags-and-filters-libraries)
  * [The Django template language: for Python programmers](https://docs.djangoproject.com/en/5.0/ref/templates/api/)
    * [Overview](https://docs.djangoproject.com/en/5.0/ref/templates/api/#overview)
    * [Configuring an engine](https://docs.djangoproject.com/en/5.0/ref/templates/api/#configuring-an-engine)
    * [Loading a template](https://docs.djangoproject.com/en/5.0/ref/templates/api/#loading-a-template)
    * [Rendering a context](https://docs.djangoproject.com/en/5.0/ref/templates/api/#rendering-a-context)
    * [Playing with `Context` objects](https://docs.djangoproject.com/en/5.0/ref/templates/api/#playing-with-context-objects)
    * [Loading templates](https://docs.djangoproject.com/en/5.0/ref/templates/api/#loading-templates)
    * [Custom loaders](https://docs.djangoproject.com/en/5.0/ref/templates/api/#custom-loaders)
    * [Template origin](https://docs.djangoproject.com/en/5.0/ref/templates/api/#template-origin)


See also
For information on writing your own custom tags and filters, see [How to create custom template tags and filters](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/).
To learn how to override templates in other Django applications, see [How to override templates](https://docs.djangoproject.com/en/5.0/howto/overriding-templates/).
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/signals/)
[The Django template language ](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
[](https://docs.djangoproject.com/en/5.0/ref/templates/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ BlockRun Inc. donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Templates](https://docs.djangoproject.com/en/5.0/ref/templates/)


### Browse
  * Prev: [Signals](https://docs.djangoproject.com/en/5.0/ref/signals/)
  * Next: [The Django template language](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Templates


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
