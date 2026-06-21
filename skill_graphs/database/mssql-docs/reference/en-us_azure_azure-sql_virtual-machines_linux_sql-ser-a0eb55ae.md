Version Azure SQL
  * [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql-db)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql-mi)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=fabricsql)
  * [SQL Server on Azure VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql-vm)


Search
Suggestions will filter as you type
  * [Azure SQL Documentation](https://learn.microsoft.com/en-us/azure/azure-sql/?view=azuresql)
  *     * [Documentation](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/?view=azuresql)
    * [What's new?](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql)
    *       *         * [About Linux SQL Server VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql)


Download PDF
Table of contents  Exit editor mode
  1. [ Learn ](https://learn.microsoft.com/en-us/?view=azuresql)
  2. [ Azure ](https://learn.microsoft.com/en-us/azure/?view=azuresql)
  3. [ Azure SQL ](https://learn.microsoft.com/en-us/azure/azure-sql/?view=azuresql)
  4. [ SQL Server on Azure Virtual Machines ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/?view=azuresql)


  1. [Learn](https://learn.microsoft.com/en-us/?view=azuresql)
  2. [Azure](https://learn.microsoft.com/en-us/azure/?view=azuresql)
  3. [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/?view=azuresql)
  4. [SQL Server on Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/?view=azuresql)


Ask Learn Ask Learn Focus mode
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql) or changing directories.
Access to this page requires authorization. You can try changing directories.
# Overview of SQL Server on Linux Azure Virtual Machines
Feedback
Summarize this article for me
##  In this article
  1. [Get started with SQL Server VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#get-started-with-sql-server-vms)
  2. [Installed packages](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#installed-packages)
  3. [Related products and services](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#related-products-and-services)
  4. [Related content](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#related-content)


**Applies to:** ![](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) [SQL Server on Azure VM](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide#applies-to)
Linux
  * [ Windows ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview?view=azuresql)
  * [ Linux ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql)


SQL Server on Azure Virtual Machines enables you to use full versions of SQL Server in the cloud without having to manage any on-premises hardware. SQL Server VMs also simplify licensing costs when you pay as you go.
Azure virtual machines run in many different [geographic regions](https://azure.microsoft.com/regions/) around the world. They also offer a variety of [machine sizes](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes). The virtual machine image gallery allows you to create a SQL Server VM with the right version, edition, and operating system. This makes virtual machines a good option for many different SQL Server workloads.
If you're new to Azure SQL, check out the _SQL Server on Azure VM Overview_ video from our in-depth [Azure SQL video series](https://learn.microsoft.com/en-us/shows/Azure-SQL-for-Beginners?WT.mc_id=azuresql4beg_azuresql-ch9-niner):
0sfast_forward
0sfast_rewind
Skip Ad
play_arrow0:00volume_up
fullscreenmore_vert
_closed_caption_disabled_ CaptionsOff _settings_ ResolutionAuto _language_ Language _picture_in_picture_alt_ Picture-in-PictureOff _cast_ Cast...Off _slow_motion_video_ Playback speed0x _control_camera_ Recenter _3d_rotation_ Toggle stereoscopic _cast_ Cast...
_arrow_back_ CaptionsOff _done_
_arrow_back_ ResolutionAuto _done_
_arrow_back_ Language
_arrow_back_ Playback speed0.5x0.75x1x1.25x1.5x1.75x2x
![Video preview image](https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-43a26814-60c4-482c-a05c-042b124b08c8/video4_960.jpg)Play videoPlay SQL Server on Azure VM Overview (4 of 61)
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#get-started-with-sql-server-vms)
## Get started with SQL Server VMs
To get started, choose a SQL Server virtual machine image with your required version, edition, and operating system. The following sections provide direct links to the Azure portal for the SQL Server virtual machine gallery images.
For more information about how to understand pricing for SQL Server images, see [the pricing page for Linux VMs running SQL Server](https://azure.microsoft.com/pricing/details/virtual-machines/linux/).
Expand table
Version | Operating system | Edition
---|---|---
**SQL Server 2022** | Ubuntu 20.04 LTS |
**SQL Server 2019** | Red Hat Enterprise Linux (RHEL) 8 |
**SQL Server 2019** | SUSE Linux Enterprise Server (SLES) v12 SP5 |
To see the available SQL Server virtual machine images for Windows, see [Overview of SQL Server on Azure Virtual Machines (Windows)](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#installed-packages)
## Installed packages
When you configure SQL Server on Linux, you install the Database Engine package and then several optional packages depending on your requirements. The Linux virtual machine images for SQL Server automatically install most packages for you. The following table shows which packages are installed for each distribution.
Expand table
Distribution | [Database Engine](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup) | [Tools](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools) | [SQL Server agent](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-sql-agent) | [Full-text search](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-full-text-search) | [SSIS](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-ssis) | [HA add-on](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-business-continuity-dr)
---|---|---|---|---|---|---
RHEL |  ![RHEL and database engine.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![RHEL and tools.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![RHEL and SQL Server agent.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![RHEL and full-text search.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![RHEL and SSIS.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![RHEL and HA add-on.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql)
SLES |  ![SLES and database engine.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![SLES and tools.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![SLES and SQL Server agent.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![SLES and full-text search.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![SLES and SSIS \(not supported\).](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/no-icon.svg?view=azuresql) |  ![SLES and HA add-on.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql)
Ubuntu |  ![Ubuntu and database engine.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![Ubuntu and tools.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![Ubuntu and SQL Server agent.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![Ubuntu and full-text search.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![Ubuntu and SSIS.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) |  ![Ubuntu and HA add-on.](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql)
SQL IaaS Agent extension for SQL Server on Azure Linux Virtual Machines is only available for Ubuntu Linux distribution.
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#related-products-and-services)
## Related products and services
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#linux-virtual-machines)
### Linux virtual machines
  * [Azure Virtual Machines overview](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/overview)


[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#storage)
### Storage
  * [Introduction to Microsoft Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction)


[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#networking)
### Networking
  * [Virtual Network overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
  * [IP addresses in Azure](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses)
  * [Create a Fully Qualified Domain Name in the Azure portal](https://learn.microsoft.com/en-us/azure/virtual-machines/create-fqdn)


[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#sql)
### SQL
  * [SQL Server on Linux documentation](https://learn.microsoft.com/en-us/sql/linux)
  * [Azure SQL Database comparison](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview?view=azuresql)


[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql#related-content)
## Related content
  * [Provision a Linux virtual machine running SQL Server in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-vm-create-portal-quickstart?view=azuresql)
  * [SQL Server on Azure Virtual Machines FAQ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/frequently-asked-questions-faq?view=azuresql)


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
  * [ Quickstart: Create a Linux SQL Server VM in Azure - SQL Server on Azure VMs ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-vm-create-portal-quickstart?source=recommendations)
This tutorial shows how to create a Linux SQL Server 2017 virtual machine in the Azure portal.
  * [ Overview of SQL Server on Azure Windows Virtual Machines - SQL Server on Azure VMs ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview?source=recommendations)
Learn how to run full editions of SQL Server on Azure Virtual Machines in the cloud without having to manage any on-premises hardware.


Learning path
[ Common Linux server configurations - Training ](https://learn.microsoft.com/en-us/training/paths/common-linux-server-configurations/?source=recommendations)
This learning path provides an overview for deploying common Linux server functions on Azure virtual machines. Learn how to deploy a SQL Server, a web application server using the MEAN stack, perform a database migration, and manage your IT operations with Azure Automanage.
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
* * *
  * Last updated on 09/26/2025


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql)
