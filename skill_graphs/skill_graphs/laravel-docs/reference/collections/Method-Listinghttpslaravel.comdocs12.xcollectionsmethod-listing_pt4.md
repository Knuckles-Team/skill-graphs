
$collection = collect([1, 2, 3]);

$result = $collection->pipeThrough([
    function (Collection $collection) {
        return $collection->merge([4, 5]);
    },
    function (Collection $collection) {
        return $collection->sum();
    },
]);

// 15

```

#### [`pluck()`](https://laravel.com/docs/12.x/collections#method-pluck)
The `pluck` method retrieves all of the values for a given key:
```


 1$collection = collect([




 2    ['product_id' => 'prod-100', 'name' => 'Desk'],




 3    ['product_id' => 'prod-200', 'name' => 'Chair'],




 4]);




 5 



 6$plucked = $collection->pluck('name');




 7 



 8$plucked->all();




 9 



10// ['Desk', 'Chair']




$collection = collect([
    ['product_id' => 'prod-100', 'name' => 'Desk'],
    ['product_id' => 'prod-200', 'name' => 'Chair'],
]);

$plucked = $collection->pluck('name');

$plucked->all();

// ['Desk', 'Chair']

```

You may also specify how you wish the resulting collection to be keyed:
```


1$plucked = $collection->pluck('name', 'product_id');




2 



3$plucked->all();




4 



5// ['prod-100' => 'Desk', 'prod-200' => 'Chair']




$plucked = $collection->pluck('name', 'product_id');

$plucked->all();

// ['prod-100' => 'Desk', 'prod-200' => 'Chair']

```

The `pluck` method also supports retrieving nested values using "dot" notation:
```


 1$collection = collect([




 2    [




 3        'name' => 'Laracon',




 4        'speakers' => [




 5            'first_day' => ['Rosa', 'Judith'],




 6        ],




 7    ],




 8    [




 9        'name' => 'VueConf',




10        'speakers' => [




11            'first_day' => ['Abigail', 'Joey'],




12        ],




13    ],




14]);




15 



16$plucked = $collection->pluck('speakers.first_day');




17 



18$plucked->all();




19 



20// [['Rosa', 'Judith'], ['Abigail', 'Joey']]




$collection = collect([
    [
        'name' => 'Laracon',
        'speakers' => [
            'first_day' => ['Rosa', 'Judith'],
        ],
    ],
    [
        'name' => 'VueConf',
        'speakers' => [
            'first_day' => ['Abigail', 'Joey'],
        ],
    ],
]);

$plucked = $collection->pluck('speakers.first_day');

$plucked->all();

// [['Rosa', 'Judith'], ['Abigail', 'Joey']]

```

If duplicate keys exist, the last matching element will be inserted into the plucked collection:
```


 1$collection = collect([




 2    ['brand' => 'Tesla',  'color' => 'red'],




 3    ['brand' => 'Pagani', 'color' => 'white'],




 4    ['brand' => 'Tesla',  'color' => 'black'],




 5    ['brand' => 'Pagani', 'color' => 'orange'],




 6]);




 7 



 8$plucked = $collection->pluck('color', 'brand');




 9 



10$plucked->all();




11 



12// ['Tesla' => 'black', 'Pagani' => 'orange']




$collection = collect([
    ['brand' => 'Tesla',  'color' => 'red'],
    ['brand' => 'Pagani', 'color' => 'white'],
    ['brand' => 'Tesla',  'color' => 'black'],
    ['brand' => 'Pagani', 'color' => 'orange'],
]);

$plucked = $collection->pluck('color', 'brand');

$plucked->all();

// ['Tesla' => 'black', 'Pagani' => 'orange']

```

#### [`pop()`](https://laravel.com/docs/12.x/collections#method-pop)
The `pop` method removes and returns the last item from the collection. If the collection is empty, `null` will be returned:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->pop();




4 



5// 5




6 



7$collection->all();




8 



9// [1, 2, 3, 4]




$collection = collect([1, 2, 3, 4, 5]);

$collection->pop();

// 5

$collection->all();

// [1, 2, 3, 4]

```

You may pass an integer to the `pop` method to remove and return multiple items from the end of a collection:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->pop(3);




4 



5// collect([5, 4, 3])




