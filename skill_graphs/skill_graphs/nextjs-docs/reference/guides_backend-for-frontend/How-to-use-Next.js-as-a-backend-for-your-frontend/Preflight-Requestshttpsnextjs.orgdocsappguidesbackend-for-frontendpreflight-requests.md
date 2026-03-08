## Preflight Requests[](https://nextjs.org/docs/app/guides/backend-for-frontend#preflight-requests)
Preflight requests use the `OPTIONS` method to ask the server if a request is allowed based on origin, method, and headers.
If `OPTIONS` is not defined, Next.js adds it automatically and sets the `Allow` header based on the other defined methods.
  * [CORS](https://nextjs.org/docs/app/api-reference/file-conventions/route#cors)
