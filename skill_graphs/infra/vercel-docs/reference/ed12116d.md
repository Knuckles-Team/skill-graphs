##  [framework](https://vercel.com/docs/project-configuration/vercel-json#framework)[](https://vercel.com/docs/project-configuration/vercel-json#framework)
This value overrides the [Framework](https://vercel.com/docs/deployments/configure-a-build#framework-preset) in Project Settings.
Type: `string | null`
Available framework slugs:
The `framework` property can be used to override the Framework Preset in the Project Settings dashboard. The value must be a valid framework slug. For more information on the default behavior of the Framework Preset, visit the [Configure a Build - Framework Preset](https://vercel.com/docs/deployments/configure-a-build#framework-preset) section.
To select "Other" as the Framework Preset, use `null`.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "framework": "nextjs"
}
```
