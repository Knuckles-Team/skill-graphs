## [Making Requests](https://laravel.com/docs/12.x/http-client#making-requests)
To make requests, you may use the `head`, `get`, `post`, `put`, `patch`, and `delete` methods provided by the `Http` facade. First, let's examine how to make a basic `GET` request to another URL:
```


1use Illuminate\Support\Facades\Http;




2 



3$response = Http::get('http://example.com');




use Illuminate\Support\Facades\Http;

$response = Http::get('http://example.com');

```

The `get` method returns an instance of `Illuminate\Http\Client\Response`, which provides a variety of methods that may be used to inspect the response:
```


 1$response->body() : string;




 2$response->json($key = null, $default = null) : mixed;




 3$response->object() : object;




 4$response->collect($key = null) : Illuminate\Support\Collection;




 5$response->resource() : resource;




 6$response->status() : int;




 7$response->successful() : bool;




 8$response->redirect(): bool;




 9$response->failed() : bool;




10$response->clientError() : bool;




11$response->header($header) : string;




12$response->headers() : array;




$response->body() : string;
$response->json($key = null, $default = null) : mixed;
$response->object() : object;
$response->collect($key = null) : Illuminate\Support\Collection;
$response->resource() : resource;
$response->status() : int;
$response->successful() : bool;
$response->redirect(): bool;
$response->failed() : bool;
$response->clientError() : bool;
$response->header($header) : string;
$response->headers() : array;

```

The `Illuminate\Http\Client\Response` object also implements the PHP `ArrayAccess` interface, allowing you to access JSON response data directly on the response:
```


1return Http::get('http://example.com/users/1')['name'];




return Http::get('http://example.com/users/1')['name'];

```

In addition to the response methods listed above, the following methods may be used to determine if the response has a specific status code:
```


 1$response->ok() : bool;                  // 200 OK




 2$response->created() : bool;             // 201 Created




 3$response->accepted() : bool;            // 202 Accepted




 4$response->noContent() : bool;           // 204 No Content




 5$response->movedPermanently() : bool;    // 301 Moved Permanently




 6$response->found() : bool;               // 302 Found




 7$response->badRequest() : bool;          // 400 Bad Request




 8$response->unauthorized() : bool;        // 401 Unauthorized




 9$response->paymentRequired() : bool;     // 402 Payment Required




10$response->forbidden() : bool;           // 403 Forbidden




11$response->notFound() : bool;            // 404 Not Found




12$response->requestTimeout() : bool;      // 408 Request Timeout




13$response->conflict() : bool;            // 409 Conflict




14$response->unprocessableEntity() : bool; // 422 Unprocessable Entity




15$response->tooManyRequests() : bool;     // 429 Too Many Requests




16$response->serverError() : bool;         // 500 Internal Server Error




$response->ok() : bool;                  // 200 OK
$response->created() : bool;             // 201 Created
$response->accepted() : bool;            // 202 Accepted
$response->noContent() : bool;           // 204 No Content
$response->movedPermanently() : bool;    // 301 Moved Permanently
$response->found() : bool;               // 302 Found
$response->badRequest() : bool;          // 400 Bad Request
$response->unauthorized() : bool;        // 401 Unauthorized
$response->paymentRequired() : bool;     // 402 Payment Required
$response->forbidden() : bool;           // 403 Forbidden
$response->notFound() : bool;            // 404 Not Found
$response->requestTimeout() : bool;      // 408 Request Timeout
$response->conflict() : bool;            // 409 Conflict
$response->unprocessableEntity() : bool; // 422 Unprocessable Entity
$response->tooManyRequests() : bool;     // 429 Too Many Requests
$response->serverError() : bool;         // 500 Internal Server Error

```

