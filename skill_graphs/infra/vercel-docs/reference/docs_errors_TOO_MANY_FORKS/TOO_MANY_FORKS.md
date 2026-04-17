# TOO_MANY_FORKS
Last updated February 9, 2026
The `TOO_MANY_FORKS` error occurs when too many forks are generated while processing the request. This usually happens when matching too many conditional routes, which could lead to a loop or excessive resource usage.
You cannot have more than 5 `has` routes matched on a single path.
502
TOO_MANY_FORKS:
Bad Gateway
####  [Troubleshoot](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)[](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)
Copy promptCopy prompt
I'm encountering an error and reviewing the docs at https://vercel.com/docs/getting-started-with-vercel.md to understand what's happening. Please help me resolve this by: 1. **Suggest the fix**: Analyze my codebase context and propose what needs to be changed to resolve this error. If you do not have access to my codebase, ask me for the codebase and try to fix the error based on the information you have. 2. **Explain the root cause**: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. **Teach the concept**: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. **Show warning signs**: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. **Discuss alternatives**: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.
To troubleshoot this error, follow these steps:
  1. Review routing configuration: Reduce the number of [rewrites](https://vercel.com/docs/rewrites), [redirects](https://vercel.com/docs/redirects#configuration-redirects), or [headers](https://vercel.com/docs/headers) with a `has` key (conditional route) that match the erroring request path
  2. Check for recursive logic: Ensure there isn't any recursive logic in the routing configuration that could lead to excessive forking
  3. Handle unhandled exceptions: Check the [application logs](https://vercel.com/docs/deployments/logs) for any unhandled exceptions that may be causing the error


* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Troubleshoot](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)


Copy as MarkdownGive feedbackAsk AI about this page
