##  [Limitations](https://vercel.com/docs/getting-started-with-vercel#limitations)[](https://vercel.com/docs/getting-started-with-vercel#limitations)
  * `express.static()` will not serve static assets. You must use [the `public/**` directory](https://vercel.com/docs/getting-started-with-vercel#serving-static-assets).


Additionally, all [Vercel Functions limitations](https://vercel.com/docs/functions/limitations) apply to the Express application, including:
  * Application size: The Express application becomes a single bundle, which must fit within the 250MB limit of Vercel Functions. Our bundling process removes all unneeded files from the deployment's bundle to reduce size, but does not perform application bundling (e.g., Webpack or Rollup).
  * Error handling: Express.js will swallow errors that can put the main function into an undefined state unless properly handled. Express.js will render its own error pages (500), which prevents Vercel from discarding the function and resetting its state. Implement robust error handling to ensure errors are properly managed and do not interfere with the serverless function's lifecycle.
