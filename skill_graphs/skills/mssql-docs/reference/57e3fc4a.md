# Install and configure SQL Server Reporting Services
Feedback
Summarize this article for me
##  In this article
  1. [Prerequisites](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#prerequisites)
  2. [Install SSRS](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#install-ssrs)
  3. [Configure your report server](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#configure-your-report-server)
  4. [Windows service](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#windows-service)
  5. [Default URL reservations](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#default-url-reservations)
  6. [Firewall](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#firewall)
  7. [Configure other features](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#configure-other-features)
  8. [Related content](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#related-content)

Show 4 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server Reporting Services (2017 and later versions) ![Not supported](https://learn.microsoft.com/en-us/sql/includes/media/no-icon.svg?view=sql-server-ver17) Power BI Report Server
This article helps you download, install, and configure SQL Server Reporting Services (SSRS). SSRS installation involves server components for storing report items, rendering reports, and processing of subscription and other report services. Alternatively, an administrator can install Reporting Services with [Microsoft Endpoint Configuration Manager](https://learn.microsoft.com/en-us/configmgr/).
Starting in SQL Server 2025 (17.x), on-premises reporting services is consolidated under [Power BI Report Server](https://learn.microsoft.com/en-us/power-bi/report-server/get-started). For more information, see [Reporting Services consolidation FAQ](https://learn.microsoft.com/en-us/sql/reporting-services/reporting-services-consolidation-faq?view=sql-server-ver17).
Download [**SQL Server 2022 Reporting Services**](https://www.microsoft.com/download/details.aspx?id=104502) from the Microsoft Download Center.
Download [**SQL Server 2019 Reporting Services**](https://www.microsoft.com/download/details.aspx?id=100122) from the Microsoft Download Center.
Download [**SQL Server 2017 Reporting Services**](https://www.microsoft.com/download/details.aspx?id=55252) from the Microsoft Download Center.
Looking for Power BI Report Server? See [Install Power BI Report Server](https://powerbi.microsoft.com/documentation/reportserver-install-report-server/).
Upgrading or migrating from a SQL Server 2016 or earlier version of Reporting Services? See [Upgrade and migrate Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#prerequisites)
## Prerequisites
Review the [Hardware and software requirements for SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-2022?view=sql-server-ver17). Ensure that the computer where you're installing SSRS meets the appropriate hardware and software prerequisites for the version you want to install.
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#install-ssrs)
## Install SSRS
Use the following steps to install SSRS.
  1. Locate `SQLServerReportingServices.exe` and launch the installer.
  2. Select **Install Reporting Services**.
  3. Choose an edition to install and select **Next**.
For a free edition, choose either Evaluation or Developer.
![Screenshot of the Reporting Services editions that are available for download.](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/media/install-reporting-services/report-server-install-edition-select.png?view=sql-server-ver17)
Otherwise, enter a product key. For more information, see [Find the product key for SQL Server Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/find-reporting-services-product-key-ssrs?view=sql-server-ver17).
  4. Accept the license terms and conditions, and then select **Next**.
  5. Select **Next**.
  6. Specify the installation location for the report server. Select **Install** to continue.
The default path is `C:\Program Files\Microsoft SQL Server Reporting Services`.
  7. After the installation completes, select **Configure report server** to launch the Report Server Configuration Manager.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#configure-your-report-server)
## Configure your report server
After you select **Configure Report Server** , the **Report Server Configuration Manager** appears. For more information, see [Report Server Configuration Manager](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/reporting-services-configuration-manager-native-mode?view=sql-server-ver17).
Follow the instructions to [Create a report server database](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/ssrs-report-server-create-a-report-server-database?view=sql-server-ver17) to complete the initial Reporting Services configuration process.
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#create-a-database-on-a-different-server)
### Create a database on a different server
If you're creating the report server database on a separate database server, change the service account for the report server to a credential recognized on the database server.
By default, the report server uses the virtual service account. Attempting to create a database on a different server might lead to the following error during the **Applying connection rights** step:
`System.Data.SqlClient.SqlException (0x80131904): Windows NT user or group '(null)' not found. Check the name again.`
To address this issue, you can change the service account to either Network Service or a domain account. Choosing **Network Service** applies rights in the context of the report server's computer account.
For more information, see [Configure the report server service account](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/configure-the-report-server-service-account-ssrs-configuration-manager?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#windows-service)
## Windows service
The installation creates a Windows service as a part of the process. The service displays as **SQL Server Reporting Services**. The service name is **SQLServerReportingServices**.
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#default-url-reservations)
## Default URL reservations
URL reservations are composed of a prefix, host name, port, and virtual directory:
Expand table
Part | Description
---|---
Prefix | The default prefix is `HTTP`. If you installed a Transport Layer Security (TLS) certificate, the installer creates URL reservations that use the `HTTPS` prefix.
Host name | The default host name is a strong wildcard (+). It specifies that the report server accepts any HTTP request on the designated port for any host name that resolves to the computer, including `https://<computername>/reportserver`, `https://localhost/reportserver`, or `https://<IPAddress>/reportserver`.
Port | The default port is 80. If you use any other port, you must explicitly add the port to the URL when you open web portal in a browser window.
Virtual directory | By default, the Report Server web service virtual directory is `reportserver`. For the web portal, the default virtual directory is `reports`.
Examples of the complete URL string are:
  * `https://+:80/reportserver`: This string provides access to the report server.
  * `https://+:80/reports`: This string provides access to the web portal.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#firewall)
## Firewall
If you're accessing the report server from a remote computer and there's a firewall present, make sure you configured any firewall rules.
Open the TCP port that you configured for your web service URL and web portal URL. By default, these URLs are configured on TCP port 80.
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#configure-other-features)
## Configure other features
You might need to configure other features for better report access and usability. You can configure integration with the Power BI service so that you can pin report items to a Power BI dashboard. For more information, see [Power BI Report Server Integration (Configuration Manager)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/power-bi-report-server-integration-configuration-manager?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#configure-email-for-subscriptions-processing)
### Configure email for subscriptions processing
To configure email for subscriptions processing, see:
  * [Email settings in SSRS native mode](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/e-mail-settings-reporting-services-native-mode-configuration-manager?view=sql-server-ver17)
  * [Email delivery in Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/subscriptions/e-mail-delivery-in-reporting-services?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#set-up-reports-from-a-remote-computer)
### Set up reports from a remote computer
You can also set up the web portal so that you can access and manage reports from a remote computer. For more information, see:
  * [Configure a firewall for report server access](https://learn.microsoft.com/en-us/sql/reporting-services/report-server/configure-a-firewall-for-report-server-access?view=sql-server-ver17)
  * [Configure a report server for remote administration](https://learn.microsoft.com/en-us/sql/reporting-services/report-server/configure-a-report-server-for-remote-administration?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#related-content)
## Related content
  * For information on how to install SQL Server Reporting Services native mode, see [Install Reporting Services native mode report server](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services-native-mode-report-server?view=sql-server-ver17).
  * With your report server installed, begin to create reports and deploy the reports to your report server. For information on how to start with Report Builder, see [Install Microsoft Report Builder](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-report-builder?view=sql-server-ver17).
  * For information on how to create reports using SQL Server Data Tools, [download SQL Server Data Tools](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-ver17).


  * For information on how to install SQL Server 2016 Reporting Services (and earlier) in SharePoint integration mode, see [Install the first Report Server in SharePoint mode](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-the-first-report-server-in-sharepoint-mode?view=sql-server-ver17).


More questions? [Try asking the Reporting Services forum](https://learn.microsoft.com/en-us/answers/search.html?c=&f=&includeChildren=&q=ssrs+OR+reporting+services&redirect=search%2fsearch&sort=relevance&type=question+OR+idea+OR+kbentry+OR+answer+OR+topic+OR+user).
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
  * [ Find the product key for SQL Server Reporting Services - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/find-reporting-services-product-key-ssrs?source=recommendations)
Learn how to find the product key for SQL Server Reporting Services (SSRS) 2017 and 2019 so you can install your server in a production environment.
  * [ Install a Reporting Services 2016 native mode report server - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services-native-mode-report-server?source=recommendations)
See how to install Reporting Services in native mode. View steps for how to use the SQL Server installation wizard to install and configure the report server.
  * [ Install SQL Server Data Tools (SSDT) - SQL Server Data Tools (SSDT) ](https://learn.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?source=recommendations)
Learn about SQL Server Data Tools (SSDT). See how to install this database development tool set with Visual Studio 2019 and 2022.
  * [ Install Reporting Services 2016 at the Command Prompt - SSRS - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services-at-the-command-prompt?source=recommendations)
Install Reporting Services 2016 at the Command Prompt - SSRS
  * [ Files-only installation (Reporting Services) - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/files-only-installation-reporting-services?source=recommendations)
Files-Only Installation (Reporting Services)


Show 2 more
Module
[ Build reports for finance and operations apps - Training ](https://learn.microsoft.com/en-us/training/modules/build-reports-finance-operations/?source=recommendations)
Organizations have a lot of data. When an organization grows, its ability to provide context for all that data becomes increasingly crucial. Reports can organize data in a meaningful way. Finance and operations apps include reporting tools to help you create reports for your organizations, SQL Server Reporting Services (SSRS), Microsoft Power BI, and Microsoft Excel reports. You can use these reporting tools to visualize a data set in many ways, including as a tabular layout with collapsible tables and by u
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 06/13/2025


##  In this article
  1. [Prerequisites](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#prerequisites)
  2. [Install SSRS](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#install-ssrs)
  3. [Configure your report server](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#configure-your-report-server)
  4. [Windows service](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#windows-service)
  5. [Default URL reservations](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#default-url-reservations)
  6. [Firewall](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#firewall)
  7. [Configure other features](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#configure-other-features)
  8. [Related content](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17#related-content)


Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
##
Ask Learn
Preview
Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Freporting-services%2Finstall-windows%2Finstall-reporting-services%3Fview%3Dsql-server-ver17)
Theme
  * Light
  * Dark
  * High contrast


  * [AI Disclaimer](https://learn.microsoft.com/en-us/principles-for-ai-generated-content)
  * [Previous Versions](https://learn.microsoft.com/en-us/previous-versions/)
  * [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
  * [Contribute](https://learn.microsoft.com/en-us/contribute)
  * [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
  * [Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)
  * [Terms of Use](https://learn.microsoft.com/en-us/legal/termsofuse)
  * [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
  * © Microsoft 2026
