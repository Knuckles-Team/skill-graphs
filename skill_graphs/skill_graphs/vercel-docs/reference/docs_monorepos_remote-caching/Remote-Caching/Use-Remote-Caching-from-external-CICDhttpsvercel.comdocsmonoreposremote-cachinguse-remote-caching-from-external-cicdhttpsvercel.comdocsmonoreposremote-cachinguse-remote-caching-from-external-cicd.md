##  [Use Remote Caching from external CI/CD](https://vercel.com/docs/monorepos/remote-caching#use-remote-caching-from-external-ci/cd)[](https://vercel.com/docs/monorepos/remote-caching#use-remote-caching-from-external-ci/cd)
To use Vercel Remote Caching with Turborepo from an external CI/CD system, you can set the following environment variables in your CI/CD system:
  * `TURBO_TOKEN`: A [Vercel Access Token](https://vercel.com/docs/rest-api#authentication)
  * `TURBO_TEAM`: The slug of the Vercel team to share the artifacts with


When these environment variables are set, Turborepo will use Vercel Remote Caching to store task artifacts.
