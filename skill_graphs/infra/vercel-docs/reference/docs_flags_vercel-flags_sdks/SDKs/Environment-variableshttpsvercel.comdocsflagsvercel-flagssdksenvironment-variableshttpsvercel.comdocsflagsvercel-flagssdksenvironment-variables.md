##  [Environment variables](https://vercel.com/docs/flags/vercel-flags/sdks#environment-variables)[](https://vercel.com/docs/flags/vercel-flags/sdks#environment-variables)
All integration methods use the same environment variables:
  * `FLAGS`: Connection string that identifies your Vercel Flags project. Vercel automatically sets this with different values for Production, Preview, and Development environments.
  * `FLAGS_SECRET`: Secret key used by Flags Explorer for secure overrides. Required if you want to use Flags Explorer.


When you create your first flag in the Vercel Dashboard, these variables are automatically added to your project.
