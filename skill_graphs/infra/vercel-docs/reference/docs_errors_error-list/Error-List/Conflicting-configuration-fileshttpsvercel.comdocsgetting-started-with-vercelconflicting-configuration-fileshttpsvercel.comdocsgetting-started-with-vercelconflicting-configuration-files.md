##  [Conflicting configuration files](https://vercel.com/docs/getting-started-with-vercel#conflicting-configuration-files)[](https://vercel.com/docs/getting-started-with-vercel#conflicting-configuration-files)
For backward compatibility purposes, there are two naming conventions for configuration files used by Vercel CLI (for example `vercel.json` and `now.json`). Both naming conventions are supported, however only _one_ may be defined at a time. Vercel CLI will output an error message if both naming conventions are used at the same time.
These conflicting configuration errors occur if:
  * Both `vercel.json` and `now.json` exist in your project.
Solution: Delete the `now.json` file
  * Both `.vercel` and `.now` directories exist in your project.
Solution: Delete the `.now` directory
  * Both `.vercelignore` and `.nowignore` files exist in your project.
Solution: Delete the `.nowignore` file
  * Environment Variables that begin with `VERCEL_` have a conflicting Environment Variable that begins with `NOW_`.
Solution: Only define the `VERCEL_` prefixed Environment Variable
