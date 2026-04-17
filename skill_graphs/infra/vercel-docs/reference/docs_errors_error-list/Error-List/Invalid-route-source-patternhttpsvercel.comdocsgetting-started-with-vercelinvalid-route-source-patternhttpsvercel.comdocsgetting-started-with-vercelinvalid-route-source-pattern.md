##  [Invalid route source pattern](https://vercel.com/docs/getting-started-with-vercel#invalid-route-source-pattern)[](https://vercel.com/docs/getting-started-with-vercel#invalid-route-source-pattern)
The `source` property follows the syntax from `RegExp` syntax.
For example, negative lookaheads must be wrapped in a group.
Before
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "source": "/feedback/(?!general)",
  "destination": "/api/feedback/general"
}
```

After
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "source": "/feedback/((?!general).*)",
  "destination": "/api/feedback/general"
}
```
