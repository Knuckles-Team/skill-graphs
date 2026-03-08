# Running management commands from your code[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#running-management-commands-from-your-code "Link to this heading")

django.core.management.call_command(_name_ , _* args_, _** options_)[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django.core.management.call_command "Link to this definition")

To call a management command from code use `call_command()`.

`name`

the name of the command to call or a command object. Passing the name is preferred unless the object is required for testing.

`*args`

a list of arguments accepted by the command. Arguments are passed to the argument parser, so you can use the same style as you would on the command line. For example, `call_command('flush', '--verbosity=0')`.

`**options`

named options accepted on the command-line. Options are passed to the command without triggering the argument parser, which means you’ll need to pass the correct type. For example, `call_command('flush', verbosity=0)` (zero must be an integer rather than a string).
Examples:
```
from django.core import management
from django.core.management.commands import loaddata

management.call_command("flush", verbosity=0, interactive=False)
management.call_command("loaddata", "test_data", verbosity=0)
management.call_command(loaddata.Command(), "test_data", verbosity=0)

```

Note that command options that take no arguments are passed as keywords with `True` or `False`, as you can see with the `interactive` option above.
Named arguments can be passed by using either one of the following syntaxes:
```
# Similar to the command line
management.call_command("dumpdata", "--natural-foreign")

# Named argument similar to the command line minus the initial dashes and
# with internal dashes replaced by underscores
management.call_command("dumpdata", natural_foreign=True)

# `use_natural_foreign_keys` is the option destination variable
management.call_command("dumpdata", use_natural_foreign_keys=True)

```

Some command options have different names when using `call_command()` instead of `django-admin` or `manage.py`. For example, `django-admin createsuperuser --no-input` translates to `call_command('createsuperuser', interactive=False)`. To find what keyword argument name to use for `call_command()`, check the command’s source code for the `dest` argument passed to `parser.add_argument()`.
Command options which take multiple options are passed a list:
```
management.call_command("dumpdata", exclude=["contenttypes", "auth"])

```

The return value of the `call_command()` function is the same as the return value of the `handle()` method of the command.
