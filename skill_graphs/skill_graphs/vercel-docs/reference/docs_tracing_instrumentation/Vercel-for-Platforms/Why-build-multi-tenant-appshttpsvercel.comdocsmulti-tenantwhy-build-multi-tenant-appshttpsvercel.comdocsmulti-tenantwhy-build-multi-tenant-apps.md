##  [Why build multi-tenant apps?](https://vercel.com/docs/multi-tenant#why-build-multi-tenant-apps)[](https://vercel.com/docs/multi-tenant#why-build-multi-tenant-apps)
Some popular multi-tenant apps on Vercel include:
  * Content platforms:
  * Documentation platforms:
  * Website and ecommerce store builders: [Super](https://vercel.com/blog/super-serves-thousands-of-domains-on-one-project-with-next-js-and-vercel),
  * B2B SaaS platforms:


For example, you might have:
  * A root domain for your platform: `acme.com`
  * Subdomains for tenants: `tenant1.acme.com`, `tenant2.acme.com`
  * Fully custom domains for certain customers: `tenantcustomdomain.com`


Vercel's platform automatically issues [SSL certificates](https://vercel.com/docs/domains/working-with-ssl), handles DNS routing via its Anycast network, and ensures each of your tenants gets low-latency responses from the closest CDN region.
