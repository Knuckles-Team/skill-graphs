# WAF System Bypass Rules
Last updated January 30, 2026
WAF System Bypass Rules are available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
While Vercel's system-level mitigations (such as [DDoS protection](https://vercel.com/docs/security/ddos-mitigation)) safeguard your websites and applications, it can happen that they block traffic from legitimate sources like proxies or shared networks in situations where traffic from these sources was identified as malicious.
You can ensure that specific IP addresses or CIDR ranges are never blocked by the Vercel Firewall's system mitigations with System Bypass Rules.
If you need to allow requests blocked by your own [WAF Custom Rules](https://vercel.com/docs/vercel-waf/custom-rules), use another [custom rule with a bypass action](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets#bypassing-custom-rules).
