
The `--no-lock` option only provides a consistent backup if the user ensures that no DDL or non-transactional table updates occur during the backup. The `--no-lock` option is not supported by MariaDB plc.

### `--no-timestamp`

This option prevents creation of a time-stamped subdirectory of the `BACKUP-ROOT-DIR` given on the command line. When it is specified, the backup is done in `BACKUP-ROOT-DIR` instead. This is only valid in `innobackupex` mode, which can be enabled with the `--innobackupex` option.

### `--no-version-check`

Disables version check.

Using this option, you can disable mariadb-backup version check.

```bash
mariadb-backup --backup --no-version-check
```

### `--open-files-limit`

Defines the maximum number of file descriptors.

```bash
--open-files-limit=#
```

Using this option, you can define the maximum number of file descriptors mariadb-backup reserves with `setrlimit()`.

```bash
mariadb-backup --backup \
      --open-files-limit=
```

### `--parallel`

Defines the number of threads to use for parallel data file transfer.

```bash
--parallel=#
```

Using this option, you can set the number of threads mariadb-backup uses for parallel data file transfers. By default, it is set to 1.

### `-p, --password`

Defines the password to use to connect to MariaDB Server.

```bash
--password=passwd
```

When you run `mariadb-backup`, it connects to MariaDB Server in order to access and back up the databases and tables. Using this option, you can set the password mariadb-backup uses to access the server. To set the user, use the `--user` option.

```bash
mariadb-backup --backup \
      --user=root \
      --password=root_password
```

### `--plugin-dir`

Defines the directory for server plugins.

```bash
--plugin-dir=PATH
```

Using this option, you can define the path `mariadb-backup` reads for MariaDB Server plugins. It only uses it during the `--prepare` phase to load the encryption plugin. It defaults to the `plugin_dir` server system variable.

```bash
mariadb-backup --backup \
      --plugin-dir=/var/mysql/lib/plugin
```

### `--plugin-load`

The option has been removed.

### `-P, --port`

Defines the server port to connect to.

```bash
--port=#
```

When you run `mariadb-backup`, it connects to MariaDB Server in order to access and back up your databases and tables. Using this option, you can set the port the utility uses to access the server over TCP/IP. To set the host, see the `--host` option. Use `mysql --help` for more details.

```bash
mariadb-backup --backup \
      --host=192.168.11.1 \
      --port=3306
```

### `--prepare`

Prepares an existing backup to restore to the MariaDB Server.

Files that `mariadb-backup` generates during `--backup` operations in the target directory are not ready for use on the Server. Before you can restore the data to MariaDB, you first need to prepare the backup.

In the case of full backups, the files are not point in time consistent, since they were taken at different times. If you try to restore the database without first preparing the data, InnoDB rejects the new data as corrupt. Running mariadb-backup with the `--prepare` command readies the data so you can restore it to MariaDB Server. When working with incremental backups, you need to use the `--prepare` command and the `--incremental-dir` option to update the base backup with the deltas from an incremental backup.

```bash
mariadb-backup --prepare
```

Once the backup is ready, you can use the `--copy-back` or the `--move-back` options to restore the backup to the server.

### `--print-defaults`

Prints the utility argument list, then exits.

Using this argument, MariaDB prints the argument list to stdout and then exits. You may find this useful in debugging to see how the options are set for the utility.

```bash
mariadb-backup --print-defaults
```

### `--print-param`

Prints the MariaDB Server options needed for `copy-back`.

Using this option, `mariadb-backup` prints to stdout the MariaDB Server options that the utility requires to run the `--copy-back` command option.

```bash
mariadb-backup --print-param
```

### `--rollback-xa`

By default, mariadb-backup will not commit or rollback uncommitted XA transactions, and when the backup is restored, any uncommitted XA transactions must be manually committed using `XA COMMIT` or manually rolled back using `XA ROLLBACK`.

**MariaDB starting with** [**10.5**](/docs/release-notes/community-server/old-releases/10.5/what-is-mariadb-105)

mariadb-backup's `--rollback-xa` option is not present because the server has more robust ways of handling uncommitted XA transactions.

This is an experimental option. Do not use this option in older versions. Older implementation can cause corruption of InnoDB data.

### `--rsync`

Defines whether to use rsync.

During normal operation, mariadb-backup transfers local non-InnoDB files using a separate call to `cp` for each file. Using this option, you can optimize this process by performing this transfer with rsync, instead.

```bash
mariadb-backup --backup --rsync
```

This option is not compatible with the `--stream` option.

