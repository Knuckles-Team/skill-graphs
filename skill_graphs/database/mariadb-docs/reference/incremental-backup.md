# incremental backup
$ mariadb-backup --backup --stream=mbstream \
  --incremental-basedir=backup_base \
  --user=mariadb-backup --password=mypassword \
  --extra-lsndir=backup_inc1 | gzip > backup-inc1.gz
```

### Preparing the Backup

Following the above steps, you have three backups in `/var/mariadb`: The first is a full backup, the others are increments on this first backup. In order to restore a backup to the database, you first need to apply the incremental backups to the base full backup. This is done using the `--prepare` command option.

Perform the following process:

First, prepare the base backup:

```bash
$ mariadb-backup --prepare \
   --target-dir=/var/mariadb/backup
```

Running this command brings the base full backup, that is, `/var/mariadb/backup`, into sync with the changes contained in the InnoDB redo log collected while the backup was taken.

Then, apply the incremental changes to the base full backup:

```bash
$ mariadb-backup --prepare \
   --target-dir=/var/mariadb/backup \
   --incremental-dir=/var/mariadb/inc1
```

Running this command brings the base full backup, that is, `/var/mariadb/backup`, into sync with the changes contained in the first incremental backup.

For each remaining incremental backup, repeat the last step to bring the base full backup into sync with the changes contained in that incremental backup.

### Restoring the Backup

Once you've applied all incremental backups to the base, you can restore the backup using either the `--copy-back` or the `--move-back` options. The `--copy-back` option allows you to keep the original backup files. The `--move-back` option actually moves the backup files to the `datadir`, so the original backup files are lost.

* First, [stop the MariaDB Server process](https://mariadb.com/kb/en/).
* Then, ensure that the `datadir` is empty.
* Then, run `mariadb-backup` with one of the options mentioned above:

```bash
$ mariadb-backup --copy-back \
   --target-dir=/var/mariadb/backup/
```

* Then, you may need to fix the file permissions.

When `mariadb-backup` restores a database, it preserves the file and directory privileges of the backup. However, it writes the files to disk as the user and group restoring the database. As such, after restoring a backup, you may need to adjust the owner of the data directory to match the user and group for the MariaDB Server, typically `mysql` for both. For example, to recursively change ownership of the files to the `mysql` user and group, you could execute:

```bash
$ chown -R mysql:mysql /var/lib/mysql/
```

* Finally, [start the MariaDB Server process](https://mariadb.com/kb/en/).

<sub>*This page is licensed: CC BY-SA / Gnu FDL*</sub>

{% @marketo/form formId="4316" %}
