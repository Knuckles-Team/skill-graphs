##  [How cron jobs work](https://vercel.com/docs/cron-jobs#how-cron-jobs-work)[](https://vercel.com/docs/cron-jobs#how-cron-jobs-work)
To trigger a cron job, Vercel makes an HTTP GET request to your project's production deployment URL, using the `path` provided in your project's `vercel.json` file. An example endpoint Vercel would make a request to in order to trigger a cron job might be: `https://*.vercel.app/api/cron`.
Vercel Functions triggered by a cron job on Vercel will always contain `vercel-cron/1.0` as the user agent.
