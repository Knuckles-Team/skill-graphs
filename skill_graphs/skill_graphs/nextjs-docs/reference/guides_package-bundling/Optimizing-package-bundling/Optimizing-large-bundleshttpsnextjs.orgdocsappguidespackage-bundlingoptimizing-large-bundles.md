## Optimizing large bundles[](https://nextjs.org/docs/app/guides/package-bundling#optimizing-large-bundles)
Once you've identified a large module, the solution will depend on your use case. Below are common causes and how to fix them:
### Packages with many exports[](https://nextjs.org/docs/app/guides/package-bundling#packages-with-many-exports)
If you're using a package that exports hundreds of modules (such as icon and utility libraries), you can optimize how those imports are resolved using the [`optimizePackageImports`](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports) option in your `next.config.js` file. This option will only load the modules you _actually_ use, while still giving you the convenience of writing import statements with many named exports.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    optimizePackageImports: ['icon-library'],
  },
}

module.exports = nextConfig
```

> **Good to know:** Next.js also optimizes some libraries automatically, thus they do not need to be included in the `optimizePackageImports` list. See the [full list](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports) of supported packages.
### Heavy client workloads[](https://nextjs.org/docs/app/guides/package-bundling#heavy-client-workloads)
A common cause of large client bundles is doing expensive rendering work in Client Components. This often happens with libraries that exist only to transform data into UI, such as syntax highlighting, chart rendering, or markdown parsing.
If that work does not require browser APIs or user interaction, it can be run in a Server Component.
In this example, a prism based highlighter runs in a Client Component. Even though the final output is just a `<code>` block, the entire highlighting library is bundled into the client JavaScript bundle:
app/blog/[slug]/page.tsx
```
'use client'

import Highlight from 'prism-react-renderer'
import theme from 'prism-react-renderer/themes/github'

export default function Page() {
  const code = `export function hello() {
    console.log("hi")
  }`

  return (
    <article>
      <h1>Blog Post Title</h1>

      {/* The prism package and its tokenization logic are shipped to the client */}
      <Highlight code={code} language="tsx" theme={theme}>
        {({ className, style, tokens, getLineProps, getTokenProps }) => (
          <pre className={className} style={style}>
            <code>
              {tokens.map((line, i) => (
                <div key={i} {...getLineProps({ line })}>
                  {line.map((token, key) => (
                    <span key={key} {...getTokenProps({ token })} />
                  ))}
                </div>
              ))}
            </code>
          </pre>
        )}
      </Highlight>
    </article>
  )
}
```

This increases bundle size because the client must download and execute the highlighting library, even though the result is static HTML.
Instead, move the highlighting logic to a Server Component and render the final HTML on the server. The client will only receive the rendered markup.
app/blog/[slug]/page.tsx
```
import { codeToHtml } from 'shiki'

export default async function Page() {
  const code = `export function hello() {
    console.log("hi")
  }`

  // The Shiki package runs on the server and is never bundled for the client.
  const highlightedHtml = await codeToHtml(code, {
    lang: 'tsx',
    theme: 'github-dark',
  })

  return (
    <article>
      <h1>Blog Post Title</h1>

      {/* Client receives plain markup */}
      <pre>
        <code dangerouslySetInnerHTML={{ __html: highlightedHtml }} />
      </pre>
    </article>
  )
}
```

### Opting specific packages out of bundling[](https://nextjs.org/docs/app/guides/package-bundling#opting-specific-packages-out-of-bundling)
Packages imported inside Server Components and Route Handlers are automatically bundled by Next.js.
You can opt specific packages out of bundling using the [`serverExternalPackages`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages) option in your `next.config.js`.
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['package-name'],
}

module.exports = nextConfig
```

Learn more about optimizing your application for production.
### [Production Recommendations to ensure the best performance and user experience before taking your Next.js application to production.](https://nextjs.org/docs/app/guides/production-checklist)
[PreviousOpenTelemetry](https://nextjs.org/docs/app/guides/open-telemetry)[NextPrefetching](https://nextjs.org/docs/app/guides/prefetching)
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
