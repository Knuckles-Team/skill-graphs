# NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule will analyze each Next.js page's `getServerSideProps` to see if the context parameter is being used and if not then it will fail.
When using `getServerSideProps` to render a Next.js page on the server, if the page doesn't require any information from the request, consider using `getStaticProps`. If you are using `getServerSideProps` to refresh the data on each page load, consider using `revalidate` property to control how often the page is regenerated. If you are using `getServerSideProps` to randomize the data on each page load, consider moving that logic to the client instead and use `getStaticProps` to reuse the statically generated page.
