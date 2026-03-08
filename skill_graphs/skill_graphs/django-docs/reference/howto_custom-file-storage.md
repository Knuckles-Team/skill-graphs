This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/custom-file-storage/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/custom-file-storage/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/custom-file-storage/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/custom-file-storage/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/custom-file-storage/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/custom-file-storage/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/custom-file-storage/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/custom-file-storage/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/custom-file-storage/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/custom-file-storage/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/custom-file-storage/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/custom-file-storage/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/custom-file-storage/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/custom-file-storage/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/custom-file-storage/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/custom-file-storage/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/custom-file-storage/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/custom-file-storage/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/custom-file-storage/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/custom-file-storage/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/custom-file-storage/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/custom-file-storage/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/custom-file-storage/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/custom-file-storage/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/custom-file-storage/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/custom-file-storage/)


  * [](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#top)


# How to write a custom storage class[¶](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#how-to-write-a-custom-storage-class "Link to this heading")
If you need to provide custom file storage – a common example is storing files on some remote system – you can do so by defining a custom storage class. You’ll need to follow these steps:
  1. Your custom storage system must be a subclass of `django.core.files.storage.Storage`:
```
from django.core.files.storage import Storage


class MyStorage(Storage): ...

```

  2. Django must be able to instantiate your storage system without any arguments. This means that any settings should be taken from `django.conf.settings`:
```
from django.conf import settings
from django.core.files.storage import Storage


class MyStorage(Storage):
    def __init__(self, option=None):
        if not option:
            option = settings.CUSTOM_STORAGE_OPTIONS
        ...

```

  3. Your storage class must implement the [`_open()`](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#django.core.files.storage._open "django.core.files.storage._open") and [`_save()`](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#django.core.files.storage._save "django.core.files.storage._save") methods, along with any other methods appropriate to your storage class. See below for more on these methods.
In addition, if your class provides local file storage, it must override the `path()` method.
  4. Your storage class must be [deconstructible](https://docs.djangoproject.com/en/5.0/topics/migrations/#custom-deconstruct-method) so it can be serialized when it’s used on a field in a migration. As long as your field has arguments that are themselves [serializable](https://docs.djangoproject.com/en/5.0/topics/migrations/#migration-serializing), you can use the `django.utils.deconstruct.deconstructible` class decorator for this (that’s what Django uses on FileSystemStorage).


By default, the following methods raise `NotImplementedError` and will typically have to be overridden:
  * [`Storage.delete()`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.Storage.delete "django.core.files.storage.Storage.delete")
  * [`Storage.exists()`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.Storage.exists "django.core.files.storage.Storage.exists")
  * [`Storage.listdir()`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.Storage.listdir "django.core.files.storage.Storage.listdir")
  * [`Storage.size()`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.Storage.size "django.core.files.storage.Storage.size")
  * [`Storage.url()`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.Storage.url "django.core.files.storage.Storage.url")


Note however that not all these methods are required and may be deliberately omitted. As it happens, it is possible to leave each method unimplemented and still have a working Storage.
By way of example, if listing the contents of certain storage backends turns out to be expensive, you might decide not to implement `Storage.listdir()`.
Another example would be a backend that only handles writing to files. In this case, you would not need to implement any of the above methods.
Ultimately, which of these methods are implemented is up to you. Leaving some methods unimplemented will result in a partial (possibly broken) interface.
You’ll also usually want to use hooks specifically designed for custom storage objects. These are:

_open(_name_ , _mode ='rb'_)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#django.core.files.storage._open "Link to this definition")

**Required**.
Called by `Storage.open()`, this is the actual mechanism the storage class uses to open the file. This must return a `File` object, though in most cases, you’ll want to return some subclass here that implements logic specific to the backend storage system. The

_save(_name_ , _content_)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#django.core.files.storage._save "Link to this definition")

Called by `Storage.save()`. The `name` will already have gone through `get_valid_name()` and `get_available_name()`, and the `content` will be a `File` object itself.
Should return the actual name of the file saved (usually the `name` passed in, but if the storage needs to change the file name return the new name instead).

get_valid_name(_name_)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#django.core.files.storage.get_valid_name "Link to this definition")

Returns a filename suitable for use with the underlying storage system. The `name` argument passed to this method is either the original filename sent to the server or, if `upload_to` is a callable, the filename returned by that method after any path information is removed. Override this to customize how non-standard characters are converted to safe filenames.
The code provided on `Storage` retains only alpha-numeric characters, periods and underscores from the original filename, removing everything else.

get_alternative_name(_file_root_ , _file_ext_)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#django.core.files.storage.get_alternative_name "Link to this definition")

Returns an alternative filename based on the `file_root` and `file_ext` parameters. By default, an underscore plus a random 7 character alphanumeric string is appended to the filename before the extension.

get_available_name(_name_ , _max_length =None_)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#django.core.files.storage.get_available_name "Link to this definition")

Returns a filename that is available in the storage mechanism, possibly taking the provided filename into account. The `name` argument passed to this method will have already cleaned to a filename valid for the storage system, according to the `get_valid_name()` method described above.
The length of the filename will not exceed `max_length`, if provided. If a free unique filename cannot be found, a [`SuspiciousFileOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") exception is raised.
If a file with `name` already exists, `get_alternative_name()` is called to obtain an alternative name.
## Use your custom storage engine[¶](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#use-your-custom-storage-engine "Link to this heading")
New in Django 4.2.
The first step to using your custom storage with Django is to tell Django about the file storage backend you’ll be using. This is done using the [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) setting. This setting maps storage aliases, which are a way to refer to a specific storage throughout Django, to a dictionary of settings for that specific storage backend. The settings in the inner dictionaries are described fully in the [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) documentation.
Storages are then accessed by alias from the [`django.core.files.storage.storages`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.storages "django.core.files.storage.storages") dictionary:
```
from django.core.files.storage import storages

example_storage = storages["example"]

```

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/)
[How to deploy Django ](https://docs.djangoproject.com/en/5.0/howto/deployment/)
[](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Om Prakash Sharma donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to write a custom storage class](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/)
    * [Use your custom storage engine](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/#use-your-custom-storage-engine)


### Browse
  * Prev: [How to create custom template tags and filters](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/)
  * Next: [How to deploy Django](https://docs.djangoproject.com/en/5.0/howto/deployment/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to write a custom storage class


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
