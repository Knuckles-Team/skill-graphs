## Troubleshooting[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#troubleshooting)
### Debugging cached data in local development[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#debugging-cached-data-in-local-development)
If you are using the `fetch` API, you can add additional logging to understand which requests are cached or uncached. [Learn more about the `logging` option](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging).
next.config.js
```
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

### Verifying correct production behavior[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#verifying-correct-production-behavior)
To verify your pages are cached and revalidated correctly in production, you can test locally by running `next build` and then `next start` to run the production Next.js server.
This will allow you to test ISR behavior as it would work in a production environment. For further debugging, add the following environment variable to your `.env` file:
.env
```
NEXT_PRIVATE_DEBUG_CACHE=1
```

This will make the Next.js server console log ISR cache hits and misses. You can inspect the output to see which pages are generated during `next build`, as well as how pages are updated as paths are accessed on-demand.
