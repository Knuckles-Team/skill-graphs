mariabackup: Stopping log copying thread.
```

Originally, `mariadb-backup` could wait indefinitely for the lock. Starting with the fix for MDEV-20230:

* The `--ftwrl-wait-timeout` option also ensures mariadb backup exits gracefully if the lock cannot be obtained within the timeout period.
* This prevents backups from hanging when lock acquisition is blocked by long-running queries.

**When to Use**

Use `--ftwrl-wait-timeout` when:

* Your workload includes long-running queries (for example, `ALTER TABLE` or large `INSERT` batches).
* Backups sometimes fail with lock wait timeout errors.
* You want `mariadb-backup` to either wait longer for the lock or exit cleanly if it cannot be obtained.

### `--galera-info`

Defines whether you want to back up information about a Galera Cluster node's state.

When this option is used, mariadb-backup creates an additional file called `xtrabackup_galera_info`, which records information about a Galera Cluster node's state. It records the values of the [wsrep\_local\_state\_uuid](/docs/galera-cluster/reference/galera-cluster-status-variables#wsrep_local_state_uuid) and [wsrep\_last\_committed](/docs/galera-cluster/reference/galera-cluster-status-variables#wsrep_last_committed) status variables.

You should only use this option when backing up a Galera Cluster node. If the server is not a Galera Cluster node, then this option has no effect.

This option, when enabled and used with GTID replication, will rotate the binary logs at backup time.

```bash
mariadb-backup --backup --galera-info
```

### `--history`

{% tabs %}
{% tab title="Current" %}
Defines whether you want to track backup history in the `mysql.mariadb_backup_history` table.

```
--history[=name]
```

When using this option, `mariadb-backup` records its operation in a table on the MariaDB Server. Passing a name to this option allows you group backups under arbitrary terms for later processing and analysis.

```bash
mariadb-backup --backup --history=backup_all
```

Information is written to `mysql.mariadb_backup_history`.

`mariadb-backup` also records this in the [mariadb\_backup\_info](/docs/server/server-usage/backup-and-restore/mariadb-backup/files-created-by-mariadb-backup#mariadb_backup_info) file.
{% endtab %}

{% tab title="< 10.11" %}
Defines whether you want to track backup history in the `PERCONA_SCHEMA.xtrabackup_history` table.

```
--history[=name]
```

When using this option, `mariadb-backup` records its operation in a table on the MariaDB Server. Passing a name to this option allows you group backups under arbitrary terms for later processing and analysis.

```bash
mariadb-backup --backup --history=backup_all
```

Information is written to `PERCONA_SCHEMA.xtrabackup_history`.

`mariadb-backup` also records this in the [xtrabackup\_info](/docs/server/server-usage/backup-and-restore/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_info) file.
{% endtab %}
{% endtabs %}

### `-H, --host`

Defines the hostname for the MariaDB Server you want to back up.

```bash
--host=name_or_ip-address
```

This option defines the hostname or IP address to use when **connecting to a local MariaDB Server over TCP/IP**. By default, `mariadb-backup` attempts to connect to `localhost`.

{% hint style="warning" %}
**The mariadb-backup client cannot create backups from a remote server.** Therefore, this option does not allow you to back up a remote server. `mariadb-backup` must always be run on the same server where the database files reside. The `--host` option is used only to establish the client connection for managing locks and retrieving metadata. The actual data files are always read from the local filesystem. Attempting to use this option to back up a remote host results in a backup of the local machine's data, associated with the remote machine's binary log coordinates.
{% endhint %}

```bash
mariadb-backup --backup \
      --host="192.168.0.33"
```

### `--include`

This option is a regular expression to be matched against table names in *`databasename.tablename`* format. It is equivalent to the `--tables` option. This is only valid in `innobackupex` mode, which can be enabled with the `--innobackupex` option.

### `--incremental`

Defines whether you want to take an increment backup, based on another backup. This is only valid in `innobackupex` mode, which can be enabled with the `--innobackupex` option.

```bash
mariadb-backup --innobackupex --incremental
```

Using this option with the `--backup` option makes the operation incremental rather than a complete overwrite. When this option is specified, either the `--incremental-lsn` or `--incremental-basedir` options can also be given. If neither option is given, `--incremental-basedir` is used by default, set to the first timestamped backup directory in the backup base directory.

```bash
mariadb-backup --innobackupex --backup --incremental \
     --incremental-basedir=/data/backups \
     --target-dir=/data/backups
