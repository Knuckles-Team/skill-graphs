##  [Responding to DDoS attacks](https://vercel.com/docs/vercel-firewall/ddos-mitigation#responding-to-ddos-attacks)[](https://vercel.com/docs/vercel-firewall/ddos-mitigation#responding-to-ddos-attacks)
Vercel mitigates against L3, L4, and L7 DDoS attacks regardless of the plan you are on. The Vercel Firewall uses hundreds of signals and detection factors to fingerprint request patterns, determining if they appear to be an attack, and challenging or blocking requests if they appear illegitimate.
However, there are other steps you can take to protect your site during DDoS attacks:
  * Enable [Attack Challenge Mode](https://vercel.com/docs/attack-challenge-mode) to challenge all visitors to your site. This is a temporary measure and provides another layer of security to ensure all traffic to your site is legitimate
  * You can set up [IP Blocking](https://vercel.com/docs/security/vercel-waf/ip-blocking) to block specific IP addresses from accessing your projects. Enterprise teams can also receive dedicated DDoS support
  * You can add [Custom Rules](https://vercel.com/docs/security/vercel-waf/custom-rules) to deny or challenge specific traffic to your site based on the conditions of the rules
  * You can also use Middleware to [rate limiting](https://vercel.com/kb/guide/add-rate-limiting-vercel).


Pro teams can [set up Spend Management](https://vercel.com/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](https://vercel.com/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.
