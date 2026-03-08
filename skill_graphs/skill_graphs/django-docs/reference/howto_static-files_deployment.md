This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/static-files/deployment/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/static-files/deployment/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/static-files/deployment/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/static-files/deployment/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/static-files/deployment/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/static-files/deployment/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/static-files/deployment/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/static-files/deployment/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/static-files/deployment/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/static-files/deployment/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/static-files/deployment/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/static-files/deployment/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/static-files/deployment/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/static-files/deployment/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/static-files/deployment/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/static-files/deployment/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/static-files/deployment/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/static-files/deployment/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/static-files/deployment/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/static-files/deployment/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/static-files/deployment/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/static-files/deployment/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/static-files/deployment/)


  * [](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#top)


# How to deploy static files[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#how-to-deploy-static-files "Link to this heading")
See also
For an introduction to the use of [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files."), see [How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/5.0/howto/static-files/).
## Serving static files in production[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#serving-static-files-in-production "Link to this heading")
The basic outline of putting static files into production consists of two steps: run the [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) command when static files change, then arrange for the collected static files directory ([`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT)) to be moved to the static file server and served. Depending the `staticfiles` [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) alias, files may need to be moved to a new location manually or the [`post_process`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.StaticFilesStorage.post_process "django.contrib.staticfiles.storage.StaticFilesStorage.post_process") method of the `Storage` class might take care of that.
As with all deployment tasks, the devil’s in the details. Every production setup will be a bit different, so you’ll need to adapt the basic outline to fit your needs. Below are a few common patterns that might help.
### Serving the site and your static files from the same server[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#serving-the-site-and-your-static-files-from-the-same-server "Link to this heading")
If you want to serve your static files from the same server that’s already serving your site, the process may look something like:
  * Push your code up to the deployment server.
  * On the server, run [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) to copy all the static files into [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT).
  * Configure your web server to serve the files in [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) under the URL [`STATIC_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_URL). For example, here’s [how to do this with Apache and mod_wsgi](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/modwsgi/#serving-files).


You’ll probably want to automate this process, especially if you’ve got multiple web servers.
### Serving static files from a dedicated server[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#serving-static-files-from-a-dedicated-server "Link to this heading")
Most larger Django sites use a separate web server – i.e., one that’s not also running Django – for serving static files. This server often runs a different type of web server – faster but less full-featured. Some common choices are:
  * A stripped-down version of


Configuring these servers is out of scope of this document; check each server’s respective documentation for instructions.
Since your static file server won’t be running Django, you’ll need to modify the deployment strategy to look something like:
  * When your static files change, run [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) locally.
  * Push your local [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) up to the static file server into the directory that’s being served.


### Serving static files from a cloud service or CDN[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#serving-static-files-from-a-cloud-service-or-cdn "Link to this heading")
Another common tactic is to serve static files from a cloud storage provider like Amazon’s S3 and/or a CDN (content delivery network). This lets you ignore the problems of serving static files and can often make for faster-loading web pages (especially when using a CDN).
When using these services, the basic workflow would look a bit like the above, except that instead of using `rsync` to transfer your static files to the server you’d need to transfer the static files to the storage provider or CDN.
There’s any number of ways you might do this, but if the provider has an API, you can use a [custom file storage backend](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/) to integrate the CDN with your Django project. If you’ve written or are using a 3rd party custom storage backend, you can tell [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) to use it by setting `staticfiles` in [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES).
For example, if you’ve written an S3 storage backend in `myproject.storage.S3Storage` you could use it with:
```
STORAGES = {
    # ...
    "staticfiles": {"BACKEND": "myproject.storage.S3Storage"}
}

```

Once that’s done, all you have to do is run [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) and your static files would be pushed through your storage package up to S3. If you later needed to switch to a different storage provider, you may only have to change `staticfiles` in the [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) setting.
For details on how you’d write one of these backends, see [How to write a custom storage class](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/). There are 3rd party apps available that provide storage backends for many common file storage APIs. A good starting point is the
Changed in Django 4.2:
The [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) setting was added.
## Learn more[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#learn-more "Link to this heading")
For complete details on all the settings, commands, template tags, and other pieces included in [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files."), see [the staticfiles reference](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/).
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/static-files/)
[How to install Django on Windows ](https://docs.djangoproject.com/en/5.0/howto/windows/)
[](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ José Sánchez Moreno donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to deploy static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/)
    * [Serving static files in production](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#serving-static-files-in-production)
      * [Serving the site and your static files from the same server](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#serving-the-site-and-your-static-files-from-the-same-server)
      * [Serving static files from a dedicated server](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#serving-static-files-from-a-dedicated-server)
      * [Serving static files from a cloud service or CDN](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#serving-static-files-from-a-cloud-service-or-cdn)
    * [Learn more](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#learn-more)


### Browse
  * Prev: [How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/5.0/howto/static-files/)
  * Next: [How to install Django on Windows](https://docs.djangoproject.com/en/5.0/howto/windows/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to deploy static files


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
