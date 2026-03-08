## [Basic Where Clauses](https://laravel.com/docs/12.x/queries#basic-where-clauses)
### [Where Clauses](https://laravel.com/docs/12.x/queries#where-clauses)
You may use the query builder's `where` method to add "where" clauses to the query. The most basic call to the `where` method requires three arguments. The first argument is the name of the column. The second argument is an operator, which can be any of the database's supported operators. The third argument is the value to compare against the column's value.
For example, the following query retrieves users where the value of the `votes` column is equal to `100` and the value of the `age` column is greater than `35`:
```


1$users = DB::table('users')




2    ->where('votes', '=', 100)




3    ->where('age', '>', 35)




4    ->get();




$users = DB::table('users')
    ->where('votes', '=', 100)
    ->where('age', '>', 35)
    ->get();

```

For convenience, if you want to verify that a column is `=` to a given value, you may pass the value as the second argument to the `where` method. Laravel will assume you would like to use the `=` operator:
```


1$users = DB::table('users')->where('votes', 100)->get();




$users = DB::table('users')->where('votes', 100)->get();

```

You may also provide an associative array to the `where` method to quickly query against multiple columns:
```


1$users = DB::table('users')->where([




2    'first_name' => 'Jane',




3    'last_name' => 'Doe',




4])->get();




$users = DB::table('users')->where([
    'first_name' => 'Jane',
    'last_name' => 'Doe',
])->get();

```

As previously mentioned, you may use any operator that is supported by your database system:
```


 1$users = DB::table('users')




 2    ->where('votes', '>=', 100)




 3    ->get();




 4 



 5$users = DB::table('users')




 6    ->where('votes', '<>', 100)




 7    ->get();




 8 



 9$users = DB::table('users')




10    ->where('name', 'like', 'T%')




11    ->get();




$users = DB::table('users')
    ->where('votes', '>=', 100)
    ->get();

$users = DB::table('users')
    ->where('votes', '<>', 100)
    ->get();

$users = DB::table('users')
    ->where('name', 'like', 'T%')
    ->get();

```

You may also pass an array of conditions to the `where` function. Each element of the array should be an array containing the three arguments typically passed to the `where` method:
```


1$users = DB::table('users')->where([




2    ['status', '=', '1'],




3    ['subscribed', '<>', '1'],




4])->get();




$users = DB::table('users')->where([
    ['status', '=', '1'],
    ['subscribed', '<>', '1'],
])->get();

```

PDO does not support binding column names. Therefore, you should never allow user input to dictate the column names referenced by your queries, including "order by" columns.
MySQL and MariaDB automatically typecast strings to integers in string-number comparisons. In this process, non-numeric strings are converted to `0`, which can lead to unexpected results. For example, if your table has a `secret` column with a value of `aaa` and you run `User::where('secret', 0)`, that row will be returned. To avoid this, ensure all values are typecast to their appropriate types before using them in queries.
### [Or Where Clauses](https://laravel.com/docs/12.x/queries#or-where-clauses)
When chaining together calls to the query builder's `where` method, the "where" clauses will be joined together using the `and` operator. However, you may use the `orWhere` method to join a clause to the query using the `or` operator. The `orWhere` method accepts the same arguments as the `where` method:
```


1$users = DB::table('users')




2    ->where('votes', '>', 100)




3    ->orWhere('name', 'John')




4    ->get();




$users = DB::table('users')
    ->where('votes', '>', 100)
    ->orWhere('name', 'John')
    ->get();

```

If you need to group an "or" condition within parentheses, you may pass a closure as the first argument to the `orWhere` method:
```


1use Illuminate\Database\Query\Builder;




2 



3$users = DB::table('users')




4    ->where('votes', '>', 100)




5    ->orWhere(function (Builder $query) {




6        $query->where('name', 'Abigail')




7            ->where('votes', '>', 50);




8        })




9    ->get();




use Illuminate\Database\Query\Builder;

$users = DB::table('users')
    ->where('votes', '>', 100)
    ->orWhere(function (Builder $query) {
        $query->where('name', 'Abigail')
            ->where('votes', '>', 50);
        })
    ->get();

```