6 



7$collection->all();




8 



9// [1, 2]




$collection = collect([1, 2, 3, 4, 5]);

$collection->pop(3);

// collect([5, 4, 3])

$collection->all();

// [1, 2]

```

#### [`prepend()`](https://laravel.com/docs/12.x/collections#method-prepend)
The `prepend` method adds an item to the beginning of the collection:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->prepend(0);




4 



5$collection->all();




6 



7// [0, 1, 2, 3, 4, 5]




$collection = collect([1, 2, 3, 4, 5]);

$collection->prepend(0);

$collection->all();

// [0, 1, 2, 3, 4, 5]

```

You may also pass a second argument to specify the key of the prepended item:
```


1$collection = collect(['one' => 1, 'two' => 2]);




2 



3$collection->prepend(0, 'zero');




4 



5$collection->all();




6 



7// ['zero' => 0, 'one' => 1, 'two' => 2]




$collection = collect(['one' => 1, 'two' => 2]);

$collection->prepend(0, 'zero');

$collection->all();

// ['zero' => 0, 'one' => 1, 'two' => 2]

```

#### [`pull()`](https://laravel.com/docs/12.x/collections#method-pull)
The `pull` method removes and returns an item from the collection by its key:
```


1$collection = collect(['product_id' => 'prod-100', 'name' => 'Desk']);




2 



3$collection->pull('name');




4 



5// 'Desk'




6 



7$collection->all();




8 



9// ['product_id' => 'prod-100']




$collection = collect(['product_id' => 'prod-100', 'name' => 'Desk']);

$collection->pull('name');

// 'Desk'

$collection->all();

// ['product_id' => 'prod-100']

```

#### [`push()`](https://laravel.com/docs/12.x/collections#method-push)
The `push` method appends an item to the end of the collection:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$collection->push(5);




4 



5$collection->all();




6 



7// [1, 2, 3, 4, 5]




$collection = collect([1, 2, 3, 4]);

$collection->push(5);

$collection->all();

// [1, 2, 3, 4, 5]

```

You may also provide multiple items to append to the end of the collection:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$collection->push(5, 6, 7);




4 



5$collection->all();




6 



7// [1, 2, 3, 4, 5, 6, 7]




$collection = collect([1, 2, 3, 4]);

$collection->push(5, 6, 7);

$collection->all();

// [1, 2, 3, 4, 5, 6, 7]

```

#### [`put()`](https://laravel.com/docs/12.x/collections#method-put)
The `put` method sets the given key and value in the collection:
```


1$collection = collect(['product_id' => 1, 'name' => 'Desk']);




2 



3$collection->put('price', 100);




4 



5$collection->all();




6 



7// ['product_id' => 1, 'name' => 'Desk', 'price' => 100]




$collection = collect(['product_id' => 1, 'name' => 'Desk']);

$collection->put('price', 100);

$collection->all();

// ['product_id' => 1, 'name' => 'Desk', 'price' => 100]

```

#### [`random()`](https://laravel.com/docs/12.x/collections#method-random)
The `random` method returns a random item from the collection:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->random();




4 



5// 4 - (retrieved randomly)




$collection = collect([1, 2, 3, 4, 5]);

$collection->random();

// 4 - (retrieved randomly)

```

You may pass an integer to `random` to specify how many items you would like to randomly retrieve. A collection of items is always returned when explicitly passing the number of items you wish to receive:
```


1$random = $collection->random(3);




2 



3$random->all();




4 



5// [2, 4, 5] - (retrieved randomly)




$random = $collection->random(3);

$random->all();

// [2, 4, 5] - (retrieved randomly)

```

If the collection instance has fewer items than requested, the `random` method will throw an `InvalidArgumentException`.
The `random` method also accepts a closure, which will receive the current collection instance:
```


1use Illuminate\Support\Collection;




2 



3$random = $collection->random(fn (Collection $items) => min(10, count($items)));




4 



5$random->all();




6 



7// [1, 2, 3, 4, 5] - (retrieved randomly)




use Illuminate\Support\Collection;

$random = $collection->random(fn (Collection $items) => min(10, count($items)));

$random->all();

// [1, 2, 3, 4, 5] - (retrieved randomly)

