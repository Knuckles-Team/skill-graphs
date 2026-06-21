## How do Server and Client Components work in Next.js?[](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs)
### On the server[](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-server)
On the server, Next.js uses React's APIs to orchestrate rendering. The rendering work is split into chunks, by individual route segments ([layouts and pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)):
  * **Server Components** are rendered into a special data format called the React Server Component Payload (RSC Payload).
  * **Client Components** and the RSC Payload are used to [pre-render](https://nextjs.org/docs/app/guides/caching#rendering-strategies) HTML.


> **What is the React Server Component Payload (RSC)?**
> The RSC Payload is a compact binary representation of the rendered React Server Components tree. It's used by React on the client to update the browser's DOM. The RSC Payload contains:
>   * The rendered result of Server Components
>   * Placeholders for where Client Components should be rendered and references to their JavaScript files
>   * Any props passed from a Server Component to a Client Component
>

### On the client (first load)[](https://nextjs.org/docs/app/getting-started/server-and-client-components#on-the-client-first-load)
Then, on the client:
  1. **HTML** is used to immediately show a fast non-interactive preview of the route to the user.
  2. **RSC Payload** is used to reconcile the Client and Server Component trees.
  3. **JavaScript** is used to hydrate Client Components and make the application interactive.


> **What is hydration?**
> Hydration is React's process for attaching
### Subsequent Navigations[](https://nextjs.org/docs/app/getting-started/server-and-client-components#subsequent-navigations)
On subsequent navigations:
  * The **RSC Payload** is prefetched and cached for instant navigation.
  * **Client Components** are rendered entirely on the client, without the server-rendered HTML.
