##  [Failed to install builder dependencies](https://vercel.com/docs/getting-started-with-vercel#failed-to-install-builder-dependencies)[](https://vercel.com/docs/getting-started-with-vercel#failed-to-install-builder-dependencies)
When running the `vercel build` or `vercel dev` commands, `npm install` errors can be encountered if `npm` was invoked to install Builders that are defined in your `vercel.json` file.
`npm install` may fail if:
  * Your internet connection is unavailable
  * The Builder that is defined in your configuration is not published to the npm registry


Double-check that the name and version of the Builder you are requesting is correct.
