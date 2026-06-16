# mariadb-backup

Get an overview of MariaDB Backup. This section introduces the hot physical backup tool, explaining its capabilities for efficient and consistent backups of your MariaDB Server.

{% columns %}
{% column %}
{% content-ref url="/pages/DKwiZ0wiRfazX4tFvWZV" %}
[mariadb-backup Overview](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to the `mariadb-backup` utility, detailing its features, installation process, and support for hot online backups of InnoDB tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/jvnNjTGSYtqVcCSBgF0n" %}
[mariadb-backup Options](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A comprehensive reference for all command-line options available in mariadb-backup, covering backup, prepare, and restore operations.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/JA4hlosWtghQ0ik4oQdl" %}
[Full Backup and Restore (mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to perform and restore full physical backups of MariaDB databases using the mariadb-backup tool, ensuring consistent data recovery.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/IhchjfWfi5t0rTl54xT6" %}
[Incremental Backup and Restore (mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide explains how to create and apply incremental backups with `mariadb-backup`, saving storage space and reducing backup time.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/jdqPsAGUrJcrO28ZU1oy" %}
[Point-In-Time Recovery (PITR, mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/point-in-time-recovery-pitr-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to restore (recover) to a specific point in time. Point-in-time recovery is often referred to as PITR.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/V6SH83yHw6QD6QIKAhEf" %}
[Partial Backup and Restore (mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/partial-backup-and-restore-with-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Back up specific databases or tables. This guide explains how to filter your backup to include only the data you need.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/qwmeRV2Tz9D5QRXGC76n" %}
[Restoring Individual Databases From a Full Backup (mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/individual-database-restores-with-mariadb-backup-from-full-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Restore a single database from a full backup. Learn the procedure to extract and recover a specific database schema from a larger backup set.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/lBgXnpIt44YMG6Qdcgsw" %}
[Restoring Individual Tables and Partitions (mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/restoring-individual-tables-and-partitions-with-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Restore specific tables from a backup. Learn the process of importing individual `.ibd` files to recover specific tables without restoring the whole database.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/4wNQZImc2FywouZNzoyS" %}
[Setting up a Replica (mariadb-backup)](/docs/server/server-usage/backup-and-restore/mariadb-backup/setting-up-a-replica-with-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Initialize a replication slave using a backup. This guide shows how to use mariadb-backup to provision a new replica from a master server.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/mYJcpaPQnAF5kc4jjrRB" %}
[Files Backed Up by mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/files-backed-up-by-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
List of file types included in a backup. Understand which data files, logs, and configuration files are preserved during the backup process.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/dcgRYG1l9omB775e5Wrx" %}
[Files Created by mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/files-created-by-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference of files generated during backup. This page explains the purpose of metadata files created by the `mariadb-backup`.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/USXP6S3Ba6lXRdAZF4Ue" %}
[Using Encryption and Compression Tools With mariadb-backup](/docs/server/server-usage/backup-and-restore/mariadb-backup/using-encryption-and-compression-tools-with-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Secure and compress backup streams. Learn to pipe backup output to tools like GPG and GZIP for encryption and storage efficiency.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/54mNLledfbbtllTPzExn" %}
[How mariadb-backup Works](/docs/server/server-usage/backup-and-restore/mariadb-backup/how-mariadb-backup-works)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deep dive into backup mechanics. Understand how the tool handles redo logs, locking, and file copying to ensure consistent backups.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/pages/qAOLwmRReWzleYTXNvar" %}
[mariadb-backup and BACKUP STAGE](/docs/server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-and-backup-stage-commands)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand backup locking stages. This page explains how mariadb-backup uses `BACKUP STAGE` statements to minimize locking during operation.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/spaces/3VYeeVGUV4AMqrA3zwy7/pages/SyBLW3HPQOhaGLD3aPGJ" %}
[mariadb-backup SST Method](/docs/galera-cluster/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure State Snapshot Transfers for Galera Cluster. Learn to use `mariadb-backup` for non-blocking data transfer when a new node joins a cluster.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/spaces/3VYeeVGUV4AMqrA3zwy7/pages/CfVfmbN1YZ2XwDSTR2IS" %}
[Manual SST of Galera Cluster Node With mariadb-backup](/docs/galera-cluster/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/manual-sst-of-galera-cluster-node-with-mariadb-backup)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform a manual node provision. This guide details the steps to manually backup a donor and restore it to a joiner node in a Galera Cluster.

<br>
{% endcolumn %}
{% endcolumns %}