Deprecated and has no effect from [MariaDB 10.11.8](/docs/release-notes/community-server/10.11/10.11.8), [MariaDB 11.0.6](/docs/release-notes/community-server/old-releases/11.0/11.0.6), [MariaDB 11.1.5](/docs/release-notes/community-server/old-releases/11.1/11.1.5) and [MariaDB 11.2.4](/docs/release-notes/community-server/old-releases/11.2/11.2.4) as rsync will not work on tables that are in use. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).

### `--safe-slave-backup`

Stops replica SQL threads for backups.

When running `mariadb-backup` on a server that uses replication, you may occasionally encounter locks that block backups. Using this option, it stops replica SQL threads and waits until the `Slave_open_temp_tables` in the `SHOW STATUS` statement is zero. If there are no open temporary tables, the backup runs, otherwise the SQL thread starts and stops until there are no open temporary tables.

```bash
mariadb-backup --backup \
      --safe-slave-backup \
      --safe-slave-backup-timeout=500
```

The backup fails if the `Slave_open_temp_tables` doesn't reach zero after the timeout period set by the `--safe-slave-backup-timeout` option.

### `--safe-slave-backup-timeout`

Defines the timeout for replica backups.

```bash
--safe-slave-backup-timeout=#
```

When running mariadb-backup on a server that uses replication, you may occasionally encounter locks that block backups. With the `--safe-slave-backup` option, it waits until the `Slave_open_temp_tables` in the `SHOW STATUS` statement reaches zero. Using this option, you set how long it waits. It defaults to 300.

```bash
mariadb-backup --backup \
      --safe-slave-backup \
      --safe-slave-backup-timeout=500
```

### `--secure-auth`

Refuses client connections to servers using the older protocol.

Using this option, you can set it explicitly to refuse client connections to the server when using the older protocol, from before 4.1.1. This feature is enabled by default. Use the `--skip-secure-auth` option to disable it.

```bash
mariadb-backup --backup --secure-auth
```

### `--skip-innodb-adaptive-hash-index`

Disables InnoDB Adaptive Hash Index.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can explicitly disable the InnoDB Adaptive Hash Index. This feature is enabled by default for mariadb-backup. If you want to explicitly enable it, use `--innodb-adaptive-hash-index`.

```bash
mariadb-backup --backup \
      --skip-innodb-adaptive-hash-index
```

### `--skip-innodb-doublewrite`

Disables doublewrites for InnoDB tables.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. When doublewrites are enabled, InnoDB improves fault tolerance with a doublewrite buffer. By default this feature is turned on. Using this option you can disable it for mariadb-backup. To explicitly enable doublewrites, use the `--innodb-doublewrite` option.

```bash
mariadb-backup --backup \
     --skip-innodb-doublewrite
```

### `--skip-innodb-log-checksums`

Defines whether to exclude checksums in the InnoDB logs.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set mariadb-backup to exclude checksums in the InnoDB logs. The feature is enabled by default. To explicitly enable it, use the `--innodb-log-checksums` option.

### `--skip-secure-auth`

Refuses client connections to servers using the older protocol.

Using this option, you can set it accept client connections to the server when using the older protocol, from before 4.1.1. By default, it refuses these connections. Use the `--secure-auth` option to explicitly enable it.

```bash
mariadb-backup --backup --skip-secure-auth
```

### `--slave-info`

Prints the binary log position and the name of the primary server.

If the server is a replica, then this option causes `mariadb-backup` to print the hostname of the replica's replication primary and the binary log file and position of the replica's SQL thread to `stdout`.

This option also causes `mariadb-backup` to record this information as a `CHANGE MASTER` statement that can be used to set up a new server as a replica of the original server's primary after the backup has been restored. This information are written to the `xtrabackup_slave_info` file.

`mariadb-backup` does **not** check if GTIDs are being used in replication. It takes a shortcut and assumes that if the `gtid_slave_pos` system variable is non-empty, then it writes the `CHANGE MASTER` statement with the `MASTER_USE_GTID` option set to `slave_pos`. Otherwise, it writes the `CHANGE MASTER` statement with the `MASTER_LOG_FILE` and `MASTER_LOG_POS` options using the primary's binary log file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.

```bash
mariadb-backup --slave-info
```

### `-S, --socket`

Defines the socket for connecting to local database.

```bash
--socket=name
```

Using this option, you can define the UNIX domain socket you want to use when connecting to a local database server. The option accepts a string argument. For more information, see the `mysql --help` command.

```bash
mariadb-backup --backup \
      --socket=/var/mysql/mysql.sock
```

### `--ssl`