```

If a backup is a incremental backup, then `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--incremental-basedir`

Defines whether you want to take an incremental backup, based on another backup.

```
--incremental-basedir=PATH
```

Using this option with the `--backup` option makes the operation incremental rather than a complete overwrite. `mariadb-backup` only copies pages from `.ibd` files if they are newer than the backup in the specified directory.

```bash
mariadb-backup --backup \
     --incremental-basedir=/data/backups \
     --target-dir=/data/backups
```

If a backup is a incremental backup, then `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--incremental-dir`

Defines whether you want to take an incremental backup, based on another backup.

```
--increment-dir=PATH
```

Using this option with `--prepare` command option makes the operation incremental rather than a complete overwrite. mariadb-backup will apply `.delta` files and log files into the target directory.

```bash
mariadb-backup --prepare \
      --increment-dir=backups/
```

If a backup is a incremental backup, then `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--incremental-force-scan`

Defines whether you want to force a full scan for incremental backups.

When using `mariadb-backup` to perform an incremental backup, this option forces it to also perform a full scan of the data pages being backed up, even when there's bitmap data on the changes. MariaDB does not support changed page bitmaps, so this option is useless in those versions. See [MDEV-18985](https://jira.mariadb.org/browse/MDEV-18985) for more information.

```bash
mariadb-backup --backup \
     --incremental-basedir=/path/to/target \
     --incremental-force-scan
```

### `--incremental-history-name`

Defines a logical name for the backup.

```bash
--incremental-history-name=name
```

`mariadb-backup` can store data about its operations on the MariaDB Server. Using this option, you can define the logical name it uses in identifying the backup.

```bash
mariadb-backup --backup \
     --incremental-history-name=morning_backup
```

The table it uses by default is named `mysql.mariadb_backup_history`. Prior to [MariaDB 10.11](/docs/release-notes/community-server/10.11/what-is-mariadb-1011), the default table was `PERCONA_SCHEMA.xtrabackup_history`.

`mariadb-backup` also records this in the `xtrabackup_info` file.

### `--incremental-history-uuid`

Defines a UUID for the backup.

```bash
--incremental-history-uuid=name
```

`mariadb-backup` can store data about its operations on the MariaDB Server. Using this option, you can define the UUID it uses in identifying a previous backup to increment from. It checks `--incremental-history-name`, `--incremental-basedir`, and `--incremental-lsn`. If mariadb-backup fails to find a valid lsn, it generates an error.

```bash
mariadb-backup --backup \
      --incremental-history-uuid=main-backup012345678
```

The table it uses is named `PERCONA_SCHEMA.xtrabackup_history`, but expect that name to change in future releases. See [MDEV-19246](https://jira.mariadb.org/browse/MDEV-19246) for more information.

Table Name and Schema Changes (MariaDB 10.11):

* MariaDB 10.11 and later: Uses mysql.mariadb\_backup\_history (InnoDB).
* MariaDB 10.10 and earlier: Uses PERCONA\_SCHEMA.xtrabackup\_history (CSV).

`mariadb-backup` also records this in the `xtrabackup_info` file.

### `--incremental-lsn`

Defines the sequence number for incremental backups.

```bash
--incremental-lsn=name
```

Using this option, you can define the sequence number (LSN) value for `--backup` operations. During backups, `mariadb-backup` only copies `.ibd` pages newer than the specified values.

{% hint style="warning" %}
Incorrect LSN values can make the backup unusable. It is impossible to diagnose this issue.
{% endhint %}

### `--innobackupex`

{% hint style="info" %}
Deprecated option.
{% endhint %}

Use to enable `innobackupex` mode, which is a compatibility mode.

```bash
mariadb-backup --innobackupex
```

### `--innodb`

This option has no effect. Set only for MySQL option compatibility.

### `--innodb-adaptive-hash-index`

Enables InnoDB Adaptive Hash Index.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can explicitly enable the InnoDB Adaptive Hash Index. This feature is enabled by default for mariadb-backup. If you want to disable it, use `--skip-innodb-adaptive-hash-index`.

```bash
mariadb-backup --backup \
      --innodb-adaptive-hash-index
