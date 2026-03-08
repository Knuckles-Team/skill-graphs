##  [Creating a Next.js JSS application](https://vercel.com/docs/integrations/cms/agility-cms#creating-a-next.js-jss-application)[](https://vercel.com/docs/integrations/cms/agility-cms#creating-a-next.js-jss-application)
To help get you started, we built a [template](https://vercel.com/templates/next.js/sitecore-starter) using Sitecore JSS for Next.js with JSS SXA headless components. This template includes only the frontend Next.js application that connects to a new or existing hosted XM Cloud website. Note that it omits the Docker configuration for running XM Cloud locally. For details on local XM Cloud configuration, refer to Sitecore's
Sitecore also offers a
[![Sitecore XM Cloud Next.js Starter](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FJAWlcS27EakxvDFRjmLwD%2F412631142afd83d7b3a926cb7c3e44bd%2FCleanShot_2023-08-25_at_20.09.25_2x.png&w=3840&q=75) Sitecore XM Cloud Next.js Starter Simple Next.js blog site that connects to a Sitecore XM Cloud site using the Sitecore JavaScript Rendering SDK (JSS). ](https://vercel.com/templates/next.js/sitecore-starter)
You can either deploy the template above to Vercel with one-click, or use the steps below to clone it to your machine and deploy it locally.
  1. ###  [Clone the repository](https://vercel.com/docs/integrations/cms/agility-cms#clone-the-repository)[](https://vercel.com/docs/integrations/cms/agility-cms#clone-the-repository)
You can clone the repo using the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm create next-app --example cms-sitecore-xmcloud
```

```
yarn create next-app --example cms-sitecore-xmcloud
```

```
npx create-next-app --example cms-sitecore-xmcloud
```

```
bunx create-next-app --example cms-sitecore-xmcloud
```

  2. ###  [Retrieve your API key, GraphQL endpoint, and JSS app name](https://vercel.com/docs/integrations/cms/agility-cms#retrieve-your-api-key-graphql-endpoint-and-jss-app-name)[](https://vercel.com/docs/integrations/cms/agility-cms#retrieve-your-api-key-graphql-endpoint-and-jss-app-name)
Next, navigate to your newly created XM Cloud site under Sites and select Settings.
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fsitecore%2Fsitecore-dashboard.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fsitecore%2Fsitecore-dashboard.png&w=3840&q=75)
Under the Developer Settings tab select Generate API Key.
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fsitecore%2Fdeveloper-settings.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fsitecore%2Fdeveloper-settings.png&w=3840&q=75)
Save the `SITECORE_API_KEY`, `JSS_APP_NAME`, and `GRAPH_QL_ENDPOINT` values – you'll need them for the next step.
  3. ###  [Configure your Next.js JSS application](https://vercel.com/docs/integrations/cms/agility-cms#configure-your-next.js-jss-application)[](https://vercel.com/docs/integrations/cms/agility-cms#configure-your-next.js-jss-application)
Next, add the `JSS_APP_NAME`, `GRAPH_QL_ENDPOINT` , `SITECORE_API_KEY`, and `SITECORE_API_HOST` values as environment variables for running locally. Create a new `.env.local` file in your application, copy the contents of `.env.example` and set the 4 environment variables.
.env.local
```
JSS_APP_NAME='your-jss-app-name'
GRAPH_QL_ENDPOINT='your-graphql-endpoint'
SITECORE_API_KEY='your-sitecore-api-key'
SITECORE_API_HOST='host-from-endpoint'
```

  4. ###  [Start your application](https://vercel.com/docs/integrations/cms/agility-cms#start-your-application)[](https://vercel.com/docs/integrations/cms/agility-cms#start-your-application)
You can now start your application with the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm install && pnpm build && pnpm dev
```

```
yarn && yarn build && yarn dev
```

```
npm install && npm run build && npm run dev
```

```
bun install && bun run build && bun run dev
```
