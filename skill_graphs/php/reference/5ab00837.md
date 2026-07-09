
$numbers = [1, 2, 3, 4, 5, 6];

[$underThree, $equalOrAboveThree] = Arr::partition($numbers, function (int $i) {
    return $i < 3;
});

dump($underThree);

// [1, 2]

dump($equalOrAboveThree);

// [3, 4, 5, 6]

```

#### [`Arr::pluck()`](https://laravel.com/docs/12.x/helpers#method-array-pluck)
The `Arr::pluck` method retrieves all of the values for a given key from an array:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    ['developer' => ['id' => 1, 'name' => 'Taylor']],




 5    ['developer' => ['id' => 2, 'name' => 'Abigail']],




 6];




 7 



 8$names = Arr::pluck($array, 'developer.name');




 9 



10// ['Taylor', 'Abigail']




use Illuminate\Support\Arr;

$array = [
    ['developer' => ['id' => 1, 'name' => 'Taylor']],
    ['developer' => ['id' => 2, 'name' => 'Abigail']],
];

$names = Arr::pluck($array, 'developer.name');

// ['Taylor', 'Abigail']

```

You may also specify how you wish the resulting list to be keyed:
```


1use Illuminate\Support\Arr;




2 



3$names = Arr::pluck($array, 'developer.name', 'developer.id');




4 



5// [1 => 'Taylor', 2 => 'Abigail']




use Illuminate\Support\Arr;

$names = Arr::pluck($array, 'developer.name', 'developer.id');

// [1 => 'Taylor', 2 => 'Abigail']

```

#### [`Arr::prepend()`](https://laravel.com/docs/12.x/helpers#method-array-prepend)
The `Arr::prepend` method will push an item onto the beginning of an array:
```


1use Illuminate\Support\Arr;




2 



3$array = ['one', 'two', 'three', 'four'];




4 



5$array = Arr::prepend($array, 'zero');




6 



7// ['zero', 'one', 'two', 'three', 'four']




use Illuminate\Support\Arr;

$array = ['one', 'two', 'three', 'four'];

$array = Arr::prepend($array, 'zero');

// ['zero', 'one', 'two', 'three', 'four']

```

If needed, you may specify the key that should be used for the value:
```


1use Illuminate\Support\Arr;




2 



3$array = ['price' => 100];




4 



5$array = Arr::prepend($array, 'Desk', 'name');




6 



7// ['name' => 'Desk', 'price' => 100]




use Illuminate\Support\Arr;

$array = ['price' => 100];

$array = Arr::prepend($array, 'Desk', 'name');

// ['name' => 'Desk', 'price' => 100]

```

#### [`Arr::prependKeysWith()`](https://laravel.com/docs/12.x/helpers#method-array-prependkeyswith)
The `Arr::prependKeysWith` prepends all key names of an associative array with the given prefix:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    'name' => 'Desk',




 5    'price' => 100,




 6];




 7 



 8$keyed = Arr::prependKeysWith($array, 'product.');




 9 



10/*




11    [




12        'product.name' => 'Desk',




13        'product.price' => 100,




14    ]




15*/




use Illuminate\Support\Arr;

$array = [
    'name' => 'Desk',
    'price' => 100,
];

$keyed = Arr::prependKeysWith($array, 'product.');

/*
    [
        'product.name' => 'Desk',
        'product.price' => 100,
    ]
*/

```

#### [`Arr::pull()`](https://laravel.com/docs/12.x/helpers#method-array-pull)
The `Arr::pull` method returns and removes a key / value pair from an array:
```


1use Illuminate\Support\Arr;




2 



3$array = ['name' => 'Desk', 'price' => 100];




4 



5$name = Arr::pull($array, 'name');




6 



7// $name: Desk




8 



9// $array: ['price' => 100]




use Illuminate\Support\Arr;

$array = ['name' => 'Desk', 'price' => 100];

$name = Arr::pull($array, 'name');

// $name: Desk

// $array: ['price' => 100]

