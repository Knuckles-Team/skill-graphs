##  `getInitialProps` with `App`[](https://nextjs.org/docs/pages/building-your-application/routing/custom-app#getinitialprops-with-app)
Using [`getInitialProps`](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props) in `App` will disable [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) for pages without [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props).
**We do not recommend using this pattern.** Instead, consider [incrementally adopting](https://nextjs.org/docs/app/guides/migrating/app-router-migration) the App Router, which allows you to more easily fetch data for pages and layouts.
pages/_app.tsx
TypeScript
JavaScript TypeScript
```
import App, { AppContext, AppInitialProps, AppProps } from 'next/app'

type AppOwnProps = { example: string }

export default function MyApp({
  Component,
  pageProps,
  example,
}: AppProps & AppOwnProps) {
  return (
    <>
      <p>Data: {example}</p>
      <Component {...pageProps} />
    </>
  )
}

MyApp.getInitialProps = async (
  context: AppContext
): Promise<AppOwnProps & AppInitialProps> => {
  const ctx = await App.getInitialProps(context)

  return { ...ctx, example: 'data' }
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
