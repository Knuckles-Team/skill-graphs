##  [How builds are triggered](https://vercel.com/docs/builds#how-builds-are-triggered)[](https://vercel.com/docs/builds#how-builds-are-triggered)
Builds can be initiated in the following ways:
  1. Push to Git: When you connect a GitHub, GitLab, or Bitbucket repository, each commit to a tracked branch initiates a new build and deployment. By default, Vercel performs a _shallow clone_ of your repo (`git clone --depth=10`) to speed up build times.
  2. Vercel CLI: Running `vercel` locally deploys your project. By default, this creates a preview build unless you add the `--prod` flag (for production).
  3. Dashboard deploy: Clicking Deploy in the dashboard or creating a new project also triggers a build.
