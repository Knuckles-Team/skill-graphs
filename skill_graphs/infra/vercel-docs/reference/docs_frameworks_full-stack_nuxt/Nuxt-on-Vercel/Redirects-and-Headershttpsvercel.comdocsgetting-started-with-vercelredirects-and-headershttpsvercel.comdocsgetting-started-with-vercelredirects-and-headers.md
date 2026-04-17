##  [Redirects and Headers](https://vercel.com/docs/getting-started-with-vercel#redirects-and-headers)[](https://vercel.com/docs/getting-started-with-vercel#redirects-and-headers)
You can define redirects and response headers with Nuxt on Vercel in your `nuxt.config.ts`:
nuxt.config.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtConfig({
  routeRules: {
    '/examples/*': { redirect: '/redirect-route' },
    '/modify-headers-route': { headers: { 'x-magic-of': 'nuxt and vercel' } },
  },
});
```