#### [URI Templates](https://laravel.com/docs/12.x/http-client#uri-templates)
The HTTP client also allows you to construct request URLs using the `withUrlParameters` method:
```


1Http::withUrlParameters([




2    'endpoint' => 'https://laravel.com',




3    'page' => 'docs',




4    'version' => '12.x',




5    'topic' => 'validation',




6])->get('{+endpoint}/{page}/{version}/{topic}');




Http::withUrlParameters([
    'endpoint' => 'https://laravel.com',
    'page' => 'docs',
    'version' => '12.x',
    'topic' => 'validation',
])->get('{+endpoint}/{page}/{version}/{topic}');

```

#### [Dumping Requests](https://laravel.com/docs/12.x/http-client#dumping-requests)
If you would like to dump the outgoing request instance before it is sent and terminate the script's execution, you may add the `dd` method to the beginning of your request definition:
```


1return Http::dd()->get('http://example.com');




return Http::dd()->get('http://example.com');

```

### [Request Data](https://laravel.com/docs/12.x/http-client#request-data)
Of course, it is common when making `POST`, `PUT`, and `PATCH` requests to send additional data with your request, so these methods accept an array of data as their second argument. By default, data will be sent using the `application/json` content type:
```


1use Illuminate\Support\Facades\Http;




2 



3$response = Http::post('http://example.com/users', [




4    'name' => 'Steve',




5    'role' => 'Network Administrator',




6]);




use Illuminate\Support\Facades\Http;

$response = Http::post('http://example.com/users', [
    'name' => 'Steve',
    'role' => 'Network Administrator',
]);

```

#### [GET Request Query Parameters](https://laravel.com/docs/12.x/http-client#get-request-query-parameters)
When making `GET` requests, you may either append a query string to the URL directly or pass an array of key / value pairs as the second argument to the `get` method:
```


1$response = Http::get('http://example.com/users', [




2    'name' => 'Taylor',




3    'page' => 1,




4]);




$response = Http::get('http://example.com/users', [
    'name' => 'Taylor',
    'page' => 1,
]);

```

Alternatively, the `withQueryParameters` method may be used:
```


1Http::retry(3, 100)->withQueryParameters([




2    'name' => 'Taylor',




3    'page' => 1,




4])->get('http://example.com/users');




Http::retry(3, 100)->withQueryParameters([
    'name' => 'Taylor',
    'page' => 1,
])->get('http://example.com/users');

```

#### [Sending Form URL Encoded Requests](https://laravel.com/docs/12.x/http-client#sending-form-url-encoded-requests)
If you would like to send data using the `application/x-www-form-urlencoded` content type, you should call the `asForm` method before making your request:
```


1$response = Http::asForm()->post('http://example.com/users', [




2    'name' => 'Sara',




3    'role' => 'Privacy Consultant',




4]);




$response = Http::asForm()->post('http://example.com/users', [
    'name' => 'Sara',
    'role' => 'Privacy Consultant',
]);

```

#### [Sending a Raw Request Body](https://laravel.com/docs/12.x/http-client#sending-a-raw-request-body)
You may use the `withBody` method if you would like to provide a raw request body when making a request. The content type may be provided via the method's second argument:
```


1$response = Http::withBody(




2    base64_encode($photo), 'image/jpeg'




3)->post('http://example.com/photo');




$response = Http::withBody(
    base64_encode($photo), 'image/jpeg'
)->post('http://example.com/photo');

```

#### [Multi-Part Requests](https://laravel.com/docs/12.x/http-client#multi-part-requests)
If you would like to send files as multi-part requests, you should call the `attach` method before making your request. This method accepts the name of the file and its contents. If needed, you may provide a third argument which will be considered the file's filename, while a fourth argument may be used to provide headers associated with the file:
```


1$response = Http::attach(




2    'attachment', file_get_contents('photo.jpg'), 'photo.jpg', ['Content-Type' => 'image/jpeg']




3)->post('http://example.com/attachments');




$response = Http::attach(
    'attachment', file_get_contents('photo.jpg'), 'photo.jpg', ['Content-Type' => 'image/jpeg']
)->post('http://example.com/attachments');

```

