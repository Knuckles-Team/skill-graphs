## Options[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#options)
### Fetching[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#fetching)
You can configure the logging level and whether the full URL is logged to the console when running Next.js in development mode.
Currently, `logging` only applies to data fetching using the `fetch` API. It does not yet apply to other logs inside of Next.js.
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

Any `fetch` requests that are restored from the [Server Components HMR cache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache) are not logged by default. However, this can be enabled by setting `logging.fetches.hmrRefreshes` to `true`.
next.config.js
```
module.exports = {
  logging: {
    fetches: {
      hmrRefreshes: true,
    },
  },
}
```

### Incoming Requests[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#incoming-requests)
By default all the incoming requests will be logged in the console during development. You can use the `incomingRequests` option to decide which requests to ignore. Since this is only logged in development, this option doesn't affect production builds.
next.config.js
```
module.exports = {
  logging: {
    incomingRequests: {
      ignore: [/\api\/v1\/health/],
    },
  },
}
```

Or you can disable incoming request logging by setting `incomingRequests` to `false`.
next.config.js
```
module.exports = {
  logging: {
    incomingRequests: false,
  },
}
```

### Disabling Logging[](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging#disabling-logging)
In addition, you can disable the development logging by setting `logging` to `false`.
next.config.js
```
module.exports = {
  logging: false,
}
```

[PreviousisolatedDevBuild](https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild)[NextmdxRs](https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
