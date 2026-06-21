## [Select Statements](https://laravel.com/docs/12.x/queries#select-statements)
#### [Specifying a Select Clause](https://laravel.com/docs/12.x/queries#specifying-a-select-clause)
You may not always want to select all columns from a database table. Using the `select` method, you can specify a custom "select" clause for the query:
```


1use Illuminate\Support\Facades\DB;




2 



3$users = DB::table('users')




4    ->select('name', 'email as user_email')




5    ->get();




use Illuminate\Support\Facades\DB;

$users = DB::table('users')
    ->select('name', 'email as user_email')
    ->get();

```

The `distinct` method allows you to force the query to return distinct results:
```


1$users = DB::table('users')->distinct()->get();




$users = DB::table('users')->distinct()->get();

```

If you already have a query builder instance and you wish to add a column to its existing select clause, you may use the `addSelect` method:
```


1$query = DB::table('users')->select('name');




2 



3$users = $query->addSelect('age')->get();




$query = DB::table('users')->select('name');

$users = $query->addSelect('age')->get();

```
