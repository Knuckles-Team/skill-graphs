##  [Check if you're running on the Edge runtime](https://vercel.com/docs/functions/runtimes/node-js#check-if-you're-running-on-the-edge-runtime)[](https://vercel.com/docs/functions/runtimes/node-js#check-if-you're-running-on-the-edge-runtime)
You can check if your function is running on the Edge runtime by checking the global `globalThis.EdgeRuntime` property. This can be helpful if you need to validate that your function is running on the Edge runtime in tests, or if you need to use a different API depending on the runtime.
```
if (typeof EdgeRuntime !== 'string') {
  // dead-code elimination is enabled for the code inside this block
}
```
