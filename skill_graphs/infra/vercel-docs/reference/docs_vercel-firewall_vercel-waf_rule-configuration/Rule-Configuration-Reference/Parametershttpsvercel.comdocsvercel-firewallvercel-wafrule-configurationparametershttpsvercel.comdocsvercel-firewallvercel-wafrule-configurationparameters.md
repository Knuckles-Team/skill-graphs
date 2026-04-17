##  [Parameters](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#parameters)[](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#parameters)
Custom Rule Parameters Parameter | Description | Example | Note
---|---|---|---
Request Path | The full request path on the incoming request, always starting with a leading `/` |  `/api`, `/signup/new` |
Route | The framework determined `x-matched-path` | `/blog/[slug]` | When matching on the route, the custom rule will run after middleware. If the rule blocks a request, middleware charges could be incurred
Server Action Name | The Next.js server action name as defined by your codebase | `app/auth/actions.ts#getUser` | Requires Next.js 15.5. When matching on the server action name, the custom rule will run after middleware. If the rule blocks a request, middleware charges could be incurred
Raw Path | The raw request path, ignoring any parsing or normalizing that might be done at the framework level |  `/api/`, `/signup/new/` |
Method | The HTTP method used to make the request |  `GET`, `POST` |
User Agent | The HTTP user agent used to make the request | `curl` |
Request Header | The request header on the original request. Define both the header key and value you want to match |  | You cannot match headers set by middleware, as the rule runs before middleware is invoked
Query | Any incoming query parameter on the original request. Define both the query key and value you want to match |  |
Cookie | Any incoming cookie on the original request. Define both the query key and value you want to match |  |
Hostname | The hostname used for the incoming request |  | This applies to projects with multiple domains such as platforms that assign a domain to each user of the platform
IP Address | The original or forwarded IP address on the incoming request |  `10.0.0.1`, `10.0.0.1/32` |
Protocol | The HTTP protocol of the original request |  `HTTP/1.1`, `HTTP/2.0` |
Environment | The Vercel Environment that received this request |  | Preview or Production
Vercel Region | The Vercel region that received this request | [Regions list](https://vercel.com/docs/regions#region-list) |
Continent | The continent based on the client IP address |  | A shorthand for the `x-vercel-ip-continent` header
State | The state (Country Region) based on the client IP address |  | A shorthand for the `x-vercel-ip-country-region` header
Country | The country based on the client IP address |  | A shorthand for the `x-vercel-ip-country` header
City | The city based on the client IP address |  | A shorthand for the `x-vercel-ip-city` header
AS Number | The Autonomous System Number based on the client IP address | Digits only, e.g. `12345` | Digits only
JA3 Digest | The calculated TLS digest of the incoming request |  |
JA4 Digest | The calculated TLS digest of the incoming request |  |
@vercel/firewall | ID for a rate limit instrumented in code via the `@vercel/firewall` package |  |
