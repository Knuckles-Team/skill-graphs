##  [Deferred Static Generation](https://vercel.com/docs/getting-started-with-vercel#deferred-static-generation)[](https://vercel.com/docs/getting-started-with-vercel#deferred-static-generation)
Deferred Static Generation (DSG) allows you to defer the generation of static pages until they are requested for the first time.
To use DSG, you must set the `defer` option to `true` in the `createPages()` function in your `gatsby-node` file.
pages/index.tsx
TypeScript
TypeScript JavaScript Bash
```
import type { GatsbyNode } from 'gatsby';

export const createPages: GatsbyNode['createPages'] = async ({ actions }) => {
  const { createPage } = actions;
  createPage({
    defer: true,
    path: '/using-dsg',
    component: require.resolve('./src/templates/using-dsg.js'),
    context: {},
  });
};
```

To summarize, DSG with Gatsby on Vercel:
  * Allows you to defer non-critical page generation to user request, speeding up build times
  * Works out of the box when you deploy on Vercel
  * Can yield dramatic speed increases for large sites with content that is infrequently visited
