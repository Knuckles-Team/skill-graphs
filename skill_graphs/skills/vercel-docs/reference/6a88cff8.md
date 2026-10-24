# Trusted IPs
Last updated November 25, 2025
Trusted IPs are available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Those with the [owner](https://vercel.com/docs/rbac/access-roles#owner-role), [member](https://vercel.com/docs/rbac/access-roles#member-role) and [admin](https://vercel.com/docs/rbac/access-roles#admin-role) roles can manage Trusted IPs
With Trusted IPs [enabled](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips#managing-trusted-ips) at the level of your [project](https://vercel.com/docs/project-configuration/project-settings), only visitors from an allowed IP address can access your deployment. The deployment URL will return `404` [No Deployment Found](https://vercel.com/docs/errors/platform-error-codes#404:-deployment_not_found) for all other requests. Trusted IPs is configured by specifying a list of IPv4 addresses and IPv4 CIDR ranges.
Trusted IPs is suitable for customers who access Vercel deployments through a specific IP address. For example, limiting preview deployment access to your VPN. Trusted IPs can also be enabled in production, for example, to restrict incoming access to only requests through your external proxy.
Want to talk to our team?
This feature is available on the Enterprise plan.
Schedule Call
![Enabling Trusted IPs.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Ftrusted-ips-dash-light.png&w=1920&q=75)![Enabling Trusted IPs.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Ftrusted-ips-dash-dark.png&w=1920&q=75)Enabling Trusted IPs.
