##  [Full `config.json` example](https://vercel.com/docs/build-output-api/configuration#full-config.json-example)[](https://vercel.com/docs/build-output-api/configuration#full-config.json-example)
```
{
  "version": 3,
  "routes": [
    {
      "src": "/redirect",
      "status": 308,
      "headers": { "Location": "https://example.com/" }
    },
    {
      "src": "/blog",
      "dest": "/blog.$wildcard.html"
    }
  ],
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
    "remotePatterns": [
      {
        "protocol": "https",
        "hostname": "^via\\.placeholder\\.com$",
        "port": "",
        "pathname": "^/1280x640/.*$",
        "search": "?v=1"
      }
    ]
  },
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
  "overrides": {
    "blog.html": {
      "path": "blog"
    }
  },
  "cache": [".cache/**", "node_modules/**"],
  "framework": {
    "version": "1.2.3"
  },
  "crons": [
    {
      "path": "/api/cron",
      "schedule": "* * * * *"
    }
  ]
}
```

* * *
[ Previous Build Output API ](https://vercel.com/docs/build-output-api)[ Next Features ](https://vercel.com/docs/build-output-api/features)
Was this helpful?
Send
On this page
  * [config.json supported properties](https://vercel.com/docs/build-output-api/configuration#config.json-supported-properties)
  * [version](https://vercel.com/docs/build-output-api/configuration#version)
  * [version example](https://vercel.com/docs/build-output-api/configuration#version-example)
  * [routes](https://vercel.com/docs/build-output-api/configuration#routes)
  * [Source route](https://vercel.com/docs/build-output-api/configuration#source-route)
  * Source route: MatchableValue
  * Source route: HasField
  * Source route: Locale
  * Source route: Mitigate
  * Source route: Transform
  * [Handler route](https://vercel.com/docs/build-output-api/configuration#handler-route)
  * [Routing rule example](https://vercel.com/docs/build-output-api/configuration#routing-rule-example)
  * [images](https://vercel.com/docs/build-output-api/configuration#images)
  * [images example](https://vercel.com/docs/build-output-api/configuration#images-example)
  * [API](https://vercel.com/docs/build-output-api/configuration#api)
  * [wildcard](https://vercel.com/docs/build-output-api/configuration#wildcard)
  * [wildcard supported properties](https://vercel.com/docs/build-output-api/configuration#wildcard-supported-properties)
  * [wildcard example](https://vercel.com/docs/build-output-api/configuration#wildcard-example)
  * [overrides](https://vercel.com/docs/build-output-api/configuration#overrides)
  * [overrides supported properties](https://vercel.com/docs/build-output-api/configuration#overrides-supported-properties)
  * [overrides example](https://vercel.com/docs/build-output-api/configuration#overrides-example)
  * [cache](https://vercel.com/docs/build-output-api/configuration#cache)
  * [cache example](https://vercel.com/docs/build-output-api/configuration#cache-example)
  * [framework](https://vercel.com/docs/build-output-api/configuration#framework)
  * [framework example](https://vercel.com/docs/build-output-api/configuration#framework-example)
  * [crons](https://vercel.com/docs/build-output-api/configuration#crons)
  * [crons example](https://vercel.com/docs/build-output-api/configuration#crons-example)
  * [Full config.json example](https://vercel.com/docs/build-output-api/configuration#full-config.json-example)


Copy as MarkdownGive feedbackAsk AI about this page
