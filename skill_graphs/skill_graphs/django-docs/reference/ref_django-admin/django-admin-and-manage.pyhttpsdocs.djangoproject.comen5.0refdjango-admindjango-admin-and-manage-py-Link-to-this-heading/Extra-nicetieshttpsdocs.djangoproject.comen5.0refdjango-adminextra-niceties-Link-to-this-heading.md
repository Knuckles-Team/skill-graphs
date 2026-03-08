## Extra niceties[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#extra-niceties "Link to this heading")
### Syntax coloring[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#syntax-coloring "Link to this heading")

DJANGO_COLORS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_COLORS "Link to this definition")

The `django-admin` / `manage.py` commands will use pretty color-coded output if your terminal supports ANSI-colored output. It won’t use the color codes if you’re piping the command’s output to another program unless the [`--force-color`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-force-color) option is used.
#### Windows support[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#windows-support "Link to this heading")
On Windows 10, the
Under Windows, the legacy `cmd.exe` native console doesn’t support ANSI escape sequences so by default there is no color output. In this case either of two third-party libraries are needed:
  * Install `colorama` can be installed via pip:
```
...\> py -m pip install "colorama >= 0.4.6"

```

  * Install `cmd.exe` to process ANSI color codes. Django commands will detect its presence and will make use of its services to color output just like on Unix-based platforms.


Other modern terminal environments on Windows, that support terminal colors, but which are not automatically detected as supported by Django, may “fake” the installation of `ANSICON` by setting the appropriate environmental variable, `ANSICON="on"`.
#### Custom colors[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#custom-colors "Link to this heading")
The colors used for syntax highlighting can be customized. Django ships with three color palettes:
  * `dark`, suited to terminals that show white text on a black background. This is the default palette.
  * `light`, suited to terminals that show black text on a white background.
  * `nocolor`, which disables syntax highlighting.


You select a palette by setting a [`DJANGO_COLORS`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_COLORS) environment variable to specify the palette you want to use. For example, to specify the `light` palette under a Unix or OS/X BASH shell, you would run the following at a command prompt:
```
export DJANGO_COLORS="light"

```

You can also customize the colors that are used. Django specifies a number of roles in which color is used:
  * `error` - A major error.
  * `notice` - A minor error.
  * `success` - A success.
  * `warning` - A warning.
  * `sql_field` - The name of a model field in SQL.
  * `sql_coltype` - The type of a model field in SQL.
  * `sql_keyword` - An SQL keyword.
  * `sql_table` - The name of a model in SQL.
  * `http_info` - A 1XX HTTP Informational server response.
  * `http_success` - A 2XX HTTP Success server response.
  * `http_not_modified` - A 304 HTTP Not Modified server response.
  * `http_redirect` - A 3XX HTTP Redirect server response other than 304.
  * `http_not_found` - A 404 HTTP Not Found server response.
  * `http_bad_request` - A 4XX HTTP Bad Request server response other than 404.
  * `http_server_error` - A 5XX HTTP Server Error response.
  * `migrate_heading` - A heading in a migrations management command.
  * `migrate_label` - A migration name.


Each of these roles can be assigned a specific foreground and background color, from the following list:
  * `black`
  * `red`
  * `green`
  * `yellow`
  * `blue`
  * `magenta`
  * `cyan`
  * `white`


Each of these colors can then be modified by using the following display options:
  * `bold`
  * `underscore`
  * `blink`
  * `reverse`
  * `conceal`


A color specification follows one of the following patterns:
  * `role=fg`
  * `role=fg/bg`
  * `role=fg,option,option`
  * `role=fg/bg,option,option`


where `role` is the name of a valid color role, `fg` is the foreground color, `bg` is the background color and each `option` is one of the color modifying options. Multiple color specifications are then separated by a semicolon. For example:
```
export DJANGO_COLORS="error=yellow/blue,blink;notice=magenta"

```

would specify that errors be displayed using blinking yellow on blue, and notices displayed using magenta. All other color roles would be left uncolored.
Colors can also be specified by extending a base palette. If you put a palette name in a color specification, all the colors implied by that palette will be loaded. So:
```
export DJANGO_COLORS="light;error=yellow/blue,blink;notice=magenta"

```

would specify the use of all the colors in the light color palette, _except_ for the colors for errors and notices which would be overridden as specified.
### Bash completion[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#bash-completion "Link to this heading")
If you use the Bash shell, consider installing the Django bash completion script, which lives in `django-admin` and `manage.py` commands, so you can, for instance…
  * Type `django-admin`.
  * Press [TAB] to see all available options.
  * Type `sql`, then [TAB], to see all available options whose names start with `sql`.


See [How to create custom django-admin commands](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/) for how to add customized actions.
### Black formatting[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#black-formatting "Link to this heading")
The Python files created by [`startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject), [`startapp`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startapp), [`optimizemigration`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-optimizemigration), [`makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations), and [`squashmigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-squashmigrations) are formatted using the `black` command if it is present on your `PATH`.
If you have `black` globally installed, but do not wish it used for the current project, you can set the `PATH` explicitly:
```
PATH=path/to/venv/bin django-admin makemigrations

```

For commands using `stdout` you can pipe the output to `black` if needed:
```
django-admin inspectdb | black -

```
