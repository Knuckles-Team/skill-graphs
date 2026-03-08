### Getting Started
[Overview](https://qdrant.tech/documentation/overview/)
  * [What is Qdrant?](https://qdrant.tech/documentation/overview/what-is-qdrant/)
  * [Understanding Vector Search in Qdrant](https://qdrant.tech/documentation/overview/vector-search/)


[Qdrant Quickstart](https://qdrant.tech/documentation/quickstart/)
[API & SDKs](https://qdrant.tech/documentation/interfaces/)
[Qdrant Web UI](https://qdrant.tech/documentation/web-ui/)
### User Manual
[Concepts](https://qdrant.tech/documentation/concepts/)
  * [Collections](https://qdrant.tech/documentation/concepts/collections/)
  * [Points](https://qdrant.tech/documentation/concepts/points/)
  * [Vectors](https://qdrant.tech/documentation/concepts/vectors/)
  * [Payload](https://qdrant.tech/documentation/concepts/payload/)
  * [Search](https://qdrant.tech/documentation/concepts/search/)
  * [Search Relevance](https://qdrant.tech/documentation/concepts/search-relevance/)
  * [Explore](https://qdrant.tech/documentation/concepts/explore/)
  * [Hybrid Queries](https://qdrant.tech/documentation/concepts/hybrid-queries/)
  * [Filtering](https://qdrant.tech/documentation/concepts/filtering/)
  * [Inference](https://qdrant.tech/documentation/concepts/inference/)
  * [Optimizer](https://qdrant.tech/documentation/concepts/optimizer/)
  * [Storage](https://qdrant.tech/documentation/concepts/storage/)
  * [Indexing](https://qdrant.tech/documentation/concepts/indexing/)
  * [Snapshots](https://qdrant.tech/documentation/concepts/snapshots/)

[Guides](https://qdrant.tech/documentation/guides/installation/)
  * [Installation](https://qdrant.tech/documentation/guides/installation/)
  * [Administration](https://qdrant.tech/documentation/guides/administration/)
  * [Running with GPU](https://qdrant.tech/documentation/guides/running-with-gpu/)
  * [Capacity Planning](https://qdrant.tech/documentation/guides/capacity-planning/)
  * [Optimize Performance](https://qdrant.tech/documentation/guides/optimize/)
  * [Low-Latency Search](https://qdrant.tech/documentation/guides/low-latency-search/)
  * [Multitenancy](https://qdrant.tech/documentation/guides/multitenancy/)
  * [Distributed Deployment](https://qdrant.tech/documentation/guides/distributed_deployment/)
  * [Quantization](https://qdrant.tech/documentation/guides/quantization/)
  * [Text Search](https://qdrant.tech/documentation/guides/text-search/)
  * [Monitoring & Telemetry](https://qdrant.tech/documentation/guides/monitoring/)
  * [Configuration](https://qdrant.tech/documentation/guides/configuration/)
  * [Security](https://qdrant.tech/documentation/guides/security/)
  * [Usage Statistics](https://qdrant.tech/documentation/guides/usage-statistics/)
  * [Troubleshooting](https://qdrant.tech/documentation/guides/common-errors/)


### Ecosystem
[FastEmbed](https://qdrant.tech/documentation/fastembed/)
  * [Quickstart](https://qdrant.tech/documentation/fastembed/fastembed-quickstart/)
  * [FastEmbed & Qdrant](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/)
  * [Working with miniCOIL](https://qdrant.tech/documentation/fastembed/fastembed-minicoil/)
  * [Working with SPLADE](https://qdrant.tech/documentation/fastembed/fastembed-splade/)
  * [Working with ColBERT](https://qdrant.tech/documentation/fastembed/fastembed-colbert/)
  * [Reranking with FastEmbed](https://qdrant.tech/documentation/fastembed/fastembed-rerankers/)
  * [Multi-Vector Postprocessing](https://qdrant.tech/documentation/fastembed/fastembed-postprocessing/)

[Qdrant Edge](https://qdrant.tech/documentation/edge/)
  * [Quickstart](https://qdrant.tech/documentation/edge/edge-quickstart/)
  * [On-Device Embeddings](https://qdrant.tech/documentation/edge/edge-fastembed-embeddings/)
  * [Data Synchronization Patterns](https://qdrant.tech/documentation/edge/edge-data-synchronization-patterns/)
  * [Synchronize with a Server](https://qdrant.tech/documentation/edge/edge-synchronization-guide/)


### Tutorials
[Overview](https://qdrant.tech/documentation/tutorials-lp-overview/)
[Basics](https://qdrant.tech/documentation/tutorials-basics/)
  * [Semantic Search 101](https://qdrant.tech/documentation/tutorials-basics/search-beginners/)

[Search Engineering](https://qdrant.tech/documentation/tutorials-search-engineering/)
  * [Hybrid Search with Reranking](https://qdrant.tech/documentation/tutorials-search-engineering/reranking-hybrid-search/)
  * [Multivectors and Late Interaction](https://qdrant.tech/documentation/tutorials-search-engineering/using-multivector-representations/)
  * [Relevance Feedback Retrieval in Qdrant](https://qdrant.tech/documentation/tutorials-search-engineering/using-relevance-feedback/)
  * [Semantic Search Basics](https://qdrant.tech/documentation/tutorials-search-engineering/neural-search/)
  * [Semantic Search for Code](https://qdrant.tech/documentation/tutorials-search-engineering/code-search/)
  * [Collaborative Filtering](https://qdrant.tech/documentation/tutorials-search-engineering/collaborative-filtering/)
  * [Hybrid Search with FastEmbed](https://qdrant.tech/documentation/tutorials-search-engineering/hybrid-search-fastembed/)
  * [Multivector Document Retrieval](https://qdrant.tech/documentation/tutorials-search-engineering/pdf-retrieval-at-scale/)
  * [Retrieval Quality Evaluation](https://qdrant.tech/documentation/tutorials-search-engineering/retrieval-quality/)
  * [Static Embeddings](https://qdrant.tech/documentation/tutorials-search-engineering/static-embeddings/)

[Operations & Scale](https://qdrant.tech/documentation/tutorials-operations/)
  * [Snapshots](https://qdrant.tech/documentation/tutorials-operations/create-snapshot/)
  * [Data Migration](https://qdrant.tech/documentation/tutorials-operations/migration/)
  * [Migrate to a New Embedding Model](https://qdrant.tech/documentation/tutorials-operations/embedding-model-migration/)
  * [Large-Scale Search](https://qdrant.tech/documentation/tutorials-operations/large-scale-search/)

[Develop & Implement](https://qdrant.tech/documentation/tutorials-develop/)
  * [Bulk Operations](https://qdrant.tech/documentation/tutorials-develop/bulk-upload/)
  * [Async API](https://qdrant.tech/documentation/tutorials-develop/async-api/)


### Support
[FAQ](https://qdrant.tech/documentation/faq/qdrant-fundamentals/)
  * [Qdrant Fundamentals](https://qdrant.tech/documentation/faq/qdrant-fundamentals/)
  * [Database Optimization](https://qdrant.tech/documentation/faq/database-optimization/)


  * [Documentation](https://qdrant.tech/documentation/)
  * [Guides](https://qdrant.tech/documentation/guides/)
  * Capacity Planning


#  [](https://qdrant.tech/documentation/guides/capacity-planning/#capacity-planning)Capacity Planning
When setting up your cluster, you’ll need to figure out the right balance of **RAM** and **disk storage**. The best setup depends on a few things:
  * How many vectors you have and their dimensions.
  * The amount of payload data you’re using and their indexes.
  * What data you want to store in memory versus on disk.
  * Your cluster’s replication settings.
  * Whether you’re using quantization and how you’ve set it up.


##  [](https://qdrant.tech/documentation/guides/capacity-planning/#calculating-ram-size)Calculating RAM size
You should store frequently accessed data in RAM for faster retrieval. If you want to keep all vectors in memory for optimal performance, you can use this rough formula for estimation:
```
memory_size = number_of_vectors * vector_dimension * 4 bytes * 1.5

```

At the end, we multiply everything by 1.5. This extra 50% accounts for metadata (such as indexes and point versions) and temporary segments created during optimization.
Let’s say you want to store 1 million vectors with 1024 dimensions:
```
memory_size = 1,000,000 * 1024 * 4 bytes * 1.5

```

The memory_size is approximately 6,144,000,000 bytes, or about 5.72 GB.
Depending on the use case, large datasets can benefit from reduced memory requirements via [quantization](https://qdrant.tech/documentation/guides/quantization/).
##  [](https://qdrant.tech/documentation/guides/capacity-planning/#calculating-payload-size)Calculating payload size
This is always different. The size of the payload depends on the [structure and content of your data](https://qdrant.tech/documentation/concepts/payload/#payload-types). For instance:
  * **Text fields** consume space based on length and encoding (e.g. a large chunk of text vs a few words).
  * **Floats** have fixed sizes of 8 bytes for `int64` or `float64`.
  * **Boolean fields** typically consume 1 byte.


Calculating total payload size is similar to vectors. We have to multiply it by 1.5 for back-end indexing processes.
```
total_payload_size = number_of_points * payload_size * 1.5

```

Let’s say you want to store 1 million points with JSON payloads of 5KB:
```
total_payload_size = 1,000,000 * 5KB * 1.5

```

The total_payload_size is approximately 5,000,000 bytes, or about 4.77 GB.
##  [](https://qdrant.tech/documentation/guides/capacity-planning/#choosing-disk-over-ram)Choosing disk over RAM
For optimal performance, you should store only frequently accessed data in RAM. The rest should be offloaded to the disk. For example, extra payload fields that you don’t use for filtering can be stored on disk.
Only [indexed fields](https://qdrant.tech/documentation/concepts/indexing/#payload-index) should be stored in RAM. You can read more about payload storage in the [Storage](https://qdrant.tech/documentation/concepts/storage/#payload-storage) section.
###  [](https://qdrant.tech/documentation/guides/capacity-planning/#storage-focused-configuration)Storage-focused configuration
If your priority is to handle large volumes of vectors with average search latency, it’s recommended to configure [memory-mapped (mmap) storage](https://qdrant.tech/documentation/concepts/storage/#configuring-memmap-storage). In this setup, vectors are stored on disk in memory-mapped files, while only the most frequently accessed vectors are cached in RAM.
The amount of available RAM greatly impacts search performance. As a general rule, if you store half as many vectors in RAM, search latency will roughly double.
Disk speed is also crucial. [Contact us](https://qdrant.tech/documentation/support/) if you have specific requirements for high-volume searches in our Cloud.
###  [](https://qdrant.tech/documentation/guides/capacity-planning/#subgroup-oriented-configuration)Subgroup-oriented configuration
If your use case involves splitting vectors into multiple collections or subgroups based on payload values (e.g., serving searches for multiple users, each with their own subset of vectors), memory-mapped storage is recommended.
In this scenario, only the active subset of vectors will be cached in RAM, allowing for fast searches for the most recent and active users. You can estimate the required memory size as:
```
memory_size = number_of_active_vectors * vector_dimension * 4 bytes * 1.5

```

Please refer to our [multitenancy](https://qdrant.tech/documentation/guides/multiple-partitions/) documentation for more details on partitioning data in a Qdrant.
##  [](https://qdrant.tech/documentation/guides/capacity-planning/#scaling-disk-space-in-qdrant-cloud)Scaling disk space in Qdrant Cloud
Clusters supporting vector search require substantial disk space compared to other search systems. If you’re running low on disk space, you can use the UI at **Scale Up** your cluster.
When running low on disk space, consider the following benefits of scaling up:
  * **Larger Datasets** : Supports larger datasets, which can improve the relevance and quality of search results.
  * **Improved Indexing** : Enables the use of advanced indexing strategies like HNSW.
  * **Caching** : Enhances speed by having more RAM, allowing more frequently accessed data to be cached.
  * **Backups and Redundancy** : Facilitates more frequent backups, which is a key advantage for data safety.


Always remember to add 50% of the vector size. This would account for things like indexes and auxiliary data used during operations such as vector insertion, deletion, and search. Thus, the estimated memory size including metadata is:
```
total_vector_size = number_of_dimensions * 4 bytes * 1.5

```

**Disclaimer**
The above calculations are estimates at best. If you’re looking for more accurate numbers, you should always test your data set in practice.
##### Was this page useful?
![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg) Yes  ![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg) No
Thank you for your feedback! 🙏
We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/capacity-planning.md) this page on GitHub, or
On this page:
  * [Capacity Planning](https://qdrant.tech/documentation/guides/capacity-planning/#capacity-planning)
    * [Calculating RAM size](https://qdrant.tech/documentation/guides/capacity-planning/#calculating-ram-size)
    * [Calculating payload size](https://qdrant.tech/documentation/guides/capacity-planning/#calculating-payload-size)
    * [Choosing disk over RAM](https://qdrant.tech/documentation/guides/capacity-planning/#choosing-disk-over-ram)
      * [Storage-focused configuration](https://qdrant.tech/documentation/guides/capacity-planning/#storage-focused-configuration)
      * [Subgroup-oriented configuration](https://qdrant.tech/documentation/guides/capacity-planning/#subgroup-oriented-configuration)
    * [Scaling disk space in Qdrant Cloud](https://qdrant.tech/documentation/guides/capacity-planning/#scaling-disk-space-in-qdrant-cloud)


×
[ Powered by ](https://qdrant.tech/)
## About cookies on this site
We use cookies to collect and analyze information on site performance and usage, to provide social media features, and to enhance and customize content and advertisements. [Learn more](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)
Cookies Settings Accept All Cookies
![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)
## Privacy Preference Center
Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser. Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.
[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)
Allow All
###  Manage Consent Preferences
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
#### Performance Cookies
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Reject All Confirm My Choices
