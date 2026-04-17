## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#examples)
### Streaming with Suspense[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#streaming-with-suspense)
In addition to `loading.js`, you can also manually create Suspense Boundaries for your own UI components. The App Router supports streaming with
`<Suspense>` works by wrapping a component that performs an asynchronous action (e.g. fetch data), showing fallback UI (e.g. skeleton, spinner) while it's happening, and then swapping in your component once the action completes.
app/dashboard/page.tsx
TypeScript
JavaScript TypeScript
```
import { Suspense } from 'react'
import { PostFeed, Weather } from './Components'

export default function Posts() {
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        <PostFeed />
      </Suspense>
      <Suspense fallback={<p>Loading weather...</p>}>
        <Weather />
      </Suspense>
    </section>
  )
}
```

By using Suspense, you get the benefits of:
  1. **Streaming Server Rendering** - Progressively rendering HTML from the server to the client.
  2. **Selective Hydration** - React prioritizes what components to make interactive first based on user interaction.


For more Suspense examples and use cases, please see the
