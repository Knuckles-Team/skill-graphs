##  [Region](https://vercel.com/docs/functions/runtimes/node-js#region)[](https://vercel.com/docs/functions/runtimes/node-js#region)
By default, Vercel Functions using the Edge runtime execute in the region closest to the incoming request. You can set one or more preferred regions using the route segment [config](https://vercel.com/docs/functions/runtimes/node-js#setting-regions-in-your-function) `preferredRegion` or specify a `regions` key within a config object to set one or more regions for your functions to execute in.
###  [Setting regions in your function](https://vercel.com/docs/functions/runtimes/node-js#setting-regions-in-your-function)[](https://vercel.com/docs/functions/runtimes/node-js#setting-regions-in-your-function)
If your function depends on a data source, you may want it to be close to that source for fast responses.
To configure which region (or multiple regions) you want your function to execute in, pass the [ID of your preferred region(s)](https://vercel.com/docs/regions#region-list) in the following way:
The `preferredRegion` option can be used to specify a single region using a string value, or multiple regions using a string array. See the
app/api/regional-example/route.ts
TypeScript
TypeScript JavaScript Bash
```
export const runtime = 'edge'; // 'nodejs' is the default
// execute this function on iad1 or hnd1, based on the connecting client location
export const preferredRegion = ['iad1', 'hnd1'];
export const dynamic = 'force-dynamic'; // no caching

export function GET(request: Request) {
  return new Response(
    `I am an Vercel Function! (executed on ${process.env.VERCEL_REGION})`,
    {
      status: 200,
    },
  );
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`