```

A default value may be passed as the third argument to the method. This value will be returned if the key doesn't exist:
```


1use Illuminate\Support\Arr;




2 



3$value = Arr::pull($array, $key, $default);




use Illuminate\Support\Arr;

$value = Arr::pull($array, $key, $default);

```

#### [`Arr::push()`](https://laravel.com/docs/12.x/helpers#method-array-push)
The `Arr::push` method pushes an item into an array using "dot" notation. If an array does not exist at the given key, it will be created:
```


1use Illuminate\Support\Arr;




2 



3$array = [];




4 



5Arr::push($array, 'office.furniture', 'Desk');




6 



7// $array: ['office' => ['furniture' => ['Desk']]]




use Illuminate\Support\Arr;

$array = [];

Arr::push($array, 'office.furniture', 'Desk');

// $array: ['office' => ['furniture' => ['Desk']]]

```

#### [`Arr::query()`](https://laravel.com/docs/12.x/helpers#method-array-query)
The `Arr::query` method converts the array into a query string:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    'name' => 'Taylor',




 5    'order' => [




 6        'column' => 'created_at',




 7        'direction' => 'desc'




 8    ]




 9];




10 



11Arr::query($array);




12 



13// name=Taylor&order[column]=created_at&order[direction]=desc




use Illuminate\Support\Arr;

$array = [
    'name' => 'Taylor',
    'order' => [
        'column' => 'created_at',
        'direction' => 'desc'
    ]
];

Arr::query($array);

// name=Taylor&order[column]=created_at&order[direction]=desc

```

#### [`Arr::random()`](https://laravel.com/docs/12.x/helpers#method-array-random)
The `Arr::random` method returns a random value from an array:
```


1use Illuminate\Support\Arr;




2 



3$array = [1, 2, 3, 4, 5];




4 



5$random = Arr::random($array);




6 



7// 4 - (retrieved randomly)




use Illuminate\Support\Arr;

$array = [1, 2, 3, 4, 5];

$random = Arr::random($array);

// 4 - (retrieved randomly)

```

You may also specify the number of items to return as an optional second argument. Note that providing this argument will return an array even if only one item is desired:
```


1use Illuminate\Support\Arr;




2 



3$items = Arr::random($array, 2);




4 



5// [2, 5] - (retrieved randomly)




use Illuminate\Support\Arr;

$items = Arr::random($array, 2);

// [2, 5] - (retrieved randomly)

```

#### [`Arr::reject()`](https://laravel.com/docs/12.x/helpers#method-array-reject)
The `Arr::reject` method removes items from an array using the given closure:
```


1use Illuminate\Support\Arr;




2 



3$array = [100, '200', 300, '400', 500];




4 



5$filtered = Arr::reject($array, function (string|int $value, int $key) {




6    return is_string($value);




7});




8 



9// [0 => 100, 2 => 300, 4 => 500]




use Illuminate\Support\Arr;

$array = [100, '200', 300, '400', 500];

$filtered = Arr::reject($array, function (string|int $value, int $key) {
    return is_string($value);
});

// [0 => 100, 2 => 300, 4 => 500]

```

#### [`Arr::select()`](https://laravel.com/docs/12.x/helpers#method-array-select)
The `Arr::select` method selects an array of values from an array:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    ['id' => 1, 'name' => 'Desk', 'price' => 200],




 5    ['id' => 2, 'name' => 'Table', 'price' => 150],




 6    ['id' => 3, 'name' => 'Chair', 'price' => 300],




 7];




 8 



 9Arr::select($array, ['name', 'price']);




10 



11// [['name' => 'Desk', 'price' => 200], ['name' => 'Table', 'price' => 150], ['name' => 'Chair', 'price' => 300]]




use Illuminate\Support\Arr;

$array = [
    ['id' => 1, 'name' => 'Desk', 'price' => 200],
    ['id' => 2, 'name' => 'Table', 'price' => 150],
    ['id' => 3, 'name' => 'Chair', 'price' => 300],
];

