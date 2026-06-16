# chown mysql:mysql /var/lib/mysql/test/address_book.*
```

5. Lastly, import the new tablespace:

```sql
ALTER TABLE test.address_book IMPORT TABLESPACE;
```

MariaDB Community Server looks in the data directory for the tablespace you copied in, then imports it for use. If the table is encrypted, it also looks for the encryption key with the relevant key ID that the table data specifies.

6. Repeat this step for every table you wish to restore.

### Partial Restore Partitioned Tables

Restoring a partitioned table from a backup requires a few extra steps compared to restoring a non-partitioned table.

To restore a partitioned table from a backup, first create a new table on MariaDB Community Server to receive the restored data. It should match the specifications of the table you're restoring, including the partition specification.

Be extra careful if the backup data is from a server with a different version than the restore server, as some differences (such as a differing ROW\_FORMAT) can cause an unexpected result.

1. Create an empty table for the data being restored:

```sql
CREATE TABLE test.students (
   id INT PRIMARY KEY AUTO_INCREMENT
   name VARCHAR(255),
   email VARCHAR(255),
   graduating_year YEAR)
PARTITION BY RANGE (graduating_year) (
   PARTITION p9 VALUES LESS THAN 2019
   PARTITION p1 VALUES LESS THAN MAXVALUE
);
```

2. Then create a second empty table matching the column specification, but without partitions. This is your working table:

```sql
CREATE TABLE test.students_work AS
SELECT * FROM test.students WHERE NULL;
```

3. For each partition you want to restore, discard the working table's tablespace:

```sql
ALTER TABLE test.students_work DISCARD TABLESPACE;
```

4. Then, copy the table files from the backup, using the new name:

```bash
