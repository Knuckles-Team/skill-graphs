##  [Server-Side Rendering](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering)[](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering)
Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, verifying authentication or checking the geolocation of an incoming request.
Vercel offers SSR that scales down resource consumption when traffic is low, and scales up with traffic surges. This protects your site from accruing costs during periods of no traffic or losing business during high-traffic periods.
###  [Using Gatsby's SSR API with Vercel](https://vercel.com/docs/getting-started-with-vercel#using-gatsby's-ssr-api-with-vercel)[](https://vercel.com/docs/getting-started-with-vercel#using-gatsby's-ssr-api-with-vercel)
You can server-render pages in your Gatsby application on Vercel [Vercel functions](https://vercel.com/docs/functions).
To server-render a Gatsby page, you must export an `async` function called `getServerData`. The function can return an object with several optional keys, `props` key will be available in your page's props in the `serverData` property.
The following example demonstrates a server-rendered Gatsby page using `getServerData`:
pages/example.tsx
TypeScript
TypeScript JavaScript Bash
```
import type { GetServerDataProps, GetServerDataReturn } from 'gatsby';

type ServerDataProps = {
  hello: string;
};

const Page = (props: PageProps) => {
  const { name } = props.serverData;
  return <div>Hello, {name}</div>;
};

export async function getServerData(
  props: GetServerDataProps,
): GetServerDataReturn<ServerDataProps> {
  try {
    const res = await fetch(`https://example-data-source.com/api/some-data`);
    return {
      props: await res.json(),
    };
  } catch (error) {
    return {
      status: 500,
      headers: {},
      props: {},
    };
  }
}

export default Page;
```

To summarize, SSR with Gatsby on Vercel:
  * Scales to zero when not in use
  * Scales automatically with traffic increases
  * Has zero-configuration support for [`Cache-Control` headers](https://vercel.com/docs/cdn-cache), including `stale-while-revalidate`
  * Framework-aware infrastructure enables switching rendering between Edge/Node.js runtimes
