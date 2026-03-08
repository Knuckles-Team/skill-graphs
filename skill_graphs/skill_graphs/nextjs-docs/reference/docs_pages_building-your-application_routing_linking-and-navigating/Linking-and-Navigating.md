# Linking and Navigating
Last updated February 27, 2026
The Next.js router allows you to do client-side route transitions between pages, similar to a single-page application.
A React component called `Link` is provided to do this client-side route transition.
```
import Link from 'next/link'

function Home() {
  return (
    <ul>
      <li>
        <Link href="/">Home</Link>
      </li>
      <li>
        <Link href="/about">About Us</Link>
      </li>
      <li>
        <Link href="/blog/hello-world">Blog Post</Link>
      </li>
    </ul>
  )
}

export default Home
```

The example above uses multiple links. Each one maps a path (`href`) to a known page:
  * `/` → `pages/index.js`
  * `/about` → `pages/about.js`
  * `/blog/hello-world` → `pages/blog/[slug].js`


Any `<Link />` in the viewport (initially or through scroll) will be prefetched by default (including the corresponding data) for pages using [Static Generation](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props). The corresponding data for [server-rendered](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) routes is fetched _only when_ the `<Link />` is clicked.
