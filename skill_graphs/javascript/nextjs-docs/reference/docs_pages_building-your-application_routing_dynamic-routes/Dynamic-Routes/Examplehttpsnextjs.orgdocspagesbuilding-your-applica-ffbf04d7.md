## Example[](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#example)
For example, a blog could include the following route `pages/blog/[slug].js` where `[slug]` is the Dynamic Segment for blog posts.
```
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()
  return <p>Post: {router.query.slug}</p>
}
```

Route | Example URL | `params`
---|---|---
`pages/blog/[slug].js` | `/blog/a` | `{ slug: 'a' }`
`pages/blog/[slug].js` | `/blog/b` | `{ slug: 'b' }`
`pages/blog/[slug].js` | `/blog/c` | `{ slug: 'c' }`
