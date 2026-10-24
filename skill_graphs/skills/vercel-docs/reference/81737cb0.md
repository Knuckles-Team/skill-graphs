##  [Environment Variables](https://vercel.com/docs/getting-started-with-vercel#environment-variables)[](https://vercel.com/docs/getting-started-with-vercel#environment-variables)
Vercel provides a set of [System Environment Variables](https://vercel.com/docs/environment-variables/system-environment-variables) that our platform automatically populates. For example, the `VERCEL_GIT_PROVIDER` variable exposes the Git provider that triggered your project's deployment on Vercel.
These environment variables will be available to your project automatically, and you can enable or disable them in your project settings on Vercel. See [our Environment Variables docs](https://vercel.com/docs/environment-variables) to learn how.
To access Vercel's System Environment Variables in Vite during the build process, prefix the variable name with `VITE`. For example, `VITE_VERCEL_ENV` will return `preview`, `production`, or `development` depending on which environment the app is running in.
The following example demonstrates a Vite config file that sets `VITE_VERCEL_ENV` as a global constant available throughout the app:
vite.config.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineConfig(() => {
  return {
    define: {
      __APP_ENV__: process.env.VITE_VERCEL_ENV,
    },
  };
});
```

If you want to read environment variables from a `.env` file, additional configuration is required. See
To summarize, the benefits of using System Environment Variables with Vite on Vercel include:
  * Access to Vercel deployment information, dynamically or statically, with our preconfigured System Environment Variables
  * Access to automatically-configured environment variables provided by [integrations for your preferred services](https://vercel.com/docs/environment-variables#integration-environment-variables)
  * Searching and filtering environment variables by name and environment in Vercel's dashboard


[Learn more about System Environment Variables](https://vercel.com/docs/environment-variables/system-environment-variables)
