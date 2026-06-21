##  [Internal requests](https://vercel.com/docs/vercel-firewall/attack-challenge-mode#internal-requests)[](https://vercel.com/docs/vercel-firewall/attack-challenge-mode#internal-requests)
When Attack Challenge Mode is enabled, requests from your own [Functions](https://vercel.com/docs/functions) and [Cron Jobs](https://vercel.com/docs/cron-jobs) are automatically allowed through without being challenged. This means your application's internal operations will continue to work normally.
For example, if you have multiple projects in your Vercel account:
  * Your projects can communicate with each other without being challenged
  * Only requests from outside your account will be challenged
  * Each Vercel account has its own secure boundary


Other Vercel accounts cannot bypass Attack Challenge Mode on your projects. The security is strictly enforced per account, ensuring that only your own projects can communicate without challenges.
