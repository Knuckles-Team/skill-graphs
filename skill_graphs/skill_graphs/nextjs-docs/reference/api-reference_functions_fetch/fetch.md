# fetch
Last updated February 27, 2026
Next.js extends the
In the browser, the `cache` option indicates how a fetch request will interact with the _browser's_ HTTP cache. With this extension, `cache` indicates how a _server-side_ fetch request will interact with the framework's persistent [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache).
You can call `fetch` with `async` and `await` directly within Server Components.
app/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page() {
  let data = await fetch('https://api.vercel.app/blog')
  let posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```
