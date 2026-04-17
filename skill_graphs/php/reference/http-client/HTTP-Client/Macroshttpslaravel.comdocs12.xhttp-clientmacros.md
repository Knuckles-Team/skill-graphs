## [Macros](https://laravel.com/docs/12.x/http-client#macros)
The Laravel HTTP client allows you to define "macros", which can serve as a fluent, expressive mechanism to configure common request paths and headers when interacting with services throughout your application. To get started, you may define the macro within the `boot` method of your application's `App\Providers\AppServiceProvider` class:
```


 1use Illuminate\Support\Facades\Http;




 2 



 3/**




 4 * Bootstrap any application services.




 5 */




 6public function boot(): void




 7{




 8    Http::macro('github', function () {




 9        return Http::withHeaders([




10            'X-Example' => 'example',




11        ])->baseUrl('https://github.com');




12    });




13}




use Illuminate\Support\Facades\Http;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Http::macro('github', function () {
        return Http::withHeaders([
            'X-Example' => 'example',
        ])->baseUrl('https://github.com');
    });
}

```

Once your macro has been configured, you may invoke it from anywhere in your application to create a pending request with the specified configuration:
```


1$response = Http::github()->get('/');




$response = Http::github()->get('/');

```
