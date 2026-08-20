## [Rate Limiting](https://laravel.com/docs/12.x/routing#rate-limiting)
### [Defining Rate Limiters](https://laravel.com/docs/12.x/routing#defining-rate-limiters)
Laravel includes powerful and customizable rate limiting services that you may utilize to restrict the amount of traffic for a given route or group of routes. To get started, you should define rate limiter configurations that meet your application's needs.
Rate limiters may be defined within the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


 1use Illuminate\Cache\RateLimiting\Limit;




 2use Illuminate\Http\Request;




 3use Illuminate\Support\Facades\RateLimiter;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    RateLimiter::for('api', function (Request $request) {




11        return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());




12    });




13}




use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    RateLimiter::for('api', function (Request $request) {
        return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());
    });
}

```

Rate limiters are defined using the `RateLimiter` facade's `for` method. The `for` method accepts a rate limiter name and a closure that returns the limit configuration that should apply to routes that are assigned to the rate limiter. Limit configuration are instances of the `Illuminate\Cache\RateLimiting\Limit` class. This class contains helpful "builder" methods so that you can quickly define your limit. The rate limiter name may be any string you wish:
```


 1use Illuminate\Cache\RateLimiting\Limit;




 2use Illuminate\Http\Request;




 3use Illuminate\Support\Facades\RateLimiter;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    RateLimiter::for('global', function (Request $request) {




11        return Limit::perMinute(1000);




12    });




13}




use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    RateLimiter::for('global', function (Request $request) {
        return Limit::perMinute(1000);
    });
}

```

If the incoming request exceeds the specified rate limit, a response with a 429 HTTP status code will automatically be returned by Laravel. If you would like to define your own response that should be returned by a rate limit, you may use the `response` method:
```


1RateLimiter::for('global', function (Request $request) {




2    return Limit::perMinute(1000)->response(function (Request $request, array $headers) {




3        return response('Custom response...', 429, $headers);




4    });




5});




RateLimiter::for('global', function (Request $request) {
    return Limit::perMinute(1000)->response(function (Request $request, array $headers) {
        return response('Custom response...', 429, $headers);
    });
});

```

Since rate limiter callbacks receive the incoming HTTP request instance, you may build the appropriate rate limit dynamically based on the incoming request or authenticated user:
```


1RateLimiter::for('uploads', function (Request $request) {




2    return $request->user()->vipCustomer()




3        ? Limit::none()




4        : Limit::perHour(10);




5});




RateLimiter::for('uploads', function (Request $request) {
    return $request->user()->vipCustomer()
        ? Limit::none()
        : Limit::perHour(10);
});

```

#### [Segmenting Rate Limits](https://laravel.com/docs/12.x/routing#segmenting-rate-limits)
Sometimes you may wish to segment rate limits by some arbitrary value. For example, you may wish to allow users to access a given route 100 times per minute per IP address. To accomplish this, you may use the `by` method when building your rate limit:
```


1RateLimiter::for('uploads', function (Request $request) {




2    return $request->user()->vipCustomer()




3        ? Limit::none()




4        : Limit::perMinute(100)->by($request->ip());




5});




RateLimiter::for('uploads', function (Request $request) {
    return $request->user()->vipCustomer()
        ? Limit::none()
        : Limit::perMinute(100)->by($request->ip());
});

```

To illustrate this feature using another example, we can limit access to the route to 100 times per minute per authenticated user ID or 10 times per minute per IP address for guests:
```


1RateLimiter::for('uploads', function (Request $request) {




2    return $request->user()




3        ? Limit::perMinute(100)->by($request->user()->id)




4        : Limit::perMinute(10)->by($request->ip());




5});




RateLimiter::for('uploads', function (Request $request) {
    return $request->user()
        ? Limit::perMinute(100)->by($request->user()->id)
        : Limit::perMinute(10)->by($request->ip());
});

```

#### [Multiple Rate Limits](https://laravel.com/docs/12.x/routing#multiple-rate-limits)
If needed, you may return an array of rate limits for a given rate limiter configuration. Each rate limit will be evaluated for the route based on the order they are placed within the array:
```


