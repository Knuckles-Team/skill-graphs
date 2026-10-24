## Environment Variables[](https://nextjs.org/docs/pages/guides/self-hosting#environment-variables)
Next.js can support both build time and runtime environment variables.
**By default, environment variables are only available on the server**. To expose an environment variable to the browser, it must be prefixed with `NEXT_PUBLIC_`. However, these public environment variables will be inlined into the JavaScript bundle during `next build`.
To read runtime environment variables, we recommend using `getServerSideProps` or [incrementally adopting the App Router](https://nextjs.org/docs/app/guides/migrating/app-router-migration).
This allows you to use a singular Docker image that can be promoted through multiple environments with different values.
> **Good to know:**
>   * You can run code on server startup using the [`register` function](https://nextjs.org/docs/app/guides/instrumentation).
>
