## Reference[](https://nextjs.org/docs/app/api-reference/functions/cookies#reference)
### Methods[](https://nextjs.org/docs/app/api-reference/functions/cookies#methods)
The following methods are available:
Method | Return Type | Description
---|---|---
`get('name')` | Object | Accepts a cookie name and returns an object with the name and value.
`getAll()` | Array of objects | Returns a list of all the cookies with a matching name.
`has('name')` | Boolean | Accepts a cookie name and returns a boolean based on if the cookie exists.
`set(name, value, options)` | - | Accepts a cookie name, value, and options and sets the outgoing request cookie.
`delete(name)` | - | Accepts a cookie name and deletes the cookie.
`toString()` | String | Returns a string representation of the cookies.
### Options[](https://nextjs.org/docs/app/api-reference/functions/cookies#options)
When setting a cookie, the following properties from the `options` object are supported:
Option | Type | Description
---|---|---
`name` | String | Specifies the name of the cookie.
`value` | String | Specifies the value to be stored in the cookie.
`expires` | Date | Defines the exact date when the cookie will expire.
`maxAge` | Number | Sets the cookie’s lifespan in seconds.
`domain` | String | Specifies the domain where the cookie is available.
`path` | String, default: `'/'` | Limits the cookie's scope to a specific path within the domain.
`secure` | Boolean | Ensures the cookie is sent only over HTTPS connections for added security.
`httpOnly` | Boolean | Restricts the cookie to HTTP requests, preventing client-side access.
`sameSite` | Boolean, `'lax'`, `'strict'`, `'none'` | Controls the cookie's cross-site request behavior.
`priority` | String (`"low"`, `"medium"`, `"high"`) | Specifies the cookie's priority
`partitioned` | Boolean | Indicates whether the cookie is
The only option with a default value is `path`.
To learn more about these options, see the
