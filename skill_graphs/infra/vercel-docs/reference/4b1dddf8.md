##  [Client-side rendering](https://vercel.com/docs/getting-started-with-vercel#client-side-rendering)[](https://vercel.com/docs/getting-started-with-vercel#client-side-rendering)
If you deploy with `nuxt build`, you can opt nuxt routes into client-side rendering using `routeRules` by setting `ssr: false` as demonstrated below:
nuxt.config.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtConfig({
  routeRules: {
    // Use client-side rendering for this route
    '/client-side-route-example': { ssr: false },
  },
});
```
