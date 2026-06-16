# Files Backed Up by mariadb-backup

List of file types included in a backup. Understand which data files, logs, and configuration files are preserved during the backup process.

{% hint style="info" %}
mariadb-backup was previously called mariabackup.
{% endhint %}

## Files Included in Backup

`mariadb-backup` backs up the files listed below.

### InnoDB Data Files

mariadb-backup backs up the following InnoDB data files:

* [InnoDB system tablespace](/docs/server/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces)
* [InnoDB file-per-table tablespaces](/docs/server/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces)

### MyRocks Data Files

{% tabs %}
{% tab title="Current" %}
`mariadb-backup` will back up tables that use the [MyRocks](/docs/server/server-usage/storage-engines/myrocks) storage engine. This data is located in the directory defined by the [rocksdb\_datadir](/docs/server/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_datadir) system variable. `mariadb-backup` backs this data up by performing a checkpoint using the [rocksdb\_create\_checkpoint](/docs/server/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_create_checkpoint) system variable.
{% endtab %}

{% tab title="< 10.3.8 to 10.2.16" %}
`mariadb-backup` will back up tables that use the MyRocks storage engine.
{% endtab %}
{% endtabs %}

### Other Data Files

`mariadb-backup` also backs up files with the following extensions:

* `frm`
* `isl`
* `MYD`
* `MYI`
* `MAD`
* `MAI`
* `MRG`
* `TRG`
* `TRN`
* `ARM`
* `ARZ`
* `CSM`
* `CSV`
* `opt`
* `par`

## Files Excluded From Backup

`mariadb-backup` does **not** back up the files listed below.

* [InnoDB Temporary Tablespaces](/docs/server/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-temporary-tablespaces)
* [Binary logs](/docs/server/server-management/server-monitoring-logs/binary-log)
* [Relay logs](/docs/server/server-management/server-monitoring-logs/binary-log/relay-log)

<sub>*This page is licensed: CC BY-SA / Gnu FDL*</sub>

{% @marketo/form formId="4316" %}
