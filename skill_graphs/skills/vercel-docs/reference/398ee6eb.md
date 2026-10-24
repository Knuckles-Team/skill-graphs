##  [Conflicting functions and builds configuration](https://vercel.com/docs/getting-started-with-vercel#conflicting-functions-and-builds-configuration)[](https://vercel.com/docs/getting-started-with-vercel#conflicting-functions-and-builds-configuration)
There are two ways to configure Vercel functions in your project: [functions](https://vercel.com/docs/project-configuration#functions) _or_ [`builds`](https://vercel.com/docs/project-configuration#builds). However, only one of them may be used at a time - they cannot be used in conjunction.
For most cases, it is recommended to use the `functions` property because it supports more features, such as:
  * Allows configuration of the amount of memory that the Vercel Function is provided with
  * More reliable because it requires a specific npm package version for the `runtime` property
  * Supports "clean URLs" by default, which means that the Vercel functions are automatically accessible without their file extension in the URL


However, the [`builds`](https://vercel.com/docs/project-configuration#builds) property will remain supported for backward compatibility purposes.
