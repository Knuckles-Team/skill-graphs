## [Method Listing](https://laravel.com/docs/12.x/collections#method-listing)
#### [`after()`](https://laravel.com/docs/12.x/collections#method-after)
The `after` method returns the item after the given item. `null` is returned if the given item is not found or is the last item:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->after(3);




4 



5// 4




6 



7$collection->after(5);




8 



9// null




$collection = collect([1, 2, 3, 4, 5]);

$collection->after(3);

// 4

$collection->after(5);

// null

```

This method searches for the given item using "loose" comparison, meaning a string containing an integer value will be considered equal to an integer of the same value. To use "strict" comparison, you may provide the `strict` argument to the method:
```


1collect([2, 4, 6, 8])->after('4', strict: true);




2 



3// null




collect([2, 4, 6, 8])->after('4', strict: true);

// null

```

Alternatively, you may provide your own closure to search for the first item that passes a given truth test:
```


1collect([2, 4, 6, 8])->after(function (int $item, int $key) {




2    return $item > 5;




3});




4 



5// 8




collect([2, 4, 6, 8])->after(function (int $item, int $key) {
    return $item > 5;
});

// 8

```

#### [`all()`](https://laravel.com/docs/12.x/collections#method-all)
The `all` method returns the underlying array represented by the collection:
```


1collect([1, 2, 3])->all();




2 



3// [1, 2, 3]




collect([1, 2, 3])->all();

// [1, 2, 3]

```

#### [`average()`](https://laravel.com/docs/12.x/collections#method-average)
Alias for the [avg](https://laravel.com/docs/12.x/collections#method-avg) method.
#### [`avg()`](https://laravel.com/docs/12.x/collections#method-avg)
The `avg` method returns the
```


 1$average = collect([




 2    ['foo' => 10],




 3    ['foo' => 10],




 4    ['foo' => 20],




 5    ['foo' => 40]




 6])->avg('foo');




 7 



 8// 20




 9 



10$average = collect([1, 1, 2, 4])->avg();




11 



12// 2




$average = collect([
    ['foo' => 10],
    ['foo' => 10],
    ['foo' => 20],
    ['foo' => 40]
])->avg('foo');

// 20

$average = collect([1, 1, 2, 4])->avg();

// 2

```

#### [`before()`](https://laravel.com/docs/12.x/collections#method-before)
The `before` method is the opposite of the [after](https://laravel.com/docs/12.x/collections#method-after) method. It returns the item before the given item. `null` is returned if the given item is not found or is the first item:
```


 1$collection = collect([1, 2, 3, 4, 5]);




 2 



 3$collection->before(3);




 4 



 5// 2




 6 



 7$collection->before(1);




 8 



 9// null




10 



11collect([2, 4, 6, 8])->before('4', strict: true);




12 



13// null




14 



15collect([2, 4, 6, 8])->before(function (int $item, int $key) {




16    return $item > 5;




17});




18 



19// 4




$collection = collect([1, 2, 3, 4, 5]);

$collection->before(3);

// 2

$collection->before(1);

// null

collect([2, 4, 6, 8])->before('4', strict: true);

// null

collect([2, 4, 6, 8])->before(function (int $item, int $key) {
    return $item > 5;
});

// 4

```

#### [`chunk()`](https://laravel.com/docs/12.x/collections#method-chunk)
The `chunk` method breaks the collection into multiple, smaller collections of a given size:
```


1$collection = collect([1, 2, 3, 4, 5, 6, 7]);




2 



3$chunks = $collection->chunk(4);




4 



5$chunks->all();




6 



7// [[1, 2, 3, 4], [5, 6, 7]]




$collection = collect([1, 2, 3, 4, 5, 6, 7]);

$chunks = $collection->chunk(4);

$chunks->all();

// [[1, 2, 3, 4], [5, 6, 7]]

```

This method is especially useful in [views](https://laravel.com/docs/12.x/views) when working with a grid system such as [Eloquent](https://laravel.com/docs/12.x/eloquent) models you want to display in a grid:
```


1@foreach ($products->chunk(3) as $chunk)




2    <div class="row">




3        @foreach ($chunk as $product)




4            <div class="col-xs-4">{{ $product->name }}</div>




5        @endforeach




6    </div>




7@endforeach




