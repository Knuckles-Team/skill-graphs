# Edge Runtime
Last updated December 8, 2025
We recommend migrating from edge to Node.js for improved performance and reliability. Both runtimes run on [Fluid compute](https://vercel.com/docs/fluid-compute) with [Active CPU pricing](https://vercel.com/docs/functions/usage-and-pricing).
To convert your Vercel Function to use the Edge runtime, add the following code to your function:
app/api/my-function/route.ts
TypeScript
TypeScript JavaScript Bash
```
export const runtime = 'edge'; // 'nodejs' is the default

export function GET(request: Request) {
  return new Response(`I am an Vercel Function!`, {
    status: 200,
  });
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`