```

#### [`range()`](https://laravel.com/docs/12.x/collections#method-range)
The `range` method returns a collection containing integers between the specified range:
```


1$collection = collect()->range(3, 6);




2 



3$collection->all();




4 



5// [3, 4, 5, 6]




$collection = collect()->range(3, 6);

$collection->all();

// [3, 4, 5, 6]

```

#### [`reduce()`](https://laravel.com/docs/12.x/collections#method-reduce)
The `reduce` method reduces the collection to a single value, passing the result of each iteration into the subsequent iteration:
```


1$collection = collect([1, 2, 3]);




2 



3$total = $collection->reduce(function (?int $carry, int $item) {




4    return $carry + $item;




5});




6 



7// 6




$collection = collect([1, 2, 3]);

$total = $collection->reduce(function (?int $carry, int $item) {
    return $carry + $item;
});

// 6

```

The value for `$carry` on the first iteration is `null`; however, you may specify its initial value by passing a second argument to `reduce`:
```


1$collection->reduce(function (int $carry, int $item) {




2    return $carry + $item;




3}, 4);




4 



5// 10




$collection->reduce(function (int $carry, int $item) {
    return $carry + $item;
}, 4);

// 10

```

The `reduce` method also passes array keys to the given callback:
```


 1$collection = collect([




 2    'usd' => 1400,




 3    'gbp' => 1200,




 4    'eur' => 1000,




 5]);




 6 



 7$ratio = [




 8    'usd' => 1,




 9    'gbp' => 1.37,




10    'eur' => 1.22,




11];




12 



13$collection->reduce(function (int $carry, int $value, string $key) use ($ratio) {




14    return $carry + ($value * $ratio[$key]);




15}, 0);




16 



17// 4264




$collection = collect([
    'usd' => 1400,
    'gbp' => 1200,
    'eur' => 1000,
]);

$ratio = [
    'usd' => 1,
    'gbp' => 1.37,
    'eur' => 1.22,
];

$collection->reduce(function (int $carry, int $value, string $key) use ($ratio) {
    return $carry + ($value * $ratio[$key]);
}, 0);

// 4264

```

#### [`reduceSpread()`](https://laravel.com/docs/12.x/collections#method-reduce-spread)
The `reduceSpread` method reduces the collection to an array of values, passing the results of each iteration into the subsequent iteration. This method is similar to the `reduce` method; however, it can accept multiple initial values:
```


 1[$creditsRemaining, $batch] = Image::where('status', 'unprocessed')




 2    ->get()




 3    ->reduceSpread(function (int $creditsRemaining, Collection $batch, Image $image) {




 4        if ($creditsRemaining >= $image->creditsRequired()) {




 5            $batch->push($image);




 6 



 7            $creditsRemaining -= $image->creditsRequired();




 8        }




 9 



10        return [$creditsRemaining, $batch];




11    }, $creditsAvailable, collect());




[$creditsRemaining, $batch] = Image::where('status', 'unprocessed')
    ->get()
    ->reduceSpread(function (int $creditsRemaining, Collection $batch, Image $image) {
        if ($creditsRemaining >= $image->creditsRequired()) {
            $batch->push($image);

            $creditsRemaining -= $image->creditsRequired();
        }

        return [$creditsRemaining, $batch];
    }, $creditsAvailable, collect());

```

#### [`reject()`](https://laravel.com/docs/12.x/collections#method-reject)
The `reject` method filters the collection using the given closure. The closure should return `true` if the item should be removed from the resulting collection:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$filtered = $collection->reject(function (int $value, int $key) {




4    return $value > 2;




5});




6 



7$filtered->all();




8 



9// [1, 2]




$collection = collect([1, 2, 3, 4]);

$filtered = $collection->reject(function (int $value, int $key) {
    return $value > 2;
});

$filtered->all();

// [1, 2]

```

