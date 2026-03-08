##  [Unmatched function pattern](https://vercel.com/docs/getting-started-with-vercel#unmatched-function-pattern)[](https://vercel.com/docs/getting-started-with-vercel#unmatched-function-pattern)
The [functions](https://vercel.com/docs/project-configuration#functions) property uses a glob pattern for each key. This pattern must match Vercel Function source files within the `api` directory.
If you are using Next.js, Vercel functions source files can be created in the following:
  * `pages/api` directory
  * `src/pages/api` directory
  * `pages` directory when the module exports
  * `src/pages` directory when the module exports


Additionally, if you'd like to use a Vercel Function that isn't written with Node.js, and in combination with Next.js, you can place it in the `api` directory (provided by the platform), since `pages/api` (provided by Next.js) only supports JavaScript.
Not Allowed
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "users/**/*.js": {
      "maxDuration": 30
    }
  }
}
```

Allowed
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/users/**/*.js": {
      "maxDuration": 30
    }
  }
}
```

Allowed (Next.js)
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "pages/api/users/**/*.js": {
      "maxDuration": 30
    }
  }
}
```
