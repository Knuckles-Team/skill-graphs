## SQL Server Analysis Services
SQL Server Analysis Services doesn't run on a failover cluster when configured using a local account. Analysis Services must be configured using a domain account.
If you use a local account on a failover cluster, you see the following error in the Windows Event Viewer:
Output
Copy
```
Server Gen2 cryptokey is not present, but server assembly object System is set to use server gen2 cryptokey. Terminating server.

```

For specific updates, see [What's new in SQL Server Analysis Services](https://learn.microsoft.com/en-us/analysis-services/what-s-new-in-sql-server-analysis-services).
[](https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025?view=sql-server-ver17#power-bi-report-server)
