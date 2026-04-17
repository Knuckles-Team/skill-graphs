##  [Bot protection managed ruleset](https://vercel.com/docs/bot-management#bot-protection-managed-ruleset)[](https://vercel.com/docs/bot-management#bot-protection-managed-ruleset)
Bot protection managed ruleset is available on [all plans](https://vercel.com/docs/plans)
With Vercel, you can use the bot protection managed ruleset to [challenge](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge) non-browser traffic from accessing your applications. It filters out automated threats while allowing legitimate traffic.
  * It identifies clients that violate browser-like behavior and serves a javascript challenge to them.
  * It prevents requests that falsely claim to be from a browser such as a `curl` request identifying as Chrome.
  * It automatically excludes [verified bots](https://vercel.com/docs/bot-management#verified-bots), such as Google's crawler, from evaluation.


To learn more about how the ruleset works, review the [Challenge](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge) section of [Firewall actions](https://vercel.com/docs/vercel-firewall/firewall-concepts#firewall-actions). To understand the details of what get logged and how to monitor your traffic, review [Firewall Observability](https://vercel.com/docs/vercel-firewall/firewall-observability).
For trusted automated traffic, you can create [custom WAF rules](https://vercel.com/docs/vercel-waf/custom-rules) with [bypass actions](https://vercel.com/docs/vercel-firewall/firewall-concepts#bypass) that will allow this traffic to skip the bot protection ruleset.
###  [Enable the ruleset](https://vercel.com/docs/bot-management#enable-the-ruleset)[](https://vercel.com/docs/bot-management#enable-the-ruleset)
You can apply the ruleset to your project in [log](https://vercel.com/docs/vercel-firewall/firewall-concepts#log) or [challenge](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge) mode. Learn how to [configure the bot protection managed ruleset](https://vercel.com/docs/vercel-waf/managed-rulesets#configure-bot-protection-managed-ruleset).
###  [Bot protection ruleset with reverse proxies](https://vercel.com/docs/bot-management#bot-protection-ruleset-with-reverse-proxies)[](https://vercel.com/docs/bot-management#bot-protection-ruleset-with-reverse-proxies)
Bot Protection doesn't work when a reverse proxy (e.g. Cloudflare, Azure, or other CDNs) is placed in front of your Vercel deployment. This setup significantly degrades detection accuracy and performance, leading to a suboptimal end-user experience.
[Reverse proxies](https://vercel.com/docs/security/reverse-proxy) interfere with Vercel's ability to reliably identify bots:
  * Obscured detection signals: Legitimate users may be incorrectly challenged because the proxy masks signals that Bot Protection relies on.
  * Frequent re-challenges: Some proxies rotate their exit node IPs frequently, forcing Vercel to re-initiate the challenge on every IP change.
