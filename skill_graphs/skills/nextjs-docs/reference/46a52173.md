## Usage[](https://nextjs.org/docs/pages/building-your-application/routing/custom-app#usage)
To override the default `App`, create the file `pages/_app` as shown below:
pages/_app.tsx
TypeScript
JavaScript TypeScript
```
import type { AppProps } from 'next/app'

export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

The `Component` prop is the active `page`, so whenever you navigate between routes, `Component` will change to the new `page`. Therefore, any props you send to `Component` will be received by the `page`.
`pageProps` is an object with the initial props that were preloaded for your page by one of our [data fetching methods](https://nextjs.org/docs/pages/building-your-application/data-fetching), otherwise it's an empty object.
> **Good to know** :
>   * If your app is running and you added a custom `App`, you'll need to restart the development server. Only required if `pages/_app.js` didn't exist before.
>   * `App` does not support Next.js [Data Fetching methods](https://nextjs.org/docs/pages/building-your-application/data-fetching) like [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) or [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props).
>
