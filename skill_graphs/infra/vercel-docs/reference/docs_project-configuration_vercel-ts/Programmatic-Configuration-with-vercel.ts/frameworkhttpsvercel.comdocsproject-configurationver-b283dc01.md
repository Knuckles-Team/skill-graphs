##  [framework](https://vercel.com/docs/project-configuration/vercel-ts#framework)[](https://vercel.com/docs/project-configuration/vercel-ts#framework)
This value overrides the [Framework](https://vercel.com/docs/deployments/configure-a-build#framework-preset) in Project Settings.
Type: `string | null`
Available framework slugs:
The `framework` property can be used to override the Framework Preset in the Project Settings dashboard. The value must be a valid framework slug. For more information on the default behavior of the Framework Preset, visit the [Configure a Build - Framework Preset](https://vercel.com/docs/deployments/configure-a-build#framework-preset) section.
To select "Other" as the Framework Preset, use `null`.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  framework: 'nextjs',
};
```
