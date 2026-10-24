##  [Using a custom `app/entry.server` file](https://vercel.com/docs/getting-started-with-vercel#using-a-custom-app/entry.server-file)[](https://vercel.com/docs/getting-started-with-vercel#using-a-custom-app/entry.server-file)
By default, Vercel supplies an implementation of the `entry.server` file which is configured for streaming to work with Vercel Functions. This version will be used when no `entry.server` file is found in the project.
However, your application may define a customized `app/entry.server.jsx` or `app/entry.server.tsx` file if necessary. When doing so, your custom `entry.server` file should use the `handleRequest` function exported by `@vercel/react-router/entry.server`.
For example, to supply the `nonce` option and set the corresponding `Content-Security-Policy` response header:
/app/entry.server.tsx
TypeScript
TypeScript JavaScript Bash
```
import { handleRequest } from '@vercel/react-router/entry.server';
import type { AppLoadContext, EntryContext } from 'react-router';

export default async function (
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  routerContext: EntryContext,
  loadContext?: AppLoadContext,
): Promise<Response> {
  const nonce = crypto.randomUUID();
  const response = await handleRequest(
    request,
    responseStatusCode,
    responseHeaders,
    routerContext,
    loadContext,
    { nonce },
  );
  response.headers.set(
    'Content-Security-Policy',
    `script-src 'nonce-${nonce}'`,
  );
  return response;
}
```
