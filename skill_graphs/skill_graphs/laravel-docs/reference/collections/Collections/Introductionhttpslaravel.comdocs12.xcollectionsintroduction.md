## [Introduction](https://laravel.com/docs/12.x/collections#introduction)
The `Illuminate\Support\Collection` class provides a fluent, convenient wrapper for working with arrays of data. For example, check out the following code. We'll use the `collect` helper to create a new collection instance from the array, run the `strtoupper` function on each element, and then remove all empty elements:
```


1$collection = collect(['Taylor', 'Abigail', null])->map(function (?string $name) {




2    return strtoupper($name);




3})->reject(function (string $name) {




4    return empty($name);




5});




$collection = collect(['Taylor', 'Abigail', null])->map(function (?string $name) {
    return strtoupper($name);
})->reject(function (string $name) {
    return empty($name);
});

```

As you can see, the `Collection` class allows you to chain its methods to perform fluent mapping and reducing of the underlying array. In general, collections are immutable, meaning every `Collection` method returns an entirely new `Collection` instance.
### [Creating Collections](https://laravel.com/docs/12.x/collections#creating-collections)
As mentioned above, the `collect` helper returns a new `Illuminate\Support\Collection` instance for the given array. So, creating a collection is as simple as:
```


1$collection = collect([1, 2, 3]);




$collection = collect([1, 2, 3]);

```

You may also create a collection using the [make](https://laravel.com/docs/12.x/collections#method-make) and [fromJson](https://laravel.com/docs/12.x/collections#method-fromjson) methods.
The results of [Eloquent](https://laravel.com/docs/12.x/eloquent) queries are always returned as `Collection` instances.
### [Extending Collections](https://laravel.com/docs/12.x/collections#extending-collections)
Collections are "macroable", which allows you to add additional methods to the `Collection` class at run time. The `Illuminate\Support\Collection` class' `macro` method accepts a closure that will be executed when your macro is called. The macro closure may access the collection's other methods via `$this`, just as if it were a real method of the collection class. For example, the following code adds a `toUpper` method to the `Collection` class:
```


 1use Illuminate\Support\Collection;




 2use Illuminate\Support\Str;




 3 



 4Collection::macro('toUpper', function () {




 5    return $this->map(function (string $value) {




 6        return Str::upper($value);




 7    });




 8});




 9 



10$collection = collect(['first', 'second']);




11 



12$upper = $collection->toUpper();




13 



14// ['FIRST', 'SECOND']




use Illuminate\Support\Collection;
use Illuminate\Support\Str;

Collection::macro('toUpper', function () {
    return $this->map(function (string $value) {
        return Str::upper($value);
    });
});

$collection = collect(['first', 'second']);

$upper = $collection->toUpper();

// ['FIRST', 'SECOND']

```

Typically, you should declare collection macros in the `boot` method of a [service provider](https://laravel.com/docs/12.x/providers).
#### [Macro Arguments](https://laravel.com/docs/12.x/collections#macro-arguments)
If necessary, you may define macros that accept additional arguments:
```


 1use Illuminate\Support\Collection;




 2use Illuminate\Support\Facades\Lang;




 3 



 4Collection::macro('toLocale', function (string $locale) {




 5    return $this->map(function (string $value) use ($locale) {




 6        return Lang::get($value, [], $locale);




 7    });




 8});




 9 



10$collection = collect(['first', 'second']);




11 



12$translated = $collection->toLocale('es');




13 



14// ['primero', 'segundo'];




use Illuminate\Support\Collection;
use Illuminate\Support\Facades\Lang;

Collection::macro('toLocale', function (string $locale) {
    return $this->map(function (string $value) use ($locale) {
        return Lang::get($value, [], $locale);
    });
});

$collection = collect(['first', 'second']);

$translated = $collection->toLocale('es');

// ['primero', 'segundo'];

```
