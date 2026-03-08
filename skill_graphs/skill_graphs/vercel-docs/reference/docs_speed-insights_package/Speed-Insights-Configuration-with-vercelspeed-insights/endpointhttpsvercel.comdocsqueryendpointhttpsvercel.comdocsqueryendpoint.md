##  [`endpoint`](https://vercel.com/docs/query#endpoint)[](https://vercel.com/docs/query#endpoint)
The `endpoint` option allows you to report the collected metrics to a different url than the default: `https://yourdomain.com/_vercel/speed-insights/vitals`.
This is useful when deploying several projects under the same domain, as it allows you to keep each application isolated.
For example, when `yourdomain.com` is managed outside of Vercel:
  1. "alice-app" is deployed under `yourdomain.com/alice/*`, vercel alias is `alice-app.vercel.sh`
  2. "bob-app" is deployed under `yourdomain.com/bob/*`, vercel alias is `bob-app.vercel.sh`
  3. `yourdomain.com/_vercel/*` is routed to `alice-app.vercel.sh`


Both applications are sending their metrics to `alice-app.vercel.sh`. To restore the isolation, "bob-app" should use:
```
<SpeedInsights endpoint="https://bob-app.vercel.sh/_vercel/speed-insights/vitals" />
```
