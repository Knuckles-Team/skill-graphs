##  [Maximum Execution Duration](https://vercel.com/docs/functions/runtimes/node-js#maximum-execution-duration)[](https://vercel.com/docs/functions/runtimes/node-js#maximum-execution-duration)
Middleware with the `edge` runtime configured must begin sending a response within 25 seconds.
You may continue streaming a response beyond that time and you can continue with asynchronous workloads in the background, after returning the response.
