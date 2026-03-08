## [Arrays & Objects](https://laravel.com/docs/12.x/helpers#arrays)
#### [`Arr::accessible()`](https://laravel.com/docs/12.x/helpers#method-array-accessible)
The `Arr::accessible` method determines if the given value is array accessible:
```


 1use Illuminate\Support\Arr;




 2use Illuminate\Support\Collection;




 3 



 4$isAccessible = Arr::accessible(['a' => 1, 'b' => 2]);




 5 



 6// true




 7 



 8$isAccessible = Arr::accessible(new Collection);




 9 



10// true




11 



12$isAccessible = Arr::accessible('abc');




13 



14// false




15 



16$isAccessible = Arr::accessible(new stdClass);




17 



18// false




use Illuminate\Support\Arr;
use Illuminate\Support\Collection;

$isAccessible = Arr::accessible(['a' => 1, 'b' => 2]);

// true

$isAccessible = Arr::accessible(new Collection);

// true

$isAccessible = Arr::accessible('abc');

// false

$isAccessible = Arr::accessible(new stdClass);

// false

```

#### [`Arr::add()`](https://laravel.com/docs/12.x/helpers#method-array-add)
The `Arr::add` method adds a given key / value pair to an array if the given key doesn't already exist in the array or is set to `null`:
```


1use Illuminate\Support\Arr;




2 



3$array = Arr::add(['name' => 'Desk'], 'price', 100);




4 



5// ['name' => 'Desk', 'price' => 100]




6 



7$array = Arr::add(['name' => 'Desk', 'price' => null], 'price', 100);




8 



9// ['name' => 'Desk', 'price' => 100]




use Illuminate\Support\Arr;

$array = Arr::add(['name' => 'Desk'], 'price', 100);

// ['name' => 'Desk', 'price' => 100]

$array = Arr::add(['name' => 'Desk', 'price' => null], 'price', 100);

// ['name' => 'Desk', 'price' => 100]

```