@foreach ($products->chunk(3) as $chunk)
    <div class="row">
        @foreach ($chunk as $product)
            <div class="col-xs-4">{{ $product->name }}</div>
        @endforeach
    </div>
@endforeach

```

#### [`chunkWhile()`](https://laravel.com/docs/12.x/collections#method-chunkwhile)
The `chunkWhile` method breaks the collection into multiple, smaller collections based on the evaluation of the given callback. The `$chunk` variable passed to the closure may be used to inspect the previous element:
```


1$collection = collect(str_split('AABBCCCD'));




2 



3$chunks = $collection->chunkWhile(function (string $value, int $key, Collection $chunk) {




4    return $value === $chunk->last();




5});




6 



7$chunks->all();




8 



9// [['A', 'A'], ['B', 'B'], ['C', 'C', 'C'], ['D']]




$collection = collect(str_split('AABBCCCD'));

$chunks = $collection->chunkWhile(function (string $value, int $key, Collection $chunk) {
    return $value === $chunk->last();
});

$chunks->all();

// [['A', 'A'], ['B', 'B'], ['C', 'C', 'C'], ['D']]

```

#### [`collapse()`](https://laravel.com/docs/12.x/collections#method-collapse)
The `collapse` method collapses a collection of arrays or collections into a single, flat collection:
```


 1$collection = collect([




 2    [1, 2, 3],




 3    [4, 5, 6],




 4    [7, 8, 9],




 5]);




 6 



 7$collapsed = $collection->collapse();




 8 



 9$collapsed->all();




10 



11// [1, 2, 3, 4, 5, 6, 7, 8, 9]




$collection = collect([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]);

$collapsed = $collection->collapse();

$collapsed->all();

// [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

#### [`collapseWithKeys()`](https://laravel.com/docs/12.x/collections#method-collapsewithkeys)
The `collapseWithKeys` method flattens a collection of arrays or collections into a single collection, keeping the original keys intact. If the collection is already flat, it will return an empty collection:
```


 1$collection = collect([




 2    ['first'  => collect([1, 2, 3])],




 3    ['second' => [4, 5, 6]],




 4    ['third'  => collect([7, 8, 9])]




 5]);




 6 



 7$collapsed = $collection->collapseWithKeys();




 8 



 9$collapsed->all();




10 



11// [




12//     'first'  => [1, 2, 3],




13//     'second' => [4, 5, 6],




14//     'third'  => [7, 8, 9],




15// ]




$collection = collect([
    ['first'  => collect([1, 2, 3])],
    ['second' => [4, 5, 6]],
    ['third'  => collect([7, 8, 9])]
]);

$collapsed = $collection->collapseWithKeys();

$collapsed->all();

// [
//     'first'  => [1, 2, 3],
//     'second' => [4, 5, 6],
//     'third'  => [7, 8, 9],
// ]

```

#### [`collect()`](https://laravel.com/docs/12.x/collections#method-collect)
The `collect` method returns a new `Collection` instance with the items currently in the collection:
```


1$collectionA = collect([1, 2, 3]);




2 



3$collectionB = $collectionA->collect();




4 



5$collectionB->all();




6 



7// [1, 2, 3]




$collectionA = collect([1, 2, 3]);

$collectionB = $collectionA->collect();

$collectionB->all();

// [1, 2, 3]

```

