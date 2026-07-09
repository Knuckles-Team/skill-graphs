#### [`uniqueStrict()`](https://laravel.com/docs/12.x/collections#method-uniquestrict)
This method has the same signature as the [unique](https://laravel.com/docs/12.x/collections#method-unique) method; however, all values are compared using "strict" comparisons.
#### [`unless()`](https://laravel.com/docs/12.x/collections#method-unless)
The `unless` method will execute the given callback unless the first argument given to the method evaluates to `true`. The collection instance and the first argument given to the `unless` method will be provided to the closure:
```


 1$collection = collect([1, 2, 3]);




 2 



 3$collection->unless(true, function (Collection $collection, bool $value) {




 4    return $collection->push(4);




 5});




 6 



 7$collection->unless(false, function (Collection $collection, bool $value) {




 8    return $collection->push(5);




 9});




10 



11$collection->all();




12 



13// [1, 2, 3, 5]




$collection = collect([1, 2, 3]);

$collection->unless(true, function (Collection $collection, bool $value) {
    return $collection->push(4);
});

$collection->unless(false, function (Collection $collection, bool $value) {
    return $collection->push(5);
});

$collection->all();

// [1, 2, 3, 5]

```

A second callback may be passed to the `unless` method. The second callback will be executed when the first argument given to the `unless` method evaluates to `true`:
```


 1$collection = collect([1, 2, 3]);




 2 



 3$collection->unless(true, function (Collection $collection, bool $value) {




 4    return $collection->push(4);




 5}, function (Collection $collection, bool $value) {




 6    return $collection->push(5);




 7});




 8 



 9$collection->all();




10 



11// [1, 2, 3, 5]




$collection = collect([1, 2, 3]);

$collection->unless(true, function (Collection $collection, bool $value) {
    return $collection->push(4);
}, function (Collection $collection, bool $value) {
    return $collection->push(5);
});

$collection->all();

// [1, 2, 3, 5]

```

For the inverse of `unless`, see the [when](https://laravel.com/docs/12.x/collections#method-when) method.
#### [`unlessEmpty()`](https://laravel.com/docs/12.x/collections#method-unlessempty)
Alias for the [whenNotEmpty](https://laravel.com/docs/12.x/collections#method-whennotempty) method.
#### [`unlessNotEmpty()`](https://laravel.com/docs/12.x/collections#method-unlessnotempty)
Alias for the [whenEmpty](https://laravel.com/docs/12.x/collections#method-whenempty) method.
#### [`unwrap()`](https://laravel.com/docs/12.x/collections#method-unwrap)
The static `unwrap` method returns the collection's underlying items from the given value when applicable:
```


 1Collection::unwrap(collect('John Doe'));




 2 



 3// ['John Doe']




 4 



 5Collection::unwrap(['John Doe']);




 6 



 7// ['John Doe']




 8 



 9Collection::unwrap('John Doe');




10 



11// 'John Doe'




Collection::unwrap(collect('John Doe'));

// ['John Doe']

Collection::unwrap(['John Doe']);

// ['John Doe']

Collection::unwrap('John Doe');

// 'John Doe'

```

#### [`value()`](https://laravel.com/docs/12.x/collections#method-value)
The `value` method retrieves a given value from the first element of the collection:
```


1$collection = collect([




2    ['product' => 'Desk', 'price' => 200],




3    ['product' => 'Speaker', 'price' => 400],




4]);




5 



6$value = $collection->value('price');




7 



8// 200




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Speaker', 'price' => 400],
]);

$value = $collection->value('price');

// 200

```

#### [`values()`](https://laravel.com/docs/12.x/collections#method-values)
The `values` method returns a new collection with the keys reset to consecutive integers:
```


 1$collection = collect([




 2    10 => ['product' => 'Desk', 'price' => 200],




 3    11 => ['product' => 'Speaker', 'price' => 400],




 4]);




 5 



 6$values = $collection->values();




 7 



 8$values->all();




 9 



10/*




11    [




12        0 => ['product' => 'Desk', 'price' => 200],




13        1 => ['product' => 'Speaker', 'price' => 400],




14    ]




15*/




$collection = collect([
    10 => ['product' => 'Desk', 'price' => 200],
    11 => ['product' => 'Speaker', 'price' => 400],
]);

$values = $collection->values();

$values->all();

/*
    [
        0 => ['product' => 'Desk', 'price' => 200],
        1 => ['product' => 'Speaker', 'price' => 400],
    ]
*/

```

#### [`when()`](https://laravel.com/docs/12.x/collections#method-when)
The `when` method will execute the given callback when the first argument given to the method evaluates to `true`. The collection instance and the first argument given to the `when` method will be provided to the closure:
```


 1$collection = collect([1, 2, 3]);




 2 



 3$collection->when(true, function (Collection $collection, bool $value) {




 4    return $collection->push(4);




 5});




 6 



 7$collection->when(false, function (Collection $collection, bool $value) {




 8    return $collection->push(5);




 9});




10 



11$collection->all();




12 



13// [1, 2, 3, 4]




$collection = collect([1, 2, 3]);

$collection->when(true, function (Collection $collection, bool $value) {
    return $collection->push(4);
});

$collection->when(false, function (Collection $collection, bool $value) {
    return $collection->push(5);
});

$collection->all();

// [1, 2, 3, 4]

```

A second callback may be passed to the `when` method. The second callback will be executed when the first argument given to the `when` method evaluates to `false`:
```


 1$collection = collect([1, 2, 3]);




 2 



 3$collection->when(false, function (Collection $collection, bool $value) {




 4    return $collection->push(4);




 5}, function (Collection $collection, bool $value) {




 6    return $collection->push(5);




 7});




 8 



 9$collection->all();




10 



11// [1, 2, 3, 5]




$collection = collect([1, 2, 3]);

$collection->when(false, function (Collection $collection, bool $value) {
    return $collection->push(4);
}, function (Collection $collection, bool $value) {
    return $collection->push(5);
});

$collection->all();

// [1, 2, 3, 5]

```

For the inverse of `when`, see the [unless](https://laravel.com/docs/12.x/collections#method-unless) method.
#### [`whenEmpty()`](https://laravel.com/docs/12.x/collections#method-whenempty)
The `whenEmpty` method will execute the given callback when the collection is empty:
```


 1$collection = collect(['Michael', 'Tom']);




 2 



 3$collection->whenEmpty(function (Collection $collection) {




 4    return $collection->push('Adam');




 5});




 6 



 7$collection->all();




 8 



 9// ['Michael', 'Tom']




10 



11$collection = collect();




12 



13$collection->whenEmpty(function (Collection $collection) {




14    return $collection->push('Adam');




15});




16 



17$collection->all();




18 



19// ['Adam']




$collection = collect(['Michael', 'Tom']);

$collection->whenEmpty(function (Collection $collection) {
    return $collection->push('Adam');
});

$collection->all();

// ['Michael', 'Tom']

$collection = collect();

$collection->whenEmpty(function (Collection $collection) {
    return $collection->push('Adam');
});

$collection->all();

// ['Adam']

```

A second closure may be passed to the `whenEmpty` method that will be executed when the collection is not empty:
```


 1$collection = collect(['Michael', 'Tom']);




 2 



 3$collection->whenEmpty(function (Collection $collection) {




 4    return $collection->push('Adam');




 5}, function (Collection $collection) {




 6    return $collection->push('Taylor');




 7});




 8 



 9$collection->all();




10 



11// ['Michael', 'Tom', 'Taylor']




$collection = collect(['Michael', 'Tom']);

$collection->whenEmpty(function (Collection $collection) {
    return $collection->push('Adam');
}, function (Collection $collection) {
    return $collection->push('Taylor');
});

$collection->all();

// ['Michael', 'Tom', 'Taylor']

```

For the inverse of `whenEmpty`, see the [whenNotEmpty](https://laravel.com/docs/12.x/collections#method-whennotempty) method.
#### [`whenNotEmpty()`](https://laravel.com/docs/12.x/collections#method-whennotempty)
The `whenNotEmpty` method will execute the given callback when the collection is not empty:
```


 1$collection = collect(['Michael', 'Tom']);




 2 



 3$collection->whenNotEmpty(function (Collection $collection) {




 4    return $collection->push('Adam');




 5});




 6 



 7$collection->all();




 8 



 9// ['Michael', 'Tom', 'Adam']




10 



11$collection = collect();




12 



13$collection->whenNotEmpty(function (Collection $collection) {




14    return $collection->push('Adam');




15});




16 



17$collection->all();




18 



19// []




$collection = collect(['Michael', 'Tom']);

$collection->whenNotEmpty(function (Collection $collection) {
    return $collection->push('Adam');
});

$collection->all();

// ['Michael', 'Tom', 'Adam']

$collection = collect();

$collection->whenNotEmpty(function (Collection $collection) {
    return $collection->push('Adam');
});

$collection->all();

// []

```

A second closure may be passed to the `whenNotEmpty` method that will be executed when the collection is empty:
```


 1$collection = collect();




 2 



 3$collection->whenNotEmpty(function (Collection $collection) {




 4    return $collection->push('Adam');




 5}, function (Collection $collection) {




 6    return $collection->push('Taylor');




 7});




 8 



 9$collection->all();




10 



11// ['Taylor']




$collection = collect();

$collection->whenNotEmpty(function (Collection $collection) {
    return $collection->push('Adam');
}, function (Collection $collection) {
    return $collection->push('Taylor');
});

$collection->all();

// ['Taylor']

```

For the inverse of `whenNotEmpty`, see the [whenEmpty](https://laravel.com/docs/12.x/collections#method-whenempty) method.
#### [`where()`](https://laravel.com/docs/12.x/collections#method-where)
The `where` method filters the collection by a given key / value pair:
```


 1$collection = collect([




 2    ['product' => 'Desk', 'price' => 200],




 3    ['product' => 'Chair', 'price' => 100],




 4    ['product' => 'Bookcase', 'price' => 150],




 5    ['product' => 'Door', 'price' => 100],




 6]);




 7 



 8$filtered = $collection->where('price', 100);




 9 



10$filtered->all();




11 



12/*




13    [




14        ['product' => 'Chair', 'price' => 100],




15        ['product' => 'Door', 'price' => 100],




16    ]




17*/




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Chair', 'price' => 100],
    ['product' => 'Bookcase', 'price' => 150],
    ['product' => 'Door', 'price' => 100],
]);

$filtered = $collection->where('price', 100);

$filtered->all();

/*
    [
        ['product' => 'Chair', 'price' => 100],
        ['product' => 'Door', 'price' => 100],
    ]
*/

```

The `where` method uses "loose" comparisons when checking item values, meaning a string with an integer value will be considered equal to an integer of the same value. Use the [whereStrict](https://laravel.com/docs/12.x/collections#method-wherestrict) method to filter using "strict" comparisons, or the [whereNull](https://laravel.com/docs/12.x/collections#method-wherenull) and [whereNotNull](https://laravel.com/docs/12.x/collections#method-wherenotnull) methods to filter for `null` values.
Optionally, you may pass a comparison operator as the second parameter. Supported operators are: '===', '!==', '!=', '==', '=', '<>', '>', '<', '>=', and '<=':
```


 1$collection = collect([




 2    ['name' => 'Jim', 'platform' => 'Mac'],




 3    ['name' => 'Sally', 'platform' => 'Mac'],




 4    ['name' => 'Sue', 'platform' => 'Linux'],




 5]);




 6 



 7$filtered = $collection->where('platform', '!=', 'Linux');




 8 



 9$filtered->all();




10 



11/*




12    [




13        ['name' => 'Jim', 'platform' => 'Mac'],




14        ['name' => 'Sally', 'platform' => 'Mac'],




15    ]




16*/




$collection = collect([
    ['name' => 'Jim', 'platform' => 'Mac'],
    ['name' => 'Sally', 'platform' => 'Mac'],
    ['name' => 'Sue', 'platform' => 'Linux'],
]);

$filtered = $collection->where('platform', '!=', 'Linux');

$filtered->all();

/*
    [
        ['name' => 'Jim', 'platform' => 'Mac'],
        ['name' => 'Sally', 'platform' => 'Mac'],
    ]
*/

```

#### [`whereStrict()`](https://laravel.com/docs/12.x/collections#method-wherestrict)
This method has the same signature as the [where](https://laravel.com/docs/12.x/collections#method-where) method; however, all values are compared using "strict" comparisons.
#### [`whereBetween()`](https://laravel.com/docs/12.x/collections#method-wherebetween)
The `whereBetween` method filters the collection by determining if a specified item value is within a given range:
```


 1$collection = collect([




 2    ['product' => 'Desk', 'price' => 200],




 3    ['product' => 'Chair', 'price' => 80],




 4    ['product' => 'Bookcase', 'price' => 150],




 5    ['product' => 'Pencil', 'price' => 30],




 6    ['product' => 'Door', 'price' => 100],




 7]);




 8 



 9$filtered = $collection->whereBetween('price', [100, 200]);




10 



11$filtered->all();




12 



13/*




14    [




15        ['product' => 'Desk', 'price' => 200],




16        ['product' => 'Bookcase', 'price' => 150],




17        ['product' => 'Door', 'price' => 100],




18    ]




19*/




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Chair', 'price' => 80],
    ['product' => 'Bookcase', 'price' => 150],
    ['product' => 'Pencil', 'price' => 30],
    ['product' => 'Door', 'price' => 100],
]);

$filtered = $collection->whereBetween('price', [100, 200]);

$filtered->all();

/*
    [
        ['product' => 'Desk', 'price' => 200],
        ['product' => 'Bookcase', 'price' => 150],
        ['product' => 'Door', 'price' => 100],
    ]
*/

```

#### [`whereIn()`](https://laravel.com/docs/12.x/collections#method-wherein)
The `whereIn` method removes elements from the collection that do not have a specified item value that is contained within the given array:
```


 1$collection = collect([




 2    ['product' => 'Desk', 'price' => 200],




 3    ['product' => 'Chair', 'price' => 100],




 4    ['product' => 'Bookcase', 'price' => 150],




 5    ['product' => 'Door', 'price' => 100],




 6]);




 7 



 8$filtered = $collection->whereIn('price', [150, 200]);




 9 



10$filtered->all();




11 



12/*




13    [




14        ['product' => 'Desk', 'price' => 200],




15        ['product' => 'Bookcase', 'price' => 150],




16    ]




17*/




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Chair', 'price' => 100],
    ['product' => 'Bookcase', 'price' => 150],
    ['product' => 'Door', 'price' => 100],
]);

$filtered = $collection->whereIn('price', [150, 200]);

$filtered->all();

/*
    [
        ['product' => 'Desk', 'price' => 200],
        ['product' => 'Bookcase', 'price' => 150],
    ]
*/

```

The `whereIn` method uses "loose" comparisons when checking item values, meaning a string with an integer value will be considered equal to an integer of the same value. Use the [whereInStrict](https://laravel.com/docs/12.x/collections#method-whereinstrict) method to filter using "strict" comparisons.
#### [`whereInStrict()`](https://laravel.com/docs/12.x/collections#method-whereinstrict)
This method has the same signature as the [whereIn](https://laravel.com/docs/12.x/collections#method-wherein) method; however, all values are compared using "strict" comparisons.
#### [`whereInstanceOf()`](https://laravel.com/docs/12.x/collections#method-whereinstanceof)
The `whereInstanceOf` method filters the collection by a given class type:
```


 1use App\Models\User;




 2use App\Models\Post;




 3 



 4$collection = collect([




 5    new User,




 6    new User,




 7    new Post,




 8]);




 9 



10$filtered = $collection->whereInstanceOf(User::class);




11 



12$filtered->all();




13 



14// [App\Models\User, App\Models\User]




use App\Models\User;
use App\Models\Post;

$collection = collect([
    new User,
    new User,
    new Post,
]);

$filtered = $collection->whereInstanceOf(User::class);

$filtered->all();

// [App\Models\User, App\Models\User]

```

#### [`whereNotBetween()`](https://laravel.com/docs/12.x/collections#method-wherenotbetween)
The `whereNotBetween` method filters the collection by determining if a specified item value is outside of a given range:
```


 1$collection = collect([




 2    ['product' => 'Desk', 'price' => 200],




 3    ['product' => 'Chair', 'price' => 80],




 4    ['product' => 'Bookcase', 'price' => 150],




 5    ['product' => 'Pencil', 'price' => 30],




 6    ['product' => 'Door', 'price' => 100],




 7]);




 8 



 9$filtered = $collection->whereNotBetween('price', [100, 200]);




10 



11$filtered->all();




12 



13/*




14    [




15        ['product' => 'Chair', 'price' => 80],




16        ['product' => 'Pencil', 'price' => 30],




17    ]




18*/




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Chair', 'price' => 80],
    ['product' => 'Bookcase', 'price' => 150],
    ['product' => 'Pencil', 'price' => 30],
    ['product' => 'Door', 'price' => 100],
]);

$filtered = $collection->whereNotBetween('price', [100, 200]);

$filtered->all();

/*
    [
        ['product' => 'Chair', 'price' => 80],
        ['product' => 'Pencil', 'price' => 30],
    ]
*/

```

#### [`whereNotIn()`](https://laravel.com/docs/12.x/collections#method-wherenotin)
The `whereNotIn` method removes elements from the collection that have a specified item value that is contained within the given array:
```


 1$collection = collect([




 2    ['product' => 'Desk', 'price' => 200],




 3    ['product' => 'Chair', 'price' => 100],




 4    ['product' => 'Bookcase', 'price' => 150],




 5    ['product' => 'Door', 'price' => 100],




 6]);




 7 



 8$filtered = $collection->whereNotIn('price', [150, 200]);




 9 



10$filtered->all();




11 



12/*




13    [




14        ['product' => 'Chair', 'price' => 100],




15        ['product' => 'Door', 'price' => 100],




16    ]




17*/




$collection = collect([
    ['product' => 'Desk', 'price' => 200],
    ['product' => 'Chair', 'price' => 100],
    ['product' => 'Bookcase', 'price' => 150],
    ['product' => 'Door', 'price' => 100],
]);

$filtered = $collection->whereNotIn('price', [150, 200]);

$filtered->all();

/*
    [
        ['product' => 'Chair', 'price' => 100],
        ['product' => 'Door', 'price' => 100],
    ]
*/

```

The `whereNotIn` method uses "loose" comparisons when checking item values, meaning a string with an integer value will be considered equal to an integer of the same value. Use the [whereNotInStrict](https://laravel.com/docs/12.x/collections#method-wherenotinstrict) method to filter using "strict" comparisons.
#### [`whereNotInStrict()`](https://laravel.com/docs/12.x/collections#method-wherenotinstrict)
This method has the same signature as the [whereNotIn](https://laravel.com/docs/12.x/collections#method-wherenotin) method; however, all values are compared using "strict" comparisons.
#### [`whereNotNull()`](https://laravel.com/docs/12.x/collections#method-wherenotnull)
The `whereNotNull` method returns items from the collection where the given key is not `null`:
```


 1$collection = collect([




 2    ['name' => 'Desk'],




 3    ['name' => null],




 4    ['name' => 'Bookcase'],




 5    ['name' => 0],




 6    ['name' => ''],




 7]);




 8 



 9$filtered = $collection->whereNotNull('name');




10 



11$filtered->all();




12 



13/*




14    [




15        ['name' => 'Desk'],




16        ['name' => 'Bookcase'],




17        ['name' => 0],




18        ['name' => ''],




19    ]




20*/




$collection = collect([
    ['name' => 'Desk'],
    ['name' => null],
    ['name' => 'Bookcase'],
    ['name' => 0],
    ['name' => ''],
]);

$filtered = $collection->whereNotNull('name');

$filtered->all();

/*
    [
        ['name' => 'Desk'],
        ['name' => 'Bookcase'],
        ['name' => 0],
        ['name' => ''],
    ]
*/

```

#### [`whereNull()`](https://laravel.com/docs/12.x/collections#method-wherenull)
The `whereNull` method returns items from the collection where the given key is `null`:
```


 1$collection = collect([




 2    ['name' => 'Desk'],




 3    ['name' => null],




 4    ['name' => 'Bookcase'],




 5    ['name' => 0],




 6    ['name' => ''],




 7]);




 8 



 9$filtered = $collection->whereNull('name');




10 



11$filtered->all();




12 



13/*




14    [




15        ['name' => null],




16    ]




17*/




$collection = collect([
    ['name' => 'Desk'],
    ['name' => null],
    ['name' => 'Bookcase'],
    ['name' => 0],
    ['name' => ''],
]);

$filtered = $collection->whereNull('name');

$filtered->all();

/*
    [
        ['name' => null],
    ]
*/

```

#### [`wrap()`](https://laravel.com/docs/12.x/collections#method-wrap)
The static `wrap` method wraps the given value in a collection when applicable:
```


 1use Illuminate\Support\Collection;




 2 



 3$collection = Collection::wrap('John Doe');




 4 



 5$collection->all();




 6 



 7// ['John Doe']




 8 



 9$collection = Collection::wrap(['John Doe']);




10 



11$collection->all();




12 



13// ['John Doe']




14 



15$collection = Collection::wrap(collect('John Doe'));




16 



17$collection->all();




18 



19// ['John Doe']




use Illuminate\Support\Collection;

$collection = Collection::wrap('John Doe');

$collection->all();

// ['John Doe']

$collection = Collection::wrap(['John Doe']);

$collection->all();

// ['John Doe']

$collection = Collection::wrap(collect('John Doe'));

$collection->all();

// ['John Doe']

```

#### [`zip()`](https://laravel.com/docs/12.x/collections#method-zip)
The `zip` method merges together the values of the given array with the values of the original collection at their corresponding index:
```


1$collection = collect(['Chair', 'Desk']);




2 



3$zipped = $collection->zip([100, 200]);




4 



5$zipped->all();




6 



7// [['Chair', 100], ['Desk', 200]]




$collection = collect(['Chair', 'Desk']);

$zipped = $collection->zip([100, 200]);

$zipped->all();

// [['Chair', 100], ['Desk', 200]]

```
