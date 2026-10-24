##  [Same-application rewrites](https://vercel.com/docs/routing/rewrites#same-application-rewrites)[](https://vercel.com/docs/routing/rewrites#same-application-rewrites)
Same-application rewrites route requests to different destinations within your project. Common uses include:
  * Friendly URLs: Transform `/products/t-shirts` into `/catalog?category=t-shirts`
  * Device-specific content: Show different layouts based on device type
  * A/B testing: Route users to different versions of a page
  * Country-specific content: Show region-specific content based on the user's location


Example: Route image resize requests to a serverless function:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/resize/:width/:height",
      "destination": "/api/sharp"
    }
  ]
}
```

This converts a request like `/resize/800/600` to `/api/sharp?width=800&height=600`.
Example: Route UK visitors to a UK-specific section:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/:path((?!uk/).*)",
      "has": [
        { "type": "header", "key": "x-vercel-ip-country", "value": "GB" }
      ],
      "destination": "/uk/:path*"
    }
  ]
}
```

This routes a UK visitor requesting `/about` to `/uk/about`.
