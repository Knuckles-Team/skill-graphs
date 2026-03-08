## [Running Migrations](https://laravel.com/docs/12.x/migrations#running-migrations)
To run all of your outstanding migrations, execute the `migrate` Artisan command:
```


1php artisan migrate




php artisan migrate

```

If you would like to see which migrations have already run and which are still pending, you may use the `migrate:status` Artisan command:
```


1php artisan migrate:status




php artisan migrate:status

```

If you provide the `--step` option to the `migrate` command, the command will run each migration as its own batch, allowing you to roll back individual migrations later using the `migrate:rollback` command:
```


1php artisan migrate --step




php artisan migrate --step

```

If you would like to see the SQL statements that will be executed by the migrations without actually running them, you may provide the `--pretend` flag to the `migrate` command:
```


1php artisan migrate --pretend




php artisan migrate --pretend

```

#### [Isolating Migration Execution](https://laravel.com/docs/12.x/migrations#isolating-migration-execution)
If you are deploying your application across multiple servers and running migrations as part of your deployment process, you likely do not want two servers attempting to migrate the database at the same time. To avoid this, you may use the `isolated` option when invoking the `migrate` command.
When the `isolated` option is provided, Laravel will acquire an atomic lock using your application's cache driver before attempting to run your migrations. All other attempts to run the `migrate` command while that lock is held will not execute; however, the command will still exit with a successful exit status code:
```


1php artisan migrate --isolated




php artisan migrate --isolated

```

To utilize this feature, your application must be using the `memcached`, `redis`, `dynamodb`, `database`, `file`, or `array` cache driver as your application's default cache driver. In addition, all servers must be communicating with the same central cache server.
#### [Forcing Migrations to Run in Production](https://laravel.com/docs/12.x/migrations#forcing-migrations-to-run-in-production)
Some migration operations are destructive, which means they may cause you to lose data. In order to protect you from running these commands against your production database, you will be prompted for confirmation before the commands are executed. To force the commands to run without a prompt, use the `--force` flag:
```


1php artisan migrate --force




php artisan migrate --force

```

### [Rolling Back Migrations](https://laravel.com/docs/12.x/migrations#rolling-back-migrations)
To roll back the latest migration operation, you may use the `rollback` Artisan command. This command rolls back the last "batch" of migrations, which may include multiple migration files:
```


1php artisan migrate:rollback




php artisan migrate:rollback

```

You may roll back a limited number of migrations by providing the `step` option to the `rollback` command. For example, the following command will roll back the last five migrations:
```


1php artisan migrate:rollback --step=5




php artisan migrate:rollback --step=5

```

You may roll back a specific "batch" of migrations by providing the `batch` option to the `rollback` command, where the `batch` option corresponds to a batch value within your application's `migrations` database table. For example, the following command will roll back all migrations in batch three:
```


1php artisan migrate:rollback --batch=3




php artisan migrate:rollback --batch=3

```

If you would like to see the SQL statements that will be executed by the migrations without actually running them, you may provide the `--pretend` flag to the `migrate:rollback` command:
```


1php artisan migrate:rollback --pretend




php artisan migrate:rollback --pretend

```

The `migrate:reset` command will roll back all of your application's migrations:
```


1php artisan migrate:reset




php artisan migrate:reset

```

#### [Roll Back and Migrate Using a Single Command](https://laravel.com/docs/12.x/migrations#roll-back-migrate-using-a-single-command)
The `migrate:refresh` command will roll back all of your migrations and then execute the `migrate` command. This command effectively re-creates your entire database:
```


1php artisan migrate:refresh




2 



3# Refresh the database and run all database seeds...




4php artisan migrate:refresh --seed




php artisan migrate:refresh

# Refresh the database and run all database seeds...
php artisan migrate:refresh --seed

```

You may roll back and re-migrate a limited number of migrations by providing the `step` option to the `refresh` command. For example, the following command will roll back and re-migrate the last five migrations:
```


1php artisan migrate:refresh --step=5




php artisan migrate:refresh --step=5

```

#### [Drop All Tables and Migrate](https://laravel.com/docs/12.x/migrations#drop-all-tables-migrate)
The `migrate:fresh` command will drop all tables from the database and then execute the `migrate` command:
```


1php artisan migrate:fresh




2 



3php artisan migrate:fresh --seed




php artisan migrate:fresh

php artisan migrate:fresh --seed

```

By default, the `migrate:fresh` command only drops tables from the default database connection. However, you may use the `--database` option to specify the database connection that should be migrated. The database connection name should correspond to a connection defined in your application's `database` [configuration file](https://laravel.com/docs/12.x/configuration):
```


1php artisan migrate:fresh --database=admin




php artisan migrate:fresh --database=admin

```

The `migrate:fresh` command will drop all database tables regardless of their prefix. This command should be used with caution when developing on a database that is shared with other applications.
