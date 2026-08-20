## [SPA Authentication](https://laravel.com/docs/12.x/passport#spa-authentication)
When building an API, it can be extremely useful to be able to consume your own API from your JavaScript application. This approach to API development allows your own application to consume the same API that you are sharing with the world. The same API may be consumed by your web application, mobile applications, third-party applications, and any SDKs that you may publish on various package managers.
Typically, if you want to consume your API from your JavaScript application, you would need to manually send an access token to the application and pass it with each request to your application. However, Passport includes a middleware that can handle this for you. All you need to do is append the `CreateFreshApiToken` middleware to the `web` middleware group in your application's `bootstrap/app.php` file:
```


1use Laravel\Passport\Http\Middleware\CreateFreshApiToken;




2 



3->withMiddleware(function (Middleware $middleware): void {




4    $middleware->web(append: [




5        CreateFreshApiToken::class,




6    ]);




7})




use Laravel\Passport\Http\Middleware\CreateFreshApiToken;

->withMiddleware(function (Middleware $middleware): void {
    $middleware->web(append: [
        CreateFreshApiToken::class,
    ]);
})

```

You should ensure that the `CreateFreshApiToken` middleware is the last middleware listed in your middleware stack.
This middleware will attach a `laravel_token` cookie to your outgoing responses. This cookie contains an encrypted JWT that Passport will use to authenticate API requests from your JavaScript application. The JWT has a lifetime equal to your `session.lifetime` configuration value. Now, since the browser will automatically send the cookie with all subsequent requests, you may make requests to your application's API without explicitly passing an access token:
```


1axios.get('/api/user')




2    .then(response => {




3        console.log(response.data);




4    });




axios.get('/api/user')
    .then(response => {
        console.log(response.data);
    });

```

#### [Customizing the Cookie Name](https://laravel.com/docs/12.x/passport#customizing-the-cookie-name)
If needed, you can customize the `laravel_token` cookie's name using the `Passport::cookie` method. Typically, this method should be called from the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


1/**




2 * Bootstrap any application services.




3 */




4public function boot(): void




5{




6    Passport::cookie('custom_name');




7}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Passport::cookie('custom_name');
}

```

#### [CSRF Protection](https://laravel.com/docs/12.x/passport#csrf-protection)
When using this method of authentication, you will need to ensure a valid CSRF token header is included in your requests. The default Laravel JavaScript scaffolding included with the skeleton application and all starter kits includes an `XSRF-TOKEN` cookie value to send an `X-XSRF-TOKEN` header on same-origin requests.
If you choose to send the `X-CSRF-TOKEN` header instead of `X-XSRF-TOKEN`, you will need to use the unencrypted token provided by `csrf_token()`.
