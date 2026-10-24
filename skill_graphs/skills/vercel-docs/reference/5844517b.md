##  [Wildcard path forwarding](https://vercel.com/docs/routing/rewrites#wildcard-path-forwarding)[](https://vercel.com/docs/routing/rewrites#wildcard-path-forwarding)
You can capture and forward parts of a path using wildcards:
```
{
  "rewrites": [
    {
      "source": "/docs/:path*",
      "destination": "/help/:path*"
    }
  ]
}
```

Some redirects and rewrites configurations can accidentally become gateways for semantic attacks. Learn how to check and protect your configurations with the [Enhancing Security for Redirects and Rewrites guide](https://vercel.com/kb/guide/enhancing-security-for-redirects-and-rewrites).
A request to `/docs/getting-started/install` will be forwarded to `/help/getting-started/install`.
You can also capture multiple path segments:
```
{
  "rewrites": [
    {
      "source": "/blog/:year/:month/:slug*",
      "destination": "/posts?date=:year-:month&slug=:slug*"
    }
  ]
}
```
