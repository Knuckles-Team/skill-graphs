## Reference[](https://nextjs.org/docs/app/api-reference/functions/after#reference)
### Parameters[](https://nextjs.org/docs/app/api-reference/functions/after#parameters)
  * A callback function which will be executed after the response (or prerender) is finished.


### Duration[](https://nextjs.org/docs/app/api-reference/functions/after#duration)
`after` will run for the platform's default or configured max duration of your route. If your platform supports it, you can configure the timeout limit using the [`maxDuration`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#maxduration) route segment config.
