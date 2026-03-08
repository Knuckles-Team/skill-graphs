##  [ignoreCommand](https://vercel.com/docs/project-configuration/vercel-ts#ignorecommand)[](https://vercel.com/docs/project-configuration/vercel-ts#ignorecommand)
This value overrides the [Ignored Build Step](https://vercel.com/docs/project-configuration/project-settings#ignored-build-step) in Project Settings.
Type: `string | null`
This `ignoreCommand` property will override the Command for Ignoring the Build Step for a given deployment. When the command exits with code 1, the build will continue. When the command exits with 0, the build is ignored. For more information on the default behavior of the Ignore Command, visit the [Ignored Build Step](https://vercel.com/docs/project-configuration/project-settings#ignored-build-step) section.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  ignoreCommand: 'git diff --quiet HEAD^ HEAD ./',
};
```
