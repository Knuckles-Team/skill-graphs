## Platform Support[](https://nextjs.org/docs/app/api-reference/functions/after#platform-support)
Deployment Option | Supported
---|---
[Node.js server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server) | Yes
[Docker container](https://nextjs.org/docs/app/getting-started/deploying#docker) | Yes
[Static export](https://nextjs.org/docs/app/getting-started/deploying#static-export) | No
[Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters) | Platform-specific
Learn how to [configure `after`](https://nextjs.org/docs/app/guides/self-hosting#after) when self-hosting Next.js.
Reference: supporting `after` for serverless platforms
Using `after` in a serverless context requires waiting for asynchronous tasks to finish after the response has been sent. In Next.js and Vercel, this is achieved using a primitive called `waitUntil(promise)`, which extends the lifetime of a serverless invocation until all promises passed to
If you want your users to be able to run `after`, you will have to provide your implementation of `waitUntil` that behaves in an analogous way.
When `after` is called, Next.js will access `waitUntil` like this:
```
const RequestContext = globalThis[Symbol.for('@next/request-context')]
const contextValue = RequestContext?.get()
const waitUntil = contextValue?.waitUntil
```

Which means that `globalThis[Symbol.for('@next/request-context')]` is expected to contain an object like this:
```
type NextRequestContext = {
  get(): NextRequestContextValue | undefined
}

type NextRequestContextValue = {
  waitUntil?: (promise: Promise<any>) => void
}
```

Here is an example of the implementation.
```
import { AsyncLocalStorage } from 'node:async_hooks'

const RequestContextStorage = new AsyncLocalStorage<NextRequestContextValue>()

// Define and inject the accessor that next.js will use
const RequestContext: NextRequestContext = {
  get() {
    return RequestContextStorage.getStore()
  },
}
globalThis[Symbol.for('@next/request-context')] = RequestContext

const handler = (req, res) => {
  const contextValue = { waitUntil: YOUR_WAITUNTIL }
  // Provide the value
  return RequestContextStorage.run(contextValue, () => nextJsHandler(req, res))
}
```
