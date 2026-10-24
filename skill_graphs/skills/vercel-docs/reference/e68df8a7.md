# NEXTJS_NO_GET_INITIAL_PROPS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
`getInitialProps` is an older Next.js API for server-side rendering that can usually be replaced with `getServerSideProps` or `getStaticProps` for more performant and secure code.
`getInitialProps` runs on both the server and the client after page load, so the JavaScript bundle will contain any dependencies used by `getInitialProps`. This means that it is possible for unintended code to be included in the client side bundle, for example, code that should only be used on the server such as database connections.
If you need to avoid a server-round trip when performing a client side transition, `getInitialProps` could be used. However, if you do not, `getServerSideProps` is a good API to use instead so that the code remains on the server and does not bloat the JavaScript bundle, or `getStaticProps` can be used if the page can be statically generated at build time.
This rule is for highlighting these concerns and while there are still valid use cases for using `getInitialProps` if you do need to do data fetching on both the client and the server, they should be reviewed and approved.
