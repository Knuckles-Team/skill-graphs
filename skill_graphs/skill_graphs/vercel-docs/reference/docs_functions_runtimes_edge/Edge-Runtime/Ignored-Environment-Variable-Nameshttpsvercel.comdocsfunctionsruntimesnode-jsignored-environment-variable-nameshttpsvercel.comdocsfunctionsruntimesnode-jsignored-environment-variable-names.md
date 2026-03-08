##  [Ignored Environment Variable Names](https://vercel.com/docs/functions/runtimes/node-js#ignored-environment-variable-names)[](https://vercel.com/docs/functions/runtimes/node-js#ignored-environment-variable-names)
Environment Variables can be accessed through the `process.env` object. Since JavaScript objects have methods to allow some operations on them, there are limitations on the names of Environment Variables to avoid having ambiguous code.
The following names will be ignored as Environment Variables to avoid overriding the `process.env` object prototype:
  * `constructor`
  * `__defineGetter__`
  * `__defineSetter__`
  * `hasOwnProperty`
  * `__lookupGetter__`
  * `__lookupSetter__`
  * `isPrototypeOf`
  * `propertyIsEnumerable`
  * `toString`
  * `valueOf`
  * `__proto__`
  * `toLocaleString`


Therefore, your code will always be able to use them with their expected behavior:
```
// returns `true`, if `process.env.MY_VALUE` is used anywhere & defined in the Vercel dashboard
process.env.hasOwnProperty('MY_VALUE');
```

* * *
[ Previous Runtimes ](https://vercel.com/docs/functions/runtimes)[ Next Advanced Node.js Usage ](https://vercel.com/docs/functions/runtimes/node-js/advanced-node-configuration)
Was this helpful?
Send
On this page
  * [Region](https://vercel.com/docs/functions/runtimes/node-js#region)
  * [Setting regions in your function](https://vercel.com/docs/functions/runtimes/node-js#setting-regions-in-your-function)
  * [Failover mode](https://vercel.com/docs/functions/runtimes/node-js#failover-mode)
  * [Maximum duration](https://vercel.com/docs/functions/runtimes/node-js#maximum-duration)
  * [Concurrency](https://vercel.com/docs/functions/runtimes/node-js#concurrency)
  * [Edge Runtime supported APIs](https://vercel.com/docs/functions/runtimes/node-js#edge-runtime-supported-apis)
  * [Supported APIs](https://vercel.com/docs/functions/runtimes/node-js#supported-apis)
  * [Network APIs](https://vercel.com/docs/functions/runtimes/node-js#network-apis)
  * [Encoding APIs](https://vercel.com/docs/functions/runtimes/node-js#encoding-apis)
  * [Stream APIs](https://vercel.com/docs/functions/runtimes/node-js#stream-apis)
  * [Crypto APIs](https://vercel.com/docs/functions/runtimes/node-js#crypto-apis)
  * [Other Web Standard APIs](https://vercel.com/docs/functions/runtimes/node-js#other-web-standard-apis)
  * [Check if you're running on the Edge runtime](https://vercel.com/docs/functions/runtimes/node-js#check-if-you're-running-on-the-edge-runtime)
  * [Compatible Node.js modules](https://vercel.com/docs/functions/runtimes/node-js#compatible-node.js-modules)
  * [Unsupported APIs](https://vercel.com/docs/functions/runtimes/node-js#unsupported-apis)
  * [Environment Variables](https://vercel.com/docs/functions/runtimes/node-js#environment-variables)
  * [Many Node.js APIs are not available](https://vercel.com/docs/functions/runtimes/node-js#many-node.js-apis-are-not-available)
  * [Dynamic code execution leads to a runtime error](https://vercel.com/docs/functions/runtimes/node-js#dynamic-code-execution-leads-to-a-runtime-error)
  * [Maximum Execution Duration](https://vercel.com/docs/functions/runtimes/node-js#maximum-execution-duration)
  * [Code size limit](https://vercel.com/docs/functions/runtimes/node-js#code-size-limit)
  * [Ignored Environment Variable Names](https://vercel.com/docs/functions/runtimes/node-js#ignored-environment-variable-names)


Copy as MarkdownGive feedbackAsk AI about this page