```

### `--innodb-autoextend-increment`

Defines the increment in megabytes for auto-extending the size of tablespace file.

```bash
--innodb-autoextend-increment=36
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the increment in megabytes for automatically extending the size of tablespace data file in InnoDB.

```bash
mariadb-backup --backup \
     --innodb-autoextend-increment=35
```

### `--innodb-buffer-pool-filename`

Using this option has no effect. It is available to provide compatibility with the MariaDB Server.

### `--innodb-buffer-pool-size`

Defines the memory buffer size InnoDB uses the cache data and indexes of the table.

```bash
--innodb-buffer-pool-size=124M
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can configure the buffer pool for InnoDB operations.

```bash
mariadb-backup --backup \
      --innodb-buffer-pool-size=124M
```

### `--innodb-checksum-algorithm`

`innodb_checksum_algorithm` has been removed.

### `--innodb-data-file-path`

Defines the path to individual data files.

```bash
--innodb-data-file-path=/path/to/file
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can define the path to InnoDB data files. Each path is appended to the `--innodb-data-home-dir` option.

```bash
mariadb-backup --backup \
     --innodb-data-file-path=ibdata1:13M:autoextend \
     --innodb-data-home-dir=/var/dbs/mysql/data
```

### `--innodb-data-home-dir`

Defines the home directory for InnoDB data files.

```bash
--innodb-data-home-dir=PATH
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can define the path to the directory containing InnoDB data files. You can specific the files using the `--innodb-data-file-path` option.

```bash
mariadb-backup --backup \
     --innodb-data-file-path=ibdata1:13M:autoextend \
     --innodb-data-home-dir=/var/dbs/mysql/data
```

### `--innodb-doublewrite`

Enables doublewrites for InnoDB tables.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. When using this option, `mariadb-backup` improves fault tolerance on InnoDB tables with a doublewrite buffer. By default, this feature is enabled. Use this option to explicitly enable it. To disable doublewrites, use the `--skip-innodb-doublewrite` option.

```bash
mariadb-backup --backup \
     --innodb-doublewrite
```

### `--innodb-encrypt-log`

Defines whether you want to encrypt InnoDB logs.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can tell mariadb-backup that you want to encrypt logs from its InnoDB activity.

### `--innodb-file-io-threads`

Defines the number of file I/O threads in InnoDB.

```bash
--innodb-file-io-threads=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the number of file I/O threads mariadb-backup uses on InnoDB tables.

```bash
mariadb-backup --backup \
     --innodb-file-io-threads=5
```

### `--innodb-file-per-table`

Defines whether you want to store each InnoDB table as an `.ibd` file.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option causes mariadb-backup to store each InnoDB table as an `.ibd` file in the target directory.

### `--innodb-flush-method`

Defines the data flush method. Ignored from [MariaDB 11.0](/docs/release-notes/community-server/old-releases/11.0/what-is-mariadb-110). For the OS-level mechanisms behind these flag names, see [Storage I/O: Buffering and Persistence](/docs/server/ha-and-performance/optimization-and-tuning/operating-system-optimizations/storage-io-buffering-and-persistence).

```bash
--innodb-flush-method=fdatasync
                     | O_DSYNC
                     | O_DIRECT
                     | O_DIRECT_NO_FSYNC
                     | ALL_O_DIRECT
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the data flush method `mariadb-backup` uses with InnoDB tables.

```bash
mariadb-backup --backup \
      --innodb-flush-method==_DIRECT_NO_FSYNC
```

### `--innodb-io-capacity`

Defines the number of IOP's the utility can perform.

```bash
--innodb-io-capacity=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can limit the I/O activity for InnoDB background tasks. It should be set around the number of I/O operations per second that the system can handle, based on drive or drives being used.

```bash
mariadb-backup --backup \
     --innodb-io-capacity=200
```

### `--innodb-log-buffer-size`

The size of the buffer that will be used for reading log during `mariadb-backup --prepare`. Ignored when using `--innodb-log-file-mmap`.

### `--innodb-log-checksums`

Defines whether to include checksums in the InnoDB logs.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can explicitly set `mariadb-backup` to include checksums in the InnoDB logs. The feature is enabled by default. To disable it, use the `--skip-innodb-log-checksums` option.

