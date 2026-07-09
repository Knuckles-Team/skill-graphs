##  [Setting up rewrites](https://vercel.com/docs/routing/rewrites#setting-up-rewrites)[](https://vercel.com/docs/routing/rewrites#setting-up-rewrites)
Rewrites are defined in a `vercel.json` file in your project's root directory:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/source-path",
      "destination": "/destination-path"
    }
  ]
}
```

For all configuration options, see the [project configuration](https://vercel.com/docs/project-configuration#rewrites) docs.
