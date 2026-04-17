##  [Code size limit](https://vercel.com/docs/functions/runtimes/node-js#code-size-limit)[](https://vercel.com/docs/functions/runtimes/node-js#code-size-limit)
Plan | Limit (after gzip compression)
---|---
Hobby | 1 MB
Pro | 2 MB
Enterprise | 4 MB
The maximum size for an Vercel Function using the Edge runtime includes your JavaScript code, imported libraries and files (such as fonts), and all files bundled in the function.
If you reach the limit, make sure the code you are importing in your function is used and is not too heavy. You can use a package size checker tool like
