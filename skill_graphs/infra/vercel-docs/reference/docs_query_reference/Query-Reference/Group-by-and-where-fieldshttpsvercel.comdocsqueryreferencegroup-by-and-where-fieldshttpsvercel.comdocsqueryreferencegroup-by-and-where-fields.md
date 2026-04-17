##  [Group by and where fields](https://vercel.com/docs/query/reference#group-by-and-where-fields)[](https://vercel.com/docs/query/reference#group-by-and-where-fields)
There are several fields available for use within the [Filter](https://vercel.com/docs/query/reference#filter) and [group by](https://vercel.com/docs/query/reference#group-by):
Field Name | Description |
---|---|---
`Request Hostname` | Group by the request's domains and subdomains |
`project` | Group by the request's project |
`Deployment ID` | Group by the request's deployment ID |
`HTTP Status` | Group by the request's HTTP response code |
`route` | The mapped path used by the request. For example, if you have a dynamic route like `/blog/[slug]` and a blog post is `/blog/my-blog-post`, the `route` is `/blog/[slug]` |
`Request Path` | The path used by the request. For example, if you have a dynamic route like `/blog/[slug]` and a blog post is `/blog/my-blog-post`, the `request_path` is `/blog/my-blog-post` |
`Cache Result` | The [cache](https://vercel.com/docs/cdn-cache#x-vercel-cache) status for the request |
`environment` | Group by the environment (`production` or [`preview`](https://vercel.com/docs/deployments/environments#preview-environment-pre-production)) |
`Request Method` | Group by the HTTP request method (`GET`, `POST`, `PUT`, etc.) |
`Referrer URL` | Group by the HTTP referrer URL |
`Referrer Hostname` | Group by the HTTP referrer domain |
`Client IP` | Group by the request's IP address |
`Client IP Country` | Group by the request's IP country |
`Client User Agent` | Group by the request's user agent |
`AS Number` | The autonomous system number (ASN) for the request. This is related to what network the request came from (either a home network or a cloud provider) |
`CDN Region` | Group by the [region](https://vercel.com/docs/regions) the request was routed to |
`ISR Cache Region` | Group by the ISR cache region |
`Cache Result` | Group by cache result |
`WAF Action` | Group by the WAF action taken by the [Vercel Firewall](https://vercel.com/docs/security/vercel-waf) (`deny`, `challenge`, `rate_limit`, `bypass` or `log`) |
`WAF Rule ID` | Group by the firewall rule ID |
`Skew Protection` | When `active`, the request would have been subject to [version skew](https://vercel.com/docs/skew-protection) but was protected, otherwise `inactive`. |
* * *
[ Previous Query ](https://vercel.com/docs/query)[ Next Monitoring ](https://vercel.com/docs/query/monitoring)
Was this helpful?
Send
On this page
  * [Metric](https://vercel.com/docs/query/reference#metric)
  * [Aggregations](https://vercel.com/docs/query/reference#aggregations)
  * [Filter](https://vercel.com/docs/query/reference#filter)
  * [Group by](https://vercel.com/docs/query/reference#group-by)
  * [Group by and where fields](https://vercel.com/docs/query/reference#group-by-and-where-fields)


Copy as MarkdownGive feedbackAsk AI about this page
