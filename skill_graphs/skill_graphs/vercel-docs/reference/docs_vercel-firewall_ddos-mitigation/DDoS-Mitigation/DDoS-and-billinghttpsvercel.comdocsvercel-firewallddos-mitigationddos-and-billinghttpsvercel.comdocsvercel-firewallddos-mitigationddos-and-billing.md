##  [DDoS and billing](https://vercel.com/docs/vercel-firewall/ddos-mitigation#ddos-and-billing)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#ddos-and-billing)
[Vercel automatically mitigates against L3, L4, and L7 DDoS attacks](https://vercel.com/docs/security/ddos-mitigation) at the platform level for all plans. Vercel does not charge customers for traffic that gets blocked by the Firewall.
Usage will be incurred for requests that are successfully served prior to us automatically mitigating the event. Usage will also be incurred for requests that are not recognized as a DDoS event, which may include bot and crawler traffic.
For an additional layer of security, we recommend that you enable [Attack Challenge Mode](https://vercel.com/docs/attack-challenge-mode) when you are under attack, which is available for free on all plans. While some malicious traffic is automatically challenged, enabling Attack Challenge Mode will challenge all traffic, including legitimate traffic to ensure that only real users can access your site.
You can monitor usage in the [Vercel Dashboard](https://vercel.com/dashboard) under the Usage section in the sidebar, although you will [receive notifications](https://vercel.com/docs/notifications#on-demand-usage-notifications) when nearing your usage limits.
* * *
[ Previous Firewall Concepts ](https://vercel.com/docs/vercel-firewall/firewall-concepts)[ Next Attack Challenge Mode ](https://vercel.com/docs/vercel-firewall/attack-challenge-mode)
Was this helpful?
Send
On this page
  * [Responding to DDoS attacks](https://vercel.com/docs/vercel-firewall/ddos-mitigation#responding-to-ddos-attacks)
  * [Bypass System-level Mitigations](https://vercel.com/docs/vercel-firewall/ddos-mitigation#bypass-system-level-mitigations)
  * [System Bypass Rules](https://vercel.com/docs/vercel-firewall/ddos-mitigation#system-bypass-rules)
  * [Dedicated DDoS support for Enterprise teams](https://vercel.com/docs/vercel-firewall/ddos-mitigation#dedicated-ddos-support-for-enterprise-teams)
  * [DDoS and billing](https://vercel.com/docs/vercel-firewall/ddos-mitigation#ddos-and-billing)


Copy as MarkdownGive feedbackAsk AI about this page