For the inverse of the `reject` method, see the [filter](https://laravel.com/docs/12.x/collections#method-filter) method.
#### [`replace()`](https://laravel.com/docs/12.x/collections#method-replace)
The `replace` method behaves similarly to `merge`; however, in addition to overwriting matching items that have string keys, the `replace` method will also overwrite items in the collection that have matching numeric keys:
```


1$collection = collect(['Taylor', 'Abigail', 'James']);




2 



3$replaced = $collection->replace([1 => 'Victoria', 3 => 'Finn']);




4 



5$replaced->all();




6 



7// ['Taylor', 'Victoria', 'James', 'Finn']




$collection = collect(['Taylor', 'Abigail', 'James']);

$replaced = $collection->replace([1 => 'Victoria', 3 => 'Finn']);

$replaced->all();

// ['Taylor', 'Victoria', 'James', 'Finn']

```

#### [`replaceRecursive()`](https://laravel.com/docs/12.x/collections#method-replacerecursive)
The `replaceRecursive` method behaves similarly to `replace`, but it will recur into arrays and apply the same replacement process to the inner values:
```


 1$collection = collect([




 2    'Taylor',




 3    'Abigail',




 4    [




 5        'James',




 6        'Victoria',




 7        'Finn'




 8    ]




 9]);




10 



11$replaced = $collection->replaceRecursive([




12    'Charlie',




13    2 => [1 => 'King']




14]);




15 



16$replaced->all();




17 



18// ['Charlie', 'Abigail', ['James', 'King', 'Finn']]




$collection = collect([
    'Taylor',
    'Abigail',
    [
        'James',
        'Victoria',
        'Finn'
    ]
]);

$replaced = $collection->replaceRecursive([
    'Charlie',
    2 => [1 => 'King']
]);

$replaced->all();

// ['Charlie', 'Abigail', ['James', 'King', 'Finn']]

```

#### [`reverse()`](https://laravel.com/docs/12.x/collections#method-reverse)
The `reverse` method reverses the order of the collection's items, preserving the original keys:
```


 1$collection = collect(['a', 'b', 'c', 'd', 'e']);




 2 



 3$reversed = $collection->reverse();




 4 



 5$reversed->all();




 6 



 7/*




 8    [




 9        4 => 'e',




10        3 => 'd',




11        2 => 'c',




12        1 => 'b',




13        0 => 'a',




14    ]




15*/




$collection = collect(['a', 'b', 'c', 'd', 'e']);

$reversed = $collection->reverse();

$reversed->all();

/*
    [
        4 => 'e',
        3 => 'd',
        2 => 'c',
        1 => 'b',
        0 => 'a',
    ]
*/

```

#### [`search()`](https://laravel.com/docs/12.x/collections#method-search)
The `search` method searches the collection for the given value and returns its key if found. If the item is not found, `false` is returned:
```


1$collection = collect([2, 4, 6, 8]);




2 



3$collection->search(4);




4 



5// 1




$collection = collect([2, 4, 6, 8]);

$collection->search(4);

// 1

```

The search is done using a "loose" comparison, meaning a string with an integer value will be considered equal to an integer of the same value. To use "strict" comparison, pass `true` as the second argument to the method:
```


1collect([2, 4, 6, 8])->search('4', strict: true);




2 



3// false




collect([2, 4, 6, 8])->search('4', strict: true);

// false

```

Alternatively, you may provide your own closure to search for the first item that passes a given truth test:
```


1collect([2, 4, 6, 8])->search(function (int $item, int $key) {




2    return $item > 5;




3});




4 



5// 2




collect([2, 4, 6, 8])->search(function (int $item, int $key) {
    return $item > 5;
});

// 2

```

#### [`select()`](https://laravel.com/docs/12.x/collections#method-select)
The `select` method selects the given keys from the collection, similar to an SQL `SELECT` statement:
```


 1$users = collect([




 2    ['name' => 'Taylor Otwell', 'role' => 'Developer', 'status' => 'active'],




 3    ['name' => 'Victoria Faith', 'role' => 'Researcher', 'status' => 'active'],




 4]);




 5 



 6$users->select(['name', 'role']);




 7 



 8/*




 9    [




10        ['name' => 'Taylor Otwell', 'role' => 'Developer'],




11        ['name' => 'Victoria Faith', 'role' => 'Researcher'],




12    ],




13*/




$users = collect([
    ['name' => 'Taylor Otwell', 'role' => 'Developer', 'status' => 'active'],
    ['name' => 'Victoria Faith', 'role' => 'Researcher', 'status' => 'active'],
]);

$users->select(['name', 'role']);

/*
    [
        ['name' => 'Taylor Otwell', 'role' => 'Developer'],
        ['name' => 'Victoria Faith', 'role' => 'Researcher'],
    ],
*/

```

#### [`shift()`](https://laravel.com/docs/12.x/collections#method-shift)
The `shift` method removes and returns the first item from the collection:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->shift();




4 



5// 1




6 



7$collection->all();




8 



9// [2, 3, 4, 5]




$collection = collect([1, 2, 3, 4, 5]);

$collection->shift();

// 1

$collection->all();

// [2, 3, 4, 5]

```

You may pass an integer to the `shift` method to remove and return multiple items from the beginning of a collection:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->shift(3);




4 



5// collect([1, 2, 3])




6 



7$collection->all();




8 



9// [4, 5]




$collection = collect([1, 2, 3, 4, 5]);

$collection->shift(3);

// collect([1, 2, 3])

$collection->all();

// [4, 5]

```

#### [`shuffle()`](https://laravel.com/docs/12.x/collections#method-shuffle)
The `shuffle` method randomly shuffles the items in the collection:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$shuffled = $collection->shuffle();




4 



5$shuffled->all();




6 



7// [3, 2, 5, 1, 4] - (generated randomly)




$collection = collect([1, 2, 3, 4, 5]);

$shuffled = $collection->shuffle();

$shuffled->all();

// [3, 2, 5, 1, 4] - (generated randomly)

```

#### [`skip()`](https://laravel.com/docs/12.x/collections#method-skip)
The `skip` method returns a new collection, with the given number of elements removed from the beginning of the collection:
```


1$collection = collect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);




