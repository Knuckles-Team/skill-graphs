##  [Monorepos](https://vercel.com/docs/builds#monorepos)[](https://vercel.com/docs/builds#monorepos)
When working in a monorepo, you can connect multiple Vercel projects within the same repository. By default, each project will build and deploy whenever you push a commit. Vercel can optimize this by:
  1. Skipping unaffected projects: Vercel automatically detects whether a project's files (or its dependencies) have changed and skips deploying projects that are unaffected. This feature reduces unnecessary builds and doesn't occupy concurrent build slots. Learn more about [skipping unaffected projects](https://vercel.com/docs/monorepos#skipping-unaffected-projects).
  2. Ignored build step: You can also write a script that cancels the build for a project if no relevant changes are detected. This approach still counts toward your concurrent build limits, but may be useful in certain scenarios. See the [Ignored Build Step](https://vercel.com/docs/project-configuration/project-settings#ignored-build-step) documentation for details.


For monorepo-specific build tools, see:
  * [Turborepo](https://vercel.com/docs/monorepos/turborepo)
  * [Nx](https://vercel.com/docs/monorepos/nx)