Instead of passing the raw contents of a file, you may pass a stream resource:
```


1$photo = fopen('photo.jpg', 'r');




2 



3$response = Http::attach(




4    'attachment', $photo, 'photo.jpg'




5)->post('http://example.com/attachments');




$photo = fopen('photo.jpg', 'r');

$response = Http::attach(
    'attachment', $photo, 'photo.jpg'
)->post('http://example.com/attachments');

```

### [Headers](https://laravel.com/docs/12.x/http-client#headers)
Headers may be added to requests using the `withHeaders` method. This `withHeaders` method accepts an array of key / value pairs:
```


1$response = Http::withHeaders([




2    'X-First' => 'foo',




3    'X-Second' => 'bar'




4])->post('http://example.com/users', [




5    'name' => 'Taylor',




6]);




$response = Http::withHeaders([
    'X-First' => 'foo',
    'X-Second' => 'bar'
])->post('http://example.com/users', [
    'name' => 'Taylor',
]);

```

You may use the `accept` method to specify the content type that your application is expecting in response to your request:
```


1$response = Http::accept('application/json')->get('http://example.com/users');




$response = Http::accept('application/json')->get('http://example.com/users');

```

For convenience, you may use the `acceptJson` method to quickly specify that your application expects the `application/json` content type in response to your request:
```


1$response = Http::acceptJson()->get('http://example.com/users');




$response = Http::acceptJson()->get('http://example.com/users');

```

The `withHeaders` method merges new headers into the request's existing headers. If needed, you may replace all of the headers entirely using the `replaceHeaders` method:
```


1$response = Http::withHeaders([




2    'X-Original' => 'foo',




3])->replaceHeaders([




4    'X-Replacement' => 'bar',




5])->post('http://example.com/users', [




6    'name' => 'Taylor',




7]);




$response = Http::withHeaders([
    'X-Original' => 'foo',
])->replaceHeaders([
    'X-Replacement' => 'bar',
])->post('http://example.com/users', [
    'name' => 'Taylor',
]);

```

### [Authentication](https://laravel.com/docs/12.x/http-client#authentication)
You may specify basic and digest authentication credentials using the `withBasicAuth` and `withDigestAuth` methods, respectively:
```


1// Basic authentication...




2$response = Http::withBasicAuth('taylor@laravel.com', 'secret')->post(/* ... */);




3 



4// Digest authentication...




5$response = Http::withDigestAuth('taylor@laravel.com', 'secret')->post(/* ... */);




// Basic authentication...
$response = Http::withBasicAuth('taylor@laravel.com', 'secret')->post(/* ... */);

// Digest authentication...
$response = Http::withDigestAuth('taylor@laravel.com', 'secret')->post(/* ... */);

```

#### [Bearer Tokens](https://laravel.com/docs/12.x/http-client#bearer-tokens)
If you would like to quickly add a bearer token to the request's `Authorization` header, you may use the `withToken` method:
```


1$response = Http::withToken('token')->post(/* ... */);




$response = Http::withToken('token')->post(/* ... */);

```

### [Timeout](https://laravel.com/docs/12.x/http-client#timeout)
The `timeout` method may be used to specify the maximum number of seconds to wait for a response. By default, the HTTP client will timeout after 30 seconds:
```


1$response = Http::timeout(3)->get(/* ... */);




$response = Http::timeout(3)->get(/* ... */);

```

If the given timeout is exceeded, an instance of `Illuminate\Http\Client\ConnectionException` will be thrown.
You may specify the maximum number of seconds to wait while trying to connect to a server using the `connectTimeout` method. The default is 10 seconds:
```


1$response = Http::connectTimeout(3)->get(/* ... */);




$response = Http::connectTimeout(3)->get(/* ... */);

```

