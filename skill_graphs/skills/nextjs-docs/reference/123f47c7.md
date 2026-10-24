# serverExternalPackages
Last updated February 27, 2026
Dependencies used inside [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) and [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) will automatically be bundled by Next.js.
If a dependency is using Node.js specific features, you can choose to opt-out specific dependencies from the Server Components bundling and use native Node.js `require`.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['@acme/ui'],
}

module.exports = nextConfig
```

Next.js includes a
  * `@alinea/generated`
  * `@appsignal/nodejs`
  * `@aws-sdk/client-s3`
  * `@aws-sdk/s3-presigned-post`
  * `@blockfrost/blockfrost-js`
  * `@highlight-run/node`
  * `@huggingface/transformers`
  * `@jpg-store/lucid-cardano`
  * `@libsql/client`
  * `@mikro-orm/core`
  * `@mikro-orm/knex`
  * `@node-rs/argon2`
  * `@node-rs/bcrypt`
  * `@prisma/client`
  * `@react-pdf/renderer`
  * `@sentry/profiling-node`
  * `@sparticuz/chromium`
  * `@sparticuz/chromium-min`
  * `@statsig/statsig-node-core`
  * `@swc/core`
  * `@xenova/transformers`
  * `@zenstackhq/runtime`
  * `argon2`
  * `autoprefixer`
  * `aws-crt`
  * `bcrypt`
  * `better-sqlite3`
  * `canvas`
  * `chromadb-default-embed`
  * `config`
  * `cpu-features`
  * `cypress`
  * `dd-trace`
  * `eslint`
  * `express`
  * `firebase-admin`
  * `htmlrewriter`
  * `import-in-the-middle`
  * `isolated-vm`
  * `jest`
  * `jsdom`
  * `keyv`
  * `libsql`
  * `mdx-bundler`
  * `mongodb`
  * `mongoose`
  * `newrelic`
  * `next-mdx-remote`
  * `next-seo`
  * `node-cron`
  * `node-pty`
  * `node-web-audio-api`
  * `onnxruntime-node`
  * `oslo`
  * `pg`
  * `pino`
  * `pino-pretty`
  * `pino-roll`
  * `playwright`
  * `playwright-core`
  * `postcss`
  * `prettier`
  * `prisma`
  * `puppeteer-core`
  * `puppeteer`
  * `ravendb`
  * `require-in-the-middle`
  * `rimraf`
  * `sharp`
  * `shiki`
  * `sqlite3`
  * `thread-stream`
  * `ts-morph`
  * `ts-node`
  * `typescript`
  * `vscode-oniguruma`
  * `webpack`
  * `websocket`
  * `zeromq`


Version | Changes
---|---
`v15.0.0` | Moved from experimental to stable. Renamed from `serverComponentsExternalPackages` to `serverExternalPackages`
[PreviousserverComponentsHmrCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)[NextstaleTimes](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)
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
