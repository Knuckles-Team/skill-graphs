##  [`config.json` supported properties](https://vercel.com/docs/build-output-api/configuration#config.json-supported-properties)[](https://vercel.com/docs/build-output-api/configuration#config.json-supported-properties)
###  [version](https://vercel.com/docs/build-output-api/configuration#version)[](https://vercel.com/docs/build-output-api/configuration#version)
`
.vercel/output/config.json
`


The `version` property indicates which version of the Build Output API has been implemented. The version described in this document is version `3`.
####  [`version` example](https://vercel.com/docs/build-output-api/configuration#version-example)[](https://vercel.com/docs/build-output-api/configuration#version-example)
```
  "version": 3
```

###  [routes](https://vercel.com/docs/build-output-api/configuration#routes)[](https://vercel.com/docs/build-output-api/configuration#routes)
`
.vercel/output/config.json
`



The `routes` property describes the routing rules that will be applied to the Deployment. It uses the same syntax as the [`routes` property of the `vercel.json` file](https://vercel.com/docs/project-configuration#routes).
Routes may be used to point certain URL paths to others on your Deployment, attach response headers to paths, and various other routing-related use-cases.
```
type Route = Source | Handler;
```

####  [`Source` route](https://vercel.com/docs/build-output-api/configuration#source-route)[](https://vercel.com/docs/build-output-api/configuration#source-route)
```
type Source = {
  src: string;
  dest?: string;
  headers?: Record<string, string>;
  methods?: string[];
  continue?: boolean;
  caseSensitive?: boolean;
  check?: boolean;
  status?: number;
  has?: HasField;
  missing?: HasField;
  locale?: Locale;
  middlewareRawSrc?: string[];
  middlewarePath?: string;
  mitigate?: Mitigate;
  transforms?: Transform[];
};
```

Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
src | [String](https://vercel.com/docs/rest-api/reference#types) | Yes | A PCRE-compatible regular expression that matches each incoming pathname (excluding querystring).
dest | [String](https://vercel.com/docs/rest-api/reference#types) | No | A destination pathname or full URL, including querystring, with the ability to embed capture groups as $1, $2, or named capture value $name.
headers | [Map](https://vercel.com/docs/rest-api/reference#types) | No | A set of headers to apply for responses.
methods | [String[]](https://vercel.com/docs/rest-api/reference#types) | No | A set of HTTP method types. If no method is provided, requests with any HTTP method will be a candidate for the route.
continue | [Boolean](https://vercel.com/docs/rest-api/reference#types) | No | A boolean to change matching behavior. If true, routing will continue even when the src is matched.
caseSensitive | [Boolean](https://vercel.com/docs/rest-api/reference#types) | No | Specifies whether or not the route `src` should match with case sensitivity.
check | [Boolean](https://vercel.com/docs/rest-api/reference#types) | No | If `true`, the route triggers `handle: 'filesystem'` and `handle: 'rewrite'`
status | [Number](https://vercel.com/docs/rest-api/reference#types) | No | A status code to respond with. Can be used in tandem with Location: header to implement redirects.
has | HasField | No | Conditions of the HTTP request that must exist to apply the route.
missing | HasField | No | Conditions of the HTTP request that must NOT exist to match the route.
locale | Locale | No | Conditions of the Locale of the requester that will redirect the browser to different routes.
middlewareRawSrc | [String[]](https://vercel.com/docs/rest-api/reference#types) | No | A list containing the original routes used to generate the `middlewarePath`.
middlewarePath | [String](https://vercel.com/docs/rest-api/reference#types) | No | Path to an Edge Runtime function that should be invoked as middleware.
mitigate | Mitigate | No | A mitigation action to apply to the route.
transforms | Transform[] | No | A list of transforms to apply to the route.
###### Source route: `MatchableValue`
```
type MatchableValue = {
  eq?: string | number;
  neq?: string;
  inc?: string[];
  ninc?: string[];
  pre?: string;
  suf?: string;
  re?: string;
  gt?: number;
  gte?: number;
  lt?: number;
  lte?: number;
};
```

Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
eq |  [String](https://vercel.com/docs/rest-api/reference#types) | [Number](https://vercel.com/docs/rest-api/reference#types) | No | Value must equal this exact value.
neq | [String](https://vercel.com/docs/rest-api/reference#types) | No | Value must not equal this value.
inc | [String[]](https://vercel.com/docs/rest-api/reference#types) | No | Value must be included in this array.
ninc | [String[]](https://vercel.com/docs/rest-api/reference#types) | No | Value must not be included in this array.
pre | [String](https://vercel.com/docs/rest-api/reference#types) | No | Value must start with this prefix.
suf | [String](https://vercel.com/docs/rest-api/reference#types) | No | Value must end with this suffix.
re | [String](https://vercel.com/docs/rest-api/reference#types) | No | Value must match this regular expression.
gt | [Number](https://vercel.com/docs/rest-api/reference#types) | No | Value must be greater than this number.
gte | [Number](https://vercel.com/docs/rest-api/reference#types) | No | Value must be greater than or equal to this number.
lt | [Number](https://vercel.com/docs/rest-api/reference#types) | No | Value must be less than this number.
lte | [Number](https://vercel.com/docs/rest-api/reference#types) | No | Value must be less than or equal to this number.
###### Source route: `HasField`
```
type HasField = Array<
  | { type: 'host'; value: string | MatchableValue }
  | {
      type: 'header' | 'cookie' | 'query';
      key: string;
      value?: string | MatchableValue;
    }
>;
```

Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
type | "host" | "header" | "cookie" | "query" | Yes | Determines the HasField type.
key | [String](https://vercel.com/docs/rest-api/reference#types) | No* | Required for header, cookie, and query types. The key to match against.
value |  [String](https://vercel.com/docs/rest-api/reference#types) | MatchableValue | No | The value to match against using string or MatchableValue conditions.
###### Source route: `Locale`
```
type Locale = {
  redirect?: Record<string, string>;
  cookie?: string;
};
```

Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
redirect | [Map](https://vercel.com/docs/rest-api/reference#types) | Yes | An object of keys that represent locales to check for (`en`, `fr`, etc.) that map to routes to redirect to (`/`, `/fr`, etc.).
cookie | [String](https://vercel.com/docs/rest-api/reference#types) | No | Cookie name that can override the Accept-Language header for determining the current locale.
###### Source route: `Mitigate`
```
type Mitigate = {
  action: 'challenge' | 'deny';
};
```

Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
action | "challenge" | "deny" | Yes | The action to take when the route is matched.
###### Source route: `Transform`
```
type Transform = {
  type: 'request.headers' | 'request.query' | 'response.headers';
  op: 'append' | 'set' | 'delete';
  target: {
    key: string | Omit<MatchableValue, 're'>; // re is not supported for transforms
  };
  args?: string | string[];
};
```

Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
type | "request.headers" | "response.headers" | "request.query" | Yes | The type of transform to apply.
op | "append" | "set" | "delete" | Yes | The operation to perform on the target.
target | `{ key: string | Omit<MatchableValue, 're'> }` | Yes | The target of the transform. Regular expression matching is not supported.
args |  [String](https://vercel.com/docs/rest-api/reference#types) | [String[]](https://vercel.com/docs/rest-api/reference#types) | No | The arguments to pass to the transform.
####  [Handler route](https://vercel.com/docs/build-output-api/configuration#handler-route)[](https://vercel.com/docs/build-output-api/configuration#handler-route)
The routing system has multiple phases. The `handle` value indicates the start of a phase. All following routes are only checked in that phase.
```
type HandleValue =
  | 'rewrite'
  | 'filesystem' // check matches after the filesystem misses
  | 'resource'
  | 'miss' // check matches after every filesystem miss
  | 'hit'
  | 'error'; //  check matches after error (500, 404, etc.)

type Handler = {
  handle: HandleValue;
  src?: string;
  dest?: string;
  status?: number;
};
```

Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
handle | HandleValue | Yes | The phase of routing when all subsequent routes should apply.
src | [String](https://vercel.com/docs/rest-api/reference#types) | No | A PCRE-compatible regular expression that matches each incoming pathname (excluding querystring).
dest | [String](https://vercel.com/docs/rest-api/reference#types) | No | A destination pathname or full URL, including querystring, with the ability to embed capture groups as $1, $2.
status | [String](https://vercel.com/docs/rest-api/reference#types) | No | A status code to respond with. Can be used in tandem with `Location:` header to implement redirects.
####  [Routing rule example](https://vercel.com/docs/build-output-api/configuration#routing-rule-example)[](https://vercel.com/docs/build-output-api/configuration#routing-rule-example)
The following example shows a routing rule that will cause the `/redirect` path to perform an HTTP redirect to an external URL:
```
  "routes": [
    {
      "src": "/redirect",
      "status": 308,
      "headers": { "Location": "https://example.com/" }
    }
  ]
```

###  [images](https://vercel.com/docs/build-output-api/configuration#images)[](https://vercel.com/docs/build-output-api/configuration#images)
`
.vercel/output/config.json
`



The `images` property defines the behavior of Vercel's native [Image Optimization API](https://vercel.com/docs/image-optimization), which allows on-demand optimization of images at runtime.
```
type ImageFormat = 'image/avif' | 'image/webp';

type RemotePattern = {
  protocol?: 'http' | 'https';
  hostname: string;
  port?: string;
  pathname?: string;
  search?: string;
};

type LocalPattern = {
  pathname?: string;
  search?: string;
};

type ImagesConfig = {
  sizes: number[];
  domains: string[];
  remotePatterns?: RemotePattern[];
  localPatterns?: LocalPattern[];
  qualities?: number[];
  minimumCacheTTL?: number; // seconds
  formats?: ImageFormat[];
  dangerouslyAllowSVG?: boolean;
  contentSecurityPolicy?: string;
  contentDispositionType?: string;
};
```

Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
sizes | [Number[]](https://vercel.com/docs/rest-api/reference#types) | Yes | Allowed image widths.
domains | [String[]](https://vercel.com/docs/rest-api/reference#types) | Yes | Allowed external domains that can use Image Optimization. Leave empty for only allowing the deployment domain to use Image Optimization.
remotePatterns | RemotePattern[] | No | Allowed external patterns that can use Image Optimization. Similar to `domains` but provides more control with RegExp.
localPatterns | LocalPattern[] | No | Allowed local patterns that can use Image Optimization. Leave undefined to allow all or use empty array to deny all.
qualities | [Number[]](https://vercel.com/docs/rest-api/reference#types) | No | Allowed image qualities. Leave undefined to allow all possibilities, 1 to 100.
minimumCacheTTL | [Number](https://vercel.com/docs/rest-api/reference#types) | No | Cache duration (in seconds) for the optimized images.
formats | ImageFormat[] | No | Supported output image formats
dangerouslyAllowSVG | [Boolean](https://vercel.com/docs/rest-api/reference#types) | No | Allow SVG input image URLs. This is disabled by default for security purposes.
contentSecurityPolicy | [String](https://vercel.com/docs/rest-api/reference#types) | No | Change the
contentDispositionType | [String](https://vercel.com/docs/rest-api/reference#types) | No | Specifies the value of the `"Content-Disposition"` response header.
####  [`images` example](https://vercel.com/docs/build-output-api/configuration#images-example)[](https://vercel.com/docs/build-output-api/configuration#images-example)
The following example shows an image optimization configuration that specifies allowed image size dimensions, external domains, caching lifetime and file formats:
```
  "images": {
    "sizes": [640, 750, 828, 1080, 1200],
    "domains": [],
    "minimumCacheTTL": 60,
    "formats": ["image/avif", "image/webp"],
    "qualities": [25, 50, 75],
    "localPatterns": [{
      "pathname": "^/assets/.*$",
      "search": ""
    }]
    "remotePatterns": [{
      "protocol": "https",
      "hostname": "^via\\.placeholder\\.com$",
      "port": "",
      "pathname": "^/1280x640/.*$",
      "search": "?v=1"
    }]
  }
```

####  [API](https://vercel.com/docs/build-output-api/configuration#api)[](https://vercel.com/docs/build-output-api/configuration#api)
When the `images` property is defined, the Image Optimization API will be available by visiting the `/_vercel/image` path. When the `images` property is undefined, visiting the `/_vercel/image` path will respond with 404 Not Found.
The API accepts the following query string parameters:
Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Example | Description
---|---|---|---|---
url | [String](https://vercel.com/docs/rest-api/reference#types) | Yes | `/assets/me.png` | The URL of the source image that should be optimized. Absolute URLs must match a pattern defined in the `remotePatterns` configuration.
w | [Integer](https://vercel.com/docs/rest-api/reference#types) | Yes | `200` | The width (in pixels) that the source image should be resized to. Must match a value defined in the `sizes` configuration.
q | [Integer](https://vercel.com/docs/rest-api/reference#types) | Yes | `75` | The quality that the source image should be reduced to. Must be between 1 (lowest quality) to 100 (highest quality).
###  [wildcard](https://vercel.com/docs/build-output-api/configuration#wildcard)[](https://vercel.com/docs/build-output-api/configuration#wildcard)
`
.vercel/output/config.json
`



The `wildcard` property relates to Vercel's Internationalization feature. The way it works is the domain names listed in this array are mapped to the `$wildcard` routing variable, which can be referenced by the [`routes` configuration](https://vercel.com/docs/build-output-api/configuration#routes).
Each of the domain names specified in the `wildcard` configuration will need to be assigned as [Production Domains in the Project Settings](https://vercel.com/docs/domains).
```
type WildCard = {
  domain: string;
  value: string;
};

type WildcardConfig = Array<WildCard>;
```

####  [`wildcard` supported properties](https://vercel.com/docs/build-output-api/configuration#wildcard-supported-properties)[](https://vercel.com/docs/build-output-api/configuration#wildcard-supported-properties)
Objects contained within the `wildcard` configuration support the following properties:
Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
domain | [String](https://vercel.com/docs/rest-api/reference#types) | Yes | The domain name to match for this wildcard configuration.
value | [String](https://vercel.com/docs/rest-api/reference#types) | Yes | The value of the `$wildcard` match that will be available for `routes` to utilize.
####  [`wildcard` example](https://vercel.com/docs/build-output-api/configuration#wildcard-example)[](https://vercel.com/docs/build-output-api/configuration#wildcard-example)
The following example shows a wildcard configuration where the matching domain name will be served the localized version of the blog post HTML file:
```
  "wildcard": [
    {
      "domain": "example.com",
      "value": "en-US"
    },
    {
      "domain": "example.nl",
      "value": "nl-NL"
    },
    {
      "domain": "example.fr",
      "value": "fr"
    }
  ],
  "routes": [
    { "src": "/blog", "dest": "/blog.$wildcard.html" }
  ]
```

###  [overrides](https://vercel.com/docs/build-output-api/configuration#overrides)[](https://vercel.com/docs/build-output-api/configuration#overrides)
`
.vercel/output/config.json
`



The `overrides` property allows for overriding the output of one or more [static files](https://vercel.com/docs/build-output-api/v3/primitives#static-files) contained within the `.vercel/output/static` directory.
The main use-cases are to override the `Content-Type` header that will be served for a static file, and/or to serve a static file in the Vercel Deployment from a different URL path than how it is stored on the file system.
```
type Override = {
  path?: string;
  contentType?: string;
};

type OverrideConfig = Record<string, Override>;
```

####  [`overrides` supported properties](https://vercel.com/docs/build-output-api/configuration#overrides-supported-properties)[](https://vercel.com/docs/build-output-api/configuration#overrides-supported-properties)
Objects contained within the `overrides` configuration support the following properties:
Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
path | [String](https://vercel.com/docs/rest-api/reference#types) | No | The URL path where the static file will be accessible from.
contentType | [String](https://vercel.com/docs/rest-api/reference#types) | No | The value of the `Content-Type` HTTP response header that will be served with the static file.
####  [`overrides` example](https://vercel.com/docs/build-output-api/configuration#overrides-example)[](https://vercel.com/docs/build-output-api/configuration#overrides-example)
The following example shows an override configuration where an HTML file can be accessed without the `.html` file extension:
```
  "overrides": {
    "blog.html": {
      "path": "blog"
    }
  }
```

###  [cache](https://vercel.com/docs/build-output-api/configuration#cache)[](https://vercel.com/docs/build-output-api/configuration#cache)
`
.vercel/output/config.json
`


The `cache` property is an array of file paths and/or glob patterns that should be re-populated within the build sandbox upon subsequent Deployments.
Note that this property is only relevant when Vercel is building a Project from source code, meaning it is not relevant when building locally or when creating a Deployment from "prebuilt" build artifacts.
```
type Cache = string[];
```

####  [`cache` example](https://vercel.com/docs/build-output-api/configuration#cache-example)[](https://vercel.com/docs/build-output-api/configuration#cache-example)
```
  "cache": [
    ".cache/**",
    "node_modules/**"
  ]
```

###  [framework](https://vercel.com/docs/build-output-api/configuration#framework)[](https://vercel.com/docs/build-output-api/configuration#framework)
`
.vercel/output/config.json
`


The optional `framework` property is an object describing the framework of the built outputs.
This value is used for display purposes only.
```
type Framework = {
  version: string;
};
```

####  [`framework` example](https://vercel.com/docs/build-output-api/configuration#framework-example)[](https://vercel.com/docs/build-output-api/configuration#framework-example)
```
  "framework": {
    "version": "1.2.3"
  }
```

###  [crons](https://vercel.com/docs/build-output-api/configuration#crons)[](https://vercel.com/docs/build-output-api/configuration#crons)
`
.vercel/output/config.json
`


The optional `crons` property is an object describing the [cron jobs](https://vercel.com/docs/cron-jobs) for the production deployment of a project.
```
type Cron = {
  path: string;
  schedule: string;
};

type CronsConfig = Cron[];
```

####  [`crons` example](https://vercel.com/docs/build-output-api/configuration#crons-example)[](https://vercel.com/docs/build-output-api/configuration#crons-example)
```
  "crons": [{
    "path": "/api/cron",
    "schedule": "0 0 * * *"
  }]
```
