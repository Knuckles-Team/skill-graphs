##  [Framework considerations](https://vercel.com/docs/routing/rewrites#framework-considerations)[](https://vercel.com/docs/routing/rewrites#framework-considerations)
External rewrites work universally with all frameworks, making them ideal for API proxying, microfrontend architectures, and serving content from external origins through Vercel's global network as a reverse proxy or standalone CDN.
For same-application rewrites, always prefer your framework's native routing capabilities:
  * Next.js:
  * Astro: [Astro routing](https://vercel.com/docs/frameworks/astro#rewrites)
  * SvelteKit: [SvelteKit routing](https://vercel.com/docs/frameworks/sveltekit#rewrites)


Use `vercel.json` rewrites for same-application routing only when your framework doesn't provide native routing features. Always consult your framework's documentation for the recommended approach.
