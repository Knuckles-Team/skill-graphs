## [Update Statements](https://laravel.com/docs/12.x/queries#update-statements)
In addition to inserting records into the database, the query builder can also update existing records using the `update` method. The `update` method, like the `insert` method, accepts an array of column and value pairs indicating the columns to be updated. The `update` method returns the number of affected rows. You may constrain the `update` query using `where` clauses:
```


1$affected = DB::table('users')




2    ->where('id', 1)




3    ->update(['votes' => 1]);




$affected = DB::table('users')
    ->where('id', 1)
    ->update(['votes' => 1]);

```

#### [Update or Insert](https://laravel.com/docs/12.x/queries#update-or-insert)
Sometimes you may want to update an existing record in the database or create it if no matching record exists. In this scenario, the `updateOrInsert` method may be used. The `updateOrInsert` method accepts two arguments: an array of conditions by which to find the record, and an array of column and value pairs indicating the columns to be updated.
The `updateOrInsert` method will attempt to locate a matching database record using the first argument's column and value pairs. If the record exists, it will be updated with the values in the second argument. If the record cannot be found, a new record will be inserted with the merged attributes of both arguments:
```


1DB::table('users')




2    ->updateOrInsert(




3        ['email' => 'john@example.com', 'name' => 'John'],




4        ['votes' => '2']




5    );




DB::table('users')
    ->updateOrInsert(
        ['email' => 'john@example.com', 'name' => 'John'],
        ['votes' => '2']
    );

```

You may provide a closure to the `updateOrInsert` method to customize the attributes that are updated or inserted into the database based on the existence of a matching record:
```


 1DB::table('users')->updateOrInsert(




 2    ['user_id' => $user_id],




 3    fn ($exists) => $exists ? [




 4        'name' => $data['name'],




 5        'email' => $data['email'],




 6    ] : [




 7        'name' => $data['name'],




 8        'email' => $data['email'],




 9        'marketable' => true,




10    ],




11);




DB::table('users')->updateOrInsert(
    ['user_id' => $user_id],
    fn ($exists) => $exists ? [
        'name' => $data['name'],
        'email' => $data['email'],
    ] : [
        'name' => $data['name'],
        'email' => $data['email'],
        'marketable' => true,
    ],
);

```

### [Updating JSON Columns](https://laravel.com/docs/12.x/queries#updating-json-columns)
When updating a JSON column, you should use `->` syntax to update the appropriate key in the JSON object. This operation is supported on MariaDB 10.3+, MySQL 5.7+, and PostgreSQL 9.5+:
```


1$affected = DB::table('users')




2    ->where('id', 1)




3    ->update(['options->enabled' => true]);




$affected = DB::table('users')
    ->where('id', 1)
    ->update(['options->enabled' => true]);

```

### [Increment and Decrement](https://laravel.com/docs/12.x/queries#increment-and-decrement)
The query builder also provides convenient methods for incrementing or decrementing the value of a given column. Both of these methods accept at least one argument: the column to modify. A second argument may be provided to specify the amount by which the column should be incremented or decremented:
```


1DB::table('users')->increment('votes');




2 



3DB::table('users')->increment('votes', 5);




4 



5DB::table('users')->decrement('votes');




6 



7DB::table('users')->decrement('votes', 5);




DB::table('users')->increment('votes');

DB::table('users')->increment('votes', 5);

DB::table('users')->decrement('votes');

DB::table('users')->decrement('votes', 5);

```

If needed, you may also specify additional columns to update during the increment or decrement operation:
```


1DB::table('users')->increment('votes', 1, ['name' => 'John']);




DB::table('users')->increment('votes', 1, ['name' => 'John']);

```

In addition, you may increment or decrement multiple columns at once using the `incrementEach` and `decrementEach` methods:
```


1DB::table('users')->incrementEach([




2    'votes' => 5,




3    'balance' => 100,




4]);




DB::table('users')->incrementEach([
    'votes' => 5,
    'balance' => 100,
]);

```