The example above will produce the following SQL:
```


1select * from users where votes > 100 or (name = 'Abigail' and votes > 50)




select * from users where votes > 100 or (name = 'Abigail' and votes > 50)

```

You should always group `orWhere` calls in order to avoid unexpected behavior when global scopes are applied.
### [Where Not Clauses](https://laravel.com/docs/12.x/queries#where-not-clauses)
The `whereNot` and `orWhereNot` methods may be used to negate a given group of query constraints. For example, the following query excludes products that are on clearance or which have a price that is less than ten:
```


1$products = DB::table('products')




2    ->whereNot(function (Builder $query) {




3        $query->where('clearance', true)




4            ->orWhere('price', '<', 10);




5        })




6    ->get();




$products = DB::table('products')
    ->whereNot(function (Builder $query) {
        $query->where('clearance', true)
            ->orWhere('price', '<', 10);
        })
    ->get();

```

### [Where Any / All / None Clauses](https://laravel.com/docs/12.x/queries#where-any-all-none-clauses)
Sometimes you may need to apply the same query constraints to multiple columns. For example, you may want to retrieve all records where any columns in a given list are `LIKE` a given value. You may accomplish this using the `whereAny` method:
```


1$users = DB::table('users')




2    ->where('active', true)




3    ->whereAny([




4        'name',




5        'email',




6        'phone',




7    ], 'like', 'Example%')




8    ->get();




$users = DB::table('users')
    ->where('active', true)
    ->whereAny([
        'name',
        'email',
        'phone',
    ], 'like', 'Example%')
    ->get();

```

The query above will result in the following SQL:
```


1SELECT *




2FROM users




3WHERE active = true AND (




4    name LIKE 'Example%' OR




5    email LIKE 'Example%' OR




6    phone LIKE 'Example%'




7)




SELECT *
FROM users
WHERE active = true AND (
    name LIKE 'Example%' OR
    email LIKE 'Example%' OR
    phone LIKE 'Example%'
)

```

Similarly, the `whereAll` method may be used to retrieve records where all of the given columns match a given constraint:
```


1$posts = DB::table('posts')




2    ->where('published', true)




3    ->whereAll([




4        'title',




5        'content',




6    ], 'like', '%Laravel%')




7    ->get();




$posts = DB::table('posts')
    ->where('published', true)
    ->whereAll([
        'title',
        'content',
    ], 'like', '%Laravel%')
    ->get();

```

The query above will result in the following SQL:
```


1SELECT *




2FROM posts




3WHERE published = true AND (




4    title LIKE '%Laravel%' AND




5    content LIKE '%Laravel%'




6)




SELECT *
FROM posts
WHERE published = true AND (
    title LIKE '%Laravel%' AND
    content LIKE '%Laravel%'
)

```

The `whereNone` method may be used to retrieve records where none of the given columns match a given constraint:
```


1$albums = DB::table('albums')




2    ->where('published', true)




3    ->whereNone([




4        'title',




5        'lyrics',




6        'tags',




7    ], 'like', '%explicit%')




8    ->get();




$albums = DB::table('albums')
    ->where('published', true)
    ->whereNone([
        'title',
        'lyrics',
        'tags',
    ], 'like', '%explicit%')
    ->get();

```

The query above will result in the following SQL:
```


1SELECT *




2FROM albums




3WHERE published = true AND NOT (




4    title LIKE '%explicit%' OR




5    lyrics LIKE '%explicit%' OR




6    tags LIKE '%explicit%'




7)




SELECT *
FROM albums
WHERE published = true AND NOT (
    title LIKE '%explicit%' OR
    lyrics LIKE '%explicit%' OR
    tags LIKE '%explicit%'
)

```

