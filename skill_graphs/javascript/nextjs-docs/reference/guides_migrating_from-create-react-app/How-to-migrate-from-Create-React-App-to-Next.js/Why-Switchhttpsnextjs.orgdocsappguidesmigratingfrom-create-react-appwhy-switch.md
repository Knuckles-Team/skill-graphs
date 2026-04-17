## Why Switch?[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#why-switch)
There are several reasons why you might want to switch from Create React App to Next.js:
### Slow initial page loading time[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#slow-initial-page-loading-time)
Create React App uses purely client-side rendering. Client-side only applications, also known as [single-page applications (SPAs)](https://nextjs.org/docs/app/guides/single-page-applications), often experience slow initial page loading time. This happens due to a couple of reasons:
  1. The browser needs to wait for the React code and your entire application bundle to download and run before your code is able to send requests to load data.
  2. Your application code grows with every new feature and dependency you add.


### No automatic code splitting[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#no-automatic-code-splitting)
The previous issue of slow loading times can be somewhat mitigated with code splitting. However, if you try to do code splitting manually, you can inadvertently introduce network waterfalls. Next.js provides automatic code splitting and tree-shaking built into its router and build pipeline.
### Network waterfalls[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#network-waterfalls)
A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One pattern for data fetching in a [SPA](https://nextjs.org/docs/app/guides/single-page-applications) is to render a placeholder, and then fetch data after the component has mounted. Unfortunately, a child component can only begin fetching data after its parent has finished loading its own data, resulting in a “waterfall” of requests.
While client-side data fetching is supported in Next.js, Next.js also lets you move data fetching to the server. This often eliminates client-server waterfalls altogether.
### Fast and intentional loading states[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#fast-and-intentional-loading-states)
With built-in support for [streaming through React Suspense](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming), you can define which parts of your UI load first and in what order, without creating network waterfalls.
This enables you to build pages that are faster to load and eliminate
### Choose the data fetching strategy[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#choose-the-data-fetching-strategy)
Depending on your needs, Next.js allows you to choose your data fetching strategy on a page or component-level basis. For example, you could fetch data from your CMS and render blog posts at build time (SSG) for quick load speeds, or fetch data at request time (SSR) when necessary.
### Proxy[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#proxy)
[Next.js Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) allows you to run code on the server before a request is completed. For instance, you can avoid a flash of unauthenticated content by redirecting a user to a login page in the proxy for authenticated-only pages. You can also use it for features like A/B testing, experimentation, and [internationalization](https://nextjs.org/docs/app/guides/internationalization).
### Built-in Optimizations[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#built-in-optimizations)
[Images](https://nextjs.org/docs/app/api-reference/components/image), [fonts](https://nextjs.org/docs/app/api-reference/components/font), and [third-party scripts](https://nextjs.org/docs/app/guides/scripts) often have a large impact on an application’s performance. Next.js includes specialized components and APIs that automatically optimize them for you.
