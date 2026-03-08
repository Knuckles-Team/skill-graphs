##  [Adding Content in Contentful](https://vercel.com/docs/integrations/cms/contentful#adding-content-in-contentful)[](https://vercel.com/docs/integrations/cms/contentful#adding-content-in-contentful)
Now that you've created your space in Contentful, add some content!
  1. ###  [Publish Contentful entries](https://vercel.com/docs/integrations/cms/contentful#publish-contentful-entries)[](https://vercel.com/docs/integrations/cms/contentful#publish-contentful-entries)
You'll notice the new author and post entries for the example we've provided. Publish each entry to make this fully live.
  2. ###  [Retrieve your Contentful Secrets](https://vercel.com/docs/integrations/cms/contentful#retrieve-your-contentful-secrets)[](https://vercel.com/docs/integrations/cms/contentful#retrieve-your-contentful-secrets)
Now, let's save the Space ID and token from earlier to add as Environment Variables for running locally. Create a new `.env.local` file in your application:
terminal
```
CONTENTFUL_SPACE_ID='your-space-id'
CONTENTFUL_ACCESS_TOKEN='your-content-api-token'
```

  3. ###  [Start your application](https://vercel.com/docs/integrations/cms/contentful#start-your-application)[](https://vercel.com/docs/integrations/cms/contentful#start-your-application)
You can now start your application with the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm install && pnpm run dev
```

```
yarn && yarn dev
```

```
npm install && npm run dev
```

```
bun install && bun run dev
```

Your project should now be running on `http://localhost:3000`.
