##  [4. Monitor the rollout](https://vercel.com/docs/rolling-releases/rolling-release-deployment#4.-monitor-the-rollout)[](https://vercel.com/docs/rolling-releases/rolling-release-deployment#4.-monitor-the-rollout)
Check the current stage, traffic split, and overall progress:
terminal
```
vercel rolling-release fetch
```

While the rollout is in progress, monitor production logs for errors coming from the new deployment:
terminal
```
vercel logs --environment production --level error --since 5m
```

To filter for specific error patterns:
terminal
```
vercel logs --environment production --level error --query "TypeError" --since 5m --expand
```

Run these checks periodically between stage transitions. If your stages have automatic durations, the rollout advances on its own. If you configured manual approval stages, you'll need to explicitly approve each one.