Enables TLS. By using this option, you can explicitly configure `mariadb-backup` to encrypt its connection with TLS when communicating with the server. You may find this useful when performing backups in environments where security is extra important or when operating over an insecure network.

TLS is also enabled even without setting this option when certain other TLS options are set. For example, see the descriptions of the following options:

* \--ssl-ca
* \--ssl-capath
* \--ssl-cert
* \--ssl-cipher
* \--ssl-key

### `--ssl-ca`

Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

See Secure Connections Overview: Certificate Authorities (CAs) for more information.

This option implies the `--ssl` option.

### `--ssl-capath`

Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-capath=/etc/my.cnf.d/certificates/ca/
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-capath=/etc/my.cnf.d/certificates/ca/
```

The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.

See Secure Connections Overview: Certificate Authorities (CAs) for more information

This option implies the `--ssl` option.

### `--ssl-cert`

Defines a path to the X509 certificate file to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option implies the `--ssl` option.

### `--ssl-cipher`

Defines the list of permitted ciphers or cipher suites to use for TLS. For example:

```
--ssl-cipher=name
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-cipher=TLSv1.2
```

To determine if the server restricts clients to specific ciphers, check the ssl\_cipher system variable.

This option implies the `--ssl` option.

### `--ssl-crl`

Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-crl=/etc/my.cnf.d/certificates/crl.pem
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-crl=/etc/my.cnf.d/certificates/crl.pem
```

See Secure Connections Overview: Certificate Revocation Lists (CRLs) for more information.

This option is only supported if `mariadb-backup` was built with OpenSSL. If `mariadb-backup` was built with yaSSL, then this option is not supported. See TLS and Cryptography Libraries Used by MariaDB for more information about which libraries are used on which platforms.

### `--ssl-crlpath`

Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-crlpath=/etc/my.cnf.d/certificates/crl/
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-crlpath=/etc/my.cnf.d/certificates/crl/
```

The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.

See Secure Connections Overview: Certificate Revocation Lists (CRLs) for more information.

This option is only supported if mariadb-backup was built with OpenSSL. If `mariadb-backup` was built with yaSSL, then this option is not supported. See TLS and Cryptography Libraries Used by MariaDB for more information about which libraries are used on which platforms.

### `--ssl-key`

Defines a path to a private key file to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-key=/etc/my.cnf.d/certificates/client-key.pem
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option implies the `--ssl` option.

### `--ssl-verify-server-cert`

Enables server certificate verification. This option is disabled by default.

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-verify-server-cert
```

### `--stream`

Streams backup files to stdout.

```bash
--stream=xbstream
```

Using this command option, you can set `mariadb-backup` to stream the backup files to `stdout` in the given format. Currently, the supported format is `xbstream`.

```bash
mariadb-backup --stream=xbstream > backup.xb
```

To extract all files from the xbstream archive into a directory use the `mbstream` utility

```bash
mbstream  -x < backup.xb
```

If a backup is streamed, then `mariadb-backup` records the format in the `xtrabackup_info` file.

### `--tables`

Defines the tables you want to include in the backup.

```bash
--tables=REGEX
```

Using this option, you can define what tables you want `mariadb-backup` to back up from the database. The table values are defined using Regular Expressions (regex[^2]). To define the tables you want to exclude from the backup, see the `--tables-exclude` option.

```bash
mariadb-backup --backup \
     --databases=example \
     --tables=nodes_* \
     --tables-exclude=nodes_tmp
```

In the example, *`nodes_*`* matches tables named *`nodes`*, *`nodes_`*, *`nodes__`*, and so forth, because `*` means *zero or more occurrences of the previous character* (`_`).

If instead you want to back up all tables whose names start with *`nodes`*, the regular expression is `^nodes.`, and to exclude tables starting with *`nodes_tmp`*, the expression is *`^nodes_tmp.`*. (Notice the trailing period (`.`); it means *zero or more occurrences of characters following `nodes`*.) The command looks like this:

```bash
mariadb-backup --backup \
     --databases=example \
     --tables=^nodes. \
     --tables-exclude=^nodes_tmp.
```

In that example, some of the tables included via the `--tables` option are excluded by `--tables-excludes`. That works because `--tables-exclude` takes precedence over `--tables`.

You can specify multiple table name regex[^2] patterns as a comma-separated list, for both the `--tables` and the `--tables-exclude` options.

The following command backs up all tables in the *`test1`* and *`test2`* databases, except the *`exclude_table`* table in the *`test2`* database, and stores the backup files under *`/path/to/backups/`*:

