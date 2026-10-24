##  [How it works](https://vercel.com/docs/integrations/cms/contentful#how-it-works)[](https://vercel.com/docs/integrations/cms/contentful#how-it-works)
Next.js is designed to integrate with any data source of your choice, including Content Management Systems. Contentful provides a helpful GraphQL API, which you can both query and mutate data from. This allows you to decouple your content from your frontend. For example:
```
async function fetchGraphQL(query) {
  return fetch(
    `https://graphql.contentful.com/content/v1/repos/${process.env.CONTENTFUL_SPACE_ID}`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.CONTENTFUL_ACCESS_TOKEN}`,
      },
      body: JSON.stringify({ query }),
    },
  ).then((response) => response.json());
}
```

This code allows you to fetch data on the server from your Contentful instance. Each space inside Contentful has its own ID (e.g. `CONTENTFUL_SPACE_ID`) which you can add as an Environment Variable inside your Next.js application.
This allows you to use secure values you don't want to commit to git, which are only evaluated on the server (e.g. `CONTENTFUL_ACCESS_TOKEN`).
