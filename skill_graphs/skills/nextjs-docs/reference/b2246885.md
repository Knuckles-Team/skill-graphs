# template.js
Last updated February 27, 2026
A **template** file is similar to a [layout](https://nextjs.org/docs/app/getting-started/layouts-and-pages#creating-a-layout) in that it wraps a layout or page. Unlike layouts that persist across routes and maintain state, templates are given a unique key, meaning children Client Components reset their state on navigation.
They are useful when you need to:
  * Resynchronize `useEffect` on navigation.
  * Reset the state of a child Client Components on navigation. For example, an input field.
  * To change default framework behavior. For example, Suspense boundaries inside layouts only show a fallback on first load, while templates show it on every navigation.
