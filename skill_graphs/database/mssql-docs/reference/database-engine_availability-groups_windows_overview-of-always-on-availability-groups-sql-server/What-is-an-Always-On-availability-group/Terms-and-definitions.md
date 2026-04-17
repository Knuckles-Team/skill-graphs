## Terms and definitions
Expand table
Term | Description
---|---
**availability group** | A container for a set of databases, _availability databases_ , that fail over together.
**availability database** | A database that belongs to an availability group. For each availability database, the availability group maintains a single read-write copy (the _primary database_) and one to eight read-only copies (_secondary databases_).
**primary database** | The read-write copy of an availability database.
**secondary database** | A read-only copy of an availability database.
**availability replica** | An instantiation of an availability group that a specific instance of SQL Server hosts and maintains a local copy of each availability database that belongs to the availability group. Two types of availability replicas exist: a single _primary replica_ and one to eight _secondary replicas_.
**primary replica** | The availability replica that makes the primary databases available for read-write connections from clients and, also, sends transaction log records for each primary database to every secondary replica.
**secondary replica** | An availability replica that maintains a secondary copy of each availability database, and serves as a potential failover targets for the availability group. Optionally, a secondary replica can support read-only access to secondary databases can support creating backups on secondary databases.
**availability group listener** | A server name to which clients can connect in order to access a database in a primary or secondary replica of an availability group. Availability group listeners direct incoming connections to the primary replica or to a read-only secondary replica.
[](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver17#availability-databases)
