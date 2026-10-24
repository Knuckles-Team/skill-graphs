##  [Bypass System-level Mitigations](https://vercel.com/docs/vercel-firewall/ddos-mitigation#bypass-system-level-mitigations)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#bypass-system-level-mitigations)
Bypass System-level Mitigations are available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
While Vercel's system-level mitigations (such as [DDoS protection](https://vercel.com/docs/security/ddos-mitigation)) safeguards your websites and applications, it can happen that they block traffic from trusted sources like proxies or shared networks in situations where traffic from these proxies or shared networks was identified as malicious. You can temporarily pause all automatic mitigations for a specific project. This can be useful on business-critical events such as Black Friday.
To temporarily pause all automatic mitigations for a specific project:
  1. Click the menu button with the ellipsis icon Firewall tab for your project.
  2. Select Pause System Mitigations.
  3. Review the warning in the Pause System Mitigations dialog and confirm that you would like to pause all automatic mitigations for that project for the next 24 hours.


To resume the automatic mitigations before the 24 hour period ends:
  1. Click the menu button with the ellipsis icon Firewall tab for your project.
  2. Select Resume System Mitigations.
  3. Select Resume from the Resume System Mitigations dialog.


You are responsible for all usage fees incurred when using this feature, including illegitimate traffic that may otherwise have been blocked.
###  [System Bypass Rules](https://vercel.com/docs/vercel-firewall/ddos-mitigation#system-bypass-rules)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#system-bypass-rules)
In situations where you need a more granular and permanent approach, you can use [System Bypass Rules](https://vercel.com/docs/security/vercel-waf/system-bypass-rules) to ensure that essential traffic is never blocked by DDoS protection.
This feature is available for Pro and Enterprise customers. Learn how to [set up a System Bypass rule](https://vercel.com/docs/security/vercel-waf/system-bypass-rules#get-started) for your project and [limits](https://vercel.com/docs/security/vercel-waf/system-bypass-rules#limits) that apply based on your plan.
