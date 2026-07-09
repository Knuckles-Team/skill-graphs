##  [Troubleshoot](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)[](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)
Copy promptCopy prompt
I'm encountering an error and reviewing the docs at https://vercel.com/docs/getting-started-with-vercel.md to understand what's happening. Please help me resolve this by: 1. **Suggest the fix**: Analyze my codebase context and propose what needs to be changed to resolve this error. If you do not have access to my codebase, ask me for the codebase and try to fix the error based on the information you have. 2. **Explain the root cause**: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. **Teach the concept**: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. **Show warning signs**: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. **Discuss alternatives**: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.
To troubleshoot this error, follow these steps:
  1. Check for typos: Verify that there are no typos in the parameter names or values
  2. Review request format: Ensure that the request URL is correctly formatted and includes the required parameters
     * The `q` parameter controls the quality of the image and must follow these rules:
       * The `q` parameter must be an integer
       * The `q` integer must be greater than or equal to 1
       * The `q` integer must be less than or equal to 100
       * The `q` integer must be the same as one specified in
     * The `w` parameter defines the width of the image and must follow these rules:
       * The `w` parameter must be an integer
       * The `w` integer must be the same as one specified in
     * The `url` parameter specifies the image location and must follow these rules:
       * The `url` parameter must start with `/`, `http://`, or `https://`
       * The `url` parameter must match one of the configured `next.config.js`
       * The `url` parameter must have a `Content-Type` header that starts with `image/`
       * The `url` parameter must have a response body less than 300 MB (or less than 100 MB for hobby), otherwise the image won't be optimized


Run `next dev` locally to reproduce the error and get additional details.
* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Troubleshoot](https://vercel.com/docs/getting-started-with-vercel#troubleshoot)


Copy as MarkdownGive feedbackAsk AI about this page