The `collect` method is primarily useful for converting [lazy collections](https://laravel.com/docs/12.x/collections#lazy-collections) into standard `Collection` instances:
```


 1$lazyCollection = LazyCollection::make(function () {




 2    yield 1;




 3    yield 2;




 4    yield 3;




 5});




 6 



 7$collection = $lazyCollection->collect();




 8 



 9$collection::class;




10 



11// 'Illuminate\Support\Collection'




12 



13$collection->all();




14 



15// [1, 2, 3]




$lazyCollection = LazyCollection::make(function () {
    yield 1;
    yield 2;
    yield 3;
});

$collection = $lazyCollection->collect();

$collection::class;

// 'Illuminate\Support\Collection'

$collection->all();

// [1, 2, 3]

```

The `collect` method is especially useful when you have an instance of `Enumerable` and need a non-lazy collection instance. Since `collect()` is part of the `Enumerable` contract, you can safely use it to get a `Collection` instance.
#### [`combine()`](https://laravel.com/docs/12.x/collections#method-combine)
The `combine` method combines the values of the collection, as keys, with the values of another array or collection:
```


1$collection = collect(['name', 'age']);




2 



3$combined = $collection->combine(['George', 29]);




4 



5$combined->all();




6 



7// ['name' => 'George', 'age' => 29]




$collection = collect(['name', 'age']);

$combined = $collection->combine(['George', 29]);

$combined->all();

// ['name' => 'George', 'age' => 29]

```

#### [`concat()`](https://laravel.com/docs/12.x/collections#method-concat)
The `concat` method appends the given array or collection's values onto the end of another collection:
```


1$collection = collect(['John Doe']);




2 



3$concatenated = $collection->concat(['Jane Doe'])->concat(['name' => 'Johnny Doe']);




4 



5$concatenated->all();




6 



7// ['John Doe', 'Jane Doe', 'Johnny Doe']




$collection = collect(['John Doe']);

$concatenated = $collection->concat(['Jane Doe'])->concat(['name' => 'Johnny Doe']);

$concatenated->all();

// ['John Doe', 'Jane Doe', 'Johnny Doe']

```

The `concat` method numerically reindexes keys for items concatenated onto the original collection. To maintain keys in associative collections, see the [merge](https://laravel.com/docs/12.x/collections#method-merge) method.
#### [`contains()`](https://laravel.com/docs/12.x/collections#method-contains)
The `contains` method determines whether the collection contains a given item. You may pass a closure to the `contains` method to determine if an element exists in the collection matching a given truth test:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->contains(function (int $value, int $key) {




4    return $value > 5;




5});




6 



7// false




$collection = collect([1, 2, 3, 4, 5]);

$collection->contains(function (int $value, int $key) {
    return $value > 5;
});

// false

```

Alternatively, you may pass a string to the `contains` method to determine whether the collection contains a given item value:
```


1$collection = collect(['name' => 'Desk', 'price' => 100]);




2 



3$collection->contains('Desk');




4 



5// true




6 



7$collection->contains('New York');




8 



9// false




$collection = collect(['name' => 'Desk', 'price' => 100]);

$collection->contains('Desk');

// true

$collection->contains('New York');

// false

```

You may also pass a key / value pair to the `contains` method, which will determine if the given pair exists in the collection:
```


1$collection = collect([




2    ['product' => 'Desk', 'price' => 200],




3    ['product' => 'Chair', 'price' => 100],




4]);




5 



6$collection->contains('product', 'Bookcase');




7 



8// false




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Chair', 'price' => 100],
]);

$collection->contains('product', 'Bookcase');

// false

```

The `contains` method uses "loose" comparisons when checking item values, meaning a string with an integer value will be considered equal to an integer of the same value. Use the [containsStrict](https://laravel.com/docs/12.x/collections#method-containsstrict) method to filter using "strict" comparisons.
For the inverse of `contains`, see the [doesntContain](https://laravel.com/docs/12.x/collections#method-doesntcontain) method.
#### [`containsStrict()`](https://laravel.com/docs/12.x/collections#method-containsstrict)
This method has the same signature as the [contains](https://laravel.com/docs/12.x/collections#method-contains) method; however, all values are compared using "strict" comparisons.
This method's behavior is modified when using [Eloquent Collections](https://laravel.com/docs/12.x/eloquent-collections#method-contains).
#### [`count()`](https://laravel.com/docs/12.x/collections#method-count)
The `count` method returns the total number of items in the collection:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$collection->count();




4 



5// 4




$collection = collect([1, 2, 3, 4]);

$collection->count();

// 4

```

#### [`countBy()`](https://laravel.com/docs/12.x/collections#method-countBy)
The `countBy` method counts the occurrences of values in the collection. By default, the method counts the occurrences of every element, allowing you to count certain "types" of elements in the collection:
```


1$collection = collect([1, 2, 2, 2, 3]);




2 



3$counted = $collection->countBy();




4 



5$counted->all();




6 



7// [1 => 1, 2 => 3, 3 => 1]




$collection = collect([1, 2, 2, 2, 3]);

$counted = $collection->countBy();

$counted->all();

// [1 => 1, 2 => 3, 3 => 1]

```

