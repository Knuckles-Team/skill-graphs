##  [Deploy Turborepo to Vercel](https://vercel.com/docs/deployment-retention#deploy-turborepo-to-vercel)[](https://vercel.com/docs/deployment-retention#deploy-turborepo-to-vercel)
Follow the steps below to deploy your Turborepo to Vercel:
  1. ###  [Handling environment variables](https://vercel.com/docs/deployment-retention#handling-environment-variables)[](https://vercel.com/docs/deployment-retention#handling-environment-variables)
It's important to ensure you are managing environment variables (and files outside of packages and apps) correctly.
If your project has environment variables, you'll need to create a list of them in your `turbo.json` so Turborepo knows to use different caches for different environments. For example, you can accidentally ship your staging environment to production if you don't tell Turborepo about your environment variables.
Frameworks like Next.js inline build-time environment variables (e.g. `NEXT_PUBLIC_XXX`) in bundled outputs as strings. Turborepo will
You can control Turborepo's cache behavior (hashing) based on the values of both environment variables and the contents of files in a few ways. Read the
`env` and `globalEnv` key support is available in Turborepo version 1.5 or later. You should update your Turborepo version if you're using an older version.
The following example shows a Turborepo configuration, that handles these suggestions:
turbo.json
```
{
  "$schema": "https://turborepo.com/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "env": [
        // env vars will impact hashes of all "build" tasks
        "SOME_ENV_VAR"
      ],
      "outputs": ["dist/**"]
    },
    "web#build": {
      // override settings for the "build" task for the "web" app
      "dependsOn": ["^build"],
      "env": ["SOME_OTHER_ENV_VAR"],
      "outputs": [".next/**", "!.next/cache/**"]
    }
  },
  "globalEnv": [
    "GITHUB_TOKEN" // env var that will impact the hashes of all tasks,
  ],
  "globalDependencies": [
    "tsconfig.json" // file contents will impact the hashes of all tasks,
  ]
}
```

In most monorepos, environment variables are usually used in applications rather than in shared packages. To get higher cache hit rates, you should only include environment variables in the app-specific tasks where they are used or inlined.
Once you've declared your environment variables, commit and push any changes you've made. When you update or add new inlined build-time environment variables, be sure to declare them in your Turborepo configuration.
  2. ###  [Import your Turborepo to Vercel](https://vercel.com/docs/deployment-retention#import-your-turborepo-to-vercel)[](https://vercel.com/docs/deployment-retention#import-your-turborepo-to-vercel)
If you haven't already connected your monorepo to Turborepo, you can follow the
[Create a new Project](https://vercel.com/new) on the Vercel dashboard and [import](https://vercel.com/docs/getting-started-with-vercel/import) your Turborepo project.
![Configuring Project settings during import, with defaults already set.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fconfig-project-light.png&w=1920&q=75)![Configuring Project settings during import, with defaults already set.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fconfig-project-dark.png&w=1920&q=75)Configuring Project settings during import, with defaults already set.
Vercel handles all aspects of configuring your monorepo, including setting [build commands](https://vercel.com/docs/deployments/configure-a-build#build-command), the [Output Directory](https://vercel.com/docs/deployments/configure-a-build#output-directory), the [Root Directory](https://vercel.com/docs/deployments/configure-a-build#root-directory), the correct directory for workspaces, and the [Ignored Build Step](https://vercel.com/docs/project-configuration/project-settings#ignored-build-step).
The table below reflects the values that Vercel will set if you'd like to set them manually in your Dashboard or in the `vercel.json` of your application's directory:
Field | Command
---|---
Framework Preset | [One of 35+ framework presets](https://vercel.com/docs/frameworks/more-frameworks)
Build Command |  `turbo run build` (requires version >=1.8) or `cd ../.. && turbo run build --filter=web`
Output Directory | Framework default
Install Command | Automatically detected by Vercel
Root Directory | App location in repository (e.g. `apps/web`)
Ignored Build Step | `npx turbo-ignore --fallback=HEAD^1`
