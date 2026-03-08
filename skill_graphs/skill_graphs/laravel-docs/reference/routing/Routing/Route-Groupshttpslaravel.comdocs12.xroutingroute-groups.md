## [Route Groups](https://laravel.com/docs/12.x/routing#route-groups)
Route groups allow you to share route attributes, such as middleware, across a large number of routes without needing to define those attributes on each individual route.
Nested groups attempt to intelligently "merge" attributes with their parent group. Middleware and `where` conditions are merged while names and prefixes are appended. Namespace delimiters and slashes in URI prefixes are automatically added where appropriate.
### [Middleware](https://laravel.com/docs/12.x/routing#route-group-middleware)
To assign [middleware](https://laravel.com/docs/12.x/middleware) to all routes within a group, you may use the `middleware` method before defining the group. Middleware are executed in the order they are listed in the array:
```


1Route::middleware(['first', 'second'])->group(function () {




2    Route::get('/', function () {




3        // Uses first & second middleware...




4    });




5 



6    Route::get('/user/profile', function () {




7        // Uses first & second middleware...




8    });




9});




Route::middleware(['first', 'second'])->group(function () {
    Route::get('/', function () {
        // Uses first & second middleware...
    });

    Route::get('/user/profile', function () {
        // Uses first & second middleware...
    });
});

```

### [Controllers](https://laravel.com/docs/12.x/routing#route-group-controllers)
If a group of routes all utilize the same [controller](https://laravel.com/docs/12.x/controllers), you may use the `controller` method to define the common controller for all of the routes within the group. Then, when defining the routes, you only need to provide the controller method that they invoke:
```


1use App\Http\Controllers\OrderController;




2 



3Route::controller(OrderController::class)->group(function () {




4    Route::get('/orders/{id}', 'show');




5    Route::post('/orders', 'store');




6});




use App\Http\Controllers\OrderController;

Route::controller(OrderController::class)->group(function () {
    Route::get('/orders/{id}', 'show');
    Route::post('/orders', 'store');
});

```

### [Subdomain Routing](https://laravel.com/docs/12.x/routing#route-group-subdomain-routing)
Route groups may also be used to handle subdomain routing. Subdomains may be assigned route parameters just like route URIs, allowing you to capture a portion of the subdomain for usage in your route or controller. The subdomain may be specified by calling the `domain` method before defining the group:
```


1Route::domain('{account}.example.com')->group(function () {




2    Route::get('/user/{id}', function (string $account, string $id) {




3        // ...




4    });




5});




Route::domain('{account}.example.com')->group(function () {
    Route::get('/user/{id}', function (string $account, string $id) {
        // ...
    });
});

```

In order to ensure your subdomain routes are reachable, you should register subdomain routes before registering root domain routes. This will prevent root domain routes from overwriting subdomain routes which have the same URI path.
### [Route Prefixes](https://laravel.com/docs/12.x/routing#route-group-prefixes)
The `prefix` method may be used to prefix each route in the group with a given URI. For example, you may want to prefix all route URIs within the group with `admin`:
```


1Route::prefix('admin')->group(function () {




2    Route::get('/users', function () {




3        // Matches The "/admin/users" URL




4    });




5});




Route::prefix('admin')->group(function () {
    Route::get('/users', function () {
        // Matches The "/admin/users" URL
    });
});

```

### [Route Name Prefixes](https://laravel.com/docs/12.x/routing#route-group-name-prefixes)
The `name` method may be used to prefix each route name in the group with a given string. For example, you may want to prefix the names of all of the routes in the group with `admin`. The given string is prefixed to the route name exactly as it is specified, so we will be sure to provide the trailing `.` character in the prefix:
```


1Route::name('admin.')->group(function () {




2    Route::get('/users', function () {




3        // Route assigned name "admin.users"...




4    })->name('users');




5});




Route::name('admin.')->group(function () {
    Route::get('/users', function () {
        // Route assigned name "admin.users"...
    })->name('users');
});

```
