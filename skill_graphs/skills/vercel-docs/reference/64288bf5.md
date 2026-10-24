##  [Vercel Firewall and microfrontends](https://vercel.com/docs/microfrontends/managing-microfrontends/security#vercel-firewall-and-microfrontends)[](https://vercel.com/docs/microfrontends/managing-microfrontends/security#vercel-firewall-and-microfrontends)
  * The [Platform-wide firewall](https://vercel.com/docs/vercel-firewall#platform-wide-firewall) is applied to all requests.
  * The customizable [Web Application Firewall (WAF)](https://vercel.com/docs/vercel-firewall/vercel-waf) from the default application and the corresponding child application is applied for a request.


###  [Vercel WAF and microfrontends](https://vercel.com/docs/microfrontends/managing-microfrontends/security#vercel-waf-and-microfrontends)[](https://vercel.com/docs/microfrontends/managing-microfrontends/security#vercel-waf-and-microfrontends)
For requests to a microfrontend host (a domain belonging to the microfrontend default application):
  * All requests are verified by the [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf) for the project of your default application
  * Requests to child applications are additionally verified by the [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf) for their project


For requests directly to a child application (a domain belonging to a child microfrontend):
  * Requests are only verified by the [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf) for the project of the child application.


This applies for the entire [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf), including [Custom Rules](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules), [IP Blocking](https://vercel.com/docs/vercel-firewall/vercel-waf/ip-blocking), [WAF Managed Rulesets](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets), and [Attack Challenge Mode](https://vercel.com/docs/vercel-firewall/attack-challenge-mode).
###  [Managing the Vercel WAF for your microfrontend](https://vercel.com/docs/microfrontends/managing-microfrontends/security#managing-the-vercel-waf-for-your-microfrontend)[](https://vercel.com/docs/microfrontends/managing-microfrontends/security#managing-the-vercel-waf-for-your-microfrontend)
  * To set a WAF rule that applies to all requests to a microfrontend, use the [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf) for your default application.
  * To set a WAF rule that applies only to requests to paths of a child application, use the [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf) for the child project.


* * *
[ Previous Managing Microfrontends ](https://vercel.com/docs/microfrontends/managing-microfrontends)[ Next Using Vercel Toolbar ](https://vercel.com/docs/microfrontends/managing-microfrontends/vercel-toolbar)
Was this helpful?
Send
On this page
  * [Deployment Protection and microfrontends](https://vercel.com/docs/microfrontends/managing-microfrontends/security#deployment-protection-and-microfrontends)
  * [Managing Deployment Protection for your microfrontend](https://vercel.com/docs/microfrontends/managing-microfrontends/security#managing-deployment-protection-for-your-microfrontend)
  * [Vercel Firewall and microfrontends](https://vercel.com/docs/microfrontends/managing-microfrontends/security#vercel-firewall-and-microfrontends)
  * [Vercel WAF and microfrontends](https://vercel.com/docs/microfrontends/managing-microfrontends/security#vercel-waf-and-microfrontends)
  * [Managing the Vercel WAF for your microfrontend](https://vercel.com/docs/microfrontends/managing-microfrontends/security#managing-the-vercel-waf-for-your-microfrontend)


Copy as MarkdownGive feedbackAsk AI about this page
