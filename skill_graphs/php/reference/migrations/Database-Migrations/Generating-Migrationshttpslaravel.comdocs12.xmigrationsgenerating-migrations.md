## [Generating Migrations](https://laravel.com/docs/12.x/migrations#generating-migrations)
You may use the `make:migration` [Artisan command](https://laravel.com/docs/12.x/artisan) to generate a database migration. The new migration will be placed in your `database/migrations` directory. Each migration filename contains a timestamp that allows Laravel to determine the order of the migrations:
```


1php artisan make:migration create_flights_table




php artisan make:migration create_flights_table

```

Laravel will use the name of the migration to attempt to guess the name of the table and whether or not the migration will be creating a new table. If Laravel is able to determine the table name from the migration name, Laravel will pre-fill the generated migration file with the specified table. Otherwise, you may simply specify the table in the migration file manually.
If you would like to specify a custom path for the generated migration, you may use the `--path` option when executing the `make:migration` command. The given path should be relative to your application's base path.
Migration stubs may be customized using [stub publishing](https://laravel.com/docs/12.x/artisan#stub-customization).
### [Squashing Migrations](https://laravel.com/docs/12.x/migrations#squashing-migrations)
As you build your application, you may accumulate more and more migrations over time. This can lead to your `database/migrations` directory becoming bloated with potentially hundreds of migrations. If you would like, you may "squash" your migrations into a single SQL file. To get started, execute the `schema:dump` command:
```


1php artisan schema:dump




2 



3# Dump the current database schema and prune all existing migrations...




4php artisan schema:dump --prune




php artisan schema:dump

# Dump the current database schema and prune all existing migrations...
php artisan schema:dump --prune

```

When you execute this command, Laravel will write a "schema" file to your application's `database/schema` directory. The schema file's name will correspond to the database connection. Now, when you attempt to migrate your database and no other migrations have been executed, Laravel will first execute the SQL statements in the schema file of the database connection you are using. After executing the schema file's SQL statements, Laravel will execute any remaining migrations that were not part of the schema dump.
If your application's tests use a different database connection than the one you typically use during local development, you should ensure you have dumped a schema file using that database connection so that your tests are able to build your database. You may wish to do this after dumping the database connection you typically use during local development:
```


1php artisan schema:dump




2php artisan schema:dump --database=testing --prune




php artisan schema:dump
php artisan schema:dump --database=testing --prune

```

You should commit your database schema file to source control so that other new developers on your team may quickly create your application's initial database structure.
Migration squashing is only available for the MariaDB, MySQL, PostgreSQL, and SQLite databases and utilizes the database's command-line client.
