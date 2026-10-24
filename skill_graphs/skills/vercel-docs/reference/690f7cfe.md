##  [Legacy](https://vercel.com/docs/project-configuration/vercel-json#legacy)[](https://vercel.com/docs/project-configuration/vercel-json#legacy)
Legacy properties are still supported for backwards compatibility, but are deprecated.
###  [name](https://vercel.com/docs/project-configuration/vercel-json#name)[](https://vercel.com/docs/project-configuration/vercel-json#name)
The `name` property has been deprecated in favor of [Project Linking](https://vercel.com/docs/cli/project-linking), which allows you to link a Vercel project to your local codebase when you run `vercel`.
Type: `String`.
Valid values: string name for the deployment.
Limits:
  * A maximum length of 52 characters
  * Only lower case alphanumeric characters or hyphens are allowed
  * Cannot begin or end with a hyphen, or contain multiple consecutive hyphens


The prefix for all new deployment instances. Vercel CLI usually generates this field automatically based on the name of the directory. But if you'd like to define it explicitly, this is the way to go.
The defined name is also used to organize the deployment into [a project](https://vercel.com/docs/projects/overview).
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "name": "example-app"
}
```

###  [version](https://vercel.com/docs/project-configuration/vercel-json#version)[](https://vercel.com/docs/project-configuration/vercel-json#version)
The `version` property should not be used anymore.
Type: `Number`.
Valid values: `1`, `2`.
Specifies the Vercel Platform version the deployment should use.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "version": 2
}
```

###  [alias](https://vercel.com/docs/project-configuration/vercel-json#alias)[](https://vercel.com/docs/project-configuration/vercel-json#alias)
The `alias` property should not be used anymore. To assign a custom Domain to your project, please [define it in the Project Settings](https://vercel.com/docs/domains/add-a-domain) instead. Once your domains are, they will take precedence over the configuration property.
Type: `Array` or `String`.
Valid values: [domain names](https://vercel.com/docs/domains/add-a-domain) (optionally including subdomains) added to the account, or a string for a suffixed URL using `.vercel.app` or a Custom Deployment Suffix ([available on the Enterprise plan](https://vercel.com/pricing)).
Limit: A maximum of 64 aliases in the array.
The alias or aliases are applied automatically using [Vercel for GitHub](https://vercel.com/docs/git/vercel-for-github), [Vercel for GitLab](https://vercel.com/docs/git/vercel-for-gitlab), or [Vercel for Bitbucket](https://vercel.com/docs/git/vercel-for-bitbucket) when merging or pushing to the [Production Branch](https://vercel.com/docs/git#production-branch).
You can deploy to the defined aliases using [Vercel CLI](https://vercel.com/docs/cli) by setting the [production deployment environment target](https://vercel.com/docs/domains/deploying-and-redirecting).
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "alias": ["my-domain.com", "my-alias"]
}
```

###  [scope](https://vercel.com/docs/project-configuration/vercel-json#scope)[](https://vercel.com/docs/project-configuration/vercel-json#scope)
The `scope` property has been deprecated in favor of [Project Linking](https://vercel.com/docs/cli/project-linking), which allows you to link a Vercel project to your local codebase when you run `vercel`.
Type: `String`.
Valid values: For teams, either an ID or slug. For users, either a email address, username, or ID.
This property determines the scope ([Hobby team](https://vercel.com/docs/accounts/create-an-account#creating-a-hobby-account) or [team](https://vercel.com/docs/accounts/create-a-team)) under which the project will be deployed by [Vercel CLI](https://vercel.com/cli).
It also affects any other actions that the user takes within the directory that contains this configuration (e.g. listing [environment variables](https://vercel.com/docs/environment-variables) using `vercel secrets ls`).
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "scope": "my-team"
}
```

Deployments made through [Git](https://vercel.com/docs/git) will ignore the `scope` property because the repository is already connected to [project](https://vercel.com/docs/projects/overview).
###  [env](https://vercel.com/docs/project-configuration/vercel-json#env)[](https://vercel.com/docs/project-configuration/vercel-json#env)
We recommend against using this property. To add custom environment variables to your project [define them in the Project Settings](https://vercel.com/docs/environment-variables).
Type: `Object` of `String` keys and values.
Valid values: environment keys and values.
Environment variables passed to the invoked [Vercel functions](https://vercel.com/docs/functions).
This example will pass the `MY_KEY` static env to all [Vercel functions](https://vercel.com/docs/functions) and the `SECRET` resolved from the `my-secret-name` [secret](https://vercel.com/docs/environment-variables/reserved-environment-variables) dynamically.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "env": {
    "MY_KEY": "this is the value",
    "SECRET": "@my-secret-name"
  }
}
```

###  [build.env](https://vercel.com/docs/project-configuration/vercel-json#build.env)[](https://vercel.com/docs/project-configuration/vercel-json#build.env)
We recommend against using this property. To add custom environment variables to your project [define them in the Project Settings](https://vercel.com/docs/environment-variables).
Type: `Object` of `String` keys and values inside the `build` `Object`.
Valid values: environment keys and values.
[Environment variables](https://vercel.com/docs/environment-variables) passed to the [Build](https://vercel.com/docs/deployments/configure-a-build) processes.
The following example will pass the `MY_KEY` environment variable to all [Builds](https://vercel.com/docs/deployments/configure-a-build) and the `SECRET` resolved from the `my-secret-name` [secret](https://vercel.com/docs/environment-variables/reserved-environment-variables) dynamically.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "env": {
    "MY_KEY": "this is the value",
    "SECRET": "@my-secret-name"
  }
}
```

###  [builds](https://vercel.com/docs/project-configuration/vercel-json#builds)[](https://vercel.com/docs/project-configuration/vercel-json#builds)
We recommend against using this property. To customize Vercel functions, please use the [functions](https://vercel.com/docs/project-configuration/vercel-json#functions) property instead. If you'd like to deploy a monorepo, see the [Monorepo docs](https://vercel.com/docs/monorepos).
Type: `Array` of build `Object`.
Valid values: a list of build descriptions whose `src` references valid source files.
####  [Build object definition](https://vercel.com/docs/project-configuration/vercel-json#build-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#build-object-definition)
  * `src` (`String`): A glob expression or pathname. If more than one file is resolved, one build will be created per matched file. It can include `*` and `**`.
  * `use` (`String`): An npm module to be installed by the build process. It can include a semver compatible version (e.g.: `@org/proj@1`).
  * `config` (`Object`): Optionally, an object including arbitrary metadata to be passed to the Builder.


The following will include all HTML files as-is (to be served statically), and build all Python files and JS files into [Vercel functions](https://vercel.com/docs/functions):
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "builds": [
    { "src": "*.html", "use": "@vercel/static" },
    { "src": "*.py", "use": "@vercel/python" },
    { "src": "*.js", "use": "@vercel/node" }
  ]
}
```

When at least one `builds` item is specified, only the outputs of the build processes will be included in the resulting deployment as a security precaution. This is why we need to allowlist static files explicitly with `@vercel/static`.
###  [routes](https://vercel.com/docs/project-configuration/vercel-json#routes)[](https://vercel.com/docs/project-configuration/vercel-json#routes)
We recommend using [cleanUrls](https://vercel.com/docs/project-configuration/vercel-json#cleanurls), [trailingSlash](https://vercel.com/docs/project-configuration/vercel-json#trailingslash), [redirects](https://vercel.com/docs/project-configuration/vercel-json#redirects), [rewrites](https://vercel.com/docs/project-configuration/vercel-json#rewrites), and/or [headers](https://vercel.com/docs/project-configuration/vercel-json#headers) instead.
The `routes` property is only meant to be used for advanced integration purposes, such as the [Build Output API](https://vercel.com/docs/build-output-api/v3), and cannot be used in conjunction with any of the properties mentioned above.
See the [upgrading routes section](https://vercel.com/docs/project-configuration/vercel-json#upgrading-legacy-routes) to learn how to migrate away from this property.
Type: `Array` of route `Object`.
Valid values: a list of route definitions.
####  [Route object definition](https://vercel.com/docs/project-configuration/vercel-json#route-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#route-object-definition)
  * `src`: A
  * `methods`: A set of HTTP method types. If no method is provided, requests with any HTTP method will be a candidate for the route.
  * `dest`: A destination pathname or full URL, including querystring, with the ability to embed capture groups as $1, $2…
  * `headers`: A set of headers to apply for responses.
  * `status`: A status code to respond with. Can be used in tandem with `Location:` header to implement redirects.
  * `continue`: A boolean to change matching behavior. If `true`, routing will continue even when the `src` is matched.
  * `has`: An optional array of `has` objects with the `type`, `key` and `value` properties. Used for conditional path matching based on the presence of specified properties
  * `missing`: An optional array of `missing` objects with the `type`, `key` and `value` properties. Used for conditional path matching based on the absence of specified properties
  * `mitigate`: An optional object with the property `action`, which can either be "challenge" or "deny". These perform [mitigation actions](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-configuration) on requests that match the route.
  * `transforms`: An optional array of `transform` objects to apply. Transform rules let you append, set, or remove request/response headers and query parameters at the edge so you can enforce security headers, inject analytics tags, or personalize content without touching your application code. See examples [below](https://vercel.com/docs/project-configuration/vercel-json#transform-examples).


Routes are processed in the order they are defined in the array, so wildcard/catch-all patterns should usually be last.
####  [Route has and missing object definition](https://vercel.com/docs/project-configuration/vercel-json#route-has-and-missing-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#route-has-and-missing-object-definition)
Property | Type | Description
---|---|---
`type` | `String` | Must be either `header`, `cookie`, `host`, or `query`. The `type` property only applies to request headers sent by clients, not response headers sent by your functions or backends.
`key` | `String` | The key from the selected type to match against. For example, if the `type` is `header` and the `key` is `X-Custom-Header`, we will match against the `X-Custom-Header` header key.
`value` |  `String` or `Object` or `undefined` | The value to check for, if `undefined` any value will match. A regex like string can be used to capture a specific part of the value. For example, if the value `first-(?<paramName>.*)` is used for `first-second` then `second` will be usable in the destination with `:paramName`. If an object is provided, it will match when all conditions are met for its fields below.
If `value` is an object, it has one or more of the following fields:
Condition | Type | Description
---|---|---
`eq` |  `String` (optional) | Check for equality
`neq` |  `String` (optional) | Check for inequality
`inc` |  `Array<String>` (optional) | Check for inclusion in the array
`ninc` |  `Array<String>` (optional) | Check for non-inclusion in the array
`pre` |  `String` (optional) | Check for prefix
`suf` |  `String` (optional) | Check for suffix
`re` |  `String` (optional) | Check for a regex match
`gt` |  `Number` (optional) | Check for greater than
`gte` |  `Number` (optional) | Check for greater than or equal to
`lt` |  `Number` (optional) | Check for less than
`lte` |  `Number` (optional) | Check for less than or equal to
This example uses the expressive `value` object to define a route that will only rewrite users to `/end` if the `X-Custom-Header` header's value is prefixed by `valid` and ends with `value`:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/start",
      "dest": "/end",
      "has": [
        {
          "type": "header",
          "key": "X-Custom-Header",
          "value": {
            "pre": "valid",
            "suf": "value"
          }
        }
      ]
    }
  ]
}
```

This example configures custom routes that map to static files and [Vercel functions](https://vercel.com/docs/functions):
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/redirect",
      "status": 308,
      "headers": { "Location": "https://example.com/" }
    },
    {
      "src": "/custom-page",
      "headers": { "cache-control": "s-maxage=1000" },
      "dest": "/index.html"
    },
    { "src": "/api", "dest": "/my-api.js" },
    { "src": "/users", "methods": ["POST"], "dest": "/users-api.js" },
    { "src": "/users/(?<id>[^/]*)", "dest": "/users-api.js?id=$id" },
    { "src": "/legacy", "status": 404 },
    { "src": "/.*", "dest": "https://my-old-site.com" }
  ]
}
```

###  [Transform object definition](https://vercel.com/docs/project-configuration/vercel-json#transform-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#transform-object-definition)
Property | Type | Description
---|---|---
`type` | `String` | Must be either `request.query`, `request.headers`, or `response.headers`. This specifies the scope of what your transforms will apply to.
`op` | `String` | These specify the possible operations:
- `append` appends `args` to the value of the key, and will set if missing
- `set` sets the key and value if missing
- `delete` deletes the key entirely if `args` is not provided; otherwise, it will delete the value of `args` from the matching key
`target` | `Object` | An object with key `key`, which is either a `String` or an `Object`. If it is a string, it will be used as the key for the target. If it is an object, it may contain one or more of the properties [seen below.](https://vercel.com/docs/project-configuration/vercel-json#transform-target-object-definition)
`args` |  `String` or `String[]` or `undefined` | If `args` is a string or string array, it will be used as the value for the target according to the `op` property.
####  [Transform target object definition](https://vercel.com/docs/project-configuration/vercel-json#transform-target-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#transform-target-object-definition)
Target is an object with a `key` property. For the `set` operation, the `key` property is used as the header or query key. For other operations, it is used as a matching condition to determine if the transform should be applied.
Property | Type | Description
---|---|---
`key` |  `String` or `Object` | It may be a string or an object. If it is an object, it must have one or more of the properties defined in the [Transform key object definition](https://vercel.com/docs/project-configuration/vercel-json#transform-key-object-definition) below.
####  [Transform key object definition](https://vercel.com/docs/project-configuration/vercel-json#transform-key-object-definition)[](https://vercel.com/docs/project-configuration/vercel-json#transform-key-object-definition)
When the `key` property is an object, it can contain one or more of the following conditional matching properties:
Property | Type | Description
---|---|---
`eq` |  `String` or `Number` | Check equality on a value
`neq` | `String` | Check inequality on a value
`inc` | `String[]` | Check inclusion in an array of values
`ninc` | `String[]` | Check non-inclusion in an array of values
`pre` | `String` | Check if value starts with a prefix
`suf` | `String` | Check if value ends with a suffix
`gt` | `Number` | Check if value is greater than
`gte` | `Number` | Check if value is greater than or equal to
`lt` | `Number` | Check if value is less than
`lte` | `Number` | Check if value is less than or equal to
####  [Transform examples](https://vercel.com/docs/project-configuration/vercel-json#transform-examples)[](https://vercel.com/docs/project-configuration/vercel-json#transform-examples)
These examples demonstrate practical use-cases for route transforms.
In this example, you remove the incoming request header `x-custom-header` from all requests and responses to the `/home` route:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/home",
      "transforms": [
        {
          "type": "request.headers",
          "op": "delete",
          "target": {
            "key": "x-custom-header"
          }
        },
        {
          "type": "response.headers",
          "op": "delete",
          "target": {
            "key": "x-custom-header"
          }
        }
      ]
    }
  ]
}
```

In this example, you override the incoming query parameter `theme` to `dark` for all requests to the `/home` route, and set if it doesn't already exist:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/home",
      "transforms": [
        {
          "type": "request.query",
          "op": "set",
          "target": {
            "key": "theme"
          },
          "args": "dark"
        }
      ]
    }
  ]
}
```

In this example, you append multiple values to the incoming request header `x-content-type-options` for all requests to the `/home` route:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/home",
      "transforms": [
        {
          "type": "request.headers",
          "op": "append",
          "target": {
            "key": "x-content-type-options"
          },
          "args": ["nosniff", "no-sniff"]
        }
      ]
    }
  ]
}
```

In this example, you delete any header that begins with `x-react-router-` for all requests to the `/home` route:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/home",
      "transforms": [
        {
          "type": "request.headers",
          "op": "delete",
          "target": {
            "key": {
              "pre": "x-react-router-"
            }
          }
        }
      ]
    }
  ]
}
```

You can integrate transforms with existing matching capabilities through the [`has` and `missing` properties for routes](https://vercel.com/docs/project-configuration#routes), along with using expressive matching conditions through the [Transform key object definition](https://vercel.com/docs/project-configuration/vercel-json#transform-key-object-definition).
###  [Upgrading legacy routes](https://vercel.com/docs/project-configuration/vercel-json#upgrading-legacy-routes)[](https://vercel.com/docs/project-configuration/vercel-json#upgrading-legacy-routes)
In most cases, you can upgrade legacy `routes` usage to the newer [`rewrites`](https://vercel.com/docs/project-configuration#rewrites), [`redirects`](https://vercel.com/docs/project-configuration#redirects), [`headers`](https://vercel.com/docs/project-configuration#headers), [`cleanUrls`](https://vercel.com/docs/project-configuration#cleanurls) or [`trailingSlash`](https://vercel.com/docs/project-configuration#trailingslash) properties.
Here are some examples that show how to upgrade legacy `routes` to the equivalent new property.
####  [Route Parameters](https://vercel.com/docs/project-configuration/vercel-json#route-parameters)[](https://vercel.com/docs/project-configuration/vercel-json#route-parameters)
With `routes`, you use a `/product/532004` and proxies to `/api/product?id=532004`:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [{ "src": "/product/(?<id>[^/]+)", "dest": "/api/product?id=$id" }]
}
```

