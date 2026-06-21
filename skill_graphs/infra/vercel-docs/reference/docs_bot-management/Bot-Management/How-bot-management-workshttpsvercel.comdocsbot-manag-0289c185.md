##  [How bot management works](https://vercel.com/docs/bot-management#how-bot-management-works)[](https://vercel.com/docs/bot-management#how-bot-management-works)
Bot management systems analyze incoming traffic to identify and classify requests based on their source and intent. This includes:
  * Verifying and allowing legitimate bots that correctly identify themselves
  * Monitoring bot traffic patterns and resource consumption
  * Detecting and challenging suspicious traffic that behaves abnormally
  * Enforcing browser-like behavior by verifying navigation patterns and cache usage


###  [Methods of bot management and protection](https://vercel.com/docs/bot-management#methods-of-bot-management-and-protection)[](https://vercel.com/docs/bot-management#methods-of-bot-management-and-protection)
To effectively manage bot traffic and protect against harmful bots, you can use various techniques, including:
  * Signature-based detection: Inspecting HTTP requests for known bot signatures
  * Rate limiting: Restricting how often certain actions can be performed to prevent abuse
  * Challenges: [Using JavaScript checks to verify human presence](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge)
  * Behavioral analysis: Detecting unusual patterns in user activity that suggest automation


With Vercel, you can use:
  * [Managed rulesets](https://vercel.com/docs/vercel-waf/managed-rulesets#configure-bot-protection-managed-ruleset) to challenge specific bot traffic
  * Rate limiting and challenge actions with [WAF custom rules](https://vercel.com/docs/vercel-waf/custom-rules) to prevent bot activity from reaching your application
  * [DDoS protection](https://vercel.com/docs/security/ddos-mitigation) to defend your application against bot driven attacks
  * [Observability](https://vercel.com/docs/observability) and [Firewall](https://vercel.com/docs/vercel-firewall/firewall-observability) to monitor bot patterns, traffic sources, and the effectiveness of your bot management strategies
