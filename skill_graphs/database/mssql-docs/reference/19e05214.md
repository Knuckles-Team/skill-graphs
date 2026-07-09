# What is SQL Server on Linux?
Feedback
Summarize this article for me
##  In this article
  1. [Install](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#install)
  2. [Connect](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#connect)
  3. [Explore](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#explore)
  4. [Get help](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#-get-help)
  5. [Contribute to SQL documentation](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#-contribute-to-sql-documentation)


**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) on Linux
SQL Server runs on Linux, starting with SQL Server 2017 (14.x). It's the same SQL Server Database Engine, with many similar features and services regardless of your operating system.
[](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#install)
## Install
To get started, install SQL Server on Linux using one of the following quickstarts:
  * [Quickstart: Install SQL Server and create a database on Red Hat Enterprise Linux](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-red-hat?view=sql-server-ver17)
  * [Quickstart: Install SQL Server and create a database on SUSE Linux Enterprise Server](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-suse?view=sql-server-ver17)
  * [Quickstart: Install SQL Server and create a database on Ubuntu](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver17)
  * [Quickstart: Run SQL Server Linux container images with Docker](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver17)
  * [Provision a SQL VM in Azure](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-vm-create-portal-quickstart?toc=/sql/toc/toc.json)


Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.
[](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#container-images)
### Container images
The SQL Server container images are published and available on the Microsoft Container Registry (MCR), and also cataloged at the following locations, based on the operating system image that was used when creating the container image:
  * For both RHEL and Ubuntu based SQL Server container images, see [SQL Server on the Microsoft Artifact Registry](https://mcr.microsoft.com/catalog?cat=Databases).
  * For RHEL-based SQL Server container images, see


Containers will only be published to MCR for the _most recent_ Linux distributions. If you create your own custom SQL Server container image for an older supported distribution, it will still be supported. For more information, see [Upcoming updates to SQL Server container images on Microsoft Artifact Registry aka (MCR)](https://techcommunity.microsoft.com/blog/sqlserver/upcoming-updates-to-sql-server-container-images-on-microsoft-artifact-registry-a/3573013).
[](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#connect)
## Connect
After installation, connect to the SQL Server instance on your Linux machine. You can connect locally or remotely and with various tools and drivers. The quickstarts demonstrate how to use the [sqlcmd](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver17) command-line tool. Other tools include the following:
Expand table
Tool | Tutorial
---|---
Visual Studio Code (VS Code) | [SQL Server extension for Visual Studio Code](https://learn.microsoft.com/en-us/sql/tools/visual-studio-code-extensions/mssql/connect-database-visual-studio-code?view=sql-server-ver17)
SQL Server Management Studio (SSMS) | [Use SQL Server Management Studio on Windows to manage SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-manage-ssms?view=sql-server-ver17)
SQL Server Data Tools (SSDT) | [Use Visual Studio to create databases for SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-develop-use-ssdt?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#explore)
## Explore
Starting with SQL Server 2017 (14.x), SQL Server has the same underlying Database Engine on all supported platforms, including Linux and containers. Therefore, many existing features and capabilities operate the same way. This area of the documentation exposes some of these features from a Linux perspective. It also calls out areas that have unique requirements on Linux.
If you're already familiar with SQL Server on Linux, review the release notes for general guidelines and known issues for this release:
  * [Release notes for SQL Server 2025 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-release-notes-2025?view=sql-server-ver17)
  * [Release notes for SQL Server 2022 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-release-notes-2022?view=sql-server-ver17)
  * [Release notes for SQL Server 2019 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-release-notes-2019?view=sql-server-ver17)
  * [Release notes for SQL Server 2017 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-release-notes-2017?view=sql-server-ver17)


To find out more about each release, see:
  * [What's new for SQL Server 2025 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-whats-new-2025?view=sql-server-ver17)
  * [What's new for SQL Server 2022 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-whats-new-2022?view=sql-server-ver17)
  * [What's new for SQL Server 2019 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-whats-new-2019?view=sql-server-ver17)
  * [What's new for SQL Server 2017 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-whats-new?view=sql-server-ver17)


To see what's new in each version for Windows, see:
  * [What's new in SQL Server 2025](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17)
  * [What's new in SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?view=sql-server-ver17)
  * [What's new in SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2019?view=sql-server-ver17)
  * [What's new in SQL Server 2017](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2017?view=sql-server-ver17)


For answers to frequently asked questions, see the [SQL Server on Linux FAQ](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-faq?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#-get-help)
##  ![](https://learn.microsoft.com/en-us/sql/includes/media/info-tip.svg?view=sql-server-ver17) Get help
  * [Microsoft Q & A (SQL Server)](https://learn.microsoft.com/en-us/answers/products/sql-server)
  * [Microsoft SQL Server License Terms and Information](https://www.microsoft.com/licensing/product-licensing/sql-server)
  * [Support options for business users](https://support.microsoft.com/support-for-business)
  * [Additional SQL Server help and feedback](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-get-help?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#-contribute-to-sql-documentation)
##  ![](https://learn.microsoft.com/en-us/sql/includes/media/edit-topic-pencil.svg?view=sql-server-ver17) Contribute to SQL documentation
Did you know that you can edit SQL content yourself? If you do so, not only do you help improve our documentation, but you also get credited as a contributor to the page.
For more information, see [Edit Microsoft Learn documentation](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-docs-contribute?view=sql-server-ver17).
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
  * [ Release Notes for SQL Server 2025 on Linux - SQL Server ](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-release-notes-2025?source=recommendations)
This article contains the release notes and supported features for SQL Server 2025 running on Linux. Release notes include the most recent release and several previous releases.
  * [ SUSE: Install SQL Server on Linux - SQL Server ](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-suse?source=recommendations)
This quickstart shows how to install SQL Server on SUSE Linux Enterprise Server and then create and query a database with sqlcmd.
  * [ Ubuntu: Install SQL Server on Linux - SQL Server ](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?source=recommendations)
This quickstart shows how to install SQL Server 2017 and later versions on Ubuntu and then create and query a database with sqlcmd.
  * [ Get Started with SQL Server (On Linux) in the Cloud - SQL Server ](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-clouds?source=recommendations)
Learn how to install SQL Server on Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), or Ubuntu in the cloud of your choice.
  * [ Use SSMS to Manage SQL Server on Linux - SQL Server ](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-manage-ssms?source=recommendations)
This article introduces SQL Server Management Studio, an integrated environment to access, configure, manage, administer, and develop components of SQL Server.
  * [ Install on SQL Server 2022 for Linux - SQL Server Machine Learning Services ](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-machine-learning-sql-2022?source=recommendations)
Learn how to install SQL Server 2022 Machine Learning Services on Linux: Red Hat, Ubuntu, and SUSE.
  * [ Installation Guidance for SQL Server on Linux - SQL Server ](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup?source=recommendations)
Install, update, and uninstall SQL Server on Linux. This article covers online, offline, and unattended scenarios.
  * [ RHEL: Install SQL Server on Linux - SQL Server ](https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-red-hat?source=recommendations)
This quickstart shows how to install SQL Server on Red Hat Enterprise Linux (RHEL) and then create and query a database with sqlcmd.


Show 5 more
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 01/02/2026


##  In this article
  1. [Install](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#install)
  2. [Connect](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#connect)
  3. [Explore](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#explore)
  4. [Get help](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#-get-help)
  5. [Contribute to SQL documentation](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17#-contribute-to-sql-documentation)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Flinux%2Fsql-server-linux-overview%3Fview%3Dsql-server-ver17)
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