2 



3$collection = $collection->skip(4);




4 



5$collection->all();




6 



7// [5, 6, 7, 8, 9, 10]




$collection = collect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

$collection = $collection->skip(4);

$collection->all();

// [5, 6, 7, 8, 9, 10]

```

#### [`skipUntil()`](https://laravel.com/docs/12.x/collections#method-skipuntil)
The `skipUntil` method skips over items from the collection while the given callback returns `false`. Once the callback returns `true` all of the remaining items in the collection will be returned as a new collection:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$subset = $collection->skipUntil(function (int $item) {




4    return $item >= 3;




5});




6 



7$subset->all();




8 



9// [3, 4]




$collection = collect([1, 2, 3, 4]);

$subset = $collection->skipUntil(function (int $item) {
    return $item >= 3;
});

$subset->all();

// [3, 4]

```

You may also pass a simple value to the `skipUntil` method to skip all items until the given value is found:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$subset = $collection->skipUntil(3);




4 



5$subset->all();




6 



7// [3, 4]




$collection = collect([1, 2, 3, 4]);

$subset = $collection->skipUntil(3);

$subset->all();

// [3, 4]

```

If the given value is not found or the callback never returns `true`, the `skipUntil` method will return an empty collection.
#### [`skipWhile()`](https://laravel.com/docs/12.x/collections#method-skipwhile)
The `skipWhile` method skips over items from the collection while the given callback returns `true`. Once the callback returns `false` all of the remaining items in the collection will be returned as a new collection:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$subset = $collection->skipWhile(function (int $item) {




4    return $item <= 3;




5});




6 



7$subset->all();




8 



9// [4]




$collection = collect([1, 2, 3, 4]);

$subset = $collection->skipWhile(function (int $item) {
    return $item <= 3;
});

$subset->all();

// [4]

```

If the callback never returns `false`, the `skipWhile` method will return an empty collection.
#### [`slice()`](https://laravel.com/docs/12.x/collections#method-slice)
The `slice` method returns a slice of the collection starting at the given index:
```


1$collection = collect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);




2 



3$slice = $collection->slice(4);




4 



5$slice->all();




6 



7// [5, 6, 7, 8, 9, 10]




$collection = collect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

$slice = $collection->slice(4);

$slice->all();

// [5, 6, 7, 8, 9, 10]

```

If you would like to limit the size of the returned slice, pass the desired size as the second argument to the method:
```


1$slice = $collection->slice(4, 2);




2 



3$slice->all();




4 



5// [5, 6]




$slice = $collection->slice(4, 2);

$slice->all();

// [5, 6]

```

