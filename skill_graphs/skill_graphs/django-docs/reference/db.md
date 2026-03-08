This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/db/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/db/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/db/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/db/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/db/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/db/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/db/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/db/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/db/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/db/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/db/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/db/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/db/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/db/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/db/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/db/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/db/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/db/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/db/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/db/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/db/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/db/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/db/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/db/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/db/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/db/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/db/)


  * [](https://docs.djangoproject.com/en/5.0/topics/db/#top)


# Models and databases[¶](https://docs.djangoproject.com/en/5.0/topics/db/#module-django.db "Link to this heading")
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
  * [Models](https://docs.djangoproject.com/en/5.0/topics/db/models/)
  * [Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/)
  * [Aggregation](https://docs.djangoproject.com/en/5.0/topics/db/aggregation/)
  * [Search](https://docs.djangoproject.com/en/5.0/topics/db/search/)
  * [Managers](https://docs.djangoproject.com/en/5.0/topics/db/managers/)
  * [Performing raw SQL queries](https://docs.djangoproject.com/en/5.0/topics/db/sql/)
  * [Database transactions](https://docs.djangoproject.com/en/5.0/topics/db/transactions/)
  * [Multiple databases](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/)
  * [Tablespaces](https://docs.djangoproject.com/en/5.0/topics/db/tablespaces/)
  * [Database access optimization](https://docs.djangoproject.com/en/5.0/topics/db/optimization/)
  * [Database instrumentation](https://docs.djangoproject.com/en/5.0/topics/db/instrumentation/)
  * [Fixtures](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/)
  * [Examples of model relationship API usage](https://docs.djangoproject.com/en/5.0/topics/db/examples/)


Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/install/)
[Models ](https://docs.djangoproject.com/en/5.0/topics/db/models/)
[](https://docs.djangoproject.com/en/5.0/topics/db/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Hardball Law donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Models and databases](https://docs.djangoproject.com/en/5.0/topics/db/)


### Browse
  * Prev: [How to install Django](https://docs.djangoproject.com/en/5.0/topics/install/)
  * Next: [Models](https://docs.djangoproject.com/en/5.0/topics/db/models/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Models and databases


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
