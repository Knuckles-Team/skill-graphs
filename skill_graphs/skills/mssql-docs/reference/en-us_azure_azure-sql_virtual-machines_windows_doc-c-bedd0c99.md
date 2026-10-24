Version Azure SQL
  * [Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql)
  * [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql-db)
  * [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql-mi)
  * [Fabric SQL database](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=fabricsql)
  * [SQL Server on Azure VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql-vm)


Search
Suggestions will filter as you type
  * [Azure SQL Documentation](https://learn.microsoft.com/en-us/azure/azure-sql/?view=azuresql)
  *     * [Documentation](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/?view=azuresql)
    * [What's new?](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql)


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
Table of contents [ Read in English ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql) Add to Collections Add to plan
* * *
#### Share via
* * *
Copy Markdown Print
* * *
Note
Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql) or changing directories.
Access to this page requires authorization. You can try changing directories.
# What's new with SQL Server on Azure Virtual Machines?
Feedback
Summarize this article for me
##  In this article
  1. [Preview](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#preview)
  2. [General availability (GA)](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#general-availability-ga)
  3. [Documentation changes](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#documentation-changes)
  4. [Archive](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#archive)
  5. [Contribute to content](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#contribute-to-content)
  6. [Additional resources](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#additional-resources)

Show 2 more
**Applies to:** ![](https://learn.microsoft.com/en-us/azure/azure-sql/media/applies-to/yes-icon.svg?view=azuresql) [SQL Server on Azure VM](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide#applies-to)
SQL Server on Azure VMs
  * [ Azure SQL Database ](https://learn.microsoft.com/en-us/azure/azure-sql/database/doc-changes-updates-release-notes-whats-new?view=azuresql&preserve-view=true)
  * [ Azure SQL Managed Instance ](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/doc-changes-updates-release-notes-whats-new?view=azuresql&preserve-view=true)
  * [ SQL Server on Azure VMs ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql&preserve-view=true)


When you deploy an Azure virtual machine (VM) with SQL Server installed on it, either manually, or through a built-in image, you can use Azure features to improve your experience. This article summarizes the documentation changes associated with new features and improvements in the recent releases of [SQL Server on Azure Virtual Machines (VMs)](https://azure.microsoft.com/services/virtual-machines/sql-server/). To learn more about SQL Server on Azure VMs, see the [overview](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview?view=azuresql).
For updates made in previous years, see the [What's new archive](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new-archive?view=azuresql).
Placing `tempdb` on the local temp disk for Azure VM images with uninitialized ephemeral disks, such as the **FXmdsv2** , isn't supported. This issue only affects Azure Virtual Machines with the new NVMe interface that also has local ephemeral storage. These deployments through the Azure portal might fail, and SQL Server can fail to start. Either use a different VM series, or place `tempdb` on non-ephemeral storage both when you deploy the SQL Server image through the Azure portal, and when you install SQL Server manually. To learn more more about the issue and also see a list of impacted VMs, review [VM deployment and SQL Server failures](https://learn.microsoft.com/en-us/troubleshoot/sql/azure-sql/sql-deployment-fails-drive-not-ready).
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#preview)
## Preview
The following table lists the features of SQL Server on Azure VMs that are currently in preview.
Features currently in preview are available under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/), review for legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability. SQL Server on Azure VMs provide previews to give you a chance to evaluate and
Expand table
Feature | Details
---|---
[Modernization Advisor](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/modernization-advisor?view=azuresql) | Use the Modernization Advisor in the Azure portal to help you determine if migrating to Azure SQL Managed Instance saves you money or optimizes performance.
[Premium SSD v2 in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/storage-configuration-premium-ssd-v2?view=azuresql) | Deploy your SQL Server on Azure VM with Premium SSD v2 disks in the Azure portal for improved throughput and performance.
[VM vCore customization](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/vm-vcore-customization-for-sql?view=azuresql) | Customize the number of vCPUs presented to the guest OS for SQL Server workloads with configurable constrained cores (CCC), and disable Simultaneous Multithreading (SMT). This capability allows you to appropriately size the vCPU count to match your SQL Server licensing needs while preserving the VM's memory and I/O capabilities.
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#general-availability-ga)
## General availability (GA)
The following table lists features of SQL Server on Azure VMs that have been made generally available (GA) within the last 12 months:
Expand table
Changes | Month | Details
---|---|---
[I/O Analysis](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/storage-performance-analysis?view=azuresql) | April 2025 | Use the Azure portal to identify performance issues with your SQL Server workloads from exceeding virtual machine and data disk limits.
[Azure Elastic SAN](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/storage-configuration-azure-elastic-san?view=azuresql) | March 2025 | Place your SQL Server workloads on an Azure Elastic SAN for improved performance, throughput, and cost.
[FCI with Azure Elastic SAN](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-azure-elastic-san-manually-configure?view=azuresql) | March 2025 | Deploy your SQL Server failover cluster instance (FCI) by using an Azure Elastic SAN.
[Managed identity support for SQL Server 2022 on Azure VM](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/managed-identity-extensible-key-management?view=azuresql) | January 2025 | Starting with SQL Server 2022 Cumulative Update 17 (CU17), managed identities are supported for SQL Server on Azure VMs (Windows only). Managed identities can be used with [SQL Server credentials](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-credential-transact-sql) to [back up to and restore SQL Server on Azure VM databases from Azure Blob storage](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/backup-restore-to-url-using-managed-identities?view=azuresql). Support for managed identities also enables functionalities like [Extensible Key Management (EKM) with Azure Key Vault (AKV) and Managed Hardware Security Modules (HSM)](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/managed-identity-extensible-key-management?view=azuresql) to be used with SQL Server on Azure VMs.
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#documentation-changes)
## Documentation changes
Learn about significant changes to the SQL Server on Azure VMs documentation. For previous years, see the [What's new archive](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new-archive?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#january-2026)
### January 2026
Expand table
Changes | Details
---|---
**VM vCore customization for SQL Server on Azure VMs preview** | You can now customize the number of vCPUs presented to the guest OS for SQL Server workloads with configurable constrained cores (CCC), and disable Simultaneous Multithreading (SMT). This capability allows you to appropriately size the vCPU count to match your SQL Server licensing needs while preserving the VM's memory and I/O capabilities. This feature is now in preview. For more information, see [VM vCore customization for SQL Server on Azure VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/vm-vcore-customization-for-sql?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#september-2025)
### September 2025
Expand table
Changes | Details
---|---
**New Azure SQL hub** | Choosing the right Azure SQL service can be challenging. To make this easier, we built the
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#archive)
## Archive
For updates made in previous years, see the [What's new archive](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new-archive?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#contribute-to-content)
## Contribute to content
To contribute to the Azure SQL documentation, see the [Docs contributor guide](https://learn.microsoft.com/en-us/contribute/).
[](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql#additional-resources)
## Additional resources
**Windows VMs** :
  * [Overview of SQL Server on Windows VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview?view=azuresql)
  * [Provision SQL Server on Windows VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/create-sql-vm-portal?view=azuresql)
  * [Migration guide: SQL Server to SQL Server on Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/migration-guides/virtual-machines/sql-server-to-sql-on-azure-vm-individual-databases-guide?view=azuresql)
  * [High availability and disaster recovery for SQL Server on Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/business-continuity-high-availability-disaster-recovery-hadr-overview?view=azuresql)
  * [Performance best practices for SQL Server on Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/performance-guidelines-best-practices-checklist?view=azuresql)
  * [Application patterns and development strategies for SQL Server on Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/application-patterns-development-strategies?view=azuresql)


**Linux VMs** :
  * [Overview of SQL Server on a Linux VM](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-server-on-linux-vm-what-is-iaas-overview?view=azuresql)
  * [Provision SQL Server on a Linux virtual machine](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/sql-vm-create-portal-quickstart?view=azuresql)
  * [FAQ (Linux)](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/linux/frequently-asked-questions-faq?view=azuresql)
  * [SQL Server on Linux documentation](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview)


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
  * [ Overview of SQL Server on Azure Windows Virtual Machines - SQL Server on Azure VMs ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/sql-server-on-azure-vm-iaas-what-is-overview?source=recommendations)
Learn how to run full editions of SQL Server on Azure Virtual Machines in the cloud without having to manage any on-premises hardware.
  * [ Modernization Advisor (Preview) - SQL Server on Azure VMs ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/modernization-advisor?source=recommendations)
This article explains the Modernization Advisor, which helps you assess whether Azure SQL Managed Instance is a more cost-effective option for your business than SQL Server on Azure VMs.
  * [ What is Azure SQL Managed Instance? - Azure SQL Managed Instance ](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?source=recommendations)
Learn about how Azure SQL Managed Instance provides near 100% compatibility with the latest SQL Server (Enterprise Edition) database engine.
  * [ Create SQL Server VM with PowerShell script - SQL Server on Azure VMs ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/scripts/create-sql-vm-powershell?source=recommendations)
This article provides an end-to-end Azure PowerShell sample script to create SQL Server on Azure VMs.
  * [ Migrating SQL Server Workloads FAQ - Azure SQL ](https://learn.microsoft.com/en-us/azure/azure-sql/migration-guides/modernization?source=recommendations)
Frequently Asked Questions about migrating from SQL Server to Azure SQL, and modernizing the data platform
  * [ What Is Azure SQL? - Azure SQL ](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview?source=recommendations)
Learn about the different options within the Azure SQL family of services: Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure VM.


Show 3 more
Learning path
[ Explore SQL Server 2025 capabilities - Training ](https://learn.microsoft.com/en-us/training/paths/explore-sql-server-2022-capabilities/?source=recommendations)
Explore SQL Server 2025 capabilities
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
* * *
  * Last updated on 03/03/2026


Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.
Please sign in to use Ask Learn.
[ Sign in ](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/doc-changes-updates-release-notes-whats-new?view=azuresql)
