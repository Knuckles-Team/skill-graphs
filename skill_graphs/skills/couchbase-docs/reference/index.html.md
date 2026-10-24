* [ ![Couchbase](https://docs.couchbase.com/_/img/couchbase-logo.svg) ](https://www.couchbase.com)
  * [ ![Couchbase Documentation](https://docs.couchbase.com/_/img/cb-documentation.svg) ![Couchbase Documentation](https://docs.couchbase.com/_/img/cb-docs-hover.svg) ](https://docs.couchbase.com/home/index.html)


  * [ ](https://docs.couchbase.com/home/index.html)
  * [ Server ](https://docs.couchbase.com/home/server.html)
  * [ Mobile / Edge ](https://docs.couchbase.com/home/mobile.html)
  * [ Capella ](https://docs.couchbase.com/home/cloud.html)
  * [ Kubernetes Operator ](https://docs.couchbase.com/operator/current/overview.html)
  * [ Develop ](https://docs.couchbase.com/home/developer.html)
    * [ Operational SDKs ](https://docs.couchbase.com/home/sdk.html)
    * [ Analytics SDKs ](https://docs.couchbase.com/home/analytics-sdk.html)


[Prev](https://docs.couchbase.com/home/index.html)No results[Next](https://docs.couchbase.com/home/index.html)
Search by
[ Downloads  ](https://www.couchbase.com/downloads) [ Try Free  ](https://cloud.couchbase.com/sign-up)
# Couchbase Documentation
_Couchbase is the modern database for enterprise applications._
Couchbase is a distributed document database with a powerful search engine and in-built operational and analytical capabilities. It brings the power of NoSQL to the edge and provides fast, efficient bidirectional synchronization of data between the edge and the cloud.
Find the documentation, samples, and references to help you use Couchbase and build applications.
```
// List the schedule of flights from Boston
// to San Francisco on JETBLUE

SELECT DISTINCT airline.name, route.schedule
FROM `travel-sample`.inventory.route
  JOIN `travel-sample`.inventory.airline
  ON KEYS route.airlineid
WHERE route.sourceairport = "BOS"
AND route.destinationairport = "SFO"
AND airline.callsign = "JETBLUE";
```

## Get Started
Couchbase Capella (DBaaS)
Explore Couchbase Capella, our fully-managed database as a service offering. Take the complexity out of deploying, managing, scaling, and securing Couchbase in the public cloud. Store, query, and analyze any amount of data — and let us handle more of the administration — all in a few clicks.
[Couchbase Capella](https://docs.couchbase.com/home/cloud.html)


Capella Analytics (RT-OLAP)
Capella Analytics is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Capella Analytics is a standalone, cloud-only offering from Couchbase under the Capella family of products.
[Capella Analytics](https://docs.couchbase.com/analytics/intro/intro.html)
Couchbase Server
Explore Couchbase Server, a modern, distributed document database with all the desired capabilities of a relational database and more. It exposes a scale-out, key-value store with managed cache for sub-millisecond data operations, purpose-built indexers for efficient queries, and a powerful query engine for executing SQL-like queries.
[Couchbase Server](https://docs.couchbase.com/home/server.html)


Enterprise Analytics (RT-OLAP)
Enterprise Analytics is a self-managed analytical database (RT-OLAP) for real time apps and operational intelligence.
[Enterprise Analytics](https://docs.couchbase.com/enterprise-analytics/current/intro/intro.html)
Couchbase Mobile
_Couchbase Mobile_ brings the power of NoSQL to the edge. The combination of _Sync Gateway_ and _Couchbase Lite_ coupled with the power of _Couchbase Server_ provides fast, efficient bidirectional synchronization of data between the edge and the cloud. Enabling you to deploy your offline-first mobile and embedded applications with greater agility on premises or in any cloud.
[Couchbase Lite](https://docs.couchbase.com/couchbase-lite/current/index.html) | [Sync Gateway](https://docs.couchbase.com/sync-gateway/current/introduction.html) | [Couchbase Edge Server](https://docs.couchbase.com/couchbase-edge-server/current/introduction/intro.html)


Capella AI Services
Capella AI Services is a fully managed set of tools that help you build, deploy, and scale your agentic and retrieval-augmented generation (RAG) AI applications. These tools integrate seamlessly with the Couchbase Capella cloud platform, enabling you to develop your AI applications on the same platform as your data.
[Capella AI Services](https://docs.couchbase.com/ai/get-started/intro.html)
## Developer Tools
SDK and Connectors
Couchbase SDKs allow applications to access a Couchbase cluster and the big data Connectors enable data exchange with other platforms.
[Developer Docs](https://docs.couchbase.com/home/developer.html) | [Operational SDKs](https://docs.couchbase.com/home/sdk.html) | [Enterprise Analytics SDKs](https://docs.couchbase.com/home/analytics-sdk.html) | [Capella Analytics SDKs](https://docs.couchbase.com/home/columnar-sdk.html)
CLI and REST APIs
Use the command-line interface (CLI) tools and REST API to manage and monitor your Couchbase deployment.
[Couchbase CLI](https://docs.couchbase.com/server/current/cli/cli-intro.html) | [REST API](https://docs.couchbase.com/server/current/rest-api/rest-intro.html)
Couchbase Shell
A modern shell to interact with Couchbase Server and Capella, now available.
## More Developer Resources
Developer Portal
Explore a variety of resources - sample apps, videos, blogs, and more, to build applications using Couchbase.
[Developer Portal](https://developer.couchbase.com) [Developer Tutorials](https://developer.couchbase.com/tutorials)
Academy
Explore extensive hands-on learning experiences through free, online courses or under the guidance of an in-person instructor.
[Academy](https://learn.couchbase.com/store)
Community
With open source roots, Couchbase has a rich history of collaboration and community. Connect with our developer community and get involved.
[Community](https://forums.couchbase.com/)
## Explore Products and Services
Cloud | Server | SDK and Connectors | Mobile
---|---|---|---
[Couchbase Capella](https://docs.couchbase.com/home/cloud.html) [Capella Analytics](https://docs.couchbase.com/analytics/intro/intro.html) |  [Couchbase Server](https://docs.couchbase.com/home/server.html) [Enterprise Analytics](https://docs.couchbase.com/enterprise-analytics/current/intro/intro.html) [Couchbase Autonomous Operator](https://docs.couchbase.com/operator/current/overview.html) [Couchbase Service Broker](https://docs.couchbase.com/home/index.html#service-broker::index.adoc) [Couchbase Monitoring and Observability Stack](https://docs.couchbase.com/cmos/current/index.html) |  [Couchbase Java SDK](https://docs.couchbase.com/java-sdk/current/hello-world/overview.html) [Couchbase Scala SDK](https://docs.couchbase.com/scala-sdk/current/hello-world/overview.html) [Couchbase .NET SDK](https://docs.couchbase.com/dotnet-sdk/current/hello-world/overview.html) [Couchbase C++ SDK](https://docs.couchbase.com/cxx-sdk/current/hello-world/overview.html) [Couchbase C SDK](https://docs.couchbase.com/c-sdk/current/hello-world/overview.html) [Couchbase Node.js SDK](https://docs.couchbase.com/nodejs-sdk/current/hello-world/overview.html) [Couchbase PHP SDK](https://docs.couchbase.com/php-sdk/current/hello-world/overview.html) [Couchbase Python SDK](https://docs.couchbase.com/python-sdk/current/hello-world/overview.html) [Couchbase Ruby SDK](https://docs.couchbase.com/ruby-sdk/current/hello-world/overview.html) [Couchbase Go SDK](https://docs.couchbase.com/go-sdk/current/hello-world/overview.html) [Couchbase Kotlin SDK](https://docs.couchbase.com/kotlin-sdk/current/hello-world/overview.html) [Couchbase Elasticsearch Connector](https://docs.couchbase.com/elasticsearch-connector/current/getting-started.html) [Couchbase Kafka Connector](https://docs.couchbase.com/kafka-connector/current/quickstart.html) [Couchbase Spark Connector](https://docs.couchbase.com/spark-connector/current/getting-started.html) [Go Analytics SDK](https://docs.couchbase.com/go-analytics-sdk/current/hello-world/overview.html) [Java Analytics SDK](https://docs.couchbase.com/java-analytics-sdk/current/hello-world/overview.html) [Node.js Analytics SDK](https://docs.couchbase.com/nodejs-analytics-sdk/current/hello-world/overview.html) [Python Analytics SDK](https://docs.couchbase.com/python-analytics-sdk/current/hello-world/overview.html) [Go Columnar SDK](https://docs.couchbase.com/go-columnar-sdk/current/hello-world/overview.html) [Java Columnar SDK](https://docs.couchbase.com/java-columnar-sdk/current/hello-world/overview.html) [Node.js Columnar SDK](https://docs.couchbase.com/nodejs-columnar-sdk/current/hello-world/overview.html) [Python Columnar SDK](https://docs.couchbase.com/python-columnar-sdk/current/hello-world/overview.html) |  [Couchbase Lite JavaScript](https://docs.couchbase.com/home/index.html#couchbase-lite:javascript:quickstart.adoc) [Couchbase Lite C#](https://docs.couchbase.com/couchbase-lite/current/csharp/quickstart.html) [Couchbase Lite Java](https://docs.couchbase.com/couchbase-lite/current/java/quickstart.html) [Couchbase Lite Java Android](https://docs.couchbase.com/couchbase-lite/current/android/quickstart.html) [Couchbase Lite Swift](https://docs.couchbase.com/couchbase-lite/current/swift/quickstart.html) [Couchbase Lite Objective-C](https://docs.couchbase.com/couchbase-lite/current/objc/quickstart.html) [Couchbase Sync Gateway](https://docs.couchbase.com/sync-gateway/current/index.html)
## Feedback and Contributions
Provide Feedback
Provide feedback, and get help with any problem you may encounter.
[Provide Feedback](https://docs.couchbase.com/server/current/introduction/contact-couchbase.html)
Contact Support
Couchbase Support provides online support for customers of Enterprise Edition who have a support contract.
[Contact Couchbase](https://docs.couchbase.com/server/current/introduction/contact-couchbase.html)
Contribute
You can submit simple changes, such as typo fixes and minor clarifications directly on GitHub. Contributions are greatly encouraged.
[Contribute to the Documentation](https://docs.couchbase.com/home/contribute/index.html)
[ ![Couchbase](https://docs.couchbase.com/_/img/couchbase-logo.svg) ](https://www.couchbase.com)
  * [Documentation](https://docs.couchbase.com)
  * [Forums](https://forums.couchbase.com)
  * [Support](https://support.couchbase.com)


  * [Developer Portal](https://developer.couchbase.com)
  * [Blog](https://blog.couchbase.com)
  * [Resources](https://www.couchbase.com/resources)


  * [Get Started](https://www.couchbase.com/get-started-developing-nosql)
  * [Downloads](https://www.couchbase.com/downloads)
  * [Training](https://learn.couchbase.com/store?utf8=%E2%9C%93&ss=1&ct=78327&commit=Filter)


© 2026 Couchbase and the Couchbase logo are registered trademarks of Couchbase, Inc. All third party trademarks (including logos and icons) referenced by Couchbase, Inc. remain the property of their respective owners.
[Terms of Use](https://www.couchbase.com/terms-of-use) [Privacy Policy](https://www.couchbase.com/privacy-policy) [Cookie Policy](https://www.couchbase.com/cookie-policy) [Support Policy](https://www.couchbase.com/support-policy) [Marketing Preference Center](https://info.couchbase.com/unsubscribe-or-manage-preferences.html)
Output
Show chat.
We use cookies to offer you a better browsing experience, analyze site traffic, personalize content, and serve targeted advertisements. Read about how we use cookies and how you can control them by clicking "Cookie Settings." By clicking “Accept All Cookies”, you consent to our use of cookies.
Cookies Settings Accept All Cookies
![](https://bat.bing.com/action/0?ti=4056036&tm=gtm002&Ver=2&mid=3e49e1af-2783-4351-abcd-683b8e7cfb10&bo=1&sid=ff23eec01b3111f19bec2b1995e08508&vid=ff2431e01b3111f1934fafb7fade9894&vids=1&msclkid=N&uach=pv%3D10.0&pi=2083220816&lg=en-US&sw=1080&sh=600&sc=24&tl=Couchbase%20Documentation%20%7C%20Couchbase%20Docs&p=https%3A%2F%2Fdocs.couchbase.com%2Fhome%2Findex.html&r=&lt=4257&evt=pageLoad&sv=2&cdb=AQET&rn=74831)
