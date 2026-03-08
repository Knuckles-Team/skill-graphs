## Output redirection[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#output-redirection "Link to this heading")
Note that you can redirect standard output and error streams as all commands support the `stdout` and `stderr` options. For example, you could write:
```
with open("/path/to/command_output", "w") as f:
    management.call_command("dumpdata", stdout=f)

```

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/databases/)
[Django Exceptions ](https://docs.djangoproject.com/en/5.0/ref/exceptions/)
[](https://docs.djangoproject.com/en/5.0/ref/django-admin/#top)
