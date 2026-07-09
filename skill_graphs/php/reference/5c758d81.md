```


1$collection->eachSpread(function (string $name, int $age) {




2    return false;




3});




$collection->eachSpread(function (string $name, int $age) {
    return false;
});

```

#### [`ensure()`](https://laravel.com/docs/12.x/collections#method-ensure)
The `ensure` method may be used to verify that all elements of a collection are of a given type or list of types. Otherwise, an `UnexpectedValueException` will be thrown:
```


1return $collection->ensure(User::class);




2 



3return $collection->ensure([User::class, Customer::class]);




return $collection->ensure(User::class);

return $collection->ensure([User::class, Customer::class]);

```

Primitive types such as `string`, `int`, `float`, `bool`, and `array` may also be specified:
```


1return $collection->ensure('int');




return $collection->ensure('int');

```

The `ensure` method does not guarantee that elements of different types will not be added to the collection at a later time.
#### [`every()`](https://laravel.com/docs/12.x/collections#method-every)
The `every` method may be used to verify that all elements of a collection pass a given truth test:
```


1collect([1, 2, 3, 4])->every(function (int $value, int $key) {




2    return $value > 2;




3});




4 



5// false




collect([1, 2, 3, 4])->every(function (int $value, int $key) {
    return $value > 2;
});

// false

```

If the collection is empty, the `every` method will return true:
```


1$collection = collect([]);




2 



3$collection->every(function (int $value, int $key) {




4    return $value > 2;




5});




6 



7// true




$collection = collect([]);

$collection->every(function (int $value, int $key) {
    return $value > 2;
});

// true

```

#### [`except()`](https://laravel.com/docs/12.x/collections#method-except)
The `except` method returns all items in the collection except for those with the specified keys:
```


1$collection = collect(['product_id' => 1, 'price' => 100, 'discount' => false]);




2 



3$filtered = $collection->except(['price', 'discount']);




4 



5$filtered->all();




6 



7// ['product_id' => 1]




$collection = collect(['product_id' => 1, 'price' => 100, 'discount' => false]);

$filtered = $collection->except(['price', 'discount']);

$filtered->all();

// ['product_id' => 1]

```

