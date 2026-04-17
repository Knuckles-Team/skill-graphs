## Cross-platform and Linux distribution interoperability
With SQL Server support on both Windows Server and Linux, this section covers how they can work together for availability in addition to other purposes. It also covers the story for solutions that incorporate more than one Linux distribution.
There are no scenarios where a WSFC-based failover cluster instance (FCI) or availability group (AG) works with a Linux-based FCI or AG directly. A Windows Server Failover Cluster (WSFC) can't be extended by a Pacemaker node and vice versa.
[](https://learn.microsoft.com/en-us/sql/database-engine/sql-server-business-continuity-dr?view=sql-server-ver17#distributed-availability-groups)
