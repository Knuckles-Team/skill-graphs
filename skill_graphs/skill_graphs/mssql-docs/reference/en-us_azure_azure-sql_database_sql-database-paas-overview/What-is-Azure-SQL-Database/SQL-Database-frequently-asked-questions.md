## SQL Database frequently asked questions
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#can-i-control-when-patching-downtime-occurs)
### Can I control when patching downtime occurs?
The [maintenance window feature](https://learn.microsoft.com/en-us/azure/azure-sql/database/maintenance-window?view=azuresql) allows you to configure predictable maintenance window schedules for eligible databases in Azure SQL Database. [Maintenance window advance notifications](https://learn.microsoft.com/en-us/azure/azure-sql/database/advance-notifications?view=azuresql) are available for databases configured to use a nondefault [maintenance window](https://learn.microsoft.com/en-us/azure/azure-sql/database/maintenance-window?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#how-do-i-plan-for-maintenance-events)
### How do I plan for maintenance events?
Patching is generally not noticeable if you [employ retry logic](https://learn.microsoft.com/en-us/azure/azure-sql/database/develop-overview?view=azuresql#resiliency) in your app. For more information, see [Planning for Azure maintenance events in Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/planned-maintenance?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#can-i-access-my-backups)
### Can I access my backups?
Azure SQL Database backups are managed automatically. No one has direct access to the backups. The backups are deleted once the configured retention period expires. For more information, see [Automated backups in Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview?view=azuresql) and [Long-term retention](https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview?view=azuresql).
[](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql#engage-with-the-sql-server-engineering-team)
