##  [Add a new path to a microfrontend](https://vercel.com/docs/deployments#add-a-new-path-to-a-microfrontend)[](https://vercel.com/docs/deployments#add-a-new-path-to-a-microfrontend)
To route paths to a new microfrontend, modify your `microfrontends.json` file. In the `routing` section for the project, add the new path:
microfrontends.json
```
{
  "$schema": "https://openapi.vercel.sh/microfrontends.json",
  "applications": {
    "web": {},
    "docs": {
      "routing": [
        {
          "paths": ["/docs/:path*", "/new-path-to-route"]
        }
      ]
    }
  }
}
```

The routing for this new path will take effect when the code is merged and the deployment is live. You can test the routing changes in Preview or pre-Production to make sure it works as expected before rolling out the change to end users.
Additionally, if you need to revert, you can use [Instant Rollback](https://vercel.com/docs/instant-rollback) to rollback the project to a deployment before the routing change to restore the old routing rules.
Changes to separate microfrontends are not rolled out in lockstep. If you need to modify `microfrontends.json`, make sure that the new application can handle the requests before merging the change. Otherwise use [flags](https://vercel.com/docs/deployments#roll-out-routing-changes-safely-with-flags) to control whether the path is routed to the microfrontend.
###  [Supported path expressions](https://vercel.com/docs/deployments#supported-path-expressions)[](https://vercel.com/docs/deployments#supported-path-expressions)
You can use following path expressions in `microfrontends.json`:
  * `/path` - Constant path.
  * `/:path` - Wildcard that matches a single path segment.
  * `/:path/suffix` - Wildcard that matches a single path segment with a constant path at the end.
  * `/prefix/:path*` - Path that ends with a wildcard that can match zero or more path segments.
  * `/prefix/:path+` - Path that ends with a wildcard that matches one or more path segments.
  * `/\\(a\\)` - Path is `/(a)`, special characters in paths are escaped with a backslash.
  * `/:path(a|b)` - Path is either `/a` or `/b`.
  * `/:path(a|\\(b\\))` - Path is either `/a` or `/(b)`, special characters are escaped with a backslash.
  * `/:path((?!a|b).*)` - Path is any single path except `/a` or `/b`.
  * `/prefix-:path-suffix` - Path that starts with `/prefix-`, ends with `-suffix`, and contains a single path segment.


The following are not supported:
  * Conflicting or overlapping paths: Paths must uniquely map to one microfrontend
  * Regular expressions not included above
  * Wildcards that can match multiple path segments (`+`, `*`) that do not come at the end of the expression


Test your path expression
Path expression
Path to test
To assert whether the path expressions will work for your path, use the [`validateRouting` test utility](https://vercel.com/docs/microfrontends/troubleshooting#validaterouting) to add unit tests that ensure paths get routed to the correct microfrontend.
