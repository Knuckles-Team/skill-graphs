## [Raw Expressions](https://laravel.com/docs/12.x/queries#raw-expressions)
Sometimes you may need to insert an arbitrary string into a query. To create a raw string expression, you may use the `raw` method provided by the `DB` facade:
```


1$users = DB::table('users')




2    ->select(DB::raw('count(*) as user_count, status'))




3    ->where('status', '<>', 1)




4    ->groupBy('status')




5    ->get();




$users = DB::table('users')
    ->select(DB::raw('count(*) as user_count, status'))
    ->where('status', '<>', 1)
    ->groupBy('status')
    ->get();

```

Raw statements will be injected into the query as strings, so you should be extremely careful to avoid creating SQL injection vulnerabilities.
### [Raw Methods](https://laravel.com/docs/12.x/queries#raw-methods)
Instead of using the `DB::raw` method, you may also use the following methods to insert a raw expression into various parts of your query. **Remember, Laravel cannot guarantee that any query using raw expressions is protected against SQL injection vulnerabilities.**
#### [`selectRaw`](https://laravel.com/docs/12.x/queries#selectraw)
The `selectRaw` method can be used in place of `addSelect(DB::raw(/* ... */))`. This method accepts an optional array of bindings as its second argument:
```


1$orders = DB::table('orders')




2    ->selectRaw('price * ? as price_with_tax', [1.0825])




3    ->get();




$orders = DB::table('orders')
    ->selectRaw('price * ? as price_with_tax', [1.0825])
    ->get();

```

#### [`whereRaw / orWhereRaw`](https://laravel.com/docs/12.x/queries#whereraw-orwhereraw)
The `whereRaw` and `orWhereRaw` methods can be used to inject a raw "where" clause into your query. These methods accept an optional array of bindings as their second argument:
```


1$orders = DB::table('orders')




2    ->whereRaw('price > IF(state = "TX", ?, 100)', [200])




3    ->get();




$orders = DB::table('orders')
    ->whereRaw('price > IF(state = "TX", ?, 100)', [200])
    ->get();

```

#### [`havingRaw / orHavingRaw`](https://laravel.com/docs/12.x/queries#havingraw-orhavingraw)
The `havingRaw` and `orHavingRaw` methods may be used to provide a raw string as the value of the "having" clause. These methods accept an optional array of bindings as their second argument:
```


1$orders = DB::table('orders')




2    ->select('department', DB::raw('SUM(price) as total_sales'))




3    ->groupBy('department')




4    ->havingRaw('SUM(price) > ?', [2500])




5    ->get();




$orders = DB::table('orders')
    ->select('department', DB::raw('SUM(price) as total_sales'))
    ->groupBy('department')
    ->havingRaw('SUM(price) > ?', [2500])
    ->get();

```

#### [`orderByRaw`](https://laravel.com/docs/12.x/queries#orderbyraw)
The `orderByRaw` method may be used to provide a raw string as the value of the "order by" clause:
```


1$orders = DB::table('orders')




2    ->orderByRaw('updated_at - created_at DESC')




3    ->get();




$orders = DB::table('orders')
    ->orderByRaw('updated_at - created_at DESC')
    ->get();

```

### [`groupByRaw`](https://laravel.com/docs/12.x/queries#groupbyraw)
The `groupByRaw` method may be used to provide a raw string as the value of the `group by` clause:
```


1$orders = DB::table('orders')




2    ->select('city', 'state')




3    ->groupByRaw('city, state')




4    ->get();




$orders = DB::table('orders')
    ->select('city', 'state')
    ->groupByRaw('city, state')
    ->get();

```
