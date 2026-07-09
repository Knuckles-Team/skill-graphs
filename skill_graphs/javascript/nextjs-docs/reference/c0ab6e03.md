## Good to know[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#good-to-know)
  * `draftMode` is an **asynchronous** function that returns a promise. You must use `async/await` or React's
    * In version 14 and earlier, `draftMode` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * A new bypass cookie value will be generated each time you run `next build`. This ensures that the bypass cookie can’t be guessed.
  * To test Draft Mode locally over HTTP, your browser will need to allow third-party cookies and local storage access.