For the inverse of `except`, see the [only](https://laravel.com/docs/12.x/collections#method-only) method.
This method's behavior is modified when using [Eloquent Collections](https://laravel.com/docs/12.x/eloquent-collections#method-except).
#### [`filter()`](https://laravel.com/docs/12.x/collections#method-filter)
The `filter` method filters the collection using the given callback, keeping only those items that pass a given truth test:
```


1$collection = collect([1, 2, 3, 4]);




2 



3$filtered = $collection->filter(function (int $value, int $key) {




4    return $value > 2;




5});




6 



7$filtered->all();




8 



9// [3, 4]




$collection = collect([1, 2, 3, 4]);

$filtered = $collection->filter(function (int $value, int $key) {
    return $value > 2;
});

$filtered->all();

// [3, 4]

```

If no callback is supplied, all entries of the collection that are equivalent to `false` will be removed:
```


1$collection = collect([1, 2, 3, null, false, '', 0, []]);




2 



3$collection->filter()->all();




4 



5// [1, 2, 3]




$collection = collect([1, 2, 3, null, false, '', 0, []]);

$collection->filter()->all();

// [1, 2, 3]

```

For the inverse of `filter`, see the [reject](https://laravel.com/docs/12.x/collections#method-reject) method.
#### [`first()`](https://laravel.com/docs/12.x/collections#method-first)
The `first` method returns the first element in the collection that passes a given truth test:
```


1collect([1, 2, 3, 4])->first(function (int $value, int $key) {




2    return $value > 2;




3});




4 



5// 3




collect([1, 2, 3, 4])->first(function (int $value, int $key) {
    return $value > 2;
});

// 3

```

You may also call the `first` method with no arguments to get the first element in the collection. If the collection is empty, `null` is returned:
```


1collect([1, 2, 3, 4])->first();




2 



3// 1




collect([1, 2, 3, 4])->first();

// 1

```

#### [`firstOrFail()`](https://laravel.com/docs/12.x/collections#method-first-or-fail)
The `firstOrFail` method is identical to the `first` method; however, if no result is found, an `Illuminate\Support\ItemNotFoundException` exception will be thrown:
```


1collect([1, 2, 3, 4])->firstOrFail(function (int $value, int $key) {




2    return $value > 5;




3});




4 



5// Throws ItemNotFoundException...




collect([1, 2, 3, 4])->firstOrFail(function (int $value, int $key) {
    return $value > 5;
});

// Throws ItemNotFoundException...

```

You may also call the `firstOrFail` method with no arguments to get the first element in the collection. If the collection is empty, an `Illuminate\Support\ItemNotFoundException` exception will be thrown:
```


1collect([])->firstOrFail();




2 



3// Throws ItemNotFoundException...




collect([])->firstOrFail();

// Throws ItemNotFoundException...

```

#### [`firstWhere()`](https://laravel.com/docs/12.x/collections#method-first-where)
The `firstWhere` method returns the first element in the collection with the given key / value pair:
```


 1$collection = collect([




 2    ['name' => 'Regena', 'age' => null],




 3    ['name' => 'Linda', 'age' => 14],




 4    ['name' => 'Diego', 'age' => 23],




 5    ['name' => 'Linda', 'age' => 84],




 6]);




 7 



 8$collection->firstWhere('name', 'Linda');




 9 



10// ['name' => 'Linda', 'age' => 14]




$collection = collect([
    ['name' => 'Regena', 'age' => null],
    ['name' => 'Linda', 'age' => 14],
    ['name' => 'Diego', 'age' => 23],
    ['name' => 'Linda', 'age' => 84],
]);

$collection->firstWhere('name', 'Linda');

// ['name' => 'Linda', 'age' => 14]

```

You may also call the `firstWhere` method with a comparison operator:
```


1$collection->firstWhere('age', '>=', 18);




2 



3// ['name' => 'Diego', 'age' => 23]




$collection->firstWhere('age', '>=', 18);

// ['name' => 'Diego', 'age' => 23]

```

Like the [where](https://laravel.com/docs/12.x/collections#method-where) method, you may pass one argument to the `firstWhere` method. In this scenario, the `firstWhere` method will return the first item where the given item key's value is "truthy":
```


1$collection->firstWhere('age');




2 



3// ['name' => 'Linda', 'age' => 14]




$collection->firstWhere('age');

// ['name' => 'Linda', 'age' => 14]

```

#### [`flatMap()`](https://laravel.com/docs/12.x/collections#method-flatmap)
The `flatMap` method iterates through the collection and passes each value to the given closure. The closure is free to modify the item and return it, thus forming a new collection of modified items. Then, the array is flattened by one level:
```


 1$collection = collect([




 2    ['name' => 'Sally'],




 3    ['school' => 'Arkansas'],




 4    ['age' => 28]




 5]);




 6 



 7$flattened = $collection->flatMap(function (array $values) {




 8    return array_map('strtoupper', $values);




 9});




10 



11$flattened->all();




12 



13// ['name' => 'SALLY', 'school' => 'ARKANSAS', 'age' => '28'];




$collection = collect([
    ['name' => 'Sally'],
    ['school' => 'Arkansas'],
    ['age' => 28]
]);

$flattened = $collection->flatMap(function (array $values) {
    return array_map('strtoupper', $values);
});

$flattened->all();

// ['name' => 'SALLY', 'school' => 'ARKANSAS', 'age' => '28'];

```

#### [`flatten()`](https://laravel.com/docs/12.x/collections#method-flatten)
The `flatten` method flattens a multi-dimensional collection into a single dimension:
```


 1$collection = collect([




 2    'name' => 'Taylor',




 3    'languages' => [




 4        'PHP', 'JavaScript'




 5    ]




 6]);




 7 



 8$flattened = $collection->flatten();




 9 



10$flattened->all();




11 



12// ['Taylor', 'PHP', 'JavaScript'];




$collection = collect([
    'name' => 'Taylor',
    'languages' => [
        'PHP', 'JavaScript'
    ]
]);

$flattened = $collection->flatten();

$flattened->all();

// ['Taylor', 'PHP', 'JavaScript'];

```

If necessary, you may pass the `flatten` method a "depth" argument:
```


 1$collection = collect([




 2    'Apple' => [




 3        [




 4            'name' => 'iPhone 6S',




 5            'brand' => 'Apple'




 6        ],




 7    ],




 8    'Samsung' => [




 9        [




10            'name' => 'Galaxy S7',




11            'brand' => 'Samsung'




12        ],




13    ],




14]);




15 



16$products = $collection->flatten(1);




17 



18$products->values()->all();




19 



20/*




21    [




22        ['name' => 'iPhone 6S', 'brand' => 'Apple'],




23        ['name' => 'Galaxy S7', 'brand' => 'Samsung'],




24    ]




25*/




$collection = collect([
    'Apple' => [
        [
            'name' => 'iPhone 6S',
            'brand' => 'Apple'
        ],
    ],
    'Samsung' => [
        [
            'name' => 'Galaxy S7',
            'brand' => 'Samsung'
        ],
    ],
]);

$products = $collection->flatten(1);

$products->values()->all();

/*
    [
        ['name' => 'iPhone 6S', 'brand' => 'Apple'],
        ['name' => 'Galaxy S7', 'brand' => 'Samsung'],
    ]
*/

```

In this example, calling `flatten` without providing the depth would have also flattened the nested arrays, resulting in `['iPhone 6S', 'Apple', 'Galaxy S7', 'Samsung']`. Providing a depth allows you to specify the number of levels nested arrays will be flattened.
#### [`flip()`](https://laravel.com/docs/12.x/collections#method-flip)
The `flip` method swaps the collection's keys with their corresponding values:
```


1$collection = collect(['name' => 'Taylor', 'framework' => 'Laravel']);




2 



3$flipped = $collection->flip();




4 



5$flipped->all();




6 



7// ['Taylor' => 'name', 'Laravel' => 'framework']




$collection = collect(['name' => 'Taylor', 'framework' => 'Laravel']);

$flipped = $collection->flip();

$flipped->all();

// ['Taylor' => 'name', 'Laravel' => 'framework']

```

#### [`forget()`](https://laravel.com/docs/12.x/collections#method-forget)
The `forget` method removes an item from the collection by its key:
```


 1$collection = collect(['name' => 'Taylor', 'framework' => 'Laravel']);




 2 



 3// Forget a single key...




 4$collection->forget('name');




 5 



 6// ['framework' => 'Laravel']




 7 



 8// Forget multiple keys...




 9$collection->forget(['name', 'framework']);




10 



11// []




$collection = collect(['name' => 'Taylor', 'framework' => 'Laravel']);

// Forget a single key...
$collection->forget('name');

// ['framework' => 'Laravel']

// Forget multiple keys...
$collection->forget(['name', 'framework']);

// []

```

Unlike most other collection methods, `forget` does not return a new modified collection; it modifies and returns the collection it is called on.
#### [`forPage()`](https://laravel.com/docs/12.x/collections#method-forpage)
The `forPage` method returns a new collection containing the items that would be present on a given page number. The method accepts the page number as its first argument and the number of items to show per page as its second argument:
```


1$collection = collect([1, 2, 3, 4, 5, 6, 7, 8, 9]);




2 



3$chunk = $collection->forPage(2, 3);




4 



5$chunk->all();




6 



7// [4, 5, 6]




$collection = collect([1, 2, 3, 4, 5, 6, 7, 8, 9]);

$chunk = $collection->forPage(2, 3);

$chunk->all();

// [4, 5, 6]

```

#### [`fromJson()`](https://laravel.com/docs/12.x/collections#method-fromjson)
The static `fromJson` method creates a new collection instance by decoding a given JSON string using the `json_decode` PHP function:
```


1use Illuminate\Support\Collection;




2 



3$json = json_encode([




4    'name' => 'Taylor Otwell',




5    'role' => 'Developer',




6    'status' => 'Active',




7]);




8 



9$collection = Collection::fromJson($json);




use Illuminate\Support\Collection;

$json = json_encode([
    'name' => 'Taylor Otwell',
    'role' => 'Developer',
    'status' => 'Active',
]);

$collection = Collection::fromJson($json);

```

#### [`get()`](https://laravel.com/docs/12.x/collections#method-get)
The `get` method returns the item at a given key. If the key does not exist, `null` is returned:
```


1$collection = collect(['name' => 'Taylor', 'framework' => 'Laravel']);




2 



3$value = $collection->get('name');




4 



5// Taylor




$collection = collect(['name' => 'Taylor', 'framework' => 'Laravel']);

$value = $collection->get('name');

// Taylor

```

You may optionally pass a default value as the second argument:
```


1$collection = collect(['name' => 'Taylor', 'framework' => 'Laravel']);




2 



3$value = $collection->get('age', 34);




4 



5// 34




$collection = collect(['name' => 'Taylor', 'framework' => 'Laravel']);

$value = $collection->get('age', 34);

// 34

```

You may even pass a callback as the method's default value. The result of the callback will be returned if the specified key does not exist:
```


1$collection->get('email', function () {




2    return 'taylor@example.com';




3});




4 



5// taylor@example.com




$collection->get('email', function () {
    return 'taylor@example.com';
});

// taylor@example.com

```

#### [`groupBy()`](https://laravel.com/docs/12.x/collections#method-groupby)
The `groupBy` method groups the collection's items by a given key:
```


 1$collection = collect([




 2    ['account_id' => 'account-x10', 'product' => 'Chair'],




 3    ['account_id' => 'account-x10', 'product' => 'Bookcase'],




 4    ['account_id' => 'account-x11', 'product' => 'Desk'],




 5]);




 6 



 7$grouped = $collection->groupBy('account_id');




 8 



 9$grouped->all();




10 



11/*




12    [




13        'account-x10' => [




14            ['account_id' => 'account-x10', 'product' => 'Chair'],




15            ['account_id' => 'account-x10', 'product' => 'Bookcase'],




16        ],




17        'account-x11' => [




18            ['account_id' => 'account-x11', 'product' => 'Desk'],




19        ],




20    ]




21*/




$collection = collect([
    ['account_id' => 'account-x10', 'product' => 'Chair'],
    ['account_id' => 'account-x10', 'product' => 'Bookcase'],
    ['account_id' => 'account-x11', 'product' => 'Desk'],
]);

$grouped = $collection->groupBy('account_id');

$grouped->all();

/*
    [
        'account-x10' => [
            ['account_id' => 'account-x10', 'product' => 'Chair'],
            ['account_id' => 'account-x10', 'product' => 'Bookcase'],
        ],
        'account-x11' => [
            ['account_id' => 'account-x11', 'product' => 'Desk'],
        ],
    ]
*/

```

Instead of passing a string `key`, you may pass a callback. The callback should return the value you wish to key the group by:
```


 1$grouped = $collection->groupBy(function (array $item, int $key) {




 2    return substr($item['account_id'], -3);




 3});




 4 



 5$grouped->all();




 6 



 7/*




 8    [




 9        'x10' => [




10            ['account_id' => 'account-x10', 'product' => 'Chair'],




11            ['account_id' => 'account-x10', 'product' => 'Bookcase'],




12        ],




13        'x11' => [




14            ['account_id' => 'account-x11', 'product' => 'Desk'],




15        ],




16    ]




17*/




$grouped = $collection->groupBy(function (array $item, int $key) {
    return substr($item['account_id'], -3);
});

$grouped->all();

/*
    [
        'x10' => [
            ['account_id' => 'account-x10', 'product' => 'Chair'],
            ['account_id' => 'account-x10', 'product' => 'Bookcase'],
        ],
        'x11' => [
            ['account_id' => 'account-x11', 'product' => 'Desk'],
        ],
    ]
*/

```

Multiple grouping criteria may be passed as an array. Each array element will be applied to the corresponding level within a multi-dimensional array:
```


 1$data = new Collection([




 2    10 => ['user' => 1, 'skill' => 1, 'roles' => ['Role_1', 'Role_3']],




 3    20 => ['user' => 2, 'skill' => 1, 'roles' => ['Role_1', 'Role_2']],




 4    30 => ['user' => 3, 'skill' => 2, 'roles' => ['Role_1']],




 5    40 => ['user' => 4, 'skill' => 2, 'roles' => ['Role_2']],




 6]);




 7 



 8$result = $data->groupBy(['skill', function (array $item) {




 9    return $item['roles'];




10}], preserveKeys: true);




11 



12/*




13[




14    1 => [




15        'Role_1' => [




16            10 => ['user' => 1, 'skill' => 1, 'roles' => ['Role_1', 'Role_3']],




17            20 => ['user' => 2, 'skill' => 1, 'roles' => ['Role_1', 'Role_2']],




18        ],




19        'Role_2' => [




20            20 => ['user' => 2, 'skill' => 1, 'roles' => ['Role_1', 'Role_2']],




21        ],




22        'Role_3' => [




23            10 => ['user' => 1, 'skill' => 1, 'roles' => ['Role_1', 'Role_3']],




24        ],




25    ],




26    2 => [




27        'Role_1' => [




28            30 => ['user' => 3, 'skill' => 2, 'roles' => ['Role_1']],




29        ],




30        'Role_2' => [




31            40 => ['user' => 4, 'skill' => 2, 'roles' => ['Role_2']],




32        ],




33    ],




34];




35*/




$data = new Collection([
    10 => ['user' => 1, 'skill' => 1, 'roles' => ['Role_1', 'Role_3']],
    20 => ['user' => 2, 'skill' => 1, 'roles' => ['Role_1', 'Role_2']],
    30 => ['user' => 3, 'skill' => 2, 'roles' => ['Role_1']],
    40 => ['user' => 4, 'skill' => 2, 'roles' => ['Role_2']],
]);

$result = $data->groupBy(['skill', function (array $item) {
    return $item['roles'];
}], preserveKeys: true);

/*
[
    1 => [
        'Role_1' => [
            10 => ['user' => 1, 'skill' => 1, 'roles' => ['Role_1', 'Role_3']],
            20 => ['user' => 2, 'skill' => 1, 'roles' => ['Role_1', 'Role_2']],
        ],
        'Role_2' => [
            20 => ['user' => 2, 'skill' => 1, 'roles' => ['Role_1', 'Role_2']],
        ],
        'Role_3' => [
            10 => ['user' => 1, 'skill' => 1, 'roles' => ['Role_1', 'Role_3']],
        ],
    ],
    2 => [
        'Role_1' => [
            30 => ['user' => 3, 'skill' => 2, 'roles' => ['Role_1']],
        ],
        'Role_2' => [
            40 => ['user' => 4, 'skill' => 2, 'roles' => ['Role_2']],
        ],
    ],
];
*/

```

#### [`has()`](https://laravel.com/docs/12.x/collections#method-has)
The `has` method determines if a given key exists in the collection:
```


 1$collection = collect(['account_id' => 1, 'product' => 'Desk', 'amount' => 5]);




 2 



 3$collection->has('product');




 4 



 5// true




 6 



 7$collection->has(['product', 'amount']);




 8 



 9// true




10 



11$collection->has(['amount', 'price']);




12 



13// false




$collection = collect(['account_id' => 1, 'product' => 'Desk', 'amount' => 5]);

$collection->has('product');

// true

$collection->has(['product', 'amount']);

// true

$collection->has(['amount', 'price']);

// false

```

#### [`hasAny()`](https://laravel.com/docs/12.x/collections#method-hasany)
The `hasAny` method determines whether any of the given keys exist in the collection:
```


1$collection = collect(['account_id' => 1, 'product' => 'Desk', 'amount' => 5]);




2 



3$collection->hasAny(['product', 'price']);




4 



5// true




6 



7$collection->hasAny(['name', 'price']);




8 



9// false




$collection = collect(['account_id' => 1, 'product' => 'Desk', 'amount' => 5]);

$collection->hasAny(['product', 'price']);

// true

$collection->hasAny(['name', 'price']);

// false

```

#### [`hasMany()`](https://laravel.com/docs/12.x/collections#method-hasmany)
The `hasMany` method determines whether the collection contains multiple items:
```


 1collect([])->hasMany();




 2 



 3// false




 4 



 5collect(['1'])->hasMany();




 6 



 7// false




 8 



 9collect([1, 2, 3])->hasMany();




10 



11// true




12 



13collect([




14    ['age' => 2],




15    ['age' => 3],




16])->hasMany(fn ($item) => $item['age'] === 2)




17 



18// false




collect([])->hasMany();

// false

collect(['1'])->hasMany();

// false

collect([1, 2, 3])->hasMany();

// true

collect([
    ['age' => 2],
    ['age' => 3],
])->hasMany(fn ($item) => $item['age'] === 2)

// false

```

#### [`hasSole()`](https://laravel.com/docs/12.x/collections#method-hassole)
The `hasSole` method determines if the collection contains a single item, optionally matching the given criteria:
```


 1collect([])->hasSole();




 2 



 3// false




 4 



 5collect(['1'])->hasSole();




 6 



 7// true




 8 



 9collect([1, 2, 3])->hasSole(fn (int $item) => $item === 2);




10 



11// true




collect([])->hasSole();

// false

collect(['1'])->hasSole();

// true

collect([1, 2, 3])->hasSole(fn (int $item) => $item === 2);

// true

```

#### [`implode()`](https://laravel.com/docs/12.x/collections#method-implode)
The `implode` method joins items in a collection. Its arguments depend on the type of items in the collection. If the collection contains arrays or objects, you should pass the key of the attributes you wish to join, and the "glue" string you wish to place between the values:
```


1$collection = collect([




2    ['account_id' => 1, 'product' => 'Desk'],




3    ['account_id' => 2, 'product' => 'Chair'],




4]);




5 



6$collection->implode('product', ', ');




7 



8// 'Desk, Chair'




$collection = collect([
    ['account_id' => 1, 'product' => 'Desk'],
    ['account_id' => 2, 'product' => 'Chair'],
]);

$collection->implode('product', ', ');

// 'Desk, Chair'

```

If the collection contains simple strings or numeric values, you should pass the "glue" as the only argument to the method:
```


1collect([1, 2, 3, 4, 5])->implode('-');




2 



3// '1-2-3-4-5'




collect([1, 2, 3, 4, 5])->implode('-');

// '1-2-3-4-5'

```

You may pass a closure to the `implode` method if you would like to format the values being imploded:
```


1$collection->implode(function (array $item, int $key) {




2    return strtoupper($item['product']);




3}, ', ');




4 



5// 'DESK, CHAIR'




$collection->implode(function (array $item, int $key) {
    return strtoupper($item['product']);
}, ', ');

// 'DESK, CHAIR'

```

#### [`intersect()`](https://laravel.com/docs/12.x/collections#method-intersect)
The `intersect` method removes any values from the original collection that are not present in the given array or collection. The resulting collection will preserve the original collection's keys:
```


1$collection = collect(['Desk', 'Sofa', 'Chair']);




2 



3$intersect = $collection->intersect(['Desk', 'Chair', 'Bookcase']);




4 



5$intersect->all();




6 



7// [0 => 'Desk', 2 => 'Chair']




$collection = collect(['Desk', 'Sofa', 'Chair']);

$intersect = $collection->intersect(['Desk', 'Chair', 'Bookcase']);

$intersect->all();

// [0 => 'Desk', 2 => 'Chair']

```

This method's behavior is modified when using [Eloquent Collections](https://laravel.com/docs/12.x/eloquent-collections#method-intersect).
#### [`intersectUsing()`](https://laravel.com/docs/12.x/collections#method-intersectusing)
The `intersectUsing` method removes any values from the original collection that are not present in the given array or collection, using a custom callback to compare the values. The resulting collection will preserve the original collection's keys:
```


1$collection = collect(['Desk', 'Sofa', 'Chair']);




2 



3$intersect = $collection->intersectUsing(['desk', 'chair', 'bookcase'], function (string $a, string $b) {




4    return strcasecmp($a, $b);




5});




6 



7$intersect->all();




8 



9// [0 => 'Desk', 2 => 'Chair']




$collection = collect(['Desk', 'Sofa', 'Chair']);

$intersect = $collection->intersectUsing(['desk', 'chair', 'bookcase'], function (string $a, string $b) {
    return strcasecmp($a, $b);
});

$intersect->all();

// [0 => 'Desk', 2 => 'Chair']

```

#### [`intersectAssoc()`](https://laravel.com/docs/12.x/collections#method-intersectAssoc)
The `intersectAssoc` method compares the original collection against another collection or array, returning the key / value pairs that are present in all of the given collections:
```


 1$collection = collect([




 2    'color' => 'red',




 3    'size' => 'M',




 4    'material' => 'cotton'




 5]);




 6 



 7$intersect = $collection->intersectAssoc([




 8    'color' => 'blue',




 9    'size' => 'M',




10    'material' => 'polyester'




11]);




12 



13$intersect->all();




14 



15// ['size' => 'M']




$collection = collect([
    'color' => 'red',
    'size' => 'M',
    'material' => 'cotton'
]);

$intersect = $collection->intersectAssoc([
    'color' => 'blue',
    'size' => 'M',
    'material' => 'polyester'
]);

$intersect->all();

// ['size' => 'M']

```

#### [`intersectAssocUsing()`](https://laravel.com/docs/12.x/collections#method-intersectassocusing)
The `intersectAssocUsing` method compares the original collection against another collection or array, returning the key / value pairs that are present in both, using a custom comparison callback to determine equality for both keys and values:
```


 1$collection = collect([




 2    'color' => 'red',




 3    'Size' => 'M',




 4    'material' => 'cotton',




 5]);




 6 



 7$intersect = $collection->intersectAssocUsing([
