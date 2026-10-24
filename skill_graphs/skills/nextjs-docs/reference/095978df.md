## Behavior[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#behavior)
  * `getServerSideProps` runs on the server.
  * `getServerSideProps` can only be exported from a **page**.
  * `getServerSideProps` returns JSON.
  * When a user visits a page, `getServerSideProps` will be used to fetch data at request time, and the data is used to render the initial HTML of the page.
  * `props` passed to the page component can be viewed on the client as part of the initial HTML. This is to allow the page to be `props`.
  * When a user visits the page through [`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) or [`next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router), Next.js sends an API request to the server, which runs `getServerSideProps`.
  * You do not have to call a Next.js [API Route](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) to fetch data when using `getServerSideProps` since the function runs on the server. Instead, you can call a CMS, database, or other third-party APIs directly from inside `getServerSideProps`.


> **Good to know:**
>   * See [`getServerSideProps` API reference](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props) for parameters and props that can be used with `getServerSideProps`.
>   * You can use the
>
