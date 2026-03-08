 8    'color' => 'blue',




 9    'size' => 'M',




10    'material' => 'polyester',




11], function (string $a, string $b) {




12    return strcasecmp($a, $b);




13});




14 



15$intersect->all();




16 



17// ['Size' => 'M']




$collection = collect([
    'color' => 'red',
    'Size' => 'M',
    'material' => 'cotton',
]);

$intersect = $collection->intersectAssocUsing([
    'color' => 'blue',
    'size' => 'M',
    'material' => 'polyester',
], function (string $a, string $b) {
    return strcasecmp($a, $b);
});

$intersect->all();

// ['Size' => 'M']

```

#### [`intersectByKeys()`](https://laravel.com/docs/12.x/collections#method-intersectbykeys)
The `intersectByKeys` method removes any keys and their corresponding values from the original collection that are not present in the given array or collection:
```


 1$collection = collect([




 2    'serial' => 'UX301', 'type' => 'screen', 'year' => 2009,




 3]);




 4 



 5$intersect = $collection->intersectByKeys([




 6    'reference' => 'UX404', 'type' => 'tab', 'year' => 2011,




 7]);




 8 



 9$intersect->all();




10 



11// ['type' => 'screen', 'year' => 2009]




$collection = collect([
    'serial' => 'UX301', 'type' => 'screen', 'year' => 2009,
]);

$intersect = $collection->intersectByKeys([
    'reference' => 'UX404', 'type' => 'tab', 'year' => 2011,
]);

$intersect->all();

// ['type' => 'screen', 'year' => 2009]

```

#### [`isEmpty()`](https://laravel.com/docs/12.x/collections#method-isempty)
The `isEmpty` method returns `true` if the collection is empty; otherwise, `false` is returned:
```


1collect([])->isEmpty();




2 



3// true




collect([])->isEmpty();

// true

```

#### [`isNotEmpty()`](https://laravel.com/docs/12.x/collections#method-isnotempty)
The `isNotEmpty` method returns `true` if the collection is not empty; otherwise, `false` is returned:
```


1collect([])->isNotEmpty();




2 



3// false




collect([])->isNotEmpty();

// false

```

#### [`join()`](https://laravel.com/docs/12.x/collections#method-join)
The `join` method joins the collection's values with a string. Using this method's second argument, you may also specify how the final element should be appended to the string:
```


1collect(['a', 'b', 'c'])->join(', '); // 'a, b, c'




2collect(['a', 'b', 'c'])->join(', ', ', and '); // 'a, b, and c'




3collect(['a', 'b'])->join(', ', ' and '); // 'a and b'




4collect(['a'])->join(', ', ' and '); // 'a'




5collect([])->join(', ', ' and '); // ''




collect(['a', 'b', 'c'])->join(', '); // 'a, b, c'
collect(['a', 'b', 'c'])->join(', ', ', and '); // 'a, b, and c'
collect(['a', 'b'])->join(', ', ' and '); // 'a and b'
collect(['a'])->join(', ', ' and '); // 'a'
collect([])->join(', ', ' and '); // ''

```

#### [`keyBy()`](https://laravel.com/docs/12.x/collections#method-keyby)
The `keyBy` method keys the collection by the given key. If multiple items have the same key, only the last one will appear in the new collection:
```


 1$collection = collect([




 2    ['product_id' => 'prod-100', 'name' => 'Desk'],




 3    ['product_id' => 'prod-200', 'name' => 'Chair'],




 4]);




 5 



 6$keyed = $collection->keyBy('product_id');




 7 



 8$keyed->all();




 9 



10/*




11    [




12        'prod-100' => ['product_id' => 'prod-100', 'name' => 'Desk'],




13        'prod-200' => ['product_id' => 'prod-200', 'name' => 'Chair'],




14    ]




15*/




$collection = collect([
    ['product_id' => 'prod-100', 'name' => 'Desk'],
    ['product_id' => 'prod-200', 'name' => 'Chair'],
]);

$keyed = $collection->keyBy('product_id');

$keyed->all();

/*
    [
        'prod-100' => ['product_id' => 'prod-100', 'name' => 'Desk'],
        'prod-200' => ['product_id' => 'prod-200', 'name' => 'Chair'],
    ]
*/

