##  [Getting started](https://vercel.com/docs/integrations/cms/contentful#getting-started)[](https://vercel.com/docs/integrations/cms/contentful#getting-started)
To help you get started, we built a [template](https://vercel.com/templates/next.js/nextjs-blog-preview-mode) using Next.js, Contentful, and Tailwind CSS.
[![Next.js Blog with Draft Mode](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5nCnKpHjzhYfrEZZFcmGxU%2F9a057ee2eba16efb26ddb59ca16d4bac%2FCleanShot_2021-07-07_at_19.43.15_2x.png&w=3840&q=75) Next.js Blog with Draft Mode Static blog with Preview Mode, built with Next.js and Contentful. ](https://vercel.com/templates/next.js/nextjs-blog-draft-mode)
You can either deploy the template above to Vercel with one click, or use the steps below to clone it to your machine and deploy it locally:
  1. ###  [Clone the repository](https://vercel.com/docs/integrations/cms/contentful#clone-the-repository)[](https://vercel.com/docs/integrations/cms/contentful#clone-the-repository)
You can clone the repo using the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm create next-app --example cms-contentful
```

```
yarn create next-app --example cms-contentful
```

```
npx create-next-app --example cms-contentful
```

```
bunx create-next-app --example cms-contentful
```

  2. ###  [Create a Contentful Account](https://vercel.com/docs/integrations/cms/contentful#create-a-contentful-account)[](https://vercel.com/docs/integrations/cms/contentful#create-a-contentful-account)
Next, create a new account on
If you have an existing account and space, you can use it with the rest of these steps.
  3. ###  [Retrieve your Contentful Space ID](https://vercel.com/docs/integrations/cms/contentful#retrieve-your-contentful-space-id)[](https://vercel.com/docs/integrations/cms/contentful#retrieve-your-contentful-space-id)
The Vercel integration uses your Contentful Space ID to communicate with Contentful. To find this, navigate to your Contentful dashboard and select Settings > API Keys. Click on Add API key and you will see your Space ID in the next screen.
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcontentful%2Fapi-section.png&w=2048&q=75)
  4. ###  [Create a Content Management API token](https://vercel.com/docs/integrations/cms/contentful#create-a-content-management-api-token)[](https://vercel.com/docs/integrations/cms/contentful#create-a-content-management-api-token)
You will also need to create a Content Management API token for Vercel to communicate back and forth with the Contentful API. You can get that by going to Settings > API Keys > Content management tokens.
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fcontentful%2Fcontent-management-tokens.png&w=1920&q=75)
Click on Generate personal token and a modal will pop up. Give your token a name and click on Generate.
Avoid sharing this token because it allows both read and write access to your Contentful space. Once the token is generated copy the key and save remotely as it will not be accessible later on. If lost, a new one must be created.
  5. ###  [Import the Content Model](https://vercel.com/docs/integrations/cms/contentful#import-the-content-model)[](https://vercel.com/docs/integrations/cms/contentful#import-the-content-model)
Use your Space ID and Content Management Token in the command below to import the pre-made content model into your space using our setup Node.js script. You can do that by running the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
npx cross-env CONTENTFUL_SPACE_ID=YOUR_SPACE_ID CONTENTFUL_MANAGEMENT_TOKEN=XXX pnpm run setup
```

```
npx cross-env CONTENTFUL_SPACE_ID=YOUR_SPACE_ID CONTENTFUL_MANAGEMENT_TOKEN=XXX yarn setup
```

```
npx cross-env CONTENTFUL_SPACE_ID=YOUR_SPACE_ID CONTENTFUL_MANAGEMENT_TOKEN=XXX npm run setup
```

```
npx cross-env CONTENTFUL_SPACE_ID=YOUR_SPACE_ID CONTENTFUL_MANAGEMENT_TOKEN=XXX bun run setup
```