### [JSON Where Clauses](https://laravel.com/docs/12.x/queries#json-where-clauses)
Laravel also supports querying JSON column types on databases that provide support for JSON column types. Currently, this includes MariaDB 10.3+, MySQL 8.0+, PostgreSQL 12.0+, SQL Server 2017+, and SQLite 3.39.0+. To query a JSON column, use the `->` operator:
```


1$users = DB::table('users')




2    ->where('preferences->dining->meal', 'salad')




3    ->get();




4 



5$users = DB::table('users')




6    ->whereIn('preferences->dining->meal', ['pasta', 'salad', 'sandwiches'])




7    ->get();




$users = DB::table('users')
    ->where('preferences->dining->meal', 'salad')
    ->get();

$users = DB::table('users')
    ->whereIn('preferences->dining->meal', ['pasta', 'salad', 'sandwiches'])
    ->get();

```

You may use the `whereJsonContains` and `whereJsonDoesntContain` methods to query JSON arrays:
```


1$users = DB::table('users')




2    ->whereJsonContains('options->languages', 'en')




3    ->get();




4 



5$users = DB::table('users')




6    ->whereJsonDoesntContain('options->languages', 'en')




7    ->get();




$users = DB::table('users')
    ->whereJsonContains('options->languages', 'en')
    ->get();

$users = DB::table('users')
    ->whereJsonDoesntContain('options->languages', 'en')
    ->get();

```

If your application uses the MariaDB, MySQL, or PostgreSQL databases, you may pass an array of values to the `whereJsonContains` and `whereJsonDoesntContain` methods:
```


1$users = DB::table('users')




2    ->whereJsonContains('options->languages', ['en', 'de'])




3    ->get();




4 



5$users = DB::table('users')




6    ->whereJsonDoesntContain('options->languages', ['en', 'de'])




7    ->get();




$users = DB::table('users')
    ->whereJsonContains('options->languages', ['en', 'de'])
    ->get();

$users = DB::table('users')
    ->whereJsonDoesntContain('options->languages', ['en', 'de'])
    ->get();

```

In addition, you may use the `whereJsonContainsKey` or `whereJsonDoesntContainKey` methods to retrieve the results that include or do not include a JSON key:
```


1$users = DB::table('users')




2    ->whereJsonContainsKey('preferences->dietary_requirements')




3    ->get();




4 



5$users = DB::table('users')




6    ->whereJsonDoesntContainKey('preferences->dietary_requirements')




7    ->get();




$users = DB::table('users')
    ->whereJsonContainsKey('preferences->dietary_requirements')
    ->get();

$users = DB::table('users')
    ->whereJsonDoesntContainKey('preferences->dietary_requirements')
    ->get();

```

Finally, you may use `whereJsonLength` method to query JSON arrays by their length:
```


1$users = DB::table('users')




2    ->whereJsonLength('options->languages', 0)




3    ->get();




4 



5$users = DB::table('users')




6    ->whereJsonLength('options->languages', '>', 1)




7    ->get();




$users = DB::table('users')
    ->whereJsonLength('options->languages', 0)
    ->get();

$users = DB::table('users')
    ->whereJsonLength('options->languages', '>', 1)
    ->get();

```

### [Additional Where Clauses](https://laravel.com/docs/12.x/queries#additional-where-clauses)
**whereLike / orWhereLike / whereNotLike / orWhereNotLike**
The `whereLike` method allows you to add "LIKE" clauses to your query for pattern matching. These methods provide a database-agnostic way of performing string matching queries, with the ability to toggle case-sensitivity. By default, string matching is case-insensitive:
```


1$users = DB::table('users')




2    ->whereLike('name', '%John%')




3    ->get();




$users = DB::table('users')
    ->whereLike('name', '%John%')
    ->get();

```

You can enable a case-sensitive search via the `caseSensitive` argument:
```


1$users = DB::table('users')




2    ->whereLike('name', '%John%', caseSensitive: true)




3    ->get();




$users = DB::table('users')
    ->whereLike('name', '%John%', caseSensitive: true)
    ->get();

```

