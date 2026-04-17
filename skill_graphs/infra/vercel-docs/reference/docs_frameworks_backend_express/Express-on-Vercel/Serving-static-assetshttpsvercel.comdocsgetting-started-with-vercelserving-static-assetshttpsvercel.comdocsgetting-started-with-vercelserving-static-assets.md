##  [Serving static assets](https://vercel.com/docs/getting-started-with-vercel#serving-static-assets)[](https://vercel.com/docs/getting-started-with-vercel#serving-static-assets)
To serve static assets, place them in the `public/**` directory. They will be served as a part of our [CDN](https://vercel.com/docs/cdn) using default [headers](https://vercel.com/docs/headers) unless otherwise specified in `vercel.json`.
`express.static()` will be ignored and will not serve static assets.
