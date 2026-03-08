##  [Limitations](https://vercel.com/docs/getting-started-with-vercel#limitations)[](https://vercel.com/docs/getting-started-with-vercel#limitations)
All [Vercel Functions limitations](https://vercel.com/docs/functions/limitations) apply to FastAPI applications, including:
  * Application size: The FastAPI application becomes a single bundle, which must fit within the 500MB limit of Vercel Functions. Our bundling process removes `__pycache__` and `.pyc` files from the deployment's bundle to reduce size, but does not perform application bundling.
