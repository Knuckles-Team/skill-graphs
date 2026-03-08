## [Tables](https://laravel.com/docs/12.x/migrations#tables)
### [Creating Tables](https://laravel.com/docs/12.x/migrations#creating-tables)
To create a new database table, use the `create` method on the `Schema` facade. The `create` method accepts two arguments: the first is the name of the table, while the second is a closure which receives a `Blueprint` object that may be used to define the new table:
```


1use Illuminate\Database\Schema\Blueprint;




2use Illuminate\Support\Facades\Schema;




3 



4Schema::create('users', function (Blueprint $table) {




5    $table->id();




6    $table->string('name');




7    $table->string('email');




8    $table->timestamps();




9});




use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::create('users', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('email');
    $table->timestamps();
});

```

When creating the table, you may use any of the schema builder's [column methods](https://laravel.com/docs/12.x/migrations#creating-columns) to define the table's columns.
#### [Determining Table / Column Existence](https://laravel.com/docs/12.x/migrations#determining-table-column-existence)
You may determine the existence of a table, column, or index using the `hashtable`, `hasColumn`, and `hasIndex` methods:
```


 1if (Schema::hashtable('users')) {




 2    // The "users" table exists...




 3}




 4 



 5if (Schema::hasColumn('users', 'email')) {




 6    // The "users" table exists and has an "email" column...




 7}




 8 



 9if (Schema::hasIndex('users', ['email'], 'unique')) {




10    // The "users" table exists and has a unique index on the "email" column...




11}




if (Schema::hashtable('users')) {
    // The "users" table exists...
}

if (Schema::hasColumn('users', 'email')) {
    // The "users" table exists and has an "email" column...
}

if (Schema::hasIndex('users', ['email'], 'unique')) {
    // The "users" table exists and has a unique index on the "email" column...
}

```

#### [Database Connection and Table Options](https://laravel.com/docs/12.x/migrations#database-connection-table-options)
If you want to perform a schema operation on a database connection that is not your application's default connection, use the `connection` method:
```


1Schema::connection('sqlite')->create('users', function (Blueprint $table) {




2    $table->id();




3});




Schema::connection('sqlite')->create('users', function (Blueprint $table) {
    $table->id();
});

```

In addition, a few other properties and methods may be used to define other aspects of the table's creation. The `engine` property may be used to specify the table's storage engine when using MariaDB or MySQL:
```


1Schema::create('users', function (Blueprint $table) {




2    $table->engine('InnoDB');




3 



4    // ...




5});




Schema::create('users', function (Blueprint $table) {
    $table->engine('InnoDB');

    // ...
});

```

The `charset` and `collation` properties may be used to specify the character set and collation for the created table when using MariaDB or MySQL:
```


1Schema::create('users', function (Blueprint $table) {




2    $table->charset('utf8mb4');




3    $table->collation('utf8mb4_unicode_ci');




4 



5    // ...




6});




Schema::create('users', function (Blueprint $table) {
    $table->charset('utf8mb4');
    $table->collation('utf8mb4_unicode_ci');

    // ...
});

```

The `temporary` method may be used to indicate that the table should be "temporary". Temporary tables are only visible to the current connection's database session and are dropped automatically when the connection is closed:
```


1Schema::create('calculations', function (Blueprint $table) {




2    $table->temporary();




3 



4    // ...




5});




Schema::create('calculations', function (Blueprint $table) {
    $table->temporary();

    // ...
});

```

If you would like to add a "comment" to a database table, you may invoke the `comment` method on the table instance. Table comments are currently only supported by MariaDB, MySQL, and PostgreSQL:
```


1Schema::create('calculations', function (Blueprint $table) {




2    $table->comment('Business calculations');




3 



4    // ...




5});




Schema::create('calculations', function (Blueprint $table) {
    $table->comment('Business calculations');

    // ...
});

```

### [Updating Tables](https://laravel.com/docs/12.x/migrations#updating-tables)
The `table` method on the `Schema` facade may be used to update existing tables. Like the `create` method, the `table` method accepts two arguments: the name of the table and a closure that receives a `Blueprint` instance you may use to add columns or indexes to the table:
```


1use Illuminate\Database\Schema\Blueprint;




2use Illuminate\Support\Facades\Schema;




3 



4Schema::table('users', function (Blueprint $table) {




5    $table->integer('votes');




6});




use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::table('users', function (Blueprint $table) {
    $table->integer('votes');
});

```

### [Renaming / Dropping Tables](https://laravel.com/docs/12.x/migrations#renaming-and-dropping-tables)
To rename an existing database table, use the `rename` method:
```


1use Illuminate\Support\Facades\Schema;




2 



3Schema::rename($from, $to);




use Illuminate\Support\Facades\Schema;

Schema::rename($from, $to);

```

To drop an existing table, you may use the `drop` or `dropIfExists` methods:
```


1Schema::drop('users');




2 



3Schema::dropIfExists('users');




Schema::drop('users');

Schema::dropIfExists('users');

```

#### [Renaming Tables With Foreign Keys](https://laravel.com/docs/12.x/migrations#renaming-tables-with-foreign-keys)
Before renaming a table, you should verify that any foreign key constraints on the table have an explicit name in your migration files instead of letting Laravel assign a convention based name. Otherwise, the foreign key constraint name will refer to the old table name.
