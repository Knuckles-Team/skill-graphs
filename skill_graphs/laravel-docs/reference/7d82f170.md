## [Fallback Routes](https://laravel.com/docs/12.x/routing#fallback-routes)
Using the `Route::fallback` method, you may define a route that will be executed when no other route matches the incoming request. Typically, unhandled requests will automatically render a "404" page via your application's exception handler. However, since you would typically define the `fallback` route within your `routes/web.php` file, all middleware in the `web` middleware group will apply to the route. You are free to add additional middleware to this route as needed:
```


1Route::fallback(function () {




2    // ...




3});




Route::fallback(function () {
    // ...
});

```
