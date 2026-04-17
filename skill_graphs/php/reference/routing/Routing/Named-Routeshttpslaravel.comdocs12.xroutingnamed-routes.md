## [Named Routes](https://laravel.com/docs/12.x/routing#named-routes)
Named routes allow the convenient generation of URLs or redirects for specific routes. You may specify a name for a route by chaining the `name` method onto the route definition:
```


1Route::get('/user/profile', function () {




2    // ...




3})->name('profile');




Route::get('/user/profile', function () {
    // ...
})->name('profile');

```

You may also specify route names for controller actions:
```


1Route::get(




2    '/user/profile',




3    [UserProfileController::class, 'show']




4)->name('profile');




Route::get(
    '/user/profile',
    [UserProfileController::class, 'show']
)->name('profile');

```

Route names should always be unique.
#### [Generating URLs to Named Routes](https://laravel.com/docs/12.x/routing#generating-urls-to-named-routes)
Once you have assigned a name to a given route, you may use the route's name when generating URLs or redirects via Laravel's `route` and `redirect` helper functions:
```


1// Generating URLs...




2$url = route('profile');




3 



4// Generating Redirects...




5return redirect()->route('profile');




6 



7return to_route('profile');




// Generating URLs...
$url = route('profile');

// Generating Redirects...
return redirect()->route('profile');

return to_route('profile');

```

If the named route defines parameters, you may pass the parameters as the second argument to the `route` function. The given parameters will automatically be inserted into the generated URL in their correct positions:
```


1Route::get('/user/{id}/profile', function (string $id) {




2    // ...




3})->name('profile');




4 



5$url = route('profile', ['id' => 1]);




Route::get('/user/{id}/profile', function (string $id) {
    // ...
})->name('profile');

$url = route('profile', ['id' => 1]);

```

If you pass additional parameters in the array, those key / value pairs will automatically be added to the generated URL's query string:
```


1Route::get('/user/{id}/profile', function (string $id) {




2    // ...




3})->name('profile');




4 



5$url = route('profile', ['id' => 1, 'photos' => 'yes']);




6 



7// http://example.com/user/1/profile?photos=yes




Route::get('/user/{id}/profile', function (string $id) {
    // ...
})->name('profile');

$url = route('profile', ['id' => 1, 'photos' => 'yes']);

// http://example.com/user/1/profile?photos=yes

```

Sometimes, you may wish to specify request-wide default values for URL parameters, such as the current locale. To accomplish this, you may use the [URL::defaults method](https://laravel.com/docs/12.x/urls#default-values).
#### [Inspecting the Current Route](https://laravel.com/docs/12.x/routing#inspecting-the-current-route)
If you would like to determine if the current request was routed to a given named route, you may use the `named` method on a Route instance. For example, you may check the current route name from a route middleware:
```


 1use Closure;




 2use Illuminate\Http\Request;




 3use Symfony\Component\HttpFoundation\Response;




 4 



 5/**




 6 * Handle an incoming request.




 7 *




 8 * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next




 9 */




10public function handle(Request $request, Closure $next): Response




11{




12    if ($request->route()->named('profile')) {




13        // ...




14    }




15 



16    return $next($request);




17}




use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

/**
 * Handle an incoming request.
 *
 * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
 */
public function handle(Request $request, Closure $next): Response
{
    if ($request->route()->named('profile')) {
        // ...
    }

    return $next($request);
}

```
