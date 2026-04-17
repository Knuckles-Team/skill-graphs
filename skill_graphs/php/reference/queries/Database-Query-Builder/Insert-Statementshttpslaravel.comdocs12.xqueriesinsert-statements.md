## [Insert Statements](https://laravel.com/docs/12.x/queries#insert-statements)
The query builder also provides an `insert` method that may be used to insert records into the database table. The `insert` method accepts an array of column names and values:
```


1DB::table('users')->insert([




2    'email' => 'kayla@example.com',




3    'votes' => 0




4]);




DB::table('users')->insert([
    'email' => 'kayla@example.com',
    'votes' => 0
]);

```

You may insert several records at once by passing an array of arrays. Each array represents a record that should be inserted into the table:
```


1DB::table('users')->insert([




2    ['email' => 'picard@example.com', 'votes' => 0],




3    ['email' => 'janeway@example.com', 'votes' => 0],




4]);




DB::table('users')->insert([
    ['email' => 'picard@example.com', 'votes' => 0],
    ['email' => 'janeway@example.com', 'votes' => 0],
]);

```

The `insertOrIgnore` method will ignore errors while inserting records into the database. When using this method, you should be aware that duplicate record errors will be ignored and other types of errors may also be ignored depending on the database engine. For example, `insertOrIgnore` will
```


1DB::table('users')->insertOrIgnore([




2    ['id' => 1, 'email' => 'sisko@example.com'],




3    ['id' => 2, 'email' => 'archer@example.com'],




4]);




DB::table('users')->insertOrIgnore([
    ['id' => 1, 'email' => 'sisko@example.com'],
    ['id' => 2, 'email' => 'archer@example.com'],
]);

```

The `insertUsing` method will insert new records into the table while using a subquery to determine the data that should be inserted:
```


1DB::table('pruned_users')->insertUsing([




2    'id', 'name', 'email', 'email_verified_at'




3], DB::table('users')->select(




4    'id', 'name', 'email', 'email_verified_at'




5)->where('updated_at', '<=', now()->minus(months: 1)));




DB::table('pruned_users')->insertUsing([
    'id', 'name', 'email', 'email_verified_at'
], DB::table('users')->select(
    'id', 'name', 'email', 'email_verified_at'
)->where('updated_at', '<=', now()->minus(months: 1)));

```

#### [Auto-Incrementing IDs](https://laravel.com/docs/12.x/queries#auto-incrementing-ids)
If the table has an auto-incrementing id, use the `insertGetId` method to insert a record and then retrieve the ID:
```


1$id = DB::table('users')->insertGetId(




2    ['email' => 'john@example.com', 'votes' => 0]




3);




$id = DB::table('users')->insertGetId(
    ['email' => 'john@example.com', 'votes' => 0]
);

```

When using PostgreSQL the `insertGetId` method expects the auto-incrementing column to be named `id`. If you would like to retrieve the ID from a different "sequence", you may pass the column name as the second parameter to the `insertGetId` method.
### [Upserts](https://laravel.com/docs/12.x/queries#upserts)
The `upsert` method will insert records that do not exist and update the records that already exist with new values that you may specify. The method's first argument consists of the values to insert or update, while the second argument lists the column(s) that uniquely identify records within the associated table. The method's third and final argument is an array of columns that should be updated if a matching record already exists in the database:
```


1DB::table('flights')->upsert(




2    [




3        ['departure' => 'Oakland', 'destination' => 'San Diego', 'price' => 99],




4        ['departure' => 'Chicago', 'destination' => 'New York', 'price' => 150]




5    ],




6    ['departure', 'destination'],




7    ['price']




8);




DB::table('flights')->upsert(
    [
        ['departure' => 'Oakland', 'destination' => 'San Diego', 'price' => 99],
        ['departure' => 'Chicago', 'destination' => 'New York', 'price' => 150]
    ],
    ['departure', 'destination'],
    ['price']
);

```

In the example above, Laravel will attempt to insert two records. If a record already exists with the same `departure` and `destination` column values, Laravel will update that record's `price` column.
All databases except SQL Server require the columns in the second argument of the `upsert` method to have a "primary" or "unique" index. In addition, the MariaDB and MySQL database drivers ignore the second argument of the `upsert` method and always use the "primary" and "unique" indexes of the table to detect existing records.
