## Usage[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#usage "Link to this heading")
/ 
```
$ django-admin <command> [options]
$ manage.py <command> [options]
$ python -m django <command> [options]

```

```
...\> django-admin <command> [options]
...\> manage.py <command> [options]
...\> py -m django <command> [options]

```

`command` should be one of the commands listed in this document. `options`, which is optional, should be zero or more of the options available for the given command.
### Getting runtime help[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#getting-runtime-help "Link to this heading")

django-admin help[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-help "Link to this definition")

Run `django-admin help` to display usage information and a list of the commands provided by each application.
Run `django-admin help --commands` to display a list of all available commands.
Run `django-admin help <command>` to display a description of the given command and a list of its available options.
### App names[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#app-names "Link to this heading")
Many commands take a list of “app names.” An “app name” is the basename of the package containing your models. For example, if your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) contains the string `'mysite.blog'`, the app name is `blog`.
### Determining the version[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#determining-the-version "Link to this heading")

django-admin version[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-version "Link to this definition")

Run `django-admin version` to display the current Django version.
The output follows the schema described in
```
1.4.dev17026
1.4a1
1.4

```

### Displaying debug output[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#displaying-debug-output "Link to this heading")
Use [`--verbosity`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-verbosity), where it is supported, to specify the amount of notification and debug information that `django-admin` prints to the console.
