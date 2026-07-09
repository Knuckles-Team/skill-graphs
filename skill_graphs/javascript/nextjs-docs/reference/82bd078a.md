# httpAgentOptions
Last updated February 27, 2026
In Node.js versions prior to 18, Next.js automatically polyfills `fetch()` with [undici](https://nextjs.org/docs/architecture/supported-browsers#polyfills) and enables
To disable HTTP Keep-Alive for all `fetch()` calls on the server-side, open `next.config.js` and add the `httpAgentOptions` config:
next.config.js
```
module.exports = {
  httpAgentOptions: {
    keepAlive: false,
  },
}
```

Was this helpful?
Send
