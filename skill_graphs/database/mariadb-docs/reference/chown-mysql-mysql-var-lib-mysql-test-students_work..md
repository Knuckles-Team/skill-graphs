# chown mysql:mysql /var/lib/mysql/test/students_work.*
```

6. Import the copied tablespace:

```sql
ALTER TABLE test.students_work IMPORT TABLESPACE;
```

7. Lastly, exchange the partition, copying the tablespace from the working table into the partition file for the target table:

```sql
ALTER TABLE test.students EXCHANGE PARTITION p0 WITH TABLE test.students_work;
```

8. Repeat the above process for each partition until you have them all exchanged into the target table. Then delete the working table, as it's no longer necessary:

```sql
DROP TABLE test.students_work;
```

This restores a partitioned table.

### Partial Restore of Tables with Full-Text Indexes

When restoring a table with a full-text search (FTS) index, InnoDB may throw a schema mismatch error.

In this case, to restore the table, it is recommended to:

* Remove the corresponding .cfg file.
* Restore data to a table without any secondary indexes including FTS.
* Add the necessary secondary indexes to the restored table.

For example, to restore table t1 with FTS index from database db1:

1. In the MariaDB shell, drop the table you are going to restore:

```sql
DROP TABLE IF EXISTS db1.t1;
```

2. Create an empty table for the data being restored:

```sql
CREATE TABLE db1.t1(f1 CHAR(10)) ENGINE=INNODB;
```

3. Modify the table to discard the tablespace:

```sql
ALTER TABLE db1.t1 DISCARD TABLESPACE;
```

4. In the operating system shell, copy the table files from the backup to the data directory of the corresponding database:

```bash
$ sudo cp /data/backups/part/db1/t1.* /var/lib/mysql/db1
```

5. Remove the .cfg file from the data directory:

```bash
$ sudo rm /var/lib/mysql/db1/t1.cfg
```

6. Change the owner of the newly copied files to the system user running MariaDB Community Server:

```bash
$ sudo chown mysql:mysql /var/lib/mysql/db1/t1.*
```

7. In the MariaDB shell, import the copied tablespace:

```sql
ALTER TABLE db1.t1 IMPORT TABLESPACE;
```

8. Verify that the data has been successfully restored:

```sql
SELECT * FROM db1.t1;
```

```
+--------+
| f1     |
+--------+
| ABC123 |
+--------+
```

9. Add the necessary secondary indexes:

```sql
ALTER TABLE db1.t1 FORCE, ADD FULLTEXT INDEX f_idx(f1);
```

10. The table is now fully restored:

```sql
SHOW CREATE TABLE db1.t1\G
```

```
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `f1` char(10) DEFAULT NULL,
  FULLTEXT KEY `f_idx` (`f1`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

## Point-in-Time Recoveries

Point-in-time recovery (PITR) is [documented here](/docs/server/server-usage/backup-and-restore/mariadb-backup/point-in-time-recovery-pitr-mariadb-backup).

<sub>*This page is: Copyright © 2025 MariaDB. All rights reserved.*</sub>

{% @marketo/form formId="4316" %}
