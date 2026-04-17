[Deployment Protection](https://vercel.com/docs/deployment-protection)
[Bypass Deployment Protection](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection)
OPTIONS Allowlist
[Deployment Protection](https://vercel.com/docs/deployment-protection)
[Bypass Deployment Protection](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection)
OPTIONS Allowlist
# OPTIONS Allowlist
Last updated September 15, 2025
OPTIONS Allowlist is available on [all plans](https://vercel.com/docs/plans)
You can use OPTIONS Allowlist to disable Deployment Protection (including [Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication), [Password Protection](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/password-protection), and [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)) on any incoming CORS preflight `OPTIONS` request for a list of paths.
When you add a path to OPTIONS Allowlist, any incoming request with the method `OPTIONS` that starts with the path will no longer be covered by Deployment Protection. When you remove a path from OPTIONS Allowlist, the path becomes protected again with the project's Deployment Protection settings.
For example, if you specify `/api`, all requests to paths that start with `/api` (such as `/api/v1/users` and `/api/v2/projects`) will be unprotected for any `OPTIONS` request.
![OPTIONS Allowlist.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-light.png&w=3840&q=75)![OPTIONS Allowlist.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-dark.png&w=3840&q=75)OPTIONS Allowlist.
##  [Enabling OPTIONS Allowlist](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#enabling-options-allowlist)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#enabling-options-allowlist)
  1. ###  [Go to Project Deployment Protection Settings](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#go-to-project-deployment-protection-settings)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#go-to-project-deployment-protection-settings)
From your Vercel [dashboard](https://vercel.com/dashboard):
    1. Select the project that you wish to enable Password Protection for
    2. Go to [Deployment Protection](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdeployment-protection&title=Go+to+Deployment+Protection+settings) in the sidebar
  2. ###  [Enable OPTIONS Allowlist](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#enable-options-allowlist)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#enable-options-allowlist)
From the OPTIONS Allowlist section, enable the toggle labelled Disabled:
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-disabled-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-disabled-dark.png&w=3840&q=75)
  3. ###  [Specify a path](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#specify-a-path)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#specify-a-path)
Specify a path to add to the OPTIONS Allowlist:
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-add-path-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-add-path-dark.png&w=3840&q=75)
  4. ###  [Add more paths](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#add-more-paths)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#add-more-paths)
To add more paths, select Add path:
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-add-another-path-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-add-another-path-dark.png&w=3840&q=75)
  5. ###  [Save changes](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#save-changes)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#save-changes)
Once all the paths are added, select Save


##  [Disabling OPTIONS Allowlist](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#disabling-options-allowlist)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#disabling-options-allowlist)
  1. ###  [Go to Project Deployment Protection Settings](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#go-to-project-deployment-protection-settings)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#go-to-project-deployment-protection-settings)
From your Vercel [dashboard](https://vercel.com/dashboard):
    1. Select the project that you wish to enable Password Protection for
    2. Go to [Deployment Protection](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdeployment-protection&title=Go+to+Deployment+Protection+settings) in the sidebar
  2. ###  [Disable OPTIONS Allowlist](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#disable-options-allowlist)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#disable-options-allowlist)
From the OPTIONS Allowlist section, select the toggle labelled Enabled:
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-light.png&w=3840&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-dark.png&w=3840&q=75)
  3. ###  [Save changes](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#save-changes)[](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist#save-changes)
Once all the paths are added, select Save


* * *
[ Previous Exceptions ](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/deployment-protection-exceptions)[ Next Protection Bypass for Automation ](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation)
Was this helpful?
Send
