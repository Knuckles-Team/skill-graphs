## Examples[](https://nextjs.org/docs/pages/api-reference/cli/next#examples)
### Debugging prerender errors[](https://nextjs.org/docs/pages/api-reference/cli/next#debugging-prerender-errors)
If you encounter prerendering errors during `next build`, you can pass the `--debug-prerender` flag to get more detailed output:
Terminal
```
next build --debug-prerender
```

This enables several experimental options to make debugging easier:
  * Disables server code minification:
    * `experimental.serverMinification = false`
    * `experimental.turbopackMinify = false`
  * Generates source maps for server bundles:
    * `experimental.serverSourceMaps = true`
  * Enables source map consumption in child processes used for prerendering:
    * `enablePrerenderSourceMaps = true`
  * Continues building even after the first prerender error, so you can see all issues at once:
    * `experimental.prerenderEarlyExit = false`


This helps surface more readable stack traces and code frames in the build output.
> **Warning** : `--debug-prerender` is for debugging in development only. Do not deploy builds generated with `--debug-prerender` to production, as it may impact performance.
### Building specific routes[](https://nextjs.org/docs/pages/api-reference/cli/next#building-specific-routes)
You can build only specific routes in the App and Pages Routers using the `--debug-build-paths` option. This is useful for faster debugging when working with large applications. The `--debug-build-paths` option accepts comma-separated file paths and supports glob patterns:
Terminal
```
# Build a specific route
next build --debug-build-paths="app/page.tsx"

# Build more than one route
next build --debug-build-paths="app/page.tsx,pages/index.tsx"

# Use glob patterns
next build --debug-build-paths="app/**/page.tsx"
next build --debug-build-paths="pages/*.tsx"
```

### Changing the default port[](https://nextjs.org/docs/pages/api-reference/cli/next#changing-the-default-port)
By default, Next.js uses `http://localhost:3000` during development and with `next start`. The default port can be changed with the `-p` option, like so:
Terminal
```
next dev -p 4000
```

Or using the `PORT` environment variable:
Terminal
```
PORT=4000 next dev
```

> **Good to know** : `PORT` cannot be set in `.env` as booting up the HTTP server happens before any other code is initialized.
### Using HTTPS during development[](https://nextjs.org/docs/pages/api-reference/cli/next#using-https-during-development)
For certain use cases like webhooks or authentication, you can use `localhost`. Next.js can generate a self-signed certificate with `next dev` using the `--experimental-https` flag:
Terminal
```
next dev --experimental-https
```

With the generated certificate, the Next.js development server will exist at `https://localhost:3000`. The default port `3000` is used unless a port is specified with `-p`, `--port`, or `PORT`.
You can also provide a custom certificate and key with `--experimental-https-key` and `--experimental-https-cert`. Optionally, you can provide a custom CA certificate with `--experimental-https-ca` as well.
Terminal
```
next dev --experimental-https --experimental-https-key ./certificates/localhost-key.pem --experimental-https-cert ./certificates/localhost.pem
```

`next dev --experimental-https` is only intended for development and creates a locally trusted certificate with
### Configuring a timeout for downstream proxies[](https://nextjs.org/docs/pages/api-reference/cli/next#configuring-a-timeout-for-downstream-proxies)
When deploying Next.js behind a downstream proxy (e.g. a load-balancer like AWS ELB/ALB), it's important to configure Next's underlying HTTP server with _larger_ than the downstream proxy's timeouts. Otherwise, once a keep-alive timeout is reached for a given TCP connection, Node.js will immediately terminate that connection without notifying the downstream proxy. This results in a proxy error whenever it attempts to reuse a connection that Node.js has already terminated.
To configure the timeout values for the production Next.js server, pass `--keepAliveTimeout` (in milliseconds) to `next start`, like so:
Terminal
```
next start --keepAliveTimeout 70000
```

### Passing Node.js arguments[](https://nextjs.org/docs/pages/api-reference/cli/next#passing-nodejs-arguments)
You can pass any `next` commands. For example:
Terminal
```
NODE_OPTIONS='--throw-deprecation' next
NODE_OPTIONS='-r esm' next
NODE_OPTIONS='--inspect' next
```

Version | Changes
---|---
`v16.1.0` | Add the `next upgrade` command
`v16.1.0` | Add the `next experimental-analyze` command
`v16.0.0` | The JS bundle size metrics have been removed from `next build`
`v15.5.0` | Add the `next typegen` command
`v15.4.0` | Add `--debug-prerender` option for `next build` to help debug prerender errors.
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
