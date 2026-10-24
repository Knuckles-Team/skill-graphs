##  [Environment variable import](https://vercel.com/docs/integrations/cms#environment-variable-import)[](https://vercel.com/docs/integrations/cms#environment-variable-import)
The most common way to setup a CMS with Vercel is by installing an integration through the [Integrations Marketplace](https://vercel.com/integrations#cms). This method allows you to quickly setup your Vercel project with environment variables from your CMS.
Once a CMS has been installed, and a project linked you can pull in environment variables from the CMS to your Vercel project using the [Vercel CLI](https://vercel.com/docs/cli/env).
  1. ###  [Install the Vercel CLI](https://vercel.com/docs/integrations/cms#install-the-vercel-cli)[](https://vercel.com/docs/integrations/cms#install-the-vercel-cli)
To pull in environment variables from your CMS to your Vercel project, you need to install the [Vercel CLI](https://vercel.com/docs/cli). Run the following command in your terminal:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i -g vercel@latest
```

```
yarn global add vercel@latest
```

```
npm i -g vercel@latest
```

```
bun add -g vercel@latest
```

  2. ###  [Install your CMS integration](https://vercel.com/docs/integrations/cms#install-your-cms-integration)[](https://vercel.com/docs/integrations/cms#install-your-cms-integration)
Navigate to the CMS integration you want to install into your project, and follow the steps to install the integration.
  3. ###  [Pull in environment variables](https://vercel.com/docs/integrations/cms#pull-in-environment-variables)[](https://vercel.com/docs/integrations/cms#pull-in-environment-variables)
Once you've installed the CMS integration, you can pull in environment variables from the CMS to your Vercel project. In your terminal, run:
```
vercel env pull
```



See your installed CMSs documentation for next steps on how to use the integration.
