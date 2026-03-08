## Lockfile[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports#lockfile)
When using URL imports, Next.js will create a `next.lock` directory containing a lockfile and fetched assets. This directory **must be committed to Git** , not ignored by `.gitignore`.
  * When running `next dev`, Next.js will download and add all newly discovered URL Imports to your lockfile.
  * When running `next build`, Next.js will use only the lockfile to build the application for production.


Typically, no network requests are needed and any outdated lockfile will cause the build to fail. One exception is resources that respond with `Cache-Control: no-cache`. These resources will have a `no-cache` entry in the lockfile and will always be fetched from the network on each build.