#### [`Arr::array()`](https://laravel.com/docs/12.x/helpers#method-array-array)
The `Arr::array` method retrieves a value from a deeply nested array using "dot" notation (just as [Arr::get()](https://laravel.com/docs/12.x/helpers#method-array-get) does), but throws an `InvalidArgumentException` if the requested value is not an `array`:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['name' => 'Joe', 'languages' => ['PHP', 'Ruby']];




 4 



 5$value = Arr::array($array, 'languages');




 6 



 7// ['PHP', 'Ruby']




 8 



 9$value = Arr::array($array, 'name');




10 



11// throws InvalidArgumentException




use Illuminate\Support\Arr;

$array = ['name' => 'Joe', 'languages' => ['PHP', 'Ruby']];

$value = Arr::array($array, 'languages');

// ['PHP', 'Ruby']

$value = Arr::array($array, 'name');

// throws InvalidArgumentException

```

#### [`Arr::boolean()`](https://laravel.com/docs/12.x/helpers#method-array-boolean)
The `Arr::boolean` method retrieves a value from a deeply nested array using "dot" notation (just as [Arr::get()](https://laravel.com/docs/12.x/helpers#method-array-get) does), but throws an `InvalidArgumentException` if the requested value is not a `boolean`:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['name' => 'Joe', 'available' => true];




 4 



 5$value = Arr::boolean($array, 'available');




 6 



 7// true




 8 



 9$value = Arr::boolean($array, 'name');




10 



11// throws InvalidArgumentException




use Illuminate\Support\Arr;

$array = ['name' => 'Joe', 'available' => true];

$value = Arr::boolean($array, 'available');

// true

$value = Arr::boolean($array, 'name');

// throws InvalidArgumentException

```

#### [`Arr::collapse()`](https://laravel.com/docs/12.x/helpers#method-array-collapse)
The `Arr::collapse` method collapses an array of arrays or collections into a single array:
```


1use Illuminate\Support\Arr;




2 



3$array = Arr::collapse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);




4 



5// [1, 2, 3, 4, 5, 6, 7, 8, 9]




use Illuminate\Support\Arr;

$array = Arr::collapse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

// [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

#### [`Arr::crossJoin()`](https://laravel.com/docs/12.x/helpers#method-array-crossjoin)
The `Arr::crossJoin` method cross joins the given arrays, returning a Cartesian product with all possible permutations:
```


 1use Illuminate\Support\Arr;




 2 



 3$matrix = Arr::crossJoin([1, 2], ['a', 'b']);




 4 



 5/*




 6    [




 7        [1, 'a'],




 8        [1, 'b'],




 9        [2, 'a'],




10        [2, 'b'],




11    ]




12*/




13 



14$matrix = Arr::crossJoin([1, 2], ['a', 'b'], ['I', 'II']);




15 



16/*




17    [




18        [1, 'a', 'I'],




19        [1, 'a', 'II'],




20        [1, 'b', 'I'],




21        [1, 'b', 'II'],




22        [2, 'a', 'I'],




23        [2, 'a', 'II'],




24        [2, 'b', 'I'],




25        [2, 'b', 'II'],




26    ]




27*/




use Illuminate\Support\Arr;

$matrix = Arr::crossJoin([1, 2], ['a', 'b']);

/*
    [
        [1, 'a'],
        [1, 'b'],
        [2, 'a'],
        [2, 'b'],
    ]
*/

$matrix = Arr::crossJoin([1, 2], ['a', 'b'], ['I', 'II']);

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

#### [`Arr::divide()`](https://laravel.com/docs/12.x/helpers#method-array-divide)
The `Arr::divide` method returns two arrays: one containing the keys and the other containing the values of the given array:
```


1use Illuminate\Support\Arr;




2 



3[$keys, $values] = Arr::divide(['name' => 'Desk']);




4 



5// $keys: ['name']




6 



7// $values: ['Desk']




use Illuminate\Support\Arr;

[$keys, $values] = Arr::divide(['name' => 'Desk']);

// $keys: ['name']

// $values: ['Desk']

```

#### [`Arr::dot()`](https://laravel.com/docs/12.x/helpers#method-array-dot)
The `Arr::dot` method flattens a multi-dimensional array into a single level array that uses "dot" notation to indicate depth:
```


1use Illuminate\Support\Arr;




2 



3$array = ['products' => ['desk' => ['price' => 100]]];




4 



5$flattened = Arr::dot($array);




6 



7// ['products.desk.price' => 100]




use Illuminate\Support\Arr;

$array = ['products' => ['desk' => ['price' => 100]]];

$flattened = Arr::dot($array);

// ['products.desk.price' => 100]

```

#### [`Arr::every()`](https://laravel.com/docs/12.x/helpers#method-array-every)
The `Arr::every` method ensures that all values in the array pass a given truth test:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [1, 2, 3];




 4 



 5Arr::every($array, fn ($i) => $i > 0);




 6 



 7// true




 8 



 9Arr::every($array, fn ($i) => $i > 2);




10 



11// false




use Illuminate\Support\Arr;

$array = [1, 2, 3];

Arr::every($array, fn ($i) => $i > 0);

// true

Arr::every($array, fn ($i) => $i > 2);

// false

```

#### [`Arr::except()`](https://laravel.com/docs/12.x/helpers#method-array-except)
The `Arr::except` method removes the given key / value pairs from an array:
```


1use Illuminate\Support\Arr;




2 



3$array = ['name' => 'Desk', 'price' => 100];




4 



5$filtered = Arr::except($array, ['price']);




6 



7// ['name' => 'Desk']




use Illuminate\Support\Arr;

$array = ['name' => 'Desk', 'price' => 100];

$filtered = Arr::except($array, ['price']);

// ['name' => 'Desk']

```

#### [`Arr::exceptValues()`](https://laravel.com/docs/12.x/helpers#method-array-except-values)
The `Arr::exceptValues` method removes the specified values from an array:
```


1use Illuminate\Support\Arr;




2 



3$array = ['foo', 'bar', 'baz', 'qux'];




4 



5$filtered = Arr::exceptValues($array, ['foo', 'baz']);




6 



7// ['bar', 'qux']




use Illuminate\Support\Arr;

$array = ['foo', 'bar', 'baz', 'qux'];

$filtered = Arr::exceptValues($array, ['foo', 'baz']);

// ['bar', 'qux']

```

You may also pass `true` to the `strict` argument to use strict type comparisons when filtering:
```


1use Illuminate\Support\Arr;




2 



3$array = [1, '1', 2, '2'];




4 



5$filtered = Arr::exceptValues($array, [1, 2], strict: true);




6 



7// ['1', '2']




use Illuminate\Support\Arr;

$array = [1, '1', 2, '2'];

$filtered = Arr::exceptValues($array, [1, 2], strict: true);

// ['1', '2']

```

#### [`Arr::exists()`](https://laravel.com/docs/12.x/helpers#method-array-exists)
The `Arr::exists` method checks that the given key exists in the provided array:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['name' => 'John Doe', 'age' => 17];




 4 



 5$exists = Arr::exists($array, 'name');




 6 



 7// true




 8 



 9$exists = Arr::exists($array, 'salary');




10 



11// false




use Illuminate\Support\Arr;

$array = ['name' => 'John Doe', 'age' => 17];

$exists = Arr::exists($array, 'name');

// true

$exists = Arr::exists($array, 'salary');

// false

```

#### [`Arr::first()`](https://laravel.com/docs/12.x/helpers#method-array-first)
The `Arr::first` method returns the first element of an array passing a given truth test:
```


1use Illuminate\Support\Arr;




2 



3$array = [100, 200, 300];




4 



5$first = Arr::first($array, function (int $value, int $key) {




6    return $value >= 150;




7});




8 



9// 200




use Illuminate\Support\Arr;

$array = [100, 200, 300];

$first = Arr::first($array, function (int $value, int $key) {
    return $value >= 150;
});

// 200

```

A default value may also be passed as the third parameter to the method. This value will be returned if no value passes the truth test:
```


1use Illuminate\Support\Arr;




2 



3$first = Arr::first($array, $callback, $default);




use Illuminate\Support\Arr;

$first = Arr::first($array, $callback, $default);

```

#### [`Arr::flatten()`](https://laravel.com/docs/12.x/helpers#method-array-flatten)
The `Arr::flatten` method flattens a multi-dimensional array into a single level array:
```


1use Illuminate\Support\Arr;




2 



3$array = ['name' => 'Joe', 'languages' => ['PHP', 'Ruby']];




4 



5$flattened = Arr::flatten($array);




6 



7// ['Joe', 'PHP', 'Ruby']




use Illuminate\Support\Arr;

$array = ['name' => 'Joe', 'languages' => ['PHP', 'Ruby']];

$flattened = Arr::flatten($array);

// ['Joe', 'PHP', 'Ruby']

```

#### [`Arr::float()`](https://laravel.com/docs/12.x/helpers#method-array-float)
The `Arr::float` method retrieves a value from a deeply nested array using "dot" notation (just as [Arr::get()](https://laravel.com/docs/12.x/helpers#method-array-get) does), but throws an `InvalidArgumentException` if the requested value is not a `float`:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['name' => 'Joe', 'balance' => 123.45];




 4 



 5$value = Arr::float($array, 'balance');




 6 



 7// 123.45




 8 



 9$value = Arr::float($array, 'name');




10 



11// throws InvalidArgumentException




use Illuminate\Support\Arr;

$array = ['name' => 'Joe', 'balance' => 123.45];

$value = Arr::float($array, 'balance');

// 123.45

$value = Arr::float($array, 'name');

// throws InvalidArgumentException

```

#### [`Arr::forget()`](https://laravel.com/docs/12.x/helpers#method-array-forget)
The `Arr::forget` method removes a given key / value pairs from a deeply nested array using "dot" notation:
```


1use Illuminate\Support\Arr;




2 



3$array = ['products' => ['desk' => ['price' => 100]]];




4 



5Arr::forget($array, 'products.desk');




6 



7// ['products' => []]




use Illuminate\Support\Arr;

$array = ['products' => ['desk' => ['price' => 100]]];

Arr::forget($array, 'products.desk');

// ['products' => []]

```

#### [`Arr::from()`](https://laravel.com/docs/12.x/helpers#method-array-from)
The `Arr::from` method converts various input types into a plain PHP array. It supports a range of input types, including arrays, objects, and several common Laravel interfaces, such as `Arrayable`, `Enumerable`, `Jsonable`, and `JsonSerializable`. Additionally, it handles `Traversable` and `WeakMap` instances:
```


 1use Illuminate\Support\Arr;




 2 



 3Arr::from((object) ['foo' => 'bar']); // ['foo' => 'bar']




 4 



 5class TestJsonableObject implements Jsonable




 6{




 7    public function toJson($options = 0)




 8    {




 9        return json_encode(['foo' => 'bar']);




10    }




11}




12 



13Arr::from(new TestJsonableObject); // ['foo' => 'bar']




use Illuminate\Support\Arr;

Arr::from((object) ['foo' => 'bar']); // ['foo' => 'bar']

class TestJsonableObject implements Jsonable
{
    public function toJson($options = 0)
    {
        return json_encode(['foo' => 'bar']);
    }
}

Arr::from(new TestJsonableObject); // ['foo' => 'bar']

```

#### [`Arr::get()`](https://laravel.com/docs/12.x/helpers#method-array-get)
The `Arr::get` method retrieves a value from a deeply nested array using "dot" notation:
```


1use Illuminate\Support\Arr;




2 



3$array = ['products' => ['desk' => ['price' => 100]]];




4 



5$price = Arr::get($array, 'products.desk.price');




6 



7// 100




use Illuminate\Support\Arr;

$array = ['products' => ['desk' => ['price' => 100]]];

$price = Arr::get($array, 'products.desk.price');

// 100

```

The `Arr::get` method also accepts a default value, which will be returned if the specified key is not present in the array:
```


1use Illuminate\Support\Arr;




2 



3$discount = Arr::get($array, 'products.desk.discount', 0);




4 



5// 0




use Illuminate\Support\Arr;

$discount = Arr::get($array, 'products.desk.discount', 0);

// 0

```

#### [`Arr::has()`](https://laravel.com/docs/12.x/helpers#method-array-has)
The `Arr::has` method checks whether a given item or items exists in an array using "dot" notation:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['product' => ['name' => 'Desk', 'price' => 100]];




 4 



 5$contains = Arr::has($array, 'product.name');




 6 



 7// true




 8 



 9$contains = Arr::has($array, ['product.price', 'product.discount']);




10 



11// false




use Illuminate\Support\Arr;

$array = ['product' => ['name' => 'Desk', 'price' => 100]];

$contains = Arr::has($array, 'product.name');

// true

$contains = Arr::has($array, ['product.price', 'product.discount']);

// false

```

#### [`Arr::hasAll()`](https://laravel.com/docs/12.x/helpers#method-array-hasall)
The `Arr::hasAll` method determines if all of the specified keys exist in the given array using "dot" notation:
```


1use Illuminate\Support\Arr;




2 



3$array = ['name' => 'Taylor', 'language' => 'PHP'];




4 



5Arr::hasAll($array, ['name']); // true




6Arr::hasAll($array, ['name', 'language']); // true




7Arr::hasAll($array, ['name', 'IDE']); // false




use Illuminate\Support\Arr;

$array = ['name' => 'Taylor', 'language' => 'PHP'];

Arr::hasAll($array, ['name']); // true
Arr::hasAll($array, ['name', 'language']); // true
Arr::hasAll($array, ['name', 'IDE']); // false

```

#### [`Arr::hasAny()`](https://laravel.com/docs/12.x/helpers#method-array-hasany)
The `Arr::hasAny` method checks whether any item in a given set exists in an array using "dot" notation:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['product' => ['name' => 'Desk', 'price' => 100]];




 4 



 5$contains = Arr::hasAny($array, 'product.name');




 6 



 7// true




 8 



 9$contains = Arr::hasAny($array, ['product.name', 'product.discount']);




10 



11// true




12 



13$contains = Arr::hasAny($array, ['category', 'product.discount']);




14 



15// false




use Illuminate\Support\Arr;

$array = ['product' => ['name' => 'Desk', 'price' => 100]];

$contains = Arr::hasAny($array, 'product.name');

// true

$contains = Arr::hasAny($array, ['product.name', 'product.discount']);

// true

$contains = Arr::hasAny($array, ['category', 'product.discount']);

// false

```

#### [`Arr::integer()`](https://laravel.com/docs/12.x/helpers#method-array-integer)
The `Arr::integer` method retrieves a value from a deeply nested array using "dot" notation (just as [Arr::get()](https://laravel.com/docs/12.x/helpers#method-array-get) does), but throws an `InvalidArgumentException` if the requested value is not an `int`:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['name' => 'Joe', 'age' => 42];




 4 



 5$value = Arr::integer($array, 'age');




 6 



 7// 42




 8 



 9$value = Arr::integer($array, 'name');




10 



11// throws InvalidArgumentException




use Illuminate\Support\Arr;

$array = ['name' => 'Joe', 'age' => 42];

$value = Arr::integer($array, 'age');

// 42

$value = Arr::integer($array, 'name');

// throws InvalidArgumentException

```

#### [`Arr::isAssoc()`](https://laravel.com/docs/12.x/helpers#method-array-isassoc)
The `Arr::isAssoc` method returns `true` if the given array is an associative array. An array is considered "associative" if it doesn't have sequential numerical keys beginning with zero:
```


1use Illuminate\Support\Arr;




2 



3$isAssoc = Arr::isAssoc(['product' => ['name' => 'Desk', 'price' => 100]]);




4 



5// true




6 



7$isAssoc = Arr::isAssoc([1, 2, 3]);




8 



9// false




use Illuminate\Support\Arr;

$isAssoc = Arr::isAssoc(['product' => ['name' => 'Desk', 'price' => 100]]);

// true

$isAssoc = Arr::isAssoc([1, 2, 3]);

// false

```

#### [`Arr::isList()`](https://laravel.com/docs/12.x/helpers#method-array-islist)
The `Arr::isList` method returns `true` if the given array's keys are sequential integers beginning from zero:
```


1use Illuminate\Support\Arr;




2 



3$isList = Arr::isList(['foo', 'bar', 'baz']);




4 



5// true




6 



7$isList = Arr::isList(['product' => ['name' => 'Desk', 'price' => 100]]);




8 



9// false




use Illuminate\Support\Arr;

$isList = Arr::isList(['foo', 'bar', 'baz']);

// true

$isList = Arr::isList(['product' => ['name' => 'Desk', 'price' => 100]]);

// false

```

#### [`Arr::join()`](https://laravel.com/docs/12.x/helpers#method-array-join)
The `Arr::join` method joins array elements with a string. Using this method's third argument, you may also specify the joining string for the final element of the array:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = ['Tailwind', 'Alpine', 'Laravel', 'Livewire'];




 4 



 5$joined = Arr::join($array, ', ');




 6 



 7// Tailwind, Alpine, Laravel, Livewire




 8 



 9$joined = Arr::join($array, ', ', ', and ');




10 



11// Tailwind, Alpine, Laravel, and Livewire




use Illuminate\Support\Arr;

$array = ['Tailwind', 'Alpine', 'Laravel', 'Livewire'];

$joined = Arr::join($array, ', ');

// Tailwind, Alpine, Laravel, Livewire

$joined = Arr::join($array, ', ', ', and ');

// Tailwind, Alpine, Laravel, and Livewire

```

#### [`Arr::keyBy()`](https://laravel.com/docs/12.x/helpers#method-array-keyby)
The `Arr::keyBy` method keys the array by the given key. If multiple items have the same key, only the last one will appear in the new array:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    ['product_id' => 'prod-100', 'name' => 'Desk'],




 5    ['product_id' => 'prod-200', 'name' => 'Chair'],




 6];




 7 



 8$keyed = Arr::keyBy($array, 'product_id');




 9 



10/*




11    [




12        'prod-100' => ['product_id' => 'prod-100', 'name' => 'Desk'],




13        'prod-200' => ['product_id' => 'prod-200', 'name' => 'Chair'],




14    ]




15*/




use Illuminate\Support\Arr;

$array = [
    ['product_id' => 'prod-100', 'name' => 'Desk'],
    ['product_id' => 'prod-200', 'name' => 'Chair'],
];

$keyed = Arr::keyBy($array, 'product_id');

/*
    [
        'prod-100' => ['product_id' => 'prod-100', 'name' => 'Desk'],
        'prod-200' => ['product_id' => 'prod-200', 'name' => 'Chair'],
    ]
*/

```

#### [`Arr::last()`](https://laravel.com/docs/12.x/helpers#method-array-last)
The `Arr::last` method returns the last element of an array passing a given truth test:
```


1use Illuminate\Support\Arr;




2 



3$array = [100, 200, 300, 110];




4 



5$last = Arr::last($array, function (int $value, int $key) {




6    return $value >= 150;




7});




8 



9// 300




use Illuminate\Support\Arr;

$array = [100, 200, 300, 110];

$last = Arr::last($array, function (int $value, int $key) {
    return $value >= 150;
});

// 300

```

A default value may be passed as the third argument to the method. This value will be returned if no value passes the truth test:
```


1use Illuminate\Support\Arr;




2 



3$last = Arr::last($array, $callback, $default);




use Illuminate\Support\Arr;

$last = Arr::last($array, $callback, $default);

```

#### [`Arr::map()`](https://laravel.com/docs/12.x/helpers#method-array-map)
The `Arr::map` method iterates through the array and passes each value and key to the given callback. The array value is replaced by the value returned by the callback:
```


1use Illuminate\Support\Arr;




2 



3$array = ['first' => 'james', 'last' => 'kirk'];




4 



5$mapped = Arr::map($array, function (string $value, string $key) {




6    return ucfirst($value);




7});




8 



9// ['first' => 'James', 'last' => 'Kirk']




use Illuminate\Support\Arr;

$array = ['first' => 'james', 'last' => 'kirk'];

$mapped = Arr::map($array, function (string $value, string $key) {
    return ucfirst($value);
});

// ['first' => 'James', 'last' => 'Kirk']

```

#### [`Arr::mapSpread()`](https://laravel.com/docs/12.x/helpers#method-array-map-spread)
The `Arr::mapSpread` method iterates over the array, passing each nested item value into the given closure. The closure is free to modify the item and return it, thus forming a new array of modified items:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    [0, 1],




 5    [2, 3],




 6    [4, 5],




 7    [6, 7],




 8    [8, 9],




 9];




10 



11$mapped = Arr::mapSpread($array, function (int $even, int $odd) {




12    return $even + $odd;




13});




14 



15/*




16    [1, 5, 9, 13, 17]




17*/




use Illuminate\Support\Arr;

$array = [
    [0, 1],
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
];

$mapped = Arr::mapSpread($array, function (int $even, int $odd) {
    return $even + $odd;
});

/*
    [1, 5, 9, 13, 17]
*/

```

#### [`Arr::mapWithKeys()`](https://laravel.com/docs/12.x/helpers#method-array-map-with-keys)
The `Arr::mapWithKeys` method iterates through the array and passes each value to the given callback. The callback should return an associative array containing a single key / value pair:
```


 1use Illuminate\Support\Arr;




 2 



 3$array = [




 4    [




 5        'name' => 'John',




 6        'department' => 'Sales',




 7        'email' => 'john@example.com',




 8    ],




 9    [




10        'name' => 'Jane',




11        'department' => 'Marketing',




12        'email' => 'jane@example.com',




13    ]




14];




15 



16$mapped = Arr::mapWithKeys($array, function (array $item, int $key) {




17    return [$item['email'] => $item['name']];




18});




19 



20/*




21    [




22        'john@example.com' => 'John',




23        'jane@example.com' => 'Jane',




24    ]




25*/




use Illuminate\Support\Arr;

$array = [
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
];

$mapped = Arr::mapWithKeys($array, function (array $item, int $key) {
    return [$item['email'] => $item['name']];
});

/*
    [
        'john@example.com' => 'John',
        'jane@example.com' => 'Jane',
    ]
*/

```

#### [`Arr::only()`](https://laravel.com/docs/12.x/helpers#method-array-only)
The `Arr::only` method returns only the specified key / value pairs from the given array:
```


1use Illuminate\Support\Arr;




2 



3$array = ['name' => 'Desk', 'price' => 100, 'orders' => 10];




4 



5$slice = Arr::only($array, ['name', 'price']);




6 



7// ['name' => 'Desk', 'price' => 100]




use Illuminate\Support\Arr;

$array = ['name' => 'Desk', 'price' => 100, 'orders' => 10];

$slice = Arr::only($array, ['name', 'price']);

// ['name' => 'Desk', 'price' => 100]

```

#### [`Arr::onlyValues()`](https://laravel.com/docs/12.x/helpers#method-array-only-values)
The `Arr::onlyValues` method returns only the specified values from an array:
```


1use Illuminate\Support\Arr;




2 



3$array = ['foo', 'bar', 'baz', 'qux'];




4 



5$filtered = Arr::onlyValues($array, ['foo', 'baz']);




6 



7// ['foo', 'baz']




use Illuminate\Support\Arr;

$array = ['foo', 'bar', 'baz', 'qux'];

$filtered = Arr::onlyValues($array, ['foo', 'baz']);

// ['foo', 'baz']

```

You may also pass `true` to the `strict` argument to use strict type comparisons when filtering:
```


1use Illuminate\Support\Arr;




2 



3$array = [1, '1', 2, '2'];




4 



5$filtered = Arr::onlyValues($array, [1, 2], strict: true);




6 



7// [1, 2]




use Illuminate\Support\Arr;

$array = [1, '1', 2, '2'];

$filtered = Arr::onlyValues($array, [1, 2], strict: true);

// [1, 2]

```

#### [`Arr::partition()`](https://laravel.com/docs/12.x/helpers#method-array-partition)
The `Arr::partition` method may be combined with PHP array destructuring to separate elements that pass a given truth test from those that do not:
```


 1<?php




 2 



 3use Illuminate\Support\Arr;




 4 



 5$numbers = [1, 2, 3, 4, 5, 6];




 6 



 7[$underThree, $equalOrAboveThree] = Arr::partition($numbers, function (int $i) {




 8    return $i < 3;




 9});




10 



11dump($underThree);




12 



13// [1, 2]




14 



15dump($equalOrAboveThree);




16 



17// [3, 4, 5, 6]




<?php

use Illuminate\Support\Arr;
