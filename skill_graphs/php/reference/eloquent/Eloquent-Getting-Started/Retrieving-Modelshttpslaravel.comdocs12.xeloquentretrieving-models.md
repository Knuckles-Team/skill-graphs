## [Retrieving Models](https://laravel.com/docs/12.x/eloquent#retrieving-models)
Once you have created a model and [its associated database table](https://laravel.com/docs/12.x/migrations#generating-migrations), you are ready to start retrieving data from your database. You can think of each Eloquent model as a powerful [query builder](https://laravel.com/docs/12.x/queries) allowing you to fluently query the database table associated with the model. The model's `all` method will retrieve all of the records from the model's associated database table:
```


1use App\Models\Flight;




2 



3foreach (Flight::all() as $flight) {




4    echo $flight->name;




5}




use App\Models\Flight;

foreach (Flight::all() as $flight) {
    echo $flight->name;
}

```

#### [Building Queries](https://laravel.com/docs/12.x/eloquent#building-queries)
The Eloquent `all` method will return all of the results in the model's table. However, since each Eloquent model serves as a [query builder](https://laravel.com/docs/12.x/queries), you may add additional constraints to queries and then invoke the `get` method to retrieve the results:
```


1$flights = Flight::where('active', 1)




2    ->orderBy('name')




3    ->limit(10)




4    ->get();




$flights = Flight::where('active', 1)
    ->orderBy('name')
    ->limit(10)
    ->get();

```

Since Eloquent models are query builders, you should review all of the methods provided by Laravel's [query builder](https://laravel.com/docs/12.x/queries). You may use any of these methods when writing your Eloquent queries.
#### [Refreshing Models](https://laravel.com/docs/12.x/eloquent#refreshing-models)
If you already have an instance of an Eloquent model that was retrieved from the database, you can "refresh" the model using the `fresh` and `refresh` methods. The `fresh` method will re-retrieve the model from the database. The existing model instance will not be affected:
```


1$flight = Flight::where('number', 'FR 900')->first();




2 



3$freshFlight = $flight->fresh();




$flight = Flight::where('number', 'FR 900')->first();

$freshFlight = $flight->fresh();

```

The `refresh` method will re-hydrate the existing model using fresh data from the database. In addition, all of its loaded relationships will be refreshed as well:
```


1$flight = Flight::where('number', 'FR 900')->first();




2 



3$flight->number = 'FR 456';




4 



5$flight->refresh();




6 



7$flight->number; // "FR 900"




$flight = Flight::where('number', 'FR 900')->first();

$flight->number = 'FR 456';

$flight->refresh();

$flight->number; // "FR 900"

```

### [Collections](https://laravel.com/docs/12.x/eloquent#collections)
As we have seen, Eloquent methods like `all` and `get` retrieve multiple records from the database. However, these methods don't return a plain PHP array. Instead, an instance of `Illuminate\Database\Eloquent\Collection` is returned.
The Eloquent `Collection` class extends Laravel's base `Illuminate\Support\Collection` class, which provides a [variety of helpful methods](https://laravel.com/docs/12.x/collections#available-methods) for interacting with data collections. For example, the `reject` method may be used to remove models from a collection based on the results of an invoked closure:
```


1$flights = Flight::where('destination', 'Paris')->get();




2 



3$flights = $flights->reject(function (Flight $flight) {




4    return $flight->cancelled;




5});




$flights = Flight::where('destination', 'Paris')->get();

$flights = $flights->reject(function (Flight $flight) {
    return $flight->cancelled;
});

```

In addition to the methods provided by Laravel's base collection class, the Eloquent collection class provides [a few extra methods](https://laravel.com/docs/12.x/eloquent-collections#available-methods) that are specifically intended for interacting with collections of Eloquent models.
Since all of Laravel's collections implement PHP's iterable interfaces, you may loop over collections as if they were an array:
```


1foreach ($flights as $flight) {




2    echo $flight->name;




3}




foreach ($flights as $flight) {
    echo $flight->name;
}

```

### [Chunking Results](https://laravel.com/docs/12.x/eloquent#chunking-results)
Your application may run out of memory if you attempt to load tens of thousands of Eloquent records via the `all` or `get` methods. Instead of using these methods, the `chunk` method may be used to process large numbers of models more efficiently.
The `chunk` method will retrieve a subset of Eloquent models, passing them to a closure for processing. Since only the current chunk of Eloquent models is retrieved at a time, the `chunk` method will provide significantly reduced memory usage when working with a large number of models:
```


1use App\Models\Flight;




2use Illuminate\Database\Eloquent\Collection;




3 



4Flight::chunk(200, function (Collection $flights) {




5    foreach ($flights as $flight) {




6        // ...




7    }




8});




use App\Models\Flight;
use Illuminate\Database\Eloquent\Collection;

Flight::chunk(200, function (Collection $flights) {
    foreach ($flights as $flight) {
        // ...
    }
});

```

The first argument passed to the `chunk` method is the number of records you wish to receive per "chunk". The closure passed as the second argument will be invoked for each chunk that is retrieved from the database. A database query will be executed to retrieve each chunk of records passed to the closure.
If you are filtering the results of the `chunk` method based on a column that you will also be updating while iterating over the results, you should use the `chunkById` method. Using the `chunk` method in these scenarios could lead to unexpected and inconsistent results. Internally, the `chunkById` method will always retrieve models with an `id` column greater than the last model in the previous chunk:
```


1Flight::where('departed', true)




2    ->chunkById(200, function (Collection $flights) {




3        $flights->each->update(['departed' => false]);




4    }, column: 'id');




Flight::where('departed', true)
    ->chunkById(200, function (Collection $flights) {
        $flights->each->update(['departed' => false]);
    }, column: 'id');

```

Since the `chunkById` and `lazyById` methods add their own "where" conditions to the query being executed, you should typically [logically group](https://laravel.com/docs/12.x/queries#logical-grouping) your own conditions within a closure:
```


1Flight::where(function ($query) {




2    $query->where('delayed', true)->orWhere('cancelled', true);




3})->chunkById(200, function (Collection $flights) {




4    $flights->each->update([




5        'departed' => false,




6        'cancelled' => true




7    ]);




8}, column: 'id');




Flight::where(function ($query) {
    $query->where('delayed', true)->orWhere('cancelled', true);
})->chunkById(200, function (Collection $flights) {
    $flights->each->update([
        'departed' => false,
        'cancelled' => true
    ]);
}, column: 'id');

```

### [Chunking Using Lazy Collections](https://laravel.com/docs/12.x/eloquent#chunking-using-lazy-collections)
The `lazy` method works similarly to [the `chunk` method](https://laravel.com/docs/12.x/eloquent#chunking-results) in the sense that, behind the scenes, it executes the query in chunks. However, instead of passing each chunk directly into a callback as is, the `lazy` method returns a flattened [LazyCollection](https://laravel.com/docs/12.x/collections#lazy-collections) of Eloquent models, which lets you interact with the results as a single stream:
```


1use App\Models\Flight;




2 



3foreach (Flight::lazy() as $flight) {




4    // ...




5}




use App\Models\Flight;

foreach (Flight::lazy() as $flight) {
    // ...
}

```

If you are filtering the results of the `lazy` method based on a column that you will also be updating while iterating over the results, you should use the `lazyById` method. Internally, the `lazyById` method will always retrieve models with an `id` column greater than the last model in the previous chunk:
```


1Flight::where('departed', true)




2    ->lazyById(200, column: 'id')




3    ->each->update(['departed' => false]);




Flight::where('departed', true)
    ->lazyById(200, column: 'id')
    ->each->update(['departed' => false]);

```

You may filter the results based on the descending order of the `id` using the `lazyByIdDesc` method.
### [Cursors](https://laravel.com/docs/12.x/eloquent#cursors)
Similar to the `lazy` method, the `cursor` method may be used to significantly reduce your application's memory consumption when iterating through tens of thousands of Eloquent model records.
The `cursor` method will only execute a single database query; however, the individual Eloquent models will not be hydrated until they are actually iterated over. Therefore, only one Eloquent model is kept in memory at any given time while iterating over the cursor.
Since the `cursor` method only ever holds a single Eloquent model in memory at a time, it cannot eager load relationships. If you need to eager load relationships, consider using [the `lazy` method](https://laravel.com/docs/12.x/eloquent#chunking-using-lazy-collections) instead.
Internally, the `cursor` method uses PHP
```


1use App\Models\Flight;




2 



3foreach (Flight::where('destination', 'Zurich')->cursor() as $flight) {




4    // ...




5}




use App\Models\Flight;

foreach (Flight::where('destination', 'Zurich')->cursor() as $flight) {
    // ...
}

```

The `cursor` returns an `Illuminate\Support\LazyCollection` instance. [Lazy collections](https://laravel.com/docs/12.x/collections#lazy-collections) allow you to use many of the collection methods available on typical Laravel collections while only loading a single model into memory at a time:
```


1use App\Models\User;




2 



3$users = User::cursor()->filter(function (User $user) {




4    return $user->id > 500;




5});




6 



7foreach ($users as $user) {




8    echo $user->id;




9}




use App\Models\User;

$users = User::cursor()->filter(function (User $user) {
    return $user->id > 500;
});

foreach ($users as $user) {
    echo $user->id;
}

```

Although the `cursor` method uses far less memory than a regular query (by only holding a single Eloquent model in memory at a time), it will still eventually run out of memory. This is [the `lazy` method](https://laravel.com/docs/12.x/eloquent#chunking-using-lazy-collections) instead.
### [Advanced Subqueries](https://laravel.com/docs/12.x/eloquent#advanced-subqueries)
#### [Subquery Selects](https://laravel.com/docs/12.x/eloquent#subquery-selects)
Eloquent also offers advanced subquery support, which allows you to pull information from related tables in a single query. For example, let's imagine that we have a table of flight `destinations` and a table of `flights` to destinations. The `flights` table contains an `arrived_at` column which indicates when the flight arrived at the destination.
Using the subquery functionality available to the query builder's `select` and `addSelect` methods, we can select all of the `destinations` and the name of the flight that most recently arrived at that destination using a single query:
```


1use App\Models\Destination;




2use App\Models\Flight;




3 



4return Destination::addSelect(['last_flight' => Flight::select('name')




5    ->whereColumn('destination_id', 'destinations.id')




6    ->orderByDesc('arrived_at')




7    ->limit(1)




8])->get();




use App\Models\Destination;
use App\Models\Flight;

return Destination::addSelect(['last_flight' => Flight::select('name')
    ->whereColumn('destination_id', 'destinations.id')
    ->orderByDesc('arrived_at')
    ->limit(1)
])->get();

```

#### [Subquery Ordering](https://laravel.com/docs/12.x/eloquent#subquery-ordering)
In addition, the query builder's `orderBy` function supports subqueries. Continuing to use our flight example, we may use this functionality to sort all destinations based on when the last flight arrived at that destination. Again, this may be done while executing a single database query:
```


1return Destination::orderByDesc(




2    Flight::select('arrived_at')




3        ->whereColumn('destination_id', 'destinations.id')




4        ->orderByDesc('arrived_at')




5        ->limit(1)




6)->get();




return Destination::orderByDesc(
    Flight::select('arrived_at')
        ->whereColumn('destination_id', 'destinations.id')
        ->orderByDesc('arrived_at')
        ->limit(1)
)->get();

```
