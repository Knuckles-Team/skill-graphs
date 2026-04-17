##  [Available actions](https://vercel.com/docs/routing/project-routing-rules#available-actions)[](https://vercel.com/docs/routing/project-routing-rules#available-actions)
When a request matches a rule, one or more actions run. Actions fall into two groups: primary actions (mutually exclusive) and modify actions (combinable).
###  [Primary actions](https://vercel.com/docs/routing/project-routing-rules#primary-actions)[](https://vercel.com/docs/routing/project-routing-rules#primary-actions)
You can use one primary action per rule.
Action | Description | Configuration
---|---|---
Rewrite | Forwards the request to a different URL. The visitor's browser still shows the original URL. | A destination URL. Can be internal (`/new-path`) or external (`https://api.example.com/:path*`).
Redirect | Sends the visitor's browser to a different URL with an HTTP status code. | A destination URL and a status code: `301` (permanent), `302` (found), `307` (temporary), or `308` (permanent).
Set status code | Returns a specific HTTP status code without changing the URL. | An HTTP status code (e.g., `404`, `503`).
###  [Modify actions](https://vercel.com/docs/routing/project-routing-rules#modify-actions)[](https://vercel.com/docs/routing/project-routing-rules#modify-actions)
You can combine multiple modify actions with each other, or pair one with a primary action.
Action | Description | Operations
---|---|---
Modify response headers | Adds, changes, or removes response headers. |  Set: replace or add a header. Append: add a value to an existing header. Delete: remove a header.
Modify request headers | Adds, changes, or removes headers on the incoming request before it reaches your application. |  Set, Append, Delete
Modify request query | Adds, changes, or removes query parameters on the incoming request. |  Set, Append, Delete
