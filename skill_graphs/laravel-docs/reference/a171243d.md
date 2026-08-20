## [Ordering, Grouping, Limit and Offset](https://laravel.com/docs/12.x/queries#ordering-grouping-limit-and-offset)
### [Ordering](https://laravel.com/docs/12.x/queries#ordering)
#### [The `orderBy` Method](https://laravel.com/docs/12.x/queries#orderby)
The `orderBy` method allows you to sort the results of the query by a given column. The first argument accepted by the `orderBy` method should be the column you wish to sort by, while the second argument determines the direction of the sort and may be either `asc` or `desc`:
```


1$users = DB::table('users')




2    ->orderBy('name', 'desc')




3    ->get();




$users = DB::table('users')
    ->orderBy('name', 'desc')
    ->get();

```

To sort by multiple columns, you may simply invoke `orderBy` as many times as necessary:
```


1$users = DB::table('users')




2    ->orderBy('name', 'desc')




3    ->orderBy('email', 'asc')




4    ->get();




$users = DB::table('users')
    ->orderBy('name', 'desc')
    ->orderBy('email', 'asc')
    ->get();

```

The sort direction is optional, and is ascending by default. If you want to sort in descending order, you can specify the second parameter for the `orderBy` method, or just use `orderByDesc`:
```


1$users = DB::table('users')




2    ->orderByDesc('verified_at')




3    ->get();




$users = DB::table('users')
    ->orderByDesc('verified_at')
    ->get();

```

Finally, using the `->` operator, the results can be sorted by a value within a JSON column:
```


1$corporations = DB::table('corporations')




2    ->where('country', 'US')




3    ->orderBy('location->state')




4    ->get();




$corporations = DB::table('corporations')
    ->where('country', 'US')
    ->orderBy('location->state')
    ->get();

```

#### [The `latest` and `oldest` Methods](https://laravel.com/docs/12.x/queries#latest-oldest)
The `latest` and `oldest` methods allow you to easily order results by date. By default, the result will be ordered by the table's `created_at` column. Or, you may pass the column name that you wish to sort by:
```


1$user = DB::table('users')




2    ->latest()




3    ->first();




$user = DB::table('users')
    ->latest()
    ->first();

```

#### [Random Ordering](https://laravel.com/docs/12.x/queries#random-ordering)
The `inRandomOrder` method may be used to sort the query results randomly. For example, you may use this method to fetch a random user:
```


1$randomUser = DB::table('users')




2    ->inRandomOrder()




3    ->first();




$randomUser = DB::table('users')
    ->inRandomOrder()
    ->first();

```

#### [Removing Existing Orderings](https://laravel.com/docs/12.x/queries#removing-existing-orderings)
The `reorder` method removes all of the "order by" clauses that have previously been applied to the query:
```


1$query = DB::table('users')->orderBy('name');




2 



3$unorderedUsers = $query->reorder()->get();




$query = DB::table('users')->orderBy('name');

$unorderedUsers = $query->reorder()->get();

```

You may pass a column and direction when calling the `reorder` method in order to remove all existing "order by" clauses and apply an entirely new order to the query:
```


1$query = DB::table('users')->orderBy('name');




2 



3$usersOrderedByEmail = $query->reorder('email', 'desc')->get();




$query = DB::table('users')->orderBy('name');

$usersOrderedByEmail = $query->reorder('email', 'desc')->get();

```

For convenience, you may use the `reorderDesc` method to reorder the query results in descending order:
```


1$query = DB::table('users')->orderBy('name');




2 



3$usersOrderedByEmail = $query->reorderDesc('email')->get();




$query = DB::table('users')->orderBy('name');

$usersOrderedByEmail = $query->reorderDesc('email')->get();

```

### [Grouping](https://laravel.com/docs/12.x/queries#grouping)
#### [The `groupBy` and `having` Methods](https://laravel.com/docs/12.x/queries#groupby-having)
As you might expect, the `groupBy` and `having` methods may be used to group the query results. The `having` method's signature is similar to that of the `where` method:
```


1$users = DB::table('users')




2    ->groupBy('account_id')




3    ->having('account_id', '>', 100)




4    ->get();




$users = DB::table('users')
    ->groupBy('account_id')
    ->having('account_id', '>', 100)
    ->get();

```

You can use the `havingBetween` method to filter the results within a given range:
```


1$report = DB::table('orders')




2    ->selectRaw('count(id) as number_of_orders, customer_id')




3    ->groupBy('customer_id')




4    ->havingBetween('number_of_orders', [5, 15])




5    ->get();




$report = DB::table('orders')
    ->selectRaw('count(id) as number_of_orders, customer_id')
    ->groupBy('customer_id')
    ->havingBetween('number_of_orders', [5, 15])
    ->get();

```

You may pass multiple arguments to the `groupBy` method to group by multiple columns:
```


1$users = DB::table('users')




2    ->groupBy('first_name', 'status')




3    ->having('account_id', '>', 100)




4    ->get();




$users = DB::table('users')
    ->groupBy('first_name', 'status')
    ->having('account_id', '>', 100)
    ->get();

```

To build more advanced `having` statements, see the [havingRaw](https://laravel.com/docs/12.x/queries#raw-methods) method.
### [Limit and Offset](https://laravel.com/docs/12.x/queries#limit-and-offset)
You may use the `limit` and `offset` methods to limit the number of results returned from the query or to skip a given number of results in the query:
```


1$users = DB::table('users')




2    ->offset(10)




3    ->limit(5)




4    ->get();




$users = DB::table('users')
    ->offset(10)
    ->limit(5)
    ->get();

```
