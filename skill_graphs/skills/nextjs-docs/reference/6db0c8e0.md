## What is a Single-Page Application?[](https://nextjs.org/docs/app/guides/single-page-applications#what-is-a-single-page-application)
The definition of a SPA varies. We’ll define a “strict SPA” as:
  * **Client-side rendering (CSR)** : The app is served by one HTML file (e.g. `index.html`). Every route, page transition, and data fetch is handled by JavaScript in the browser.
  * **No full-page reloads** : Rather than requesting a new document for each route, client-side JavaScript manipulates the current page’s DOM and fetches data as needed.


Strict SPAs often require large amounts of JavaScript to load before the page can be interactive. Further, client data waterfalls can be challenging to manage. Building SPAs with Next.js can address these issues.
