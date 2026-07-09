##  [Using a Wasm file](https://vercel.com/docs/functions/runtimes#using-a-wasm-file)[](https://vercel.com/docs/functions/runtimes#using-a-wasm-file)
You can use Wasm in your production deployment or locally, using [`vercel dev`](https://vercel.com/docs/cli/dev).
  1. ###  [Get your Wasm file ready](https://vercel.com/docs/functions/runtimes#get-your-wasm-file-ready)[](https://vercel.com/docs/functions/runtimes#get-your-wasm-file-ready)
     * Compile your existing C, Go, and Rust project to create a binary `.wasm` file. For this example, we use a
     * Copy the compiled file (in our example, `ts` definition for the function such as
  2. ###  [Create an API route for calling the Wasm file](https://vercel.com/docs/functions/runtimes#create-an-api-route-for-calling-the-wasm-file)[](https://vercel.com/docs/functions/runtimes#create-an-api-route-for-calling-the-wasm-file)
With `nodejs` runtime that uses [Fluid compute](https://vercel.com/docs/fluid-compute) by default:
api/wasm/route.ts
```
import path from 'node:path';
import fs from 'node:fs';
import type * as addWasmModule from '../../../add.wasm'; // import type definitions at the root of your project

const wasmBuffer = fs.readFileSync(path.resolve(process.cwd(), './add.wasm')); // path from root
const wasmPromise = WebAssembly.instantiate(wasmBuffer);

export async function GET(request: Request) {
  const url = new URL(request.url);
  const num = Number(url.searchParams.get('number') || 10);
  const { add_one: addOne } = (await wasmPromise).instance
    .exports as typeof addWasmModule;

  return new Response(`got: ${addOne(num)}`);
}
```

  3. ###  [Call the Wasm endpoint](https://vercel.com/docs/functions/runtimes#call-the-wasm-endpoint)[](https://vercel.com/docs/functions/runtimes#call-the-wasm-endpoint)
     * Run the project locally with `vercel dev`
     * Browse to `http://localhost:3000/api/wasm?number=12` which should return `got: 13`


* * *
[ Previous Streaming ](https://vercel.com/docs/functions/streaming-functions)[ Next Node.js ](https://vercel.com/docs/functions/runtimes/node-js)
Was this helpful?
Send
On this page
  * [Using a Wasm file](https://vercel.com/docs/functions/runtimes#using-a-wasm-file)
  * [Get your Wasm file ready](https://vercel.com/docs/functions/runtimes#get-your-wasm-file-ready)
  * [Create an API route for calling the Wasm file](https://vercel.com/docs/functions/runtimes#create-an-api-route-for-calling-the-wasm-file)
  * [Call the Wasm endpoint](https://vercel.com/docs/functions/runtimes#call-the-wasm-endpoint)


Copy as MarkdownGive feedbackAsk AI about this page
