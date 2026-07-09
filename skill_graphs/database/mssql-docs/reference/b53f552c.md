# Upgrade and migrate Reporting Services
Feedback
Summarize this article for me
##  In this article
  1. [Known upgrade issues and best practices](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_known_issues)
  2. [Side by side installations](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_side_by_side)
  3. [In-place upgrades](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_inplace_upgrade)
  4. [Pre-upgrade checklist](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_upgrade_checklist)
  5. [Overview of migration scenarios](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#overview-of-migration-scenarios)
  6. [Native mode upgrade and migration scenarios](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_native_scenarios)
  7. [Upgrade a Reporting Services Native mode scale-out deployment](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_native_scaleout)
  8. [Roll back a Reporting Services cumulative update](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#rollback_native)
  9. [SharePoint mode upgrade and migration scenarios](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_sharePoint_scenarios)
  10. [Considerations for a migration](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_migration_considerations)
  11. [Related content](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#related-content)

Show 7 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2016 (13.x) Reporting Services and later versions ![Not supported](https://learn.microsoft.com/en-us/sql/includes/media/no-icon.svg?view=sql-server-ver17) Power BI Report Server ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SharePoint
This article is an overview of the upgrade and migration options for SQL Server Reporting Services. Here are the general approaches to upgrading a SQL Server Reporting Services deployment:
  * **Upgrade _to_ Reporting Services 2016 and older _from_ Reporting Services 2016 and older:** You upgrade the Reporting Services components on the servers and instances where they're currently installed. This process is commonly called an "in place" upgrade. In-place upgrade isn't supported from one mode of Reporting Services server to another. For example, you can't upgrade a Native Mode report server to a SharePoint mode report server. You can migrate your report items from one mode to another. For more information, see the [SharePoint mode upgrade and migration scenarios](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_sharePoint_scenarios) section later in this document.
  * **Upgrade _to_ Reporting Services 2017 and later _from_ Reporting Services 2016 and older:** This upgrade scenario isn't the same as previous versions. When upgrading _to_ Reporting Services 2016 and older versions, you could follow an in-place upgrade process using SQL Server installation media. When upgrading _to_ Reporting Services 2017 and later _from_ Reporting Services 2016 and older, you can't follow the same steps because the new Reporting Services installation is a standalone product. It's no longer part of the SQL Server installation media.
To upgrade from Reporting Services 2016 and older versions to Reporting Services 2017 and later, follow the [Migrate a Reporting Services Installation (Native Mode)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/migrate-a-reporting-services-installation-native-mode?view=sql-server-ver17) article, with Reporting Services 2017 or later as your destination instance.
  * **Upgrade _from_ Reporting Services 2017 to future versions** is again an in-place upgrade scenario, because the product installation GUIDs are the same. Run the SQLServerReportingServices.exe installation file to begin the in-place upgrade on the server where Reporting Services is currently installed.
  * **Migrate** : You install and configure a new SharePoint environment, copy your report items and resources to the new environment, and configure the new environment to use existing content. A lower level form of migration is to copy the Reporting Services databases, configuration files, and if you're using SharePoint mode, the SharePoint content databases.


Reporting Services integration with SharePoint isn't available after SQL Server 2016.
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_known_issues)
##  Known upgrade issues and best practices
For a detailed list of the supported editions and versions you can upgrade, see [Supported version and edition upgrades](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/supported-version-and-edition-upgrades?view=sql-server-ver17).
For the latest information regarding issues with SQL Server, see [SQL Server 2016 release notes](https://learn.microsoft.com/en-us/sql/sql-server/sql-server-2016-release-notes?view=sql-server-ver17).
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_side_by_side)
##  Side by side installations
SQL Server Reporting Services Native mode can be installed side-by-side with a SQL Server 2012 (11.x) or SQL Server 2014 (12.x) Native mode deployment.
There's no support for side-by-side deployments of SQL Server Reporting Services in SharePoint mode and any previous versions of Reporting Services SharePoint mode components.
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_inplace_upgrade)
##  In-place upgrades
SQL Server Setup completes the upgrade. SQL Server Setup can be used to upgrade any or all SQL Server components, including Reporting Services. Setup detects the existing instances and prompts you to upgrade. SQL Server Setup provides upgrade options that you can specify as a command-line argument or in the Setup wizard.
When you run SQL Server Setup, you can select the option to upgrade from one of the following versions or you can install a new instance of SQL Server Reporting Services that runs side-by-side existing installations:
  * SQL Server 2014 (12.x)
  * SQL Server 2012 (11.x)
  * SQL Server 2008 R2 (10.50.x)
  * SQL Server 2008 (10.0.x)


For more information on SQL Server, see:
  * [Upgrade to SQL Server 2016](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server?view=sql-server-ver17)
  * [Upgrade to SQL Server 2016 Using the Installation Wizard (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server-using-the-installation-wizard-setup?view=sql-server-ver17)
  * [Install SQL Server 2016 from the Command Prompt](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server-from-the-command-prompt?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_upgrade_checklist)
##  Pre-upgrade checklist
Before upgrading to SQL Server Reporting Services:
  * Review requirements to determine whether your hardware and software can support SQL Server 2016 (13.x) Reporting Services or later (SSRS). For more information, see [Hardware and Software Requirements for Installing SQL Server 2016](https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server?view=sql-server-ver17).
  * Use System Configuration Checker (SCC) to scan the report server computer for any conditions that might prevent a successful installation of SQL Server Reporting Services. For more information, see [Check Parameters for the System Configuration Checker](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/check-parameters-for-the-system-configuration-checker?view=sql-server-ver17).
  * Review security best practices and guidance for SQL Server. For more information, see [Security Considerations for a SQL Server Installation](https://learn.microsoft.com/en-us/sql/sql-server/install/security-considerations-for-a-sql-server-installation?view=sql-server-ver17).
  * Back up your symmetric key. For more information, see [Back Up and Restore Reporting Services Encryption Keys](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/ssrs-encryption-keys-back-up-and-restore-encryption-keys?view=sql-server-ver17).
  * Back up your report server databases and configuration files. For more information, see [Backup and Restore Operations for Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/backup-and-restore-operations-for-reporting-services?view=sql-server-ver17).
  * Back up any customizations to existing Reporting Services virtual directories in IIS.
  * Remove invalid TLS/SSL certificates, including certificates that are expired and you don't plan to update before upgrading Reporting Services. Invalid certificates cause upgrades to fail and an error similar to the following message is written to the Reporting Services Log file: **Microsoft.ReportingServices.WmiProvider.WMIProviderException: A Secure Sockets Layer (SSL) certificate is not configured on the Web site.**.


Before you upgrade a production environment, always run a test upgrade in a preproduction environment that has the same configuration as your production environment.
These steps must be completed in full for a later rollback to be possible. Microsoft Support cannot recover backups, encryption keys, or configuration files that were not backed up.
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#overview-of-migration-scenarios)
## Overview of migration scenarios
If you're upgrading from a supported version of Reporting Services to SQL Server, you can usually run the SQL Server Setup Wizard to upgrade the report server program files, database, and all application data.
However, **migrating** a report server installation manually is required if you encounter any of the following conditions:
  * You want to change the type of report server used in your deployment. For example, you can't upgrade or convert a native mode report server to SharePoint mode. For more information, see [Native to SharePoint Migration (SSRS)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/native-to-sharepoint-migration-ssrs?view=sql-server-ver17).
  * You want to minimize the amount of time the report server is taken offline during the upgrade process. Your current installation remains online while you copy content data to a new report server instance and test the installation without changing the state of your existing report server installation.
  * You want to migrate a SharePoint 2010 deployment of Reporting Services to SharePoint 2013/2016. SharePoint 2013/2016 doesn't support in-place upgrade from SharePoint 2010. For more information, see [Migrate a Reporting Services Installation (SharePoint Mode)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/migrate-a-reporting-services-installation-sharepoint-mode?view=sql-server-ver17).


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_native_scenarios)
##  Native mode upgrade and migration scenarios
**Upgrade:** In-place upgrade for Native mode is the same process for each of the supported versions that are listed earlier in this article. Run the SQL Server installation wizard or a command line installation. Following installation, the report server database automatically upgrades to the new report server database schema. For more information, see [In-place Upgrade](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_inplace_upgrade) in this article.
The upgrade process begins when you select an existing report server instance to upgrade.
  1. If the report server database is on a remote computer and you don't have permission to update that database, Setup prompts you to provide credentials to update to a remote report server database. Be sure to provide credentials that have **sysadmin** or database update permissions.
  2. Setup checks for conditions or settings that prevent upgrade and reads configuration settings. Examples include custom extensions deployed on the report server. If upgrade is blocked, you must either modify your installation so that upgrade is no longer blocked, or migrate to a new SQL Server Reporting Services instance. For more information, see the Upgrade Advisor documentation.
  3. If upgrade can proceed, Setup prompts you to continue with the upgrade process.
  4. Setup creates new folders for SQL Server Reporting Services program files. The program folders for a Reporting Services installation include MSRS13.<_instance name_ >.
  5. Setup adds the SQL Server Reporting Services report server program files, configuration tools, and command line utilities that are part of the report server feature.
    1. Program files from the previous version are removed.
    2. Report server configuration tools and utilities that are upgraded to the new version include the Native Mode Reporting Services Configuration tool, command line utilities such as RS.exe, and Report Builder.
    3. Other client tools such as SQL Server Management Studio are a separate download and need to be upgraded separately. Install the latest version of [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/install/install).
    4. SQL Server Data Tools (SSDT) is a separate download. For more information, see [SQL Server Data Tools in Visual Studio 2015](https://learn.microsoft.com/en-us/previous-versions/mt186501\(v=msdn.10\)).
  6. Setup reuses the service entry in Service Control Manager for the SQL Server Reporting Services Report Server service. This service entry includes the Report Server Windows service account.
  7. Setup reserves new URLs based on existing virtual directory settings in IIS. Setup might not remove virtual directories in IIS, so be sure to remove those directories manually after upgrade is finished.
  8. Setup merges settings in the configuration files. Setup uses the configuration files from the current installation as the basis to add new entries. Obsolete entries aren't removed, but they're no longer be read by the report server after the upgrade is finished. An upgrade doesn't delete old log files, the obsolete RSWebApplication.config file, or virtual directory settings in IIS. An upgrade doesn't remove older versions of Report Designer, Management Studio, or other client tools. If you no longer require them, remove these files and tools after the upgrade is finished.


**Migration:** Migrating a previous version of a native mode installation to SQL Server Reporting Services is the same steps for all of the supported versions that are listed earlier in this article. For more information, see [Migrate a Reporting Services Installation (Native Mode)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/migrate-a-reporting-services-installation-native-mode?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_native_scaleout)
##  Upgrade a Reporting Services Native mode scale-out deployment
The following summary explains how to upgrade a Reporting Services Native mode deployment that is scaled-out to more than one report server. This process requires downtime of the Reporting Services deployment:
  1. Back up the report server databases and encryption keys. For more information, see [Backup and Restore Operations for Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/backup-and-restore-operations-for-reporting-services?view=sql-server-ver17) and [Add and Remove Encryption Keys for Scale-Out Deployment (Report Server Configuration Manager)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/add-and-remove-encryption-keys-for-scale-out-deployment?view=sql-server-ver17).
  2. Use the Reporting Services Configuration Manager and remove all of the report servers from the scaled-out deployment. For more information, see [Configure a Native Mode Report Server Scale-Out Deployment (Report Server Configuration Manager)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/configure-a-native-mode-report-server-scale-out-deployment?view=sql-server-ver17).
  3. Upgrade one of the report servers to SQL Server Reporting Services.
  4. Use the Reporting Services Configuration Manager to add the report servers back to the scale-out deployment. For more information, see [Configure a Native Mode Report Server Scale-Out Deployment (Report Server Configuration Manager)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/configure-a-native-mode-report-server-scale-out-deployment?view=sql-server-ver17).
For each server, repeat the upgrade and Scale-out steps.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#rollback_native)
##  Roll back a Reporting Services cumulative update
Cumulative Updates in Reporting Services versions 2017 and later support in-place upgrade but can't be selectively uninstalled. To roll back an upgrade, you must uninstall the entire service and reinstall the prior version:
These steps require that the pre-upgrade checklist has been followed completely. Step 2 will render existing configuration files, service configurations, and encryption keys irrecoverable. Microsoft Support cannot recover these configuration files or decrypt these encryption keys to assist in rollback.
  1. Take note of any custom configurations including service credentials, email or file share settings, or report server URLs.
  2. Uninstall SQL Server Reporting Services. In a scale-out deployment, repeat for all nodes in the scale-out. For more information, see [Uninstall Native Mode](https://learn.microsoft.com/en-us/sql/sql-server/install/uninstall-reporting-services?view=sql-server-ver17).
  3. Restore backups of ReportServer database. For more information, see [Backup and Restore Operations for Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/backup-and-restore-operations-for-reporting-services?view=sql-server-ver17).
  4. Reinstall the prior update of SQL Server Reporting Services.
  5. Restore preupgrade configuration files.
  6. Restore the encryption key backup. For more information, see [Back Up and Restore Encryption Keys](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/ssrs-encryption-keys-back-up-and-restore-encryption-keys?view=sql-server-ver17).
  7. Recreate all of the custom configurations noted in step 1.
  8. In a scale-out deployment, repeat steps 4 through 7 for all other nodes in the scale-out deployment.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_sharePoint_scenarios)
##  SharePoint mode upgrade and migration scenarios
The following sections describe the issues and basic steps needed to upgrade or migrate from specified versions of Reporting Services SharePoint mode to SQL Server Reporting Services Reporting Services SharePoint mode.
There are two installation components to upgrade a Reporting Services SharePoint Mode deployment.
  * Reporting Services SharePoint Shared Service.
Use the Reporting Services SharePoint cmdlet `Get-SPRSServiceApplicationServers` to determine servers in the SharePoint farm that are currently running the Reporting Services SharePoint Shared Service and therefore require an upgrade.
  * Reporting Services Add-in for SharePoint products. For more information, see [Install or Uninstall the Reporting Services Add-in for SharePoint](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-or-uninstall-the-reporting-services-add-in-for-sharepoint?view=sql-server-ver17).


For detailed steps on Migrating a SharePoint mode installation, see [Migrate a Reporting Services Installation (SharePoint Mode)](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/migrate-a-reporting-services-installation-sharepoint-mode?view=sql-server-ver17).
Some of the following scenarios require down time of the SharePoint environment due to the different technologies that need to be upgraded. If your situation does not allow for down time, you will need to complete a migration instead of an in-place upgrade.
[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#-to-sql-server-reporting-services)
### SQL Server 2014 (12.x) to SQL Server Reporting Services
**Starting environment:** SQL Server 2014 (12.x) or SQL Server 2014 (12.x) SP1, SharePoint 2010, or SharePoint 2013.
**Ending environment:** SQL Server Reporting Services, SharePoint 2013, or SharePoint 2016.
  * **SharePoint 2013/2016:** SharePoint 2013/2016 doesn't support in-place upgrade from SharePoint 2010. However the procedure of **database-attach upgrade** is supported.
If you have a Reporting Services installation integrated with SharePoint 2010, you can't upgrade in-place the SharePoint server. However you can migrate content databases and service application databases from the SharePoint 2010 farm to a SharePoint 2013/2016 farm.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#-to-sql-server-reporting-services-1)
### SQL Server 2012 (11.x) to SQL Server Reporting Services
**Starting environment:** SQL Server 2012 (11.x) or SQL Server 2012 SP1 (11.0.3x), SharePoint 2010.
**Ending environment:** SQL Server Reporting Services, SharePoint 2013, or SharePoint 2016.
  * **SharePoint 2013/2016:** SharePoint 2013/2016 doesn't support in-place upgrade from SharePoint 2010. However the procedure of **database-attach upgrade** is supported.
If you have a Reporting Services installation integrated with SharePoint 2010, you can't upgrade in-place the SharePoint server. However you can migrate content databases and service application databases from the SharePoint 2010 farm to a SharePoint 2013/2016 farm.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#-to-sql-server-reporting-services-2)
### SQL Server 2008 R2 (10.50.x) to SQL Server Reporting Services
**Starting environment:** SQL Server 2008 R2 (10.50.x), SharePoint 2010.
**Ending environment:** SQL Server Reporting Services, SharePoint 2013, or SharePoint 2016.
  * **SharePoint 2013/2016:** SharePoint 2013/2016 doesn't support in-place upgrade from SharePoint 2010. However the procedure of **database-attach upgrade** is supported.
SharePoint must be migrated first before you can upgrade Reporting Services.
  * Install the SQL Server Reporting Services version of the Reporting Services add-in for SharePoint on each web front-end in the farm. You can install the add-in by using the SQL Server Reporting Services installation wizard or by downloading the add-in.
  * Run SQL Server Reporting Services installation to upgrade SharePoint mode for each 'report server'. The SQL Server installation wizard installs the Reporting Services Service and creates a new Service application.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_migration_considerations)
##  Considerations for a migration
When moving application data, you should be aware of the following concerns and restrictions:
  * Protection of encryption key includes a hash that incorporates machine identity.
  * Report server database names are fixed and can't be renamed on new computer.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#encryption-key-considerations)
### Encryption key considerations
Always back up the encryption keys before moving a report server database to a new computer.
Moving a report server installation to another computer invalidates the hash that protects the encryption keys used to help secure sensitive data stored in the report server database. Each report server instance that uses the database has its copy of the encryption key, which is encrypted with the identity of the service account as it is defined on the current computer. If you change computers, the service no longer has access to its key, even if you use the same account name on the new computer.
To re-establish reversible encryption on the new report server computer, you must restore the key that you previously backed up. The complete key set that is stored in the report server database consists of a symmetric key value, plus service identity information used to restrict access to the key so only the report server instance that stored it can use it. During key restoration, the report server replaces existing copies of the key with new versions. The new version includes machine and service identity values as defined on the current computer. For more information, see:
  * SharePoint mode: See the "Key Management" section of [Manage a Reporting Services SharePoint Service Application](https://learn.microsoft.com/en-us/sql/reporting-services/report-server-sharepoint/manage-a-reporting-services-sharepoint-service-application?view=sql-server-ver17)
  * Native Mode: See [Back Up and Restore Reporting Services Encryption Keys](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/ssrs-encryption-keys-back-up-and-restore-encryption-keys?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#fixed-database-name)
### Fixed database name
You can't rename the report server database. The identity of the database is recorded in report server stored procedures when the database is created. Renaming either the report server primary or temporary databases cause errors when the procedures run, invalidating your report server installation.
If the database name from the existing installation isn't suited for the new installation, consider creating a new database that has the name that you prefer. Then load existing application data using the techniques in the following list:
  * Write a Visual Basic script that calls Report Server Web service SOAP methods to copy data between databases. You can use the RS.exe utility to run the script. For more information about this approach, see [Scripting and PowerShell with Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/tools/scripting-and-powershell-with-reporting-services?view=sql-server-ver17).
  * Write code that calls the WMI provider to copy data between databases. For more information about this approach, see [Access the Reporting Services WMI Provider](https://learn.microsoft.com/en-us/sql/reporting-services/tools/access-the-reporting-services-wmi-provider?view=sql-server-ver17).
  * If you have just a few items, you can republish reports, and shared data sources from Report Designer, Model Designer, and Report Builder to the new report server. You must re-create role assignments, subscriptions, shared schedules, report snapshot schedules, custom properties that you set on reports or other items, model item security, and properties that you set on the report server. You lose report history and report execution log data.


[](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#related-content)
## Related content
  * [Overview of the upgrade process to SharePoint 2016](https://technet.microsoft.com/library/cc262483\(v=office.16\))
  * [Overview of the upgrade process to SharePoint 2013](https://learn.microsoft.com/en-us/SharePoint/upgrade-and-update/overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013)
  * [Clean up preparations before an upgrade to SharePoint 2013](https://learn.microsoft.com/en-us/SharePoint/upgrade-and-update/clean-up-an-environment-before-an-upgrade-to-sharepoint-2013)
  * [Upgrade databases from SharePoint 2013 to SharePoint 2016](https://technet.microsoft.com/library/cc303436\(v=office.16\))
  * [Upgrade databases from SharePoint 2010 to SharePoint 2013](https://learn.microsoft.com/en-us/SharePoint/upgrade-and-update/upgrade-content-databases-from-sharepoint-2010-to-sharepoint-2013)
  * [Upgrade Reports](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-reports?view=sql-server-ver17)
  * [Upgrade to SQL Server 2016 Using the Installation Wizard (Setup)](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server-using-the-installation-wizard-setup?view=sql-server-ver17)
  * [Reporting Services forum](https://learn.microsoft.com/en-us/answers/search.html?c=&f=&includeChildren=&q=ssrs+OR+reporting+services&redirect=search%2fsearch&sort=relevance&type=question+OR+idea+OR+kbentry+OR+answer+OR+topic+OR+user)


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
  * [ Migrate a Reporting Services Installation (Native Mode) - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/migrate-a-reporting-services-installation-native-mode?source=recommendations)
Learn how to migrate a supported version of Reporting Services Installation native mode deployment to a new SQL Server Reporting Services instance.
  * [ Upgrade a Report Server Database - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-a-report-server-database?source=recommendations)
Upgrade a Report Server Database
  * [ Backup and restore operations for Reporting Services - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/backup-and-restore-operations-for-reporting-services?source=recommendations)
Backup and Restore Operations for Reporting Services
  * [ Move report server databases to another computer (native mode) - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/report-server/moving-the-report-server-databases-to-another-computer-ssrs-native-mode?source=recommendations)
Find out how to move report server databases to a different SQL Server instance. See how to attach and detach the databases or use backup and restore actions.
  * [ Release notes for Reporting Services 2017 and later - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/release-notes-reporting-services?source=recommendations)
Learn details about the changes in SQL Server Reporting Services (SSRS), for versions 2017 and later.
  * [ Back up and restore SQL Server Reporting Services (SSRS) encryption keys - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/ssrs-encryption-keys-back-up-and-restore-encryption-keys?source=recommendations)
Learn how to back up and restore SSRS encryption keys by using Report Server Configuration Manager.
  * [ SQL Server Reporting Services Features Supported by Editions - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/reporting-services-features-supported-by-the-editions-of-sql-server-2016?source=recommendations)
Learn about SQL Server Reporting Services (SSRS) features supported by the different editions of SQL Server.
  * [ Upgrade Reports - SQL Server Reporting Services (SSRS) ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-reports?source=recommendations)
Upgrade Reports (SSRS)


Show 5 more
Module
[ Migrate SQL Server workloads to Azure Virtual Machine - Training ](https://learn.microsoft.com/en-us/training/modules/migrate-sql-workloads-azure-virtual-machines/?source=recommendations)
Discover the tools and features available to migrate SQL workloads from on-premises to Azure Virtual Machines (VMs).
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 09/27/2024


##  In this article
  1. [Known upgrade issues and best practices](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_known_issues)
  2. [Side by side installations](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_side_by_side)
  3. [In-place upgrades](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_inplace_upgrade)
  4. [Pre-upgrade checklist](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_upgrade_checklist)
  5. [Overview of migration scenarios](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#overview-of-migration-scenarios)
  6. [Native mode upgrade and migration scenarios](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_native_scenarios)
  7. [Upgrade a Reporting Services Native mode scale-out deployment](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_native_scaleout)
  8. [Roll back a Reporting Services cumulative update](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#rollback_native)
  9. [SharePoint mode upgrade and migration scenarios](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_sharePoint_scenarios)
  10. [Considerations for a migration](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#bkmk_migration_considerations)
  11. [Related content](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17#related-content)

Show 2 more
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
[ Sign in ](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/upgrade-and-migrate-reporting-services?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Freporting-services%2Finstall-windows%2Fupgrade-and-migrate-reporting-services%3Fview%3Dsql-server-ver17)
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
