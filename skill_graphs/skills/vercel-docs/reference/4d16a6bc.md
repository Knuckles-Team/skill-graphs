##  [Enabling attack challenge mode](https://vercel.com/docs/vercel-firewall/attack-challenge-mode#enabling-attack-challenge-mode)[](https://vercel.com/docs/vercel-firewall/attack-challenge-mode#enabling-attack-challenge-mode)
While Vercel's Firewall [automatically monitors for and mitigates attacks](https://vercel.com/docs/security/ddos-mitigation#what-to-do-in-case-of-a-ddos-attack), you can enable Attack Challenge Mode during targeted attacks for additional security.
To enable:
  1. Select your project from the [Dashboard](https://vercel.com/dashboard).
  2. Open [Firewall](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall&title=Go+to+Firewall) in the sidebar.
  3. Click Bot Management.
  4. Under Attack Challenge Mode, select Enable.


All traffic initiated by web browsers, including API traffic, is supported. For example, a Next.js frontend calling a Next.js API in the same project will work properly.
Standalone APIs, other backend frameworks, and non-recognized automated services may not be able to pass challenges and could be blocked. If you need more control over what traffic is challenged, consider using [Custom Rules with the Vercel WAF](https://vercel.com/docs/security/vercel-waf/custom-rules).
