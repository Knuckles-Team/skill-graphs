# NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This check disallows dependencies on client libraries, such as `react` and `next/router` in Next.js middleware. Since middleware runs on the server and runs on every request, this code is not able to run any client side code and it should have a small bundle size to improve loading and execution times.