With [`rewrites`](https://vercel.com/docs/project-configuration#rewrites), named parameters are automatically passed in the query string. The following example is equivalent to the legacy `routes` usage above, but uses `rewrites` instead:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [{ "source": "/product/:id", "destination": "/api/product" }]
}
```

####  [Legacy redirects](https://vercel.com/docs/project-configuration/vercel-json#legacy-redirects)[](https://vercel.com/docs/project-configuration/vercel-json#legacy-redirects)
With `routes`, you specify the status code to use a 307 Temporary Redirect. Also, this redirect needs to be defined before other routes. The following example redirects all paths in the `posts` directory to the `blog` directory, but keeps the path in the new location:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/posts/(.*)",
      "headers": { "Location": "/blog/$1" },
      "status": 307
    }
  ]
}
```

With [`redirects`](https://vercel.com/docs/project-configuration#redirects), you disable the `permanent` property to use a 307 Temporary Redirect. Also, `redirects` are always processed before `rewrites`. The following example is equivalent to the legacy `routes` usage above, but uses `redirects` instead:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "redirects": [
    {
      "source": "/posts/:id",
      "destination": "/blog/:id",
      "permanent": false
    }
  ]
}
```

####  [Legacy SPA Fallback](https://vercel.com/docs/project-configuration/vercel-json#legacy-spa-fallback)[](https://vercel.com/docs/project-configuration/vercel-json#legacy-spa-fallback)
With `routes`, you use `"handle": "filesystem"` to give precedence to the filesystem and exit early if the requested path matched a file. The following example will serve the `index.html` file for all paths that do not match a file in the filesystem:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    { "handle": "filesystem" },
    { "src": "/(.*)", "dest": "/index.html" }
  ]
}
```

