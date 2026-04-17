# NO_RESPONSE_FROM_FUNCTION
Last updated February 9, 2026
The `NO_RESPONSE_FROM_FUNCTION` error occurs when a function invocation completes without returning a response. This might happen if the function encounters an error that prevents it from responding, or if it fails to generate a response within the allowed execution time.
Potential causes include:
  * A global uncaught exception
  * A global unhandled rejection
  * A deployment that introduced incorrect syntax


502
NO_RESPONSE_FROM_FUNCTION:
Bad Gateway
####  [Troubleshoot](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)[](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)
Copy promptCopy prompt
I'm encountering an error and reviewing the docs at https://vercel.com/docs/errors/NO_RESPONSE_FROM_FUNCTION.md to understand what's happening. Please help me resolve this by: 1. **Suggest the fix**: Analyze my codebase context and propose what needs to be changed to resolve this error. If you do not have access to my codebase, ask me for the codebase and try to fix the error based on the information you have. 2. **Explain the root cause**: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. **Teach the concept**: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. **Show warning signs**: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. **Discuss alternatives**: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.
To troubleshoot this error, follow these steps:
  1. Verify return statements: Ensure that the function has the necessary return statements to generate a response
  2. Check the function logs: Open the [realtime request logs](https://vercel.com/docs/logs#function-logs) for the application in a separate tab - this tab must be kept open while reproducing the error
  3. Review realtime logs: Repeat the application behavior that led to the error being thrown and review the realtime request logs where it will now show
     * Use the information contained within the error logs to understand where the function is failing
  4. Use Log Drains: Create a [Log Drain](https://vercel.com/docs/drains) if you do not have one yet, to persist errors from Vercel functions
  5. Check external dependencies: If the function relies on external services or APIs, ensure they are responding in a timely manner


* * *
Was this helpful?
Send
On this page
  * [Troubleshoot](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)


Copy as MarkdownGive feedbackAsk AI about this page
