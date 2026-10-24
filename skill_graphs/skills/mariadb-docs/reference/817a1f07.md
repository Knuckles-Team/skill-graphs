# mariadb-backup Options

Reference for mariadb-backup (mariabackup) command-line options. Covers --backup, --prepare, --copy-back, --move-back, streaming, and incremental backups.

{% hint style="info" %}
mariadb-backup was previously called mariabackup.
{% endhint %}

## `mariadb-backup` Options (mariabackup)

Use this page as a reference for **`mariadb-backup` / `mariabackup` command-line options**. It focuses on the options (flags) you use for **physical (file-based) MariaDB backups**, including **hot online backups** for InnoDB.

### Quick Reference (Most Searched Options)

* Take a physical backup: [`--backup`](#backup) + [`--target-dir`](#target-dir)
* Prepare a backup: [`--prepare`](#prepare) (or legacy [`--apply-log`](#apply-log))
* Restore a backup: [`--copy-back`](#copy-back) or [`--move-back`](#move-back)
* Incremental backups: [`--incremental-basedir`](#incremental-basedir) + [`--incremental-dir`](#incremental-dir)
* Replication/Galera metadata: [`--slave-info`](#slave-info), [`--binlog-info`](#binlog-info), [`--galera-info`](#galera-info)
* Stream output (pipes to gzip/gpg/etc): [`--stream`](#stream) + [`--extra-lsndir`](#extra-lsndir)

### Common Command Patterns

Full backup (physical):

```bash
mariadb-backup --backup --target-dir=/backups/full \
  --user=mariadb-backup --password=...
```

Prepare (make files consistent for restore):

```bash
mariadb-backup --prepare --target-dir=/backups/full
```

Restore:

```bash
mariadb-backup --copy-back --target-dir=/backups/full
```

Incremental backup (delta against an existing base backup):

```bash
mariadb-backup --backup --target-dir=/backups/inc1 \
  --incremental-basedir=/backups/full
```

### Related Pages

* [mariadb-backup Overview](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview)
* [Full Backup and Restore (mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup)
* [Incremental Backup and Restore (mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup)
* [Using Encryption and Compression Tools With mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/using-encryption-and-compression-tools-with-mariadb-backup)

## Options

### `--apply-log`

Prepares an existing backup to restore to the MariaDB Server. This is only valid in `innobackupex` mode, which can be enabled with the [--innobackupex](#innobackupex) option.

Files that `mariadb-backup` generates during [--backup](#backup) operations in the target directory are not ready for use on the Server. Before you can restore the data to MariaDB, you first need to prepare the backup.

In the case of full backups, the files are not point in time consistent, since they were taken at different times. If you try to restore the database without first preparing the data, InnoDB rejects the new data as corrupt. Running `mariadb-backup` with the [--prepare](#prepare) command readies the data so you can restore it to MariaDB Server. When working with incremental backups, you need to use the `--prepare` command and the [--incremental-dir](#incremental-dir) option to update the base backup with the deltas from an incremental backup.

```bash
mariadb-backup --innobackupex --apply-log
```

Once the backup is ready, you can use the [--copy-back](#copy-back) or the [--move-back](#move-back) commands to restore the backup to the server.

### `--apply-log-only`

If this option is used when preparing a backup, then only the redo log apply stage are performed, and other stages of crash recovery are ignored. This option is used with incremental backups.

{% hint style="danger" %}
**Note:** This option is not needed or supported anymore.
{% endhint %}

### `--backup`

Backs up your databases.

Using this command option, `mariadb-backup` performs a backup operation on your database or databases. The backups are written to the target directory, as set by the [--target-dir](#target-dir) option.

```bash
mariadb-backup --backup
      --target-dir /path/to/backup \
      --user user_name --password user_passwd
```

`mariadb-backup` can perform full and incremental backups. A full backup creates a snapshot of the database in the target directory. An incremental backup checks the database against a previously taken full backup, (defined by the [--incremental-basedir](#incremental-basedir) option) and creates delta files for these changes.

In order to restore from a backup, you first need to run `mariadb-backup` with the `--prepare` option, to make a full backup point-in-time consistent or to apply incremental backup deltas to base. Then you can run `mariadb-backup` again with either the [--copy-back](#copy-back) or [--move-back](#move-back) commands to restore the database.

For more information, see [Full Backup and Restore](/docs/server/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup) and [Incremental Backup and Restore](/docs/server/server-usage/backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup).

### `--binlog-info`

Defines how `mariadb-backup` retrieves the binary log coordinates from the server.

```bash
--binlog-info[=OFF | ON | LOCKLESS | AUTO]
```

The `--binlog-info` option supports the following retrieval methods. When no retrieval method is provided, it defaults to `AUTO`.

| Option     | Description                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| `OFF`      | Disables the retrieval of binary log information                                                        |
| `ON`       | Enables the retrieval of binary log information, performs locking where available to ensure consistency |
| `LOCKLESS` | Unsupported option                                                                                      |
| `AUTO`     | Enables the retrieval of binary log information using `ON` or `LOCKLESS` where supported                |

Using this option, you can control how `mariadb-backup` retrieves the server's binary log coordinates corresponding to the backup.

When enabled, whether using `ON` or `AUTO`, `mariadb-backup` retrieves information from the binlog during the backup process. When disabled with `OFF`, `mariadb-backup` runs without attempting to retrieve binary log information. You may find this useful when you need to copy data without metadata like the binlog or replication coordinates.

```bash
mariadb-backup --binlog-info --backup
```

Currently, the `LOCKLESS` option depends on features unsupported by MariaDB Server. See the description of the [xtrabackup\_binlog\_pos\_innodb](/docs/server/server-usage/backup-and-restore/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_binlog_pos_innodb) file for more information. If you attempt to run `mariadb-backup` with this option, then it causes the utility to exit with an error.

### `--close-files`

Defines whether you want to close file handles.

Using this option, you can tell `mariadb-backup` that you want to close file handles. Without this option, `mariadb-backup` keeps files open in order to manage DDL operations. When working with particularly large tablespaces, closing the file can make the backup more manageable. However, it can also lead to inconsistent backups. Use at your own risk.

```bash
mariadb-backup --close-files --prepare
```

### `--compress`

{% hint style="warning" %}
This option was deprecated as it relies on the no longer maintained [QuickLZ](https://github.com/RT-Thread-packages/quicklz/) library. It are removed in a future release - versions supporting this function will not be affected. It is recommended to instead backup to a stream (stdout), and use a 3rd party compression library to compress the stream, as described in [Using Encryption and Compression Tools With mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/using-encryption-and-compression-tools-with-mariadb-backup).
{% endhint %}

Defines the compression algorithm for backup files.

```bash
--compress[=compression_algorithm]
```

The `--compress` option only supports the now deprecated `quicklz` algorithm.

| Option    | Description                            |
| --------- | -------------------------------------- |
| `quicklz` | Uses the QuickLZ compression algorithm |

```bash
mariadb-backup --compress --backup
```

If a backup is compressed using this option, then `mariadb-backup` will record that detail in the [xtrabackup\_info](/docs/server/server-usage/backup-and-restore/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_info) file.

### `--compress-chunk-size`

{% hint style="warning" %}
Deprecated, for details see the [--compress](#compress) option.
{% endhint %}

Defines the working buffer size for compression threads.

```bash
--compress-chunk-size=#
```

`mariadb-backup` can perform compression operations on the backup files before writing them to disk. It can also use multiple threads for parallel data compression during this process. Using this option, you can set the chunk size each thread uses during compression. It defaults to `64K`.

```bash
mariadb-backup --backup --compress \
     --compress-threads=12 --compress-chunk-size=5M
```

To further configure backup compression, see the [--compress](#compress) and [--compress-threads](#compress-threads) options.

### `--compress-threads`

{% hint style="warning" %}
Deprecated, for details see the [--compress](#compress) option.
{% endhint %}

Defines the number of threads to use in compression.

```
--compress-threads=#
```

`mariadb-backup` can perform compression operations on the backup files before writing them to disk. Using this option, you can define the number of threads you want to use for this operation. You may find this useful in speeding up the compression of particularly large databases. It defaults to single-threaded.

```
mariadb-backup --compress --compress-threads=12 --backup
```

To further configure backup compression, see the [--compress](#compress) and [--compress-chunk-size](#compress-chunk-size) options.

### `--copy-back`

Restores the backup to the data directory.

Using this command, `mariadb-backup` copies the backup from the target directory to the data directory, as defined by the `--datadir` option. You must stop the MariaDB Server before running this command. The data directory must be empty. If you want to overwrite the data directory with the backup, use the `--force-non-empty-directories` option.

Bear in mind, before you can restore a backup, you first need to run mariadb-backup with the --prepare option. In the case of full backups, this makes the files point-in-time consistent. With incremental backups, this applies the deltas to the base backup. Once the backup is prepared, you can run `--copy-back` to apply it to MariaDB Server.

```bash
mariadb-backup --copy-back --force-non-empty-directories
```

Running the `--copy-back` command copies the backup files to the data directory. Use this command if you want to save the backup for later. If you don't want to save the backup for later, use the `--move-back` option.

### `--core-file`

Defines whether to write a core file.

Using this option, you can configure `mariadb-backup` to dump its core to file in the event that it encounters fatal signals. You may find this useful for review and debugging purposes.

```bash
mariadb-backup --core-file --backup
```

### `--databases`

Defines the databases and tables you want to back up.

```
--databases="database[.table][ database[.table] ...]"
```

Using this option, you can define the specific database or databases you want to back up. In cases where you have a particularly large database or otherwise only want to back up a portion of it, you can optionally also define the tables on the database.

```bash
mariadb-backup --backup \
      --databases="example.table1 example.table2"
```

In cases where you want to back up most databases on a server or tables on a database, but not all, you can set the specific databases or tables you don't want to back up using the `--databases-exclude` option.

If a backup is a partial backup, then mariadb-backup will record that detail in the `xtrabackup_info` file.

In `innobackupex` mode, which can be enabled with the `--innobackupex` option, the `--databases` option can be used as described above, or it can be used to refer to a file, just as the [--databases-file option](#databases-file) can in the normal mode.

### `--databases-exclude`

Defines the databases you don't want to back up.

```
--databases-exclude="database[.table][ database[.table] ...]"
```

Using this option, you can define the specific database or databases you want to exclude from the backup process. You may find it useful when you want to back up most databases on the server or tables on a database, but would like to exclude a few from the process.

```bash
mariadb-backup --backup \
      --databases="example" \
      --databases-exclude="example.table1 example.table2"
```

To include databases in the backup, see the `--databases` option option.

If a backup is a partial backup, then `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--databases-file`

Defines the path to a file listing databases and/or tables you want to back up.

```bash
--databases-file="/path/to/database-file"
```

Format the databases file to list one element per line, with the following syntax:

```bash
database[.table]
```

In cases where you need to back up a number of databases or specific tables in a database, you may find the syntax for the `--databases` and `--databases-exclude` options a little cumbersome. Using this option you can set the path to a file listing the databases or databases and tables you want to back up.

For instance, listing the databases and tables for a backup in a file called `main-backup`:

```bash
cat main-backup
```

```
example1
example2.table1
example2.table2
```

```bash
mariadb-backup --backup --databases-file=main-backup
```

If a backup is a partial backup, `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `-h, --datadir`

Defines the path to the database root.

```bash
--datadir=PATH
```

Using this option, you can define the path to the source directory. This is the directory that `mariadb-backup` reads for the data it backs up. It should be the same as the MariaDB Server `datadir` system variable.

```
mariadb-backup --backup -h /var/lib64/mysql
```

### `--debug-sleep-before-unlock`

This is a debug-only option used by the Xtrabackup test suite.

### `--decompress`

Deprecated, for details see the `--compress` option.

This option requires that you have the `qpress` utility installed on your system.

Defines whether you want to decompress previously compressed backup files.

When you run mariadb-backup with the `--compress` option, it compresses the subsequent backup files, using the QuickLZ algorithm. Using this option, `mariadb-backup` decompresses the compressed files from a previous backup.

For instance, run a backup with compression:

```bash
mariadb-backup --compress --backup
```

Then, decompress the backup:

```bash
mariadb-backup --decompress
```

You can enable the decryption of multiple files at a time using the `--parallel` option. By default, mariadb-backup does not remove the compressed files from the target directory. To delete these files, use the `--remove-original` option.

### `--debug-sync`

Defines the debug sync point. This option is only used by the `mariadb-backup` test suite.

### `--defaults-extra-file`

Defines the path to an extra default option file.

```
--defaults-extra-file=/path/to/config
```

Using this option, you can define an extra default option file for `mariadb-backup`. Unlike `--defaults-file`, this file is read after the default option files are read, allowing you to only overwrite the existing defaults.

```bash
mariadb-backup --backup \
      --defaults-file-extra=addition-config.cnf \
      --defaults-file=config.cnf
```

### `--defaults-file`

Defines the path to the default option file.

```
--defaults-file=/path/to/config
```

Using this option, you can define a default option file for `mariadb-backup`. Unlike the `--defaults-extra-file` option, when this option is provided, it completely replaces all default option files.

```bash
mariadb-backup --backup \
     --defaults-file=config.cnf
```

### `--defaults-group`

Defines the option group to read in the option file.

```bash
--defaults-group="name"
```

In situations where you find yourself using certain `mariadb-backup` options consistently every time you call it, you can set the options in an option file. The `--defaults-group` option defines what option group `mariadb-backup` reads for its options.

Options you define from the command-line can be set in the configuration file using minor formatting changes. For instance, if you find yourself perform compression operations frequently, you might set `--compress-threads` and `--compress-chunk-size` options in this way:

```
[mariadb-backup]
compress_threads = 12
compress_chunk_size = 64K
```

Now whenever you run a backup with the `--compress` option, it always performs the compression using 12 threads and 64K chunks.

```bash
mariadb-backup --compress --backup
```

See [mariadb-backup Overview: Server Option Groups](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview#server-option-groups) and [mariadb-backup Overview: Client Option Groups](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview#client-option-groups) for a list of the option groups read by `mariadb-backup` by default.

### `--encrypted-backup`

When this option is used with `--backup`, if `mariadb-backup` encounters a page that has a non-zero `key_version` value, then mariadb-backup assumes that the page is encrypted.

Use `--skip-encrypted-backup` instead to allow mariadb-backup to copy unencrypted tables that were originally created before MySQL 5.1.48.

### `--export`

If this option is provided during the `--prepare` stage, then it tells `mariadb-backup` to create `.cfg` files for each InnoDB file-per-table tablespace. These `.cfg` files are used to import transportable tablespaces in the process of restoring partial backups and restoring individual tables and partitions.

The `--export` option could require rolling back incomplete transactions that had modified the table. This will likely create a "new branch of history" that does not correspond to the server that had been backed up, which makes it impossible to apply another incremental backup on top of such additional changes. The option should only be applied when doing a `--prepare` of the last incremental.

```bash
mariadb-backup --prepare --export
```

`mariadb-backup` did not support the `--export` option. See [MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466) about that. In earlier versions of MariaDB, this means that mariadb-backup could not create `.cfg` files for InnoDB file-per-table tablespaces during the `--prepare` stage. You can still import file-per-table tablespaces without the `.cfg` files in many cases, so it may still be possible in those versions to restore partial backups or to restore individual tables and partitions with just the `.ibd` files. If you have a full backup and you need to create `.cfg` files for InnoDB file-per-table tablespaces, then you can do so by preparing the backup as usual without the `--export` option, and then restoring the backup, and then starting the server. At that point, you can use the server's built-in features to copy the transportable tablespaces.

### `--extra-lsndir`

Saves an extra copy of the `xtrabackup_checkpoints` and `xtrabackup_info` files into the given directory.

```bash
--extra-lsndir=PATH
```

When using the `--backup` option, `mariadb-backup` produces a number of backup files in the target directory. Using this option, you can have `mariadb-backup` produce additional copies of the `xtrabackup_checkpoints` and `xtrabackup_info` files in the given directory.

```bash
mariadb-backup --extra-lsndir=extras/ --backup
```

This is especially useful when using `--stream` for streaming output, e.g. for compression and/or encryption using external tools in combination with incremental backups, as the `xtrabackup_checkpoints` file necessary to determine the LSN to continue the incremental backup from is still accessible without uncompressing / decrypting the backup file first. Pass in the `--extra-lsndir` of the previous backup as `--incremental-basedir` .

### `--force-non-empty-directories`

Allows `--copy-back` or `--move-back` options to use non-empty target directories.

When using `mariadb-backup` with the `--copy-back` or `--move-back` options, they normally require a non-empty target directory to avoid conflicts. Using this option with either of command allows `mariadb-backup` to use a non-empty directory.

```bash
mariadb-backup --force-non-empty-directories --copy-back
```

Bear in mind that this option does not enable overwrites. When copying or moving files into the target directory, if `mariadb-backup` finds that the target file already exists, it fails with an error.

### `--ftwrl-wait-query-type`

Defines the type of query allowed to complete before `mariadb-backup` issues the global lock.

```bash
--ftwrl-wait-query-type=[ALL | UPDATE | SELECT]
```

The `--ftwrl-wait-query-type` option supports the following query types. The default value is `ALL`.

| Option | Description                                                           |
| ------ | --------------------------------------------------------------------- |
| ALL    | Waits until all queries complete before issuing the global lock       |
| SELECT | Waits until SELECT statements complete before issuing the global lock |
| UPDATE | Waits until UPDATE statements complete before issuing the global lock |

When `mariadb-backup` runs, it issues a global lock to prevent data from changing during the backup process. When it encounters a statement in the process of executing, it waits until the statement is finished before issuing the global lock. Using this option, you can modify this default behavior to ensure that it waits only for certain query types, such as for `SELECT` and `UPDATE` statements.

```bash
mariadb-backup --backup  \
      --ftwrl-wait-query-type=UPDATE
```

### `--ftwrl-wait-threshold`

Defines the minimum threshold for identifying long-running queries for FTWRL.

```bash
--ftwrl-wait-threshold=#
```

When `mariadb-backup` runs, it issues a global lock to prevent data from changing during the backup process and ensure a consistent record. If it encounters statements still in the process of executing, it waits until they complete before setting the lock. Using this option, you can set the threshold at which mariadb-backup engages FTWRL[^1]. When it `--ftwrl-wait-timeout` is not 0 and a statement has run for at least the amount of time given this argument, mariadb-backup waits until the statement completes or until the `--ftwrl-wait-timeout` expires before setting the global lock and starting the backup.

```bash
mariadb-backup --backup \
     --ftwrl-wait-timeout=90 \
     --ftwrl-wait-threshold=30
```

### `--ftwrl-wait-timeout`

Defines the timeout to wait for queries before trying to acquire the global lock. The global lock refers to `BACKUP STAGE BLOCK_COMMIT`. The global lock refers to `FLUSH TABLES WITH READ LOCK` (FTWRL).

```bash
--ftwrl-wait-timeout=#
```

When `mariadb-backup` runs, it acquires a global lock to prevent data from changing during the backup process and ensure a consistent record. If it encounters statements still in the process of executing, it can be configured to wait until the statements complete before trying to acquire the global lock.

If the `--ftwrl-wait-timeout` is set to 0, `mariadb-backup` tries to acquire the global lock immediately without waiting. This is the default value.

If the `--ftwrl-wait-timeout` is set to a non-zero value, then `mariadb-backup` waits for the configured number of seconds until trying to acquire the global lock.

`mariadb-backup` exits if it can't acquire the global lock after waiting for the configured number of seconds.

```bash
mariadb-backup --backup \
      --ftwrl-wait-query-type=UPDATE \
      --ftwrl-wait-timeout=5
```

The `--ftwrl-wait-timeout` option specifies the maximum time that `mariadb-backup` will wait to obtain the global lock required to begin a consistent backup.

{% tabs %}
{% tab title="From MariaDB 10.4" %}
this lock is acquired with **`BACKUP STAGE BLOCK_COMMIT`**.
{% endtab %}

{% tab title="Before 10.4" %}
this lock is acquired with **`FLUSH TABLES WITH READ LOCK (FTWRL)`**.
{% endtab %}
{% endtabs %}

If the lock cannot be obtained within the configured timeout, the backup process fails.

This option helps avoid failures caused by long-running MariaDB queries that block backup locks.

**Example Errors**

When the timeout is not set appropriately, backups may fail with messages such as:

```vbnet
Unable to obtain lock. Please try again later.
```

or

```vbnet
FATAL ERROR: failed to execute query BACKUP STAGE START:
Lock wait timeout exceeded; try restarting transaction
```

Example log excerpt:

```vbnet
[00] 2022-02-08 15:43:25 Unable to obtain lock. Please try again later.
[00] 2022-02-08 15:43:25 Error on BACKUP STAGE START query execution
