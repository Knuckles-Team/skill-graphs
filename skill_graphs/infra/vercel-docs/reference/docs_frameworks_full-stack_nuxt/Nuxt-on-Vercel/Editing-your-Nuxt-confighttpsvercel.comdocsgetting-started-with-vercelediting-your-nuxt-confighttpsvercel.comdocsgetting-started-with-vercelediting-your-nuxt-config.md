##  [Editing your Nuxt config](https://vercel.com/docs/getting-started-with-vercel#editing-your-nuxt-config)[](https://vercel.com/docs/getting-started-with-vercel#editing-your-nuxt-config)
You can configure your Nuxt deployment by creating a Nuxt config file in your project's root directory. It can be a TypeScript, JavaScript, or MJS file, but
Your Nuxt config file should default export `defineNuxtConfig` by default, which you can add an options object to.
The following is an example of a Nuxt config file with no options defined:
nuxt.config.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtConfig({
  // Config options here
});
```

###  [Using `routeRules`](https://vercel.com/docs/getting-started-with-vercel#using-routerules)[](https://vercel.com/docs/getting-started-with-vercel#using-routerules)
With the `routeRules` config option, you can:
  * Create redirects
  * Modify a route's response headers
  * Enable ISR
  * Deploy specific routes statically
  * Deploy specific routes with SSR
  * and more


At the moment, there is no way to configure route deployment options within your page components, but development of this feature is in progress.
The following is an example of a Nuxt config that:
  * Creates a redirect
  * Modifies a route's response headers
  * Opts a set of routes into client-side rendering


nuxt.config.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtConfig({
  routeRules: {
    '/examples/*': { redirect: '/redirect-route' },
    '/modify-headers-route': { headers: { 'x-magic-of': 'nuxt and vercel' } },
    // Enables client-side rendering
    '/spa': { ssr: false },
  },
});
```

To learn more about `routeRules`:
