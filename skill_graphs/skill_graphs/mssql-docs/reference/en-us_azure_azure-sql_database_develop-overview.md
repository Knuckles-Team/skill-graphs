Version Azure SQL
  * [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql-db)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql-mi)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=fabricsql)
  * [SQL Server on Azure VMs](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql-vm)


Search
Suggestions will filter as you type
  * [Azure SQL Documentation](https://learn.microsoft.com/en-us/azure/azure-sql/?view=azuresql)
  *     *       *         * [Overview](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql)
        * [Working with JSON data](https://learn.microsoft.com/en-us/azure/azure-sql/database/json-features?view=azuresql)
        * [Use Spark Connector](https://learn.microsoft.com/en-us/azure/azure-sql/database/spark-connector?view=azuresql)
        * [Use ASP.NET App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-dotnet-sqldatabase?toc=%2Fazure%2Fazure-sql%2Ftoc.json&view=azuresql)
        * [Use Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenario-database-table-cleanup?toc=%2Fazure%2Fazure-sql%2Ftoc.json&view=azuresql)
        * [Use Azure Logic Apps](https://learn.microsoft.com/en-us/azure/connectors/connectors-create-api-sqlazure?toc=%2Fazure%2Fazure-sql%2Ftoc.json&view=azuresql)
        * [Index with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-howto-connecting-azure-sql-database-to-azure-search-using-indexers?toc=%2Fazure%2Fazure-sql%2Ftoc.json&view=azuresql)
        * [Server-side CLR/.NET integration](https://learn.microsoft.com/en-us/sql/relational-databases/clr-integration/common-language-runtime-integration-overview?view=azuresql)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=azuresql)
  2. [ Azure ](https://learn.microsoft.com/en-us/azure/?view=azuresql)
  3. [ Azure SQL ](https://learn.microsoft.com/en-us/azure/azure-sql/?view=azuresql)
  4. [ Azure SQL Database ](https://learn.microsoft.com/en-us/azure/azure-sql/database/?view=azuresql)


  1. [Learn](https://learn.microsoft.com/en-us/?view=azuresql)
  2. [Azure](https://learn.microsoft.com/en-us/azure/?view=azuresql)
  3. [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/?view=azuresql)
  4. [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/?view=azuresql)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql) or changing directories.
Access to this page requires authorization. You can try changing directories.
# Application development overview - Azure SQL Database & Azure SQL Managed Instance
Feedback
Summarize this article for me
##  In this article
  1. [Language and platform](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#language-and-platform)
  2. [Authentication](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#authentication)
  3. [Client connections](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#client-connections)
  4. [Resiliency](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#resiliency)
  5. [Network considerations](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#network-considerations)
  6. [Related content](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#related-content)

Show 2 more
**Applies to:** ![](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) [Azure SQL Database](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide#applies-to) ![](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide#applies-to) ![](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) [SQL database in Fabric](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide#applies-to)
This article walks through the basic considerations that a developer should be aware of when writing code to connect to your database in Azure. This article applies to Azure SQL Database, and Azure SQL Managed Instance.
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#language-and-platform)
## Language and platform
You can use various [programming languages and platforms](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-content-reference-guide?view=azuresql) to connect and query Azure SQL Database. You can find [sample applications](https://azure.microsoft.com/resources/samples/?service=sql-database&sort=0) that you can use to connect to the database.
You can use open-source tools like [Visual Studio](https://visualstudio.microsoft.com/downloads) and [SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms). You can also use the Azure portal, PowerShell, and REST APIs to help you gain more productivity.
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#authentication)
## Authentication
Access to Azure SQL Database is protected with logins and firewalls. Azure SQL Database and SQL Managed Instance support users and logins for both SQL authentication and [authentication](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-overview?view=azuresql) with Microsoft Entra ID ([formerly Azure Active Directory](https://learn.microsoft.com/en-us/entra/fundamentals/new-name)). Microsoft Entra logins are generally available in SQL Managed Instance and are in Public Preview for Azure SQL Database.
Learn more about [managing database access and logins](https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#client-connections)
## Client connections
In your client connection logic, override the default timeout to be 30 seconds. The default of 15 seconds is too short for connections that depend on the internet.
If you're using a [connection pool](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql-server-connection-pooling), be sure to close the connection the instant your program isn't actively using it, and isn't preparing to reuse it.
Avoid long-running transactions because any infrastructure or connection failure might roll back the transaction. If possible, split the transaction in the multiple smaller transactions and use [batching to improve performance](https://learn.microsoft.com/en-us/azure/azure-sql/performance-improve-use-batching?view=azuresql).
It's possible to connect your application to your Azure SQL resource by using the following languages:
  * [.NET with Visual Studio](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-dotnet-visual-studio?view=azuresql)
  * [.NET with Windows, Linux, and macOS](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-dotnet-core?view=azuresql)
  * [Go](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-go?view=azuresql)
  * [Node.js](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-nodejs?view=azuresql)
  * [PHP](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-php?view=azuresql)
  * [Python](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql)
  * [Ruby](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-ruby?view=azuresql)


It's possible to configure Microsoft Entra authentication to your Azure SQL resource. Review the following articles for more information:
  * [Connect to Azure SQL with Microsoft Entra authentication and SqlClient](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql/azure-active-directory-authentication)
  * [Managed identities in Microsoft Entra for Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-azure-ad-user-assigned-managed-identity?view=azuresql)
  * [Connect to SQL Database from .NET App Service without secrets using a managed identity](https://learn.microsoft.com/en-us/azure/app-service/tutorial-connect-msi-sql-database)


[](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#resiliency)
## Resiliency
Azure SQL Database is a cloud service where you might expect transient errors that happen in the underlying infrastructure or in the communication between cloud entities. Although Azure SQL Database is resilient on the transitive infrastructure failures, any network infrastructure failures could briefly affect your connectivity. When a transient error occurs while connecting to SQL Database, your code should [retry the call](https://learn.microsoft.com/en-us/azure/azure-sql/database/troubleshoot-common-connectivity-issues?view=azuresql#retry-logic-for-transient-errors).
We recommend that retry logic always retry after delay, using backoff logic, so that it doesn't overwhelm the service with multiple clients retrying simultaneously. Retry logic depends on the [error messages for SQL Database client programs](https://learn.microsoft.com/en-us/azure/azure-sql/database/troubleshoot-common-errors-issues?view=azuresql#list-of-transient-fault-error-codes).
For more information on retry logic after delay:
  * [Azure Architecture Center: Retry pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)
  * [Troubleshoot transient connection errors](https://learn.microsoft.com/en-us/azure/azure-sql/database/troubleshoot-common-connectivity-issues?view=azuresql-db&preserve-view=true#retry-logic-for-transient-errors)
  * [Configurable retry logic in Microsoft.Data.SqlClient](https://learn.microsoft.com/en-us/sql/connect/ado-net/configurable-retry-logic-sqlclient-introduction?view=azuresqldb-current&preserve-view=true)
  * [DevBlog: Introducing Configurable Retry Logic in Microsoft.Data.SqlClient](https://devblogs.microsoft.com/azure-sql/configurable-retry-logic-for-microsoft-data-sqlclient/)


For more information about how to prepare for planned maintenance events on your Azure SQL Database, see [planning for Azure maintenance events in Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/planned-maintenance?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#network-considerations)
## Network considerations
  * On the computer that hosts your client program, ensure the firewall allows outgoing TCP communication on port 1433. More information: [Azure SQL Database IP firewall rules](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure?view=azuresql).
  * If your client program connects to SQL Database while your client runs on an Azure virtual machine (VM), you must open certain port ranges on the VM. More information: [Ports beyond 1433 for ADO.NET 4.5](https://learn.microsoft.com/en-us/azure/azure-sql/database/adonet-v12-develop-direct-route-ports?view=azuresql).
  * Client connections to Azure SQL Database sometimes bypass the proxy and interact directly with the database. Ports other than 1433 become important. For more information, [Connectivity architecture](https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-architecture?view=azuresql) and [Ports beyond 1433 for ADO.NET 4.5](https://learn.microsoft.com/en-us/azure/azure-sql/database/adonet-v12-develop-direct-route-ports?view=azuresql).
  * For networking configuration for an instance of SQL Managed Instance, see [network configuration for SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/how-to-content-reference-guide?view=azuresql#network-configuration).


[](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#related-content)
## Related content
Explore all the capabilities of [SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql) and [SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql).
To get started, see the guides for [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/quickstart-content-reference-guide?view=azuresql) and [Azure SQL Managed Instances](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/quickstart-content-reference-guide?view=azuresql).
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
  * [ What is the Azure SQL Database service? - Azure SQL Database ](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?source=recommendations)
Get an introduction to SQL Database: technical details and capabilities of the Microsoft relational database management system (RDBMS) in the cloud.
  * [ What Is Azure SQL? - Azure SQL ](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview?source=recommendations)
Learn about the different options within the Azure SQL family of services: Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VM.
  * [ Single Database Quickstart Content Reference - Azure SQL Database ](https://learn.microsoft.com/en-us/azure/azure-sql/database/quickstart-content-reference-guide?source=recommendations)
Find a content reference of all the quickstarts that help you quickly get started with Azure SQL Database.
  * [ Create a Single Database - Azure SQL Database ](https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?source=recommendations)
Create a single database in Azure SQL Database using the Azure portal, PowerShell, or the Azure CLI.
  * [ Glossary of Terms - Azure SQL Database & SQL Managed Instance ](https://learn.microsoft.com/en-us/azure/azure-sql/glossary-terms?source=recommendations)
A glossary of terms for working with Azure SQL Database, Azure SQL Managed Instance, and SQL on Azure VM.
  * [ Tutorial: Design Your First Relational Database Using SSMS - Azure SQL Database ](https://learn.microsoft.com/en-us/azure/azure-sql/database/design-first-database-tutorial?source=recommendations)
Learn to design your first relational database in Azure SQL Database using SQL Server Management Studio.


Show 3 more
Learning path
[ Develop data-driven applications by using Azure SQL Database - Training ](https://learn.microsoft.com/en-us/training/paths/develop-data-driven-app-sql-db/?source=recommendations)
Learn how to develop data-driven applications by using Microsoft Azure SQL Database. DP-3020
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
* * *
  * Last updated on 06/11/2025


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql)
