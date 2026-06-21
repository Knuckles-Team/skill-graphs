## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-styled-jsx-in-document#possible-ways-to-fix-it)
If you need shared CSS for all of your pages, take a look at the [Custom `App`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) file or define a custom layout.
For example, consider the following stylesheet named `styles.css`:
styles.css
```
body {
  font-family:
    'SF Pro Text', 'SF Pro Icons', 'Helvetica Neue', 'Helvetica', 'Arial',
    sans-serif;
  padding: 20px 20px 60px;
  max-width: 680px;
  margin: 0 auto;
}
```

Create a `pages/_app.{js,tsx}` file if not already present. Then, import the `styles.css` file.
pages/_app.js
```
import '../styles.css'

// This default export is required in a new `pages/_app.js` file.
export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

These styles (`styles.css`) will apply to all pages and components in your application.
