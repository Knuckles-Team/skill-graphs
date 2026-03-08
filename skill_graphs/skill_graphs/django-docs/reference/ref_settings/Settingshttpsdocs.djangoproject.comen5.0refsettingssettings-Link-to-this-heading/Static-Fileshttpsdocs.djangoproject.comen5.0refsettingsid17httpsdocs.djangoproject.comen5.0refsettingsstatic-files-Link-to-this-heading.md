##  [Static Files](https://docs.djangoproject.com/en/5.0/ref/settings/#id17)[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#static-files "Link to this heading")
Settings for [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.").
###  `STATIC_ROOT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#static-root "Link to this heading")
Default: `None`
The absolute path to the directory where [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) will collect static files for deployment.
Example: `"/var/www/example.com/static/"`
If the [staticfiles](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/) contrib app is enabled (as in the default project template), the [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command will collect static files into this directory. See the how-to on [managing static files](https://docs.djangoproject.com/en/5.0/howto/static-files/) for more details about usage.
Warning
This should be an initially empty destination directory for collecting your static files from their permanent locations into one directory for ease of deployment; it is **not** a place to store your static files permanently. You should do that in directories that will be found by [staticfiles](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/)’s [`finders`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_FINDERS), which by default, are `'static/'` app sub-directories and any directories you include in [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS)).
###  `STATIC_URL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#static-url "Link to this heading")
Default: `None`
URL to use when referring to static files located in [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT).
Example: `"static/"` or `"http://static.example.com/"`
If not `None`, this will be used as the base path for [asset definitions](https://docs.djangoproject.com/en/5.0/topics/forms/media/#form-asset-paths) (the `Media` class) and the [staticfiles app](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/).
It must end in a slash if set to a non-empty value.
You may need to [configure these files to be served in development](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-in-development) and will definitely need to do so [in production](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/).
Note
If [`STATIC_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_URL) is a relative path, then it will be prefixed by the server-provided value of `SCRIPT_NAME` (or `/` if not set). This makes it easier to serve a Django application in a subpath without adding an extra configuration to the settings.
###  `STATICFILES_DIRS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#staticfiles-dirs "Link to this heading")
Default: `[]` (Empty list)
This setting defines the additional locations the staticfiles app will traverse if the `FileSystemFinder` finder is enabled, e.g. if you use the [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) or [`findstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-findstatic) management command or use the static file serving view.
This should be set to a list of strings that contain full paths to your additional files directory(ies) e.g.:
```
STATICFILES_DIRS = [
    "/home/special.polls.com/polls/static",
    "/home/polls.com/polls/static",
    "/opt/webfiles/common",
]

```

Note that these paths should use Unix-style forward slashes, even on Windows (e.g. `"C:/Users/user/mysite/extra_static_content"`).
#### Prefixes (optional)[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#prefixes-optional "Link to this heading")
In case you want to refer to files in one of the locations with an additional namespace, you can **optionally** provide a prefix as `(prefix, path)` tuples, e.g.:
```
STATICFILES_DIRS = [
    # ...
    ("downloads", "/opt/webfiles/stats"),
]

```

For example, assuming you have [`STATIC_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_URL) set to `'static/'`, the [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command would collect the “stats” files in a `'downloads'` subdirectory of [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT).
This would allow you to refer to the local file `'/opt/webfiles/stats/polls_20101022.tar.gz'` with `'/static/downloads/polls_20101022.tar.gz'` in your templates, e.g.:
```
<a href="{% static 'downloads/polls_20101022.tar.gz' %}">

```

###  `STATICFILES_STORAGE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#staticfiles-storage "Link to this heading")
Default: `'django.contrib.staticfiles.storage.StaticFilesStorage'`
The file storage engine to use when collecting static files with the [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command.
A ready-to-use instance of the storage backend defined in this setting can be found under `staticfiles` key in `django.core.files.storage.storages`.
For an example, see [Serving static files from a cloud service or CDN](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#staticfiles-from-cdn).
Deprecated since version 4.2: This setting is deprecated. Starting with Django 4.2, static files storage engine can be configured with the [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) setting under the `staticfiles` key.
###  `STATICFILES_FINDERS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#staticfiles-finders "Link to this heading")
Default:
```
[
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

```

The list of finder backends that know how to find static files in various locations.
The default will find files stored in the [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS) setting (using `django.contrib.staticfiles.finders.FileSystemFinder`) and in a `static` subdirectory of each app (using `django.contrib.staticfiles.finders.AppDirectoriesFinder`). If multiple files with the same name are present, the first file that is found will be used.
One finder is disabled by default: `django.contrib.staticfiles.finders.DefaultStorageFinder`. If added to your [`STATICFILES_FINDERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_FINDERS) setting, it will look for static files in the default file storage as defined by the `default` key in the [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) setting.
Note
When using the `AppDirectoriesFinder` finder, make sure your apps can be found by staticfiles by adding the app to the [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) setting of your site.
Static file finders are currently considered a private interface, and this interface is thus undocumented.