With [`rewrites`](https://vercel.com/docs/project-configuration#rewrites), the filesystem check is the default behavior. If you want to change the name of files at the filesystem level, file renames can be performed during the [Build Step](https://vercel.com/docs/deployments/configure-a-build), but not with `rewrites`. The following example is equivalent to the legacy `routes` usage above, but uses `rewrites` instead:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
```

####  [Legacy Headers](https://vercel.com/docs/project-configuration/vercel-json#legacy-headers)[](https://vercel.com/docs/project-configuration/vercel-json#legacy-headers)
With `routes`, you use `"continue": true` to prevent stopping at the first match. The following example adds `Cache-Control` headers to the favicon and other static assets:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/favicon.ico",
      "headers": { "Cache-Control": "public, max-age=3600" },
      "continue": true
    },
    {
      "src": "/assets/(.*)",
      "headers": { "Cache-Control": "public, max-age=31556952, immutable" },
      "continue": true
    }
  ]
}
```

With [`headers`](https://vercel.com/docs/project-configuration#headers), this is no longer necessary since that is the default behavior. The following example is equivalent to the legacy `routes` usage above, but uses `headers` instead:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "headers": [
    {
      "source": "/favicon.ico",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=3600"
        }
      ]
    },
    {
      "source": "/assets/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31556952, immutable"
        }
      ]
    }
  ]
}
```

####  [Legacy Pattern Matching](https://vercel.com/docs/project-configuration/vercel-json#legacy-pattern-matching)[](https://vercel.com/docs/project-configuration/vercel-json#legacy-pattern-matching)
With `routes`, you need to escape a dot with two backslashes, otherwise it would match any character `atom.xml` and proxies to `/api/rss` to dynamically generate RSS:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [{ "src": "/atom\\.xml", "dest": "/api/rss" }]
}
```