```bash
mariadb-backup --backup \
     --tables=test1[.].*,test2[.].* \
     --tables-exclude=^test2[.]exclude_table
     --target-dir=/path/to/backups/
```

{% hint style="warning" %}
The [`--databases`](#databases) and [`--databases-exclude`](#databases-exclude) options, if used, take precedence over `--tables` and `--tables-exclude`. That is, they can filter out tables, which are then not "visible" to the latter mentioned options.
{% endhint %}

If a backup is a partial backup, `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--tables-exclude`

Defines the tables you want to exclude from the backup.

```bash
--tables-exclude=REGEX
```

Using this option, you can define what tables you want `mariadb-backup` to exclude from the backup. The table values are defined using Regular Expressions. To define the tables you want to include from the backup, see the `--tables` option.

{% hint style="info" %}
See [the `--tables` option](#tables) for examples and hints regarding regular expressions.
{% endhint %}

If a backup is a partial backup, `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--tables-file`

Defines path to file with tables for backups.

```bash
--tables-file=/path/to/file
```

Using this option, you can set a path to a file listing the tables you want to back up. `mariadb-backup` iterates over each line in the file. The format is `database.table`.

```bash
mariadb-backup --backup \
     --databases=example \
     --tables-file=/etc/mysql/backup-file
```

If a backup is a partial backup, then mariadb-backup will record that detail in the `xtrabackup_info` file.

### `--target-dir`

Defines the destination directory.

```bash
--target-dir=/path/to/target
```

Using this option you can define the destination directory for the backup. `mariadb-backup` writes all backup files to this directory. mariadb-backup will create the directory, if it does not exist (but it does not create the full path recursively, i.e. at least parent directory if the `--target-dir` must exist.

```bash
mariadb-backup --backup \
       --target-dir=/data/backups
```

### `--throttle`

Defines the limit for I/O operations per second in IOS values.

```bash
--throttle=#
```

Using this option, you can set a limit on the I/O operations mariadb-backup performs per second in IOS values. It is only used during the `--backup` option.

### `--tls-version`

This option accepts a comma-separated list of TLS protocol versions. A TLS protocol version is only enabled if it is present in this list. All other TLS protocol versions will not be permitted. For example:

```bash
--tls-version="TLSv1.2,TLSv1.3"
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --tls-version="TLSv1.2,TLSv1.3"
```

See Secure Connections Overview: TLS Protocol Versions for more information.

### `-t, --tmpdir`

Defines path for temporary files.

```bash
--tmpdir=/path/tmp[;/path/tmp...]
```

Using this option, you can define the path to a directory `mariadb-backup` uses in writing temporary files. If you want to use more than one, separate the values by a semicolon (that is, `;`). When passing multiple temporary directories, it cycles through them using round-robin.

```bash
mariadb-backup --backup \
     --tmpdir=/data/tmp;/tmp
```

### `--use-memory`

Defines the buffer pool size that is used during the prepare stage.

```bash
--use-memory=124M
```

Using this option, you can define the buffer pool size for `mariadb-backup`. Use it instead of `buffer_pool_size`.

```bash
mariadb-backup --prepare \
      --use-memory=124M
```

### `--user`

Defines the username for connecting to the MariaDB Server.

```bash
--user=name
-u name
```

When `mariadb-backup` runs, it connects to the specified MariaDB Server to get its backups. Using this option, you can define the database user used for authentication. Starting from [MariaDB 10.6.17](/docs/release-notes/community-server/10.6/10.6.17), [MariaDB 10.11.7](/docs/release-notes/community-server/10.11/10.11.7), [MariaDB 11.0.5](/docs/release-notes/community-server/old-releases/11.0/11.0.5), [MariaDB 11.1.4](/docs/release-notes/community-server/old-releases/11.1/11.1.4), [MariaDB 11.2.3](/docs/release-notes/community-server/old-releases/11.2/11.2.3), [MariaDB 11.3.2](/docs/release-notes/community-server/old-releases/11.3/11.3.2), [MariaDB 11.4.1](/docs/release-notes/community-server/11.4/11.4.1), if the `--user` option is omitted, the user name is detected from the OS.

```bash
mariadb-backup --backup \
      --user=root \
      --password=root_passwd
```

### `--verbose`

Displays verbose output.

```bash
mariadb-backup --verbose
```

### `--version`

Prints the `mariadb-backup` version information to `stdout`.

```bash
mariadb-backup --version
```

<sub>*This page is licensed: CC BY-SA / Gnu FDL*</sub>

{% @marketo/form formId="4316" %}

[^1]: FLUSH TABLES WITH READ LOCK

[^2]: regular expression
