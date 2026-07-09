# check=error=true
```

> Note
> When using the `check` directive, with `error=true` option, it is recommended to pin the [Dockerfile syntax](https://docs.docker.com/reference/dockerfile#syntax) to a specific version. Otherwise, your build may start to fail when new checks are added in the future versions.
To combine both the `skip` and `error` options, use a semi-colon to separate them:
```
