## [HTTP Basic Authentication](https://laravel.com/docs/12.x/authentication#http-basic-authentication)
`auth.basic` [middleware](https://laravel.com/docs/12.x/middleware) to a route. The `auth.basic` middleware is included with the Laravel framework, so you do not need to define it:
```


1Route::get('/profile', function () {




2    // Only authenticated users may access this route...




3})->middleware('auth.basic');




Route::get('/profile', function () {
    // Only authenticated users may access this route...
})->middleware('auth.basic');

```

Once the middleware has been attached to the route, you will automatically be prompted for credentials when accessing the route in your browser. By default, the `auth.basic` middleware will assume the `email` column on your `users` database table is the user's "username".
#### [A Note on FastCGI](https://laravel.com/docs/12.x/authentication#a-note-on-fastcgi)
If you are using `.htaccess` file:
```


1RewriteCond %{HTTP:Authorization} ^(.+)$




2RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]




RewriteCond %{HTTP:Authorization} ^(.+)$
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]

```

### [Stateless HTTP Basic Authentication](https://laravel.com/docs/12.x/authentication#stateless-http-basic-authentication)
You may also use HTTP Basic Authentication without setting a user identifier cookie in the session. This is primarily helpful if you choose to use HTTP Authentication to authenticate requests to your application's API. To accomplish this, [define a middleware](https://laravel.com/docs/12.x/middleware) that calls the `onceBasic` method. If no response is returned by the `onceBasic` method, the request may be passed further into the application:
```


 1<?php




 2 



 3namespace App\Http\Middleware;




 4 



 5use Closure;




 6use Illuminate\Http\Request;




 7use Illuminate\Support\Facades\Auth;




 8use Symfony\Component\HttpFoundation\Response;




 9 



10class AuthenticateOnceWithBasicAuth




11{




12    /**




13     * Handle an incoming request.




14     *




15     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next




16     */




17    public function handle(Request $request, Closure $next): Response




18    {




19        return Auth::onceBasic() ?: $next($request);




20    }




21 



22}




<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Symfony\Component\HttpFoundation\Response;

class AuthenticateOnceWithBasicAuth
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        return Auth::onceBasic() ?: $next($request);
    }

}

```

Next, attach the middleware to a route:
```


1Route::get('/api/user', function () {




2    // Only authenticated users may access this route...




3})->middleware(AuthenticateOnceWithBasicAuth::class);




Route::get('/api/user', function () {
    // Only authenticated users may access this route...
})->middleware(AuthenticateOnceWithBasicAuth::class);

```
