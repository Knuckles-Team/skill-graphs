## Linking to dynamic paths[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#linking-to-dynamic-paths)
You can also use interpolation to create the path, which comes in handy for [dynamic route segments](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes). For example, to show a list of posts which have been passed to the component as a prop:
```
import Link from 'next/link'

function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link href={`/blog/${encodeURIComponent(post.slug)}`}>
            {post.title}
          </Link>
        </li>
      ))}
    </ul>
  )
}

export default Posts
```

Alternatively, using a URL Object:
```
import Link from 'next/link'

function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link
            href={{
              pathname: '/blog/[slug]',
              query: { slug: post.slug },
            }}
          >
            {post.title}
          </Link>
        </li>
      ))}
    </ul>
  )
}

export default Posts
```

Now, instead of using interpolation to create the path, we use a URL object in `href` where:
  * `pathname` is the name of the page in the `pages` directory. `/blog/[slug]` in this case.
  * `query` is an object with the dynamic segment. `slug` in this case.
