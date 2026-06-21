##  [crons](https://vercel.com/docs/project-configuration/vercel-ts#crons)[](https://vercel.com/docs/project-configuration/vercel-ts#crons)
Used to configure [cron jobs](https://vercel.com/docs/cron-jobs) for the production deployment of a project.
Type: `Array` of cron `Object`.
Limits:
  * A maximum of string length of 512 for the `path` value.
  * A maximum of string length of 256 for the `schedule` value.


###  [Cron object definition](https://vercel.com/docs/project-configuration/vercel-ts#cron-object-definition)[](https://vercel.com/docs/project-configuration/vercel-ts#cron-object-definition)
  * `path` - Required - The path to invoke when the cron job is triggered. Must start with `/`.
  * `schedule` - Required - The [cron schedule expression](https://vercel.com/docs/cron-jobs#cron-expressions) to use for the cron job.


vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  crons: [
    {
      path: '/api/every-minute',
      schedule: '* * * * *',
    },
    {
      path: '/api/every-hour',
      schedule: '0 * * * *',
    },
    {
      path: '/api/every-day',
      schedule: '0 0 * * *',
    },
  ],
};
```
