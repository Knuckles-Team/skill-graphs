##  [Limitations](https://vercel.com/docs/observability/observability-plus#limitations)[](https://vercel.com/docs/observability/observability-plus#limitations)
Feature | Observability | Observability Plus
---|---|---
Data Retention | Hobby: 12 hours
Pro: 1 day
Enterprise: 3 days | 30 days
Monitoring access | Not Included | Included for existing Monitoring users.
See [Existing monitoring users](https://vercel.com/docs/observability#existing-monitoring-users) for more information
Vercel Functions | No Latency (p75) data, no breakdown by path | Latency data, sort by p75, breakdown by path and routes
External APIs | No ability to sort by error rate or p75 duration, only request totals for each hostname | Sorting and filtering by requests, p75 duration, and duration. Latency, Requests, API Endpoint and function calls for each hostname
Edge Requests | No breakdown by path | Full request data
Fast Data Transfer | No breakdown by path | Full request data
ISR (Incremental Static Regeneration) | No access to average duration or revalidation data. Limited function data for each route | Access to sorting and filtering by duration and revalidation. Full function data for each route
Build Diagnostics | Full access | Full access
In-function Concurrency | Full access when enabled | Full access when enabled
Runtime logs | Hobby: 1 hour
Pro: 1 day
Enterprise: 3 days | 30 days, max selection window of 14 consecutive days
To access Observability Plus features, you can start a Pro trial using the button below.
### Experience Vercel Pro for free
Unlock the full potential of Vercel Pro during your 14-day trial with $20 in credits. Benefit from 1 TB Fast Data Transfer, 10,000,000 Edge Requests, up to 200 hours of Build Execution, and access to Pro features like team collaboration and enhanced analytics.
[Start your free Pro trial](https://vercel.com/signup?next=/upgrade/docs-trial-button&plan=pro)
