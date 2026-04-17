##  [Quick reference](https://vercel.com/docs/rolling-releases/rolling-release-deployment#quick-reference)[](https://vercel.com/docs/rolling-releases/rolling-release-deployment#quick-reference)
Use this block when you already know what you're doing and want the full command sequence. Use the steps below for context and checks.
terminal
```
# 1. Configure rolling release stages
vercel rolling-release configure --cfg '{"enabled":true,"advancementType":"automatic","stages":[{"targetPercentage":10,"duration":5},{"targetPercentage":50,"duration":10},{"targetPercentage":100}]}'

# 2. Deploy to production (triggers rolling release automatically)
vercel deploy --prod

# 3. Start the rolling release
vercel rolling-release start --dpl <deployment-url>

# 4. Monitor the rollout
vercel rolling-release fetch
vercel logs --environment production --level error --since 5m

# 5. Advance to the next stage (if manual approval is configured)
vercel rolling-release approve --dpl <deployment-url> --currentStageIndex 0

# IF errors spike during rollout:
vercel rolling-release abort --dpl <deployment-url>

# 6. Complete the rollout (100% traffic)
vercel rolling-release complete --dpl <deployment-url>
```
