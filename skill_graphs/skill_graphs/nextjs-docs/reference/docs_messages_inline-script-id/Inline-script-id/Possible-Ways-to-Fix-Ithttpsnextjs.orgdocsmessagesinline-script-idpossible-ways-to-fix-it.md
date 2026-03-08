## Possible Ways to Fix It[](https://nextjs.org/docs/messages/inline-script-id#possible-ways-to-fix-it)
Add an `id` attribute to the `next/script` component.
pages/_app.js
```
import Script from 'next/script'

export default function App({ Component, pageProps }) {
  return (
    <>
      <Script id="my-script">{`console.log('Hello world!');`}</Script>
      <Component {...pageProps} />
    </>
  )
}
```
