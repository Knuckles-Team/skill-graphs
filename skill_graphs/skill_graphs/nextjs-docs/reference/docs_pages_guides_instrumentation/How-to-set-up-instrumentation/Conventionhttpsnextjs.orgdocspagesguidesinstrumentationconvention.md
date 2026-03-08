## Convention[](https://nextjs.org/docs/pages/guides/instrumentation#convention)
To set up instrumentation, create `instrumentation.ts|js` file in the **root directory** of your project (or inside the [`src`](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder) folder if using one).
Then, export a `register` function in the file. This function will be called **once** when a new Next.js server instance is initiated, and must complete before the server is ready to handle requests.
For example, to use Next.js with
instrumentation.ts
TypeScript
JavaScript TypeScript
```
import { registerOTel } from '@vercel/otel'

export function register() {
  registerOTel('next-app')
}
```

See the
> **Good to know** :
>   * The `instrumentation` file should be in the root of your project and not inside the `app` or `pages` directory. If you're using the `src` folder, then place the file inside `src` alongside `pages` and `app`.
>   * If you use the [`pageExtensions` config option](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions) to add a suffix, you will also need to update the `instrumentation` filename to match.
>
