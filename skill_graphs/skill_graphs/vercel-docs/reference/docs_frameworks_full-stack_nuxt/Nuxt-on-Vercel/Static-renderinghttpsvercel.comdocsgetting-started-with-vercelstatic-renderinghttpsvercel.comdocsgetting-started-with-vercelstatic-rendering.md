##  [Static rendering](https://vercel.com/docs/getting-started-with-vercel#static-rendering)[](https://vercel.com/docs/getting-started-with-vercel#static-rendering)
To deploy a fully static site on Vercel, build your project with `nuxt generate`.
Alternatively, you can statically generate some Nuxt routes at build time using the `prerender` route rule in your `nuxt.config.ts`:
nuxt.config.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtConfig({
  routeRules: {
    // prerender index route by default
    '/': { prerender: true },
    // prerender this route and all child routes
    '/prerender-multiple/**': { prerender: true },
  },
});
```

To verify that a route is prerendered at build time, check `useNuxtApp().payload.prerenderedAt`.
