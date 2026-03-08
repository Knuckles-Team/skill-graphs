##  In this article
  1. [SQL Server scenarios that use availability features](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#sql-server-scenarios-that-use-availability-features)
  2. [High availability](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#high-availability)
  3. [Disaster recovery](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#disaster-recovery)
  4. [Migrations and upgrades](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#migrations-and-upgrades)
  5. [Read-scale](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#read-scale)
  6. [Cross-platform and Linux distribution interoperability](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#cross-platform-and-linux-distribution-interoperability)
  7. [Distributed availability groups](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#distributed-availability-groups)
  8. [Log shipping](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#log-shipping)
  9. [Summary](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#summary)
  10. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#related-content)

Show 6 more
**Applies to:** ![](https://learn.microsoft.com/en-us/sql/includes/media/yes-icon.svg?view=sql-server-ver17) SQL Server 2016 (13.x) and later versions
This article provides an overview of business continuity solutions for high availability and disaster recovery in SQL Server, on Windows and Linux.
Everyone who deploys SQL Server needs to make sure that all mission critical SQL Server instances and the databases within them are available when the business and end users need them, whether that availability is during regular business hours or around the clock. The goal is to keep the business up and running with minimal or no interruption. This concept is also known as _business continuity_.
SQL Server 2017 (14.x) and later versions introduced features and enhancements for availability. The biggest addition is support for SQL Server on Linux distributions. For a full list of the new features in SQL Server, see the following articles:
Expand table
Version | Operating system
---|---
What's new in SQL Server 2025 (17.x) |  [Windows](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17) | [Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-whats-new-2025?view=sql-server-ver17)
What's new in SQL Server 2022 (16.x) |  [Windows](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022?view=sql-server-ver17) | [Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-whats-new-2022?view=sql-server-ver17)
What's new in SQL Server 2019 (15.x) |  [Windows](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2019?view=sql-server-ver17) | [Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-whats-new-2019?view=sql-server-ver17)
What's new in SQL Server 2017 (14.x) |  [Windows](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2017?view=sql-server-ver17) | [Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-whats-new?view=sql-server-ver17)
This article focuses on the availability scenarios in SQL Server 2017 (14.x) and later versions, as well as the new and enhanced availability features. The scenarios include hybrid ones that can span SQL Server deployments on both Windows Server and Linux, and ones that can increase the number of readable copies of a database.
While this article doesn't cover availability options external to SQL Server (such as virtualization), everything discussed here applies to SQL Server installations inside a guest virtual machine whether in the public cloud or hosted by an on-premises hypervisor server.
[](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#sql-server-scenarios-that-use-availability-features)
##  In this article
  1. [SQL Server scenarios that use availability features](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#sql-server-scenarios-that-use-availability-features)
  2. [High availability](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#high-availability)
  3. [Disaster recovery](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#disaster-recovery)
  4. [Migrations and upgrades](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#migrations-and-upgrades)
  5. [Read-scale](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#read-scale)
  6. [Cross-platform and Linux distribution interoperability](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#cross-platform-and-linux-distribution-interoperability)
  7. [Distributed availability groups](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#distributed-availability-groups)
  8. [Log shipping](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#log-shipping)
  9. [Summary](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#summary)
  10. [Related content](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#related-content)


Was this page helpful?
Yes No No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn Ask Learn
Suggest a fix?
