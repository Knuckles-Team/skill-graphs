##  [Deploy Nx to Vercel](https://vercel.com/docs/monorepos/nx#deploy-nx-to-vercel)[](https://vercel.com/docs/monorepos/nx#deploy-nx-to-vercel)
  1. ###  [Ensure your Nx project is configured correctly](https://vercel.com/docs/monorepos/nx#ensure-your-nx-project-is-configured-correctly)[](https://vercel.com/docs/monorepos/nx#ensure-your-nx-project-is-configured-correctly)
If you haven't already connected your monorepo to Nx, you can follow the
To ensure the best experience using Nx with Vercel, the following versions and settings are recommended:
     * Use `nx` version `14.6.2` or later
     * Use `nx-cloud` version `14.6.0` or later
There are also additional settings if you are [using Remote Caching](https://vercel.com/docs/monorepos/nx#setup-remote-caching-for-nx-on-vercel)
All Nx starters and examples are preconfigured with these settings.
  2. ###  [Import your project](https://vercel.com/docs/monorepos/nx#import-your-project)[](https://vercel.com/docs/monorepos/nx#import-your-project)
[Create a new Project](https://vercel.com/docs/projects/overview#creating-a-project) on the Vercel dashboard and [import](https://vercel.com/docs/getting-started-with-vercel/import) your monorepo project.
Vercel handles all aspects of configuring your monorepo, including setting [build commands](https://vercel.com/docs/deployments/configure-a-build#build-command), the [Root Directory](https://vercel.com/docs/deployments/configure-a-build#root-directory), the correct directory for npm workspaces, and the [ignored build step](https://vercel.com/docs/project-configuration/project-settings#ignored-build-step).
  3. ###  [Next steps](https://vercel.com/docs/monorepos/nx#next-steps)[](https://vercel.com/docs/monorepos/nx#next-steps)
Your Nx monorepo is now configured and ready to be used with Vercel!
You can now [setup Remote Caching for Nx on Vercel](https://vercel.com/docs/monorepos/nx#setup-remote-caching-for-nx-on-vercel) or configure additional deployment options, such as [environment variables](https://vercel.com/docs/environment-variables).
