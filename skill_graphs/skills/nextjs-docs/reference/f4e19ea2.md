## Local dev vs. production[](https://nextjs.org/docs/app/guides/local-development#local-dev-vs-production)
The development process with `next dev` is different than `next build` and `next start`.
`next dev` compiles routes in your application as you open or navigate to them. This enables you to start the dev server without waiting for every route in your application to compile, which is both faster and uses less memory. Running a production build applies other optimizations, like minifying files and creating content hashes, which are not needed for local development.
