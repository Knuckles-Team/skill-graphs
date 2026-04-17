#### [`sortBy()`](https://laravel.com/docs/12.x/collections#method-sortby)
The `sortBy` method sorts the collection by the given key. The sorted collection keeps the original array keys, so in the following example we will use the [values](https://laravel.com/docs/12.x/collections#method-values) method to reset the keys to consecutively numbered indexes:
```


 1$collection = collect([




 2    ['name' => 'Desk', 'price' => 200],




 3    ['name' => 'Chair', 'price' => 100],




 4    ['name' => 'Bookcase', 'price' => 150],




 5]);




 6 



 7$sorted = $collection->sortBy('price');




 8 



 9$sorted->values()->all();




10 



11/*




12    [




13        ['name' => 'Chair', 'price' => 100],




14        ['name' => 'Bookcase', 'price' => 150],




15        ['name' => 'Desk', 'price' => 200],




16    ]




17*/




$collection = collect([
    ['name' => 'Desk', 'price' => 200],
    ['name' => 'Chair', 'price' => 100],
    ['name' => 'Bookcase', 'price' => 150],
]);

$sorted = $collection->sortBy('price');

$sorted->values()->all();

/*
    [
        ['name' => 'Chair', 'price' => 100],
        ['name' => 'Bookcase', 'price' => 150],
        ['name' => 'Desk', 'price' => 200],
    ]
*/

```

The `sortBy` method accepts
```


 1$collection = collect([




 2    ['title' => 'Item 1'],




 3    ['title' => 'Item 12'],




 4    ['title' => 'Item 3'],




 5]);




 6 



 7$sorted = $collection->sortBy('title', SORT_NATURAL);




 8 



 9$sorted->values()->all();




10 



11/*




12    [




13        ['title' => 'Item 1'],




14        ['title' => 'Item 3'],




15        ['title' => 'Item 12'],




16    ]




17*/




$collection = collect([
    ['title' => 'Item 1'],
    ['title' => 'Item 12'],
    ['title' => 'Item 3'],
]);

$sorted = $collection->sortBy('title', SORT_NATURAL);

$sorted->values()->all();

/*
    [
        ['title' => 'Item 1'],
        ['title' => 'Item 3'],
        ['title' => 'Item 12'],
    ]
*/

```

Alternatively, you may pass your own closure to determine how to sort the collection's values:
```


 1$collection = collect([




 2    ['name' => 'Desk', 'colors' => ['Black', 'Mahogany']],




 3    ['name' => 'Chair', 'colors' => ['Black']],




 4    ['name' => 'Bookcase', 'colors' => ['Red', 'Beige', 'Brown']],




 5]);




 6 



 7$sorted = $collection->sortBy(function (array $product, int $key) {




 8    return count($product['colors']);




 9});




10 



11$sorted->values()->all();




12 



13/*




14    [




15        ['name' => 'Chair', 'colors' => ['Black']],




16        ['name' => 'Desk', 'colors' => ['Black', 'Mahogany']],




17        ['name' => 'Bookcase', 'colors' => ['Red', 'Beige', 'Brown']],




18    ]




19*/




$collection = collect([
    ['name' => 'Desk', 'colors' => ['Black', 'Mahogany']],
    ['name' => 'Chair', 'colors' => ['Black']],
    ['name' => 'Bookcase', 'colors' => ['Red', 'Beige', 'Brown']],
]);

$sorted = $collection->sortBy(function (array $product, int $key) {
    return count($product['colors']);
});

$sorted->values()->all();

/*
    [
        ['name' => 'Chair', 'colors' => ['Black']],
        ['name' => 'Desk', 'colors' => ['Black', 'Mahogany']],
        ['name' => 'Bookcase', 'colors' => ['Red', 'Beige', 'Brown']],
    ]
*/

```

If you would like to sort your collection by multiple attributes, you may pass an array of sort operations to the `sortBy` method. Each sort operation should be an array consisting of the attribute that you wish to sort by and the direction of the desired sort:
```


 1$collection = collect([




 2    ['name' => 'Taylor Otwell', 'age' => 34],




 3    ['name' => 'Abigail Otwell', 'age' => 30],




 4    ['name' => 'Taylor Otwell', 'age' => 36],




 5    ['name' => 'Abigail Otwell', 'age' => 32],




 6]);




 7 



 8$sorted = $collection->sortBy([




 9    ['name', 'asc'],




10    ['age', 'desc'],




11]);




12 



13$sorted->values()->all();




14 



15/*




16    [




17        ['name' => 'Abigail Otwell', 'age' => 32],




18        ['name' => 'Abigail Otwell', 'age' => 30],




19        ['name' => 'Taylor Otwell', 'age' => 36],




20        ['name' => 'Taylor Otwell', 'age' => 34],




21    ]




22*/




$collection = collect([
    ['name' => 'Taylor Otwell', 'age' => 34],
    ['name' => 'Abigail Otwell', 'age' => 30],
    ['name' => 'Taylor Otwell', 'age' => 36],
    ['name' => 'Abigail Otwell', 'age' => 32],
]);

$sorted = $collection->sortBy([
    ['name', 'asc'],
    ['age', 'desc'],
]);

$sorted->values()->all();

/*
    [
        ['name' => 'Abigail Otwell', 'age' => 32],
        ['name' => 'Abigail Otwell', 'age' => 30],
        ['name' => 'Taylor Otwell', 'age' => 36],
        ['name' => 'Taylor Otwell', 'age' => 34],
    ]
*/

```

When sorting a collection by multiple attributes, you may also provide closures that define each sort operation:
```


 1$collection = collect([




 2    ['name' => 'Taylor Otwell', 'age' => 34],




 3    ['name' => 'Abigail Otwell', 'age' => 30],




 4    ['name' => 'Taylor Otwell', 'age' => 36],




 5    ['name' => 'Abigail Otwell', 'age' => 32],




 6]);




 7 



 8$sorted = $collection->sortBy([




 9    fn (array $a, array $b) => $a['name'] <=> $b['name'],




10    fn (array $a, array $b) => $b['age'] <=> $a['age'],




11]);




12 



13$sorted->values()->all();




14 



15/*




16    [




17        ['name' => 'Abigail Otwell', 'age' => 32],




18        ['name' => 'Abigail Otwell', 'age' => 30],




19        ['name' => 'Taylor Otwell', 'age' => 36],




20        ['name' => 'Taylor Otwell', 'age' => 34],




21    ]




22*/




$collection = collect([
    ['name' => 'Taylor Otwell', 'age' => 34],
    ['name' => 'Abigail Otwell', 'age' => 30],
    ['name' => 'Taylor Otwell', 'age' => 36],
    ['name' => 'Abigail Otwell', 'age' => 32],
]);

$sorted = $collection->sortBy([
    fn (array $a, array $b) => $a['name'] <=> $b['name'],
    fn (array $a, array $b) => $b['age'] <=> $a['age'],
]);

$sorted->values()->all();

/*
    [
        ['name' => 'Abigail Otwell', 'age' => 32],
        ['name' => 'Abigail Otwell', 'age' => 30],
        ['name' => 'Taylor Otwell', 'age' => 36],
        ['name' => 'Taylor Otwell', 'age' => 34],
    ]
*/

```

#### [`sortByDesc()`](https://laravel.com/docs/12.x/collections#method-sortbydesc)
This method has the same signature as the [sortBy](https://laravel.com/docs/12.x/collections#method-sortby) method, but will sort the collection in the opposite order.
#### [`sortDesc()`](https://laravel.com/docs/12.x/collections#method-sortdesc)
This method will sort the collection in the opposite order as the [sort](https://laravel.com/docs/12.x/collections#method-sort) method:
```


1$collection = collect([5, 3, 1, 2, 4]);




2 



3$sorted = $collection->sortDesc();




4 



5$sorted->values()->all();




6 



7// [5, 4, 3, 2, 1]




$collection = collect([5, 3, 1, 2, 4]);

$sorted = $collection->sortDesc();

$sorted->values()->all();

// [5, 4, 3, 2, 1]

```

Unlike `sort`, you may not pass a closure to `sortDesc`. Instead, you should use the [sort](https://laravel.com/docs/12.x/collections#method-sort) method and invert your comparison.
#### [`sortKeys()`](https://laravel.com/docs/12.x/collections#method-sortkeys)
The `sortKeys` method sorts the collection by the keys of the underlying associative array:
```


 1$collection = collect([




 2    'id' => 22345,




 3    'first' => 'John',




 4    'last' => 'Doe',




 5]);




 6 



 7$sorted = $collection->sortKeys();




 8 



 9$sorted->all();




10 



11/*




12    [




13        'first' => 'John',




14        'id' => 22345,




15        'last' => 'Doe',




16    ]




17*/




$collection = collect([
    'id' => 22345,
    'first' => 'John',
    'last' => 'Doe',
]);

$sorted = $collection->sortKeys();

$sorted->all();

/*
    [
        'first' => 'John',
        'id' => 22345,
        'last' => 'Doe',
    ]
*/

```

#### [`sortKeysDesc()`](https://laravel.com/docs/12.x/collections#method-sortkeysdesc)
This method has the same signature as the [sortKeys](https://laravel.com/docs/12.x/collections#method-sortkeys) method, but will sort the collection in the opposite order.
#### [`sortKeysUsing()`](https://laravel.com/docs/12.x/collections#method-sortkeysusing)
The `sortKeysUsing` method sorts the collection by the keys of the underlying associative array using a callback:
```


 1$collection = collect([




 2    'ID' => 22345,




 3    'first' => 'John',




 4    'last' => 'Doe',




 5]);




 6 



 7$sorted = $collection->sortKeysUsing('strnatcasecmp');




 8 



 9$sorted->all();




10 



11/*




12    [




13        'first' => 'John',




14        'ID' => 22345,




15        'last' => 'Doe',




16    ]




17*/




$collection = collect([
    'ID' => 22345,
    'first' => 'John',
    'last' => 'Doe',
]);

$sorted = $collection->sortKeysUsing('strnatcasecmp');

$sorted->all();

/*
    [
        'first' => 'John',
        'ID' => 22345,
        'last' => 'Doe',
    ]
*/

```

The callback must be a comparison function that returns an integer less than, equal to, or greater than zero. For more information, refer to the PHP documentation on `sortKeysUsing` method utilizes internally.
#### [`splice()`](https://laravel.com/docs/12.x/collections#method-splice)
The `splice` method removes and returns a slice of items starting at the specified index:
```


 1$collection = collect([1, 2, 3, 4, 5]);




 2 



 3$chunk = $collection->splice(2);




 4 



 5$chunk->all();




 6 



 7// [3, 4, 5]




 8 



 9$collection->all();




10 



11// [1, 2]




$collection = collect([1, 2, 3, 4, 5]);

$chunk = $collection->splice(2);

$chunk->all();

// [3, 4, 5]

$collection->all();

// [1, 2]

```

You may pass a second argument to limit the size of the resulting collection:
```


 1$collection = collect([1, 2, 3, 4, 5]);




 2 



 3$chunk = $collection->splice(2, 1);




 4 



 5$chunk->all();




 6 



 7// [3]




 8 



 9$collection->all();




10 



11// [1, 2, 4, 5]




$collection = collect([1, 2, 3, 4, 5]);

$chunk = $collection->splice(2, 1);

$chunk->all();

// [3]

$collection->all();

// [1, 2, 4, 5]

```

In addition, you may pass a third argument containing the new items to replace the items removed from the collection:
```


 1$collection = collect([1, 2, 3, 4, 5]);




 2 



 3$chunk = $collection->splice(2, 1, [10, 11]);




 4 



 5$chunk->all();




 6 



 7// [3]




 8 



 9$collection->all();




10 



11// [1, 2, 10, 11, 4, 5]




$collection = collect([1, 2, 3, 4, 5]);

$chunk = $collection->splice(2, 1, [10, 11]);

$chunk->all();

// [3]

$collection->all();

// [1, 2, 10, 11, 4, 5]

```

#### [`split()`](https://laravel.com/docs/12.x/collections#method-split)
The `split` method breaks a collection into the given number of groups:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$groups = $collection->split(3);




4 



5$groups->all();




6 



7// [[1, 2], [3, 4], [5]]




$collection = collect([1, 2, 3, 4, 5]);

$groups = $collection->split(3);

$groups->all();

// [[1, 2], [3, 4], [5]]

```

#### [`splitIn()`](https://laravel.com/docs/12.x/collections#method-splitin)
The `splitIn` method breaks a collection into the given number of groups, filling non-terminal groups completely before allocating the remainder to the final group:
```


1$collection = collect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);




2 



3$groups = $collection->splitIn(3);




4 



5$groups->all();




6 



7// [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]




$collection = collect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

$groups = $collection->splitIn(3);

$groups->all();

// [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]

```

#### [`sum()`](https://laravel.com/docs/12.x/collections#method-sum)
The `sum` method returns the sum of all items in the collection:
```


1collect([1, 2, 3, 4, 5])->sum();




2 



3// 15




collect([1, 2, 3, 4, 5])->sum();

// 15

```

If the collection contains nested arrays or objects, you should pass a key that will be used to determine which values to sum:
```


1$collection = collect([




2    ['name' => 'JavaScript: The Good Parts', 'pages' => 176],




3    ['name' => 'JavaScript: The Definitive Guide', 'pages' => 1096],




4]);




5 



6$collection->sum('pages');




7 



8// 1272




$collection = collect([
    ['name' => 'JavaScript: The Good Parts', 'pages' => 176],
    ['name' => 'JavaScript: The Definitive Guide', 'pages' => 1096],
]);

$collection->sum('pages');

// 1272

```

In addition, you may pass your own closure to determine which values of the collection to sum:
```


 1$collection = collect([




 2    ['name' => 'Chair', 'colors' => ['Black']],




 3    ['name' => 'Desk', 'colors' => ['Black', 'Mahogany']],




 4    ['name' => 'Bookcase', 'colors' => ['Red', 'Beige', 'Brown']],




 5]);




 6 



 7$collection->sum(function (array $product) {




 8    return count($product['colors']);




 9});




10 



11// 6




$collection = collect([
    ['name' => 'Chair', 'colors' => ['Black']],
    ['name' => 'Desk', 'colors' => ['Black', 'Mahogany']],
    ['name' => 'Bookcase', 'colors' => ['Red', 'Beige', 'Brown']],
]);

$collection->sum(function (array $product) {
    return count($product['colors']);
});

// 6

```

#### [`take()`](https://laravel.com/docs/12.x/collections#method-take)
The `take` method returns a new collection with the specified number of items:
```


1$collection = collect([0, 1, 2, 3, 4, 5]);




2 



3$chunk = $collection->take(3);




4 



5$chunk->all();




6 



7// [0, 1, 2]




$collection = collect([0, 1, 2, 3, 4, 5]);

$chunk = $collection->take(3);

$chunk->all();

// [0, 1, 2]

```

You may also pass a negative integer to take the specified number of items from the end of the collection:
```


1$collection = collect([0, 1, 2, 3, 4, 5]);




2 



3$chunk = $collection->take(-2);




4 



5$chunk->all();




6 



7// [4, 5]




$collection = collect([0, 1, 2, 3, 4, 5]);

$chunk = $collection->take(-2);

$chunk->all();

// [4, 5]

```

#### [`takeUntil()`](https://laravel.com/docs/12.x/collections#method-takeuntil)
The `takeUntil` method returns items in the collection until the given callback returns `true`:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$subset = $collection->takeUntil(function (int $item) {




4    return $item >= 3;




5});




6 



7$subset->all();




8 



9// [1, 2]




$collection = collect([1, 2, 3, 4]);

$subset = $collection->takeUntil(function (int $item) {
    return $item >= 3;
});

$subset->all();

// [1, 2]

```

You may also pass a simple value to the `takeUntil` method to get the items until the given value is found:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$subset = $collection->takeUntil(3);




4 



5$subset->all();




6 



7// [1, 2]




$collection = collect([1, 2, 3, 4]);

$subset = $collection->takeUntil(3);

$subset->all();

// [1, 2]

```

If the given value is not found or the callback never returns `true`, the `takeUntil` method will return all items in the collection.
#### [`takeWhile()`](https://laravel.com/docs/12.x/collections#method-takewhile)
The `takeWhile` method returns items in the collection until the given callback returns `false`:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$subset = $collection->takeWhile(function (int $item) {




4    return $item < 3;




5});




6 



7$subset->all();




8 



9// [1, 2]




$collection = collect([1, 2, 3, 4]);

$subset = $collection->takeWhile(function (int $item) {
    return $item < 3;
});

$subset->all();

// [1, 2]

```

If the callback never returns `false`, the `takeWhile` method will return all items in the collection.
#### [`tap()`](https://laravel.com/docs/12.x/collections#method-tap)
The `tap` method passes the collection to the given callback, allowing you to "tap" into the collection at a specific point and do something with the items while not affecting the collection itself. The collection is then returned by the `tap` method:
```


1collect([2, 4, 3, 1, 5])




2    ->sort()




3    ->tap(function (Collection $collection) {




4        Log::debug('Values after sorting', $collection->values()->all());




5    })




6    ->shift();




7 



8// 1




collect([2, 4, 3, 1, 5])
    ->sort()
    ->tap(function (Collection $collection) {
        Log::debug('Values after sorting', $collection->values()->all());
    })
    ->shift();

// 1

```

#### [`times()`](https://laravel.com/docs/12.x/collections#method-times)
The static `times` method creates a new collection by invoking the given closure a specified number of times:
```


1$collection = Collection::times(10, function (int $number) {




2    return $number * 9;




3});




4 



5$collection->all();




6 



7// [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]




$collection = Collection::times(10, function (int $number) {
    return $number * 9;
});

$collection->all();

// [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]

```

#### [`toArray()`](https://laravel.com/docs/12.x/collections#method-toarray)
The `toArray` method converts the collection into a plain PHP `array`. If the collection's values are [Eloquent](https://laravel.com/docs/12.x/eloquent) models, the models will also be converted to arrays:
```


1$collection = collect(['name' => 'Desk', 'price' => 200]);




2 



3$collection->toArray();




4 



5/*




6    [




7        ['name' => 'Desk', 'price' => 200],




8    ]




9*/




$collection = collect(['name' => 'Desk', 'price' => 200]);

$collection->toArray();

/*
    [
        ['name' => 'Desk', 'price' => 200],
    ]
*/

```

`toArray` also converts all of the collection's nested objects that are an instance of `Arrayable` to an array. If you want to get the raw array underlying the collection, use the [all](https://laravel.com/docs/12.x/collections#method-all) method instead.
#### [`toJson()`](https://laravel.com/docs/12.x/collections#method-tojson)
The `toJson` method converts the collection into a JSON serialized string:
```


1$collection = collect(['name' => 'Desk', 'price' => 200]);




2 



3$collection->toJson();




4 



5// '{"name":"Desk", "price":200}'




$collection = collect(['name' => 'Desk', 'price' => 200]);

$collection->toJson();

// '{"name":"Desk", "price":200}'

```

#### [`toPrettyJson()`](https://laravel.com/docs/12.x/collections#method-to-pretty-json)
The `toPrettyJson` method converts the collection into a formatted JSON string using the `JSON_PRETTY_PRINT` option:
```


1$collection = collect(['name' => 'Desk', 'price' => 200]);




2 



3$collection->toPrettyJson();




$collection = collect(['name' => 'Desk', 'price' => 200]);

$collection->toPrettyJson();

```

#### [`transform()`](https://laravel.com/docs/12.x/collections#method-transform)
The `transform` method iterates over the collection and calls the given callback with each item in the collection. The items in the collection will be replaced by the values returned by the callback:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->transform(function (int $item, int $key) {




4    return $item * 2;




5});




6 



7$collection->all();




8 



9// [2, 4, 6, 8, 10]




$collection = collect([1, 2, 3, 4, 5]);

$collection->transform(function (int $item, int $key) {
    return $item * 2;
});

$collection->all();

// [2, 4, 6, 8, 10]

```

Unlike most other collection methods, `transform` modifies the collection itself. If you wish to create a new collection instead, use the [map](https://laravel.com/docs/12.x/collections#method-map) method.
#### [`undot()`](https://laravel.com/docs/12.x/collections#method-undot)
The `undot` method expands a single-dimensional collection that uses "dot" notation into a multi-dimensional collection:
```


 1$person = collect([




 2    'name.first_name' => 'Marie',




 3    'name.last_name' => 'Valentine',




 4    'address.line_1' => '2992 Eagle Drive',




 5    'address.line_2' => '',




 6    'address.suburb' => 'Detroit',




 7    'address.state' => 'MI',




 8    'address.postcode' => '48219'




 9]);




10 



11$person = $person->undot();




12 



13$person->toArray();




14 



15/*




16    [




17        "name" => [




18            "first_name" => "Marie",




19            "last_name" => "Valentine",




20        ],




21        "address" => [




22            "line_1" => "2992 Eagle Drive",




23            "line_2" => "",




24            "suburb" => "Detroit",




25            "state" => "MI",




26            "postcode" => "48219",




27        ],




28    ]




29*/




$person = collect([
    'name.first_name' => 'Marie',
    'name.last_name' => 'Valentine',
    'address.line_1' => '2992 Eagle Drive',
    'address.line_2' => '',
    'address.suburb' => 'Detroit',
    'address.state' => 'MI',
    'address.postcode' => '48219'
]);

$person = $person->undot();

$person->toArray();

/*
    [
        "name" => [
            "first_name" => "Marie",
            "last_name" => "Valentine",
        ],
        "address" => [
            "line_1" => "2992 Eagle Drive",
            "line_2" => "",
            "suburb" => "Detroit",
            "state" => "MI",
            "postcode" => "48219",
        ],
    ]
*/

```

#### [`union()`](https://laravel.com/docs/12.x/collections#method-union)
The `union` method adds the given array to the collection. If the given array contains keys that are already in the original collection, the original collection's values will be preferred:
```


1$collection = collect([1 => ['a'], 2 => ['b']]);




2 



3$union = $collection->union([3 => ['c'], 1 => ['d']]);




4 



5$union->all();




6 



7// [1 => ['a'], 2 => ['b'], 3 => ['c']]




$collection = collect([1 => ['a'], 2 => ['b']]);

$union = $collection->union([3 => ['c'], 1 => ['d']]);

$union->all();

// [1 => ['a'], 2 => ['b'], 3 => ['c']]

```

#### [`unique()`](https://laravel.com/docs/12.x/collections#method-unique)
The `unique` method returns all of the unique items in the collection. The returned collection keeps the original array keys, so in the following example we will use the [values](https://laravel.com/docs/12.x/collections#method-values) method to reset the keys to consecutively numbered indexes:
```


1$collection = collect([1, 1, 2, 2, 3, 4, 2]);




2 



3$unique = $collection->unique();




4 



5$unique->values()->all();




6 



7// [1, 2, 3, 4]




$collection = collect([1, 1, 2, 2, 3, 4, 2]);

$unique = $collection->unique();

$unique->values()->all();

// [1, 2, 3, 4]

```

When dealing with nested arrays or objects, you may specify the key used to determine uniqueness:
```


 1$collection = collect([




 2    ['name' => 'iPhone 6', 'brand' => 'Apple', 'type' => 'phone'],




 3    ['name' => 'iPhone 5', 'brand' => 'Apple', 'type' => 'phone'],




 4    ['name' => 'Apple Watch', 'brand' => 'Apple', 'type' => 'watch'],




 5    ['name' => 'Galaxy S6', 'brand' => 'Samsung', 'type' => 'phone'],




 6    ['name' => 'Galaxy Gear', 'brand' => 'Samsung', 'type' => 'watch'],




 7]);




 8 



 9$unique = $collection->unique('brand');




10 



11$unique->values()->all();




12 



13/*




14    [




15        ['name' => 'iPhone 6', 'brand' => 'Apple', 'type' => 'phone'],




16        ['name' => 'Galaxy S6', 'brand' => 'Samsung', 'type' => 'phone'],




17    ]




18*/




$collection = collect([
    ['name' => 'iPhone 6', 'brand' => 'Apple', 'type' => 'phone'],
    ['name' => 'iPhone 5', 'brand' => 'Apple', 'type' => 'phone'],
    ['name' => 'Apple Watch', 'brand' => 'Apple', 'type' => 'watch'],
    ['name' => 'Galaxy S6', 'brand' => 'Samsung', 'type' => 'phone'],
    ['name' => 'Galaxy Gear', 'brand' => 'Samsung', 'type' => 'watch'],
]);

$unique = $collection->unique('brand');

$unique->values()->all();

/*
    [
        ['name' => 'iPhone 6', 'brand' => 'Apple', 'type' => 'phone'],
        ['name' => 'Galaxy S6', 'brand' => 'Samsung', 'type' => 'phone'],
    ]
*/

```

Finally, you may also pass your own closure to the `unique` method to specify which value should determine an item's uniqueness:
```


 1$unique = $collection->unique(function (array $item) {




 2    return $item['brand'].$item['type'];




 3});




 4 



 5$unique->values()->all();




 6 



 7/*




 8    [




 9        ['name' => 'iPhone 6', 'brand' => 'Apple', 'type' => 'phone'],




10        ['name' => 'Apple Watch', 'brand' => 'Apple', 'type' => 'watch'],




11        ['name' => 'Galaxy S6', 'brand' => 'Samsung', 'type' => 'phone'],




12        ['name' => 'Galaxy Gear', 'brand' => 'Samsung', 'type' => 'watch'],




13    ]




14*/




$unique = $collection->unique(function (array $item) {
    return $item['brand'].$item['type'];
});

$unique->values()->all();

/*
    [
        ['name' => 'iPhone 6', 'brand' => 'Apple', 'type' => 'phone'],
        ['name' => 'Apple Watch', 'brand' => 'Apple', 'type' => 'watch'],
        ['name' => 'Galaxy S6', 'brand' => 'Samsung', 'type' => 'phone'],
        ['name' => 'Galaxy Gear', 'brand' => 'Samsung', 'type' => 'watch'],
    ]
*/

```

The `unique` method uses "loose" comparisons when checking item values, meaning a string with an integer value will be considered equal to an integer of the same value. Use the [uniqueStrict](https://laravel.com/docs/12.x/collections#method-uniquestrict) method to filter using "strict" comparisons.
This method's behavior is modified when using [Eloquent Collections](https://laravel.com/docs/12.x/eloquent-collections#method-unique).
