##  [regions](https://vercel.com/docs/project-configuration/vercel-json#regions)[](https://vercel.com/docs/project-configuration/vercel-json#regions)
This value overrides the [Vercel Function Region](https://vercel.com/docs/functions/regions) in Project Settings.
Type: `Array` of region identifier `String`.
Valid values: List of [regions](https://vercel.com/docs/regions), defaults to `iad1`.
You can define the regions where your [Vercel functions](https://vercel.com/docs/functions) are executed. Users on Pro and Enterprise can deploy to multiple regions. Hobby plans can select any single region. To learn more, see [Configuring Regions](https://vercel.com/docs/functions/configuring-functions/region#project-configuration).
Function responses [can be cached](https://vercel.com/docs/cdn-cache) in the requested regions. Selecting a Vercel Function region does not impact static files, which are deployed to every region by default.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "regions": ["sfo1"]
}
```

You can also set `regions` on individual functions using the [`functions`](https://vercel.com/docs/project-configuration#functions) property to override the project-level default. See [per-function region configuration](https://vercel.com/docs/functions/configuring-functions/region#per-function-configuration) for more details.
