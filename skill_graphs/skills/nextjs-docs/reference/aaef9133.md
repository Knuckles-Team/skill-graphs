## Good to know[](https://nextjs.org/docs/app/api-reference/functions/after#good-to-know)
  * `after` will be executed even if the response didn't complete successfully. Including when an error is thrown or when `notFound` or `redirect` is called.
  * You can use React `cache` to deduplicate functions called inside `after`.
  * `after` can be nested inside other `after` calls, for example, you can create utility functions that wrap `after` calls to add additional functionality.
