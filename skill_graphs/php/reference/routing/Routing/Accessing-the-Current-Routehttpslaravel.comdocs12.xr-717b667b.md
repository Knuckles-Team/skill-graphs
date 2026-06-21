## [Accessing the Current Route](https://laravel.com/docs/12.x/routing#accessing-the-current-route)
You may use the `current`, `currentRouteName`, and `currentRouteAction` methods on the `Route` facade to access information about the route handling the incoming request:
```


1use Illuminate\Support\Facades\Route;




2 



3$route = Route::current(); // Illuminate\Routing\Route




4$name = Route::currentRouteName(); // string




5$action = Route::currentRouteAction(); // string




use Illuminate\Support\Facades\Route;

$route = Route::current(); // Illuminate\Routing\Route
$name = Route::currentRouteName(); // string
$action = Route::currentRouteAction(); // string

```

You may refer to the API documentation for both the [underlying class of the Route facade](https://api.laravel.com/docs/12.x/Illuminate/Routing/Router.html) and [Route instance](https://api.laravel.com/docs/12.x/Illuminate/Routing/Route.html) to review all of the methods that are available on the router and route classes.
