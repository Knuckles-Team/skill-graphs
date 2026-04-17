##  [Password Protection security considerations](https://vercel.com/docs/accounts#password-protection-security-considerations)[](https://vercel.com/docs/accounts#password-protection-security-considerations)
The table below outlines key considerations and security implications when using Password Protection for your deployments on Vercel.
Consideration | Description
---|---
Environment Configuration | Can be enabled for different environments. See [Understanding Deployment Protection by environment](https://vercel.com/docs/security/deployment-protection#understanding-deployment-protection-by-environment)
Compatibility | Compatible with [Vercel Authentication](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) and [Trusted IPs](https://vercel.com/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)
Bypass Methods | Can be bypassed using [Shareable Links](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) and [Protection bypass for Automation](https://vercel.com/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation)
Password Persistence | Users only need to enter the password once per deployment, or when the password changes, due to cookie set by the feature being invalidated on password change
Password Changes | Users must re-enter a new password if you change the existing one
Disabling Protection | All existing deployments become unprotected if you disable the feature
Token Scope | JWT tokens set as cookies are valid only for the URL they were set for and can't be reused for different URLs, even if those URLs point to the same deployment
