## Understanding Cookie Behavior in Server Components[](https://nextjs.org/docs/app/api-reference/functions/cookies#understanding-cookie-behavior-in-server-components)
When working with cookies in Server Components, it's important to understand that cookies are fundamentally a client-side storage mechanism:
  * **Reading cookies** works in Server Components because you're accessing the cookie data that the client's browser sends to the server in the HTTP request headers.
  * **Setting cookies** is not supported during Server Component rendering. To modify cookies, invoke a Server Function from the client or use a Route Handler.


The server can only send instructions (via `Set-Cookie` headers) to tell the browser to store cookies - the actual storage happens on the client side. This is why cookie operations that modify state (`.set`, `.delete`) must be performed in a Server Function or Route Handler where the response headers can be properly set.
