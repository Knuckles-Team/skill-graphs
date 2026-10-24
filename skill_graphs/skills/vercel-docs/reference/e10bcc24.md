##  [Using a reverse proxy server](https://vercel.com/docs/security/reverse-proxy#using-a-reverse-proxy-server)[](https://vercel.com/docs/security/reverse-proxy#using-a-reverse-proxy-server)
However, you may still need to use a reverse proxy server. For example, your organization has legacy web applications protected by a reverse proxy and mandates that your Vercel project also uses this reverse proxy.
In such a case, you want to ensure that Vercel's [platform-wide firewall](https://vercel.com/docs/vercel-firewall#platform-wide-firewall) does not block this proxy server due to the reasons mentioned above.
###  [Prerequisites](https://vercel.com/docs/security/reverse-proxy#prerequisites)[](https://vercel.com/docs/security/reverse-proxy#prerequisites)
  * TLS setup: Disable HTTP→HTTPS redirection for `http://<DOMAIN>/.well-known/acme-challenge/*` on port 80
  * Cache control: Never cache `https://<DOMAIN>/.well-known/vercel/*` paths
  * Plan eligibility:
    * Hobby/Pro: Verified Proxy Lite only
    * Enterprise: Lite + Advanced (self-hosted/geolocation preservation)


###  [Automatic vs. Manual enablement](https://vercel.com/docs/security/reverse-proxy#automatic-vs.-manual-enablement)[](https://vercel.com/docs/security/reverse-proxy#automatic-vs.-manual-enablement)
Verified Proxy is automatically enabled for the providers listed below on all plans. Any other provider or a self-hosted proxy (for example, Nginx, HAProxy, etc) requires a manual onboarding process (Enterprise only).
###  [Supported providers (Verified Proxy Lite)](https://vercel.com/docs/security/reverse-proxy#supported-providers-verified-proxy-lite)[](https://vercel.com/docs/security/reverse-proxy#supported-providers-verified-proxy-lite)
Provider | Required Header | Configuration
---|---|---
Fastly | `Fastly-Client-IP` | A built-in header. No additional configuration required.
Google Cloud Load Balancing | `X-GCP-Connecting-IP` | Add a custom header: `X-GCP-Connecting-IP: {client_ip_address}` using their
Cloudflare | `CF-Connecting-IP` | A built-in header. No additional configuration required.
AWS CloudFront | `CloudFront-Viewer-Address` | Enable the header via the
Imperva CDN (Cloud WAF) | `Incap-Client-IP` | A built-in header. No additional configuration required.
Akamai | `True-Client-IP` | Enable the header via the property manager. Clients may be able to spoof the header; work with Akamai to harden the configuration. You must also enable the
Azure Front Door | `X-Azure-ClientIP` | A built-in header. No additional configuration required.
F5 | `X-F5-True-Client-IP` | Add a custom header: `X-F5-True-Client-IP: {client_ip_address}`
###  [Self-hosted reverse proxies (Verified Proxy Advanced)](https://vercel.com/docs/security/reverse-proxy#self-hosted-reverse-proxies-verified-proxy-advanced)[](https://vercel.com/docs/security/reverse-proxy#self-hosted-reverse-proxies-verified-proxy-advanced)
Verified Proxy Advanced is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Ensure that the following requirements are met if you are running self-hosted reverse proxies:
  * Your proxy must have static egress IP addresses assigned. We cannot support dynamic IP addresses.
  * Your proxy must send a custom request header that carries the real client IP (e.g. `x-${team-slug}-connecting-ip`).
  * Your proxy must enable SNI (Server Name Indication) on outbound TLS connections.
  * Use consistent and predictable Vercel project domains for onboarding. For example, use *.vercel.example.com and ensure your Proxy always sends traffic to those specific hostnames.


For detailed setup instructions, please contact your Customer Success Manager (CSM) or Account Executive (AE).
