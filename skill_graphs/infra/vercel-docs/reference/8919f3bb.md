# Advanced Configuration
Last updated May 21, 2025
For an advanced configuration, you can create a `vercel.json` file to use [Runtimes](https://vercel.com/docs/functions/runtimes) and other customizations. To view more about the properties you can customize, see the [Configuring Functions](https://vercel.com/docs/functions/configuring-functions) and [Project config with vercel.json](https://vercel.com/docs/project-configuration).
If your use case requires that you work asynchronously with the results of a function invocation, you may need to consider a queuing, pooling, or [streaming](https://vercel.com/docs/functions/streaming-functions) approach because of how functions are created on Vercel.
