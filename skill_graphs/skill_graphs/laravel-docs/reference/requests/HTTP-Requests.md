# HTTP Requests
  * [Introduction](https://laravel.com/docs/12.x/requests#introduction)
  * [Interacting With The Request](https://laravel.com/docs/12.x/requests#interacting-with-the-request)
    * [Accessing the Request](https://laravel.com/docs/12.x/requests#accessing-the-request)
    * [Request Path, Host, and Method](https://laravel.com/docs/12.x/requests#request-path-and-method)
    * [Request Headers](https://laravel.com/docs/12.x/requests#request-headers)
    * [Request IP Address](https://laravel.com/docs/12.x/requests#request-ip-address)
    * [Content Negotiation](https://laravel.com/docs/12.x/requests#content-negotiation)
    * [PSR-7 Requests](https://laravel.com/docs/12.x/requests#psr7-requests)
  * [Input](https://laravel.com/docs/12.x/requests#input)
    * [Retrieving Input](https://laravel.com/docs/12.x/requests#retrieving-input)
    * [Input Presence](https://laravel.com/docs/12.x/requests#input-presence)
    * [Merging Additional Input](https://laravel.com/docs/12.x/requests#merging-additional-input)
    * [Old Input](https://laravel.com/docs/12.x/requests#old-input)
    * [Cookies](https://laravel.com/docs/12.x/requests#cookies)
    * [Input Trimming and Normalization](https://laravel.com/docs/12.x/requests#input-trimming-and-normalization)
  * [Files](https://laravel.com/docs/12.x/requests#files)
    * [Retrieving Uploaded Files](https://laravel.com/docs/12.x/requests#retrieving-uploaded-files)
    * [Storing Uploaded Files](https://laravel.com/docs/12.x/requests#storing-uploaded-files)
  * [Configuring Trusted Proxies](https://laravel.com/docs/12.x/requests#configuring-trusted-proxies)
  * [Configuring Trusted Hosts](https://laravel.com/docs/12.x/requests#configuring-trusted-hosts)


## [Introduction](https://laravel.com/docs/12.x/requests#introduction)
Laravel's `Illuminate\Http\Request` class provides an object-oriented way to interact with the current HTTP request being handled by your application as well as retrieve the input, cookies, and files that were submitted with the request.
## [Interacting With The Request](https://laravel.com/docs/12.x/requests#interacting-with-the-request)
### [Accessing the Request](https://laravel.com/docs/12.x/requests#accessing-the-request)
To obtain an instance of the current HTTP request via dependency injection, you should type-hint the `Illuminate\Http\Request` class on your route closure or controller method. The incoming request instance will automatically be injected by the Laravel [service container](https://laravel.com/docs/12.x/container):
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Http\RedirectResponse;




 6use Illuminate\Http\Request;




 7 



 8class UserController extends Controller




 9{




10    /**




11     * Store a new user.




12     */




13    public function store(Request $request): RedirectResponse




14    {




15        $name = $request->input('name');




16 



17        // Store the user...




18 



19        return redirect('/users');




20    }




21}




<?php

namespace App\Http\Controllers;

use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class UserController extends Controller
{
    /**
     * Store a new user.
     */
    public function store(Request $request): RedirectResponse
    {
        $name = $request->input('name');

        // Store the user...

        return redirect('/users');
    }
}

```

As mentioned, you may also type-hint the `Illuminate\Http\Request` class on a route closure. The service container will automatically inject the incoming request into the closure when it is executed:
```


1use Illuminate\Http\Request;




2 



3Route::get('/', function (Request $request) {




4    // ...




5});




use Illuminate\Http\Request;

Route::get('/', function (Request $request) {
    // ...
});

```

#### [Dependency Injection and Route Parameters](https://laravel.com/docs/12.x/requests#dependency-injection-route-parameters)
If your controller method is also expecting input from a route parameter you should list your route parameters after your other dependencies. For example, if your route is defined like so:
```


1use App\Http\Controllers\UserController;




2 



3Route::put('/user/{id}', [UserController::class, 'update']);




use App\Http\Controllers\UserController;

Route::put('/user/{id}', [UserController::class, 'update']);

```

You may still type-hint the `Illuminate\Http\Request` and access your `id` route parameter by defining your controller method as follows:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Http\RedirectResponse;




 6use Illuminate\Http\Request;




 7 



 8class UserController extends Controller




 9{




10    /**




11     * Update the specified user.




12     */




13    public function update(Request $request, string $id): RedirectResponse




14    {




15        // Update the user...




16 



17        return redirect('/users');




18    }




19}




<?php

namespace App\Http\Controllers;

use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class UserController extends Controller
{
    /**
     * Update the specified user.
     */
    public function update(Request $request, string $id): RedirectResponse
    {
        // Update the user...

        return redirect('/users');
    }
}

```

### [Request Path, Host, and Method](https://laravel.com/docs/12.x/requests#request-path-and-method)
The `Illuminate\Http\Request` instance provides a variety of methods for examining the incoming HTTP request and extends the `Symfony\Component\HttpFoundation\Request` class. We will discuss a few of the most important methods below.
#### [Retrieving the Request Path](https://laravel.com/docs/12.x/requests#retrieving-the-request-path)
The `path` method returns the request's path information. So, if the incoming request is targeted at `http://example.com/foo/bar`, the `path` method will return `foo/bar`:
```


1$uri = $request->path();




$uri = $request->path();

```

#### [Inspecting the Request Path / Route](https://laravel.com/docs/12.x/requests#inspecting-the-request-path)
The `is` method allows you to verify that the incoming request path matches a given pattern. You may use the `*` character as a wildcard when utilizing this method:
```


1if ($request->is('admin/*')) {




2    // ...




3}




if ($request->is('admin/*')) {
    // ...
}

```

Using the `routeIs` method, you may determine if the incoming request has matched a [named route](https://laravel.com/docs/12.x/routing#named-routes):
```


1if ($request->routeIs('admin.*')) {




2    // ...




3}




if ($request->routeIs('admin.*')) {
    // ...
}

```

#### [Retrieving the Request URL](https://laravel.com/docs/12.x/requests#retrieving-the-request-url)
To retrieve the full URL for the incoming request you may use the `url` or `fullUrl` methods. The `url` method will return the URL without the query string, while the `fullUrl` method includes the query string:
```


1$url = $request->url();




2 



3$urlWithQueryString = $request->fullUrl();




$url = $request->url();

$urlWithQueryString = $request->fullUrl();

```

If you would like to append query string data to the current URL, you may call the `fullUrlWithQuery` method. This method merges the given array of query string variables with the current query string:
```


1$request->fullUrlWithQuery(['type' => 'phone']);




$request->fullUrlWithQuery(['type' => 'phone']);

```

If you would like to get the current URL without a given query string parameter, you may utilize the `fullUrlWithoutQuery` method:
```


1$request->fullUrlWithoutQuery(['type']);




$request->fullUrlWithoutQuery(['type']);

```

#### [Retrieving the Request Host](https://laravel.com/docs/12.x/requests#retrieving-the-request-host)
You may retrieve the "host" of the incoming request via the `host`, `httpHost`, and `schemeAndHttpHost` methods:
```


1$request->host();




2$request->httpHost();




3$request->schemeAndHttpHost();




$request->host();
$request->httpHost();
$request->schemeAndHttpHost();

```

#### [Retrieving the Request Method](https://laravel.com/docs/12.x/requests#retrieving-the-request-method)
The `method` method will return the HTTP verb for the request. You may use the `isMethod` method to verify that the HTTP verb matches a given string:
```


1$method = $request->method();




2 



3if ($request->isMethod('post')) {




4    // ...




5}




$method = $request->method();

if ($request->isMethod('post')) {
    // ...
}

```

### [Request Headers](https://laravel.com/docs/12.x/requests#request-headers)
You may retrieve a request header from the `Illuminate\Http\Request` instance using the `header` method. If the header is not present on the request, `null` will be returned. However, the `header` method accepts an optional second argument that will be returned if the header is not present on the request:
```


1$value = $request->header('X-Header-Name');




2 



3$value = $request->header('X-Header-Name', 'default');




$value = $request->header('X-Header-Name');

$value = $request->header('X-Header-Name', 'default');

```

The `hasHeader` method may be used to determine if the request contains a given header:
```


1if ($request->hasHeader('X-Header-Name')) {




2    // ...




3}




if ($request->hasHeader('X-Header-Name')) {
    // ...
}

```

For convenience, the `bearerToken` method may be used to retrieve a bearer token from the `Authorization` header. If no such header is present, an empty string will be returned:
```


1$token = $request->bearerToken();




$token = $request->bearerToken();

```

### [Request IP Address](https://laravel.com/docs/12.x/requests#request-ip-address)
The `ip` method may be used to retrieve the IP address of the client that made the request to your application:
```


1$ipAddress = $request->ip();




$ipAddress = $request->ip();

```

If you would like to retrieve an array of IP addresses, including all of the client IP addresses that were forwarded by proxies, you may use the `ips` method. The "original" client IP address will be at the end of the array:
```


1$ipAddresses = $request->ips();




$ipAddresses = $request->ips();

```

In general, IP addresses should be considered untrusted, user-controlled input and be used for informational purposes only.
### [Content Negotiation](https://laravel.com/docs/12.x/requests#content-negotiation)
Laravel provides several methods for inspecting the incoming request's requested content types via the `Accept` header. First, the `getAcceptableContentTypes` method will return an array containing all of the content types accepted by the request:
```


1$contentTypes = $request->getAcceptableContentTypes();




$contentTypes = $request->getAcceptableContentTypes();

```

The `accepts` method accepts an array of content types and returns `true` if any of the content types are accepted by the request. Otherwise, `false` will be returned:
```


1if ($request->accepts(['text/html', 'application/json'])) {




2    // ...




3}




if ($request->accepts(['text/html', 'application/json'])) {
    // ...
}

```

You may use the `prefers` method to determine which content type out of a given array of content types is most preferred by the request. If none of the provided content types are accepted by the request, `null` will be returned:
```


1$preferred = $request->prefers(['text/html', 'application/json']);




$preferred = $request->prefers(['text/html', 'application/json']);

```

Since many applications only serve HTML or JSON, you may use the `expectsJson` method to quickly determine if the incoming request expects a JSON response:
```


1if ($request->expectsJson()) {




2    // ...




3}




if ($request->expectsJson()) {
    // ...
}

```

### [PSR-7 Requests](https://laravel.com/docs/12.x/requests#psr7-requests)
The _Symfony HTTP Message Bridge_ component to convert typical Laravel requests and responses into PSR-7 compatible implementations:
```


1composer require symfony/psr-http-message-bridge




2composer require nyholm/psr7




composer require symfony/psr-http-message-bridge
composer require nyholm/psr7

```

Once you have installed these libraries, you may obtain a PSR-7 request by type-hinting the request interface on your route closure or controller method:
```


1use Psr\Http\Message\ServerRequestInterface;




2 



3Route::get('/', function (ServerRequestInterface $request) {




4    // ...




5});




use Psr\Http\Message\ServerRequestInterface;

Route::get('/', function (ServerRequestInterface $request) {
    // ...
});

```

If you return a PSR-7 response instance from a route or controller, it will automatically be converted back to a Laravel response instance and be displayed by the framework.
## [Input](https://laravel.com/docs/12.x/requests#input)
### [Retrieving Input](https://laravel.com/docs/12.x/requests#retrieving-input)
#### [Retrieving All Input Data](https://laravel.com/docs/12.x/requests#retrieving-all-input-data)
You may retrieve all of the incoming request's input data as an `array` using the `all` method. This method may be used regardless of whether the incoming request is from an HTML form or is an XHR request:
```


1$input = $request->all();




$input = $request->all();

```

Using the `collect` method, you may retrieve all of the incoming request's input data as a [collection](https://laravel.com/docs/12.x/collections):
```


1$input = $request->collect();




$input = $request->collect();

```

The `collect` method also allows you to retrieve a subset of the incoming request's input as a collection:
```


1$request->collect('users')->each(function (string $user) {




2    // ...




3});




$request->collect('users')->each(function (string $user) {
    // ...
});

```

#### [Retrieving an Input Value](https://laravel.com/docs/12.x/requests#retrieving-an-input-value)
Using a few simple methods, you may access all of the user input from your `Illuminate\Http\Request` instance without worrying about which HTTP verb was used for the request. Regardless of the HTTP verb, the `input` method may be used to retrieve user input:
```


1$name = $request->input('name');




$name = $request->input('name');

```

You may pass a default value as the second argument to the `input` method. This value will be returned if the requested input value is not present on the request:
```


1$name = $request->input('name', 'Sally');




$name = $request->input('name', 'Sally');

```

When working with forms that contain array inputs, use "dot" notation to access the arrays:
```


1$name = $request->input('products.0.name');




2 



3$names = $request->input('products.*.name');




$name = $request->input('products.0.name');

$names = $request->input('products.*.name');

```

You may call the `input` method without any arguments in order to retrieve all of the input values as an associative array:
```


1$input = $request->input();




$input = $request->input();

```

#### [Retrieving Input From the Query String](https://laravel.com/docs/12.x/requests#retrieving-input-from-the-query-string)
While the `input` method retrieves values from the entire request payload (including the query string), the `query` method will only retrieve values from the query string:
```


1$name = $request->query('name');




$name = $request->query('name');

```

If the requested query string value data is not present, the second argument to this method will be returned:
```


1$name = $request->query('name', 'Helen');




$name = $request->query('name', 'Helen');

```

You may call the `query` method without any arguments in order to retrieve all of the query string values as an associative array:
```


1$query = $request->query();




$query = $request->query();

```

#### [Retrieving JSON Input Values](https://laravel.com/docs/12.x/requests#retrieving-json-input-values)
When sending JSON requests to your application, you may access the JSON data via the `input` method as long as the `Content-Type` header of the request is properly set to `application/json`. You may even use "dot" syntax to retrieve values that are nested within JSON arrays / objects:
```


1$name = $request->input('user.name');




$name = $request->input('user.name');

```

#### [Retrieving Stringable Input Values](https://laravel.com/docs/12.x/requests#retrieving-stringable-input-values)
Instead of retrieving the request's input data as a primitive `string`, you may use the `string` method to retrieve the request data as an instance of [Illuminate\Support\Stringable](https://laravel.com/docs/12.x/strings):
```


1$name = $request->string('name')->trim();




$name = $request->string('name')->trim();

```

#### [Retrieving Integer Input Values](https://laravel.com/docs/12.x/requests#retrieving-integer-input-values)
To retrieve input values as integers, you may use the `integer` method. This method will attempt to cast the input value to an integer. If the input is not present or the cast fails, it will return the default value you specify. This is particularly useful for pagination or other numeric inputs:
```


1$perPage = $request->integer('per_page');




$perPage = $request->integer('per_page');

```

#### [Retrieving Boolean Input Values](https://laravel.com/docs/12.x/requests#retrieving-boolean-input-values)
When dealing with HTML elements like checkboxes, your application may receive "truthy" values that are actually strings. For example, "true" or "on". For convenience, you may use the `boolean` method to retrieve these values as booleans. The `boolean` method returns `true` for 1, "1", true, "true", "on", and "yes". All other values will return `false`:
```


1$archived = $request->boolean('archived');




$archived = $request->boolean('archived');

```

#### [Retrieving Array Input Values](https://laravel.com/docs/12.x/requests#retrieving-array-input-values)
Input values containing arrays may be retrieved using the `array` method. This method will always cast the input value to an array. If the request does not contain an input value with the given name, an empty array will be returned:
```


1$versions = $request->array('versions');




$versions = $request->array('versions');

```

#### [Retrieving Date Input Values](https://laravel.com/docs/12.x/requests#retrieving-date-input-values)
For convenience, input values containing dates / times may be retrieved as Carbon instances using the `date` method. If the request does not contain an input value with the given name, `null` will be returned:
```


1$birthday = $request->date('birthday');




$birthday = $request->date('birthday');

```

The second and third arguments accepted by the `date` method may be used to specify the date's format and timezone, respectively:
```


1$elapsed = $request->date('elapsed', '!H:i', 'Europe/Madrid');




$elapsed = $request->date('elapsed', '!H:i', 'Europe/Madrid');

```

If the input value is present but has an invalid format, an `InvalidArgumentException` will be thrown; therefore, it is recommended that you validate the input before invoking the `date` method.
#### [Retrieving Enum Input Values](https://laravel.com/docs/12.x/requests#retrieving-enum-input-values)
Input values that correspond to `null` will be returned. The `enum` method accepts the name of the input value and the enum class as its first and second arguments:
```


1use App\Enums\Status;




2 



3$status = $request->enum('status', Status::class);




use App\Enums\Status;

$status = $request->enum('status', Status::class);

```

You may also provide a default value that will be returned if the value is missing or invalid:
```


1$status = $request->enum('status', Status::class, Status::Pending);




$status = $request->enum('status', Status::class, Status::Pending);

```

If the input value is an array of values that correspond to a PHP enum, you may use the `enums` method to retrieve the array of values as enum instances:
```


1use App\Enums\Product;




2 



3$products = $request->enums('products', Product::class);




use App\Enums\Product;

$products = $request->enums('products', Product::class);

```

#### [Retrieving Input via Dynamic Properties](https://laravel.com/docs/12.x/requests#retrieving-input-via-dynamic-properties)
You may also access user input using dynamic properties on the `Illuminate\Http\Request` instance. For example, if one of your application's forms contains a `name` field, you may access the value of the field like so:
```


1$name = $request->name;




$name = $request->name;

```

When using dynamic properties, Laravel will first look for the parameter's value in the request payload. If it is not present, Laravel will search for the field in the matched route's parameters.
#### [Retrieving a Portion of the Input Data](https://laravel.com/docs/12.x/requests#retrieving-a-portion-of-the-input-data)
If you need to retrieve a subset of the input data, you may use the `only` and `except` methods. Both of these methods accept a single `array` or a dynamic list of arguments:
```


1$input = $request->only(['username', 'password']);




2 



3$input = $request->only('username', 'password');




4 



5$input = $request->except(['credit_card']);




6 



7$input = $request->except('credit_card');




$input = $request->only(['username', 'password']);

$input = $request->only('username', 'password');

$input = $request->except(['credit_card']);

$input = $request->except('credit_card');

```

The `only` method returns all of the key / value pairs that you request; however, it will not return key / value pairs that are not present on the request.
### [Input Presence](https://laravel.com/docs/12.x/requests#input-presence)
You may use the `has` method to determine if a value is present on the request. The `has` method returns `true` if the value is present on the request:
```


1if ($request->has('name')) {




2    // ...




3}




if ($request->has('name')) {
    // ...
}

```

When given an array, the `has` method will determine if all of the specified values are present:
```


1if ($request->has(['name', 'email'])) {




2    // ...




3}




if ($request->has(['name', 'email'])) {
    // ...
}

```

The `hasAny` method returns `true` if any of the specified values are present:
```


1if ($request->hasAny(['name', 'email'])) {




2    // ...




3}




if ($request->hasAny(['name', 'email'])) {
    // ...
}

```

The `whenHas` method will execute the given closure if a value is present on the request:
```


1$request->whenHas('name', function (string $input) {




2    // ...




3});




$request->whenHas('name', function (string $input) {
    // ...
});

```

A second closure may be passed to the `whenHas` method that will be executed if the specified value is not present on the request:
```


1$request->whenHas('name', function (string $input) {




2    // The "name" value is present...




3}, function () {




4    // The "name" value is not present...




5});




$request->whenHas('name', function (string $input) {
    // The "name" value is present...
}, function () {
    // The "name" value is not present...
});

```

If you would like to determine if a value is present on the request and is not an empty string, you may use the `filled` method:
```


1if ($request->filled('name')) {




2    // ...




3}




if ($request->filled('name')) {
    // ...
}

```

If you would like to determine if a value is missing from the request or is an empty string, you may use the `isNotFilled` method:
```


1if ($request->isNotFilled('name')) {




2    // ...




3}




if ($request->isNotFilled('name')) {
    // ...
}

```

When given an array, the `isNotFilled` method will determine if all of the specified values are missing or empty:
```


1if ($request->isNotFilled(['name', 'email'])) {




2    // ...




3}




if ($request->isNotFilled(['name', 'email'])) {
    // ...
}

```

The `anyFilled` method returns `true` if any of the specified values is not an empty string:
```


1if ($request->anyFilled(['name', 'email'])) {




2    // ...




3}




if ($request->anyFilled(['name', 'email'])) {
    // ...
}

```

The `whenFilled` method will execute the given closure if a value is present on the request and is not an empty string:
```


1$request->whenFilled('name', function (string $input) {




2    // ...




3});




$request->whenFilled('name', function (string $input) {
    // ...
});

```

A second closure may be passed to the `whenFilled` method that will be executed if the specified value is not "filled":
```


1$request->whenFilled('name', function (string $input) {




2    // The "name" value is filled...




3}, function () {




4    // The "name" value is not filled...




5});




$request->whenFilled('name', function (string $input) {
    // The "name" value is filled...
}, function () {
    // The "name" value is not filled...
});

```

To determine if a given key is absent from the request, you may use the `missing` and `whenMissing` methods:
```


1if ($request->missing('name')) {




2    // ...




3}




4 



5$request->whenMissing('name', function () {




6    // The "name" value is missing...




7}, function () {




8    // The "name" value is present...




9});




if ($request->missing('name')) {
    // ...
}

$request->whenMissing('name', function () {
    // The "name" value is missing...
}, function () {
    // The "name" value is present...
});

```

### [Merging Additional Input](https://laravel.com/docs/12.x/requests#merging-additional-input)
Sometimes you may need to manually merge additional input into the request's existing input data. To accomplish this, you may use the `merge` method. If a given input key already exists on the request, it will be overwritten by the data provided to the `merge` method:
```


1$request->merge(['votes' => 0]);




$request->merge(['votes' => 0]);

```

The `mergeIfMissing` method may be used to merge input into the request if the corresponding keys do not already exist within the request's input data:
```


1$request->mergeIfMissing(['votes' => 0]);




$request->mergeIfMissing(['votes' => 0]);

```

### [Old Input](https://laravel.com/docs/12.x/requests#old-input)
Laravel allows you to keep input from one request during the next request. This feature is particularly useful for re-populating forms after detecting validation errors. However, if you are using Laravel's included [validation features](https://laravel.com/docs/12.x/validation), it is possible that you will not need to manually use these session input flashing methods directly, as some of Laravel's built-in validation facilities will call them automatically.
#### [Flashing Input to the Session](https://laravel.com/docs/12.x/requests#flashing-input-to-the-session)
The `flash` method on the `Illuminate\Http\Request` class will flash the current input to the [session](https://laravel.com/docs/12.x/session) so that it is available during the user's next request to the application:
```


1$request->flash();




$request->flash();

```

You may also use the `flashOnly` and `flashExcept` methods to flash a subset of the request data to the session. These methods are useful for keeping sensitive information such as passwords out of the session:
```


1$request->flashOnly(['username', 'email']);




2 



3$request->flashExcept('password');




$request->flashOnly(['username', 'email']);

$request->flashExcept('password');

```

#### [Flashing Input Then Redirecting](https://laravel.com/docs/12.x/requests#flashing-input-then-redirecting)
Since you often will want to flash input to the session and then redirect to the previous page, you may easily chain input flashing onto a redirect using the `withInput` method:
```


1return redirect('/form')->withInput();




2 



3return redirect()->route('user.create')->withInput();




4 



5return redirect('/form')->withInput(




6    $request->except('password')




7);




return redirect('/form')->withInput();

return redirect()->route('user.create')->withInput();

return redirect('/form')->withInput(
    $request->except('password')
);

```

#### [Retrieving Old Input](https://laravel.com/docs/12.x/requests#retrieving-old-input)
To retrieve flashed input from the previous request, invoke the `old` method on an instance of `Illuminate\Http\Request`. The `old` method will pull the previously flashed input data from the [session](https://laravel.com/docs/12.x/session):
```


1$username = $request->old('username');




$username = $request->old('username');

```

Laravel also provides a global `old` helper. If you are displaying old input within a [Blade template](https://laravel.com/docs/12.x/blade), it is more convenient to use the `old` helper to repopulate the form. If no old input exists for the given field, `null` will be returned:
```


1<input type="text" name="username" value="{{ old('username') }}">




<input type="text" name="username" value="{{ old('username') }}">

```

### [Cookies](https://laravel.com/docs/12.x/requests#cookies)
#### [Retrieving Cookies From Requests](https://laravel.com/docs/12.x/requests#retrieving-cookies-from-requests)
All cookies created by the Laravel framework are encrypted and signed with an authentication code, meaning they will be considered invalid if they have been changed by the client. To retrieve a cookie value from the request, use the `cookie` method on an `Illuminate\Http\Request` instance:
```


1$value = $request->cookie('name');




$value = $request->cookie('name');

```

## [Input Trimming and Normalization](https://laravel.com/docs/12.x/requests#input-trimming-and-normalization)
By default, Laravel includes the `Illuminate\Foundation\Http\Middleware\TrimStrings` and `Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull` middleware in your application's global middleware stack. These middleware will automatically trim all incoming string fields on the request, as well as convert any empty string fields to `null`. This allows you to not have to worry about these normalization concerns in your routes and controllers.
#### Disabling Input Normalization
If you would like to disable this behavior for all requests, you may remove the two middleware from your application's middleware stack by invoking the `$middleware->remove` method in your application's `bootstrap/app.php` file:
```


1use Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull;




2use Illuminate\Foundation\Http\Middleware\TrimStrings;




3 



4->withMiddleware(function (Middleware $middleware): void {




5    $middleware->remove([




6        ConvertEmptyStringsToNull::class,




7        TrimStrings::class,




8    ]);




9})




use Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull;
use Illuminate\Foundation\Http\Middleware\TrimStrings;

->withMiddleware(function (Middleware $middleware): void {
    $middleware->remove([
        ConvertEmptyStringsToNull::class,
        TrimStrings::class,
    ]);
})

```

If you would like to disable string trimming and empty string conversion for a subset of requests to your application, you may use the `trimStrings` and `convertEmptyStringsToNull` middleware methods within your application's `bootstrap/app.php` file. Both methods accept an array of closures, which should return `true` or `false` to indicate whether input normalization should be skipped:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->convertEmptyStringsToNull(except: [




3        fn (Request $request) => $request->is('admin/*'),




4    ]);




5 



6    $middleware->trimStrings(except: [




7        fn (Request $request) => $request->is('admin/*'),




8    ]);




9})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->convertEmptyStringsToNull(except: [
        fn (Request $request) => $request->is('admin/*'),
    ]);

    $middleware->trimStrings(except: [
        fn (Request $request) => $request->is('admin/*'),
    ]);
})

```

## [Files](https://laravel.com/docs/12.x/requests#files)
### [Retrieving Uploaded Files](https://laravel.com/docs/12.x/requests#retrieving-uploaded-files)
You may retrieve uploaded files from an `Illuminate\Http\Request` instance using the `file` method or using dynamic properties. The `file` method returns an instance of the `Illuminate\Http\UploadedFile` class, which extends the PHP `SplFileInfo` class and provides a variety of methods for interacting with the file:
```


1$file = $request->file('photo');




2 



3$file = $request->photo;




$file = $request->file('photo');

$file = $request->photo;

```

You may determine if a file is present on the request using the `hasFile` method:
```


1if ($request->hasFile('photo')) {




2    // ...




3}




if ($request->hasFile('photo')) {
    // ...
}

```

#### [Validating Successful Uploads](https://laravel.com/docs/12.x/requests#validating-successful-uploads)
In addition to checking if the file is present, you may verify that there were no problems uploading the file via the `isValid` method:
```


1if ($request->file('photo')->isValid()) {




2    // ...




3}




if ($request->file('photo')->isValid()) {
    // ...
}

```

#### [File Paths and Extensions](https://laravel.com/docs/12.x/requests#file-paths-extensions)
The `UploadedFile` class also contains methods for accessing the file's fully-qualified path and its extension. The `extension` method will attempt to guess the file's extension based on its contents. This extension may be different from the extension that was supplied by the client:
```


1$path = $request->photo->path();




2 



3$extension = $request->photo->extension();




$path = $request->photo->path();

$extension = $request->photo->extension();

```

#### [Other File Methods](https://laravel.com/docs/12.x/requests#other-file-methods)
There are a variety of other methods available on `UploadedFile` instances. Check out the
### [Storing Uploaded Files](https://laravel.com/docs/12.x/requests#storing-uploaded-files)
To store an uploaded file, you will typically use one of your configured [filesystems](https://laravel.com/docs/12.x/filesystem). The `UploadedFile` class has a `store` method that will move an uploaded file to one of your disks, which may be a location on your local filesystem or a cloud storage location like Amazon S3.
The `store` method accepts the path where the file should be stored relative to the filesystem's configured root directory. This path should not contain a filename, since a unique ID will automatically be generated to serve as the filename.
The `store` method also accepts an optional second argument for the name of the disk that should be used to store the file. The method will return the path of the file relative to the disk's root:
```


1$path = $request->photo->store('images');




2 



3$path = $request->photo->store('images', 's3');




$path = $request->photo->store('images');

$path = $request->photo->store('images', 's3');

```

If you do not want a filename to be automatically generated, you may use the `storeAs` method, which accepts the path, filename, and disk name as its arguments:
```


1$path = $request->photo->storeAs('images', 'filename.jpg');




2 



3$path = $request->photo->storeAs('images', 'filename.jpg', 's3');




$path = $request->photo->storeAs('images', 'filename.jpg');

$path = $request->photo->storeAs('images', 'filename.jpg', 's3');

```

For more information about file storage in Laravel, check out the complete [file storage documentation](https://laravel.com/docs/12.x/filesystem).
## [Configuring Trusted Proxies](https://laravel.com/docs/12.x/requests#configuring-trusted-proxies)
When running your applications behind a load balancer that terminates TLS / SSL certificates, you may notice your application sometimes does not generate HTTPS links when using the `url` helper. Typically this is because your application is being forwarded traffic from your load balancer on port 80 and does not know it should generate secure links.
To solve this, you may enable the `Illuminate\Http\Middleware\TrustProxies` middleware that is included in your Laravel application, which allows you to quickly customize the load balancers or proxies that should be trusted by your application. Your trusted proxies should be specified using the `trustProxies` middleware method in your application's `bootstrap/app.php` file:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->trustProxies(at: [




3        '192.168.1.1',




4        '10.0.0.0/8',




5    ]);




6})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->trustProxies(at: [
        '192.168.1.1',
        '10.0.0.0/8',
    ]);
})

```

In addition to configuring the trusted proxies, you may also configure the proxy headers that should be trusted:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->trustProxies(headers: Request::HEADER_X_FORWARDED_FOR |




3        Request::HEADER_X_FORWARDED_HOST |




4        Request::HEADER_X_FORWARDED_PORT |




5        Request::HEADER_X_FORWARDED_PROTO |




6        Request::HEADER_X_FORWARDED_AWS_ELB




7    );




8})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->trustProxies(headers: Request::HEADER_X_FORWARDED_FOR |
        Request::HEADER_X_FORWARDED_HOST |
        Request::HEADER_X_FORWARDED_PORT |
        Request::HEADER_X_FORWARDED_PROTO |
        Request::HEADER_X_FORWARDED_AWS_ELB
    );
})

```

If you are using AWS Elastic Load Balancing, the `headers` value should be `Request::HEADER_X_FORWARDED_AWS_ELB`. If your load balancer uses the standard `Forwarded` header from `headers` value should be `Request::HEADER_FORWARDED`. For more information on the constants that may be used in the `headers` value, check out Symfony's documentation on
#### [Trusting All Proxies](https://laravel.com/docs/12.x/requests#trusting-all-proxies)
If you are using Amazon AWS or another "cloud" load balancer provider, you may not know the IP addresses of your actual balancers. In this case, you may use `*` to trust all proxies:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->trustProxies(at: '*');




3})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->trustProxies(at: '*');
})

```

## [Configuring Trusted Hosts](https://laravel.com/docs/12.x/requests#configuring-trusted-hosts)
By default, Laravel will respond to all requests it receives regardless of the content of the HTTP request's `Host` header. In addition, the `Host` header's value will be used when generating absolute URLs to your application during a web request.
Typically, you should configure your web server, such as Nginx or Apache, to only send requests to your application that match a given hostname. However, if you do not have the ability to customize your web server directly and need to instruct Laravel to only respond to certain hostnames, you may do so by enabling the `Illuminate\Http\Middleware\TrustHosts` middleware for your application.
To enable the `TrustHosts` middleware, you should invoke the `trustHosts` middleware method in your application's `bootstrap/app.php` file. Using the `at` argument of this method, you may specify the hostnames that your application should respond to. The hostname string is treated as a regular expression. Incoming requests with other `Host` headers will be rejected:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->trustHosts(at: ['^laravel\.test$']);




3})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->trustHosts(at: ['^laravel\.test$']);
})

```

By default, requests coming from subdomains of the application's URL are also automatically trusted. If you would like to disable this behavior, you may use the `subdomains` argument:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->trustHosts(at: ['^laravel\.test$'], subdomains: false);




3})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->trustHosts(at: ['^laravel\.test$'], subdomains: false);
})

```

If you need to access your application's configuration files or database to determine your trusted hosts, you may provide a closure to the `at` argument:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->trustHosts(at: fn () => config('app.trusted_hosts'));




3})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->trustHosts(at: fn () => config('app.trusted_hosts'));
})

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/requests#introduction)
  * [ Interacting With The Request ](https://laravel.com/docs/12.x/requests#interacting-with-the-request)
    * [ Accessing the Request ](https://laravel.com/docs/12.x/requests#accessing-the-request)
    * [ Request Path, Host, and Method ](https://laravel.com/docs/12.x/requests#request-path-and-method)
    * [ Request Headers ](https://laravel.com/docs/12.x/requests#request-headers)
    * [ Request IP Address ](https://laravel.com/docs/12.x/requests#request-ip-address)
    * [ Content Negotiation ](https://laravel.com/docs/12.x/requests#content-negotiation)
    * [ PSR-7 Requests ](https://laravel.com/docs/12.x/requests#psr7-requests)
  * [ Input ](https://laravel.com/docs/12.x/requests#input)
    * [ Retrieving Input ](https://laravel.com/docs/12.x/requests#retrieving-input)
    * [ Input Presence ](https://laravel.com/docs/12.x/requests#input-presence)
    * [ Merging Additional Input ](https://laravel.com/docs/12.x/requests#merging-additional-input)
    * [ Old Input ](https://laravel.com/docs/12.x/requests#old-input)
    * [ Cookies ](https://laravel.com/docs/12.x/requests#cookies)
    * [ Input Trimming and Normalization ](https://laravel.com/docs/12.x/requests#input-trimming-and-normalization)
  * [ Files ](https://laravel.com/docs/12.x/requests#files)
    * [ Retrieving Uploaded Files ](https://laravel.com/docs/12.x/requests#retrieving-uploaded-files)
    * [ Storing Uploaded Files ](https://laravel.com/docs/12.x/requests#storing-uploaded-files)
  * [ Configuring Trusted Proxies ](https://laravel.com/docs/12.x/requests#configuring-trusted-proxies)
  * [ Configuring Trusted Hosts ](https://laravel.com/docs/12.x/requests#configuring-trusted-hosts)


[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [ More Partners ](https://partners.laravel.com)
