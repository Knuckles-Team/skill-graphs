##  [crons](https://vercel.com/docs/project-configuration/vercel-json#crons)[](https://vercel.com/docs/project-configuration/vercel-json#crons)
Used to configure [cron jobs](https://vercel.com/docs/cron-jobs) for the production deployment of a project.
Type: `Array` of cron `Object`.
Limits:
  * A maximum of string length of 512 for the `path` value.
  * A maximum of string length of 256 for the `schedule` value.


###  [Cron object definition](https://vercel.com/docs/project-configuration/vercel-json#cron-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#cron-object-definition)
  * `path` - Required - The path to invoke when the cron job is triggered. Must start with `/`.
  * `schedule` - Required - The [cron schedule expression](https://vercel.com/docs/cron-jobs#cron-expressions) to use for the cron job.


vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "crons": [
    {
      "path": "/api/every-minute",
      "schedule": "* * * * *"
    },
    {
      "path": "/api/every-hour",
      "schedule": "0 * * * *"
    },
    {
      "path": "/api/every-day",
      "schedule": "0 0 * * *"
    }
  ]
}
```