```bash
mariadb-backup --backup \
      --innodb-log-checksums
```

### `--innodb-log-checkpoint-now`

At the start of a backup, instruct the server to write out all modified pages to the data files, to minimize the size of the `ib_logfile0` that needs to be copied.

```bash
mariadb-backup --backup \
      --innodb-log-checkpoint-now
```

### `--innodb-log-file-mmap`

{% hint style="info" %}
This variable is available from MariaDB 11.4.4 and 10.11.10.
{% endhint %}

When this option is enabled, `mariadb-backup` reads the `ib_logfile0` via a memory mapping, rather than by reading into a separately allocated buffer of `--innodb-log-buffer-size`.

### `--innodb-log-files-in-group`

This option has no functionality in `mariadb-backup`. It exists for MariaDB Server compatibility.

### `--innodb-log-group-home-dir`

Defines the path to InnoDB log files.

```bash
--innodb-log-group-home-dir=PATH
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the path to InnoDB log files.

```bash
mariadb-backup --backup \
     --innodb-log-group-home-dir=/path/to/logs
```

### `--innodb-max-dirty-pages-pct`

Defines the percentage of dirty pages allowed in the InnoDB buffer pool.

```bash
--innodb-max-dirty-pages-pct=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the maximum percentage of dirty, (that is, unwritten) pages that mariadb-backup allows in the InnoDB buffer pool.

```bash
mariadb-backup --backup \
     --innodb-max-dirty-pages-pct=80
```

### `--innodb-open-files`

Defines the number of files kept open at a time.

```bash
--innodb-open-files=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the maximum number of files InnoDB keeps open at a given time during backups.

```bash
mariadb-backup --backup \
      --innodb-open-files=10
```

### `--innodb-page-size`

Defines the universal page size.

```bash
--innodb-page-size=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the universal page size in bytes for `mariadb-backup`.

```bash
mariadb-backup --backup \
     --innodb-page-size=16k
```

### `--innodb-read-io-threads`

Defines the number of background read I/O threads in InnoDB.

```bash
--innodb-read-io-threads=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the number of I/O threads MariaDB uses when reading from InnoDB.

```bash
mariadb-backup --backup \
      --innodb-read-io-threads=4
```

### `--innodb-undo-directory`

Defines the directory for the undo tablespace files.

```bash
--innodb-undo-directory=PATH
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the path to the directory where you want MariaDB to store the undo tablespace on InnoDB tables. The path can be absolute.

```bash
mariadb-backup --backup \
     --innodb-undo-directory=/path/to/innodb_undo
```

### `--innodb-undo-tablespaces`

Defines the number of undo tablespaces to use.

```bash
--innodb-undo-tablespaces=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the number of undo tablespaces you want to use during the backup.

```bash
mariadb-backup --backup \
      --innodb-undo-tablespaces=10
```

### `--innodb-use-native-aio`

Defines whether you want to use native AI/O.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can enable the use of the native asynchronous I/O subsystem. It is only available on Linux operating systems.

```bash
mariadb-backup --backup \
      --innodb-use-native-aio
```

### `--innodb-write-io-threads`

Defines the number of background write I/O threads in InnoDB.

```bash
--innodb-write-io-threads=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the number of background write I/O threads `mariadb-backup` uses.

```bash
mariadb-backup --backup \
     --innodb-write-io-threads=4
```

### `--kill-long-queries-timeout`

Defines the timeout for blocking queries.

```bash
--kill-long-queries-timeout=#
```

When `mariadb-backup` runs, it issues a `FLUSH TABLES WITH READ LOCK` statement. It then identifies blocking queries. Using this option you can set a timeout in seconds for these blocking queries. When the time runs out, `mariadb-backup` kills the queries.

The default value is `0`, which causes `mariadb-backup` to not attempt killing any queries.

```bash
mariadb-backup --backup \
      --kill-long-queries-timeout=10
```

### `--kill-long-query-type`

Defines the query type the utility can kill to unblock the global lock.

```bash
--kill-long-query-type=ALL | UPDATE | SELECT
```

When `mariadb-backup` encounters a query that sets a global lock, it can kill the query in order to free up MariaDB Server for the backup. Using this option, you can choose the types of query it kills: `SELECT`, `UPDATE`, or both set with `ALL`. The default is `ALL`.

