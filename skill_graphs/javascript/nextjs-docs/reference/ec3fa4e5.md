## Possible Ways to Fix It[](https://nextjs.org/docs/messages/google-font-display#possible-ways-to-fix-it)
For most cases, the best font display strategy for custom fonts is `optional`.
pages/index.js
```
import Head from 'next/head'

export default function IndexPage() {
  return (
    <div>
      <Head>
        <link
          href="https://fonts.googleapis.com/css2?family=Krona+One&display=optional"
          rel="stylesheet"
        />
      </Head>
    </div>
  )
}
```

Specifying `display=optional` minimizes the risk of invisible text or layout shift. If swapping to the custom font after it has loaded is important to you, then use `display=swap` instead.
### When Not To Use It[](https://nextjs.org/docs/messages/google-font-display#when-not-to-use-it)
If you want to specifically display a font using an `auto`, `block`, or `fallback` strategy, then you can disable this rule.
