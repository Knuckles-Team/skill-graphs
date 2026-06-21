##  [Group by and where fields](https://vercel.com/docs/logs#group-by-and-where-fields)[](https://vercel.com/docs/logs#group-by-and-where-fields)
There are several fields available for use within the [where](https://vercel.com/docs/logs#where) and [group by](https://vercel.com/docs/logs#group-by) clauses:
Field Name | Description |
---|---|---
`host` | Group by the request's domains and subdomains |
`path_type` | Group by the request's [resource type](https://vercel.com/docs/logs#path-types) |
`project_id` | Group by the request's project ID |
`status` | Group by the request's HTTP response code |
`source_path` | The mapped path used by the request. For example, if you have a dynamic route like `/blog/[slug]` and a blog post is `/blog/my-blog-post`, the `source_path` is `/blog/[slug]` |
`request_path` | The path used by the request. For example, if you have a dynamic route like `/blog/[slug]` and a blog post is `/blog/my-blog-post`, the `request_path` is `/blog/my-blog-post` |
`cache` | The [cache](https://vercel.com/docs/cdn-cache#x-vercel-cache) status for the request |
`error_details` | Group by the [errors](https://vercel.com/docs/errors) that were thrown on Vercel |
`deployment_id` | Group by the request's deployment ID |
`environment` | Group by the environment (`production` or [`preview`](https://vercel.com/docs/deployments/environments#preview-environment-pre-production)) |
`request_method` | Group by the HTTP request method (`GET`, `POST`, `PUT`, etc.) |
`http_referer` | Group by the HTTP referer |
`public_ip` | Group by the request's IP address |
`user_agent` | Group by the request's user agent |
`asn` | The autonomous system number (ASN) for the request. This is related to what network the request came from (either a home network or a cloud provider) |
`bot_name` | Group by the request's bot crawler name. This field will contain the name of a known crawler (e.g. Google, Bing) |
`region` | Group by the [region](https://vercel.com/docs/regions) the request was routed to |
`waf_action` | Group by the WAF action taken by the [Vercel Firewall](https://vercel.com/docs/security/vercel-waf) (`deny`, `challenge`, `rate_limit`, `bypass` or `log`) |
`action` | Group by the action taken by [Vercel DDoS Mitigations](https://vercel.com/docs/security/ddos-mitigation) (`deny` or `challenge`) |
`skew_protection` | When `active`, the request would have been subject to [version skew](https://vercel.com/docs/deployments/skew-protection) but was protected. When `inactive`, the request did not require skew protection to be fulfilled. |
###  [Path types](https://vercel.com/docs/logs#path-types)[](https://vercel.com/docs/logs#path-types)
All your project's resources like pages, functions, and images have a path type:
Path Type | Description
---|---
`static` | A static asset (`.js`, `.css`, `.png`, etc.)
`func` | A [Vercel Function](https://vercel.com/docs/functions)
`external` | A resource that is outside of Vercel. This is usually caused when you have [rewrite rules](https://vercel.com/docs/project-configuration#rewrites)
`edge` | A [Vercel Function](https://vercel.com/docs/functions) using [Edge runtime](https://vercel.com/docs/functions/runtimes/edge)
`prerender` | A pre-rendered page built using [Incremental Static Regeneration](https://vercel.com/docs/incremental-static-regeneration)
`streaming_func` | A [streaming Vercel Function](https://vercel.com/docs/functions/streaming-functions)
`background_func` | The [Incremental Static Regeneration Render Function](https://vercel.com/docs/incremental-static-regeneration) used to create or update a static page