1RateLimiter::for('login', function (Request $request) {




2    return [




3        Limit::perMinute(500),




4        Limit::perMinute(3)->by($request->input('email')),




5    ];




6});




RateLimiter::for('login', function (Request $request) {
    return [
        Limit::perMinute(500),
        Limit::perMinute(3)->by($request->input('email')),
    ];
});

```

If you're assigning multiple rate limits segmented by identical `by` values, you should ensure that each `by` value is unique. The easiest way to achieve this is to prefix the values given to the `by` method:
```


1RateLimiter::for('uploads', function (Request $request) {




2    return [




3        Limit::perMinute(10)->by('minute:'.$request->user()->id),




4        Limit::perDay(1000)->by('day:'.$request->user()->id),




5    ];




6});




RateLimiter::for('uploads', function (Request $request) {
    return [
        Limit::perMinute(10)->by('minute:'.$request->user()->id),
        Limit::perDay(1000)->by('day:'.$request->user()->id),
    ];
});

```

#### [Response-Based Rate Limiting](https://laravel.com/docs/12.x/routing#response-base-rate-limiting)
In addition to rate limiting incoming requests, Laravel allows you to rate limit based on the response using the `after` method. This is useful when you only want to count certain responses toward the rate limit, such as validation errors, 404 responses, or other specific HTTP status codes.
The `after` method accepts a closure that receives the response and should return `true` if the response should be counted toward the rate limit, or `false` if it should be ignored. This is particularly useful for preventing enumeration attacks by limiting consecutive 404 responses, or allowing users to retry requests that fail validation without exhausting their rate limit on an endpoint that should only throttle successful operations:
```


 1use Illuminate\Cache\RateLimiting\Limit;




 2use Illuminate\Http\Request;




 3use Illuminate\Support\Facades\RateLimiter;




 4use Symfony\Component\HttpFoundation\Response;




 5 



 6RateLimiter::for('resource-not-found', function (Request $request) {




 7    return Limit::perMinute(10)




 8        ->by($request->user()?->id ?: $request->ip())




 9        ->after(function (Response $response) {




10            // Only count 404 responses toward the rate limit to prevent enumeration...




11            return $response->status() === 404;




12        });




13});




use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;
use Symfony\Component\HttpFoundation\Response;

RateLimiter::for('resource-not-found', function (Request $request) {
    return Limit::perMinute(10)
        ->by($request->user()?->id ?: $request->ip())
        ->after(function (Response $response) {
            // Only count 404 responses toward the rate limit to prevent enumeration...
            return $response->status() === 404;
        });
});

```

### [Attaching Rate Limiters to Routes](https://laravel.com/docs/12.x/routing#attaching-rate-limiters-to-routes)
Rate limiters may be attached to routes or route groups using the `throttle` [middleware](https://laravel.com/docs/12.x/middleware). The throttle middleware accepts the name of the rate limiter you wish to assign to the route:
```


1Route::middleware(['throttle:uploads'])->group(function () {




2    Route::post('/audio', function () {




3        // ...




4    });




5 



6    Route::post('/video', function () {




7        // ...




8    });




9});




Route::middleware(['throttle:uploads'])->group(function () {
    Route::post('/audio', function () {
        // ...
    });

    Route::post('/video', function () {
        // ...
    });
});

```

#### [Throttling With Redis](https://laravel.com/docs/12.x/routing#throttling-with-redis)
By default, the `throttle` middleware is mapped to the `Illuminate\Routing\Middleware\ThrottleRequests` class. However, if you are using Redis as your application's cache driver, you may wish to instruct Laravel to use Redis to manage rate limiting. To do so, you should use the `throttleWithRedis` method in your application's `bootstrap/app.php` file. This method maps the `throttle` middleware to the `Illuminate\Routing\Middleware\ThrottleRequestsWithRedis` middleware class:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->throttleWithRedis();




3    // ...




4})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->throttleWithRedis();
    // ...
})

```
