## Overview[](https://nextjs.org/docs/app/guides/caching#overview)
Here's a high-level overview of the different caching mechanisms and their purpose:
Mechanism | What | Where | Purpose | Duration
---|---|---|---|---
[Request Memoization](https://nextjs.org/docs/app/guides/caching#request-memoization) | Return values of functions | Server | Reuse data in a React Component tree | Per-request lifecycle
[Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache) | Data | Server | Store data across user requests and deployments | Persistent (can be revalidated)
[Full Route Cache](https://nextjs.org/docs/app/guides/caching#full-route-cache) | HTML and RSC payload | Server | Reduce rendering cost and improve performance | Persistent (can be revalidated)
[Router Cache](https://nextjs.org/docs/app/guides/caching#client-side-router-cache) | RSC Payload | Client | Reduce server requests on navigation | User session or time-based
By default, Next.js will cache as much as possible to improve performance and reduce cost. This means routes are **statically rendered** and data requests are **cached** unless you opt out. The diagram below shows the default caching behavior: when a route is statically rendered at build time and when a static route is first visited.
![Diagram showing the default caching behavior in Next.js for the four mechanisms, with HIT, MISS and SET at build time and when a route is first visited.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fcaching-overview.png&w=3840&q=75)![Diagram showing the default caching behavior in Next.js for the four mechanisms, with HIT, MISS and SET at build time and when a route is first visited.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fcaching-overview.png&w=3840&q=75)
Caching behavior changes depending on whether the route is statically or dynamically rendered, data is cached or uncached, and whether a request is part of an initial visit or a subsequent navigation. Depending on your use case, you can configure the caching behavior for individual routes and data requests.
Fetch caching is **not** supported in `proxy`. Any fetches done inside of your `proxy` will be uncached.
