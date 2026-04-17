## Why This Error Occurred[](https://nextjs.org/docs/messages/no-html-link-for-pages#why-this-error-occurred)
An `<a>` element was used to navigate to a page route without using the `next/link` component, causing unnecessary full-page refreshes.
The `Link` component is required to enable client-side route transitions between pages and provide a single-page app experience.