### [Retries](https://laravel.com/docs/12.x/http-client#retries)
If you would like the HTTP client to automatically retry the request if a client or server error occurs, you may use the `retry` method. The `retry` method accepts the maximum number of times the request should be attempted and the number of milliseconds that Laravel should wait in between attempts:
```


1$response = Http::retry(3, 100)->post(/* ... */);




$response = Http::retry(3, 100)->post(/* ... */);

```

If you would like to manually calculate the number of milliseconds to sleep between attempts, you may pass a closure as the second argument to the `retry` method:
```


1use Exception;




2 



3$response = Http::retry(3, function (int $attempt, Exception $exception) {




4    return $attempt * 100;




5})->post(/* ... */);




use Exception;

$response = Http::retry(3, function (int $attempt, Exception $exception) {
    return $attempt * 100;
})->post(/* ... */);

```

For convenience, you may also provide an array as the first argument to the `retry` method. This array will be used to determine how many milliseconds to sleep between subsequent attempts:
```


1$response = Http::retry([100, 200])->post(/* ... */);




$response = Http::retry([100, 200])->post(/* ... */);

```

If needed, you may pass a third argument to the `retry` method. The third argument should be a callable that determines if the retries should actually be attempted. For example, you may wish to only retry the request if the initial request encounters an `ConnectionException`:
```


1use Illuminate\Http\Client\PendingRequest;




2use Throwable;




3 



4$response = Http::retry(3, 100, function (Throwable $exception, PendingRequest $request) {




5    return $exception instanceof ConnectionException;




6})->post(/* ... */);




use Illuminate\Http\Client\PendingRequest;
use Throwable;

$response = Http::retry(3, 100, function (Throwable $exception, PendingRequest $request) {
    return $exception instanceof ConnectionException;
})->post(/* ... */);

```

If a request attempt fails, you may wish to make a change to the request before a new attempt is made. You can achieve this by modifying the request argument provided to the callable you provided to the `retry` method. For example, you might want to retry the request with a new authorization token if the first attempt returned an authentication error:
```


 1use Illuminate\Http\Client\PendingRequest;




 2use Illuminate\Http\Client\RequestException;




 3use Throwable;




 4 



 5$response = Http::withToken($this->getToken())->retry(2, 0, function (Throwable $exception, PendingRequest $request) {




 6    if (! $exception instanceof RequestException || $exception->response->status() !== 401) {




 7        return false;




 8    }




 9 



10    $request->withToken($this->getNewToken());




11 



12    return true;




13})->post(/* ... */);




use Illuminate\Http\Client\PendingRequest;
use Illuminate\Http\Client\RequestException;
use Throwable;

$response = Http::withToken($this->getToken())->retry(2, 0, function (Throwable $exception, PendingRequest $request) {
    if (! $exception instanceof RequestException || $exception->response->status() !== 401) {
        return false;
    }

    $request->withToken($this->getNewToken());

    return true;
})->post(/* ... */);

```

If all of the requests fail, an instance of `Illuminate\Http\Client\RequestException` will be thrown. If you would like to disable this behavior, you may provide a `throw` argument with a value of `false`. When disabled, the last response received by the client will be returned after all retries have been attempted:
```


1$response = Http::retry(3, 100, throw: false)->post(/* ... */);




$response = Http::retry(3, 100, throw: false)->post(/* ... */);

```

If all of the requests fail because of a connection issue, a `Illuminate\Http\Client\ConnectionException` will still be thrown even when the `throw` argument is set to `false`.
### [Error Handling](https://laravel.com/docs/12.x/http-client#error-handling)
Unlike Guzzle's default behavior, Laravel's HTTP client wrapper does not throw exceptions on client or server errors (`400` and `500` level responses from servers). You may determine if one of these errors was returned using the `successful`, `clientError`, or `serverError` methods:
```


 1// Determine if the status code is >= 200 and < 300...




 2$response->successful();




 3 



 4// Determine if the status code is >= 400...




 5$response->failed();




 6 



 7// Determine if the response has a 400 level status code...




 8$response->clientError();




 9 



10// Determine if the response has a 500 level status code...




11$response->serverError();




12 



13// Immediately execute the given callback if there was a client or server error...




14$response->onError(callable $callback);




// Determine if the status code is >= 200 and < 300...
$response->successful();

// Determine if the status code is >= 400...
$response->failed();

// Determine if the response has a 400 level status code...
$response->clientError();

// Determine if the response has a 500 level status code...
$response->serverError();

// Immediately execute the given callback if there was a client or server error...
$response->onError(callable $callback);

```