```

You may also pass a callback to the method. The callback should return the value to key the collection by:
```


 1$keyed = $collection->keyBy(function (array $item, int $key) {




 2    return strtoupper($item['product_id']);




 3});




 4 



 5$keyed->all();




 6 



 7/*




 8    [




 9        'PROD-100' => ['product_id' => 'prod-100', 'name' => 'Desk'],




10        'PROD-200' => ['product_id' => 'prod-200', 'name' => 'Chair'],




11    ]




12*/




$keyed = $collection->keyBy(function (array $item, int $key) {
    return strtoupper($item['product_id']);
});

$keyed->all();

/*
    [
        'PROD-100' => ['product_id' => 'prod-100', 'name' => 'Desk'],
        'PROD-200' => ['product_id' => 'prod-200', 'name' => 'Chair'],
    ]
*/

```

#### [`keys()`](https://laravel.com/docs/12.x/collections#method-keys)
The `keys` method returns all of the collection's keys:
```


 1$collection = collect([




 2    'prod-100' => ['product_id' => 'prod-100', 'name' => 'Desk'],




 3    'prod-200' => ['product_id' => 'prod-200', 'name' => 'Chair'],




 4]);




 5 



 6$keys = $collection->keys();




 7 



 8$keys->all();




 9 



10// ['prod-100', 'prod-200']




$collection = collect([
    'prod-100' => ['product_id' => 'prod-100', 'name' => 'Desk'],
    'prod-200' => ['product_id' => 'prod-200', 'name' => 'Chair'],
]);

$keys = $collection->keys();

$keys->all();

// ['prod-100', 'prod-200']

```

#### [`last()`](https://laravel.com/docs/12.x/collections#method-last)
The `last` method returns the last element in the collection that passes a given truth test:
```


1collect([1, 2, 3, 4])->last(function (int $value, int $key) {




2    return $value < 3;




3});




4 



5// 2




collect([1, 2, 3, 4])->last(function (int $value, int $key) {
    return $value < 3;
});

// 2

```

You may also call the `last` method with no arguments to get the last element in the collection. If the collection is empty, `null` is returned:
```


1collect([1, 2, 3, 4])->last();




2 



3// 4




collect([1, 2, 3, 4])->last();

// 4

```

#### [`lazy()`](https://laravel.com/docs/12.x/collections#method-lazy)
The `lazy` method returns a new [LazyCollection](https://laravel.com/docs/12.x/collections#lazy-collections) instance from the underlying array of items:
```


1$lazyCollection = collect([1, 2, 3, 4])->lazy();




2 



3$lazyCollection::class;




4 



5// Illuminate\Support\LazyCollection




6 



7$lazyCollection->all();




8 



9// [1, 2, 3, 4]




$lazyCollection = collect([1, 2, 3, 4])->lazy();

$lazyCollection::class;

// Illuminate\Support\LazyCollection

$lazyCollection->all();

// [1, 2, 3, 4]

```

This is especially useful when you need to perform transformations on a huge `Collection` that contains many items:
```


1$count = $hugeCollection




2    ->lazy()




3    ->where('country', 'FR')




4    ->where('balance', '>', '100')




5    ->count();




$count = $hugeCollection
    ->lazy()
    ->where('country', 'FR')
    ->where('balance', '>', '100')
    ->count();

```

By converting the collection to a `LazyCollection`, we avoid having to allocate a ton of additional memory. Though the original collection still keeps _its_ values in memory, the subsequent filters will not. Therefore, virtually no additional memory will be allocated when filtering the collection's results.
#### [`macro()`](https://laravel.com/docs/12.x/collections#method-macro)
The static `macro` method allows you to add methods to the `Collection` class at run time. Refer to the documentation on [extending collections](https://laravel.com/docs/12.x/collections#extending-collections) for more information.
#### [`make()`](https://laravel.com/docs/12.x/collections#method-make)
The static `make` method creates a new collection instance. See the [Creating Collections](https://laravel.com/docs/12.x/collections#creating-collections) section.
```


1use Illuminate\Support\Collection;




2 



3$collection = Collection::make([1, 2, 3]);




use Illuminate\Support\Collection;

$collection = Collection::make([1, 2, 3]);

```

#### [`map()`](https://laravel.com/docs/12.x/collections#method-map)
The `map` method iterates through the collection and passes each value to the given callback. The callback is free to modify the item and return it, thus forming a new collection of modified items:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$multiplied = $collection->map(function (int $item, int $key) {




4    return $item * 2;




5});




6 



7$multiplied->all();




8 



9// [2, 4, 6, 8, 10]




$collection = collect([1, 2, 3, 4, 5]);

$multiplied = $collection->map(function (int $item, int $key) {
    return $item * 2;
});

$multiplied->all();

// [2, 4, 6, 8, 10]

```

