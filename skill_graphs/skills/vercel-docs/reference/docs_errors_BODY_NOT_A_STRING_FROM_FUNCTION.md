Menu
Menu
# BODY_NOT_A_STRING_FROM_FUNCTION
Last updated February 9, 2026
The `BODY_NOT_A_STRING_FROM_FUNCTION` error occurs when a function returns a body that is not a string. It's essential that functions return a string body to ensure that they can be correctly processed and executed.
502
BODY_NOT_A_STRING_FROM_FUNCTION:
Bad Gateway
##  [Troubleshoot](https://vercel.com/docs/errors/BODY_NOT_A_STRING_FROM_FUNCTION#troubleshoot)[](https://vercel.com/docs/errors/BODY_NOT_A_STRING_FROM_FUNCTION#troubleshoot)
Copy promptCopy prompt
I'm encountering an error and reviewing the docs at https://vercel.com/docs/errors/BODY_NOT_A_STRING_FROM_FUNCTION.md to understand what's happening. Please help me resolve this by: 1. **Suggest the fix**: Analyze my codebase context and propose what needs to be changed to resolve this error. If you do not have access to my codebase, ask me for the codebase and try to fix the error based on the information you have. 2. **Explain the root cause**: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. **Teach the concept**: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. **Show warning signs**: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. **Discuss alternatives**: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.
To troubleshoot this error, follow these steps:
  1. Check function return type: Ensure that the function is structured to return a string. If the function is returning a different data type, modify the function to return a string, using `JSON.stringify()` if necessary
  2. Review function code: Inspect the function code for any logic that might cause a non-string value to be returned
  3. Check data types: If the function is processing input data or retrieving data from external sources, ensure that the data is being correctly converted to a string before being returned
  4. Review function logs: Check the [function logs](https://vercel.com/docs/runtime-logs#type) for any errors or warnings that might indicate why a non-string value is being returned


* * *
Was this helpful?
Send
