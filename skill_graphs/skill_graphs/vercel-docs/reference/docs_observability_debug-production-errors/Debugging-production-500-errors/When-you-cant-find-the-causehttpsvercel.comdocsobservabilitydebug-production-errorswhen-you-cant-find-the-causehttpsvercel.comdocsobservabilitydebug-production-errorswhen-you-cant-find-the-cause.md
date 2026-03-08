##  [When you can't find the cause](https://vercel.com/docs/observability/debug-production-errors#when-you-can't-find-the-cause)[](https://vercel.com/docs/observability/debug-production-errors#when-you-can't-find-the-cause)
If the error started between two deployments and you can't pinpoint the change, use `vercel bisect` to binary-search through your deployment history:
terminal
```
vercel bisect --good <good-deployment-url> --bad <bad-deployment-url> --path /api/failing-route
```

This steps through deployments between the good and bad ones, letting you identify exactly which deployment introduced the regression.