You may pass a closure to the `countBy` method to count all items by a custom value:
```


1$collection = collect(['alice@gmail.com', 'bob@yahoo.com', 'carlos@gmail.com']);




2 



3$counted = $collection->countBy(function (string $email) {




4    return substr(strrchr($email, '@'), 1);




5});




6 



7$counted->all();




8 



9// ['gmail.com' => 2, 'yahoo.com' => 1]




$collection = collect(['alice@gmail.com', 'bob@yahoo.com', 'carlos@gmail.com']);

$counted = $collection->countBy(function (string $email) {
    return substr(strrchr($email, '@'), 1);
});

$counted->all();

// ['gmail.com' => 2, 'yahoo.com' => 1]

```

#### [`crossJoin()`](https://laravel.com/docs/12.x/collections#method-crossjoin)
The `crossJoin` method cross joins the collection's values among the given arrays or collections, returning a Cartesian product with all possible permutations:
```


 1$collection = collect([1, 2]);




 2 



 3$matrix = $collection->crossJoin(['a', 'b']);




 4 



 5$matrix->all();




 6 



 7/*




 8    [




 9        [1, 'a'],




10        [1, 'b'],




11        [2, 'a'],




12        [2, 'b'],




13    ]




14*/




15 



16$collection = collect([1, 2]);




17 



18$matrix = $collection->crossJoin(['a', 'b'], ['I', 'II']);




19 



20$matrix->all();




21 



22/*




23    [




24        [1, 'a', 'I'],




25        [1, 'a', 'II'],




26        [1, 'b', 'I'],




27        [1, 'b', 'II'],




28        [2, 'a', 'I'],




29        [2, 'a', 'II'],




30        [2, 'b', 'I'],




31        [2, 'b', 'II'],




32    ]




33*/




$collection = collect([1, 2]);

$matrix = $collection->crossJoin(['a', 'b']);

$matrix->all();

/*
    [
        [1, 'a'],
        [1, 'b'],
        [2, 'a'],
        [2, 'b'],
    ]
*/

$collection = collect([1, 2]);

$matrix = $collection->crossJoin(['a', 'b'], ['I', 'II']);

$matrix->all();

/*
    [
        [1, 'a', 'I'],
        [1, 'a', 'II'],
        [1, 'b', 'I'],
        [1, 'b', 'II'],
        [2, 'a', 'I'],
        [2, 'a', 'II'],
        [2, 'b', 'I'],
        [2, 'b', 'II'],
    ]
*/

```

#### [`dd()`](https://laravel.com/docs/12.x/collections#method-dd)
The `dd` method dumps the collection's items and ends execution of the script:
```


 1$collection = collect(['John Doe', 'Jane Doe']);




 2 



 3$collection->dd();




 4 



 5/*




 6    array:2 [




 7        0 => "John Doe"




 8        1 => "Jane Doe"




 9    ]




10*/




$collection = collect(['John Doe', 'Jane Doe']);

$collection->dd();

/*
    array:2 [
        0 => "John Doe"
        1 => "Jane Doe"
    ]
*/

```