The returned slice will preserve keys by default. If you do not wish to preserve the original keys, you can use the [values](https://laravel.com/docs/12.x/collections#method-values) method to reindex them.
#### [`sliding()`](https://laravel.com/docs/12.x/collections#method-sliding)
The `sliding` method returns a new collection of chunks representing a "sliding window" view of the items in the collection:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$chunks = $collection->sliding(2);




4 



5$chunks->toArray();




6 



7// [[1, 2], [2, 3], [3, 4], [4, 5]]




$collection = collect([1, 2, 3, 4, 5]);

$chunks = $collection->sliding(2);

$chunks->toArray();

// [[1, 2], [2, 3], [3, 4], [4, 5]]

```

This is especially useful in conjunction with the [eachSpread](https://laravel.com/docs/12.x/collections#method-eachspread) method:
```


1$transactions->sliding(2)->eachSpread(function (Collection $previous, Collection $current) {




2    $current->total = $previous->total + $current->amount;




3});




$transactions->sliding(2)->eachSpread(function (Collection $previous, Collection $current) {
    $current->total = $previous->total + $current->amount;
});

```

You may optionally pass a second "step" value, which determines the distance between the first item of every chunk:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$chunks = $collection->sliding(3, step: 2);




4 



5$chunks->toArray();




6 



7// [[1, 2, 3], [3, 4, 5]]




$collection = collect([1, 2, 3, 4, 5]);

$chunks = $collection->sliding(3, step: 2);

$chunks->toArray();

// [[1, 2, 3], [3, 4, 5]]

```

#### [`sole()`](https://laravel.com/docs/12.x/collections#method-sole)
The `sole` method returns the first element in the collection that passes a given truth test, but only if the truth test matches exactly one element:
```


1collect([1, 2, 3, 4])->sole(function (int $value, int $key) {




2    return $value === 2;




3});




4 



5// 2




collect([1, 2, 3, 4])->sole(function (int $value, int $key) {
    return $value === 2;
});

// 2

```

You may also pass a key / value pair to the `sole` method, which will return the first element in the collection that matches the given pair, but only if it exactly one element matches:
```


1$collection = collect([




2    ['product' => 'Desk', 'price' => 200],




3    ['product' => 'Chair', 'price' => 100],




4]);




5 



6$collection->sole('product', 'Chair');




7 



8// ['product' => 'Chair', 'price' => 100]




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Chair', 'price' => 100],
]);

$collection->sole('product', 'Chair');

// ['product' => 'Chair', 'price' => 100]

```

Alternatively, you may also call the `sole` method with no argument to get the first element in the collection if there is only one element:
```


1$collection = collect([




2    ['product' => 'Desk', 'price' => 200],




3]);




4 



5$collection->sole();




6 



7// ['product' => 'Desk', 'price' => 200]




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
]);

$collection->sole();

// ['product' => 'Desk', 'price' => 200]

```

If there are no elements in the collection that should be returned by the `sole` method, an `\Illuminate\Collections\ItemNotFoundException` exception will be thrown. If there is more than one element that should be returned, an `\Illuminate\Collections\MultipleItemsFoundException` will be thrown.
#### [`some()`](https://laravel.com/docs/12.x/collections#method-some)
Alias for the [contains](https://laravel.com/docs/12.x/collections#method-contains) method.
#### [`sort()`](https://laravel.com/docs/12.x/collections#method-sort)
The `sort` method sorts the collection. The sorted collection keeps the original array keys, so in the following example we will use the [values](https://laravel.com/docs/12.x/collections#method-values) method to reset the keys to consecutively numbered indexes:
```


1$collection = collect([5, 3, 1, 2, 4]);




2 



3$sorted = $collection->sort();




4 



5$sorted->values()->all();




6 



7// [1, 2, 3, 4, 5]




$collection = collect([5, 3, 1, 2, 4]);

$sorted = $collection->sort();

$sorted->values()->all();

// [1, 2, 3, 4, 5]

```

If your sorting needs are more advanced, you may pass a callback to `sort` with your own algorithm. Refer to the PHP documentation on `sort` method calls utilizes internally.
If you need to sort a collection of nested arrays or objects, see the [sortBy](https://laravel.com/docs/12.x/collections#method-sortby) and [sortByDesc](https://laravel.com/docs/12.x/collections#method-sortbydesc) methods.
