##  [Invalid route destination segment](https://vercel.com/docs/getting-started-with-vercel#invalid-route-destination-segment)[](https://vercel.com/docs/getting-started-with-vercel#invalid-route-destination-segment)
The `source` property follows the syntax from
A colon (`:`) defines the start of a
A named segment parameter defined in the `destination` property must also be defined in the `source` property.
Before
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "source": "/feedback/:type",
  "destination": "/api/feedback/:id"
}
```

After
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "source": "/feedback/:id",
  "destination": "/api/feedback/:id"
}
```
