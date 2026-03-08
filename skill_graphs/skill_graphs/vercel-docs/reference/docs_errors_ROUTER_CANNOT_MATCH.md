Menu
Menu
# ROUTER_CANNOT_MATCH
Last updated February 9, 2026
The `ROUTER_CANNOT_MATCH` error occurs when the router is unable to match the requested route to any of the known patterns. This could happen due to a misconfiguration in the routing setup or an erroneous request path.
502
ROUTER_CANNOT_MATCH:
Bad Gateway
##  [Troubleshoot](https://vercel.com/docs/errors/ROUTER_CANNOT_MATCH#troubleshoot)[](https://vercel.com/docs/errors/ROUTER_CANNOT_MATCH#troubleshoot)
Copy promptCopy prompt
I'm encountering an error and reviewing the docs at https://vercel.com/docs/errors/ROUTER_CANNOT_MATCH.md to understand what's happening. Please help me resolve this by: 1. **Suggest the fix**: Analyze my codebase context and propose what needs to be changed to resolve this error. If you do not have access to my codebase, ask me for the codebase and try to fix the error based on the information you have. 2. **Explain the root cause**: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. **Teach the concept**: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. **Show warning signs**: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. **Discuss alternatives**: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.
To troubleshoot this error, follow these steps:
  1. Review routing configuration: Check the [routing configuration](https://vercel.com/docs/redirects#configuration-redirects) to ensure that it is correctly set up to handle the requested route
  2. Verify request path: Ensure that the request path is correct and adheres to the expected patterns defined in the routing configuration
  3. Check for typos: Look for any typos or misconfigurations in the routing setup that might be causing the mismatch
  4. Review application logs: Inspect the [application logs](https://vercel.com/docs/deployments/logs) for any warnings or errors related to routing


* * *
Was this helpful?
Send