Arr::select($array, ['name', 'price']);

// [['name' => 'Desk', 'price' => 200], ['name' => 'Table', 'price' => 150], ['name' => 'Chair', 'price' => 300]]

```

#### [`Arr::set()`](https://laravel.com/docs/12.x/helpers#method-array-set)
The `Arr::set` method sets a value within a deeply nested array using "dot" notation:
```


1use Illuminate\Support\Arr;




2 



3$array = ['products' => ['desk' => ['price' => 100]]];




4 



5Arr::set($array, 'products.desk.price', 200);




6 



7// ['products' => ['desk' => ['price' => 200]]]




use Illuminate\Support\Arr;

$array = ['products' => ['desk' => ['price' => 100]]];

Arr::set($array, 'products.desk.price', 200);

// ['products' => ['desk' => ['price' => 200]]]

```

#### [`Arr::shuffle()`](https://laravel.com/docs/12.x/helpers#method-array-shuffle)
The `Arr::shuffle` method randomly shuffles the items in the array:
```


1use Illuminate\Support\Arr;




2 



3$array = Arr::shuffle([1, 2, 3, 4, 5]);




4 



5// [3, 2, 5, 1, 4] - (generated randomly)




use Illuminate\Support\Arr;

$array = Arr::shuffle([1, 2, 3, 4, 5]);

// [3, 2, 5, 1, 4] - (generated randomly)

```

#### [`Arr::sole()`](https://laravel.com/docs/12.x/helpers#method-array-sole)
The `Arr::sole` method retrieves a single value from an array using the given closure. If more than one value within the array matches the given truth test, an `Illuminate\Support\MultipleItemsFoundException` exception will be thrown. If no values match the truth test, an `Illuminate\Support\ItemNotFoundException` exception will be thrown:
```


1use Illuminate\Support\Arr;




2 



3$array = ['Desk', 'Table', 'Chair'];




4 



5$value = Arr::sole($array, fn (string $value) => $value === 'Desk');




6 



7// 'Desk'




use Illuminate\Support\Arr;

$array = ['Desk', 'Table', 'Chair'];

$value = Arr::sole($array, fn (string $value) => $value === 'Desk');

// 'Desk'

```

#### [`Arr::some()`](https://laravel.com/docs/12.x/helpers#method-array-some)
The `Arr::some` method ensures that at least one of the values in the array passes a given truth test:
```


1use Illuminate\Support\Arr;




2 



3$array = [1, 2, 3];




4 



5Arr::some($array, fn ($i) => $i > 2);




6 



7// true




use Illuminate\Support\Arr;

$array = [1, 2, 3];

Arr::some($array, fn ($i) => $i > 2);

// true

```

#### [`Arr::sort()`](https://laravel.com/docs/12.x/helpers#method-array-sort)
The `Arr::sort` method sorts an array by its values:
```


1use Illuminate\Support\Arr;




2 



3$array = ['Desk', 'Table', 'Chair'];




4 



5$sorted = Arr::sort($array);




6 



7// ['Chair', 'Desk', 'Table']




use Illuminate\Support\Arr;

$array = ['Desk', 'Table', 'Chair'];

$sorted = Arr::sort($array);

// ['Chair', 'Desk', 'Table']

```

You may also sort the array by the results of a given closure:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    ['name' => 'Desk'],




 5    ['name' => 'Table'],




 6    ['name' => 'Chair'],




 7];




 8 



 9$sorted = array_values(Arr::sort($array, function (array $value) {




10    return $value['name'];




11}));




12 



13/*




14    [




15        ['name' => 'Chair'],




16        ['name' => 'Desk'],




17        ['name' => 'Table'],




18    ]




19*/




use Illuminate\Support\Arr;

$array = [
    ['name' => 'Desk'],
    ['name' => 'Table'],
    ['name' => 'Chair'],
];

$sorted = array_values(Arr::sort($array, function (array $value) {
    return $value['name'];
}));

/*
    [
        ['name' => 'Chair'],
        ['name' => 'Desk'],
        ['name' => 'Table'],
    ]
*/

```

