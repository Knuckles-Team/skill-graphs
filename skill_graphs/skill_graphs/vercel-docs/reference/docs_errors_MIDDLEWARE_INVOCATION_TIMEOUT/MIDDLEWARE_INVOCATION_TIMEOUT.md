# MIDDLEWARE_INVOCATION_TIMEOUT
Last updated February 9, 2026
The `MIDDLEWARE_INVOCATION_TIMEOUT` error occurs when an Routing Middleware takes [longer than the allowed execution time](https://vercel.com/docs/functions/runtimes/edge#maximum-execution-duration) to complete or doesn't send a response chunk for a certain amount of time. This can be caused by long-running processes within the function or external dependencies that fail to respond in a timely manner.
If your backend API takes time to respond, we recommend [streaming the response](https://vercel.com/docs/functions/streaming-functions) to avoid the idle timeout.
504
MIDDLEWARE_INVOCATION_TIMEOUT:
Gateway Timeout
