##  [Environment variables](https://vercel.com/docs/builds#environment-variables)[](https://vercel.com/docs/builds#environment-variables)
Vercel can automatically inject environment variables such as API keys, database connections, or feature flags during the build:
  1. Project-Level Variables: Define variables under Settings for each environment (Preview, Production, or any custom environment).
  2. Pull Locally: Use `vercel env pull` to download environment variables for local development. This command populates your `.env.local` file.
  3. Security: Environment variables remain private within the build environment and are never exposed in logs.
