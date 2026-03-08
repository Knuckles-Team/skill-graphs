# Develop with Enterprise Analytics
[Enterprise Analytics](https://docs.couchbase.com/enterprise-analytics/current/intro/intro.html) is a self-managed, JSON-native NoSQL analytical database. It serves to unify data from diverse sources, allowing for the execution of complex analytical queries and the extraction of timely insights.


## SDK APIs to work with Enterprise Analytics
Analytics SDKs are developed from the ground-up and while they maintain some syntactic similarities with the [operational SDKs](https://docs.couchbase.com/home/sdk.html), they are purpose built for Enterprise Analytics' real-time analytical use cases. They support streaming APIs to handle large datasets, as well as the common features expected to be present in any modern database SDK — such as connection management and robust error handling.
  * .NET
  * Go
  * Java
  * Node.js
  * Python


[.NET Analytics SDK Docs](https://docs.couchbase.com/dotnet-analytics-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/dotnet-analytics-sdk/current/hello-world/start-using-sdk.html) | | [.NET Analytics API Reference](https://docs.couchbase.com/sdk-api/analytics-dotnet-client)
[Go Analytics SDK Docs](https://docs.couchbase.com/go-analytics-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/go-analytics-sdk/current/hello-world/start-using-sdk.html) |
[Java Analytics SDK Docs](https://docs.couchbase.com/java-analytics-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/java-analytics-sdk/current/hello-world/start-using-sdk.html) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-analytics-java-client/)
[Node.js Analytics SDK Docs](https://docs.couchbase.com/nodejs-analytics-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/nodejs-analytics-sdk/current/hello-world/start-using-sdk.html) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/analytics-nodejs-client)
[Python Analytics SDK Docs](https://docs.couchbase.com/python-analytics-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/python-analytics-sdk/current/hello-world/start-using-sdk.html) | [Python API Reference](https://docs.couchbase.com/sdk-api/analytics-python-client)


### Big Data Connectors
The available options for Enterprise Analytics `DataFrame` and `Dataset` operations with the [Couchbase Spark Connector](https://docs.couchbase.com/spark-connector/current/index.html) can be found on the Spark [DataFrames, Datasets, and SQL](https://docs.couchbase.com/spark-connector/current/spark-sql.html#enterprise-analytics-options) page.
See the [Enterprise Analytics](https://docs.couchbase.com/enterprise-analytics/current/sources/manage-remote.html) docs for information on streaming from Confluent for Kafka.


## Other Analytics Services
Table 1. SDK Compatibility with Analytics Service Analytics solution | Development option
---|---
[Enterprise Analytics](https://docs.couchbase.com/enterprise-analytics/current/intro/intro.html) | [Analytics SDKs](https://docs.couchbase.com/home/analytics-sdk.html)
[Capella Analytics](https://docs.couchbase.com/analytics/intro/intro.html) | [Columnar (Capella Analytics) SDKs](https://docs.couchbase.com/home/columnar-sdk.html)
[CBAS (Couchbase Analytics Service)](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/analytics-service.html) | [Operational SDKs](https://docs.couchbase.com/home/sdk.html)
In addition to the Enterprise Analytics, older Couchbase Analytics services are available — Enterprise Analytics' forerunner, Columnar, remains available as Capella Analytics for the present time.
Traditional, row-based analytics is also available in Couchbase operational clusters — self-managed, or Capella Operational.


### SDK APIs to work with Capella Analytics:
[Capella Analytics](https://docs.couchbase.com/analytics/intro/intro.html) is a standalone, managed cloud offering from Couchbase under the Capella family of products.
Capella Analytics SDKs, formerly known as Columnar SDKs, are similar to the Enterprise Analytics SDKs. They must be used to connect to the current Capella Analytics Service, as it presents a different connection interface, without Enterprise Analytics' load balancer.
  * Go
  * Java
  * Node.js
  * Python


[Go Columnar SDK Docs](https://docs.couchbase.com/go-columnar-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/go-columnar-sdk/current/hello-world/start-using-sdk.html) |
[Java Columnar SDK Docs](https://docs.couchbase.com/java-columnar-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/java-columnar-sdk/current/hello-world/start-using-sdk.html) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client)
[Node.js Columnar SDK Docs](https://docs.couchbase.com/nodejs-columnar-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/nodejs-columnar-sdk/current/hello-world/start-using-sdk.html) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/columnar-nodejs-client)
[Python Columnar SDK Docs](https://docs.couchbase.com/python-columnar-sdk/current/hello-world/overview.html) | [Quickstart](https://docs.couchbase.com/python-columnar-sdk/current/hello-world/start-using-sdk.html) | [Python API Reference](https://docs.couchbase.com/sdk-api/columnar-python-client)


### Row-Based Couchbase Analytics
[CBAS (Couchbase Analytics Service)](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/analytics-service.html) is our classic OLAP available as part of self-managed Couchbase Server and Capella Operational. Use the [operational SDKs](https://docs.couchbase.com/home/sdk.html) to develop for this service.
Output
Show chat.
![](https://bat.bing.com/action/0?ti=4056036&tm=gtm002&Ver=2&mid=b04525b8-086d-4929-b136-f91e7e2a917e&bo=1&sid=ff23eec01b3111f19bec2b1995e08508&vid=ff2431e01b3111f1934fafb7fade9894&vids=0&msclkid=N&uach=pv%3D10.0&pi=2083220816&lg=en-US&sw=1080&sh=600&sc=24&tl=Develop%20with%20Enterprise%20Analytics%20%7C%20Couchbase%20Docs&p=https%3A%2F%2Fdocs.couchbase.com%2Fhome%2Fanalytics-sdk.html&r=&evt=pageLoad&sv=2&cdb=AQET&rn=380340)
