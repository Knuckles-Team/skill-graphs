## [Authentication](https://laravel.com/docs/12.x/mcp#authentication)
Just like routes, you can authenticate web MCP servers with middleware. Adding authentication to your MCP server will require a user to authenticate before using any capability of the server.
There are two ways to authenticate access to your MCP server: simple, token based authentication via [Laravel Sanctum](https://laravel.com/docs/12.x/sanctum) or any token which is passed via the `Authorization` HTTP header. Or, you may authenticate via OAuth using [Laravel Passport](https://laravel.com/docs/12.x/passport).
### [OAuth 2.1](https://laravel.com/docs/12.x/mcp#oauth)
The most robust way to protect your web-based MCP servers is with OAuth using [Laravel Passport](https://laravel.com/docs/12.x/passport).
When authenticating your MCP server via OAuth, invoke the `Mcp::oauthRoutes` method in your `routes/ai.php` file to register the required OAuth2 discovery and client registration routes. Then, apply Passport's `auth:api` middleware to your `Mcp::web` route in your `routes/ai.php` file:
```


1use App\Mcp\Servers\WeatherExample;




2use Laravel\Mcp\Facades\Mcp;




3 



4Mcp::oauthRoutes();




5 



6Mcp::web('/mcp/weather', WeatherExample::class)




7    ->middleware('auth:api');




use App\Mcp\Servers\WeatherExample;
use Laravel\Mcp\Facades\Mcp;

Mcp::oauthRoutes();

Mcp::web('/mcp/weather', WeatherExample::class)
    ->middleware('auth:api');

```

#### New Passport Installation
If your application is not already using Laravel Passport, follow Passport's [installation and deployment guide](https://laravel.com/docs/12.x/passport#installation) to add Passport to your application. You should have an `OAuthenticatable` model, new authentication guard, and passport keys before moving on.
Next, you should publish Laravel MCP's provided Passport authorization view:
```


1php artisan vendor:publish --tag=mcp-views




php artisan vendor:publish --tag=mcp-views

```

Then, instruct Passport to use this view using the `Passport::authorizationView` method. Typically, this method should be invoked in the `boot` method of your application's `AppServiceProvider`:
```


 1use Laravel\Passport\Passport;




 2 



 3/**




 4 * Bootstrap any application services.




 5 */




 6public function boot(): void




 7{




 8    Passport::authorizationView(function ($parameters) {




 9        return view('mcp.authorize', $parameters);




10    });




11}




use Laravel\Passport\Passport;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Passport::authorizationView(function ($parameters) {
        return view('mcp.authorize', $parameters);
    });
}

```

This view will be displayed to the end-user during authentication to reject or approve the AI agent's authentication attempt.
![Authorization screen example](https://laravel.com/docs/12.x/mcp)
In this scenario, we're simply using OAuth as a translation layer to the underlying authenticatable model. We are ignoring many aspects of OAuth, such as scopes.
#### Using an Existing Passport Installation
If your application is already using Laravel Passport, Laravel MCP should work seamlessly within your existing Passport installation, but custom scopes aren't currently supported as OAuth is primarily used as a translation layer to the underlying authenticatable model.
Laravel MCP, via the `Mcp::oauthRoutes` method discussed above, adds, advertises, and uses a single `mcp:use` scope.
#### Passport vs. Sanctum
OAuth2.1 is the documented authentication mechanism in the Model Context Protocol specification, and is the most widely supported among MCP clients. For that reason, we recommend using Passport when possible.
If your application is already using [Sanctum](https://laravel.com/docs/12.x/sanctum) then adding Passport may be cumbersome. In this instance, we recommend using Sanctum without Passport until you have a clear, necessary requirement to use an MCP client that only supports OAuth.
### [Sanctum](https://laravel.com/docs/12.x/mcp#sanctum)
If you would like to protect your MCP server using [Sanctum](https://laravel.com/docs/12.x/sanctum), simply add Sanctum's authentication middleware to your server in your `routes/ai.php` file. Then, ensure your MCP clients provide an `Authorization: Bearer <token>` header to ensure successful authentication:
```


1use App\Mcp\Servers\WeatherExample;




2use Laravel\Mcp\Facades\Mcp;




3 



4Mcp::web('/mcp/demo', WeatherExample::class)




5    ->middleware('auth:sanctum');




use App\Mcp\Servers\WeatherExample;
use Laravel\Mcp\Facades\Mcp;

Mcp::web('/mcp/demo', WeatherExample::class)
    ->middleware('auth:sanctum');

```

#### [Custom MCP Authentication](https://laravel.com/docs/12.x/mcp#custom-mcp-authentication)
If your application issues its own custom API tokens, you may authenticate your MCP server by assigning any middleware you wish to your `Mcp::web` routes. Your custom middleware can inspect the `Authorization` header manually to authenticate the incoming MCP request.
