# Script
Last updated February 27, 2026
This API reference will help you understand how to use [props](https://nextjs.org/docs/pages/api-reference/components/script#props) available for the Script Component. For features and usage, please see the [Optimizing Scripts](https://nextjs.org/docs/app/guides/scripts) page.
app/dashboard/page.tsx
TypeScript
JavaScript TypeScript
```
import Script from 'next/script'

export default function Dashboard() {
  return (
    <>
      <Script src="https://example.com/script.js" />
    </>
  )
}
```
