## [Retrieving Single Models / Aggregates](https://laravel.com/docs/12.x/eloquent#retrieving-single-models)
In addition to retrieving all of the records matching a given query, you may also retrieve single records using the `find`, `first`, or `firstWhere` methods. Instead of returning a collection of models, these methods return a single model instance:
```


 1use App\Models\Flight;




 2 



 3// Retrieve a model by its primary key...




 4$flight = Flight::find(1);




 5 



 6// Retrieve the first model matching the query constraints...




 7$flight = Flight::where('active', 1)->first();




 8 



 9// Alternative to retrieving the first model matching the query constraints...




10$flight = Flight::firstWhere('active', 1);




use App\Models\Flight;

// Retrieve a model by its primary key...
$flight = Flight::find(1);

// Retrieve the first model matching the query constraints...
$flight = Flight::where('active', 1)->first();

// Alternative to retrieving the first model matching the query constraints...
$flight = Flight::firstWhere('active', 1);

```

Sometimes you may wish to perform some other action if no results are found. The `findOr` and `firstOr` methods will return a single model instance or, if no results are found, execute the given closure. The value returned by the closure will be considered the result of the method:
```


1$flight = Flight::findOr(1, function () {




2    // ...




3});




4 



5$flight = Flight::where('legs', '>', 3)->firstOr(function () {




6    // ...




7});




$flight = Flight::findOr(1, function () {
    // ...
});

$flight = Flight::where('legs', '>', 3)->firstOr(function () {
    // ...
});

```

#### [Not Found Exceptions](https://laravel.com/docs/12.x/eloquent#not-found-exceptions)
Sometimes you may wish to throw an exception if a model is not found. This is particularly useful in routes or controllers. The `findOrFail` and `firstOrFail` methods will retrieve the first result of the query; however, if no result is found, an `Illuminate\Database\Eloquent\ModelNotFoundException` will be thrown:
```


1$flight = Flight::findOrFail(1);




2 



3$flight = Flight::where('legs', '>', 3)->firstOrFail();




$flight = Flight::findOrFail(1);

$flight = Flight::where('legs', '>', 3)->firstOrFail();

```

If the `ModelNotFoundException` is not caught, a 404 HTTP response is automatically sent back to the client:
```


1use App\Models\Flight;




2 



3Route::get('/api/flights/{id}', function (string $id) {




4    return Flight::findOrFail($id);




5});




use App\Models\Flight;

Route::get('/api/flights/{id}', function (string $id) {
    return Flight::findOrFail($id);
});

```

### [Retrieving or Creating Models](https://laravel.com/docs/12.x/eloquent#retrieving-or-creating-models)
The `firstOrCreate` method will attempt to locate a database record using the given column / value pairs. If the model cannot be found in the database, a record will be inserted with the attributes resulting from merging the first array argument with the optional second array argument.
The `firstOrNew` method, like `firstOrCreate`, will attempt to locate a record in the database matching the given attributes. However, if a model is not found, a new model instance will be returned. Note that the model returned by `firstOrNew` has not yet been persisted to the database. You will need to manually call the `save` method to persist it:
```


 1use App\Models\Flight;




 2 



 3// Retrieve flight by name or create it if it doesn't exist...




 4$flight = Flight::firstOrCreate([




 5    'name' => 'London to Paris'




 6]);




 7 



 8// Retrieve flight by name or create it with the name, delayed, and arrival_time attributes...




 9$flight = Flight::firstOrCreate(




10    ['name' => 'London to Paris'],




11    ['delayed' => 1, 'arrival_time' => '11:30']




12);




13 



14// Retrieve flight by name or instantiate a new Flight instance...




15$flight = Flight::firstOrNew([




16    'name' => 'London to Paris'




17]);




18 



19// Retrieve flight by name or instantiate with the name, delayed, and arrival_time attributes...




20$flight = Flight::firstOrNew(




21    ['name' => 'Tokyo to Sydney'],




22    ['delayed' => 1, 'arrival_time' => '11:30']




23);




use App\Models\Flight;

// Retrieve flight by name or create it if it doesn't exist...
$flight = Flight::firstOrCreate([
    'name' => 'London to Paris'
]);

// Retrieve flight by name or create it with the name, delayed, and arrival_time attributes...
$flight = Flight::firstOrCreate(
    ['name' => 'London to Paris'],
    ['delayed' => 1, 'arrival_time' => '11:30']
);

// Retrieve flight by name or instantiate a new Flight instance...
$flight = Flight::firstOrNew([
    'name' => 'London to Paris'
]);

// Retrieve flight by name or instantiate with the name, delayed, and arrival_time attributes...
$flight = Flight::firstOrNew(
    ['name' => 'Tokyo to Sydney'],
    ['delayed' => 1, 'arrival_time' => '11:30']
);

```

### [Retrieving Aggregates](https://laravel.com/docs/12.x/eloquent#retrieving-aggregates)
When interacting with Eloquent models, you may also use the `count`, `sum`, `max`, and other [aggregate methods](https://laravel.com/docs/12.x/queries#aggregates) provided by the Laravel [query builder](https://laravel.com/docs/12.x/queries). As you might expect, these methods return a scalar value instead of an Eloquent model instance:
```


1$count = Flight::where('active', 1)->count();




2 



3$max = Flight::where('active', 1)->max('price');




$count = Flight::where('active', 1)->count();

$max = Flight::where('active', 1)->max('price');

```