If you do not want to stop executing the script, use the [dump](https://laravel.com/docs/12.x/collections#method-dump) method instead.
#### [`diff()`](https://laravel.com/docs/12.x/collections#method-diff)
The `diff` method compares the collection against another collection or a plain PHP `array` based on its values. This method will return the values in the original collection that are not present in the given collection:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$diff = $collection->diff([2, 4, 6, 8]);




4 



5$diff->all();




6 



7// [1, 3, 5]




$collection = collect([1, 2, 3, 4, 5]);

$diff = $collection->diff([2, 4, 6, 8]);

$diff->all();

// [1, 3, 5]

```

This method's behavior is modified when using [Eloquent Collections](https://laravel.com/docs/12.x/eloquent-collections#method-diff).
#### [`diffAssoc()`](https://laravel.com/docs/12.x/collections#method-diffassoc)
The `diffAssoc` method compares the collection against another collection or a plain PHP `array` based on its keys and values. This method will return the key / value pairs in the original collection that are not present in the given collection:
```


 1$collection = collect([




 2    'color' => 'orange',




 3    'type' => 'fruit',




 4    'remain' => 6,




 5]);




 6 



 7$diff = $collection->diffAssoc([




 8    'color' => 'yellow',




 9    'type' => 'fruit',




10    'remain' => 3,




11    'used' => 6,




12]);




13 



14$diff->all();




15 



16// ['color' => 'orange', 'remain' => 6]




$collection = collect([
    'color' => 'orange',
    'type' => 'fruit',
    'remain' => 6,
]);

$diff = $collection->diffAssoc([
    'color' => 'yellow',
    'type' => 'fruit',
    'remain' => 3,
    'used' => 6,
]);

$diff->all();

// ['color' => 'orange', 'remain' => 6]

```

#### [`diffAssocUsing()`](https://laravel.com/docs/12.x/collections#method-diffassocusing)
Unlike `diffAssoc`, `diffAssocUsing` accepts a user supplied callback function for the indices comparison:
```


 1$collection = collect([




 2    'color' => 'orange',




 3    'type' => 'fruit',




 4    'remain' => 6,




 5]);




 6 



 7$diff = $collection->diffAssocUsing([




 8    'Color' => 'yellow',




 9    'Type' => 'fruit',




10    'Remain' => 3,




11], 'strnatcasecmp');




12 



13$diff->all();




14 



15// ['color' => 'orange', 'remain' => 6]




$collection = collect([
    'color' => 'orange',
    'type' => 'fruit',
    'remain' => 6,
]);

$diff = $collection->diffAssocUsing([
    'Color' => 'yellow',
    'Type' => 'fruit',
    'Remain' => 3,
], 'strnatcasecmp');

$diff->all();

// ['color' => 'orange', 'remain' => 6]

```

The callback must be a comparison function that returns an integer less than, equal to, or greater than zero. For more information, refer to the PHP documentation on `diffAssocUsing` method utilizes internally.
#### [`diffKeys()`](https://laravel.com/docs/12.x/collections#method-diffkeys)
The `diffKeys` method compares the collection against another collection or a plain PHP `array` based on its keys. This method will return the key / value pairs in the original collection that are not present in the given collection:
```


 1$collection = collect([




 2    'one' => 10,




 3    'two' => 20,




 4    'three' => 30,




 5    'four' => 40,




 6    'five' => 50,




 7]);




 8 



 9$diff = $collection->diffKeys([




10    'two' => 2,




11    'four' => 4,




12    'six' => 6,




13    'eight' => 8,




14]);




15 



16$diff->all();




17 



18// ['one' => 10, 'three' => 30, 'five' => 50]




$collection = collect([
    'one' => 10,
    'two' => 20,
    'three' => 30,
    'four' => 40,
    'five' => 50,
]);

$diff = $collection->diffKeys([
    'two' => 2,
    'four' => 4,
    'six' => 6,
    'eight' => 8,
]);

$diff->all();

// ['one' => 10, 'three' => 30, 'five' => 50]

```

#### [`doesntContain()`](https://laravel.com/docs/12.x/collections#method-doesntcontain)
The `doesntContain` method determines whether the collection does not contain a given item. You may pass a closure to the `doesntContain` method to determine if an element does not exist in the collection matching a given truth test:
```


1$collection = collect([1, 2, 3, 4, 5]);




2 



3$collection->doesntContain(function (int $value, int $key) {




4    return $value < 5;




5});




6 



7// false




$collection = collect([1, 2, 3, 4, 5]);

$collection->doesntContain(function (int $value, int $key) {
    return $value < 5;
});

// false

```

Alternatively, you may pass a string to the `doesntContain` method to determine whether the collection does not contain a given item value:
```


1$collection = collect(['name' => 'Desk', 'price' => 100]);




2 



3$collection->doesntContain('Table');




4 



5// true




6 



7$collection->doesntContain('Desk');




8 



9// false




$collection = collect(['name' => 'Desk', 'price' => 100]);

$collection->doesntContain('Table');

// true

$collection->doesntContain('Desk');

// false

```

You may also pass a key / value pair to the `doesntContain` method, which will determine if the given pair does not exist in the collection:
```


1$collection = collect([




2    ['product' => 'Desk', 'price' => 200],




3    ['product' => 'Chair', 'price' => 100],




4]);




5 



6$collection->doesntContain('product', 'Bookcase');




7 



8// true




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Chair', 'price' => 100],
]);

$collection->doesntContain('product', 'Bookcase');

// true

