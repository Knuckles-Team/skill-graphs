This document is for Django's development version, which can be significantly different from previous releases. For older releases, use the version selector floating in the bottom right corner of this page.
[Skip to main content](https://docs.djangoproject.com/en/dev/#main-content)
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
[Documentation](https://docs.djangoproject.com/en/dev/)
  * [ Getting Help ](https://docs.djangoproject.com/en/dev/faq/help/)


  * Language: **en**


  * Documentation version: **development**
  * [6.0](https://docs.djangoproject.com/en/6.0/)
  * [5.2](https://docs.djangoproject.com/en/5.2/)
  * [5.1](https://docs.djangoproject.com/en/5.1/)
  * [5.0](https://docs.djangoproject.com/en/5.0/)
  * [4.2](https://docs.djangoproject.com/en/4.2/)
  * [4.1](https://docs.djangoproject.com/en/4.1/)
  * [4.0](https://docs.djangoproject.com/en/4.0/)
  * [3.2](https://docs.djangoproject.com/en/3.2/)
  * [3.1](https://docs.djangoproject.com/en/3.1/)
  * [3.0](https://docs.djangoproject.com/en/3.0/)
  * [2.2](https://docs.djangoproject.com/en/2.2/)
  * [2.1](https://docs.djangoproject.com/en/2.1/)
  * [2.0](https://docs.djangoproject.com/en/2.0/)
  * [1.11](https://docs.djangoproject.com/en/1.11/)
  * [1.10](https://docs.djangoproject.com/en/1.10/)
  * [1.8](https://docs.djangoproject.com/en/1.8/)


  * [](https://docs.djangoproject.com/en/dev/#top)


# Django documentation[¶](https://docs.djangoproject.com/en/dev/#django-documentation "Link to this heading")
Everything you need to know about Django.
## First steps[¶](https://docs.djangoproject.com/en/dev/#first-steps "Link to this heading")
Are you new to Django or to programming? This is the place to start!
  * **From scratch:** [Overview](https://docs.djangoproject.com/en/dev/intro/overview/) | [Installation](https://docs.djangoproject.com/en/dev/intro/install/)
  * **Tutorial:** [Part 1: Requests and responses](https://docs.djangoproject.com/en/dev/intro/tutorial01/) | [Part 2: Models and the admin site](https://docs.djangoproject.com/en/dev/intro/tutorial02/) | [Part 3: Views and templates](https://docs.djangoproject.com/en/dev/intro/tutorial03/) | [Part 4: Forms and generic views](https://docs.djangoproject.com/en/dev/intro/tutorial04/) | [Part 5: Testing](https://docs.djangoproject.com/en/dev/intro/tutorial05/) | [Part 6: Static files](https://docs.djangoproject.com/en/dev/intro/tutorial06/) | [Part 7: Customizing the admin site](https://docs.djangoproject.com/en/dev/intro/tutorial07/) | [Part 8: Adding third-party packages](https://docs.djangoproject.com/en/dev/intro/tutorial08/)
  * **Advanced Tutorials:** [How to write reusable apps](https://docs.djangoproject.com/en/dev/intro/reusable-apps/) | [Writing your first contribution to Django](https://docs.djangoproject.com/en/dev/intro/contributing/)


## Getting help[¶](https://docs.djangoproject.com/en/dev/#getting-help "Link to this heading")
Having trouble? We’d like to help!
  * Try the [FAQ](https://docs.djangoproject.com/en/dev/faq/) – it’s got answers to many common questions.
  * Looking for specific information? Try the [Index](https://docs.djangoproject.com/en/dev/genindex/), [Module Index](https://docs.djangoproject.com/en/dev/py-modindex/) or the [detailed table of contents](https://docs.djangoproject.com/en/dev/contents/).
  * Not found anything? See [FAQ: Getting Help](https://docs.djangoproject.com/en/dev/faq/help/) for information on getting support and asking questions to the community.
  * Report bugs with Django in our [ticket tracker](https://code.djangoproject.com/).


## How the documentation is organized[¶](https://docs.djangoproject.com/en/dev/#how-the-documentation-is-organized "Link to this heading")
Django has a lot of documentation. A high-level overview of how it’s organized will help you know where to look for certain things:
  * [Tutorials](https://docs.djangoproject.com/en/dev/intro/) take you by the hand through a series of steps to create a web application. Start here if you’re new to Django or web application development. Also look at the “[First steps](https://docs.djangoproject.com/en/dev/#index-first-steps)”.
  * [Topic guides](https://docs.djangoproject.com/en/dev/topics/) discuss key topics and concepts at a fairly high level and provide useful background information and explanation.
  * [Reference guides](https://docs.djangoproject.com/en/dev/ref/) contain technical reference for APIs and other aspects of Django’s machinery. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.
  * [How-to guides](https://docs.djangoproject.com/en/dev/howto/) are recipes. They guide you through the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume some knowledge of how Django works.


## The model layer[¶](https://docs.djangoproject.com/en/dev/#the-model-layer "Link to this heading")
Django provides an abstraction layer (the “models”) for structuring and manipulating the data of your web application. Learn more about it below:
  * **Models:** [Introduction to models](https://docs.djangoproject.com/en/dev/topics/db/models/) | [Field types](https://docs.djangoproject.com/en/dev/ref/models/fields/) | [Indexes](https://docs.djangoproject.com/en/dev/ref/models/indexes/) | [Meta options](https://docs.djangoproject.com/en/dev/ref/models/options/) | [Model class](https://docs.djangoproject.com/en/dev/ref/models/class/)
  * **QuerySets:** [Making queries](https://docs.djangoproject.com/en/dev/topics/db/queries/) | [QuerySet method reference](https://docs.djangoproject.com/en/dev/ref/models/querysets/) | [Lookup expressions](https://docs.djangoproject.com/en/dev/ref/models/lookups/)
  * **Model instances:** [Instance methods](https://docs.djangoproject.com/en/dev/ref/models/instances/) | [Accessing related objects](https://docs.djangoproject.com/en/dev/ref/models/relations/)
  * **Migrations:** [Introduction to Migrations](https://docs.djangoproject.com/en/dev/topics/migrations/) | [Operations reference](https://docs.djangoproject.com/en/dev/ref/migration-operations/) | [SchemaEditor](https://docs.djangoproject.com/en/dev/ref/schema-editor/) | [Writing migrations](https://docs.djangoproject.com/en/dev/howto/writing-migrations/)
  * **Advanced:** [Managers](https://docs.djangoproject.com/en/dev/topics/db/managers/) | [Raw SQL](https://docs.djangoproject.com/en/dev/topics/db/sql/) | [Transactions](https://docs.djangoproject.com/en/dev/topics/db/transactions/) | [Aggregation](https://docs.djangoproject.com/en/dev/topics/db/aggregation/) | [Search](https://docs.djangoproject.com/en/dev/topics/db/search/) | [Custom fields](https://docs.djangoproject.com/en/dev/howto/custom-model-fields/) | [Multiple databases](https://docs.djangoproject.com/en/dev/topics/db/multi-db/) | [Custom lookups](https://docs.djangoproject.com/en/dev/howto/custom-lookups/) | [Query Expressions](https://docs.djangoproject.com/en/dev/ref/models/expressions/) | [Conditional Expressions](https://docs.djangoproject.com/en/dev/ref/models/conditional-expressions/) | [Database Functions](https://docs.djangoproject.com/en/dev/ref/models/database-functions/)
  * **Other:** [Supported databases](https://docs.djangoproject.com/en/dev/ref/databases/) | [Legacy databases](https://docs.djangoproject.com/en/dev/howto/legacy-databases/) | [Providing initial data](https://docs.djangoproject.com/en/dev/howto/initial-data/) | [Optimize database access](https://docs.djangoproject.com/en/dev/topics/db/optimization/) | [PostgreSQL specific features](https://docs.djangoproject.com/en/dev/ref/contrib/postgres/)


## The view layer[¶](https://docs.djangoproject.com/en/dev/#the-view-layer "Link to this heading")
Django has the concept of “views” to encapsulate the logic responsible for processing a user’s request and for returning the response. Find all you need to know about views via the links below:
  * **The basics:** [URLconfs](https://docs.djangoproject.com/en/dev/topics/http/urls/) | [View functions](https://docs.djangoproject.com/en/dev/topics/http/views/) | [Shortcuts](https://docs.djangoproject.com/en/dev/topics/http/shortcuts/) | [Decorators](https://docs.djangoproject.com/en/dev/topics/http/decorators/) | [Asynchronous Support](https://docs.djangoproject.com/en/dev/topics/async/)
  * **Reference:** [Built-in Views](https://docs.djangoproject.com/en/dev/ref/views/) | [Request/response objects](https://docs.djangoproject.com/en/dev/ref/request-response/) | [TemplateResponse objects](https://docs.djangoproject.com/en/dev/ref/template-response/)
  * **File uploads:** [Overview](https://docs.djangoproject.com/en/dev/topics/http/file-uploads/) | [File objects](https://docs.djangoproject.com/en/dev/ref/files/file/) | [Storage API](https://docs.djangoproject.com/en/dev/ref/files/storage/) | [Managing files](https://docs.djangoproject.com/en/dev/topics/files/) | [Custom storage](https://docs.djangoproject.com/en/dev/howto/custom-file-storage/)
  * **Class-based views:** [Overview](https://docs.djangoproject.com/en/dev/topics/class-based-views/) | [Built-in display views](https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-display/) | [Built-in editing views](https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/) | [Using mixins](https://docs.djangoproject.com/en/dev/topics/class-based-views/mixins/) | [API reference](https://docs.djangoproject.com/en/dev/ref/class-based-views/) | [Flattened index](https://docs.djangoproject.com/en/dev/ref/class-based-views/flattened-index/)
  * **Advanced:** [Generating CSV](https://docs.djangoproject.com/en/dev/howto/outputting-csv/) | [Generating PDF](https://docs.djangoproject.com/en/dev/howto/outputting-pdf/)
  * **Middleware:** [Overview](https://docs.djangoproject.com/en/dev/topics/http/middleware/) | [Built-in middleware classes](https://docs.djangoproject.com/en/dev/ref/middleware/)


## The template layer[¶](https://docs.djangoproject.com/en/dev/#the-template-layer "Link to this heading")
The template layer provides a designer-friendly syntax for rendering the information to be presented to the user. Learn how this syntax can be used by designers and how it can be extended by programmers:
  * **The basics:** [Overview](https://docs.djangoproject.com/en/dev/topics/templates/)
  * **For designers:** [Language overview](https://docs.djangoproject.com/en/dev/ref/templates/language/) | [Built-in tags and filters](https://docs.djangoproject.com/en/dev/ref/templates/builtins/) | [Humanization](https://docs.djangoproject.com/en/dev/ref/contrib/humanize/)
  * **For programmers:** [Template API](https://docs.djangoproject.com/en/dev/ref/templates/api/) | [Custom tags and filters](https://docs.djangoproject.com/en/dev/howto/custom-template-tags/) | [Custom template backend](https://docs.djangoproject.com/en/dev/howto/custom-template-backend/)


## Forms[¶](https://docs.djangoproject.com/en/dev/#forms "Link to this heading")
Django provides a rich framework to facilitate the creation of forms and the manipulation of form data.
  * **The basics:** [Overview](https://docs.djangoproject.com/en/dev/topics/forms/) | [Form API](https://docs.djangoproject.com/en/dev/ref/forms/api/) | [Built-in fields](https://docs.djangoproject.com/en/dev/ref/forms/fields/) | [Built-in widgets](https://docs.djangoproject.com/en/dev/ref/forms/widgets/)
  * **Advanced:** [Forms for models](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/) | [Integrating media](https://docs.djangoproject.com/en/dev/topics/forms/media/) | [Formsets](https://docs.djangoproject.com/en/dev/topics/forms/formsets/) | [Customizing validation](https://docs.djangoproject.com/en/dev/ref/forms/validation/)


## The development process[¶](https://docs.djangoproject.com/en/dev/#the-development-process "Link to this heading")
Learn about the various components and tools to help you in the development and testing of Django applications:
  * **Settings:** [Overview](https://docs.djangoproject.com/en/dev/topics/settings/) | [Full list of settings](https://docs.djangoproject.com/en/dev/ref/settings/)
  * **Applications:** [Overview](https://docs.djangoproject.com/en/dev/ref/applications/)
  * **Exceptions:** [Overview](https://docs.djangoproject.com/en/dev/ref/exceptions/)
  * **django-admin and manage.py:** [Overview](https://docs.djangoproject.com/en/dev/ref/django-admin/) | [Adding custom commands](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)
  * **Testing:** [Introduction](https://docs.djangoproject.com/en/dev/topics/testing/) | [Writing and running tests](https://docs.djangoproject.com/en/dev/topics/testing/overview/) | [Included testing tools](https://docs.djangoproject.com/en/dev/topics/testing/tools/) | [Advanced topics](https://docs.djangoproject.com/en/dev/topics/testing/advanced/)
  * **Deployment:** [Overview](https://docs.djangoproject.com/en/dev/howto/deployment/) | [WSGI servers](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/) | [ASGI servers](https://docs.djangoproject.com/en/dev/howto/deployment/asgi/) | [Deploying static files](https://docs.djangoproject.com/en/dev/howto/static-files/deployment/) | [Tracking code errors by email](https://docs.djangoproject.com/en/dev/howto/error-reporting/) | [Deployment checklist](https://docs.djangoproject.com/en/dev/howto/deployment/checklist/)


## The admin[¶](https://docs.djangoproject.com/en/dev/#the-admin "Link to this heading")
Find all you need to know about the automated admin interface, one of Django’s most popular features:
  * [Admin site](https://docs.djangoproject.com/en/dev/ref/contrib/admin/)
  * [Admin actions](https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/)
  * [Admin documentation generator](https://docs.djangoproject.com/en/dev/ref/contrib/admin/admindocs/)


## Security[¶](https://docs.djangoproject.com/en/dev/#security "Link to this heading")
Security is a topic of paramount importance in the development of web applications and Django provides multiple protection tools and mechanisms:
  * [Security overview](https://docs.djangoproject.com/en/dev/topics/security/)
  * [Disclosed security issues in Django](https://docs.djangoproject.com/en/dev/releases/security/)
  * [Clickjacking protection](https://docs.djangoproject.com/en/dev/ref/clickjacking/)
  * [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/dev/ref/csrf/)
  * [Cryptographic signing](https://docs.djangoproject.com/en/dev/topics/signing/)
  * [Security Middleware](https://docs.djangoproject.com/en/dev/ref/middleware/#security-middleware)
  * [Content Security Policy](https://docs.djangoproject.com/en/dev/ref/csp/)


## Internationalization and localization[¶](https://docs.djangoproject.com/en/dev/#internationalization-and-localization "Link to this heading")
Django offers a robust internationalization and localization framework to assist you in the development of applications for multiple languages and world regions:
  * [Overview](https://docs.djangoproject.com/en/dev/topics/i18n/) | [Internationalization](https://docs.djangoproject.com/en/dev/topics/i18n/translation/) | [Localization](https://docs.djangoproject.com/en/dev/topics/i18n/translation/#how-to-create-language-files) | [Localized web UI formatting and form input](https://docs.djangoproject.com/en/dev/topics/i18n/formatting/)
  * [Time zones](https://docs.djangoproject.com/en/dev/topics/i18n/timezones/)


## Performance and optimization[¶](https://docs.djangoproject.com/en/dev/#performance-and-optimization "Link to this heading")
There are a variety of techniques and tools that can help get your code running more efficiently - faster, and using fewer system resources.
  * [Performance and optimization overview](https://docs.djangoproject.com/en/dev/topics/performance/)


## Geographic framework[¶](https://docs.djangoproject.com/en/dev/#geographic-framework "Link to this heading")
[GeoDjango](https://docs.djangoproject.com/en/dev/ref/contrib/gis/) intends to be a world-class geographic web framework. Its goal is to make it as easy as possible to build GIS web applications and harness the power of spatially enabled data.
## Common web application tools[¶](https://docs.djangoproject.com/en/dev/#common-web-application-tools "Link to this heading")
Django offers multiple tools commonly needed in the development of web applications:
  * **Authentication:** [Overview](https://docs.djangoproject.com/en/dev/topics/auth/) | [Using the authentication system](https://docs.djangoproject.com/en/dev/topics/auth/default/) | [Password management](https://docs.djangoproject.com/en/dev/topics/auth/passwords/) | [Customizing authentication](https://docs.djangoproject.com/en/dev/topics/auth/customizing/) | [API Reference](https://docs.djangoproject.com/en/dev/ref/contrib/auth/)
  * [Caching](https://docs.djangoproject.com/en/dev/topics/cache/)
  * [Logging](https://docs.djangoproject.com/en/dev/topics/logging/)
  * [Tasks framework](https://docs.djangoproject.com/en/dev/topics/tasks/)
  * [Sending emails](https://docs.djangoproject.com/en/dev/topics/email/)
  * [Syndication feeds (RSS/Atom)](https://docs.djangoproject.com/en/dev/ref/contrib/syndication/)
  * [Pagination](https://docs.djangoproject.com/en/dev/topics/pagination/)
  * [Messages framework](https://docs.djangoproject.com/en/dev/ref/contrib/messages/)
  * [Serialization](https://docs.djangoproject.com/en/dev/topics/serialization/)
  * [Sessions](https://docs.djangoproject.com/en/dev/topics/http/sessions/)
  * [Sitemaps](https://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/)
  * [Static files management](https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/)
  * [Data validation](https://docs.djangoproject.com/en/dev/ref/validators/)


## Other core functionalities[¶](https://docs.djangoproject.com/en/dev/#other-core-functionalities "Link to this heading")
Learn about some other core functionalities of the Django framework:
  * [Conditional content processing](https://docs.djangoproject.com/en/dev/topics/conditional-view-processing/)
  * [Content types and generic relations](https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/)
  * [Flatpages](https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/)
  * [Redirects](https://docs.djangoproject.com/en/dev/ref/contrib/redirects/)
  * [Signals](https://docs.djangoproject.com/en/dev/topics/signals/)
  * [System check framework](https://docs.djangoproject.com/en/dev/topics/checks/)
  * [The sites framework](https://docs.djangoproject.com/en/dev/ref/contrib/sites/)
  * [Unicode in Django](https://docs.djangoproject.com/en/dev/ref/unicode/)


## The Django open-source project[¶](https://docs.djangoproject.com/en/dev/#the-django-open-source-project "Link to this heading")
Learn about the development process for the Django project itself and about how you can contribute:
  * **Community:** [Contributing to Django](https://docs.djangoproject.com/en/dev/internals/contributing/) | [The release process](https://docs.djangoproject.com/en/dev/internals/release-process/) | [Team organization](https://docs.djangoproject.com/en/dev/internals/organization/) | [The Django source code repository](https://docs.djangoproject.com/en/dev/internals/git/) | [Security policies](https://docs.djangoproject.com/en/dev/internals/security/) | [Mailing lists and Forum](https://docs.djangoproject.com/en/dev/internals/mailing-lists/)
  * **Design philosophies:** [Overview](https://docs.djangoproject.com/en/dev/misc/design-philosophies/)
  * **Documentation:** [About this documentation](https://docs.djangoproject.com/en/dev/internals/contributing/writing-documentation/)
  * **Third-party distributions:** [Overview](https://docs.djangoproject.com/en/dev/misc/distributions/)
  * **Django over time:** [API stability](https://docs.djangoproject.com/en/dev/misc/api-stability/) | [Release notes and upgrading instructions](https://docs.djangoproject.com/en/dev/releases/) | [Deprecation Timeline](https://docs.djangoproject.com/en/dev/internals/deprecation/)

Previous page and next page
[](https://docs.djangoproject.com/en/dev/contents/)
[Getting started ](https://docs.djangoproject.com/en/dev/intro/)
[](https://docs.djangoproject.com/en/dev/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ gitaarik donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Browse
  * Prev: [Django documentation contents](https://docs.djangoproject.com/en/dev/contents/)
  * Next: [Getting started](https://docs.djangoproject.com/en/dev/intro/)
  * [Table of contents](https://docs.djangoproject.com/en/dev/contents/)
  * [General Index](https://docs.djangoproject.com/en/dev/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/dev/py-modindex/)


### You are here:
  * [Django dev documentation](https://docs.djangoproject.com/en/dev/)
    * Django documentation


### Getting help

[FAQ](https://docs.djangoproject.com/en/dev/faq/)
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
Offline (development version): [HTML](https://media.djangoproject.com/docs/django-docs-dev-en.zip) |
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
