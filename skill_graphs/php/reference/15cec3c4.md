## [Route Parameters](https://laravel.com/docs/12.x/routing#route-parameters)
### [Required Parameters](https://laravel.com/docs/12.x/routing#required-parameters)
Sometimes you will need to capture segments of the URI within your route. For example, you may need to capture a user's ID from the URL. You may do so by defining route parameters:
```


1Route::get('/user/{id}', function (string $id) {




2    return 'User '.$id;




3});




Route::get('/user/{id}', function (string $id) {
    return 'User '.$id;
});

```

You may define as many route parameters as required by your route:
```


1Route::get('/posts/{post}/comments/{comment}', function (string $postId, string $commentId) {




2    // ...




3});




Route::get('/posts/{post}/comments/{comment}', function (string $postId, string $commentId) {
    // ...
});

```

Route parameters are always encased within `{}` braces and should consist of alphabetic characters. Underscores (`_`) are also acceptable within route parameter names. Route parameters are injected into route callbacks / controllers based on their order - the names of the route callback / controller arguments do not matter.
#### [Parameters and Dependency Injection](https://laravel.com/docs/12.x/routing#parameters-and-dependency-injection)
If your route has dependencies that you would like the Laravel service container to automatically inject into your route's callback, you should list your route parameters after your dependencies:
```


1use Illuminate\Http\Request;




2 



3Route::get('/user/{id}', function (Request $request, string $id) {




4    return 'User '.$id;




5});




use Illuminate\Http\Request;

Route::get('/user/{id}', function (Request $request, string $id) {
    return 'User '.$id;
});

```

### [Optional Parameters](https://laravel.com/docs/12.x/routing#parameters-optional-parameters)
Occasionally you may need to specify a route parameter that may not always be present in the URI. You may do so by placing a `?` mark after the parameter name. Make sure to give the route's corresponding variable a default value:
```


1Route::get('/user/{name?}', function (?string $name = null) {




2    return $name;




3});




4 



5Route::get('/user/{name?}', function (?string $name = 'John') {




6    return $name;




7});




Route::get('/user/{name?}', function (?string $name = null) {
    return $name;
});

Route::get('/user/{name?}', function (?string $name = 'John') {
    return $name;
});

```

### [Regular Expression Constraints](https://laravel.com/docs/12.x/routing#parameters-regular-expression-constraints)
You may constrain the format of your route parameters using the `where` method on a route instance. The `where` method accepts the name of the parameter and a regular expression defining how the parameter should be constrained:
```


 1Route::get('/user/{name}', function (string $name) {




 2    // ...




 3})->where('name', '[A-Za-z]+');




 4 



 5Route::get('/user/{id}', function (string $id) {




 6    // ...




 7})->where('id', '[0-9]+');




 8 



 9Route::get('/user/{id}/{name}', function (string $id, string $name) {




10    // ...




11})->where(['id' => '[0-9]+', 'name' => '[a-z]+']);




Route::get('/user/{name}', function (string $name) {
    // ...
})->where('name', '[A-Za-z]+');

Route::get('/user/{id}', function (string $id) {
    // ...
})->where('id', '[0-9]+');

Route::get('/user/{id}/{name}', function (string $id, string $name) {
    // ...
})->where(['id' => '[0-9]+', 'name' => '[a-z]+']);

```

For convenience, some commonly used regular expression patterns have helper methods that allow you to quickly add pattern constraints to your routes:
```


 1Route::get('/user/{id}/{name}', function (string $id, string $name) {




 2    // ...




 3})->whereNumber('id')->whereAlpha('name');




 4 



 5Route::get('/user/{name}', function (string $name) {




 6    // ...




 7})->whereAlphaNumeric('name');




 8 



 9Route::get('/user/{id}', function (string $id) {




10    // ...




11})->whereUuid('id');




12 



13Route::get('/user/{id}', function (string $id) {




14    // ...




15})->whereUlid('id');




16 



17Route::get('/category/{category}', function (string $category) {




18    // ...




19})->whereIn('category', ['movie', 'song', 'painting']);




20 



21Route::get('/category/{category}', function (string $category) {




22    // ...




23})->whereIn('category', CategoryEnum::cases());




Route::get('/user/{id}/{name}', function (string $id, string $name) {
    // ...
})->whereNumber('id')->whereAlpha('name');

Route::get('/user/{name}', function (string $name) {
    // ...
})->whereAlphaNumeric('name');

Route::get('/user/{id}', function (string $id) {
    // ...
})->whereUuid('id');

Route::get('/user/{id}', function (string $id) {
    // ...
})->whereUlid('id');

Route::get('/category/{category}', function (string $category) {
    // ...
})->whereIn('category', ['movie', 'song', 'painting']);

Route::get('/category/{category}', function (string $category) {
    // ...
})->whereIn('category', CategoryEnum::cases());

```

If the incoming request does not match the route pattern constraints, a 404 HTTP response will be returned.
#### [Global Constraints](https://laravel.com/docs/12.x/routing#parameters-global-constraints)
If you would like a route parameter to always be constrained by a given regular expression, you may use the `pattern` method. You should define these patterns in the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


1use Illuminate\Support\Facades\Route;




2 



3/**




4 * Bootstrap any application services.




5 */




6public function boot(): void




7{




8    Route::pattern('id', '[0-9]+');




9}




use Illuminate\Support\Facades\Route;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Route::pattern('id', '[0-9]+');
}

```

Once the pattern has been defined, it is automatically applied to all routes using that parameter name:
```


1Route::get('/user/{id}', function (string $id) {




2    // Only executed if {id} is numeric...




3});




Route::get('/user/{id}', function (string $id) {
    // Only executed if {id} is numeric...
});

```

#### [Encoded Forward Slashes](https://laravel.com/docs/12.x/routing#parameters-encoded-forward-slashes)
The Laravel routing component allows all characters except `/` to be present within route parameter values. You must explicitly allow `/` to be part of your placeholder using a `where` condition regular expression:
```


1Route::get('/search/{search}', function (string $search) {




2    return $search;




3})->where('search', '.*');




Route::get('/search/{search}', function (string $search) {
    return $search;
})->where('search', '.*');

```

Encoded forward slashes are only supported within the last route segment.
