# mariadb-backup Overview

Complete MariaDB backup and recovery guide. Complete resource for backup methods, mariadb-backup usage, scheduling, and restoration for production use.

{% hint style="info" %}
mariadb-backup was previously called mariabackup.
{% endhint %}

**mariadb-backup** is an open source tool provided by MariaDB for performing physical online backups of InnoDB, Aria and MyISAM tables. For InnoDB, “hot online” backups are possible. It was originally forked from Percona XtraBackup 2.3.8. It is available on Linux and Windows.

This tool provides a production-quality, nearly non-blocking method for performing full backups on running systems. While partial backups with mariadb-backup are technically possible, they require many steps and cannot be restored directly onto existing servers containing other data.

## Supported Features

`mariadb-backup` supports all of the main features of Percona XtraBackup 2.3.8, plus:

* Backup/Restore of tables using Data-at-Rest Encryption.
* Backup/Restore of tables using InnoDB Page Compression.
* [mariadb-backup SST method](/docs/galera-cluster/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method) with Galera Cluster.
* Microsoft Windows support.
* Backup/Restore of tables using the MyRocks storage engine. See [Files Backed up by mariadb-backup: MyRocks Data Files](/docs/server/server-usage/backup-and-restore/mariadb-backup/files-backed-up-by-mariadb-backup#myrocks-data-files) for more information.

## **Supported Features in MariaDB Enterprise Backup**

{% tabs %}
{% tab title="Current" %}
MariaDB Backup supports some additional features, such as:

* Minimizes locks during the backup to permit more concurrency and to enable faster backups.
  * This relies on the usage of `BACKUP STAGE` commands and DDL logging.
  * This includes no locking during the copy phase of `ALTER TABLE` statements, which tends to be the longest phase of these statements.
* Provides optimal backup support for all storage engines that store things on local disk.
  {% endtab %}

{% tab title="< 10.11.8" %}
MariaDB Backup does **not** support some additional features.
{% endtab %}
{% endtabs %}

## Backup Types

mariadb-backup supports various type of backups (and restores from those backups), documented on separate pages:

* [Full backup and restore](/docs/server/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup)
* [Incremental backup and restore](/docs/server/server-usage/backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup)
* [Partial backup and restore](/docs/server/server-usage/backup-and-restore/mariadb-backup/partial-backup-and-restore-with-mariadb-backup)
* Restoring [individual databases](/docs/server/server-usage/backup-and-restore/mariadb-backup/individual-database-restores-with-mariadb-backup-from-full-backup), [tables, and partitions](/docs/server/server-usage/backup-and-restore/mariadb-backup/restoring-individual-tables-and-partitions-with-mariadb-backup)
* [Point-in-time recovery (PITR)](/docs/server/server-usage/backup-and-restore/mariadb-backup/point-in-time-recovery-pitr-mariadb-backup)

## Installing `mariadb-backup`

### Installing on Linux

The `mariadb-backup` executable is included in binary tarballs on Linux.

### **Installing with a Package Manager**

mariadb-backup can also be installed via a package manager on Linux. Many Linux distributions provide MariaDB software "out of the box", including `mariadb-backup`. If your Linux distribution doesn't, however, you can install using a MariaDB repository.

In order to do so, your system needs to be configured to install from one of the MariaDB repositories.

You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the MariaDB Package Repository setup script.

You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](/docs/server/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage).

**Installing with yum/dnf**

On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant RPM package from MariaDB's repository using yum or [dnf](https://en.wikipedia.org/wiki/DNF_\(software\)). Starting with RHEL 8 and Fedora 22, `yum` has been replaced by `dnf`, which is the next major version of `yum`. However, `yum` commands still work on many systems that use `dnf`. For example:

```bash
sudo yum install MariaDB-backup
```

**Installing with apt-get**

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant DEB package from MariaDB's repository using [apt-get](https://wiki.debian.org/apt-get). For example:

```bash
sudo apt-get install mariadb-backup
```

**Installing with zypper**

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant RPM package from MariaDB's repository using zypper. For example:

```bash
sudo zypper install MariaDB-backup
```