#### [Throwing Exceptions](https://laravel.com/docs/12.x/http-client#throwing-exceptions)
If you have a response instance and would like to throw an instance of `Illuminate\Http\Client\RequestException` if the response status code indicates a client or server error, you may use the `throw` or `throwIf` methods:
```


 1use Illuminate\Http\Client\Response;




 2 



 3$response = Http::post(/* ... */);




 4 



 5// Throw an exception if a client or server error occurred...




 6$response->throw();




 7 



 8// Throw an exception if an error occurred and the given condition is true...




 9$response->throwIf($condition);




10 



11// Throw an exception if an error occurred and the given closure resolves to true...




12$response->throwIf(fn (Response $response) => true);




13 



14// Throw an exception if an error occurred and the given condition is false...




15$response->throwUnless($condition);




16 



17// Throw an exception if an error occurred and the given closure resolves to false...




18$response->throwUnless(fn (Response $response) => false);




19 



20// Throw an exception if the response has a specific status code...




21$response->throwIfStatus(403);




22 



23// Throw an exception unless the response has a specific status code...




24$response->throwUnlessStatus(200);




25 



26return $response['user']['id'];




use Illuminate\Http\Client\Response;

$response = Http::post(/* ... */);

// Throw an exception if a client or server error occurred...
$response->throw();

// Throw an exception if an error occurred and the given condition is true...
$response->throwIf($condition);

// Throw an exception if an error occurred and the given closure resolves to true...
$response->throwIf(fn (Response $response) => true);

// Throw an exception if an error occurred and the given condition is false...
$response->throwUnless($condition);

// Throw an exception if an error occurred and the given closure resolves to false...
$response->throwUnless(fn (Response $response) => false);

// Throw an exception if the response has a specific status code...
$response->throwIfStatus(403);

// Throw an exception unless the response has a specific status code...
$response->throwUnlessStatus(200);

return $response['user']['id'];

```

The `Illuminate\Http\Client\RequestException` instance has a public `$response` property which will allow you to inspect the returned response.
The `throw` method returns the response instance if no error occurred, allowing you to chain other operations onto the `throw` method:
```


1return Http::post(/* ... */)->throw()->json();




return Http::post(/* ... */)->throw()->json();

```

If you would like to perform some additional logic before the exception is thrown, you may pass a closure to the `throw` method. The exception will be thrown automatically after the closure is invoked, so you do not need to re-throw the exception from within the closure:
```


1use Illuminate\Http\Client\Response;




2use Illuminate\Http\Client\RequestException;




3 



4return Http::post(/* ... */)->throw(function (Response $response, RequestException $e) {




5    // ...




6})->json();




use Illuminate\Http\Client\Response;
use Illuminate\Http\Client\RequestException;

return Http::post(/* ... */)->throw(function (Response $response, RequestException $e) {
    // ...
})->json();

```

By default, `RequestException` messages are truncated to 120 characters when logged or reported. To customize or disable this behavior, you may utilize the `truncateAt` and `dontTruncate` methods when configuring your application's registered behavior in your `bootstrap/app.php` file:
```


1use Illuminate\Http\Client\RequestException;




2 



3->registered(function (): void {




4    // Truncate request exception messages to 240 characters...




5    RequestException::truncateAt(240);




6 



7    // Disable request exception message truncation...




8    RequestException::dontTruncate();




9})




use Illuminate\Http\Client\RequestException;

->registered(function (): void {
    // Truncate request exception messages to 240 characters...
    RequestException::truncateAt(240);

    // Disable request exception message truncation...
    RequestException::dontTruncate();
})

```