Like most other collection methods, `map` returns a new collection instance; it does not modify the collection it is called on. If you want to transform the original collection, use the [transform](https://laravel.com/docs/12.x/collections#method-transform) method.
#### [`mapInto()`](https://laravel.com/docs/12.x/collections#method-mapinto)
The `mapInto()` method iterates over the collection, creating a new instance of the given class by passing the value into the constructor:
```


 1class Currency




 2{




 3    /**




 4     * Create a new currency instance.




 5     */




 6    function __construct(




 7        public string $code,




 8    ) {}




 9}




10 



11$collection = collect(['USD', 'EUR', 'GBP']);




12 



13$currencies = $collection->mapInto(Currency::class);




14 



15$currencies->all();




16 



17// [Currency('USD'), Currency('EUR'), Currency('GBP')]




class Currency
{
    /**
     * Create a new currency instance.
     */
    function __construct(
        public string $code,
    ) {}
}

$collection = collect(['USD', 'EUR', 'GBP']);

$currencies = $collection->mapInto(Currency::class);

$currencies->all();

// [Currency('USD'), Currency('EUR'), Currency('GBP')]

```

#### [`mapSpread()`](https://laravel.com/docs/12.x/collections#method-mapspread)
The `mapSpread` method iterates over the collection's items, passing each nested item value into the given closure. The closure is free to modify the item and return it, thus forming a new collection of modified items:
```


 1$collection = collect([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);




 2 



 3$chunks = $collection->chunk(2);




 4 



 5$sequence = $chunks->mapSpread(function (int $even, int $odd) {




 6    return $even + $odd;




 7});




 8 



 9$sequence->all();




10 



11// [1, 5, 9, 13, 17]




$collection = collect([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

$chunks = $collection->chunk(2);

$sequence = $chunks->mapSpread(function (int $even, int $odd) {
    return $even + $odd;
});

$sequence->all();

// [1, 5, 9, 13, 17]

```

#### [`mapToGroups()`](https://laravel.com/docs/12.x/collections#method-maptogroups)
The `mapToGroups` method groups the collection's items by the given closure. The closure should return an associative array containing a single key / value pair, thus forming a new collection of grouped values:
```


 1$collection = collect([




 2    [




 3        'name' => 'John Doe',




 4        'department' => 'Sales',




 5    ],




 6    [




 7        'name' => 'Jane Doe',




 8        'department' => 'Sales',




 9    ],




10    [




11        'name' => 'Johnny Doe',




12        'department' => 'Marketing',




13    ]




14]);




15 



16$grouped = $collection->mapToGroups(function (array $item, int $key) {




17    return [$item['department'] => $item['name']];




18});




19 



20$grouped->all();




21 



22/*




23    [




24        'Sales' => ['John Doe', 'Jane Doe'],




25        'Marketing' => ['Johnny Doe'],




26    ]




27*/




28 



29$grouped->get('Sales')->all();




30 



31// ['John Doe', 'Jane Doe']




$collection = collect([
    [
        'name' => 'John Doe',
        'department' => 'Sales',
    ],
    [
        'name' => 'Jane Doe',
        'department' => 'Sales',
    ],
    [
        'name' => 'Johnny Doe',
        'department' => 'Marketing',
    ]
]);

$grouped = $collection->mapToGroups(function (array $item, int $key) {
    return [$item['department'] => $item['name']];
});

$grouped->all();

/*
    [
        'Sales' => ['John Doe', 'Jane Doe'],
        'Marketing' => ['Johnny Doe'],
    ]
*/

$grouped->get('Sales')->all();

// ['John Doe', 'Jane Doe']

```

#### [`mapWithKeys()`](https://laravel.com/docs/12.x/collections#method-mapwithkeys)
The `mapWithKeys` method iterates through the collection and passes each value to the given callback. The callback should return an associative array containing a single key / value pair:
```


 1$collection = collect([




 2    [




 3        'name' => 'John',




 4        'department' => 'Sales',




 5        'email' => 'john@example.com',




 6    ],




 7    [




 8        'name' => 'Jane',




 9        'department' => 'Marketing',




10        'email' => 'jane@example.com',




11    ]




12]);




13 



14$keyed = $collection->mapWithKeys(function (array $item, int $key) {




15    return [$item['email'] => $item['name']];




16});




17 



18$keyed->all();




19 



20/*




21    [




22        'john@example.com' => 'John',




23        'jane@example.com' => 'Jane',




24    ]




25*/




$collection = collect([
    [
        'name' => 'John',
        'department' => 'Sales',
        'email' => 'john@example.com',
    ],
    [
        'name' => 'Jane',
        'department' => 'Marketing',
        'email' => 'jane@example.com',
    ]
]);

$keyed = $collection->mapWithKeys(function (array $item, int $key) {
    return [$item['email'] => $item['name']];
});

$keyed->all();

/*
    [
        'john@example.com' => 'John',
        'jane@example.com' => 'Jane',
    ]
*/

```

#### [`max()`](https://laravel.com/docs/12.x/collections#method-max)
The `max` method returns the maximum value of a given key:
```


 1$max = collect([




 2    ['foo' => 10],




 3    ['foo' => 20]




 4])->max('foo');




 5 



 6// 20




 7 



 8$max = collect([1, 2, 3, 4, 5])->max();




 9 



10// 5




$max = collect([
    ['foo' => 10],
    ['foo' => 20]
])->max('foo');

// 20

$max = collect([1, 2, 3, 4, 5])->max();

// 5

```

#### [`median()`](https://laravel.com/docs/12.x/collections#method-median)
The `median` method returns the
```


 1$median = collect([




 2    ['foo' => 10],




 3    ['foo' => 10],




 4    ['foo' => 20],




 5    ['foo' => 40]




 6])->median('foo');




 7 



 8// 15




 9 



10$median = collect([1, 1, 2, 4])->median();




11 



12// 1.5




$median = collect([
    ['foo' => 10],
    ['foo' => 10],
    ['foo' => 20],
    ['foo' => 40]
])->median('foo');

// 15

$median = collect([1, 1, 2, 4])->median();

// 1.5

```

#### [`merge()`](https://laravel.com/docs/12.x/collections#method-merge)
The `merge` method merges the given array or collection with the original collection. If a string key in the given items matches a string key in the original collection, the given item's value will overwrite the value in the original collection:
```


1$collection = collect(['product_id' => 1, 'price' => 100]);




2 



3$merged = $collection->merge(['price' => 200, 'discount' => false]);




4 



5$merged->all();




6 



7// ['product_id' => 1, 'price' => 200, 'discount' => false]




$collection = collect(['product_id' => 1, 'price' => 100]);

$merged = $collection->merge(['price' => 200, 'discount' => false]);

$merged->all();

// ['product_id' => 1, 'price' => 200, 'discount' => false]

```

If the given item's keys are numeric, the values will be appended to the end of the collection:
```


1$collection = collect(['Desk', 'Chair']);




2 



3$merged = $collection->merge(['Bookcase', 'Door']);




4 



5$merged->all();




6 



7// ['Desk', 'Chair', 'Bookcase', 'Door']




$collection = collect(['Desk', 'Chair']);

$merged = $collection->merge(['Bookcase', 'Door']);

$merged->all();

// ['Desk', 'Chair', 'Bookcase', 'Door']

```

#### [`mergeRecursive()`](https://laravel.com/docs/12.x/collections#method-mergerecursive)
The `mergeRecursive` method merges the given array or collection recursively with the original collection. If a string key in the given items matches a string key in the original collection, then the values for these keys are merged together into an array, and this is done recursively:
```


 1$collection = collect(['product_id' => 1, 'price' => 100]);




 2 



 3$merged = $collection->mergeRecursive([




 4    'product_id' => 2,




 5    'price' => 200,




 6    'discount' => false




 7]);




 8 



 9$merged->all();




10 



11// ['product_id' => [1, 2], 'price' => [100, 200], 'discount' => false]




$collection = collect(['product_id' => 1, 'price' => 100]);

$merged = $collection->mergeRecursive([
    'product_id' => 2,
    'price' => 200,
    'discount' => false
]);

$merged->all();

// ['product_id' => [1, 2], 'price' => [100, 200], 'discount' => false]

```

#### [`min()`](https://laravel.com/docs/12.x/collections#method-min)
The `min` method returns the minimum value of a given key:
```


 1$min = collect([




 2    ['foo' => 10],




 3    ['foo' => 20]




 4])->min('foo');




 5 



 6// 10




 7 



 8$min = collect([1, 2, 3, 4, 5])->min();




 9 



10// 1




$min = collect([
    ['foo' => 10],
    ['foo' => 20]
])->min('foo');

// 10

$min = collect([1, 2, 3, 4, 5])->min();

// 1

```

#### [`mode()`](https://laravel.com/docs/12.x/collections#method-mode)
The `mode` method returns the
```


 1$mode = collect([




 2    ['foo' => 10],




 3    ['foo' => 10],




 4    ['foo' => 20],




 5    ['foo' => 40]




 6])->mode('foo');




 7 



 8// [10]




 9 



10$mode = collect([1, 1, 2, 4])->mode();




11 



12// [1]




13 



14$mode = collect([1, 1, 2, 2])->mode();




15 



16// [1, 2]




$mode = collect([
    ['foo' => 10],
    ['foo' => 10],
    ['foo' => 20],
    ['foo' => 40]
])->mode('foo');

// [10]

$mode = collect([1, 1, 2, 4])->mode();

// [1]

$mode = collect([1, 1, 2, 2])->mode();

// [1, 2]

```

#### [`multiply()`](https://laravel.com/docs/12.x/collections#method-multiply)
The `multiply` method creates the specified number of copies of all items in the collection:
```


 1$users = collect([




 2    ['name' => 'User #1', 'email' => 'user1@example.com'],




 3    ['name' => 'User #2', 'email' => 'user2@example.com'],




 4])->multiply(3);




 5 



 6/*




 7    [




 8        ['name' => 'User #1', 'email' => 'user1@example.com'],




 9        ['name' => 'User #2', 'email' => 'user2@example.com'],




10        ['name' => 'User #1', 'email' => 'user1@example.com'],




11        ['name' => 'User #2', 'email' => 'user2@example.com'],




12        ['name' => 'User #1', 'email' => 'user1@example.com'],




13        ['name' => 'User #2', 'email' => 'user2@example.com'],




14    ]




15*/




$users = collect([
    ['name' => 'User #1', 'email' => 'user1@example.com'],
    ['name' => 'User #2', 'email' => 'user2@example.com'],
])->multiply(3);

/*
    [
        ['name' => 'User #1', 'email' => 'user1@example.com'],
        ['name' => 'User #2', 'email' => 'user2@example.com'],
        ['name' => 'User #1', 'email' => 'user1@example.com'],
        ['name' => 'User #2', 'email' => 'user2@example.com'],
        ['name' => 'User #1', 'email' => 'user1@example.com'],
        ['name' => 'User #2', 'email' => 'user2@example.com'],
    ]
*/

```

#### [`nth()`](https://laravel.com/docs/12.x/collections#method-nth)
The `nth` method creates a new collection consisting of every n-th element:
```


1$collection = collect(['a', 'b', 'c', 'd', 'e', 'f']);




2 



3$collection->nth(4);




4 



5// ['a', 'e']




$collection = collect(['a', 'b', 'c', 'd', 'e', 'f']);

$collection->nth(4);

// ['a', 'e']

```

You may optionally pass a starting offset as the second argument:
```


1$collection->nth(4, 1);




2 



3// ['b', 'f']




$collection->nth(4, 1);

// ['b', 'f']

```

#### [`only()`](https://laravel.com/docs/12.x/collections#method-only)
The `only` method returns the items in the collection with the specified keys:
```


 1$collection = collect([




 2    'product_id' => 1,




 3    'name' => 'Desk',




 4    'price' => 100,




 5    'discount' => false




 6]);




 7 



 8$filtered = $collection->only(['product_id', 'name']);




 9 



10$filtered->all();




11 



12// ['product_id' => 1, 'name' => 'Desk']




$collection = collect([
    'product_id' => 1,
    'name' => 'Desk',
    'price' => 100,
    'discount' => false
]);

$filtered = $collection->only(['product_id', 'name']);

$filtered->all();

// ['product_id' => 1, 'name' => 'Desk']

```

For the inverse of `only`, see the [except](https://laravel.com/docs/12.x/collections#method-except) method.
This method's behavior is modified when using [Eloquent Collections](https://laravel.com/docs/12.x/eloquent-collections#method-only).
#### [`pad()`](https://laravel.com/docs/12.x/collections#method-pad)
The `pad` method will fill the array with the given value until the array reaches the specified size. This method behaves like the
To pad to the left, you should specify a negative size. No padding will take place if the absolute value of the given size is less than or equal to the length of the array:
```


 1$collection = collect(['A', 'B', 'C']);




 2 



 3$filtered = $collection->pad(5, 0);




 4 



 5$filtered->all();




 6 



 7// ['A', 'B', 'C', 0, 0]




 8 



 9$filtered = $collection->pad(-5, 0);




10 



11$filtered->all();




12 



13// [0, 0, 'A', 'B', 'C']




$collection = collect(['A', 'B', 'C']);

$filtered = $collection->pad(5, 0);

$filtered->all();

// ['A', 'B', 'C', 0, 0]

$filtered = $collection->pad(-5, 0);

$filtered->all();

// [0, 0, 'A', 'B', 'C']

```

#### [`partition()`](https://laravel.com/docs/12.x/collections#method-partition)
The `partition` method may be combined with PHP array destructuring to separate elements that pass a given truth test from those that do not:
```


 1$collection = collect([1, 2, 3, 4, 5, 6]);




 2 



 3[$underThree, $equalOrAboveThree] = $collection->partition(function (int $i) {




 4    return $i < 3;




 5});




 6 



 7$underThree->all();




 8 



 9// [1, 2]




10 



11$equalOrAboveThree->all();




12 



13// [3, 4, 5, 6]




$collection = collect([1, 2, 3, 4, 5, 6]);

[$underThree, $equalOrAboveThree] = $collection->partition(function (int $i) {
    return $i < 3;
});

$underThree->all();

// [1, 2]

$equalOrAboveThree->all();

// [3, 4, 5, 6]

```

This method's behavior is modified when interacting with [Eloquent collections](https://laravel.com/docs/12.x/eloquent-collections#method-partition).
#### [`percentage()`](https://laravel.com/docs/12.x/collections#method-percentage)
The `percentage` method may be used to quickly determine the percentage of items in the collection that pass a given truth test:
```


1$collection = collect([1, 1, 2, 2, 2, 3]);




2 



3$percentage = $collection->percentage(fn (int $value) => $value === 1);




4 



5// 33.33




$collection = collect([1, 1, 2, 2, 2, 3]);

$percentage = $collection->percentage(fn (int $value) => $value === 1);

// 33.33

```

By default, the percentage will be rounded to two decimal places. However, you may customize this behavior by providing a second argument to the method:
```


1$percentage = $collection->percentage(fn (int $value) => $value === 1, precision: 3);




2 



3// 33.333




$percentage = $collection->percentage(fn (int $value) => $value === 1, precision: 3);

// 33.333

```

#### [`pipe()`](https://laravel.com/docs/12.x/collections#method-pipe)
The `pipe` method passes the collection to the given closure and returns the result of the executed closure:
```


1$collection = collect([1, 2, 3]);




2 



3$piped = $collection->pipe(function (Collection $collection) {




4    return $collection->sum();




5});




6 



7// 6




$collection = collect([1, 2, 3]);

$piped = $collection->pipe(function (Collection $collection) {
    return $collection->sum();
});

// 6

```

#### [`pipeInto()`](https://laravel.com/docs/12.x/collections#method-pipeinto)
The `pipeInto` method creates a new instance of the given class and passes the collection into the constructor:
```


 1class ResourceCollection




 2{




 3    /**




 4     * Create a new ResourceCollection instance.




 5     */




 6    public function __construct(




 7        public Collection $collection,




 8    ) {}




 9}




10 



11$collection = collect([1, 2, 3]);




12 



13$resource = $collection->pipeInto(ResourceCollection::class);




14 



15$resource->collection->all();




16 



17// [1, 2, 3]




class ResourceCollection
{
    /**
     * Create a new ResourceCollection instance.
     */
    public function __construct(
        public Collection $collection,
    ) {}
}

$collection = collect([1, 2, 3]);

$resource = $collection->pipeInto(ResourceCollection::class);

$resource->collection->all();

// [1, 2, 3]

```

#### [`pipeThrough()`](https://laravel.com/docs/12.x/collections#method-pipethrough)
The `pipeThrough` method passes the collection to the given array of closures and returns the result of the executed closures:
```


 1use Illuminate\Support\Collection;




 2 



 3$collection = collect([1, 2, 3]);




 4 



 5$result = $collection->pipeThrough([




 6    function (Collection $collection) {




 7        return $collection->merge([4, 5]);




 8    },




 9    function (Collection $collection) {




10        return $collection->sum();




11    },




12]);




13 



14// 15




use Illuminate\Support\Collection;
