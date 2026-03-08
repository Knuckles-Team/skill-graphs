## [Indexes](https://laravel.com/docs/12.x/migrations#indexes)
### [Creating Indexes](https://laravel.com/docs/12.x/migrations#creating-indexes)
The Laravel schema builder supports several types of indexes. The following example creates a new `email` column and specifies that its values should be unique. To create the index, we can chain the `unique` method onto the column definition:
```


1use Illuminate\Database\Schema\Blueprint;




2use Illuminate\Support\Facades\Schema;




3 



4Schema::table('users', function (Blueprint $table) {




5    $table->string('email')->unique();




6});




use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::table('users', function (Blueprint $table) {
    $table->string('email')->unique();
});

```

Alternatively, you may create the index after defining the column. To do so, you should call the `unique` method on the schema builder blueprint. This method accepts the name of the column that should receive a unique index:
```


1$table->unique('email');




$table->unique('email');

```

You may even pass an array of columns to an index method to create a compound (or composite) index:
```


1$table->index(['account_id', 'created_at']);




$table->index(['account_id', 'created_at']);

```

When creating an index, Laravel will automatically generate an index name based on the table, column names, and the index type, but you may pass a second argument to the method to specify the index name yourself:
```


1$table->unique('email', 'unique_email');




$table->unique('email', 'unique_email');

```

#### [Available Index Types](https://laravel.com/docs/12.x/migrations#available-index-types)
Laravel's schema builder blueprint class provides methods for creating each type of index supported by Laravel. Each index method accepts an optional second argument to specify the name of the index. If omitted, the name will be derived from the names of the table and column(s) used for the index, as well as the index type. Each of the available index methods is described in the table below:
Command | Description
---|---
`$table->primary('id');` | Adds a primary key.
`$table->primary(['id', 'parent_id']);` | Adds composite keys.
`$table->unique('email');` | Adds a unique index.
`$table->index('state');` | Adds an index.
`$table->fullText('body');` | Adds a full text index (MariaDB / MySQL / PostgreSQL).
`$table->fullText('body')->language('english');` | Adds a full text index of the specified language (PostgreSQL).
`$table->spatialIndex('location');` | Adds a spatial index (except SQLite).
#### [Online Index Creation](https://laravel.com/docs/12.x/migrations#online-index-creation)
By default, creating an index on a large table can lock the table and block reads or writes while the index is being built. When using PostgreSQL or SQL Server, you may chain the `online` method onto an index definition to create the index without locking the table, allowing your application to continue reading and writing data during index creation:
```


1$table->string('email')->unique()->online();




$table->string('email')->unique()->online();

```

When using PostgreSQL, this adds the `CONCURRENTLY` option to the index creation statement. When using SQL Server, this adds the `WITH (online = on)` option.
### [Renaming Indexes](https://laravel.com/docs/12.x/migrations#renaming-indexes)
To rename an index, you may use the `renameIndex` method provided by the schema builder blueprint. This method accepts the current index name as its first argument and the desired name as its second argument:
```


1$table->renameIndex('from', 'to')




$table->renameIndex('from', 'to')

```

### [Dropping Indexes](https://laravel.com/docs/12.x/migrations#dropping-indexes)
To drop an index, you must specify the index's name. By default, Laravel automatically assigns an index name based on the table name, the name of the indexed column, and the index type. Here are some examples:
Command | Description
---|---
`$table->dropPrimary('users_id_primary');` | Drop a primary key from the "users" table.
`$table->dropUnique('users_email_unique');` | Drop a unique index from the "users" table.
`$table->dropIndex('geo_state_index');` | Drop a basic index from the "geo" table.
`$table->dropFullText('posts_body_fulltext');` | Drop a full text index from the "posts" table.
`$table->dropSpatialIndex('geo_location_spatialindex');` | Drop a spatial index from the "geo" table (except SQLite).
If you pass an array of columns into a method that drops indexes, the conventional index name will be generated based on the table name, columns, and index type:
```


1Schema::table('geo', function (Blueprint $table) {




2    $table->dropIndex(['state']); // Drops index 'geo_state_index'




3});




Schema::table('geo', function (Blueprint $table) {
    $table->dropIndex(['state']); // Drops index 'geo_state_index'
});

```