```bash
mariadb-backup --backup \
      --kill-long-query-type=UPDATE
```

### `--lock-ddl-per-table`

Prevents DDL for each table to be backed up by acquiring MDL lock on that.

{% hint style="info" %}
Unless the `--no-lock` option is also specified, conflicting DDL queries are killed at the end of backup This is done to avoid a deadlock between `FLUSH TABLE WITH READ LOCK`, user's DDL query (`ALTER`, `RENAME`), and MDL lock on table.
{% endhint %}

### `--log`

This option has no functionality. It is set to ensure compatibility with MySQL.

### `--log-bin`

Defines the base name for the log sequence.

```bash
--log-bin[=name]
```

Using this option you, you can set the base name for `mariadb-backup` to use in log sequences.

### `--log-copy-interval`

Defines the copy interval between checks done by the log copying thread.

```bash
--log-copy-interval=#
```

Using this option, you can define the copy interval mariadb-backup uses between checks done by the log copying thread. The given value is in milliseconds.

```bash
mariadb-backup --backup \
      --log-copy-interval=50
```

### `--log-innodb-page-corruption`

Continue backup if InnoDB corrupted pages are found. The pages are logged in `innodb_corrupted_pages` and backup is finished with error. `--prepare` will try to fix corrupted pages. If `innodb_corrupted_pages` exists after --prepare in base backup directory, backup still contains corrupted pages and can not be considered as consistent.

### `--move-back`

Restores the backup to the data directory.

Using this command, `mariadb-backup` moves the backup from the target directory to the data directory, as defined by the `--datadir` option. You must stop the MariaDB Server before running this command. The data directory must be empty. If you want to overwrite the data directory with the backup, use the `--force-non-empty-directories` option.

Bear in mind, before you can restore a backup, you first need to run `mariadb-backup` with the `--prepare` option. In the case of full backups, this makes the files point-in-time consistent. With incremental backups, this applies the deltas to the base backup. Once the backup is prepared, you can run `--move-back` to apply it to MariaDB Server.

```bash
mariadb-backup --move-back \
      --datadir=/var/mysql
```

Running the `--move-back` command moves the backup files to the data directory. Use this command if you don't want to save the backup for later. If you do want to save the backup for later, use the `--copy-back` option.

### `--mysqld`

Used internally to prepare a backup.

### `--no-backup-locks`

`mariadb-backup` locks the database by default when it runs. This option disables support for Percona Server's backup locks.

When backing up Percona Server, mariadb-backup would use backup locks by default. To be specific, backup locks refers to the `LOCK TABLES FOR BACKUP` and `LOCK BINLOG FOR BACKUP` statements. This option can be used to disable support for Percona Server's backup locks. This option has no effect when the server does not support Percona's backup locks.

Deprecated and has no effect from [MariaDB 10.11.8](/docs/release-notes/community-server/10.11/10.11.8), [MariaDB 11.0.6](/docs/release-notes/community-server/old-releases/11.0/11.0.6), [MariaDB 11.1.5](/docs/release-notes/community-server/old-releases/11.1/11.1.5) and [MariaDB 11.2.4](/docs/release-notes/community-server/old-releases/11.2/11.2.4) as MariaDB now always uses backup locks for better performance. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).

```bash
mariadb-backup --backup --no-backup-locks
```

### `--no-lock`

Disables table locks with the `FLUSH TABLE WITH READ LOCK` statement.

Using this option causes mariadb-backup to disable table locks with the `FLUSH TABLE WITH READ LOCK` statement. Only use this option if:

* You are not executing DML statements on non-InnoDB tables during the backup. This includes the `mysql` database system tables (which are MyISAM).
* You are not executing any DDL statements during the backup.
* You are *not* using the file `xtrabackup_binlog_info`, which is not consistent with the data when `--no-lock` is used. Use the file `xtrabackup_binlog_pos_innodb` instead.
* All tables you're backing up use the InnoDB storage engine.

```bash
mariadb-backup --backup --no-lock
```

If you're considering `--no-lock` due to backups failing to acquire locks, this may be due to incoming replication events preventing the lock. Consider using the `--safe-slave-backup` option to momentarily stop the replica thread. This alternative may help the backup to succeed without resorting to `--no-lock`.
