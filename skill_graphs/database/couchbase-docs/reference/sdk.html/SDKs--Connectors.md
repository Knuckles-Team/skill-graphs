# SDKs & Connectors
Couchbase provides several SDKs to allow applications to access a Couchbase cluster (Capella or self-managed), as well as [Couchbase Lite](https://docs.couchbase.com/home/mobile.html) — an embedded, NoSQL JSON Document Style database for your mobile apps. To exchange data with other platforms, we offer various Big Data Connectors.
```



scala


Copy


val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.reactive.upsert("document-key", json)
    .doOnError(err  => println(s"Error during upsert: ${err}"))
    .doOnNext(_     => println("Success"))
    .subscribe()
```

|  Analytics SDKs SDKs for [Enterprise Analytics](https://docs.couchbase.com/enterprise-analytics/current/intro/intro.html) — Couchbase’s analytical database (RT-OLAP) for real time apps and operational intelligence — are [available](https://docs.couchbase.com/home/analytics-sdk.html) for the Go, Java, Node.js, and Python platforms. SDKs for [Capella Analytics](https://docs.couchbase.com/analytics/intro/intro.html) are similar to the Enterprise Analytics SDKs. They must be used to connect to the current Capella Analytics Service, as it presents a different connection interface, without Enterprise Analytics' load balancer. They are [available](https://docs.couchbase.com/home/columnar-sdk.html) for the Go, Java, Node.js, and Python platforms.
---|---