### [Foreign Key Constraints](https://laravel.com/docs/12.x/migrations#foreign-key-constraints)
Laravel also provides support for creating foreign key constraints, which are used to force referential integrity at the database level. For example, let's define a `user_id` column on the `posts` table that references the `id` column on a `users` table:
```


1use Illuminate\Database\Schema\Blueprint;




2use Illuminate\Support\Facades\Schema;




3 



4Schema::table('posts', function (Blueprint $table) {




5    $table->unsignedBigInteger('user_id');




6 



7    $table->foreign('user_id')->references('id')->on('users');




8});




use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::table('posts', function (Blueprint $table) {
    $table->unsignedBigInteger('user_id');

    $table->foreign('user_id')->references('id')->on('users');
});

```

Since this syntax is rather verbose, Laravel provides additional, terser methods that use conventions to provide a better developer experience. When using the `foreignId` method to create your column, the example above can be rewritten like so:
```


1Schema::table('posts', function (Blueprint $table) {




2    $table->foreignId('user_id')->constrained();




3});




Schema::table('posts', function (Blueprint $table) {
    $table->foreignId('user_id')->constrained();
});

```

The `foreignId` method creates an `UNSIGNED BIGINT` equivalent column, while the `constrained` method will use conventions to determine the table and column being referenced. If your table name does not match Laravel's conventions, you may manually provide it to the `constrained` method. In addition, the name that should be assigned to the generated index may be specified as well:
```


1Schema::table('posts', function (Blueprint $table) {




2    $table->foreignId('user_id')->constrained(




3        table: 'users', indexName: 'posts_user_id'




4    );




5});




Schema::table('posts', function (Blueprint $table) {
    $table->foreignId('user_id')->constrained(
        table: 'users', indexName: 'posts_user_id'
    );
});

```

You may also specify the desired action for the "on delete" and "on update" properties of the constraint:
```


1$table->foreignId('user_id')




2    ->constrained()




3    ->onUpdate('cascade')




4    ->onDelete('cascade');




$table->foreignId('user_id')
    ->constrained()
    ->onUpdate('cascade')
    ->onDelete('cascade');

```

An alternative, expressive syntax is also provided for these actions:
Method | Description
---|---
`$table->cascadeOnUpdate();` | Updates should cascade.
`$table->restrictOnUpdate();` | Updates should be restricted.
`$table->nullOnUpdate();` | Updates should set the foreign key value to null.
`$table->noActionOnUpdate();` | No action on updates.
`$table->cascadeOnDelete();` | Deletes should cascade.
`$table->restrictOnDelete();` | Deletes should be restricted.
`$table->nullOnDelete();` | Deletes should set the foreign key value to null.
`$table->noActionOnDelete();` | Prevents deletes if child records exist.
Any additional [column modifiers](https://laravel.com/docs/12.x/migrations#column-modifiers) must be called before the `constrained` method:
```


1$table->foreignId('user_id')




2    ->nullable()




3    ->constrained();




$table->foreignId('user_id')
    ->nullable()
    ->constrained();

```

#### [Dropping Foreign Keys](https://laravel.com/docs/12.x/migrations#dropping-foreign-keys)
To drop a foreign key, you may use the `dropForeign` method, passing the name of the foreign key constraint to be deleted as an argument. Foreign key constraints use the same naming convention as indexes. In other words, the foreign key constraint name is based on the name of the table and the columns in the constraint, followed by a "_foreign" suffix:
```


1$table->dropForeign('posts_user_id_foreign');




$table->dropForeign('posts_user_id_foreign');

```

Alternatively, you may pass an array containing the column name that holds the foreign key to the `dropForeign` method. The array will be converted to a foreign key constraint name using Laravel's constraint naming conventions:
```


1$table->dropForeign(['user_id']);




$table->dropForeign(['user_id']);

```

#### [Toggling Foreign Key Constraints](https://laravel.com/docs/12.x/migrations#toggling-foreign-key-constraints)
You may enable or disable foreign key constraints within your migrations by using the following methods:
```


1Schema::enableForeignKeyConstraints();




2 



3Schema::disableForeignKeyConstraints();




4 



5Schema::withoutForeignKeyConstraints(function () {




6    // Constraints disabled within this closure...




7});




Schema::enableForeignKeyConstraints();

Schema::disableForeignKeyConstraints();

Schema::withoutForeignKeyConstraints(function () {
    // Constraints disabled within this closure...
});

```

SQLite disables foreign key constraints by default. When using SQLite, make sure to [enable foreign key support](https://laravel.com/docs/12.x/database#configuration) in your database configuration before attempting to create them in your migrations.
