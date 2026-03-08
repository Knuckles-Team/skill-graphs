##  [How to fix](https://vercel.com/docs/conformance/rules/NO_INLINE_SVG#how-to-fix)[](https://vercel.com/docs/conformance/rules/NO_INLINE_SVG#how-to-fix)
If you hit this issue, you can resolve it by using SVGs as an `next.config.js` file, and use the `unoptimized` component prop.
.app/page.js
```
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/logo.svg"
      width={100}
      height={100}
      alt="Logo of ACME"
      unoptimized
    />
  )
}
```

* * *
Was this helpful?
Send
On this page
  * [How to fix](https://vercel.com/docs/conformance/rules/NO_INLINE_SVG#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