Alternatively, you may customize the exception truncation behavior per request using the `truncateExceptionsAt` method:
```


1return Http::truncateExceptionsAt(240)->post(/* ... */);




return Http::truncateExceptionsAt(240)->post(/* ... */);

```

### [Guzzle Middleware](https://laravel.com/docs/12.x/http-client#guzzle-middleware)
Since Laravel's HTTP client is powered by Guzzle, you may take advantage of `withRequestMiddleware` method:
```


1use Illuminate\Support\Facades\Http;




2use Psr\Http\Message\RequestInterface;




3 



4$response = Http::withRequestMiddleware(




5    function (RequestInterface $request) {




6        return $request->withHeader('X-Example', 'Value');




7    }




8)->get('http://example.com');




use Illuminate\Support\Facades\Http;
use Psr\Http\Message\RequestInterface;

$response = Http::withRequestMiddleware(
    function (RequestInterface $request) {
        return $request->withHeader('X-Example', 'Value');
    }
)->get('http://example.com');

```

Likewise, you can inspect the incoming HTTP response by registering a middleware via the `withResponseMiddleware` method:
```


 1use Illuminate\Support\Facades\Http;




 2use Psr\Http\Message\ResponseInterface;




 3 



 4$response = Http::withResponseMiddleware(




 5    function (ResponseInterface $response) {




 6        $header = $response->getHeader('X-Example');




 7 



 8        // ...




 9 



10        return $response;




11    }




12)->get('http://example.com');




use Illuminate\Support\Facades\Http;
use Psr\Http\Message\ResponseInterface;

$response = Http::withResponseMiddleware(
    function (ResponseInterface $response) {
        $header = $response->getHeader('X-Example');

        // ...

        return $response;
    }
)->get('http://example.com');

```

#### [Global Middleware](https://laravel.com/docs/12.x/http-client#global-middleware)
Sometimes, you may want to register a middleware that applies to every outgoing request and incoming response. To accomplish this, you may use the `globalRequestMiddleware` and `globalResponseMiddleware` methods. Typically, these methods should be invoked in the `boot` method of your application's `AppServiceProvider`:
```


1use Illuminate\Support\Facades\Http;




2 



3Http::globalRequestMiddleware(fn ($request) => $request->withHeader(




4    'User-Agent', 'Example Application/1.0'




5));




6 



7Http::globalResponseMiddleware(fn ($response) => $response->withHeader(




8    'X-Finished-At', now()->toDateTimeString()




9));




use Illuminate\Support\Facades\Http;

Http::globalRequestMiddleware(fn ($request) => $request->withHeader(
    'User-Agent', 'Example Application/1.0'
));

Http::globalResponseMiddleware(fn ($response) => $response->withHeader(
    'X-Finished-At', now()->toDateTimeString()
));

```

### [Guzzle Options](https://laravel.com/docs/12.x/http-client#guzzle-options)
You may specify additional `withOptions` method. The `withOptions` method accepts an array of key / value pairs:
```


1$response = Http::withOptions([




2    'debug' => true,




3])->get('http://example.com/users');




$response = Http::withOptions([
    'debug' => true,
])->get('http://example.com/users');

```

#### [Global Options](https://laravel.com/docs/12.x/http-client#global-options)
To configure default options for every outgoing request, you may utilize the `globalOptions` method. Typically, this method should be invoked from the `boot` method of your application's `AppServiceProvider`:
```


 1use Illuminate\Support\Facades\Http;




 2 



 3/**




 4 * Bootstrap any application services.




 5 */




 6public function boot(): void




 7{




 8    Http::globalOptions([




 9        'allow_redirects' => false,




10    ]);




11}




use Illuminate\Support\Facades\Http;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Http::globalOptions([
        'allow_redirects' => false,
    ]);
}

```