#### [`Arr::sortDesc()`](https://laravel.com/docs/12.x/helpers#method-array-sort-desc)
The `Arr::sortDesc` method sorts an array in descending order by its values:
```


1use Illuminate\Support\Arr;




2 



3$array = ['Desk', 'Table', 'Chair'];




4 



5$sorted = Arr::sortDesc($array);




6 



7// ['Table', 'Desk', 'Chair']




use Illuminate\Support\Arr;

$array = ['Desk', 'Table', 'Chair'];

$sorted = Arr::sortDesc($array);

// ['Table', 'Desk', 'Chair']

```

You may also sort the array by the results of a given closure:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    ['name' => 'Desk'],




 5    ['name' => 'Table'],




 6    ['name' => 'Chair'],




 7];




 8 



 9$sorted = array_values(Arr::sortDesc($array, function (array $value) {




10    return $value['name'];




11}));




12 



13/*




14    [




15        ['name' => 'Table'],




16        ['name' => 'Desk'],




17        ['name' => 'Chair'],




18    ]




19*/




use Illuminate\Support\Arr;

$array = [
    ['name' => 'Desk'],
    ['name' => 'Table'],
    ['name' => 'Chair'],
];

$sorted = array_values(Arr::sortDesc($array, function (array $value) {
    return $value['name'];
}));

/*
    [
        ['name' => 'Table'],
        ['name' => 'Desk'],
        ['name' => 'Chair'],
    ]
*/

```

#### [`Arr::sortRecursive()`](https://laravel.com/docs/12.x/helpers#method-array-sort-recursive)
The `Arr::sortRecursive` method recursively sorts an array using the `sort` function for numerically indexed sub-arrays and the `ksort` function for associative sub-arrays:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    ['Roman', 'Taylor', 'Li'],




 5    ['PHP', 'Ruby', 'JavaScript'],




 6    ['one' => 1, 'two' => 2, 'three' => 3],




 7];




 8 



 9$sorted = Arr::sortRecursive($array);




10 



11/*




12    [




13        ['JavaScript', 'PHP', 'Ruby'],




14        ['one' => 1, 'three' => 3, 'two' => 2],




15        ['Li', 'Roman', 'Taylor'],




16    ]




17*/




use Illuminate\Support\Arr;

$array = [
    ['Roman', 'Taylor', 'Li'],
    ['PHP', 'Ruby', 'JavaScript'],
    ['one' => 1, 'two' => 2, 'three' => 3],
];

$sorted = Arr::sortRecursive($array);

/*
    [
        ['JavaScript', 'PHP', 'Ruby'],
        ['one' => 1, 'three' => 3, 'two' => 2],
        ['Li', 'Roman', 'Taylor'],
    ]
*/

```

If you would like the results sorted in descending order, you may use the `Arr::sortRecursiveDesc` method.
```


1$sorted = Arr::sortRecursiveDesc($array);




$sorted = Arr::sortRecursiveDesc($array);

```

