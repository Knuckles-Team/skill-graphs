## [URLs](https://laravel.com/docs/12.x/helpers#urls)
#### [`action()`](https://laravel.com/docs/12.x/helpers#method-action)
The `action` function generates a URL for the given controller action:
```


1use App\Http\Controllers\HomeController;




2 



3$url = action([HomeController::class, 'index']);




use App\Http\Controllers\HomeController;

$url = action([HomeController::class, 'index']);

```

If the method accepts route parameters, you may pass them as the second argument to the method:
```


1$url = action([UserController::class, 'profile'], ['id' => 1]);




$url = action([UserController::class, 'profile'], ['id' => 1]);

```

#### [`asset()`](https://laravel.com/docs/12.x/helpers#method-asset)
The `asset` function generates a URL for an asset using the current scheme of the request (HTTP or HTTPS):
```


1$url = asset('img/photo.jpg');




$url = asset('img/photo.jpg');

```

You can configure the asset URL host by setting the `ASSET_URL` variable in your `.env` file. This can be useful if you host your assets on an external service like Amazon S3 or another CDN:
```


1// ASSET_URL=http://example.com/assets




2 



3$url = asset('img/photo.jpg'); // http://example.com/assets/img/photo.jpg




// ASSET_URL=http://example.com/assets

$url = asset('img/photo.jpg'); // http://example.com/assets/img/photo.jpg

```

#### [`route()`](https://laravel.com/docs/12.x/helpers#method-route)
The `route` function generates a URL for a given [named route](https://laravel.com/docs/12.x/routing#named-routes):
```


1$url = route('route.name');




$url = route('route.name');

```

If the route accepts parameters, you may pass them as the second argument to the function:
```


1$url = route('route.name', ['id' => 1]);




$url = route('route.name', ['id' => 1]);

```

By default, the `route` function generates an absolute URL. If you wish to generate a relative URL, you may pass `false` as the third argument to the function:
```


1$url = route('route.name', ['id' => 1], false);




$url = route('route.name', ['id' => 1], false);

```

#### [`secure_asset()`](https://laravel.com/docs/12.x/helpers#method-secure-asset)
The `secure_asset` function generates a URL for an asset using HTTPS:
```


1$url = secure_asset('img/photo.jpg');




$url = secure_asset('img/photo.jpg');

```

#### [`secure_url()`](https://laravel.com/docs/12.x/helpers#method-secure-url)
The `secure_url` function generates a fully qualified HTTPS URL to the given path. Additional URL segments may be passed in the function's second argument:
```


1$url = secure_url('user/profile');




2 



3$url = secure_url('user/profile', [1]);




$url = secure_url('user/profile');

$url = secure_url('user/profile', [1]);

```

#### [`to_action()`](https://laravel.com/docs/12.x/helpers#method-to-action)
The `to_action` function generates a [redirect HTTP response](https://laravel.com/docs/12.x/responses#redirects) for a given controller action:
```


1use App\Http\Controllers\UserController;




2 



3return to_action([UserController::class, 'show'], ['user' => 1]);




use App\Http\Controllers\UserController;

return to_action([UserController::class, 'show'], ['user' => 1]);

```

If necessary, you may pass the HTTP status code that should be assigned to the redirect and any additional response headers as the third and fourth arguments to the `to_action` method:
```


1return to_action(




2    [UserController::class, 'show'],




3    ['user' => 1],




4    302,




5    ['X-Framework' => 'Laravel']




6);




return to_action(
    [UserController::class, 'show'],
    ['user' => 1],
    302,
    ['X-Framework' => 'Laravel']
);

```

#### [`to_route()`](https://laravel.com/docs/12.x/helpers#method-to-route)
The `to_route` function generates a [redirect HTTP response](https://laravel.com/docs/12.x/responses#redirects) for a given [named route](https://laravel.com/docs/12.x/routing#named-routes):
```


1return to_route('users.show', ['user' => 1]);




return to_route('users.show', ['user' => 1]);

```

If necessary, you may pass the HTTP status code that should be assigned to the redirect and any additional response headers as the third and fourth arguments to the `to_route` method:
```


1return to_route('users.show', ['user' => 1], 302, ['X-Framework' => 'Laravel']);




return to_route('users.show', ['user' => 1], 302, ['X-Framework' => 'Laravel']);

```

#### [`uri()`](https://laravel.com/docs/12.x/helpers#method-uri)
The `uri` function generates a [fluent URI instance](https://laravel.com/docs/12.x/helpers#uri) for the given URI:
```


1$uri = uri('https://example.com')




2    ->withPath('/users')




3    ->withQuery(['page' => 1]);




$uri = uri('https://example.com')
    ->withPath('/users')
    ->withQuery(['page' => 1]);

```

If the `uri` function is given an array containing a callable controller and method pair, the function will create a `Uri` instance for the controller method's route path:
```


1use App\Http\Controllers\UserController;




2 



3$uri = uri([UserController::class, 'show'], ['user' => $user]);




use App\Http\Controllers\UserController;

$uri = uri([UserController::class, 'show'], ['user' => $user]);

```

If the controller is invocable, you may simply provide the controller class name:
```


1use App\Http\Controllers\UserIndexController;




2 



3$uri = uri(UserIndexController::class);




use App\Http\Controllers\UserIndexController;

$uri = uri(UserIndexController::class);

```

If the value given to the `uri` function matches the name of a [named route](https://laravel.com/docs/12.x/routing#named-routes), a `Uri` instance will be generated for that route's path:
```


1$uri = uri('users.show', ['user' => $user]);




$uri = uri('users.show', ['user' => $user]);

```

#### [`url()`](https://laravel.com/docs/12.x/helpers#method-url)
The `url` function generates a fully qualified URL to the given path:
```


1$url = url('user/profile');




2 



3$url = url('user/profile', [1]);




$url = url('user/profile');

$url = url('user/profile', [1]);

```

If no path is provided, an `Illuminate\Routing\UrlGenerator` instance is returned:
```


1$current = url()->current();




2 



3$full = url()->full();




4 



5$previous = url()->previous();




$current = url()->current();

$full = url()->full();

$previous = url()->previous();

```

For more information on working with the `url` function, consult the [URL generation documentation](https://laravel.com/docs/12.x/urls#generating-urls).
