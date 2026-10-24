##  [Go Build Configuration](https://vercel.com/docs/functions/quickstart#go-build-configuration)[](https://vercel.com/docs/functions/quickstart#go-build-configuration)
You can provide custom build flags by using the `GO_BUILD_FLAGS` [Environment Variable](https://vercel.com/docs/environment-variables).
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "build": {
    "env": {
      "GO_BUILD_FLAGS": "-ldflags '-s -w'"
    }
  }
}
```

An example `-ldflags` flag with `-s -w`. This will remove debug information from the output file. This is the default value when no `GO_BUILD_FLAGS` are provided.
