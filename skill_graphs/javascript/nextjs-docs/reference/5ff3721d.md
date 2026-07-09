## FAQ[](https://nextjs.org/docs/app/api-reference/functions/redirect#faq)
### Why does `redirect` use 307 and 308?[](https://nextjs.org/docs/app/api-reference/functions/redirect#why-does-redirect-use-307-and-308)
When using `redirect()` you may notice that the status codes used are `307` for a temporary redirect, and `308` for a permanent redirect. While traditionally a `302` was used for a temporary redirect, and a `301` for a permanent redirect, many browsers changed the request method of the redirect, from a `POST` to `GET` request when using a `302`, regardless of the origins request method.
Taking the following example of a redirect from `/users` to `/people`, if you make a `POST` request to `/users` to create a new user, and are conforming to a `302` temporary redirect, the request method will be changed from a `POST` to a `GET` request. This doesn't make sense, as to create a new user, you should be making a `POST` request to `/people`, and not a `GET` request.
The introduction of the `307` status code means that the request method is preserved as `POST`.
  * `302` - Temporary redirect, will change the request method from `POST` to `GET`
  * `307` - Temporary redirect, will preserve the request method as `POST`


The `redirect()` method uses a `307` by default, instead of a `302` temporary redirect, meaning your requests will _always_ be preserved as `POST` requests.
