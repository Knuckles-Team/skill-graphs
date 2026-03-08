## Using getStaticProps to fetch data from a CMS[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#using-getstaticprops-to-fetch-data-from-a-cms)
The following example shows how you can fetch a list of blog posts from a CMS.
pages/blog.tsx
TypeScript
JavaScript TypeScript
```
// posts will be populated at build time by getStaticProps()
export default function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It won't be called on client-side, so you can even do
// direct database queries.
export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}
```

The [`getStaticProps` API reference](https://nextjs.org/docs/pages/api-reference/functions/get-static-props) covers all parameters and props that can be used with `getStaticProps`.
