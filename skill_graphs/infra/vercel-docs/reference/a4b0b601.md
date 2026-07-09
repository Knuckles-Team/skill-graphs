# DDoS Mitigation
Last updated January 5, 2026
DDoS Mitigation is available on [all plans](https://vercel.com/docs/plans)
Vercel provides automatic DDoS mitigation for all deployments, regardless of your plan. We block incoming traffic if we identify abnormal or suspicious levels of incoming requests.
Vercel does not charge customers for traffic that gets blocked with DDoS mitigation.
It works by:
  * Monitoring traffic: Vercel Firewall continuously analyzes incoming traffic to detect signs of DDoS attacks. This helps to identify and mitigate threats in real-time
  * Blocking traffic: Vercel Firewall filters out malicious traffic while allowing legitimate requests to pass through
  * Scaling resources: During a DDoS attack, Vercel Firewall dynamically scales resources to absorb the increased traffic, preventing your applications or sites from being overwhelmed


If you need further control over incoming traffic, you can temporarily enable [Attack Challenge Mode](https://vercel.com/docs/attack-challenge-mode) to challenge all traffic to your site, ensuring only legitimate users can access it.
Learn more about [DoS, DDoS and the Open System Interconnection model](https://vercel.com/docs/security/firewall-concepts#understanding-ddos).
