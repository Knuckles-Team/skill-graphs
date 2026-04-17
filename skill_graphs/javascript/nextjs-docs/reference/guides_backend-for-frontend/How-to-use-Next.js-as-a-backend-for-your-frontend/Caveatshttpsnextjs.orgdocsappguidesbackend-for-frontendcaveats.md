## Caveats[](https://nextjs.org/docs/app/guides/backend-for-frontend#caveats)
### Server Components[](https://nextjs.org/docs/app/guides/backend-for-frontend#server-components)
Fetch data in Server Components directly from its source, not via Route Handlers.
For Server Components pre-rendered at build time, using Route Handlers will fail the build step. This is because, while building there is no server listening for these requests.
For Server Components rendered on demand, fetching from Route Handlers is slower due to the extra HTTP round trip between the handler and the render process.
> A server side `fetch` request uses absolute URLs. This implies an HTTP round trip, to an external server. During development, your own development server acts as the external server. At build time there is no server, and at runtime, the server is available through your public facing domain.
Server Components cover most data-fetching needs. However, fetching data client side might be necessary for:
  * Data that depends on client-only Web APIs:
    * Geo-location API
    * Storage API
    * Audio API
    * File API
  * Frequently polled data


For these, use community libraries like
### Server Actions[](https://nextjs.org/docs/app/guides/backend-for-frontend#server-actions)
Server Actions let you run server-side code from the client. Their primary purpose is to mutate data from your frontend client.
Server Actions are queued. Using them for data fetching introduces sequential execution.
###  `export` mode[](https://nextjs.org/docs/app/guides/backend-for-frontend#export-mode)
`export` mode outputs a static site without a runtime server. Features that require the Next.js runtime are [not supported](https://nextjs.org/docs/app/guides/static-exports#unsupported-features), because this mode produces a static site, and no runtime server.
In `export mode`, only `GET` Route Handlers are supported, in combination with the [`dynamic`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) route segment config, set to `'force-static'`.
This can be used to generate static HTML, JSON, TXT, or other files.
app/hello-world/route.ts
```
export const dynamic = 'force-static'

export function GET() {
  return new Response('Hello World', { status: 200 })
}
```

### Deployment environment[](https://nextjs.org/docs/app/guides/backend-for-frontend#deployment-environment)
Some hosts deploy Route Handlers as lambda functions. This means:
  * Route Handlers cannot share data between requests.
  * The environment may not support writing to File System.
  * Long-running handlers may be terminated due to timeouts.
  * WebSockets won’t work because the connection closes on timeout, or after the response is generated.
