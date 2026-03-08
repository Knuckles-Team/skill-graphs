# EDGE_FUNCTION_INVOCATION_TIMEOUT
Last updated February 9, 2026
The `EDGE_FUNCTION_INVOCATION_TIMEOUT` error occurs when an Edge Function takes longer than the allowed execution time to complete or doesn't send a response chunk for a certain amount of time. This can be caused by long-running processes within the function or external dependencies that fail to respond in a timely manner.
If your backend API takes time to respond, we recommend [streaming the response](https://vercel.com/docs/functions/streaming-functions) to avoid the idle timeout. For longer-running workloads, consider migrating to [Fluid compute](https://vercel.com/docs/fluid-compute) which provides significantly longer durations and optimized performance.
504
EDGE_FUNCTION_INVOCATION_TIMEOUT:
Gateway Timeout
