## Possible Ways to Fix It[](https://nextjs.org/docs/messages/next-script-for-ga#possible-ways-to-fix-it)
### Use `@next/third-parties` to add Google Analytics[](https://nextjs.org/docs/messages/next-script-for-ga#use-nextthird-parties-to-add-google-analytics)
**`@next/third-parties`**is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries in your Next.js application. It is available with Next.js 14 (install`next@latest`).
The `GoogleAnalytics` component can be used to include `gtag.js`). By default, it fetches the original scripts after hydration occurs on the page.
> **Recommendation** : If Google Tag Manager is already included in your application, you can configure Google Analytics directly using it, rather than including Google Analytics as a separate component. Refer to the `gtag.js`.
To load Google Analytics for all routes, include the component directly in your root layout and pass in your measurement ID:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { GoogleAnalytics } from '@next/third-parties/google'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
      <GoogleAnalytics gaId="G-XYZ" />
    </html>
  )
}
```

To load Google Analytics for a single route, include the component in your page file:
app/page.js
```
import { GoogleAnalytics } from '@next/third-parties/google'

export default function Page() {
  return <GoogleAnalytics gaId="G-XYZ" />
}
```

### Use `@next/third-parties` to add Google Tag Manager[](https://nextjs.org/docs/messages/next-script-for-ga#use-nextthird-parties-to-add-google-tag-manager)
The `GoogleTagManager` component can be used to add
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { GoogleTagManager } from '@next/third-parties/google'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <GoogleTagManager gtmId="GTM-XYZ" />
      <body>{children}</body>
    </html>
  )
}
```

To load Google Tag Manager for a single route, include the component in your page file:
app/page.js
```
import { GoogleTagManager } from '@next/third-parties/google'

export default function Page() {
  return <GoogleTagManager gtmId="GTM-XYZ" />
}
```