#### [`Arr::string()`](https://laravel.com/docs/12.x/helpers#method-array-string)
The `Arr::string` method retrieves a value from a deeply nested array using "dot" notation (just as [Arr::get()](https://laravel.com/docs/12.x/helpers#method-array-get) does), but throws an `InvalidArgumentException` if the requested value is not a `string`:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['name' => 'Joe', 'languages' => ['PHP', 'Ruby']];




 4 



 5$value = Arr::string($array, 'name');




 6 



 7// Joe




 8 



 9$value = Arr::string($array, 'languages');




10 



11// throws InvalidArgumentException




use Illuminate\Support\Arr;

$array = ['name' => 'Joe', 'languages' => ['PHP', 'Ruby']];

$value = Arr::string($array, 'name');

// Joe

$value = Arr::string($array, 'languages');

// throws InvalidArgumentException

```

#### [`Arr::take()`](https://laravel.com/docs/12.x/helpers#method-array-take)
The `Arr::take` method returns a new array with the specified number of items:
```


1use Illuminate\Support\Arr;




2 



3$array = [0, 1, 2, 3, 4, 5];




4 



5$chunk = Arr::take($array, 3);




6 



7// [0, 1, 2]




use Illuminate\Support\Arr;

$array = [0, 1, 2, 3, 4, 5];

$chunk = Arr::take($array, 3);

// [0, 1, 2]

```

You may also pass a negative integer to take the specified number of items from the end of the array:
```


1$array = [0, 1, 2, 3, 4, 5];




2 



3$chunk = Arr::take($array, -2);




4 



5// [4, 5]




$array = [0, 1, 2, 3, 4, 5];

$chunk = Arr::take($array, -2);

// [4, 5]

```

#### [`Arr::toCssClasses()`](https://laravel.com/docs/12.x/helpers#method-array-to-css-classes)
The `Arr::toCssClasses` method conditionally compiles a CSS class string. The method accepts an array of classes where the array key contains the class or classes you wish to add, while the value is a boolean expression. If the array element has a numeric key, it will always be included in the rendered class list:
```


 1use Illuminate\Support\Arr;




 2 



 3$isActive = false;




 4$hasError = true;




 5 



 6$array = ['p-4', 'font-bold' => $isActive, 'bg-red' => $hasError];




 7 



 8$classes = Arr::toCssClasses($array);




 9 



10/*




11    'p-4 bg-red'




12*/




use Illuminate\Support\Arr;

$isActive = false;
$hasError = true;

$array = ['p-4', 'font-bold' => $isActive, 'bg-red' => $hasError];

$classes = Arr::toCssClasses($array);

/*
    'p-4 bg-red'
*/

```

#### [`Arr::toCssStyles()`](https://laravel.com/docs/12.x/helpers#method-array-to-css-styles)
The `Arr::toCssStyles` method conditionally compiles a CSS style string. The method accepts an array of CSS declarations where the array key contains the CSS declaration you wish to add, while the value is a boolean expression. If the array element has a numeric key, it will always be included in the compiled CSS style string:
```


 1use Illuminate\Support\Arr;




 2 



 3$hasColor = true;




 4 



 5$array = ['background-color: blue', 'color: blue' => $hasColor];




 6 



 7$classes = Arr::toCssStyles($array);




 8 



 9/*




10    'background-color: blue; color: blue;'




11*/




use Illuminate\Support\Arr;

$hasColor = true;

$array = ['background-color: blue', 'color: blue' => $hasColor];

$classes = Arr::toCssStyles($array);

/*
    'background-color: blue; color: blue;'
*/

```

This method powers Laravel's functionality allowing [merging classes with a Blade component's attribute bag](https://laravel.com/docs/12.x/blade#conditionally-merge-classes) as well as the `@class` [Blade directive](https://laravel.com/docs/12.x/blade#conditional-classes).
#### [`Arr::undot()`](https://laravel.com/docs/12.x/helpers#method-array-undot)
The `Arr::undot` method expands a single-dimensional array that uses "dot" notation into a multi-dimensional array:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    'user.name' => 'Kevin Malone',




 5    'user.occupation' => 'Accountant',




 6];




 7 



 8$array = Arr::undot($array);




 9 



10// ['user' => ['name' => 'Kevin Malone', 'occupation' => 'Accountant']]




use Illuminate\Support\Arr;

$array = [
    'user.name' => 'Kevin Malone',
    'user.occupation' => 'Accountant',
];

$array = Arr::undot($array);

// ['user' => ['name' => 'Kevin Malone', 'occupation' => 'Accountant']]

```

#### [`Arr::where()`](https://laravel.com/docs/12.x/helpers#method-array-where)
The `Arr::where` method filters an array using the given closure:
```


1use Illuminate\Support\Arr;




2 



3$array = [100, '200', 300, '400', 500];




4 



5$filtered = Arr::where($array, function (string|int $value, int $key) {




6    return is_string($value);




7});




8 



9// [1 => '200', 3 => '400']




use Illuminate\Support\Arr;

$array = [100, '200', 300, '400', 500];

$filtered = Arr::where($array, function (string|int $value, int $key) {
    return is_string($value);
});

// [1 => '200', 3 => '400']

```

#### [`Arr::whereNotNull()`](https://laravel.com/docs/12.x/helpers#method-array-where-not-null)
The `Arr::whereNotNull` method removes all `null` values from the given array:
```


1use Illuminate\Support\Arr;




2 



3$array = [0, null];




4 



5$filtered = Arr::whereNotNull($array);




6 



7// [0 => 0]




use Illuminate\Support\Arr;

$array = [0, null];

$filtered = Arr::whereNotNull($array);

// [0 => 0]

```

#### [`Arr::wrap()`](https://laravel.com/docs/12.x/helpers#method-array-wrap)
The `Arr::wrap` method wraps the given value in an array. If the given value is already an array it will be returned without modification:
```


1use Illuminate\Support\Arr;




2 



3$string = 'Laravel';




4 



5$array = Arr::wrap($string);




6 



7// ['Laravel']




use Illuminate\Support\Arr;

$string = 'Laravel';

$array = Arr::wrap($string);

// ['Laravel']

```

If the given value is `null`, an empty array will be returned:
```


1use Illuminate\Support\Arr;




2 



3$array = Arr::wrap(null);




4 



5// []




use Illuminate\Support\Arr;

$array = Arr::wrap(null);

// []

```

#### [`data_fill()`](https://laravel.com/docs/12.x/helpers#method-data-fill)
The `data_fill` function sets a missing value within a nested array or object using "dot" notation:
```


1$data = ['products' => ['desk' => ['price' => 100]]];




2 



3data_fill($data, 'products.desk.price', 200);




4 



5// ['products' => ['desk' => ['price' => 100]]]




6 



7data_fill($data, 'products.desk.discount', 10);




8 



9// ['products' => ['desk' => ['price' => 100, 'discount' => 10]]]




$data = ['products' => ['desk' => ['price' => 100]]];

data_fill($data, 'products.desk.price', 200);

// ['products' => ['desk' => ['price' => 100]]]

data_fill($data, 'products.desk.discount', 10);

// ['products' => ['desk' => ['price' => 100, 'discount' => 10]]]

```

This function also accepts asterisks as wildcards and will fill the target accordingly:
```


 1$data = [




 2    'products' => [




 3        ['name' => 'Desk 1', 'price' => 100],




 4        ['name' => 'Desk 2'],




 5    ],




 6];




 7 



 8data_fill($data, 'products.*.price', 200);




 9 



10/*




11    [




12        'products' => [




13            ['name' => 'Desk 1', 'price' => 100],




14            ['name' => 'Desk 2', 'price' => 200],




15        ],




16    ]




17*/




$data = [
    'products' => [
        ['name' => 'Desk 1', 'price' => 100],
        ['name' => 'Desk 2'],
    ],
];

data_fill($data, 'products.*.price', 200);

/*
    [
        'products' => [
            ['name' => 'Desk 1', 'price' => 100],
            ['name' => 'Desk 2', 'price' => 200],
        ],
    ]
*/

```

#### [`data_get()`](https://laravel.com/docs/12.x/helpers#method-data-get)
The `data_get` function retrieves a value from a nested array or object using "dot" notation:
```


1$data = ['products' => ['desk' => ['price' => 100]]];




2 



3$price = data_get($data, 'products.desk.price');




4 



5// 100




$data = ['products' => ['desk' => ['price' => 100]]];

$price = data_get($data, 'products.desk.price');

// 100

```

The `data_get` function also accepts a default value, which will be returned if the specified key is not found:
```


1$discount = data_get($data, 'products.desk.discount', 0);




2 



3// 0




$discount = data_get($data, 'products.desk.discount', 0);

// 0

```

The function also accepts wildcards using asterisks, which may target any key of the array or object:
```


1$data = [




2    'product-one' => ['name' => 'Desk 1', 'price' => 100],




3    'product-two' => ['name' => 'Desk 2', 'price' => 150],




4];




5 



6data_get($data, '*.name');




7 



8// ['Desk 1', 'Desk 2'];




$data = [
    'product-one' => ['name' => 'Desk 1', 'price' => 100],
    'product-two' => ['name' => 'Desk 2', 'price' => 150],
];

data_get($data, '*.name');

// ['Desk 1', 'Desk 2'];

```

The `{first}` and `{last}` placeholders may be used to retrieve the first or last items in an array:
```


 1$flight = [




 2    'segments' => [




 3        ['from' => 'LHR', 'departure' => '9:00', 'to' => 'IST', 'arrival' => '15:00'],




 4        ['from' => 'IST', 'departure' => '16:00', 'to' => 'PKX', 'arrival' => '20:00'],




 5    ],




 6];




 7 



 8data_get($flight, 'segments.{first}.arrival');




 9 



10// 15:00




$flight = [
    'segments' => [
        ['from' => 'LHR', 'departure' => '9:00', 'to' => 'IST', 'arrival' => '15:00'],
        ['from' => 'IST', 'departure' => '16:00', 'to' => 'PKX', 'arrival' => '20:00'],
    ],
];

data_get($flight, 'segments.{first}.arrival');

// 15:00

```

#### [`data_set()`](https://laravel.com/docs/12.x/helpers#method-data-set)
The `data_set` function sets a value within a nested array or object using "dot" notation:
```


1$data = ['products' => ['desk' => ['price' => 100]]];




2 



3data_set($data, 'products.desk.price', 200);




4 



5// ['products' => ['desk' => ['price' => 200]]]




$data = ['products' => ['desk' => ['price' => 100]]];

data_set($data, 'products.desk.price', 200);

// ['products' => ['desk' => ['price' => 200]]]

```

This function also accepts wildcards using asterisks and will set values on the target accordingly:
```


 1$data = [




 2    'products' => [




 3        ['name' => 'Desk 1', 'price' => 100],




 4        ['name' => 'Desk 2', 'price' => 150],




 5    ],




 6];




 7 



 8data_set($data, 'products.*.price', 200);




 9 



10/*




11    [




12        'products' => [




13            ['name' => 'Desk 1', 'price' => 200],




14            ['name' => 'Desk 2', 'price' => 200],




15        ],




16    ]




17*/




$data = [
    'products' => [
        ['name' => 'Desk 1', 'price' => 100],
        ['name' => 'Desk 2', 'price' => 150],
    ],
];

data_set($data, 'products.*.price', 200);

/*
    [
        'products' => [
            ['name' => 'Desk 1', 'price' => 200],
            ['name' => 'Desk 2', 'price' => 200],
        ],
    ]
*/

```

By default, any existing values are overwritten. If you wish to only set a value if it doesn't exist, you may pass `false` as the fourth argument to the function:
```


1$data = ['products' => ['desk' => ['price' => 100]]];




2 



3data_set($data, 'products.desk.price', 200, overwrite: false);




4 



5// ['products' => ['desk' => ['price' => 100]]]




$data = ['products' => ['desk' => ['price' => 100]]];

data_set($data, 'products.desk.price', 200, overwrite: false);

// ['products' => ['desk' => ['price' => 100]]]

```

#### [`data_forget()`](https://laravel.com/docs/12.x/helpers#method-data-forget)
The `data_forget` function removes a value within a nested array or object using "dot" notation:
```


1$data = ['products' => ['desk' => ['price' => 100]]];




2 



3data_forget($data, 'products.desk.price');




4 



5// ['products' => ['desk' => []]]




$data = ['products' => ['desk' => ['price' => 100]]];

data_forget($data, 'products.desk.price');

// ['products' => ['desk' => []]]

```

This function also accepts wildcards using asterisks and will remove values on the target accordingly:
```


 1$data = [
