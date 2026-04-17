## [Unions](https://laravel.com/docs/12.x/queries#unions)
The query builder also provides a convenient method to "union" two or more queries together. For example, you may create an initial query and use the `union` method to union it with more queries:
```


1use Illuminate\Support\Facades\DB;




2 



3$usersWithoutFirstName = DB::table('users')




4    ->whereNull('first_name');




5 



6$users = DB::table('users')




7    ->whereNull('last_name')




8    ->union($usersWithoutFirstName)




9    ->get();




use Illuminate\Support\Facades\DB;

$usersWithoutFirstName = DB::table('users')
    ->whereNull('first_name');

$users = DB::table('users')
    ->whereNull('last_name')
    ->union($usersWithoutFirstName)
    ->get();

```

In addition to the `union` method, the query builder provides a `unionAll` method. Queries that are combined using the `unionAll` method will not have their duplicate results removed. The `unionAll` method has the same method signature as the `union` method.
