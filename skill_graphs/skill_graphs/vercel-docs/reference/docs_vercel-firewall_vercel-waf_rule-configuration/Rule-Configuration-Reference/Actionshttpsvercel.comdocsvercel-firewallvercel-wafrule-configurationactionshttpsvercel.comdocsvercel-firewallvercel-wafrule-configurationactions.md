##  [Actions](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#actions)[](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#actions)
Name | Description | Note
---|---|---
Log | Tracks the matching of this rule without blocking traffic. Requests matching this rule are visible in the Firewall overview page. |
  * If another rule blocks the traffic **before** a log rule executes, the request is not considered a match for that log rule
  * If another rule blocks the traffic **after** a log rule executes, the request is tagged to the rule that blocked the traffic and does not appear in the log rule


Challenge | Conditionally blocks traffic with [browser challenge](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge). |
  * If the client fails to solve the challenge, the rule continues to block the traffic
  * Once the client solves the challenge, the rule is bypassed and remaining rules (if any) are evaluated. The request is allowed if none of the remaining rules block


Deny | Blocks the request and no further rules are evaluated. |
Bypass | If matched, it bypasses any remaining custom rules. | WAF bypass rules **do not** bypass system-level mitigations such as [DDoS Mitigation](https://vercel.com/docs/security/ddos-mitigation). To do so, you can use the [Bypass System-level Mitigations](https://vercel.com/docs/security/ddos-mitigation#bypass-system-level-mitigations) feature.
Redirect | If matched, it redirects the client to the target path set in the `to` field. |
  * Redirects the request and no further rules are evaluated
  * The target path in the `to`field can be absolute or relative to the project deployment's root
  * It's a temporary redirect (307)


* * *
[ Previous Rate Limiting ](https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting)[ Next System Bypass Rules ](https://vercel.com/docs/vercel-firewall/vercel-waf/system-bypass-rules)
Was this helpful?
Send
On this page
  * [Parameters](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#parameters)
  * [Operators](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#operators)
  * [Actions](https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration#actions)


Copy as MarkdownGive feedbackAsk AI about this page
