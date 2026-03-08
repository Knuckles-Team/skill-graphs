Version SQL Server Analysis Services 2025
  * [All Analysis Services](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=asallproducts-allversions)
  * [Azure Analysis Services](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=azure-analysis-services-current)
  * [Fabric/Power BI Premium](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=power-bi-premium-current)
  * SQL Server Analysis Services
    * [2025](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025)
    * [2022](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2022)
    * [2019](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2019)
    * [2017](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2017)
    * [2016](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2016)


Search
Suggestions will filter as you type
  * [Analysis Services documentation](https://learn.microsoft.com/en-us/analysis-services/?view=sql-analysis-services-2025)
  * [Analysis Services tools](https://learn.microsoft.com/en-us/analysis-services/tools-and-applications-used-in-analysis-services?view=sql-analysis-services-2025)
  * [Comparing tabular and multidimensional](https://learn.microsoft.com/en-us/analysis-services/comparing-tabular-and-multidimensional-solutions-ssas?view=sql-analysis-services-2025)
  *     *       * [Install SQL Server Analysis Services](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025)
      * [Verify cumulative update build version](https://learn.microsoft.com/en-us/analysis-services/instances/analysis-services-component-version?view=sql-analysis-services-2025)
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
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025) or changing directories.
Access to this page requires authorization. You can try changing directories.
# Install SQL Server Analysis Services
Feedback
Summarize this article for me
##  In this article
  1. [Install using the wizard](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025#install-using-the-wizard)
  2. [Command Line Setup](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025#command-line-setup)
  3. [Get tools and designers](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025#get-tools-and-designers)
  4. [See also](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025#see-also)


**Applies to:** ![](https://learn.microsoft.com/en-us/analysis-services/includes/media/yes.png?view=sql-analysis-services-2025) SQL Server Analysis Services ![](https://learn.microsoft.com/en-us/analysis-services/includes/media/no.png?view=sql-analysis-services-2025) Azure Analysis Services ![](https://learn.microsoft.com/en-us/analysis-services/includes/media/no.png?view=sql-analysis-services-2025) Fabric/Power BI Premium
SQL Server Analysis Services is installed by using the SQL Server Installation Wizard (setup.exe). This article describes only those Wizard pages or command line settings necessary for installing and specifying initial configuration settings when installing an Analysis Services instance by using the Wizard.
If you've never installed SQL Server or SQL Server Analysis Services before, it's important you have a good understanding of the Wizard. For more detailed step-by-step information about using the wizard, see [Install SQL Server from the Installation Wizard (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-from-the-installation-wizard-setup). For more detailed information about Wizard configuration pages, see [Installation Wizard help](https://learn.microsoft.com/en-us/sql/sql-server/install/instance-configuration)
SQL Server Analysis Services is multi-instance, meaning you can install more than one copy on a single computer, or run new and old versions side-by-side. An instance runs in either Tabular mode (default) or Multidimensional mode. If you want to run more than one mode, you'll need a separate instance for each one.
After you install the server in a particular mode, you can use it host solutions that conform to that mode. For example, a tabular mode server is required if you want tabular model data access over the network.
[](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025#install-using-the-wizard)
## Install using the wizard
The following shows which pages in the SQL Server Installation Wizard are used to install Analysis Services.
  1. On the **Feature Selection** page, select **Analysis Services** from the feature tree.
![Setup feature tree showing Analysis Services](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/media/install-analysis-services/ssas-install-feature-selection.png?view=sql-analysis-services-2025)
  2. On the **Analysis Services Configuration** page > **Server Configuration** tab, select a mode. Then add users that will have Administrator permissions for the instance. Click the **Data Directories** tab verify default or specify different [data directories](https://learn.microsoft.com/en-us/sql/sql-server/install/instance-configuration#analysis-services-configuration---data-directories-page).
![Setup page with Analysis Services config options](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/media/install-analysis-services/ssas-install-asmode-config.png?view=sql-analysis-services-2025)


Tabular mode uses the VertiPaq in-memory analytics engine (VertiPaq), which is the default storage for tabular models. After you deploy tabular models to the server, you can selectively configure tabular solutions to use DirectQuery disk storage as an alternative to memory-bound storage.
Multidimensional mode uses MOLAP as the default storage for models deployed to Analysis Services. After deploying to the server, you can configure a solution to use ROLAP if you want to run queries directly against the relational database rather than storing query data in an Analysis Services multidimensional database .
Memory management and IO settings can be adjusted to get better performance when using non-default storage modes. See [Server properties in Analysis Services](https://learn.microsoft.com/en-us/analysis-services/server-properties/server-properties-in-analysis-services?view=sql-analysis-services-2025) for more information.
[](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025#command-line-setup)
## Command Line Setup
SQL Server Setup includes a parameter (**ASSERVERMODE**) that specifies the server mode. The following example illustrates a command line setup that installs Analysis Services in Tabular server mode.
Copy
```
Setup.exe /q /IAcceptSQLServerLicenseTerms /ACTION=install /FEATURES=AS /ASSERVERMODE=TABULAR /INSTANCENAME=ASTabular /INDICATEPROGRESS /ASSVCACCOUNT=<DomainName\UserName> /ASSVCPASSWORD=<StrongPassword> /ASSYSADMINACCOUNTS=<DomainName\UserName>

```

**INSTANCENAME** must be less than 17 characters.
All placeholder account values must be replaced with valid accounts and password.
**ASSERVERMODE** is case-sensitive. All values must be expressed in upper case. The following table describes the valid values for **ASSERVERMODE**.
Expand table
Value | Description
---|---
TABULAR | This is the default value. If you do not set **ASSERVERMODE** , the server is installed in Tabular mode.
MULTIDIMENSIONAL | This value is optional.
[](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025#get-tools-and-designers)
## Get tools and designers
The Wizard no longer installs SQL Server Data Tools (SSDT) used for designing models or SQL Server Management Studio (SSMS) used for server administration. Designers and tools now have a separate installation. To learn about and install both Microsoft and third party tools, see [Analysis Services tools](https://learn.microsoft.com/en-us/analysis-services/tools-and-applications-used-in-analysis-services?view=sql-analysis-services-2025).
You'll need both Visual Studio with the Analysis Services projects extension and SSMS to create, deploy, and work with Analysis Services instances and databases. Tools can be installed anywhere, but be sure to configure ports on the server before attempting a connection. See [Configure the Windows Firewall to Allow Analysis Services Access](https://learn.microsoft.com/en-us/analysis-services/instances/configure-the-windows-firewall-to-allow-analysis-services-access?view=sql-analysis-services-2025) for details.
[](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025#see-also)
## See also
[SQL Server Installation Wizard](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/installation-for-sql-server)
[Determine the Server Mode of an Analysis Services Instance](https://learn.microsoft.com/en-us/analysis-services/instances/determine-the-server-mode-of-an-analysis-services-instance?view=sql-analysis-services-2025)
[Comparing tabular and multidimensional solutions](https://learn.microsoft.com/en-us/analysis-services/comparing-tabular-and-multidimensional-solutions-ssas?view=sql-analysis-services-2025)
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
  * [ Analysis Services tools ](https://learn.microsoft.com/en-us/analysis-services/tools-and-applications-used-in-analysis-services?source=recommendations)
Learn how to find the tools and applications you'll need for building Analysis Services models and managing deployed databases.
  * [ SQL Server Analysis Services overview ](https://learn.microsoft.com/en-us/analysis-services/ssas-overview?source=recommendations)
Describes SQL Server Analysis Services.
  * [ Install and configure a SQL Analysis Server - Virtual Machine Manager ](https://learn.microsoft.com/en-us/troubleshoot/system-center/vmm/install-configure-sql-analysis-server?source=recommendations)
Describes how to how to install and configure a SQL Analysis Server using service templates in System Center 2012 Virtual Machine Manager.
  * [ Determine the Server Mode of an Analysis Services Instance ](https://learn.microsoft.com/en-us/analysis-services/instances/determine-the-server-mode-of-an-analysis-services-instance?source=recommendations)
Learn how to determine the server mode of an Analysis Services Instance, which is determined during setup when you choose options for installing the server.
  * [ Create an Analysis Services Project ](https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/create-an-analysis-services-project-ssdt?source=recommendations)
Define an Analysis Services project in SQL Server Data Tools by using the Analysis Services Project template or the Import Analysis Services Database Wizard.
  * [ Install Business Intelligence Features - SQL Server ](https://learn.microsoft.com/en-us/sql/sql-server/install/install-sql-server-business-intelligence-features?source=recommendations)
This article provides links to information to install SQL Server features that are part of the Microsoft Business Intelligence platform.
  * [ Analysis Services features supported by SQL Server edition ](https://learn.microsoft.com/en-us/analysis-services/analysis-services-features-by-edition?source=recommendations)
Learn about features supported by different editions of SQL Server 2016, 2017, 2019 Analysis Services.
  * [ Post-install Configuration (Analysis Services) ](https://learn.microsoft.com/en-us/analysis-services/instances/post-install-configuration-analysis-services?source=recommendations)
Learn about further configuration after installing Analysis Services that is required to make the server fully operational and available for general use.


Show 5 more
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
* * *
  * Last updated on 02/05/2024


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=sql-analysis-services-2025)