```

The `doesntContain` method uses "loose" comparisons when checking item values, meaning a string with an integer value will be considered equal to an integer of the same value.
#### [`doesntContainStrict()`](https://laravel.com/docs/12.x/collections#method-doesntcontainstrict)
This method has the same signature as the [doesntContain](https://laravel.com/docs/12.x/collections#method-doesntcontain) method; however, all values are compared using "strict" comparisons.
#### [`dot()`](https://laravel.com/docs/12.x/collections#method-dot)
The `dot` method flattens a multi-dimensional collection into a single level collection that uses "dot" notation to indicate depth:
```


1$collection = collect(['products' => ['desk' => ['price' => 100]]]);




2 



3$flattened = $collection->dot();




4 



5$flattened->all();




6 



7// ['products.desk.price' => 100]




$collection = collect(['products' => ['desk' => ['price' => 100]]]);

$flattened = $collection->dot();

$flattened->all();

// ['products.desk.price' => 100]

```

#### [`dump()`](https://laravel.com/docs/12.x/collections#method-dump)
The `dump` method dumps the collection's items:
```


 1$collection = collect(['John Doe', 'Jane Doe']);




 2 



 3$collection->dump();




 4 



 5/*




 6    array:2 [




 7        0 => "John Doe"




 8        1 => "Jane Doe"




 9    ]




10*/




$collection = collect(['John Doe', 'Jane Doe']);

$collection->dump();

/*
    array:2 [
        0 => "John Doe"
        1 => "Jane Doe"
    ]
*/

```

If you want to stop executing the script after dumping the collection, use the [dd](https://laravel.com/docs/12.x/collections#method-dd) method instead.
#### [`duplicates()`](https://laravel.com/docs/12.x/collections#method-duplicates)
The `duplicates` method retrieves and returns duplicate values from the collection:
```


1$collection = collect(['a', 'b', 'a', 'c', 'b']);




2 



3$collection->duplicates();




4 



5// [2 => 'a', 4 => 'b']




$collection = collect(['a', 'b', 'a', 'c', 'b']);

$collection->duplicates();

// [2 => 'a', 4 => 'b']

```

If the collection contains arrays or objects, you can pass the key of the attributes that you wish to check for duplicate values:
```


1$employees = collect([




2    ['email' => 'abigail@example.com', 'position' => 'Developer'],




3    ['email' => 'james@example.com', 'position' => 'Designer'],




4    ['email' => 'victoria@example.com', 'position' => 'Developer'],




5]);




6 



7$employees->duplicates('position');




8 



9// [2 => 'Developer']




$employees = collect([
    ['email' => 'abigail@example.com', 'position' => 'Developer'],
    ['email' => 'james@example.com', 'position' => 'Designer'],
    ['email' => 'victoria@example.com', 'position' => 'Developer'],
]);

$employees->duplicates('position');

// [2 => 'Developer']

```

#### [`duplicatesStrict()`](https://laravel.com/docs/12.x/collections#method-duplicatesstrict)
This method has the same signature as the [duplicates](https://laravel.com/docs/12.x/collections#method-duplicates) method; however, all values are compared using "strict" comparisons.
#### [`each()`](https://laravel.com/docs/12.x/collections#method-each)
The `each` method iterates over the items in the collection and passes each item to a closure:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$collection->each(function (int $item, int $key) {




4    // ...




5});




$collection = collect([1, 2, 3, 4]);

$collection->each(function (int $item, int $key) {
    // ...
});

```

If you would like to stop iterating through the items, you may return `false` from your closure:
```


1$collection->each(function (int $item, int $key) {




2    if (/* condition */) {




3        return false;




4    }




5});




$collection->each(function (int $item, int $key) {
    if (/* condition */) {
        return false;
    }
});

```

#### [`eachSpread()`](https://laravel.com/docs/12.x/collections#method-eachspread)
The `eachSpread` method iterates over the collection's items, passing each nested item value into the given callback:
```


1$collection = collect([['John Doe', 35], ['Jane Doe', 33]]);




2 



3$collection->eachSpread(function (string $name, int $age) {




4    // ...




5});




$collection = collect([['John Doe', 35], ['Jane Doe', 33]]);

$collection->eachSpread(function (string $name, int $age) {
    // ...
});

```

You may stop iterating through the items by returning `false` from the callback:
