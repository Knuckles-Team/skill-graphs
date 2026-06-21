##  [Trusted IPs security considerations](https://vercel.com/docs/sign-in-with-vercel#trusted-ips-security-considerations)[](https://vercel.com/docs/sign-in-with-vercel#trusted-ips-security-considerations)
The table below outlines key considerations and security implications when using Trusted IPs for your deployments on Vercel.
Consideration | Description
---|---
General Considerations |
Environment Configuration | Can be enabled for different environments. See [Understanding Deployment Protection by environment](https://vercel.com/docs/security/deployment-protection#understanding-deployment-protection-by-environment)
Compatibility | Operates as a required layer on top of [Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) and [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection).
Bypass Methods | Can be bypassed using [Shareable Links](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) and [Protection Bypass for Automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation)
IP Address Support | Supports IPv4 addresses and IPv4 CIDR ranges
Prerequisites |
Preview Environment Requirements | Can only be enabled in preview when [Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) is also enabled.
External Proxy Configuration | Requires [rulesets](https://vercel.com/kb/guide/can-i-use-a-proxy-on-top-of-my-vercel-deployment) configuration to avoid blocking proxy IPs. [Contact our sales team for more information](https://vercel.com/contact/sales)
Security Considerations |
Firewall Precedence |  [Vercel Firewall](https://vercel.com/docs/vercel-firewall) takes precedence over Trusted IPs
IP Blocking | IPs or CIDRs listed in [IP Blocking](https://vercel.com/docs/security/vercel-waf/ip-blocking) will be blocked even if listed in Trusted IPs
DDoS Mitigation | Trusted IPs do not bypass [DDoS Mitigation](https://vercel.com/docs/security/ddos-mitigation) unless configured
Deployment Impact | Changing the Trusted IPs list affects all deployments
Disabling Trusted IPs | Disabling makes all existing deployments accessible from any IP
