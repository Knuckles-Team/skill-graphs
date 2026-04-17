##  [functions](https://vercel.com/docs/project-configuration/vercel-json#functions)[](https://vercel.com/docs/project-configuration/vercel-json#functions)
Type: `Object` of key `String` and value `Object`.
###  [Key definition](https://vercel.com/docs/project-configuration/vercel-json#key-definition)[](https://vercel.com/docs/project-configuration/vercel-json#key-definition)
A
  * `api/*.js` (matches one level e.g. `api/hello.js` but not `api/hello/world.js`)
  * `api/**/*.ts` (matches all levels `api/hello.ts` and `api/hello/world.ts`)
  * `src/pages/**/*` (matches all functions from `src/pages`)
  * `api/test.js`


###  [Value definition](https://vercel.com/docs/project-configuration/vercel-json#value-definition)[](https://vercel.com/docs/project-configuration/vercel-json#value-definition)
  * `runtime` (optional): The npm package name of a [Runtime](https://vercel.com/docs/functions/runtimes), including its version.
  * `memory`: Memory cannot be set in `vercel.json` with [Fluid compute](https://vercel.com/docs/fluid-compute) enabled. Instead set it in the Functions section in your project dashboard sidebar. See [setting default function memory](https://vercel.com/docs/functions/configuring-functions/memory#setting-your-default-function-memory-/-cpu-size) for more information.
  * `maxDuration` (optional): An integer defining how long your Vercel Function should be allowed to run on every request in seconds (between `1` and the maximum limit of your plan, as mentioned below).
  * `supportsCancellation` (optional): A boolean defining whether your Vercel Function should [support request cancellation](https://vercel.com/docs/functions/functions-api-reference#cancel-requests). This is only available when you're using the Node.js runtime.
  * `includeFiles` (optional): A `next.config.js` )
  * `excludeFiles` (optional): A `next.config.js` )
  * `regions` (optional): An array of [region](https://vercel.com/docs/regions) identifiers specifying where this specific function should be deployed. This overrides the project-level [`regions`](https://vercel.com/docs/project-configuration#regions) setting for the matched functions. See [per-function region configuration](https://vercel.com/docs/functions/configuring-functions/region#per-function-configuration) for more details.
  * `functionFailoverRegions` (optional): An array of [region](https://vercel.com/docs/regions) identifiers specifying passive regions this specific function can fail over to during an outage. This overrides the project-level [`functionFailoverRegions`](https://vercel.com/docs/project-configuration#functionfailoverregions) setting for the matched functions. Enterprise only. See [per-function region configuration](https://vercel.com/docs/functions/configuring-functions/region#per-function-configuration) for more details.


###  [Description](https://vercel.com/docs/project-configuration/vercel-json#description)[](https://vercel.com/docs/project-configuration/vercel-json#description)
By default, no configuration is needed to deploy Vercel functions to Vercel.
For all [officially supported runtimes](https://vercel.com/docs/functions/runtimes), the only requirement is to create an `api` directory at the root of your project directory, placing your Vercel functions inside.
The `functions` property cannot be used in combination with `builds`. Since the latter is a legacy configuration property, we recommend dropping it in favor of the new one.
Because [Incremental Static Regeneration (ISR)](https://vercel.com/docs/incremental-static-regeneration) uses Vercel functions, the same configurations apply. The ISR route can be defined using a glob pattern, and accepts the same properties as when using Vercel functions.
When deployed, each Vercel Function receives the following properties:
  * Memory: 1024 MB (1 GB) - (Optional)
  * Maximum Duration: 10s default - 60s / 1 minute (Hobby), 15s default - 300s / 5 minutes (Pro), or 15s default - 900s / 15 minutes (Enterprise). This [can be configured](https://vercel.com/docs/functions/configuring-functions/duration) up to the respective plan limit) - (Optional)


To configure them, you can add the `functions` property.
####  [`functions` property with Vercel functions](https://vercel.com/docs/project-configuration/vercel-json#functions-property-with-vercel-functions)[](https://vercel.com/docs/project-configuration/vercel-json#functions-property-with-vercel-functions)
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/test.js": {
      "memory": 3009,
      "maxDuration": 30
    },
    "api/*.js": {
      "memory": 3009,
      "maxDuration": 30
    }
  }
}
```

####  [`functions` property with ISR](https://vercel.com/docs/project-configuration/vercel-json#functions-property-with-isr)[](https://vercel.com/docs/project-configuration/vercel-json#functions-property-with-isr)
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "pages/blog/[hello].tsx": {
      "memory": 1024
    },
    "src/pages/isr/**/*": {
      "maxDuration": 10
    }
  }
}
```

####  [Per-function `regions` and `functionFailoverRegions`](https://vercel.com/docs/project-configuration/vercel-json#per-function-regions-and-functionfailoverregions)[](https://vercel.com/docs/project-configuration/vercel-json#per-function-regions-and-functionfailoverregions)
You can set `regions` and `functionFailoverRegions` on individual functions to override the project-level defaults. This is useful when different functions need to run in different regions, for example when they access different data sources.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "regions": ["iad1"],
  "functions": {
    "api/eu-data.js": {
      "regions": ["cdg1"],
      "functionFailoverRegions": ["lhr1"]
    },
    "api/us-data.js": {
      "regions": ["sfo1", "iad1"],
      "functionFailoverRegions": ["pdx1"]
    }
  }
}
```

In the example above, `api/eu-data.js` runs in Paris (`cdg1`) with London (`lhr1`) as a failover, while `api/us-data.js` runs in San Francisco (`sfo1`) and Washington, D.C. (`iad1`) with Portland (`pdx1`) as a failover. All other functions use the project-level default of `iad1`.
###  [Using unsupported runtimes](https://vercel.com/docs/project-configuration/vercel-json#using-unsupported-runtimes)[](https://vercel.com/docs/project-configuration/vercel-json#using-unsupported-runtimes)
In order to use a runtime that is not [officially supported](https://vercel.com/docs/functions/runtimes), you can add a `runtime` property to the definition:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/test.php": {
      "runtime": "vercel-php@0.5.2"
    }
  }
}
```

In the example above, the `api/test.php` Vercel Function does not use one of the [officially supported runtimes](https://vercel.com/docs/functions/runtimes). In turn, a `runtime` property was added in order to invoke the
For more information on Runtimes, see the [Runtimes documentation](https://vercel.com/docs/functions/runtimes):