The `orWhereLike` method allows you to add an "or" clause with a LIKE condition:
```


1$users = DB::table('users')




2    ->where('votes', '>', 100)




3    ->orWhereLike('name', '%John%')




4    ->get();




$users = DB::table('users')
    ->where('votes', '>', 100)
    ->orWhereLike('name', '%John%')
    ->get();

```

The `whereNotLike` method allows you to add "NOT LIKE" clauses to your query:
```


1$users = DB::table('users')




2    ->whereNotLike('name', '%John%')




3    ->get();




$users = DB::table('users')
    ->whereNotLike('name', '%John%')
    ->get();

```

Similarly, you can use `orWhereNotLike` to add an "or" clause with a NOT LIKE condition:
```


1$users = DB::table('users')




2    ->where('votes', '>', 100)




3    ->orWhereNotLike('name', '%John%')




4    ->get();




$users = DB::table('users')
    ->where('votes', '>', 100)
    ->orWhereNotLike('name', '%John%')
    ->get();

```

The `whereLike` case-sensitive search option is currently not supported on SQL Server.
**whereIn / whereNotIn / orWhereIn / orWhereNotIn**
The `whereIn` method verifies that a given column's value is contained within the given array:
```


1$users = DB::table('users')




2    ->whereIn('id', [1, 2, 3])




3    ->get();




$users = DB::table('users')
    ->whereIn('id', [1, 2, 3])
    ->get();

```

The `whereNotIn` method verifies that the given column's value is not contained in the given array:
```


1$users = DB::table('users')




2    ->whereNotIn('id', [1, 2, 3])




3    ->get();




$users = DB::table('users')
    ->whereNotIn('id', [1, 2, 3])
    ->get();

```

You may also provide a query object as the `whereIn` method's second argument:
```


1$activeUsers = DB::table('users')->select('id')->where('is_active', 1);




2 



3$comments = DB::table('comments')




4    ->whereIn('user_id', $activeUsers)




5    ->get();




$activeUsers = DB::table('users')->select('id')->where('is_active', 1);

$comments = DB::table('comments')
    ->whereIn('user_id', $activeUsers)
    ->get();

```

The example above will produce the following SQL:
```


1select * from comments where user_id in (




2    select id




3    from users




4    where is_active = 1




5)




select * from comments where user_id in (
    select id
    from users
    where is_active = 1
)

```

If you are adding a large array of integer bindings to your query, the `whereIntegerInRaw` or `whereIntegerNotInRaw` methods may be used to greatly reduce your memory usage.
**whereBetween / orWhereBetween**
The `whereBetween` method verifies that a column's value is between two values:
```


1$users = DB::table('users')




2    ->whereBetween('votes', [1, 100])




3    ->get();




$users = DB::table('users')
    ->whereBetween('votes', [1, 100])
    ->get();

```

**whereNotBetween / orWhereNotBetween**
The `whereNotBetween` method verifies that a column's value lies outside of two values:
```


1$users = DB::table('users')




2    ->whereNotBetween('votes', [1, 100])




3    ->get();




$users = DB::table('users')
    ->whereNotBetween('votes', [1, 100])
    ->get();

```

**whereBetweenColumns / whereNotBetweenColumns / orWhereBetweenColumns / orWhereNotBetweenColumns**
The `whereBetweenColumns` method verifies that a column's value is between the two values of two columns in the same table row:
```


1$patients = DB::table('patients')




2    ->whereBetweenColumns('weight', ['minimum_allowed_weight', 'maximum_allowed_weight'])




3    ->get();




$patients = DB::table('patients')
    ->whereBetweenColumns('weight', ['minimum_allowed_weight', 'maximum_allowed_weight'])
    ->get();

```

