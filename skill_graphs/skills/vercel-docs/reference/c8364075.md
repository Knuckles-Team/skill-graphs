##  [When you need to abort](https://vercel.com/docs/rolling-releases/rolling-release-deployment#when-you-need-to-abort)[](https://vercel.com/docs/rolling-releases/rolling-release-deployment#when-you-need-to-abort)
If you see a spike in errors during any stage, abort the rolling release immediately. This reverts all traffic back to the previous deployment:
terminal
```
vercel rolling-release abort --dpl <deployment-url>
```

After aborting, investigate the errors and fix them before attempting another rollout:
terminal
```
vercel logs --environment production --level error --since 30m --expand
```
