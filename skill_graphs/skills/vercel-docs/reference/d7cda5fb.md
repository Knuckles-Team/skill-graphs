##  [Cron expressions](https://vercel.com/docs/cron-jobs#cron-expressions)[](https://vercel.com/docs/cron-jobs#cron-expressions)
Vercel supports the following cron expressions format:
Field | Value Range | Example Expression | Description
---|---|---|---
Minute | 0 - 59 | `5 * * * *` | Triggers at 5 minutes past the hour
Hour | 0 - 23 | `* 5 * * *` | Triggers every minute, between 05:00 AM and 05:59 AM
Day of Month | 1 - 31 | `* * 5 * *` | Triggers every minute, on day 5 of the month
Month | 1 - 12 | `* * * 5 *` | Triggers every minute, only in May
Day of Week | 0 - 6 (Sun-Sat) | `* * * * 5` | Triggers every minute, only on Friday
###  [Validate cron expressions](https://vercel.com/docs/cron-jobs#validate-cron-expressions)[](https://vercel.com/docs/cron-jobs#validate-cron-expressions)
To validate your cron expressions, you can use the following tool to quickly verify the syntax and timing of your scheduled tasks to ensure they run as intended.
Cron job validator
Use the input below to validate a cron expression. A human readable version of the expression will be displayed when submitted.
Cron expression
Your cron job will run:
Submit
You can also use
###  [Cron expression limitations](https://vercel.com/docs/cron-jobs#cron-expression-limitations)[](https://vercel.com/docs/cron-jobs#cron-expression-limitations)
  * Cron jobs on Vercel do not support alternative expressions like `MON`, `SUN`, `JAN`, or `DEC`
  * You cannot configure both day of the month and day of the week at the same time. When one has a value, the other must be `*`
  * The timezone is always UTC