The `whereNotBetweenColumns` method verifies that a column's value lies outside the two values of two columns in the same table row:
```


1$patients = DB::table('patients')




2    ->whereNotBetweenColumns('weight', ['minimum_allowed_weight', 'maximum_allowed_weight'])




3    ->get();




$patients = DB::table('patients')
    ->whereNotBetweenColumns('weight', ['minimum_allowed_weight', 'maximum_allowed_weight'])
    ->get();

```

**whereValueBetween / whereValueNotBetween / orWhereValueBetween / orWhereValueNotBetween**
The `whereValueBetween` method verifies that a given value is between the values of two columns of the same type in the same table row:
```


1$products = DB::table('products')




2    ->whereValueBetween(100, ['min_price', 'max_price'])




3    ->get();




$products = DB::table('products')
    ->whereValueBetween(100, ['min_price', 'max_price'])
    ->get();

```

The `whereValueNotBetween` method verifies that a value lies outside the values of two columns in the same table row:
```


1$products = DB::table('products')




2    ->whereValueNotBetween(100, ['min_price', 'max_price'])




3    ->get();




$products = DB::table('products')
    ->whereValueNotBetween(100, ['min_price', 'max_price'])
    ->get();

```

**whereNull / whereNotNull / orWhereNull / orWhereNotNull**
The `whereNull` method verifies that the value of the given column is `NULL`:
```


1$users = DB::table('users')




2    ->whereNull('updated_at')




3    ->get();




$users = DB::table('users')
    ->whereNull('updated_at')
    ->get();

```

The `whereNotNull` method verifies that the column's value is not `NULL`:
```


1$users = DB::table('users')




2    ->whereNotNull('updated_at')




3    ->get();




$users = DB::table('users')
    ->whereNotNull('updated_at')
    ->get();

```

**whereDate / whereMonth / whereDay / whereYear / whereTime**
The `whereDate` method may be used to compare a column's value against a date:
```


1$users = DB::table('users')




2    ->whereDate('created_at', '2016-12-31')




3    ->get();




$users = DB::table('users')
    ->whereDate('created_at', '2016-12-31')
    ->get();

```

The `whereMonth` method may be used to compare a column's value against a specific month:
```


1$users = DB::table('users')




2    ->whereMonth('created_at', '12')




3    ->get();




$users = DB::table('users')
    ->whereMonth('created_at', '12')
    ->get();

```

The `whereDay` method may be used to compare a column's value against a specific day of the month:
```


1$users = DB::table('users')




2    ->whereDay('created_at', '31')




3    ->get();




$users = DB::table('users')
    ->whereDay('created_at', '31')
    ->get();

```

The `whereYear` method may be used to compare a column's value against a specific year:
```


1$users = DB::table('users')




2    ->whereYear('created_at', '2016')




3    ->get();




$users = DB::table('users')
    ->whereYear('created_at', '2016')
    ->get();

```

The `whereTime` method may be used to compare a column's value against a specific time:
```


1$users = DB::table('users')




2    ->whereTime('created_at', '=', '11:20:45')




3    ->get();




$users = DB::table('users')
    ->whereTime('created_at', '=', '11:20:45')
    ->get();

```

**wherePast / whereFuture / whereToday / whereBeforeToday / whereAfterToday**
The `wherePast` and `whereFuture` methods may be used to determine if a column's value is in the past or future:
```


1$invoices = DB::table('invoices')




2    ->wherePast('due_at')




3    ->get();




4 



5$invoices = DB::table('invoices')




6    ->whereFuture('due_at')




7    ->get();




$invoices = DB::table('invoices')
    ->wherePast('due_at')
    ->get();

$invoices = DB::table('invoices')
    ->whereFuture('due_at')
    ->get();

```

The `whereNowOrPast` and `whereNowOrFuture` methods may be used to determine if a column's value is in the past or future, inclusive of the current date and time:
```


1$invoices = DB::table('invoices')




2    ->whereNowOrPast('due_at')




3    ->get();




4 



5$invoices = DB::table('invoices')




6    ->whereNowOrFuture('due_at')




7    ->get();




$invoices = DB::table('invoices')
    ->whereNowOrPast('due_at')
    ->get();

$invoices = DB::table('invoices')
    ->whereNowOrFuture('due_at')
    ->get();

```

