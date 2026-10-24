Search
Suggestions will filter as you type
  * [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/azure/storage/blobs/)
  *     * [What is Azure Blob Storage?](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview)
    * [Compare core storage services](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction?toc=/azure/storage/blobs/toc.json&bc=/azure/storage/blobs/breadcrumb/toc.json)
    * [Blob Storage feature support](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-feature-support-in-storage-accounts)
  *     *       * [Introduction to Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)
      * [Blob Storage feature support](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-feature-support-in-storage-accounts)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/)
  2. [ Azure ](https://learn.microsoft.com/en-us/azure/)
  3. [ Storage ](https://learn.microsoft.com/en-us/azure/storage/)
  4. [ Blobs ](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)


  1. [Learn](https://learn.microsoft.com/en-us/)
  2. [Azure](https://learn.microsoft.com/en-us/azure/)
  3. [Storage](https://learn.microsoft.com/en-us/azure/storage/)
  4. [Blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) or changing directories.
Access to this page requires authorization. You can try changing directories.
# Introduction to Azure Data Lake Storage
Feedback
Summarize this article for me
##  In this article
  1. [What is a Data Lake?](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#what-is-a-data-lake)
  2. [Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#data-lake-storage)
  3. [Built on Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#built-on-azure-blob-storage)
  4. [Documentation and terminology](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#documentation-and-terminology)
  5. [See also](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#see-also)


Azure Data Lake Storage is a set of capabilities dedicated to big data analytics, built on [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction).
Azure Data Lake Storage converges the capabilities of [Azure Data Lake Storage Gen1](https://learn.microsoft.com/en-us/azure/data-lake-store/) with Azure Blob Storage. For example, Data Lake Storage provides file system semantics, file-level security, and scale. Because these capabilities are built on Blob storage, you also get low-cost, tiered storage, with high availability/disaster recovery capabilities.
Data Lake Storage makes Azure Storage the foundation for building enterprise data lakes on Azure. Designed from the start to service multiple petabytes of information while sustaining hundreds of gigabits of throughput, Data Lake Storage allows you to easily manage massive amounts of data.
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#what-is-a-data-lake)
## What is a Data Lake?
A _data lake_ is a single, centralized repository where you can store all your data, both structured and unstructured. A data lake enables your organization to quickly and more easily store, access, and analyze a wide variety of data in a single location. With a data lake, you don't need to conform your data to fit an existing structure. Instead, you can store your data in its raw or native format, usually as files or as binary large objects (blobs).
_Azure Data Lake Storage_ is a cloud-based, enterprise data lake solution. It's engineered to store massive amounts of data in any format, and to facilitate big data analytical workloads. You use it to capture data of any type and ingestion speed in a single location for easy access and analysis using various frameworks.
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#data-lake-storage)
## Data Lake Storage
Azure Data Lake Storage isn't a dedicated service or account type. Instead, it's implemented as a set of capabilities that you use with the Blob Storage service of your Azure Storage account. You can unlock these capabilities by enabling the hierarchical namespace setting.
Data Lake Storage includes the following capabilities.
✓ Hadoop-compatible access
✓ Hierarchical directory structure
✓ Optimized cost and performance
✓ Finer grain security model
✓ Massive scalability
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#hadoop-compatible-access)
#### Hadoop-compatible access
Azure Data Lake Storage is primarily designed to work with Hadoop and all frameworks that use the Apache [Azure Blob File System (ABFS)](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-abfs-driver) driver, which enables many applications and frameworks to access Azure Blob Storage data directly. The ABFS driver is [optimized specifically](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-abfs-driver) for big data analytics. The corresponding REST APIs are surfaced through the endpoint `dfs.core.windows.net`.
Data analysis frameworks that use HDFS as their data access layer can directly access Azure Data Lake Storage data through ABFS. The Apache Spark analytics engine and the Presto SQL query engine are examples of such frameworks.
For more information about supported services and platforms, see [Azure services that support Azure Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-supported-azure-services) and [Open source platforms that support Azure Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-supported-open-source-platforms).
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#hierarchical-directory-structure)
#### Hierarchical directory structure
The [hierarchical namespace](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-namespace) is a key feature that enables Azure Data Lake Storage to provide high-performance data access at object storage scale and price. You can use this feature to organize all the objects and files within your storage account into a hierarchy of directories and nested subdirectories. In other words, your Azure Data Lake Storage data is organized in much the same way that files are organized on your computer.
Operations such as renaming or deleting a directory, become single atomic metadata operations on the directory. There's no need to enumerate and process all objects that share the name prefix of the directory.
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#optimized-cost-and-performance)
#### Optimized cost and performance
Azure Data Lake Storage is priced at Azure Blob Storage levels. It builds on Azure Blob Storage capabilities such as automated lifecycle policy management and object level tiering to manage big data storage costs.
Performance is optimized because you don't need to copy or transform data as a prerequisite for analysis. The hierarchical namespace capability of Azure Data Lake Storage allows for efficient access and navigation. This architecture means that data processing requires fewer computational resources, reducing both the speed and cost of accessing data.
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#finer-grain-security-model)
#### Finer grain security model
The Azure Data Lake Storage access control model supports both Azure role-based access control (Azure RBAC) and Portable Operating System Interface for UNIX (POSIX) access control lists (ACLs). There are also a few extra security settings that are specific to Azure Data Lake Storage. You can set permissions either at the directory level or at the file level. All stored data is encrypted at rest by using either Microsoft-managed or customer-managed encryption keys.
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#massive-scalability)
#### Massive scalability
Azure Data Lake Storage offers massive storage and accepts numerous data types for analytics. It doesn't impose any limits on account sizes, file sizes, or the amount of data that can be stored in the data lake. Individual files can have sizes that range from a few kilobytes (KBs) to hundreds of terabytes (TBs). Processing is executed at near-constant per-request latencies that are measured at the service, account, and file levels.
This design means that Azure Data Lake Storage can easily and quickly scale up to meet the most demanding workloads. It can also just as easily scale back down when demand drops.
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#built-on-azure-blob-storage)
## Built on Azure Blob Storage
The data that you ingest persist as blobs in the storage account. The service that manages blobs is the Azure Blob Storage service. Data Lake Storage describes the capabilities or "enhancements" to this service that caters to the demands of big data analytic workloads.
Because these capabilities are built on Blob Storage, features such as diagnostic logging, access tiers, and lifecycle management policies are available to your account. Most Blob Storage features are fully supported, but some features might be supported only at the preview level and there are a handful of them that aren't yet supported. For a complete list of support statements, see [Blob Storage feature support in Azure Storage accounts](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-feature-support-in-storage-accounts). The status of each listed feature will change over time as support continues to expand.
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#documentation-and-terminology)
## Documentation and terminology
The Azure Blob Storage table of contents features two sections of content. The **Data Lake Storage** section of content provides best practices and guidance for using Data Lake Storage capabilities. The **Blob Storage** section of content provides guidance for account features not specific to Data Lake Storage.
As you move between sections, you might notice some slight terminology differences. For example, content featured in the Blob Storage documentation, will use the term _blob_ instead of _file_. Technically, the files that you ingest to your storage account become blobs in your account. Therefore, the term is correct. However, the term _blob_ can cause confusion if you're used to the term _file_. You'll also see the term _container_ used to refer to a _file system_. Consider these terms as synonymous.
[](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction#see-also)
## See also
  * [Introduction to Azure Data Lake Storage (Training module)](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-data-lake-storage/)
  * [Best practices for using Azure Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-best-practices)
  * [Known issues with Azure Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-known-issues)
  * [Multi-protocol access on Azure Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-multi-protocol-access)


* * *
## Feedback
Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
* * *
##  Additional resources
  * [ Best practices for using Azure Data Lake Storage - Azure Storage ](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-best-practices?source=recommendations)
Learn how to optimize performance, reduce costs, and secure your Data Lake Storage enabled Azure Storage account.
  * [ Create a storage account for Azure Data Lake Storage - Azure Storage ](https://learn.microsoft.com/en-us/azure/storage/blobs/create-data-lake-storage-account?source=recommendations)
Learn how to create a storage account for use with Azure Data Lake Storage.
  * [ Azure Data Lake Storage Gen2 overview in HDInsight ](https://learn.microsoft.com/en-us/azure/hdinsight/overview-data-lake-storage-gen2?source=recommendations)
Overview of Data Lake Storage Gen2 in HDInsight.
  * [ Azure services that support Azure Data Lake Storage - Azure Storage ](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-supported-azure-services?source=recommendations)
Learn about which Azure services integrate with Azure Data Lake Storage
  * [ Azure Data Lake Storage hierarchical namespace - Azure Storage ](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-namespace?source=recommendations)
Describes the concept of a hierarchical namespace for Azure Data Lake Storage
  * [ Premium tier for Azure Data Lake Storage - Azure Storage ](https://learn.microsoft.com/en-us/azure/storage/blobs/premium-tier-for-data-lake-storage?source=recommendations)
Use the premium performance tier with Azure Data Lake Storage
  * [ Known issues with Azure Data Lake Storage - Azure Storage ](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-known-issues?source=recommendations)
Learn about limitations and known issues of Azure Data Lake Storage.


Show 4 more
Module
[ Introduction to Azure Data Lake Storage Gen2 - Training ](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-data-lake-storage/?source=recommendations)
Discover how Data Lake Storage provides a repository where you can upload and store unstructured data bringing new efficiencies to processing big data analytics.
* * *
  * Last updated on 11/15/2024


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)
