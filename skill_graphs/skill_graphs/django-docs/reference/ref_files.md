This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/files/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/files/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/files/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/files/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/files/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/files/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/files/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/files/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/files/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/files/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/files/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/files/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/files/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/files/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/files/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/files/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/files/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/files/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/files/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/files/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/files/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/files/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/files/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/files/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/files/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/files/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/files/)


  * [](https://docs.djangoproject.com/en/5.0/ref/files/#top)


# File handling[¶](https://docs.djangoproject.com/en/5.0/ref/files/#module-django.core.files "Link to this heading")
  * [The `File` object](https://docs.djangoproject.com/en/5.0/ref/files/file/)
    * [The `File` class](https://docs.djangoproject.com/en/5.0/ref/files/file/#the-file-class)
    * [The `ContentFile` class](https://docs.djangoproject.com/en/5.0/ref/files/file/#the-contentfile-class)
    * [The `ImageFile` class](https://docs.djangoproject.com/en/5.0/ref/files/file/#the-imagefile-class)
    * [Additional methods on files attached to objects](https://docs.djangoproject.com/en/5.0/ref/files/file/#additional-methods-on-files-attached-to-objects)
  * [File storage API](https://docs.djangoproject.com/en/5.0/ref/files/storage/)
    * [Getting the default storage class](https://docs.djangoproject.com/en/5.0/ref/files/storage/#getting-the-default-storage-class)
    * [The `FileSystemStorage` class](https://docs.djangoproject.com/en/5.0/ref/files/storage/#the-filesystemstorage-class)
    * [The `InMemoryStorage` class](https://docs.djangoproject.com/en/5.0/ref/files/storage/#the-inmemorystorage-class)
    * [The `Storage` class](https://docs.djangoproject.com/en/5.0/ref/files/storage/#the-storage-class)
  * [Uploaded Files and Upload Handlers](https://docs.djangoproject.com/en/5.0/ref/files/uploads/)
    * [Uploaded files](https://docs.djangoproject.com/en/5.0/ref/files/uploads/#uploaded-files)
    * [Built-in upload handlers](https://docs.djangoproject.com/en/5.0/ref/files/uploads/#module-django.core.files.uploadhandler)
    * [Writing custom upload handlers](https://docs.djangoproject.com/en/5.0/ref/files/uploads/#writing-custom-upload-handlers)


Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/exceptions/)
[The `File` object ](https://docs.djangoproject.com/en/5.0/ref/files/file/)
[](https://docs.djangoproject.com/en/5.0/ref/files/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Lee Semel donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [File handling](https://docs.djangoproject.com/en/5.0/ref/files/)


### Browse
  * Prev: [Django Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/)
  * Next: [The `File` object](https://docs.djangoproject.com/en/5.0/ref/files/file/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * File handling


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
