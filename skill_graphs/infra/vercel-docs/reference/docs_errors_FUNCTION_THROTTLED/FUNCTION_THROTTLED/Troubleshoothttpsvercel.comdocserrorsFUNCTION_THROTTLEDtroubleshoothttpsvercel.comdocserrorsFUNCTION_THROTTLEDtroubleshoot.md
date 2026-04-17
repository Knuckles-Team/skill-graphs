##  [Troubleshoot](https://vercel.com/docs/errors/FUNCTION_THROTTLED#troubleshoot)[](https://vercel.com/docs/errors/FUNCTION_THROTTLED#troubleshoot)
Copy promptCopy prompt
I'm encountering an error and reviewing the docs at https://vercel.com/docs/errors/FUNCTION_THROTTLED.md to understand what's happening. Please help me resolve this by: 1. **Suggest the fix**: Analyze my codebase context and propose what needs to be changed to resolve this error. If you do not have access to my codebase, ask me for the codebase and try to fix the error based on the information you have. 2. **Explain the root cause**: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. **Teach the concept**: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. **Show warning signs**: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. **Discuss alternatives**: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.
To troubleshoot this error, follow these steps:
  1. Check application logs: Review the application logs to identify any specific errors related to the Vercel Function being invoked. For example, your function might be waiting for a slow backend API without a reasonable timeout. These information can be found at the host URL under [the `/_logs` path](https://vercel.com/docs/deployments/build-features#logs-view), as well as the [Observability](https://vercel.com/docs/observability) section in the sidebar in the Vercel dashboard.
  2. Handle request spikes: If you're experiencing a sudden spike in requests, consider using the [Vercel Firewall](https://vercel.com/docs/vercel-firewall) to block unwanted traffic, or enabling [Rate Limiting](https://vercel.com/docs/security/vercel-waf/rate-limiting) to limit the number of requests per second.
  3. Optimize your function: Review your function code to ensure it's optimized for performance. For example, you can use [Vercel's CDN Cache](https://vercel.com/docs/cdn-cache) to cache responses and reduce the number of invocations. You can also enable [fluid compute](https://vercel.com/docs/fluid-compute) to handle more requests concurrently on a single function instance.


* * *
Was this helpful?
Send
On this page
  * [Troubleshoot](https://vercel.com/docs/errors/FUNCTION_THROTTLED#troubleshoot)


Copy as MarkdownGive feedbackAsk AI about this page