With [`rewrites`](https://vercel.com/docs/project-configuration#rewrites), the `.` is not a special character so it does not need to be escaped. The following example is equivalent to the legacy `routes` usage above, but instead uses `rewrites`:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [{ "source": "/atom.xml", "destination": "/api/rss" }]
}
```

####  [Legacy Negative Lookahead](https://vercel.com/docs/project-configuration/vercel-json#legacy-negative-lookahead)[](https://vercel.com/docs/project-configuration/vercel-json#legacy-negative-lookahead)
With `routes`, you use `/maintenance` page except for `/maintenance` itself to avoid infinite loop:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [{ "src": "/(?!maintenance)", "dest": "/maintenance" }]
}
```

With [`rewrites`](https://vercel.com/docs/project-configuration#rewrites), the Regex needs to be wrapped. The following example is equivalent to the legacy `routes` usage above, but instead uses `rewrites`:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    { "source": "/((?!maintenance).*)", "destination": "/maintenance" }
  ]
}
```

####  [Legacy Case Sensitivity](https://vercel.com/docs/project-configuration/vercel-json#legacy-case-sensitivity)[](https://vercel.com/docs/project-configuration/vercel-json#legacy-case-sensitivity)
With `routes`, the `src` property is case-insensitive leading to duplicate content, where multiple request paths with difference cases serve the same page.
With [`rewrites`](https://vercel.com/docs/project-configuration#rewrites) / [`redirects`](https://vercel.com/docs/project-configuration#redirects) / [`headers`](https://vercel.com/docs/project-configuration#headers), the `source` property is case-sensitive so you don't accidentally create duplicate content.
* * *
[ Previous Project Configuration ](https://vercel.com/docs/project-configuration)[ Next vercel.ts ](https://vercel.com/docs/project-configuration/vercel-ts)
Was this helpful?
Send
On this page
  * [schema autocomplete](https://vercel.com/docs/project-configuration/vercel-json#schema-autocomplete)
  * [buildCommand](https://vercel.com/docs/project-configuration/vercel-json#buildcommand)
  * [bunVersion](https://vercel.com/docs/project-configuration/vercel-json#bunversion)
  * [cleanUrls](https://vercel.com/docs/project-configuration/vercel-json#cleanurls)
  * [crons](https://vercel.com/docs/project-configuration/vercel-json#crons)
  * [Cron object definition](https://vercel.com/docs/project-configuration/vercel-json#cron-object-definition)
  * [devCommand](https://vercel.com/docs/project-configuration/vercel-json#devcommand)
  * [fluid](https://vercel.com/docs/project-configuration/vercel-json#fluid)
  * [framework](https://vercel.com/docs/project-configuration/vercel-json#framework)
  * [functions](https://vercel.com/docs/project-configuration/vercel-json#functions)
  * [Key definition](https://vercel.com/docs/project-configuration/vercel-json#key-definition)
  * [Value definition](https://vercel.com/docs/project-configuration/vercel-json#value-definition)
  * [Description](https://vercel.com/docs/project-configuration/vercel-json#description)
  * [functions property with Vercel functions](https://vercel.com/docs/project-configuration/vercel-json#functions-property-with-vercel-functions)
  * [functions property with ISR](https://vercel.com/docs/project-configuration/vercel-json#functions-property-with-isr)
  * [Per-function regions and functionFailoverRegions](https://vercel.com/docs/project-configuration/vercel-json#per-function-regions-and-functionfailoverregions)
  * [Using unsupported runtimes](https://vercel.com/docs/project-configuration/vercel-json#using-unsupported-runtimes)
  * [headers](https://vercel.com/docs/project-configuration/vercel-json#headers)
  * [Header object definition](https://vercel.com/docs/project-configuration/vercel-json#header-object-definition)
  * [Header has or missing object definition](https://vercel.com/docs/project-configuration/vercel-json#header-has-or-missing-object-definition)
  * [ignoreCommand](https://vercel.com/docs/project-configuration/vercel-json#ignorecommand)
  * [installCommand](https://vercel.com/docs/project-configuration/vercel-json#installcommand)
  * [images](https://vercel.com/docs/project-configuration/vercel-json#images)
  * [Value definition](https://vercel.com/docs/project-configuration/vercel-json#value-definition)
  * [outputDirectory](https://vercel.com/docs/project-configuration/vercel-json#outputdirectory)
  * [public](https://vercel.com/docs/project-configuration/vercel-json#public)
  * [redirects](https://vercel.com/docs/project-configuration/vercel-json#redirects)
  * [Redirects examples](https://vercel.com/docs/project-configuration/vercel-json#redirects-examples)
  * [Redirect object definition](https://vercel.com/docs/project-configuration/vercel-json#redirect-object-definition)
  * [Redirect has or missing object definition](https://vercel.com/docs/project-configuration/vercel-json#redirect-has-or-missing-object-definition)
  * [bulkRedirectsPath](https://vercel.com/docs/project-configuration/vercel-json#bulkredirectspath)
  * [CSV](https://vercel.com/docs/project-configuration/vercel-json#csv)
  * [JSON](https://vercel.com/docs/project-configuration/vercel-json#json)
  * [JSONL](https://vercel.com/docs/project-configuration/vercel-json#jsonl)
  * [Bulk redirect field definition](https://vercel.com/docs/project-configuration/vercel-json#bulk-redirect-field-definition)
  * [regions](https://vercel.com/docs/project-configuration/vercel-json#regions)
  * [functionFailoverRegions](https://vercel.com/docs/project-configuration/vercel-json#functionfailoverregions)
  * [rewrites](https://vercel.com/docs/project-configuration/vercel-json#rewrites)
  * [Rewrites examples](https://vercel.com/docs/project-configuration/vercel-json#rewrites-examples)
  * [Rewrite object definition](https://vercel.com/docs/project-configuration/vercel-json#rewrite-object-definition)
  * [Rewrite has or missing object definition](https://vercel.com/docs/project-configuration/vercel-json#rewrite-has-or-missing-object-definition)
  * [trailingSlash](https://vercel.com/docs/project-configuration/vercel-json#trailingslash)
  * [false](https://vercel.com/docs/project-configuration/vercel-json#false)
  * [true](https://vercel.com/docs/project-configuration/vercel-json#true)
  * [undefined](https://vercel.com/docs/project-configuration/vercel-json#undefined)
  * [Legacy](https://vercel.com/docs/project-configuration/vercel-json#legacy)
  * [name](https://vercel.com/docs/project-configuration/vercel-json#name)
  * [version](https://vercel.com/docs/project-configuration/vercel-json#version)
  * [alias](https://vercel.com/docs/project-configuration/vercel-json#alias)
  * [scope](https://vercel.com/docs/project-configuration/vercel-json#scope)
  * [env](https://vercel.com/docs/project-configuration/vercel-json#env)
  * [build.env](https://vercel.com/docs/project-configuration/vercel-json#build.env)
  * [builds](https://vercel.com/docs/project-configuration/vercel-json#builds)
  * [Build object definition](https://vercel.com/docs/project-configuration/vercel-json#build-object-definition)
  * [routes](https://vercel.com/docs/project-configuration/vercel-json#routes)
  * [Route object definition](https://vercel.com/docs/project-configuration/vercel-json#route-object-definition)
  * [Route has and missing object definition](https://vercel.com/docs/project-configuration/vercel-json#route-has-and-missing-object-definition)
  * [Transform object definition](https://vercel.com/docs/project-configuration/vercel-json#transform-object-definition)
  * [Transform target object definition](https://vercel.com/docs/project-configuration/vercel-json#transform-target-object-definition)
  * [Transform key object definition](https://vercel.com/docs/project-configuration/vercel-json#transform-key-object-definition)
  * [Transform examples](https://vercel.com/docs/project-configuration/vercel-json#transform-examples)
  * [Upgrading legacy routes](https://vercel.com/docs/project-configuration/vercel-json#upgrading-legacy-routes)
  * [Route Parameters](https://vercel.com/docs/project-configuration/vercel-json#route-parameters)
  * [Legacy redirects](https://vercel.com/docs/project-configuration/vercel-json#legacy-redirects)
  * [Legacy SPA Fallback](https://vercel.com/docs/project-configuration/vercel-json#legacy-spa-fallback)
  * [Legacy Headers](https://vercel.com/docs/project-configuration/vercel-json#legacy-headers)
  * [Legacy Pattern Matching](https://vercel.com/docs/project-configuration/vercel-json#legacy-pattern-matching)
  * [Legacy Negative Lookahead](https://vercel.com/docs/project-configuration/vercel-json#legacy-negative-lookahead)
  * [Legacy Case Sensitivity](https://vercel.com/docs/project-configuration/vercel-json#legacy-case-sensitivity)


Copy as MarkdownGive feedbackAsk AI about this page
[Project Configuration](https://vercel.com/docs/project-configuration)
vercel.json
