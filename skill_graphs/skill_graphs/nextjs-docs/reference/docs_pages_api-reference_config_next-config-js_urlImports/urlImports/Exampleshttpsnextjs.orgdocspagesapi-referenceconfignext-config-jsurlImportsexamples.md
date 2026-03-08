## Examples[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#examples)
### Skypack[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#skypack)
```
import confetti from 'https://cdn.skypack.dev/canvas-confetti'
import { useEffect } from 'react'

export default () => {
  useEffect(() => {
    confetti()
  })
  return <p>Hello</p>
}
```

### Static Image Imports[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#static-image-imports)
```
import Image from 'next/image'
import logo from 'https://example.com/assets/logo.png'

export default () => (
  <div>
    <Image src={logo} placeholder="blur" />
  </div>
)
```

### URLs in CSS[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#urls-in-css)
```
.className {
  background: url('https://example.com/assets/hero.jpg');
}
```

### Asset Imports[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#asset-imports)
```
const logo = new URL('https://example.com/assets/file.txt', import.meta.url)

console.log(logo.pathname)

// prints "/_next/static/media/file.a9727b5d.txt"
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
