##  [functionFailoverRegions](https://vercel.com/docs/project-configuration/vercel-ts#functionfailoverregions)[](https://vercel.com/docs/project-configuration/vercel-ts#functionfailoverregions)
Setting failover regions for Vercel functions are available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Set this property to specify the [region](https://vercel.com/docs/functions/regions) to which a Vercel Function should fallback when the default region(s) are unavailable.
Type: `Array` of region identifier `String`.
Valid values: List of [regions](https://vercel.com/docs/regions).
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  functionFailoverRegions: ['iad1', 'sfo1'],
};
```

You can also set `functionFailoverRegions` on individual functions using the [`functions`](https://vercel.com/docs/project-configuration#functions) property to override the project-level default. See [per-function region configuration](https://vercel.com/docs/functions/configuring-functions/region#per-function-configuration) for more details.
These regions serve as a fallback to any regions specified in the [`regions` configuration](https://vercel.com/docs/project-configuration#regions). The region Vercel selects to invoke your function depends on availability and ingress. For instance:
  * Vercel always attempts to invoke the function in the primary region. If you specify more than one primary region in the `regions` property, Vercel selects the region geographically closest to the request
  * If all primary regions are unavailable, Vercel automatically fails over to the regions specified in `functionFailoverRegions`, selecting the region geographically closest to the request
  * The order of the regions in `functionFailoverRegions` does not matter as Vercel automatically selects the region geographically closest to the request


To learn more about automatic failover for Vercel Functions, see [Automatic failover](https://vercel.com/docs/functions/configuring-functions/region#automatic-failover). Vercel Functions using the Edge runtime will [automatically failover](https://vercel.com/docs/functions/configuring-functions/region#automatic-failover) with no configuration required.
Region failover is supported with Secure Compute, see [Region Failover](https://vercel.com/docs/secure-compute#region-failover) to learn more.
Want to talk to our team?
This feature is available on the Enterprise plan.
Schedule Call
