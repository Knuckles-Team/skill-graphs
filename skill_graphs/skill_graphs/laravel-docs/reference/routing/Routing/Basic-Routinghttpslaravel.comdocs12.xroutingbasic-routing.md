## [Basic Routing](https://laravel.com/docs/12.x/routing#basic-routing)
The most basic Laravel routes accept a URI and a closure, providing a very simple and expressive method of defining routes and behavior without complicated routing configuration files:
```


1use Illuminate\Support\Facades\Route;




2 



3Route::get('/greeting', function () {




4    return 'Hello World';




5});




use Illuminate\Support\Facades\Route;

Route::get('/greeting', function () {
    return 'Hello World';
});

```

### [The Default Route Files](https://laravel.com/docs/12.x/routing#the-default-route-files)
All Laravel routes are defined in your route files, which are located in the `routes` directory. These files are automatically loaded by Laravel using the configuration specified in your application's `bootstrap/app.php` file. The `routes/web.php` file defines routes that are for your web interface. These routes are assigned the `web` [middleware group](https://laravel.com/docs/12.x/middleware#laravels-default-middleware-groups), which provides features like session state and CSRF protection.
For most applications, you will begin by defining routes in your `routes/web.php` file. The routes defined in `routes/web.php` may be accessed by entering the defined route's URL in your browser. For example, you may access the following route by navigating to `http://example.com/user` in your browser:
```


1use App\Http\Controllers\UserController;




2 



3Route::get('/user', [UserController::class, 'index']);




use App\Http\Controllers\UserController;

Route::get('/user', [UserController::class, 'index']);

```

#### [API Routes](https://laravel.com/docs/12.x/routing#api-routes)
If your application will also offer a stateless API, you may enable API routing using the `install:api` Artisan command:
```


1php artisan install:api




php artisan install:api

```

