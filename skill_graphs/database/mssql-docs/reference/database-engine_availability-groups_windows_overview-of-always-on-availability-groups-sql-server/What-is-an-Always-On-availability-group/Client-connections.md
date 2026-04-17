## Client connections
You can provide client connectivity to the primary replica of a given availability group by creating an availability group listener. An _availability group listener_ provides a set of resources that is attached to a given availability group to direct client connections to the appropriate availability replica.
An availability group listener is associated with a unique DNS name that serves as a virtual network name (VNN), one or more virtual IP addresses (VIPs), and a TCP port number. For more information, see [Connect to an Always On availability group listener](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/listeners-client-connectivity-application-failover?view=sql-server-ver17).
If an availability group has only two availability replicas and isn't configured to allow read-access to the secondary replica, clients can connect to the primary replica by using a [database mirroring connection string](https://learn.microsoft.com/en-us/sql/database-engine/database-mirroring/connect-clients-to-a-database-mirroring-session-sql-server?view=sql-server-ver17). This approach can be useful temporarily after you migrate a database from database mirroring to Always On availability groups. Before you add secondary replicas, you need to create an availability group listener for the availability group and update your applications to use the network name of the listener.
[](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17#tds-8-support-in-sql-server-2025)
### TDS 8 support in SQL Server 2025
SQL Server 2025 (17.x) introduces TDS 8.0 support, which allows enforcing strict [TLS 1.3](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/tls-1-3?view=sql-server-ver17) encryption for connections to your Always On availability group replicas and listener.
**Configuration requirements** :
  * **New availability groups** : Create the AG with `Encrypt=Strict` in the `CLUSTER_CONNECTION_OPTIONS` clause and failover to apply settings.
  * **Existing availability groups** : Alter the AG with `CLUSTER_CONNECTION_OPTIONS` clause to set `Encrypt=Strict` and failover to apply settings.
  * **Force Strict Encryption** : Set this option to **Yes** in SQL Server Configuration Manager for each replica and restart SQL Server replicas.
  * **Certificate requirements** : When `Encrypt=Strict` is set, `TrustServerCertificate` is ignored.


To get started, review [Connect with strict encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/connect-with-strict-encryption?view=sql-server-ver17#connect-to-an-always-on-availability-group).
[](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17#active-secondary-replicas)