### Installing on Windows

The `mariadb-backup` executable is included in MSI and ZIP packages on Windows.

When using the [Windows MSI installer](/docs/server/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows), `mariadb-backup` can be installed by selecting *Backup utilities*:

<figure><img src="/files/ysBiS9PGAxsUo61O4voc" alt=""><figcaption><p>MariaDB MSI Installer showing the Backup utilities install option</p></figcaption></figure>

## Usage

The command to use `mariadb-backup` and the general syntax is:

```bash
mariadb-backup <options>
```

For in-depth explanations on how to use `mariadb-backup`, see:

* [Full Backup and Restore with mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup)
* [Incremental Backup and Restore with mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup)
* [Partial Backup and Restore with mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/partial-backup-and-restore-with-mariadb-backup)
* [Restoring Individual Tables and Partitions with mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/restoring-individual-tables-and-partitions-with-mariadb-backup)
* [Setting up a Replica with mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/setting-up-a-replica-with-mariadb-backup)
* [Using Encryption and Compression Tools With mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/using-encryption-and-compression-tools-with-mariadb-backup)

## Options

Options supported by mariadb-backup can be found on the [mariadb-backup Options](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options) page.

{% hint style="warning" %}
`mariadb-backup` will currently silently ignore unknown command-line options, so be extra careful about accidentally including typos in options or accidentally using options from later `mariadb-backup` versions. The reason for this is that `mariadb-backup` currently treats command-line options and options from [option files](/docs/server/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) equivalently. When it reads from these [option files](/docs/server/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files), it has to read a lot of options from the server option groups read by [mariadbd](/docs/server/server-management/starting-and-stopping-mariadb/mariadbd-options). However, `mariadb-backup` does not know about many of the options that it normally reads in these option groups. If `mariadb-backup` raised an error or warning when it encountered an unknown option, then this process would generate a large amount of log messages under normal use. Therefore, `mariadb-backup` is designed to silently ignore the unknown options instead. See [MDEV-18215](https://jira.mariadb.org/browse/MDEV-18215) about that.
{% endhint %}

### Option Files

In addition to reading options from the command-line, mariadb-backup can also read options from option files.

The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:

| Option                      | Description                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------- |
| `--print-defaults`          | Print the program argument list and exit.                                           |
| `--no-defaults`             | Don't read default options from any option file.                                    |
| `--defaults-file=#`         | Only read default options from the given option file.                               |
| `--defaults-extra-file=#`   | Read this file after the global files are read.                                     |
| `--defaults-group-suffix=#` | In addition to the default option groups, also read option groups with this suffix. |

#### **Server Option Groups**

mariadb-backup reads server options from the following [option groups](/docs/server/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) from [option files](/docs/server/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files):

| Group              | Description                                                                                                                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[mariadb-backup]` | Options read by `mariadb-backup`.                                                                                                                                                                                                                                                      |
| `[mariadb-backup]` | Options read by `mariadb-backup`.                                                                                                                                                                                                                                                      |
| `[xtrabackup]`     | Options read by `mariadb-backup` and Percona XtraBackup.                                                                                                                                                                                                                               |
| `[server]`         | Options read by MariaDB Server.                                                                                                                                                                                                                                                        |
| `[mysqld]`         | Options read by `mariadbd`, which includes both MariaDB Server and MySQL Server (where it is called `mysqld`).                                                                                                                                                                         |
| `[mysqld-X.Y]`     | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example: `[mysqld-10.6]`.                                                                                                                                                       |
| `[mariadb]`        | Options read by MariaDB Server.                                                                                                                                                                                                                                                        |
| `[mariadb-X.Y]`    | Options read by a specific version of MariaDB Server. For example: `[mariadb-10.6]`.                                                                                                                                                                                                   |
| `[mariadbd]`       | Options read by MariaDB Server. Available from MariaDB 10.5.4.                                                                                                                                                                                                                         |
| `[mariadbd-X.Y]`   | Options read by a specific version of MariaDB Server. For example: `[mariadbd-10.6]`. Available from MariaDB 10.5.4.                                                                                                                                                                   |
| `[client-server]`  | Options read by all MariaDB client programs and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients.                                                                                                               |
| `[galera]`         | Options read by MariaDB Server, but only if it is compiled with Galera Cluster support. All builds on Linux are compiled with Galera Cluster support. When using one of these builds, options from this option group are read even if the Galera Cluster functionality is not enabled. |

#### **Client Option Groups**

mariadb-backup reads client options from the following option groups from option files:

| Group              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[mariadb-backup]` | Options read by mariadb-backup. Available starting with [MariaDB 10.1.31](/docs/release-notes/community-server/old-releases/10.1/10.1.31) and [MariaDB 10.2.13](/docs/release-notes/community-server/old-releases/10.2/10.2.13).                                                                                                                                                                                                                              |
| `[mariadb-backup]` | Options read by mariadb-backup. Available starting with [MariaDB 10.4.14](/docs/release-notes/community-server/old-releases/10.4/10.4.14) and [MariaDB 10.5.4](/docs/release-notes/community-server/old-releases/10.5/10.5.4)                                                                                                                                                                                                                                 |
| `[xtrabackup]`     | Options read by mariadb-backup and Percona XtraBackup.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `[client]`         | Options read by all MariaDB and MySQL client programs, which includes both MariaDB and MySQL clients. For example, mysqldump.                                                                                                                                                                                                                                                                                                                                 |
| `[client-server]`  | Options read by all MariaDB client programs and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. Available starting with [MariaDB 10.1.38](/docs/release-notes/community-server/old-releases/10.1/10.1.38), [MariaDB 10.2.22](/docs/release-notes/community-server/old-releases/10.2/10.2.22), and [MariaDB 10.3.13](/docs/release-notes/community-server/old-releases/10.3/10.3.13). |
| `[client-mariadb]` | Options read by all MariaDB client programs. Available starting with [MariaDB 10.1.38](/docs/release-notes/community-server/old-releases/10.1/10.1.38), [MariaDB 10.2.22](/docs/release-notes/community-server/old-releases/10.2/10.2.22), and [MariaDB 10.3.13](/docs/release-notes/community-server/old-releases/10.3/10.3.13).                                                                                                                             |

### Backup History Table

`mariadb-backup` can optionally track your backup operations in a database table. This provides a centralized audit log and allows you to automate incremental backups by referencing the logical name of the previous backup instead of managing file paths.

**Table Location and Schema Changes (MariaDB 10.11):**

* **MariaDB 10.11 and later:** The history table is `mysql.mariadb_backup_history` and uses the **InnoDB** storage engine (transactional).
* **MariaDB 10.10 and earlier:** The history table is `PERCONA_SCHEMA.xtrabackup_history` and uses the **CSV** storage engine.

{% hint style="info" %}
On the first run after upgrading to MariaDB 10.11, `mariadb-backup` will attempt to migrate the old CSV table to the new InnoDB table. This requires specific privileges (see below).
{% endhint %}

## Authentication and Privileges

`mariadb-backup` needs to authenticate with the database server when it performs a backup operation (i.e. when the [--backup ](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#backup)option is specified). For most use cases, the user account that performs the backup needs to have the following global privileges on the database server.

{% tabs %}
{% tab title="Current" %}
The required privileges are:

```sql
CREATE USER 'mariadb-backup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR ON *.* TO 'mariadb-backup'@'localhost';
```

{% endtab %}

{% tab title="< 10.5" %}
The required privileges are:

```sql
CREATE USER 'mariadb-backup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'mariadb-backup'@'localhost';
```

{% endtab %}
{% endtabs %}

If your database server is also using the [MyRocks storage engine](/docs/server/server-usage/storage-engines/myrocks), then the user account that performs the backup will also need the `SUPER` [global privilege](/docs/server/reference/sql-statements/account-management-sql-statements/grant#global-privileges). This is because `mariadb-backup` creates a checkpoint of this data by setting the [rocksdb\_create\_checkpoint](/docs/server/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_create_checkpoint) system variable, which requires this privilege. See [MDEV-20577](https://jira.mariadb.org/browse/MDEV-20577) for more information.

`CONNECTION ADMIN` is also required where [--kill-long-queries-timeout](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#kill-long-queries-timeout) is greater than `0`, and [--no-lock](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#no-lock) isn't applied in order to [KILL](/docs/server/reference/sql-statements/administrative-sql-statements/kill) queries.

`REPLICA MONITOR` (or alias `SLAVE MONITOR`) is also required where [--galera-info](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#galera-info) or [--slave-info](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#slave-info) is specified.

To use the [--history](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#history) option(or the incremental history options), the backup user requires specific privileges on the history table.

{% tabs %}
{% tab title="Current" %}
The user needs `INSERT` to create history records and `SELECT` to read them for incremental backups:

{% code overflow="wrap" %}

```sql
GRANT SELECT, INSERT, CREATE, ALTER ON mysql.mariadb_backup_history TO 'mariadb-backup'@'localhost';
```

{% endcode %}
{% endtab %}

{% tab title="< MariaDB 10.10" %}
The user needs privileges on the legacy `PERCONA_SCHEMA`:

{% code overflow="wrap" %}

```sql
GRANT SELECT, INSERT, CREATE, ALTER ON PERCONA_SCHEMA.xtrabackup_history TO 'mariadb-backup'@'localhost';
```

{% endcode %}
{% endtab %}
{% endtabs %}

**For Upgrading to 10.11 (One-Time Migration)**

If upgrading from an older version, `mariadb-backup` will attempt to migrate the old table to the new location on the first run. The backup user needs privileges to move and modify the old table:

```sql
GRANT DROP, ALTER, RENAME ON PERCONA_SCHEMA.xtrabackup_history TO 'mariadb-backup'@'localhost';
GRANT CREATE ON PERCONA_SCHEMA TO 'mariadb-backup'@'localhost';
```

Alternatively, you can perform this migration manually before running the backup:

```sql
RENAME TABLE PERCONA_SCHEMA.xtrabackup_history TO mysql.mariadb_backup_history;
ALTER TABLE mysql.mariadb_backup_history ENGINE=InnoDB;
```

The user account information can be specified with the [--user](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#user) and [--password](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#p-password) command-line options. For example:

```bash
mariadb-backup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

The user account information can also be specified in a supported [client option group](#client-option-groups) in an [option file](/docs/server/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files). For example:

```ini
[mariadb-backup]
user=mariadb-backup
password=mypassword
```

`mariadb-backup` does not need to authenticate with the database server when preparing or restoring a backup.

### File System Permissions

`mariadb-backup` has to read MariaDB's files from the file system. Therefore, when you run `mariadb-backup` as a specific operating system user, you should ensure that user account has sufficient permissions to read those files.

If you are using Linux and if you installed MariaDB with a package manager, then MariaDB's files will probably be owned by the `mysql` user and the `mysql` group.

## Using `mariadb-backup` with Data-at-Rest Encryption

`mariadb-backup` supports [Data-at-Rest Encryption](/docs/server/security/encryption/data-at-rest-encryption).

mariadb-backup will query the server to determine which [key management and encryption plugin](/docs/server/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management) is being used, and then it will load that plugin itself, which means that `mariadb-backup` needs to be able to load the key management and encryption plugin's shared library.

mariadb-backup will also query the server to determine which [encryption keys](/docs/server/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management#using-multiple-encryption-keys) it needs to use.

In other words, `mariadb-backup` is able to figure out a lot of encryption-related information on its own, so normally one doesn't need to provide any extra options to backup or restore encrypted tables.

`mariadb-backup` backs up encrypted and unencrypted tables as they are on the original server. If a table is encrypted, then the table will remain encrypted in the backup. Similarly, if a table is unencrypted, then the table will remain unencrypted in the backup.

The primary reason that mariadb-backup needs to be able to encrypt and decrypt data is that it needs to apply [InnoDB redo log](/docs/server/server-usage/storage-engines/innodb/innodb-redo-log) records to make the data consistent when the backup is prepared. As a consequence, mariadb-backup does not perform many encryption or decryption operations when the backup is initially taken. MariaDB performs more encryption and decryption operations when the backup is prepared. This means that some encryption-related problems (such as using the wrong encryption keys) may not become apparent until the backup is prepared.

## Using `mariadb-backup` for Galera SSTs

The `mariadb-backup` SST method uses the `mariadb-backup` utility for performing SSTs. See [mariadb-backup SST method](/docs/galera-cluster/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method) for more information.

## Files Backed up by `mariadb-backup`

`mariadb-backup` backs up many different files in order to perform its backup operation. See [Files Backed up by mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/files-backed-up-by-mariadb-backup) for a list of these files.

## Files Created by `mariadb-backup`

`mariadb-backup` creates several different types of files during the backup and prepare phases. See [Files Created by mariadb-backup](#files-created-by-mariadb-backup) for a list of these files.

## Binary Logs

`mariadb-backup` can store the binary log position in the backup. See [--binlog-info](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#binlog-info). This can be used for point-in-time recovery and to use the backup to setup a slave with the correct binlog position.

## Known Issues

### No Default Data Directory

`mariadb-backup` defaults to the server's default `datadir` value. See [MDEV-12956](https://jira.mariadb.org/browse/MDEV-12956) for more information.

### Too Many Open Files

If `mariadb-backup` uses more file descriptors than the system is configured to allow, then users can see errors like the following:

```log
2019-02-12 09:48:38 7ffff7fdb820  InnoDB: Operating system error number 23 in a file operation.
InnoDB: Error number 23 means 'Too many open files in system'.
InnoDB: Some operating system error numbers are described at
InnoDB: http://dev.mysql.com/doc/refman/5.6/en/operating-system-error-codes.html
InnoDB: Error: could not open single-table tablespace file ./db1/tab1.ibd
InnoDB: We do not continue the crash recovery, because the table may become
InnoDB: corrupt if we cannot apply the log records in the InnoDB log to it.
InnoDB: To fix the problem and start mysqld:
InnoDB: 1) If there is a permission problem in the file and mysqld cannot
InnoDB: open the file, you should modify the permissions.
InnoDB: 2) If the table is not needed, or you can restore it from a backup,
InnoDB: then you can remove the .ibd file, and InnoDB will do a normal
InnoDB: crash recovery and ignore that table.
InnoDB: 3) If the file system or the disk is broken, and you cannot remove
InnoDB: the .ibd file, you can set innodb_force_recovery > 0 in my.cnf
InnoDB: and force InnoDB to continue crash recovery here.
```

`mariadb-backup` throws an error and aborts when this error is encountered. See [MDEV-19060](https://jira.mariadb.org/browse/MDEV-19060) for more information.

When this error is encountered, one solution is to explicitly specify a value for the [--open-files-limit](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#open-files-limit) option either on the command line or in one of the supported [server option group](#server-option-groups) s in an [option file](/docs/server/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files). For example:

```bash
[mariadb-backup]
open_files_limit=65535
```

An alternative solution is to set the soft and hard limits for the user account that runs `mariadb-backup` by adding new limits to [/etc/security/limits.conf](https://linux.die.net/man/5/limits.conf). For example, if `mariadb-backup` is run by the `mysql` user, then you could add lines like the following:

```
mysql soft nofile 65535
mysql hard nofile 65535
```

After the system is rebooted, the above configuration should set new open file limits for the `mysql` user, and the user's `ulimit` output should look like the following:

```bash
ulimit -Sn
65535
ulimit -Hn
65535
```

## See Also

* [mariadb-dump/mysqldump](/docs/server/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump)
* [How to backup with MariaDB](https://www.youtube.com/watch?v=xB4ImmmzXqU) (video)
* [MariaDB point-in-time recovery](https://www.youtube.com/watch?v=ezHmnNmmcDo) (video)
* [mariadb-backup and Restic](https://www.youtube.com/watch?v=b-KFj8GfvzE) (video)

<sub>*This page is licensed: CC BY-SA / Gnu FDL*</sub>

{% @marketo/form formId="4316" %}