The `whereToday`, `whereBeforeToday`, and `whereAfterToday` methods may be used to determine if a column's value is today, before today, or after today, respectively:
```


 1$invoices = DB::table('invoices')




 2    ->whereToday('due_at')




 3    ->get();




 4 



 5$invoices = DB::table('invoices')




 6    ->whereBeforeToday('due_at')




 7    ->get();




 8 



 9$invoices = DB::table('invoices')




10    ->whereAfterToday('due_at')




11    ->get();




$invoices = DB::table('invoices')
    ->whereToday('due_at')
    ->get();

$invoices = DB::table('invoices')
    ->whereBeforeToday('due_at')
    ->get();

$invoices = DB::table('invoices')
    ->whereAfterToday('due_at')
    ->get();

```

Similarly, the `whereTodayOrBefore` and `whereTodayOrAfter` methods may be used to determine if a column's value is before today or after today, inclusive of today's date:
```


1$invoices = DB::table('invoices')




2    ->whereTodayOrBefore('due_at')




3    ->get();




4 



5$invoices = DB::table('invoices')




6    ->whereTodayOrAfter('due_at')




7    ->get();




$invoices = DB::table('invoices')
    ->whereTodayOrBefore('due_at')
    ->get();

$invoices = DB::table('invoices')
    ->whereTodayOrAfter('due_at')
    ->get();

```

**whereColumn / orWhereColumn**
The `whereColumn` method may be used to verify that two columns are equal:
```


1$users = DB::table('users')




2    ->whereColumn('first_name', 'last_name')




3    ->get();




$users = DB::table('users')
    ->whereColumn('first_name', 'last_name')
    ->get();

```

You may also pass a comparison operator to the `whereColumn` method:
```


1$users = DB::table('users')




2    ->whereColumn('updated_at', '>', 'created_at')




3    ->get();




$users = DB::table('users')
    ->whereColumn('updated_at', '>', 'created_at')
    ->get();

```

You may also pass an array of column comparisons to the `whereColumn` method. These conditions will be joined using the `and` operator:
```


1$users = DB::table('users')




2    ->whereColumn([




3        ['first_name', '=', 'last_name'],




4        ['updated_at', '>', 'created_at'],




5    ])->get();




$users = DB::table('users')
    ->whereColumn([
        ['first_name', '=', 'last_name'],
        ['updated_at', '>', 'created_at'],
    ])->get();

```

### [Logical Grouping](https://laravel.com/docs/12.x/queries#logical-grouping)
Sometimes you may need to group several "where" clauses within parentheses in order to achieve your query's desired logical grouping. In fact, you should generally always group calls to the `orWhere` method in parentheses in order to avoid unexpected query behavior. To accomplish this, you may pass a closure to the `where` method:
```


1$users = DB::table('users')




2    ->where('name', '=', 'John')




3    ->where(function (Builder $query) {




4        $query->where('votes', '>', 100)




5            ->orWhere('title', '=', 'Admin');




6    })




7    ->get();




$users = DB::table('users')
    ->where('name', '=', 'John')
    ->where(function (Builder $query) {
        $query->where('votes', '>', 100)
            ->orWhere('title', '=', 'Admin');
    })
    ->get();

```

As you can see, passing a closure into the `where` method instructs the query builder to begin a constraint group. The closure will receive a query builder instance which you can use to set the constraints that should be contained within the parenthesis group. The example above will produce the following SQL:
```


1select * from users where name = 'John' and (votes > 100 or title = 'Admin')




select * from users where name = 'John' and (votes > 100 or title = 'Admin')

```

You should always group `orWhere` calls in order to avoid unexpected behavior when global scopes are applied.
