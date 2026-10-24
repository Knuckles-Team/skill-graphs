Menu
Menu
# NEXTJS_NO_TURBO_CACHE
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule prevents the `.next/cache` folder from being added to the Turborepo cache. This is important because including the `.next/cache` folder in the Turborepo cache can cause the cache to grow to an excessive size. Vercel also already includes this cache in the build container cache.
##  [Examples](https://vercel.com/docs/conformance/rules/NEXTJS_NO_TURBO_CACHE#examples)[](https://vercel.com/docs/conformance/rules/NEXTJS_NO_TURBO_CACHE#examples)
The following `turbo.json` config will be caught by this rule for Next.js apps:
turbo.json
```
{
  "extends": ["//"],
  "pipeline": {
    "build": {
      "outputs": [".next/**"]
    }
  }
}
```

##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_NO_TURBO_CACHE#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_NO_TURBO_CACHE#how-to-fix)
To fix, add `"!.next/cache/**"` to the list of outputs for the task.
turbo.json
```
{
  "extends": ["//"],
  "pipeline": {
    "build": {
      "outputs": [".next/**", "!.next/cache/**"]
    }
  }
}
```

* * *
Was this helpful?
Send
