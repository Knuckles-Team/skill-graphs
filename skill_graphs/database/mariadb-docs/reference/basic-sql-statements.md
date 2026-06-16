# Basic SQL Statements

A quick reference guide for essential SQL statements in MariaDB, categorized by Data Definition, Data Manipulation, and Transaction Control.

<table data-view="cards"><thead><tr><th align="center"></th><th align="center"></th><th align="center"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td align="center"><strong>WEBINAR</strong></td><td align="center">MariaDB 101: Learning the Basics of MariaDB</td><td align="center"><a href="https://go.mariadb.com/MariaDB101-2024-10-16_Registration-LP.html?utm_source=onpagepromo&#x26;utm_medium=kb&#x26;utm_campaign=webinar-mariadb-101"><strong>Watch Now</strong></a></td><td><a href="/files/OcSFjQe7EtkSet78TesE">/files/OcSFjQe7EtkSet78TesE</a></td></tr></tbody></table>

This page lists the most important SQL statements and contains links to their documentation pages. If you need a basic tutorial on how to use the MariaDB database server and how to execute simple commands, see [A MariaDB Primer](/docs/server/server-usage/basics/mariadb-usage-guide-1).

Also see [Common MariaDB Queries](/docs/server/mariadb-quickstart-guides/mariadb-advanced-sql-guide) for examples of commonly-used queries.

## Defining How Your Data Is Stored

* [CREATE DATABASE](/docs/server/reference/sql-statements/data-definition/create/create-database) is used to create a new, empty database.
* [DROP DATABASE](/docs/server/reference/sql-statements/data-definition/drop/drop-database) is used to completely destroy an existing database.
* [USE](/docs/server/reference/sql-statements/administrative-sql-statements/use-database) is used to select a default database.
* [CREATE TABLE](/docs/server/server-usage/tables/create-table) is used to create a new table, which is where your data is actually stored.
* [ALTER TABLE](/docs/server/reference/sql-statements/data-definition/alter/alter-table) is used to modify an existing table's definition.
* [DROP TABLE](/docs/server/server-usage/tables/drop-table) is used to completely destroy an existing table.
* [DESCRIBE](/docs/server/reference/sql-statements/administrative-sql-statements/describe) shows the structure of a table.

## Manipulating Your Data

* [SELECT](/docs/server/reference/sql-statements/data-manipulation/selecting-data/select) is used when you want to read (or select) your data.
* [INSERT](/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert) is used when you want to add (or insert) new data.
* [UPDATE](/docs/server/reference/sql-statements/data-manipulation/changing-deleting-data/update) is used when you want to change (or update) existing data.
* [DELETE](/docs/server/reference/sql-statements/data-manipulation/changing-deleting-data/delete) is used when you want to remove (or delete) existing data.
* [REPLACE](/docs/server/reference/sql-statements/data-manipulation/changing-deleting-data/replace) is used when you want to add or change (or replace) new or existing data.
* [TRUNCATE](/docs/server/reference/sql-statements/table-statements/truncate-table) is used when you want to empty (or delete) all data from the template.

## Transactions

* [START TRANSACTION](/docs/server/reference/sql-statements/transactions/start-transaction) is used to begin a transaction.
* [COMMIT](/docs/server/reference/sql-statements/transactions/commit) is used to apply changes and end transaction.
* [ROLLBACK](/docs/server/reference/sql-statements/transactions/rollback) is used to discard changes and end transaction.

### A Simple Example

```sql
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE mytable ( id INT PRIMARY KEY, name VARCHAR(20) );
INSERT INTO mytable VALUES ( 1, 'Will' );
INSERT INTO mytable VALUES ( 2, 'Marry' );
INSERT INTO mytable VALUES ( 3, 'Dean' );
SELECT id, name FROM mytable WHERE id = 1;
UPDATE mytable SET name = 'Willy' WHERE id = 1;
SELECT id, name FROM mytable;
DELETE FROM mytable WHERE id = 1;
SELECT id, name FROM mytable;
DROP DATABASE mydb;
SELECT COUNT(1) FROM mytable; gives the NUMBER OF records IN the TABLE
```

*The first version of this article was copied, with permission, from* [*Basic\_SQL\_Statements*](https://hashmysql.org/wiki/Basic_SQL_Statements) *on 2012-10-05.*

<sub>*This page is licensed: CC BY-SA / Gnu FDL*</sub>

{% @marketo/form formId="4316" %}
