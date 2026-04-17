##  [Quick reference](https://vercel.com/docs/observability/debug-production-errors#quick-reference)[](https://vercel.com/docs/observability/debug-production-errors#quick-reference)
Use this block when you already know what you're doing and want the full command sequence. Use the steps below for context and checks.
terminal
```
# 1. Find 500 errors in production
vercel logs --environment production --status-code 5xx --since 1h

# 2. Get structured data to filter programmatically
vercel logs --environment production --status-code 500 --json --since 1h \
  | jq '{path: .path, message: .message, timestamp: .timestamp}'

# 3. Narrow the time range once you know when errors started
vercel logs --environment production --status-code 500 --since 2h --until 1h

# 4. Identify the failing deployment
vercel list --prod
vercel inspect <deployment-url>
vercel inspect <deployment-url> --logs    # build logs

# 5. Correlate with source code
git log --oneline -10
git show <commit-sha> --stat

# 6. Fix locally, then deploy a preview
vercel deploy

# 7. Verify the fix against the preview
vercel curl /api/failing-route --deployment <preview-url>
vercel logs --deployment <preview-deployment-id> --level error

# 8. Ship to production
vercel deploy --prod

# 9. Confirm the fix
vercel logs --environment production --status-code 500 --since 5m

# IF you cannot identify the failing deployment from logs:
vercel bisect --good <good-deployment-url> --bad <bad-deployment-url> --path /api/failing-route

# IF errors are severe and you need to restore service before debugging:
vercel rollback
vercel rollback status
```
