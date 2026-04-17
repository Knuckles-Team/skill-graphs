## [Joins](https://laravel.com/docs/12.x/queries#joins)
#### [Inner Join Clause](https://laravel.com/docs/12.x/queries#inner-join-clause)
The query builder may also be used to add join clauses to your queries. To perform a basic "inner join", you may use the `join` method on a query builder instance. The first argument passed to the `join` method is the name of the table you need to join to, while the remaining arguments specify the column constraints for the join. You may even join multiple tables in a single query:
```


1use Illuminate\Support\Facades\DB;




2 



3$users = DB::table('users')




4    ->join('contacts', 'users.id', '=', 'contacts.user_id')




5    ->join('orders', 'users.id', '=', 'orders.user_id')




6    ->select('users.*', 'contacts.phone', 'orders.price')




7    ->get();




use Illuminate\Support\Facades\DB;

$users = DB::table('users')
    ->join('contacts', 'users.id', '=', 'contacts.user_id')
    ->join('orders', 'users.id', '=', 'orders.user_id')
    ->select('users.*', 'contacts.phone', 'orders.price')
    ->get();

```

#### [Left Join / Right Join Clause](https://laravel.com/docs/12.x/queries#left-join-right-join-clause)
If you would like to perform a "left join" or "right join" instead of an "inner join", use the `leftJoin` or `rightJoin` methods. These methods have the same signature as the `join` method:
```


1$users = DB::table('users')




2    ->leftJoin('posts', 'users.id', '=', 'posts.user_id')




3    ->get();




4 



5$users = DB::table('users')




6    ->rightJoin('posts', 'users.id', '=', 'posts.user_id')




7    ->get();




$users = DB::table('users')
    ->leftJoin('posts', 'users.id', '=', 'posts.user_id')
    ->get();

$users = DB::table('users')
    ->rightJoin('posts', 'users.id', '=', 'posts.user_id')
    ->get();

```

#### [Cross Join Clause](https://laravel.com/docs/12.x/queries#cross-join-clause)
You may use the `crossJoin` method to perform a "cross join". Cross joins generate a cartesian product between the first table and the joined table:
```


1$sizes = DB::table('sizes')




2    ->crossJoin('colors')




3    ->get();




$sizes = DB::table('sizes')
    ->crossJoin('colors')
    ->get();

```

#### [Advanced Join Clauses](https://laravel.com/docs/12.x/queries#advanced-join-clauses)
You may also specify more advanced join clauses. To get started, pass a closure as the second argument to the `join` method. The closure will receive a `Illuminate\Database\Query\JoinClause` instance which allows you to specify constraints on the "join" clause:
```


1DB::table('users')




2    ->join('contacts', function (JoinClause $join) {




3        $join->on('users.id', '=', 'contacts.user_id')->orOn(/* ... */);




4    })




5    ->get();




DB::table('users')
    ->join('contacts', function (JoinClause $join) {
        $join->on('users.id', '=', 'contacts.user_id')->orOn(/* ... */);
    })
    ->get();

```

If you would like to use a "where" clause on your joins, you may use the `where` and `orWhere` methods provided by the `JoinClause` instance. Instead of comparing two columns, these methods will compare the column against a value:
```


1DB::table('users')




2    ->join('contacts', function (JoinClause $join) {




3        $join->on('users.id', '=', 'contacts.user_id')




4            ->where('contacts.user_id', '>', 5);




5    })




6    ->get();




DB::table('users')
    ->join('contacts', function (JoinClause $join) {
        $join->on('users.id', '=', 'contacts.user_id')
            ->where('contacts.user_id', '>', 5);
    })
    ->get();

```

#### [Subquery Joins](https://laravel.com/docs/12.x/queries#subquery-joins)
You may use the `joinSub`, `leftJoinSub`, and `rightJoinSub` methods to join a query to a subquery. Each of these methods receives three arguments: the subquery, its table alias, and a closure that defines the related columns. In this example, we will retrieve a collection of users where each user record also contains the `created_at` timestamp of the user's most recently published blog post:
```


1$latestPosts = DB::table('posts')




2    ->select('user_id', DB::raw('MAX(created_at) as last_post_created_at'))




3    ->where('is_published', true)




4    ->groupBy('user_id');




5 



6$users = DB::table('users')




7    ->joinSub($latestPosts, 'latest_posts', function (JoinClause $join) {




8        $join->on('users.id', '=', 'latest_posts.user_id');




9    })->get();




$latestPosts = DB::table('posts')
    ->select('user_id', DB::raw('MAX(created_at) as last_post_created_at'))
    ->where('is_published', true)
    ->groupBy('user_id');

$users = DB::table('users')
    ->joinSub($latestPosts, 'latest_posts', function (JoinClause $join) {
        $join->on('users.id', '=', 'latest_posts.user_id');
    })->get();

```

#### [Lateral Joins](https://laravel.com/docs/12.x/queries#lateral-joins)
Lateral joins are currently supported by PostgreSQL, MySQL >= 8.0.14, and SQL Server.
You may use the `joinLateral` and `leftJoinLateral` methods to perform a "lateral join" with a subquery. Each of these methods receives two arguments: the subquery and its table alias. The join condition(s) should be specified within the `where` clause of the given subquery. Lateral joins are evaluated for each row and can reference columns outside the subquery.
In this example, we will retrieve a collection of users as well as the user's three most recent blog posts. Each user can produce up to three rows in the result set: one for each of their most recent blog posts. The join condition is specified with a `whereColumn` clause within the subquery, referencing the current user row:
```


1$latestPosts = DB::table('posts')




2    ->select('id as post_id', 'title as post_title', 'created_at as post_created_at')




3    ->whereColumn('user_id', 'users.id')




4    ->orderBy('created_at', 'desc')




5    ->limit(3);




6 



7$users = DB::table('users')




8    ->joinLateral($latestPosts, 'latest_posts')




9    ->get();




$latestPosts = DB::table('posts')
    ->select('id as post_id', 'title as post_title', 'created_at as post_created_at')
    ->whereColumn('user_id', 'users.id')
    ->orderBy('created_at', 'desc')
    ->limit(3);

$users = DB::table('users')
    ->joinLateral($latestPosts, 'latest_posts')
    ->get();

```
