# How to load and optimize scripts
Last updated February 27, 2026
### Application Scripts[](https://nextjs.org/docs/pages/guides/scripts#application-scripts)
To load a third-party script for all routes, import `next/script` and include the script directly in your custom `_app`:
pages/_app.js
```
import Script from 'next/script'

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <Script src="https://example.com/script.js" />
    </>
  )
}
```

This script will load and execute when _any_ route in your application is accessed. Next.js will ensure the script will **only load once** , even if a user navigates between multiple pages.
> **Recommendation** : We recommend only including third-party scripts in specific pages or layouts in order to minimize any unnecessary impact to performance.
### Strategy[](https://nextjs.org/docs/pages/guides/scripts#strategy)
Although the default behavior of `next/script` allows you to load third-party scripts in any page or layout, you can fine-tune its loading behavior by using the `strategy` property:
  * `beforeInteractive`: Load the script before any Next.js code and before any page hydration occurs.
  * `afterInteractive`: (**default**) Load the script early but after some hydration on the page occurs.
  * `lazyOnload`: Load the script later during browser idle time.
  * `worker`: (experimental) Load the script in a web worker.


Refer to the [`next/script`](https://nextjs.org/docs/app/api-reference/components/script#strategy) API reference documentation to learn more about each strategy and their use cases.
### Offloading Scripts To A Web Worker (experimental)[](https://nextjs.org/docs/pages/guides/scripts#offloading-scripts-to-a-web-worker-experimental)
> **Warning:** The `worker` strategy is not yet stable and does not yet work with the App Router. Use with caution.
Scripts that use the `worker` strategy are offloaded and executed in a web worker with
This strategy is still experimental and can only be used if the `nextScriptWorkers` flag is enabled in `next.config.js`:
next.config.js
```
module.exports = {
  experimental: {
    nextScriptWorkers: true,
  },
}
```

Then, run the development server and Next.js will guide you through the installation of the required packages to finish the setup:
pnpmnpmyarnbun
Terminal
```
pnpm dev
```

You'll see instructions like these: Please install Partytown by running `npm install @qwik.dev/partytown`
Once setup is complete, defining `strategy="worker"` will automatically instantiate Partytown in your application and offload the script to a web worker.
pages/home.tsx
TypeScript
JavaScript TypeScript
```
import Script from 'next/script'

export default function Home() {
  return (
    <>
      <Script src="https://example.com/script.js" strategy="worker" />
    </>
  )
}
```

There are a number of trade-offs that need to be considered when loading a third-party script in a web worker. Please see Partytown's
#### Using custom Partytown configuration[](https://nextjs.org/docs/pages/guides/scripts#using-custom-partytown-configuration)
Although the `worker` strategy does not require any additional configuration to work, Partytown supports the use of a config object to modify some of its settings, including enabling `debug` mode and forwarding events and triggers.
If you would like to add additional configuration options, you can include it within the `<Head />` component used in a [custom `_document.js`](https://nextjs.org/docs/pages/building-your-application/routing/custom-document):
_pages/document.jsx
```
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html>
      <Head>
        <script
          data-partytown-config
          dangerouslySetInnerHTML={{
            __html: `
              partytown = {
                lib: "/_next/static/~partytown/",
                debug: true
              };
            `,
          }}
        />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

In order to modify Partytown's configuration, the following conditions must be met:
  1. The `data-partytown-config` attribute must be used in order to overwrite the default configuration used by Next.js
  2. Unless you decide to save Partytown's library files in a separate directory, the `lib: "/_next/static/~partytown/"` property and value must be included in the configuration object in order to let Partytown know where Next.js stores the necessary static files.


> **Note** : If you are using an [asset prefix](https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix) and would like to modify Partytown's default configuration, you must include it as part of the `lib` path.
Take a look at Partytown's
### Inline Scripts[](https://nextjs.org/docs/pages/guides/scripts#inline-scripts)
Inline scripts, or scripts not loaded from an external file, are also supported by the Script component. They can be written by placing the JavaScript within curly braces:
```
<Script id="show-banner">
  {`document.getElementById('banner').classList.remove('hidden')`}
</Script>
```

Or by using the `dangerouslySetInnerHTML` property:
```
<Script
  id="show-banner"
  dangerouslySetInnerHTML={{
    __html: `document.getElementById('banner').classList.remove('hidden')`,
  }}
/>
```

> **Warning** : An `id` property must be assigned for inline scripts in order for Next.js to track and optimize the script.
### Executing Additional Code[](https://nextjs.org/docs/pages/guides/scripts#executing-additional-code)
Event handlers can be used with the Script component to execute additional code after a certain event occurs:
  * `onLoad`: Execute code after the script has finished loading.
  * `onReady`: Execute code after the script has finished loading and every time the component is mounted.
  * `onError`: Execute code if the script fails to load.


These handlers will only work when `next/script` is imported and used inside of a [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) where `"use client"` is defined as the first line of code:
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        onLoad={() => {
          console.log('Script has loaded')
        }}
      />
    </>
  )
}
```

Refer to the [`next/script`](https://nextjs.org/docs/pages/api-reference/components/script#onload) API reference to learn more about each event handler and view examples.
### Additional Attributes[](https://nextjs.org/docs/pages/guides/scripts#additional-attributes)
There are many DOM attributes that can be assigned to a `<script>` element that are not used by the Script component, like `<script>` element that is included in the HTML.
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        id="example-script"
        nonce="XUENAJFW"
        data-test="script"
      />
    </>
  )
}
```

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
