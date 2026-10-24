##  [Deployment Protection and microfrontends](https://vercel.com/docs/microfrontends/managing-microfrontends/security#deployment-protection-and-microfrontends)[](https://vercel.com/docs/microfrontends/managing-microfrontends/security#deployment-protection-and-microfrontends)
Because each URL is protected by the [Deployment Protection](https://vercel.com/docs/security/deployment-protection) settings of the project it belongs to, the deployment protection for the microfrontend experience as a whole is determined by the default application.
For requests to a microfrontend host (a domain belonging to the microfrontend default application):
  * Requests are only verified by the [Deployment Protection](https://vercel.com/docs/security/deployment-protection) settings for the project of your default application


For requests directly to a child application (a domain belonging to a child microfrontend):
  * Requests are only verified by the [Deployment Protection](https://vercel.com/docs/security/deployment-protection) settings for the project of the child application


This applies to all [protection methods](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments) and [bypass methods](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection), including:
  * [Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication)
  * [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection)
  * [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)
  * [Shareable Links](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links)
  * [Protection Bypass for Automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation)
  * [Deployment Protection Exceptions](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/deployment-protection-exceptions)
  * [OPTIONS Allowlist](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist).


###  [Managing Deployment Protection for your microfrontend](https://vercel.com/docs/microfrontends/managing-microfrontends/security#managing-deployment-protection-for-your-microfrontend)[](https://vercel.com/docs/microfrontends/managing-microfrontends/security#managing-deployment-protection-for-your-microfrontend)
Use the [Deployment Protection](https://vercel.com/docs/security/deployment-protection) settings for the project of the default application to control access to the microfrontend.
We recommend the following configuration:
  * Default app: Use [Standard Protection](https://vercel.com/docs/security/deployment-protection) so that end users can access the microfrontend through the default app's URL.
  * Child apps: Enable [protection for all deployments](https://vercel.com/docs/security/deployment-protection) so that child apps are not directly accessible. Since child app content is served through the default app's URL, child apps can only be accessed via the URL of the default project.


This works because Vercel handles routing to child apps within a single request at the network layer — as explained in [Path Routing](https://vercel.com/docs/microfrontends/path-routing) — it is not a rewrite that would result in a separate request to the child app's URL. Deployment protection on the child app therefore applies only when the child app's URL is accessed directly.
