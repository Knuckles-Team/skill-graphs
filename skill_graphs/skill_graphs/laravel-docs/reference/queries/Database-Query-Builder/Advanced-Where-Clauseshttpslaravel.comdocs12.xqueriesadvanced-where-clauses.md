## [Advanced Where Clauses](https://laravel.com/docs/12.x/queries#advanced-where-clauses)
### [Where Exists Clauses](https://laravel.com/docs/12.x/queries#where-exists-clauses)
The `whereExists` method allows you to write "where exists" SQL clauses. The `whereExists` method accepts a closure which will receive a query builder instance, allowing you to define the query that should be placed inside of the "exists" clause:
```


1$users = DB::table('users')




2    ->whereExists(function (Builder $query) {




3        $query->select(DB::raw(1))




4            ->from('orders')




5            ->whereColumn('orders.user_id', 'users.id');




6    })




7    ->get();




$users = DB::table('users')
    ->whereExists(function (Builder $query) {
        $query->select(DB::raw(1))
            ->from('orders')
            ->whereColumn('orders.user_id', 'users.id');
    })
    ->get();

```

Alternatively, you may provide a query object to the `whereExists` method instead of a closure:
```


1$orders = DB::table('orders')




2    ->select(DB::raw(1))




3    ->whereColumn('orders.user_id', 'users.id');




4 



5$users = DB::table('users')




6    ->whereExists($orders)




7    ->get();




$orders = DB::table('orders')
    ->select(DB::raw(1))
    ->whereColumn('orders.user_id', 'users.id');

$users = DB::table('users')
    ->whereExists($orders)
    ->get();

```

Both of the examples above will produce the following SQL:
```


1select * from users




2where exists (




3    select 1




4    from orders




5    where orders.user_id = users.id




6)




select * from users
where exists (
    select 1
    from orders
    where orders.user_id = users.id
)

```

### [Subquery Where Clauses](https://laravel.com/docs/12.x/queries#subquery-where-clauses)
Sometimes you may need to construct a "where" clause that compares the results of a subquery to a given value. You may accomplish this by passing a closure and a value to the `where` method. For example, the following query will retrieve all users who have a recent "membership" of a given type;
```


 1use App\Models\User;




 2use Illuminate\Database\Query\Builder;




 3 



 4$users = User::where(function (Builder $query) {




 5    $query->select('type')




 6        ->from('membership')




 7        ->whereColumn('membership.user_id', 'users.id')




 8        ->orderByDesc('membership.start_date')




 9        ->limit(1);




10}, 'Pro')->get();




use App\Models\User;
use Illuminate\Database\Query\Builder;

$users = User::where(function (Builder $query) {
    $query->select('type')
        ->from('membership')
        ->whereColumn('membership.user_id', 'users.id')
        ->orderByDesc('membership.start_date')
        ->limit(1);
}, 'Pro')->get();

```

Or, you may need to construct a "where" clause that compares a column to the results of a subquery. You may accomplish this by passing a column, operator, and closure to the `where` method. For example, the following query will retrieve all income records where the amount is less than average;
```


1use App\Models\Income;




2use Illuminate\Database\Query\Builder;




3 



4$incomes = Income::where('amount', '<', function (Builder $query) {




5    $query->selectRaw('avg(i.amount)')->from('incomes as i');




6})->get();




use App\Models\Income;
use Illuminate\Database\Query\Builder;

$incomes = Income::where('amount', '<', function (Builder $query) {
    $query->selectRaw('avg(i.amount)')->from('incomes as i');
})->get();

```

### [Full Text Where Clauses](https://laravel.com/docs/12.x/queries#full-text-where-clauses)
Full text where clauses are currently supported by MariaDB, MySQL, and PostgreSQL.
The `whereFullText` and `orWhereFullText` methods may be used to add full text "where" clauses to a query for columns that have [full text indexes](https://laravel.com/docs/12.x/migrations#available-index-types). These methods will be transformed into the appropriate SQL for the underlying database system by Laravel. For example, a `MATCH AGAINST` clause will be generated for applications utilizing MariaDB or MySQL:
```


1$users = DB::table('users')




2    ->whereFullText('bio', 'web developer')




3    ->get();




$users = DB::table('users')
    ->whereFullText('bio', 'web developer')
    ->get();

```

### [Vector Similarity Clauses](https://laravel.com/docs/12.x/queries#vector-similarity-clauses)
Vector similarity clauses are currently only supported on PostgreSQL connections using the `pgvector` extension. For information on defining vector columns and indexes, consult the [migration documentation](https://laravel.com/docs/12.x/migrations#available-column-types).
The `whereVectorSimilarTo` method filters results by cosine similarity to a given vector and orders the results by relevance. The `minSimilarity` threshold should be a value between `0.0` and `1.0`, where `1.0` is identical:
```


1$documents = DB::table('documents')




2    ->whereVectorSimilarTo('embedding', $queryEmbedding, minSimilarity: 0.4)




3    ->limit(10)




4    ->get();




$documents = DB::table('documents')
    ->whereVectorSimilarTo('embedding', $queryEmbedding, minSimilarity: 0.4)
    ->limit(10)
    ->get();

```

When a plain string is given as the vector argument, Laravel will automatically generate embeddings for it using the [Laravel AI SDK](https://laravel.com/docs/12.x/ai-sdk#embeddings):
```


1$documents = DB::table('documents')




2    ->whereVectorSimilarTo('embedding', 'Best wineries in Napa Valley')




3    ->limit(10)




4    ->get();




$documents = DB::table('documents')
    ->whereVectorSimilarTo('embedding', 'Best wineries in Napa Valley')
    ->limit(10)
    ->get();

```

By default, `whereVectorSimilarTo` also orders results by distance (most similar first). You may disable this ordering by passing `false` as the `order` argument:
```


1$documents = DB::table('documents')




2    ->whereVectorSimilarTo('embedding', $queryEmbedding, minSimilarity: 0.4, order: false)




3    ->orderBy('created_at', 'desc')




4    ->limit(10)




5    ->get();




$documents = DB::table('documents')
    ->whereVectorSimilarTo('embedding', $queryEmbedding, minSimilarity: 0.4, order: false)
    ->orderBy('created_at', 'desc')
    ->limit(10)
    ->get();

```

If you need more control, you may use the `selectVectorDistance`, `whereVectorDistanceLessThan`, and `orderByVectorDistance` methods independently:
```


1$documents = DB::table('documents')




2    ->select('*')




3    ->selectVectorDistance('embedding', $queryEmbedding, as: 'distance')




4    ->whereVectorDistanceLessThan('embedding', $queryEmbedding, maxDistance: 0.3)




5    ->orderByVectorDistance('embedding', $queryEmbedding)




6    ->limit(10)




7    ->get();




$documents = DB::table('documents')
    ->select('*')
    ->selectVectorDistance('embedding', $queryEmbedding, as: 'distance')
    ->whereVectorDistanceLessThan('embedding', $queryEmbedding, maxDistance: 0.3)
    ->orderByVectorDistance('embedding', $queryEmbedding)
    ->limit(10)
    ->get();

```

When utilizing PostgreSQL, the `pgvector` extension must be loaded before `vector` columns can be created:
```


1Schema::ensureVectorExtensionExists();




Schema::ensureVectorExtensionExists();

```
