Menu
Menu
# RESOURCE_NOT_FOUND
Last updated February 9, 2026
The `RESOURCE_NOT_FOUND` error indicates that a requested resource is not available or cannot be found. This error typically arises when a request is made for a resource that either does not exist or is currently inaccessible.
404
RESOURCE_NOT_FOUND:
Not Found
##  [Troubleshoot](https://vercel.com/docs/errors/RESOURCE_NOT_FOUND#troubleshoot)[](https://vercel.com/docs/errors/RESOURCE_NOT_FOUND#troubleshoot)
Copy promptCopy prompt
I'm encountering an error and reviewing the docs at https://vercel.com/docs/errors/RESOURCE_NOT_FOUND.md to understand what's happening. Please help me resolve this by: 1. **Suggest the fix**: Analyze my codebase context and propose what needs to be changed to resolve this error. If you do not have access to my codebase, ask me for the codebase and try to fix the error based on the information you have. 2. **Explain the root cause**: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. **Teach the concept**: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. **Show warning signs**: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. **Discuss alternatives**: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.
To troubleshoot this error, follow these steps:
  1. Verify resource existence: Confirm that the resource you're attempting to access exists. Check for any typos or errors in the resource name or path
  2. Review access permissions: Ensure that your application or function has the necessary permissions to access the resource
  3. Inspect resource path: Double-check the path or URL to the resource. Ensure it is correctly formatted and corresponds to the intended resource
  4. Check application configuration: Review your application's configuration settings to ensure they are correctly set up to locate and access the resource
  5. Review logs: Consult your [application logs](https://vercel.com/docs/runtime-logs) for more details or clues as to why the resource could not be found. This can provide insights into whether the issue is due to an incorrect path, permissions, or other reasons


Additionally, the error can also occur in the context of the [Vercel REST API](https://vercel.com/docs/rest-api), where it is similar to the [HTTP 500 Internal Server Error](https://vercel.com/docs/rest-api/reference/errors#resource-not-found). In this case, the error message will contain the details of the resource that could not be found.
* * *
Was this helpful?
Send
