## Collation in Microsoft Fabric
In Microsoft Fabric Data Warehouse, the only collations allowed are: `Latin1_General_100_BIN2_UTF8` and `Latin1_General_100_CI_AS_KS_WS_SC_UTF8`.
In SQL database in Microsoft Fabric, by default the collation is `SQL_Latin1_General_CP1_CI_AS` and currently can't be updated. Collations on individual columns are supported.
[](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver17#utf-8-support)
