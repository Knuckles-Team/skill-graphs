# check=error=<boolean>
```

The `check` directive is used to configure how [build checks](https://docs.docker.com/build/checks/) are evaluated. By default, all checks are run, and failures are treated as warnings.
You can disable specific checks using `#check=skip=<check-name>`. To specify multiple checks to skip, separate them with a comma:
```
