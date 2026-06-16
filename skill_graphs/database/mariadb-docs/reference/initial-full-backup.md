# initial full backup
$ mariadb-backup --backup --stream=mbstream \
  --user=mariadb-backup --password=mypassword \
  --extra-lsndir=backup_base | gzip > backup_base.gz
