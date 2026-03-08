##  [Ignoring files](https://vercel.com/docs/conformance/customize#ignoring-files)[](https://vercel.com/docs/conformance/customize#ignoring-files)
To exclude one or more files from Conformance, use the `ignorePatterns` field in the top level of the config file:
conformance.config.jsonc
```
{
  "ignorePatterns": ["generated/**/*.js"],
}
```

This field accepts an array of glob patterns as strings.
