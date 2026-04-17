# What is SQL Server Reporting Services (SSRS)?
Feedback
Summarize this article for me
##  In this article
  1. [Create, deploy, and manage reports](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#create-deploy-and-manage-reports)
  2. [Paginated reports](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#paginated-reports)
  3. [Web portal](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#web-portal)
  4. [Reporting Services programming features](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#-programming-features)
  5. [Related content](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2016 (13.x) Reporting Services and later versions ![Not supported](https://learn.microsoft.com/en-us/sql/includes/media/no-icon.svg?view=sql-server-ver17) Power BI Report Server
Starting in SQL Server 2025 (17.x), on-premises reporting services is consolidated under [Power BI Report Server](https://learn.microsoft.com/en-us/power-bi/report-server/get-started). For more information, see [Reporting Services consolidation FAQ](https://learn.microsoft.com/en-us/sql/reporting-services/reporting-services-consolidation-faq?view=sql-server-ver17).
SQL Server Reporting Services (SSRS) provides a set of on-premises tools and services to create, deploy, and manage paginated reports. Download [**SQL Server 2022 Reporting Services**](https://www.microsoft.com/download/details.aspx?id=104502) from the Microsoft Download Center, and then [install Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver17).
![Screenshot of a SQL Server 2022 Reporting Services report.](https://learn.microsoft.com/en-us/sql/reporting-services/media/report-server-2022-coho-winery.png?view=sql-server-ver17)
Looking for Power BI Report Server? See [What is Power BI Report Server?](https://learn.microsoft.com/en-us/power-bi/report-server/get-started)
[](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#create-deploy-and-manage-reports)
## Create, deploy, and manage reports
SSRS makes it easy to deliver the right information to the right users. You can view reports in a web browser on your computer, mobile device, or receive them via email.
SSRS offers an updated suite of products:
  * **Paginated reports** : Create modern-looking reports with updated tools and new features.
  * **A modern web portal** : Organize and display paginated Reporting Services reports and KPIs in any modern browser. Store Excel workbooks on the portal as well.


  * **Mobile reports** : Create reports with responsive layouts that adapt to different devices and orientations.


[](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#paginated-reports)
## Paginated reports
![Diagram of paginated reports on a desktop screen and a tablet device.](https://learn.microsoft.com/en-us/sql/reporting-services/media/ssrs-paginated-reports.png?view=sql-server-ver17)
Paginated reports are perfect for fixed-layout documents optimized for printing, such as PDFs and Word files. You can create innovative reports with newly updated features, by using [Report Builder](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-report-builder?view=sql-server-ver17), or [Report Designer](https://learn.microsoft.com/en-us/sql/reporting-services/tools/design-reporting-services-paginated-reports-with-report-designer-ssrs?view=sql-server-ver17) in [SQL Server Data Tools (SSDT)](https://learn.microsoft.com/en-us/sql/reporting-services/tools/reporting-services-in-sql-server-data-tools-ssdt?view=sql-server-ver17). We updated the core BI workload with:
  * **New styles and color palettes** : Create reports with a fresh, minimalist style by default.
  * **Updated Parameter pane** : Arrange parameters exactly the way you want them.
  * **Export to new formats** : Export reports to PowerPoint with live, editable visualizations.
  * **Hybrid Power BI/SSRS experience** : Pin visuals from SSRS reports to your Power BI dashboards and monitor everything in one place.


[](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#mobile-reports)
## Mobile reports
![Diagram of mobile reports on a desktop screen and a tablet device.](https://learn.microsoft.com/en-us/sql/reporting-services/media/ssrs-mobile-reports.png?view=sql-server-ver17)
Mobile computing transforms how we work, creating new reporting needs. Fixed-layout reports don't work well on tablets and phones. They're designed for wide PC screens, not small, portrait, or landscape screens.
To meet these demands, mobile reports have responsive layouts that adapt to different devices and orientations. Based on Datazen technology, these reports ensure your data looks great no matter where you view it. You can even migrate existing Datazen reports to Reporting Services with the [SQL Server Migration Assistant for Datazen](https://www.microsoft.com/download/details.aspx?id=53128).
Create these mobile reports with the [Mobile Report Publisher](https://learn.microsoft.com/en-us/sql/reporting-services/mobile-reports/create-mobile-reports-with-sql-server-mobile-report-publisher?view=sql-server-ver17) app. Whether you're on Windows, iOS, Android, or HTML5, you can access your data in Power BI, the cloud, or SSRS through the [Power BI apps for mobile devices](https://powerbi.microsoft.com/documentation/powerbi-power-bi-apps-for-mobile-devices/).
As you build your visualizations, Mobile Report Publisher automatically generates sample data, so you can see exactly how your data looks and which types of data work best in each visualization.
[](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#web-portal)
## Web portal
![Screenshot of the Reporting Services web portal.](https://learn.microsoft.com/en-us/sql/reporting-services/media/report-server-2022-web-portal.png?view=sql-server-ver17)
For Reporting Services, the front door is a modern web portal. The web portal is a complete redesign of Report Manager. Now, you can access all your Reporting Services reports and KPIs in the new portal. KPIs can surface key business metrics immediately in the browser without opening a report.
The web portal is a sleek, single-page, standards-based HTML5 app that works with all major browsers, including Microsoft Edge, Internet Explorer 10 and 11, Chrome, Firefox, and Safari. Access your SSRS reports and KPIs in one place. The content on the web portal is organized by type:
  * Paginated reports
  * KPIs
  * Excel workbooks
  * Shared datasets
  * Shared data sources


  * Mobile reports


Store and manage your content securely the traditional folder hierarchy. Tag your favorite reports for quick access. Those users with appropriate permissions can manage and administer SSRS content. Schedule report processing, access reports on demand, and subscribe to published reports
To learn more, see [The web portal of a report server - SSRS Native mode](https://learn.microsoft.com/en-us/sql/reporting-services/web-portal-ssrs-native-mode?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#reporting-services-in-sharepoint-integrated-mode)
## Reporting Services in SharePoint integrated mode
You can publish your reports with Reporting Services in SharePoint integrated mode. Schedule report processing, access reports on demand, subscribe to published reports, and export them to applications like Microsoft Excel. You can also create data alerts on reports published to a SharePoint site and receive email notifications when report data changes.
To learn more, see [Reporting Services report server in SharePoint integrated mode](https://learn.microsoft.com/en-us/sql/reporting-services/report-server-sharepoint/reporting-services-report-server-sharepoint-mode?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#-programming-features)
## Reporting Services programming features
Extend and customize your reporting functionality with Reporting Services programming features. Use the SSRS APIs to integrate or extend data and report processing in your custom applications.
To learn more, see [Reporting Services developer documentation](https://learn.microsoft.com/en-us/sql/reporting-services/reporting-services-developer-documentation?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#related-content)
## Related content
  * [What's new in Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/what-s-new-in-sql-server-reporting-services-ssrs?view=sql-server-ver17)
  * [Try asking the Reporting Services forum](https://learn.microsoft.com/en-us/answers/search.html?c=&f=&includeChildren=&q=ssrs+OR+reporting+services&redirect=search%2fsearch&sort=relevance&type=question+OR+idea+OR+kbentry+OR+answer+OR+topic+OR+user)


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
  * [ Reporting Services Reports - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/reports/reporting-services-reports-ssrs?source=recommendations)
Learn details about Reporting Services reports, including the benefits of the reports, how to create paginated reports, and how to view reports.
  * [ SQL Server Reporting Services tools - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/tools/reporting-services-tools?source=recommendations)
Find out about the tools for development, configuration, administration, and report viewing that are available in SQL Server Reporting Services.
  * [ Reporting Services concepts - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/reporting-services-concepts-ssrs?source=recommendations)
Learn about SQL Server Reporting Services (SSRS) concepts, including scheduling reports, roles and permissions, and report subscriptions and delivery.
  * [ What's New in SQL Server Reporting Services (SSRS) - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/what-s-new-in-sql-server-reporting-services-ssrs?source=recommendations)
Learn about what's new in the different versions of SQL Server Reporting Services (SSRS), including changes to the major feature areas.
  * [ Reporting Services in SQL Server Data Tools (SSDT) - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/tools/reporting-services-in-sql-server-data-tools-ssdt?source=recommendations)
See how to use the SQL Server Data Tools Report Designer authoring environment in Microsoft Visual Studio to create solutions for Reporting Services.
  * [ Reporting Services features and tasks - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/reporting-services-features-and-tasks-ssrs?source=recommendations)
Learn how to access Reporting Services foundational content organized by reports and report features, report server features, and Reporting Services product features.
  * [ Design Reporting Services paginated reports with Report Designer (SSRS) - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/tools/design-reporting-services-paginated-reports-with-report-designer-ssrs?source=recommendations)
See how to use Report Designer in SQL Server Reporting Services to create full-featured paginated reports and reporting solutions.
  * [ Intro to Report Data in SQL Server Reporting Services (SSRS) - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/report-data/report-data-ssrs?source=recommendations)
Learn introductory information about report data in SQL Server Reporting Services (SRRS), such as how to create data sources.


Show 5 more
Module
[ Build reports for finance and operations apps - Training ](https://learn.microsoft.com/en-us/training/modules/build-reports-finance-operations/?source=recommendations)
Organizations have a lot of data. When an organization grows, its ability to provide context for all that data becomes increasingly crucial. Reports can organize data in a meaningful way. Finance and operations apps include reporting tools to help you create reports for your organizations, SQL Server Reporting Services (SSRS), Microsoft Power BI, and Microsoft Excel reports. You can use these reporting tools to visualize a data set in many ways, including as a tabular layout with collapsible tables and by u
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 06/16/2025


##  In this article
  1. [Create, deploy, and manage reports](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#create-deploy-and-manage-reports)
  2. [Paginated reports](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#paginated-reports)
  3. [Web portal](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#web-portal)
  4. [Reporting Services programming features](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#-programming-features)
  5. [Related content](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17#related-content)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Freporting-services%2Fcreate-deploy-and-manage-mobile-and-paginated-reports%3Fview%3Dsql-server-ver17)
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
