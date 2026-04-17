## [Cross-Origin Resource Sharing (CORS)](https://laravel.com/docs/12.x/routing#cors)
Laravel can automatically respond to CORS `OPTIONS` HTTP requests with values that you configure. The `OPTIONS` requests will automatically be handled by the `HandleCors` [middleware](https://laravel.com/docs/12.x/middleware) that is automatically included in your application's global middleware stack.
Sometimes, you may need to customize the CORS configuration values for your application. You may do so by publishing the `cors` configuration file using the `config:publish` Artisan command:
```


1php artisan config:publish cors




php artisan config:publish cors

```

This command will place a `cors.php` configuration file within your application's `config` directory.
For more information on CORS and CORS headers, please consult the
