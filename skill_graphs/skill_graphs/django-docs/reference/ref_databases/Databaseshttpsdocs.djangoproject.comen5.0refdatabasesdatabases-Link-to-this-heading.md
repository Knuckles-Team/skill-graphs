# Databases[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#databases "Link to this heading")
Django officially supports the following databases:
  * [PostgreSQL](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes)
  * [MariaDB](https://docs.djangoproject.com/en/5.0/ref/databases/#mariadb-notes)
  * [MySQL](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-notes)
  * [Oracle](https://docs.djangoproject.com/en/5.0/ref/databases/#oracle-notes)
  * [SQLite](https://docs.djangoproject.com/en/5.0/ref/databases/#sqlite-notes)


There are also a number of [database backends provided by third parties](https://docs.djangoproject.com/en/5.0/ref/databases/#third-party-notes).
Django attempts to support as many features as possible on all database backends. However, not all database backends are alike, and we’ve had to make design decisions on which features to support and which assumptions we can make safely.
This file describes some of the features that might be relevant to Django usage. It is not intended as a replacement for server-specific documentation or reference manuals.
