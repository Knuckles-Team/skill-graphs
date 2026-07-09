## Polyfills[](https://nextjs.org/docs/architecture/supported-browsers#polyfills)
We inject
  * `whatwg-fetch` and `unfetch`.
  * `object-assign`, `object.assign`, and `core-js/object/assign`.


If any of your dependencies include these polyfills, they’ll be eliminated automatically from the production build to avoid duplication.
In addition, to reduce bundle size, Next.js will only load these polyfills for browsers that require them. The majority of the web traffic globally will not download these polyfills.
### Custom Polyfills[](https://nextjs.org/docs/architecture/supported-browsers#custom-polyfills)
If your own code or any external npm dependencies require features not supported by your target browsers (such as IE 11), you need to add polyfills yourself.
#### In App Router[](https://nextjs.org/docs/architecture/supported-browsers#in-app-router)
To include polyfills, you can import them into the [`instrumentation-client.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client).
instrumentation-client.ts
```
import './polyfills'
```

#### In Pages Router[](https://nextjs.org/docs/architecture/supported-browsers#in-pages-router)
In this case, you should add a top-level import for the **specific polyfill** you need in your [Custom `<App>`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) or the individual component.
pages/_app.tsx
TypeScript
JavaScript TypeScript
```
import './polyfills'

import type { AppProps } from 'next/app'

export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

#### Conditionally loading polyfills[](https://nextjs.org/docs/architecture/supported-browsers#conditionally-loading-polyfills)
The best approach is to isolate unsupported features to specific UI sections and conditionally load the polyfill if needed.
hooks/analytics.ts
TypeScript
JavaScript TypeScript
```
import { useCallback } from 'react'

export const useAnalytics = () => {
  const tracker = useCallback(async (data: unknown) => {
    if (!('structuredClone' in globalThis)) {
      import('polyfills/structured-clone').then((mod) => {
        globalThis.structuredClone = mod.default
      })
    }

    /* Do some work that uses structured clone */
  }, [])

  return tracker
}
```
