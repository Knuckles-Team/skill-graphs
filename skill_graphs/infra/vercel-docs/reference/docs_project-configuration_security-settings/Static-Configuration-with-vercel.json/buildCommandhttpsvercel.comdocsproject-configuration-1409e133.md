##  [buildCommand](https://vercel.com/docs/project-configuration/vercel-json#buildcommand)[](https://vercel.com/docs/project-configuration/vercel-json#buildcommand)
Type: `string | null`
The `buildCommand` property can be used to override the Build Command in the Project Settings dashboard, and the `build` script from the `package.json` file for a given deployment. For more information on the default behavior of the Build Command, visit the [Configure a Build - Build Command](https://vercel.com/docs/deployments/configure-a-build#build-command) section.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "buildCommand": "next build"
}
```

This value overrides the [Build Command](https://vercel.com/docs/deployments/configure-a-build#build-command) in Project Settings.
