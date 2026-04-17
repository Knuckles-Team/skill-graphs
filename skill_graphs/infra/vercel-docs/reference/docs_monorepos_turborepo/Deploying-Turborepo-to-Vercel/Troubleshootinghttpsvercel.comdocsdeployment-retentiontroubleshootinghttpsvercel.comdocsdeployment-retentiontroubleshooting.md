##  [Troubleshooting](https://vercel.com/docs/deployment-retention#troubleshooting)[](https://vercel.com/docs/deployment-retention#troubleshooting)
###  [Build outputs cannot be found on cache hit](https://vercel.com/docs/deployment-retention#build-outputs-cannot-be-found-on-cache-hit)[](https://vercel.com/docs/deployment-retention#build-outputs-cannot-be-found-on-cache-hit)
For Vercel to deploy your application, the outputs need to be present for your [Framework Preset](https://vercel.com/docs/deployments/configure-a-build#framework-preset) after your application builds. If you're getting an error that the outputs from your build don't exist after a cache hit:
  * Confirm that your outputs match [the expected Output Directory for your Framework Preset](https://vercel.com/docs/monorepos/turborepo#import-your-turborepo-to-vercel). Run `turbo build` locally and check for the directory where you expect to see the outputs from your build
  * Make sure the application outputs defined in the `outputs` key of your `turbo.json` for your build task are aligned with your Framework Preset. A few examples are below:


turbo.json
```
{
  "$schema": "https://turborepo.com/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [
        // Next.js
        ".next/**", "!.next/cache/**"
        // SvelteKit
        ".svelte-kit/**", ".vercel/**",
        // Build Output API
        ".vercel/output/**"
        // Other frameworks
        ".nuxt/**", "dist/**" "other-output-directory/**"
      ]
    }
  }
}
```

Visit `outputs` key.
###  [Unexpected cache misses](https://vercel.com/docs/deployment-retention#unexpected-cache-misses)[](https://vercel.com/docs/deployment-retention#unexpected-cache-misses)
When using Turborepo on Vercel, all information used by `turbo` during the build process is automatically collected to help debug cache misses.
Turborepo Run Summary is only available in Turborepo version `1.9` or later. To upgrade, use `npx @turbo/codemod upgrade`.
To view the Turborepo Run Summary for a deployment, use the following steps:
  1. From your [dashboard](https://vercel.com/dashboard), select your project and open Deployments in the sidebar.
  2. Select a Deployment from the list to view the deployment details
  3. Select the Run Summary button to the right of the Building section, under the Deployment Status heading:

![Open Turborepo Run Summary from the Deployment Details page](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fmonorepos%2Fturborepo%2Fturbo-run-summary-cta.png&w=3840&q=75)![Open Turborepo Run Summary from the Deployment Details page](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fmonorepos%2Fturborepo%2Fturbo-run-summary-cta-dark.png&w=3840&q=75)Open Turborepo Run Summary from the Deployment Details page
This opens a view containing a review of the build, including:
  * All
  * The execution time and cache status for each task
  * All data that `turbo` used to construct the cache key (the


If a previous deployment from the same branch is available, the difference between the cache inputs for the current and previous build will be automatically displayed, highlighting the specific changes that caused the cache miss.
![Turborepo Run Summary](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fmonorepos%2Fturborepo%2Fturbo-run-summary.png&w=3840&q=75)![Turborepo Run Summary](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fmonorepos%2Fturborepo%2Fturbo-run-summary-dark.png&w=3840&q=75)Turborepo Run Summary
This information can be helpful in identifying exactly why a cache miss occurred, and can be used to determine if a cache miss is due to a change in the project, or a change in the environment.
To change the comparison, select a different deployment from the dropdown, or search for a deployment ID. The summary data can also be downloaded for comparison with a local build.
Environment variable values are encrypted when displayed in Turborepo Run Summary, and can only be compared with summary files generated locally when viewed by a team member with access to the projects environment variables. [Learn more](https://vercel.com/docs/rbac/access-roles/team-level-roles)