The `install:api` command installs [Laravel Sanctum](https://laravel.com/docs/12.x/sanctum), which provides a robust, yet simple API token authentication guard which can be used to authenticate third-party API consumers, SPAs, or mobile applications. In addition, the `install:api` command creates the `routes/api.php` file:
```


1Route::get('/user', function (Request $request) {




2    return $request->user();




3})->middleware('auth:sanctum');




Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

```

Of course, you are free to omit the `auth:sanctum` middleware on routes that should be publicly accessible.
The routes in `routes/api.php` are stateless and are assigned to the `api` [middleware group](https://laravel.com/docs/12.x/middleware#laravels-default-middleware-groups). Additionally, the `/api` URI prefix is automatically applied to these routes, so you do not need to manually apply it to every route in the file. You may change the prefix by modifying your application's `bootstrap/app.php` file:
```


1->withRouting(




2    api: __DIR__.'/../routes/api.php',




3    apiPrefix: 'api/admin',




4    // ...




5)




->withRouting(
    api: __DIR__.'/../routes/api.php',
    apiPrefix: 'api/admin',
    // ...
)

```

#### [Available Router Methods](https://laravel.com/docs/12.x/routing#available-router-methods)
The router allows you to register routes that respond to any HTTP verb:
```


1Route::get($uri, $callback);




2Route::post($uri, $callback);




3Route::put($uri, $callback);




4Route::patch($uri, $callback);




5Route::delete($uri, $callback);




6Route::options($uri, $callback);




Route::get($uri, $callback);
Route::post($uri, $callback);
Route::put($uri, $callback);
Route::patch($uri, $callback);
Route::delete($uri, $callback);
Route::options($uri, $callback);

```

Sometimes you may need to register a route that responds to multiple HTTP verbs. You may do so using the `match` method. Or, you may even register a route that responds to all HTTP verbs using the `any` method:
```


1Route::match(['get', 'post'], '/', function () {




2    // ...




3});




4 



5Route::any('/', function () {




6    // ...




7});




Route::match(['get', 'post'], '/', function () {
    // ...
});

Route::any('/', function () {
    // ...
});

```

When defining multiple routes that share the same URI, routes using the `get`, `post`, `put`, `patch`, `delete`, and `options` methods should be defined before routes using the `any`, `match`, and `redirect` methods. This ensures the incoming request is matched with the correct route.
#### [Dependency Injection](https://laravel.com/docs/12.x/routing#dependency-injection)
You may type-hint any dependencies required by your route in your route's callback signature. The declared dependencies will automatically be resolved and injected into the callback by the Laravel [service container](https://laravel.com/docs/12.x/container). For example, you may type-hint the `Illuminate\Http\Request` class to have the current HTTP request automatically injected into your route callback:
```


1use Illuminate\Http\Request;




2 



3Route::get('/users', function (Request $request) {




4    // ...




5});




use Illuminate\Http\Request;

Route::get('/users', function (Request $request) {
    // ...
});

```

#### [CSRF Protection](https://laravel.com/docs/12.x/routing#csrf-protection)
Remember, any HTML forms pointing to `POST`, `PUT`, `PATCH`, or `DELETE` routes that are defined in the `web` routes file should include a CSRF token field. Otherwise, the request will be rejected. You can read more about CSRF protection in the [CSRF documentation](https://laravel.com/docs/12.x/csrf):
```


1<form method="POST" action="/profile">




2    @csrf




3    ...




4</form>




<form method="POST" action="/profile">
    @csrf
    ...
</form>

```

### [Redirect Routes](https://laravel.com/docs/12.x/routing#redirect-routes)
If you are defining a route that redirects to another URI, you may use the `Route::redirect` method. This method provides a convenient shortcut so that you do not have to define a full route or controller for performing a simple redirect:
```


1Route::redirect('/here', '/there');




Route::redirect('/here', '/there');

```

By default, `Route::redirect` returns a `302` status code. You may customize the status code using the optional third parameter:
```


1Route::redirect('/here', '/there', 301);




Route::redirect('/here', '/there', 301);

```

Or, you may use the `Route::permanentRedirect` method to return a `301` status code:
```


1Route::permanentRedirect('/here', '/there');




Route::permanentRedirect('/here', '/there');

```

When using route parameters in redirect routes, the following parameters are reserved by Laravel and cannot be used: `destination` and `status`.
### [View Routes](https://laravel.com/docs/12.x/routing#view-routes)
If your route only needs to return a [view](https://laravel.com/docs/12.x/views), you may use the `Route::view` method. Like the `redirect` method, this method provides a simple shortcut so that you do not have to define a full route or controller. The `view` method accepts a URI as its first argument and a view name as its second argument. In addition, you may provide an array of data to pass to the view as an optional third argument:
```


1Route::view('/welcome', 'welcome');




2 



3Route::view('/welcome', 'welcome', ['name' => 'Taylor']);




Route::view('/welcome', 'welcome');

Route::view('/welcome', 'welcome', ['name' => 'Taylor']);

```

When using route parameters in view routes, the following parameters are reserved by Laravel and cannot be used: `view`, `data`, `status`, and `headers`.
### [Listing Your Routes](https://laravel.com/docs/12.x/routing#listing-your-routes)
The `route:list` Artisan command can easily provide an overview of all of the routes that are defined by your application:
```


1php artisan route:list




php artisan route:list

```

By default, the route middleware that are assigned to each route will not be displayed in the `route:list` output; however, you can instruct Laravel to display the route middleware and middleware group names by adding the `-v` option to the command:
```


1php artisan route:list -v




2 



3# Expand middleware groups...




4php artisan route:list -vv




php artisan route:list -v

# Expand middleware groups...
php artisan route:list -vv

```

You may also instruct Laravel to only show routes that begin with a given URI:
```


1php artisan route:list --path=api




php artisan route:list --path=api

```

In addition, you may instruct Laravel to hide any routes that are defined by third-party packages by providing the `--except-vendor` option when executing the `route:list` command:
```


1php artisan route:list --except-vendor




php artisan route:list --except-vendor

```

Likewise, you may also instruct Laravel to only show routes that are defined by third-party packages by providing the `--only-vendor` option when executing the `route:list` command:
```


1php artisan route:list --only-vendor




php artisan route:list --only-vendor

```

### [Routing Customization](https://laravel.com/docs/12.x/routing#routing-customization)
By default, your application's routes are configured and loaded by the `bootstrap/app.php` file:
```


 1<?php




 2 



 3use Illuminate\Foundation\Application;




 4 



 5return Application::configure(basePath: dirname(__DIR__))




 6    ->withRouting(




 7        web: __DIR__.'/../routes/web.php',




 8        commands: __DIR__.'/../routes/console.php',




 9        health: '/up',




10    )->create();




<?php

use Illuminate\Foundation\Application;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        commands: __DIR__.'/../routes/console.php',
        health: '/up',
    )->create();

```

However, sometimes you may want to define an entirely new file to contain a subset of your application's routes. To accomplish this, you may provide a `then` closure to the `withRouting` method. Within this closure, you may register any additional routes that are necessary for your application:
```


 1use Illuminate\Support\Facades\Route;




 2 



 3->withRouting(




 4    web: __DIR__.'/../routes/web.php',




 5    commands: __DIR__.'/../routes/console.php',




 6    health: '/up',




 7    then: function () {




 8        Route::middleware('api')




 9            ->prefix('webhooks')




10            ->name('webhooks.')




11            ->group(base_path('routes/webhooks.php'));




12    },




13)




use Illuminate\Support\Facades\Route;

->withRouting(
    web: __DIR__.'/../routes/web.php',
    commands: __DIR__.'/../routes/console.php',
    health: '/up',
    then: function () {
        Route::middleware('api')
            ->prefix('webhooks')
            ->name('webhooks.')
            ->group(base_path('routes/webhooks.php'));
    },
)

```

Or, you may even take complete control over route registration by providing a `using` closure to the `withRouting` method. When this argument is passed, no HTTP routes will be registered by the framework and you are responsible for manually registering all routes:
```


 1use Illuminate\Support\Facades\Route;




 2 



 3->withRouting(




 4    commands: __DIR__.'/../routes/console.php',




 5    using: function () {




 6        Route::middleware('api')




 7            ->prefix('api')




 8            ->group(base_path('routes/api.php'));




 9 



10        Route::middleware('web')




11            ->group(base_path('routes/web.php'));




12    },




13)




use Illuminate\Support\Facades\Route;

->withRouting(
    commands: __DIR__.'/../routes/console.php',
    using: function () {
        Route::middleware('api')
            ->prefix('api')
            ->group(base_path('routes/api.php'));

        Route::middleware('web')
            ->group(base_path('routes/web.php'));
    },
)

```
