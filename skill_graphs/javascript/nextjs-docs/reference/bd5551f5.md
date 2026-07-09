## Request Helpers[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#request-helpers)
API Routes provide built-in request helpers which parse the incoming request (`req`):
  * `req.cookies` - An object containing the cookies sent by the request. Defaults to `{}`
  * `req.query` - An object containing the `{}`
  * `req.body` - An object containing the body parsed by `content-type`, or `null` if no body was sent


### Custom config[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#custom-config)
Every API Route can export a `config` object to change the default configuration, which is the following:
```
export const config = {
  api: {
    bodyParser: {
      sizeLimit: '1mb',
    },
  },
  // Specifies the maximum allowed duration for this function to execute (in seconds)
  maxDuration: 5,
}
```

`bodyParser` is automatically enabled. If you want to consume the body as a `Stream` or with `false`.
One use case for disabling the automatic `bodyParsing` is to allow you to verify the raw body of a **webhook** request, for example
```
export const config = {
  api: {
    bodyParser: false,
  },
}
```

`bodyParser.sizeLimit` is the maximum size allowed for the parsed body, in any format supported by
```
export const config = {
  api: {
    bodyParser: {
      sizeLimit: '500kb',
    },
  },
}
```

`externalResolver` is an explicit flag that tells the server that this route is being handled by an external resolver like _express_ or _connect_. Enabling this option disables warnings for unresolved requests.
```
export const config = {
  api: {
    externalResolver: true,
  },
}
```

`responseLimit` is automatically enabled, warning when an API Routes' response body is over 4MB.
If you are not using Next.js in a serverless environment, and understand the performance implications of not using a CDN or dedicated media host, you can set this limit to `false`.
```
export const config = {
  api: {
    responseLimit: false,
  },
}
```

`responseLimit` can also take the number of bytes or any string format supported by `bytes`, for example `1000`, `'500kb'` or `'3mb'`. This value will be the maximum response size before a warning is displayed. Default is 4MB. (see above)
```
export const config = {
  api: {
    responseLimit: '8mb',
  },
}
```
