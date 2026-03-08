##  [Firewall actions](https://vercel.com/docs/vercel-firewall/firewall-concepts#firewall-actions)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#firewall-actions)
The Vercel Firewall allows several possible actions to be taken when traffic matches a rule. These actions, that can be taken by custom rules or system DDoS mitigations, apply when detecting malicious traffic. You can view the actions and their results in the [Firewall and Monitoring](https://vercel.com/docs/vercel-firewall#observability) tabs.
###  [Log](https://vercel.com/docs/vercel-firewall/firewall-concepts#log)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#log)
The log action allows you to monitor and record specific traffic patterns without affecting the request. When a request matches a rule with the log action:
  * The request is allowed to proceed normally.
  * Details about the request are logged and displayed in the Firewall and Monitoring tabs, and sent to log drains for analysis.
  * There is no impact on the visitor's experience.


This is useful for monitoring suspicious patterns or gathering data about specific types of traffic before implementing stricter actions.
###  [Deny](https://vercel.com/docs/vercel-firewall/firewall-concepts#deny)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#deny)
The deny action blocks requests immediately when they match a rule. When a request is denied:
  * A `403 Forbidden` response is returned.
  * The request does not reach your application.
  * Usage is incurred only for the edge request and ingress [Fast Data Transfer](https://vercel.com/docs/manage-cdn-usage#fast-data-transfer) which are required to process the custom rule.


This is the most restrictive action and you should use it for known malicious traffic patterns or IP addresses.
###  [Challenge](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge)
A security challenge verifies that incoming traffic originates from a real web browser with JavaScript capabilities. Only human visitors using a web browser can pass the challenge and access protected resources, while non-browser clients (bots, scripts, etc.) cannot.
Use the challenge action when you want to block automated traffic while allowing legitimate users to access your content. It offers a middle ground between the log and deny actions, protecting against bots while maintaining accessibility for real visitors through a simple one-time verification.
When the challenge action is applied:
  1. ###  [Initial challenge](https://vercel.com/docs/vercel-firewall/firewall-concepts#initial-challenge)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#initial-challenge)
During this process, visitors see a Vercel Security Checkpoint screen:
![Vercel challenge page](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fchallenge-light.png&w=1920&q=75)![Vercel challenge page](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fchallenge-dark.png&w=1920&q=75)Vercel challenge page
     * The browser must execute JavaScript code to prove it's a real browser.
     * The code computes and submits a challenge solution.
     * The system validates browser characteristics to prevent automated tools from passing.
     * If the challenge succeeds, the [WAF](https://vercel.com/docs/vercel-firewall/vercel-waf) validates the request as a legitimate browser client and continues processing the request, which includes evaluating any additional WAF rules.
     * If the challenge fails, the request is blocked before reaching your application.
The checkpoint page localizes to a language based on the visitor's browser settings and respects their preferred color scheme, ensuring a seamless experience for legitimate users.
  2. ###  [Challenge session](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge-session)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge-session)
     * Upon successful verification, a challenge session is created in the browser.
     * Sessions are valid for 1 hour.
     * All subsequent requests within the session are allowed.
     * Challenge sessions are tied to the browser that completed the challenge, ensuring secure session management.
     * After session expiration, the client must re-solve the challenge.


####  [Challenge subrequests and APIs](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge-subrequests-and-apis)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge-subrequests-and-apis)
If your application makes additional requests (e.g., API calls) during a valid session, they automatically succeed. This is particularly useful for server-side rendered applications where the server makes additional requests to APIs in the same application.
####  [Challenge limitations](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge-limitations)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#challenge-limitations)
  * API routes that are protected by a challenge rule can only be accessed within a valid challenge session.
  * Direct API calls (e.g., from scripts, cURL, or Postman) will fail if they require challenge validation.
  * Direct API calls from outside a valid challenge session will not succeed.
  * If a user hasn't completed a challenge session through your website first, they cannot access challenged API routes.
  * Automated tools and scripts cannot establish challenge sessions. For legitimate automation needs, use [Bypass](https://vercel.com/docs/vercel-firewall/firewall-concepts#bypass) to allow specific trusted sources.


###  [Bypass](https://vercel.com/docs/vercel-firewall/firewall-concepts#bypass)[](https://vercel.com/docs/vercel-firewall/firewall-concepts#bypass)
The bypass action allows specific traffic to skip any subsequent firewall rules. When a request matches a bypass rule:
  * For custom rule bypasses, the request is allowed through any custom or managed rules.
  * For system bypasses, the request is allowed through any system-level mitigations.
  * The request proceeds directly to your application.


This is useful for trusted traffic sources, internal tools, or critical services that should never be blocked.
