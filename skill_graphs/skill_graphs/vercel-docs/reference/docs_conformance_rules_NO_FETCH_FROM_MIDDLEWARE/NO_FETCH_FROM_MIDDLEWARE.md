# NO_FETCH_FROM_MIDDLEWARE
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
`fetch` call, it may be to a backend that is not globally distributed, in which case the latency of the middleware function will be really slow. To prevent this, `fetch` calls that can be made from middleware are flagged and reviewed to make sure that it looks like an appropriate use.
