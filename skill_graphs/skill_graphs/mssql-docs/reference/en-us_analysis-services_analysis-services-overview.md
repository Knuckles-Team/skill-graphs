Version SQL Server Analysis Services 2025
  * [All Analysis Services](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=asallproducts-allversions)
  * [Azure Analysis Services](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=azure-analysis-services-current)
  * [Fabric/Power BI Premium](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=power-bi-premium-current)
  * SQL Server Analysis Services
    * [2025](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2025)
    * [2022](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2022)
    * [2019](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2019)
    * [2017](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2017)
    * [2016](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2016)


Search
Suggestions will filter as you type
  * [Analysis Services documentation](https://learn.microsoft.com/en-us/analysis-services/?view=sql-analysis-services-2025)
  *     * [What is Analysis Services?](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2025)
    * [Understanding documentation](https://learn.microsoft.com/en-us/analysis-services/analysis-services-docs?view=sql-analysis-services-2025)
  * [Analysis Services tools](https://learn.microsoft.com/en-us/analysis-services/tools-and-applications-used-in-analysis-services?view=sql-analysis-services-2025)
  * [Comparing tabular and multidimensional](https://learn.microsoft.com/en-us/analysis-services/comparing-tabular-and-multidimensional-solutions-ssas?view=sql-analysis-services-2025)
  * [References](https://learn.microsoft.com/en-us/analysis-services/analysis-services-references?view=sql-analysis-services-2025)
  * [Samples](https://learn.microsoft.com/en-us/analysis-services/analysis-services-samples?view=sql-analysis-services-2025)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=sql-analysis-services-2025)
  2. [ Power Platform ](https://learn.microsoft.com/en-us/power-platform/?view=sql-analysis-services-2025)
  3. [ Power BI ](https://learn.microsoft.com/en-us/power-bi/?view=sql-analysis-services-2025)


  1. [Learn](https://learn.microsoft.com/en-us/?view=sql-analysis-services-2025)
  2. [Power Platform](https://learn.microsoft.com/en-us/power-platform/?view=sql-analysis-services-2025)
  3. [Power BI](https://learn.microsoft.com/en-us/power-bi/?view=sql-analysis-services-2025)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2025) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2025) or changing directories.
Access to this page requires authorization. You can try changing directories.
# What is Analysis Services?
Feedback
Summarize this article for me
##  In this article
**Applies to:** ![](https://learn.microsoft.com/en-us/analysis-services/includes/media/yes.png?view=sql-analysis-services-2025) SQL Server Analysis Services ![](https://learn.microsoft.com/en-us/analysis-services/includes/media/yes.png?view=sql-analysis-services-2025) Azure Analysis Services ![](https://learn.microsoft.com/en-us/analysis-services/includes/media/yes.png?view=sql-analysis-services-2025) Fabric/Power BI Premium
Analysis Services is an analytical data engine (VertiPaq) used in decision support and business analytics. It provides enterprise-grade semantic data model capabilities for business intelligence (BI), data analysis, and reporting applications such as Fabric/Power BI, Excel, Reporting Services, and other data visualization tools. Analysis Services is available in different platforms:
**Power BI** - The Analysis Services engine supports the semantic model (previously known as dataset) artifact in [Power BI](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview). Semantic models are created in Power BI Desktop and then published to the Power BI service. Any number of reports can then be created using the model and those reports can be shared across the organization in the Power BI service.
The Analysis Service engine also provides programmability, client application, and tool support for Power BI Premium and Premium Per User semantic models through client libraries and APIs that support the open-standard XMLA protocol. Premium models support connections through XMLA endpoints for _read-only_ and _read-write_ operations from Microsoft and third-party client applications and tools. To learn more, see [What is Power BI Premium](https://learn.microsoft.com/en-us/power-bi/service-premium-what-is#analysis-services-in-power-bi-premium) and [Semantic model connectivity with the XMLA Endpoint](https://learn.microsoft.com/en-us/power-bi/service-premium-connect-tools).
**Microsoft Fabric** - Microsoft Fabric includes Power BI. And much like Power BI, the Analysis Services engine supports Microsoft Fabric semantic models. The [Lakehouse](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview) architecture in Microsoft Fabric includes the concept of a _default semantic model_ in the SQL endpoint, also supported by Analysis Services. Unique in Microsoft Fabric, with Lakehouse delta tables you have the option to use _Direct Lake storage mode_. Direct Lake mode is a groundbreaking data access technology for semantic models based on loading Delta-Parquet files directly from OneLake without having to import or duplicate the data. Direct Lake combines the advantages of DirectQuery and Import modes to deliver fast query performance without any data movement. To learn more, see [What is Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview) and [Learn about Direct Lake in Power BI and Microsoft Fabric](https://learn.microsoft.com/en-us/power-bi/enterprise/directlake-overview).
  * **Mirroring to Microsoft Fabric** Mirroring to Fabric provides the ability to unify your data estate with OneLake in Fabric and open access to your data in Delta Parquet format. With Mirroring to Microsoft Fabric, you can continuously replicate your existing data estate directly into OneLake in Fabric, including data from SQL Server 2016+, Azure SQL Database, Azure SQL Managed Instance, Cosmos DB, Oracle, Snowflake, and more. For more information, see [Microsoft Fabric mirrored databases](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/overview).


**Azure Analysis Services** - Created as an Azure resource, Azure Analysis Services server resources support tabular models at the 1200 and higher compatibility levels. DirectQuery, partitions, row-level security, bi-directional relationships, and translations are all supported. To learn more, see [What is Azure Analysis Services](https://learn.microsoft.com/en-us/azure/analysis-services/analysis-services-overview).
**SQL Server Analysis Services** - Installed as an on-premises or VM server instance, SQL Server Analysis Services supports tabular models at all compatibility levels (depending on version), multidimensional models, and Power Pivot for SharePoint. To learn more, see [SQL Server Analysis Services overview](https://learn.microsoft.com/en-us/analysis-services/ssas-overview?view=sql-analysis-services-2025).
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
  * [ SQL Server Analysis Services overview ](https://learn.microsoft.com/en-us/analysis-services/ssas-overview?source=recommendations)
Describes SQL Server Analysis Services.
  * [ Comparing Analysis Services tabular and multidimensional models ](https://learn.microsoft.com/en-us/analysis-services/comparing-tabular-and-multidimensional-solutions-ssas?source=recommendations)
Describes the differences between Analysis Services multidimensional and tabular model solutions.
  * [ Analysis Services tools ](https://learn.microsoft.com/en-us/analysis-services/tools-and-applications-used-in-analysis-services?source=recommendations)
Learn how to find the tools and applications you'll need for building Analysis Services models and managing deployed databases.
  * [ What's new in SQL Server Analysis Services ](https://learn.microsoft.com/en-us/analysis-services/what-s-new-in-sql-server-analysis-services?source=recommendations)
Learn about new features and improvements in the most recent versions of SQL Server Analysis Services (SSAS).
  * [ Analysis Services documentation overview ](https://learn.microsoft.com/en-us/analysis-services/analysis-services-docs?source=recommendations)
Describes Analysis Services documentation.
  * [ Analysis Services Tutorials ](https://learn.microsoft.com/en-us/analysis-services/analysis-services-tutorials-ssas?source=recommendations)
Learn about the different models and data mining that the Analysis Services tutorials cover.
  * [ Analysis Services features supported by SQL Server edition ](https://learn.microsoft.com/en-us/analysis-services/analysis-services-features-by-edition?source=recommendations)
Learn about features supported by different editions of SQL Server 2016, 2017, 2019 Analysis Services.


Show 4 more
Certification
[ Microsoft Certified: Power BI Data Analyst Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/?source=recommendations)
Demonstrate methods and best practices that align with business and technical requirements for modeling, visualizing, and analyzing data with Microsoft Power BI.
* * *
  * Last updated on 11/18/2025


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/analysis-services/analysis-services-overview?view=sql-analysis-services-2025)
