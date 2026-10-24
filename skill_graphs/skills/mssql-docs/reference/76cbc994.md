# SQL Server Replication
Feedback
Summarize this article for me
##  In this article
  1. [What's new](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#whats-new)
  2. [Replication security](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#replication-security)
  3. [Publishing and Distribution](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#publishing-and-distribution)
  4. [Publications and Articles](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#publications-and-articles)
  5. [Manage Subscriptions](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#manage-subscriptions)
  6. [Synchronize Subscriptions](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#synchronize-subscriptions)
  7. [Administration](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#administration)
  8. [Monitor](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#monitor)

Show 4 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to) ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) [Azure SQL Managed Instance](https://learn.microsoft.com/en-us/sql/sql-server/sql-docs-navigation-guide?view=sql-server-ver17#applies-to)
Replication is a set of technologies for copying and distributing data and database objects from one database to another and then synchronizing between databases to maintain consistency. Use replication to distribute data to different locations and to remote or mobile users over local and wide area networks, dial-up connections, wireless connections, and the Internet.
Transactional replication is typically used in server-to-server scenarios that require high throughput, including: improving scalability and availability; data warehousing and reporting; integrating data from multiple sites; integrating heterogeneous data; and offloading batch processing. Merge replication is primarily designed for mobile applications or distributed server applications that have possible data conflicts. Common scenarios include: exchanging data with mobile users; consumer point of sale (POS) applications; and integration of data from multiple sites. Snapshot replication is used to provide the initial data set for transactional and merge replication; it can also be used when complete refreshes of data are appropriate. With these three types of replication, SQL Server provides a powerful and flexible system for synchronizing data across your enterprise. Replication to SQLCE 3.5 and SQLCE 4.0 is supported on both Windows Server 2012 and Windows 8.
[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#whats-new)
## What's new
  * SQL Server 2022 hasn't introduced significant new features to SQL Server replication.
  * SQL Server 2019 hasn't introduced significant new features to SQL Server replication.
  * SQL Server 2017 hasn't introduced significant new features to SQL Server replication.
  * SQL Server 2016 hasn't introduced significant new features to SQL Server replication.


For backward compatibility information see, [Replication Backward Compatibility](https://learn.microsoft.com/en-us/sql/relational-databases/replication/replication-backward-compatibility?view=sql-server-ver17)
[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#replication-security)
## Replication security
  * [View and Modify Replication Security Settings](https://learn.microsoft.com/en-us/sql/relational-databases/replication/security/view-and-modify-replication-security-settings?view=sql-server-ver17)
  * [Manage Logins in the Publication Access List](https://learn.microsoft.com/en-us/sql/relational-databases/replication/security/manage-logins-in-the-publication-access-list?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#publishing-and-distribution)
## Publishing and Distribution
  * [Configure Publishing and Distribution](https://learn.microsoft.com/en-us/sql/relational-databases/replication/configure-publishing-and-distribution?view=sql-server-ver17)
  * [View and Modify Publication Properties](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/view-and-modify-publication-properties?view=sql-server-ver17)
  * [Disable Publishing and Distribution](https://learn.microsoft.com/en-us/sql/relational-databases/replication/disable-publishing-and-distribution?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#publications-and-articles)
## Publications and Articles
  * [Create a Publication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/create-a-publication?view=sql-server-ver17)
  * [Define an Article](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/define-an-article?view=sql-server-ver17)
  * [View and Modify Publication Properties](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/view-and-modify-publication-properties?view=sql-server-ver17)
  * [View and Modify Article Properties](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/view-and-modify-article-properties?view=sql-server-ver17)
  * [Delete a Publication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/delete-a-publication?view=sql-server-ver17)
  * [Delete an Article](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/delete-an-article?view=sql-server-ver17)
  * [Create a Publication from an Oracle Database](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/create-a-publication-from-an-oracle-database?view=sql-server-ver17)
  * [Set the Expiration Period for Subscriptions](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/set-the-expiration-period-for-subscriptions?view=sql-server-ver17)
  * [Specify Schema Options](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/specify-schema-options?view=sql-server-ver17)
  * [Replicate Schema Changes](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/replicate-schema-changes?view=sql-server-ver17)
  * [Manage Identity Columns](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/manage-identity-columns?view=sql-server-ver17)
  * [Set the Compatibility Level for Merge Publications](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/set-the-compatibility-level-for-merge-publications?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#snapshot-options)
### Snapshot Options
  * [Configure Snapshot Properties](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/configure-snapshot-properties-replication-transact-sql-programming?view=sql-server-ver17)
  * [Deliver a Snapshot Through FTP](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/deliver-a-snapshot-through-ftp?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#filter-data)
### Filter Data
  * [Define and Modify a Column Filter](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/define-and-modify-a-column-filter?view=sql-server-ver17)
  * [Define and Modify a Static Row Filter](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/define-and-modify-a-static-row-filter?view=sql-server-ver17)
  * [Define and Modify a Parameterized Row Filter for a Merge Article](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/define-and-modify-a-parameterized-row-filter-for-a-merge-article?view=sql-server-ver17)
  * [Optimize Parameterized Row Filters](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/optimize-parameterized-row-filters?view=sql-server-ver17)
  * [Define and Modify a Join Filter Between Merge Articles](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/define-and-modify-a-join-filter-between-merge-articles?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#transactional-replication-options)
### Transactional Replication Options
  * [Set the Propagation Method for Data Changes to Transactional Articles](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/set-the-propagation-method-for-data-changes-to-transactional-articles?view=sql-server-ver17)
  * [Enable Updating Subscriptions for Transactional Publications](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/enable-updating-subscriptions-for-transactional-publications?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#merge-replication-options)
### Merge Replication Options
  * [Define a Logical Record Relationship Between Merge Table Articles](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/define-a-logical-record-relationship-between-merge-table-articles?view=sql-server-ver17)
  * [Specify Merge replication properties](https://learn.microsoft.com/en-us/sql/relational-databases/replication/merge/specify-merge-replication-properties?view=sql-server-ver17)
  * [Specify a Merge Article Resolver](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/specify-a-merge-article-resolver?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#manage-subscriptions)
## Manage Subscriptions
  * [Create a Pull Subscription](https://learn.microsoft.com/en-us/sql/relational-databases/replication/create-a-pull-subscription?view=sql-server-ver17)
  * [View and Modify Pull Subscription Properties](https://learn.microsoft.com/en-us/sql/relational-databases/replication/view-and-modify-pull-subscription-properties?view=sql-server-ver17)
  * [Delete a Pull Subscription](https://learn.microsoft.com/en-us/sql/relational-databases/replication/delete-a-pull-subscription?view=sql-server-ver17)
  * [Create a Push Subscription](https://learn.microsoft.com/en-us/sql/relational-databases/replication/create-a-push-subscription?view=sql-server-ver17)
  * [View and Modify Push Subscription Properties](https://learn.microsoft.com/en-us/sql/relational-databases/replication/view-and-modify-push-subscription-properties?view=sql-server-ver17)
  * [Delete a Push Subscription](https://learn.microsoft.com/en-us/sql/relational-databases/replication/delete-a-push-subscription?view=sql-server-ver17)
  * [Specify Synchronization Schedules](https://learn.microsoft.com/en-us/sql/relational-databases/replication/specify-synchronization-schedules?view=sql-server-ver17)
  * [Create an Updatable Subscription to a Transactional Publication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/create-an-updatable-subscription-to-a-transactional-publication?view=sql-server-ver17)
  * [Create a Subscription for a Non-SQL Server Subscriber](https://learn.microsoft.com/en-us/sql/relational-databases/replication/create-a-subscription-for-a-non-sql-server-subscriber?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#synchronize-subscriptions)
## Synchronize Subscriptions
  * [Create and Apply the Initial Snapshot](https://learn.microsoft.com/en-us/sql/relational-databases/replication/create-and-apply-the-initial-snapshot?view=sql-server-ver17)
  * [Create a Snapshot for a Merge Publication with Parameterized Filters](https://learn.microsoft.com/en-us/sql/relational-databases/replication/create-a-snapshot-for-a-merge-publication-with-parameterized-filters?view=sql-server-ver17)
  * [Initialize a Transactional Subscription from a Backup (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/initialize-a-transactional-subscription-from-a-backup?view=sql-server-ver17)
  * [Initialize a Subscription Manually](https://learn.microsoft.com/en-us/sql/relational-databases/replication/initialize-a-subscription-manually?view=sql-server-ver17)
  * [Synchronize a Pull Subscription](https://learn.microsoft.com/en-us/sql/relational-databases/replication/synchronize-a-pull-subscription?view=sql-server-ver17)
  * [Synchronize a Push Subscription](https://learn.microsoft.com/en-us/sql/relational-databases/replication/synchronize-a-push-subscription?view=sql-server-ver17)
  * [Reinitialize a Subscription](https://learn.microsoft.com/en-us/sql/relational-databases/replication/reinitialize-a-subscription?view=sql-server-ver17)
  * [Execute Scripts During Synchronization (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/execute-scripts-during-synchronization-replication-transact-sql-programming?view=sql-server-ver17)
  * [Implement a Business Logic Handler for a Merge Article](https://learn.microsoft.com/en-us/sql/relational-databases/replication/implement-a-business-logic-handler-for-a-merge-article?view=sql-server-ver17)
  * [Debug a Business Logic Handler (Replication Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/debug-a-business-logic-handler-replication-programming?view=sql-server-ver17)
  * [Control the Behavior of Triggers and Constraints During Synchronization (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/control-behavior-of-triggers-and-constraints-in-synchronization?view=sql-server-ver17)
  * [Implement a Custom Conflict Resolver for a Merge Article](https://learn.microsoft.com/en-us/sql/relational-databases/replication/implement-a-custom-conflict-resolver-for-a-merge-article?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#administration)
## Administration
  * [Work with Replication Agent Profiles](https://learn.microsoft.com/en-us/sql/relational-databases/replication/agents/work-with-replication-agent-profiles?view=sql-server-ver17)
  * [Validate Data at the Subscriber](https://learn.microsoft.com/en-us/sql/relational-databases/replication/validate-data-at-the-subscriber?view=sql-server-ver17)
  * [Manage Partitions for a Merge Publication with Parameterized Filters](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/manage-partitions-for-a-merge-publication-with-parameterized-filters?view=sql-server-ver17)
  * [Bulk-Load Data into Tables in a Merge Publication (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/bulk-load-data-into-tables-in-a-merge-publication?view=sql-server-ver17)
  * [Clean Up Merge Metadata (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/clean-up-merge-metadata-replication-transact-sql-programming?view=sql-server-ver17)
  * [Perform a Dummy Update for a Merge Article (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/perform-a-dummy-update-for-a-merge-article-replication-transact-sql-programming?view=sql-server-ver17)
  * [View Replicated Commands and Other Information in the Distribution Database (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/monitor/view-replicated-commands-and-information-in-distribution-database?view=sql-server-ver17)
  * [Enable Coordinated Backups for Transactional Replication (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/enable-coordinated-backups-for-transactional-replication?view=sql-server-ver17)
  * [Administer a Peer-to-Peer Topology (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/administer-a-peer-to-peer-topology-replication-transact-sql-programming?view=sql-server-ver17)
  * [Quiesce a Replication Topology (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/quiesce-a-replication-topology-replication-transact-sql-programming?view=sql-server-ver17)
  * [Configure the Transaction Set Job for an Oracle Publisher (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/configure-the-transaction-set-job-for-an-oracle-publisher?view=sql-server-ver17)
  * [Upgrade Replication Scripts (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/upgrade-replication-scripts-replication-transact-sql-programming?view=sql-server-ver17)


[](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#monitor)
## Monitor
  * [Allow Non-Administrators to Use Replication Monitor](https://learn.microsoft.com/en-us/sql/relational-databases/replication/monitor/allow-non-administrators-to-use-replication-monitor?view=sql-server-ver17)
  * [Programmatically Monitor Replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/monitor/programmatically-monitor-replication?view=sql-server-ver17)
  * [View Replicated Commands and Other Information in the Distribution Database (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/monitor/view-replicated-commands-and-information-in-distribution-database?view=sql-server-ver17)
  * [View Conflict Information for Merge Publications (Replication Transact-SQL Programming)](https://learn.microsoft.com/en-us/sql/relational-databases/replication/view-and-resolve-data-conflicts-for-merge-publications?view=sql-server-ver17)
  * [Measure Latency and Validate Connections for Transactional Replication](https://learn.microsoft.com/en-us/sql/relational-databases/replication/monitor/measure-latency-and-validate-connections-for-transactional-replication?view=sql-server-ver17)


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
  * [ Create a publication - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/create-a-publication?source=recommendations)
Learn how to create a publication in SQL Server by using SQL Server Management Studio, Transact-SQL, or Replication Management Objects.
  * [ Enable a database for Replication (SSMS) - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/enable-a-database-for-replication-sql-server-management-studio?source=recommendations)
Learn how to enable a database for Replication using SQL Server Management Studio (SSMS) or Transact-SQL (T-SQL).
  * [ Configure Publishing and Distribution - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/configure-publishing-and-distribution?source=recommendations)
Learn how to configure publishing and distribution in SQL Server by using SQL Server Management Studio, Transact-SQL, or Replication Management Objects.
  * [ Snapshot Replication - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/snapshot-replication?source=recommendations)
Snapshot replication distributes data as it appears at a moment in time. It doesn't monitor for updates. A snapshot is generated and sent to Subscribers.
  * [ View and Modify Replication Security Settings - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/security/view-and-modify-replication-security-settings?source=recommendations)
Learn how to view and modify replication security settings in SQL Server by using SQL Server Management Studio, Transact-SQL, or Replication Management Objects.
  * [ Replication Publishing Model Overview - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/publish/replication-publishing-model-overview?source=recommendations)
Learn about the replication publishing model in SQL Server, including Publisher, Distributor, Subscribers, publications, articles, and subscriptions.
  * [ Best Practices for Replication Administration - SQL Server ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/administration/best-practices-for-replication-administration?source=recommendations)
After you configure replication, use these best practices to administer your replication topology in SQL Server.


Show 4 more
Module
[ Configure replication and manage failovers in Azure Cosmos DB - Training ](https://learn.microsoft.com/en-us/training/modules/configure-replication-manage-failovers-azure-cosmos-db/?source=recommendations)
Configure replication and manage failovers in Azure Cosmos DB
Certification
[ Microsoft Certified: Azure Database Administrator Associate - Certifications ](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/?source=recommendations)
Administer an SQL Server database infrastructure for cloud, on-premises and hybrid relational databases using the Microsoft PaaS relational database offerings.
Mar 8, 4 PM - Mar 8, 4 PM
Experiment with what's next in AI-driven apps and agent design
* * *
  * Last updated on 09/29/2024


##  In this article
  1. [What's new](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#whats-new)
  2. [Replication security](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#replication-security)
  3. [Publishing and Distribution](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#publishing-and-distribution)
  4. [Publications and Articles](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#publications-and-articles)
  5. [Manage Subscriptions](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#manage-subscriptions)
  6. [Synchronize Subscriptions](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#synchronize-subscriptions)
  7. [Administration](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#administration)
  8. [Monitor](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17#monitor)


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
[ Sign in ](https://learn.microsoft.com/en-us/sql/relational-databases/replication/sql-server-replication?view=sql-server-ver17)
[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fsql%2Frelational-databases%2Freplication%2Fsql-server-replication%3Fview%3Dsql-server-ver17)
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
