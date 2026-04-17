##  [Limits](https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting#limits)[](https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting#limits)
Resource | Hobby | Pro | Enterprise
---|---|---|---
Included counting keys | IP, JA4 Digest | IP, JA4 Digest | IP, JA4 Digest, User Agent and arbitrary Header keys
Counting algorithm | Fixed window | Fixed window | Fixed window, Token bucket
Counting window | Minimum: 10s, Maximum: 10mins | Minimum: 10s, Maximum: 10mins | Minimum: 10s, Maximum: 1hr
Number of rules | 1 per project | 40 per project | 1000 per project
Included requests | 1,000,000 Allowed requests | 1,000,000 Allowed requests |
