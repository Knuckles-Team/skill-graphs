# How to preview content with Draft Mode in Next.js
Last updated February 27, 2026
In the [Pages documentation](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts) and the [Data Fetching documentation](https://nextjs.org/docs/pages/building-your-application/data-fetching), we talked about how to pre-render a page at build time (**Static Generation**) using `getStaticProps` and `getStaticPaths`.
Static Generation is useful when your pages fetch data from a headless CMS. However, it’s not ideal when you’re writing a draft on your headless CMS and want to view the draft immediately on your page. You’d want Next.js to render these pages at **request time** instead of build time and fetch the draft content instead of the published content. You’d want Next.js to bypass Static Generation only for this specific case.
Next.js has a feature called **Draft Mode** which solves this problem. Here are instructions on how to use it.
