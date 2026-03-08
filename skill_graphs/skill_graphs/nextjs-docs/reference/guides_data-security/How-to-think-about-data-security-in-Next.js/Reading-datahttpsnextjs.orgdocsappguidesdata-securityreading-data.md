## Reading data[](https://nextjs.org/docs/app/guides/data-security#reading-data)
### Passing data from server to client[](https://nextjs.org/docs/app/guides/data-security#passing-data-from-server-to-client)
On the initial load, both Server and Client Components run on the server to generate HTML. However, they execute in isolated module systems. This ensures that Server Components can access private data and APIs, while Client Components cannot.
**Server Components:**
  * Run only on the server.
  * Can safely access environment variables, secrets, databases, and internal APIs.


**Client Components:**
  * Run on the server during pre-rendering, but must follow the same security assumptions as code running in the browser.
  * Must not access privileged data or server-only modules.


This ensures the app is secure by default, but it's possible to accidentally expose private data through how data is fetched or passed to components.
### Tainting[](https://nextjs.org/docs/app/guides/data-security#tainting)
To prevent accidental exposure of private data to the client, you can use React Taint APIs:
You can enable usage in your Next.js app with the [`experimental.taint`](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint) option in `next.config.js`:
next.config.js
```
module.exports = {
  experimental: {
    taint: true,
  },
}
```

This prevents the tainted objects or values from being passed to the client. However, it's an additional layer of protection, you should still filter and sanitize the data in your [DAL](https://nextjs.org/docs/app/guides/data-security#data-access-layer) before passing it to React's render context.
> **Good to know:**
>   * By default, environment variables are only available on the Server. Next.js exposes any environment variable prefixed with `NEXT_PUBLIC_` to the client. [Learn more](https://nextjs.org/docs/app/guides/environment-variables).
>   * Functions and classes are already blocked from being passed to Client Components by default.
>

### Preventing client-side execution of server-only code[](https://nextjs.org/docs/app/guides/data-security#preventing-client-side-execution-of-server-only-code)
To prevent server-only code from being executed on the client, you can mark a module with the
pnpmnpmyarnbun
Terminal
```
pnpm add server-only
```

lib/data.ts
```
import 'server-only'

//...
```

This ensures that proprietary code or internal business logic stays on the server by causing a build error if the module is imported in the client environment.
