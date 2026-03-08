# How to lazy load Client Components and libraries
Last updated February 27, 2026
It allows you to defer loading of **Client Components** and imported libraries, and only include them in the client bundle when they're needed. For example, you might want to defer loading a modal until a user clicks to open it.
There are two ways you can implement lazy loading in Next.js:
  1. Using [Dynamic Imports](https://nextjs.org/docs/app/guides/lazy-loading#nextdynamic) with `next/dynamic`
  2. Using


By default, Server Components are automatically [streaming](https://nextjs.org/docs/app/api-reference/file-conventions/loading) to progressively send pieces of UI from the server to the client. Lazy loading applies to Client Components.
