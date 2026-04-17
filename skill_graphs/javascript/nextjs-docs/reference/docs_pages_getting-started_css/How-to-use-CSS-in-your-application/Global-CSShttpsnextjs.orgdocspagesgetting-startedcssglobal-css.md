## Global CSS[](https://nextjs.org/docs/pages/getting-started/css#global-css)
You can use global CSS to apply styles across your application.
Import the stylesheet in the `pages/_app.js` file to apply the styles to **every route** in your application:
pages/_app.js
```
import '@/styles/global.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Due to the global nature of stylesheets, and to avoid conflicts, you should import them inside [`pages/_app.js`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app).
