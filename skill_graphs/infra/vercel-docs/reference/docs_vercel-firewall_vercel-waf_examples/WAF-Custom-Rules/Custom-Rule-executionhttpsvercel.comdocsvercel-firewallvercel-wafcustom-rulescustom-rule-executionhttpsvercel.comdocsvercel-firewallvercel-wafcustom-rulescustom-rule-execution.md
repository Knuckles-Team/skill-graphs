##  [Custom Rule execution](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-execution)[](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-execution)
When a rule denies or challenges the traffic to your site and the client has not previously solved the challenge (in the case of challenge mode), the rule execution stops and blocks or challenges the request.
After a Log rule runs, the rule execution continues. If no other rule matches and acts on the request, the Log rule that is last matched is reported.
When you apply a [rate limiting](https://vercel.com/docs/security/vercel-waf/rate-limiting) rule, you need to include a follow up action that will log, deny, challenge, or return a 429 response.
