## Why Switch?[](https://nextjs.org/docs/pages/guides/migrating/from-vite#why-switch)
There are several reasons why you might want to switch from Vite to Next.js:
### Slow initial page loading time[](https://nextjs.org/docs/pages/guides/migrating/from-vite#slow-initial-page-loading-time)
If you have built your application with the
  1. The browser needs to wait for the React code and your entire application bundle to download and run before your code is able to send requests to load some data.
  2. Your application code grows with every new feature and extra dependency you add.


### No automatic code splitting[](https://nextjs.org/docs/pages/guides/migrating/from-vite#no-automatic-code-splitting)
The previous issue of slow loading times can be somewhat managed with code splitting. However, if you try to do code splitting manually, you'll often make performance worse. It's easy to inadvertently introduce network waterfalls when code-splitting manually. Next.js provides automatic code splitting built into its router.
### Network waterfalls[](https://nextjs.org/docs/pages/guides/migrating/from-vite#network-waterfalls)
A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One common pattern for data fetching in an SPA is to initially render a placeholder, and then fetch data after the component has mounted. Unfortunately, this means that a child component that fetches data can't start fetching until the parent component has finished loading its own data.
While fetching data on the client is supported with Next.js, it also gives you the option to shift data fetching to the server, which can eliminate client-server waterfalls.
### Fast and intentional loading states[](https://nextjs.org/docs/pages/guides/migrating/from-vite#fast-and-intentional-loading-states)
With built-in support for [streaming through React Suspense](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming), you can be more intentional about which parts of your UI you want to load first and in what order without introducing network waterfalls.
This enables you to build pages that are faster to load and eliminate
### Choose the data fetching strategy[](https://nextjs.org/docs/pages/guides/migrating/from-vite#choose-the-data-fetching-strategy)
Depending on your needs, Next.js allows you to choose your data fetching strategy on a page and component basis. You can decide to fetch at build time, at request time on the server, or on the client. For example, you can fetch data from your CMS and render your blog posts at build time, which can then be efficiently cached on a CDN.
### Proxy[](https://nextjs.org/docs/pages/guides/migrating/from-vite#proxy)
[Next.js Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) allows you to run code on the server before a request is completed. This is especially useful to avoid having a flash of unauthenticated content when the user visits an authenticated-only page by redirecting the user to a login page. The proxy is also useful for experimentation and [internationalization](https://nextjs.org/docs/app/guides/internationalization).
### Built-in Optimizations[](https://nextjs.org/docs/pages/guides/migrating/from-vite#built-in-optimizations)
[Images](https://nextjs.org/docs/app/api-reference/components/image), [fonts](https://nextjs.org/docs/app/api-reference/components/font), and [third-party scripts](https://nextjs.org/docs/app/guides/scripts) often have significant impact on an application's performance. Next.js comes with built-in components that automatically optimize those for you.
