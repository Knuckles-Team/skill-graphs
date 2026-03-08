##  [When you need to restore service immediately](https://vercel.com/docs/observability/debug-production-errors#when-you-need-to-restore-service-immediately)[](https://vercel.com/docs/observability/debug-production-errors#when-you-need-to-restore-service-immediately)
If the errors are severe and you need to restore service while you investigate, roll back to the previous production deployment:
terminal
```
vercel rollback
```

This instantly points production traffic to your previous deployment. You can then debug at your own pace and deploy the fix when it's ready.
To check the rollback status:
terminal
```
vercel rollback status
```
