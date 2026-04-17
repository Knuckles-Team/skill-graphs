##  [Match conditions](https://vercel.com/docs/routing/project-routing-rules#match-conditions)[](https://vercel.com/docs/routing/project-routing-rules#match-conditions)
Each rule requires a path condition and supports additional conditions to narrow the match.
###  [Path matching](https://vercel.com/docs/routing/project-routing-rules#path-matching)[](https://vercel.com/docs/routing/project-routing-rules#path-matching)
Every rule matches against the request path. You can choose from three syntax modes:
Mode | Description | Example
---|---|---
Exact match | Matches a specific path | `/blog`
Path pattern | Express-style `:param` syntax with wildcards |  `/blog/:slug`, `/api/:path*`
Regex | Full regular expression | `^/posts/[0-9]+$`
###  [Additional conditions](https://vercel.com/docs/routing/project-routing-rules#additional-conditions)[](https://vercel.com/docs/routing/project-routing-rules#additional-conditions)
You can add conditions to match on other parts of the request. Each condition specifies a field, an operator, and a value.
Field | Description | Example use case
---|---|---
Host | The request hostname | Route differently for `app.example.com` vs `www.example.com`
Header | A request header key and value | Match requests with a specific `Accept-Language`
Cookie | A cookie key and value | Target users with a specific session or feature flag cookie
Query | A query parameter key and value | Match requests with `?preview=true`
Each condition supports these operators:
Operator | Description
---|---
Equals | Exact string match
Contains | Substring match
Matches regex | Regular expression match
Exists | Field is present (value isn't checked)
You can also negate any condition to match when the field is _missing_ or doesn't match.
