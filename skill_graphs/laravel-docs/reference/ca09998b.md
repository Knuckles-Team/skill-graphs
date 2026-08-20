## [Concurrent Requests](https://laravel.com/docs/12.x/http-client#concurrent-requests)
Sometimes, you may wish to make multiple HTTP requests concurrently. In other words, you want several requests to be dispatched at the same time instead of issuing the requests sequentially. This can lead to substantial performance improvements when interacting with slow HTTP APIs.
### [Request Pooling](https://laravel.com/docs/12.x/http-client#request-pooling)
Thankfully, you may accomplish this using the `pool` method. The `pool` method accepts a closure which receives an `Illuminate\Http\Client\Pool` instance, allowing you to easily add requests to the request pool for dispatching:
```


 1use Illuminate\Http\Client\Pool;




 2use Illuminate\Support\Facades\Http;




 3 



 4$responses = Http::pool(fn (Pool $pool) => [




 5    $pool->get('http://localhost/first'),




 6    $pool->get('http://localhost/second'),




 7    $pool->get('http://localhost/third'),




 8]);




 9 



10return $responses[0]->ok() &&




11       $responses[1]->ok() &&




12       $responses[2]->ok();




use Illuminate\Http\Client\Pool;
use Illuminate\Support\Facades\Http;

$responses = Http::pool(fn (Pool $pool) => [
    $pool->get('http://localhost/first'),
    $pool->get('http://localhost/second'),
    $pool->get('http://localhost/third'),
]);

return $responses[0]->ok() &&
       $responses[1]->ok() &&
       $responses[2]->ok();

```

As you can see, each response instance can be accessed based on the order it was added to the pool. If you wish, you can name the requests using the `as` method, which allows you to access the corresponding responses by name:
```


 1use Illuminate\Http\Client\Pool;




 2use Illuminate\Support\Facades\Http;




 3 



 4$responses = Http::pool(fn (Pool $pool) => [




 5    $pool->as('first')->get('http://localhost/first'),




 6    $pool->as('second')->get('http://localhost/second'),




 7    $pool->as('third')->get('http://localhost/third'),




 8]);




 9 



10return $responses['first']->ok();




use Illuminate\Http\Client\Pool;
use Illuminate\Support\Facades\Http;

$responses = Http::pool(fn (Pool $pool) => [
    $pool->as('first')->get('http://localhost/first'),
    $pool->as('second')->get('http://localhost/second'),
    $pool->as('third')->get('http://localhost/third'),
]);

return $responses['first']->ok();

```

The maximum concurrency of the request pool may be controlled by providing the `concurrency` argument to the `pool` method. This value determines the maximum number of HTTP requests that may be concurrently in-flight while processing the request pool:
```


1$responses = Http::pool(fn (Pool $pool) => [




2    // ...




3], concurrency: 5);




$responses = Http::pool(fn (Pool $pool) => [
    // ...
], concurrency: 5);

```

#### [Customizing Concurrent Requests](https://laravel.com/docs/12.x/http-client#customizing-concurrent-requests)
The `pool` method cannot be chained with other HTTP client methods such as the `withHeaders` or `middleware` methods. If you want to apply custom headers or middleware to pooled requests, you should configure those options on each request in the pool:
```


 1use Illuminate\Http\Client\Pool;




 2use Illuminate\Support\Facades\Http;




 3 



 4$headers = [




 5    'X-Example' => 'example',




 6];




 7 



 8$responses = Http::pool(fn (Pool $pool) => [




 9    $pool->withHeaders($headers)->get('http://laravel.test/test'),




10    $pool->withHeaders($headers)->get('http://laravel.test/test'),




11    $pool->withHeaders($headers)->get('http://laravel.test/test'),




12]);




use Illuminate\Http\Client\Pool;
use Illuminate\Support\Facades\Http;

$headers = [
    'X-Example' => 'example',
];

$responses = Http::pool(fn (Pool $pool) => [
    $pool->withHeaders($headers)->get('http://laravel.test/test'),
    $pool->withHeaders($headers)->get('http://laravel.test/test'),
    $pool->withHeaders($headers)->get('http://laravel.test/test'),
]);

```

### [Request Batching](https://laravel.com/docs/12.x/http-client#request-batching)
Another way of working with concurrent requests in Laravel is to use the `batch` method. Like the `pool` method, it accepts a closure which receives an `Illuminate\Http\Client\Batch` instance, allowing you to easily add requests to the request pool for dispatching, but it also allows you to define completion callbacks:
```


 1use Illuminate\Http\Client\Batch;




 2use Illuminate\Http\Client\ConnectionException;




 3use Illuminate\Http\Client\RequestException;




 4use Illuminate\Http\Client\Response;




 5use Illuminate\Support\Facades\Http;




 6 



 7$responses = Http::batch(fn (Batch $batch) => [




 8    $batch->get('http://localhost/first'),




 9    $batch->get('http://localhost/second'),




10    $batch->get('http://localhost/third'),




11])->before(function (Batch $batch) {




12    // The batch has been created but no requests have been initialized...




13})->progress(function (Batch $batch, int|string $key, Response $response) {




14    // An individual request has completed successfully...




15})->then(function (Batch $batch, array $results) {




16    // All requests completed successfully...




17})->catch(function (Batch $batch, int|string $key, Response|RequestException|ConnectionException $response) {




18    // Batch request failure detected...




19})->finally(function (Batch $batch, array $results) {




20    // The batch has finished executing...




21})->send();




use Illuminate\Http\Client\Batch;
use Illuminate\Http\Client\ConnectionException;
use Illuminate\Http\Client\RequestException;
use Illuminate\Http\Client\Response;
use Illuminate\Support\Facades\Http;

$responses = Http::batch(fn (Batch $batch) => [
    $batch->get('http://localhost/first'),
    $batch->get('http://localhost/second'),
    $batch->get('http://localhost/third'),
])->before(function (Batch $batch) {
    // The batch has been created but no requests have been initialized...
})->progress(function (Batch $batch, int|string $key, Response $response) {
    // An individual request has completed successfully...
})->then(function (Batch $batch, array $results) {
    // All requests completed successfully...
})->catch(function (Batch $batch, int|string $key, Response|RequestException|ConnectionException $response) {
    // Batch request failure detected...
})->finally(function (Batch $batch, array $results) {
    // The batch has finished executing...
})->send();

```

Like the `pool` method, you can use the `as` method to name your requests:
```


1$responses = Http::batch(fn (Batch $batch) => [




2    $batch->as('first')->get('http://localhost/first'),




3    $batch->as('second')->get('http://localhost/second'),




4    $batch->as('third')->get('http://localhost/third'),




5])->send();




$responses = Http::batch(fn (Batch $batch) => [
    $batch->as('first')->get('http://localhost/first'),
    $batch->as('second')->get('http://localhost/second'),
    $batch->as('third')->get('http://localhost/third'),
])->send();

```

After a `batch` is started by calling the `send` method, you can't add new requests to it. Trying to do so will result in a `Illuminate\Http\Client\BatchInProgressException` exception being thrown.
The maximum concurrency of the request batch may be controlled via the `concurrency` method. This value determines the maximum number of HTTP requests that may be concurrently in-flight while processing the request batch:
```


1$responses = Http::batch(fn (Batch $batch) => [




2    // ...




3])->concurrency(5)->send();




$responses = Http::batch(fn (Batch $batch) => [
    // ...
])->concurrency(5)->send();

```

#### [Inspecting Batches](https://laravel.com/docs/12.x/http-client#inspecting-batches)
The `Illuminate\Http\Client\Batch` instance that is provided to batch completion callbacks has a variety of properties and methods to assist you in interacting with and inspecting a given batch of requests:
```


 1// The number of requests assigned to the batch...




 2$batch->totalRequests;




 3 



 4// The number of requests that have not been processed yet...




 5$batch->pendingRequests;




 6 



 7// The number of requests that have failed...




 8$batch->failedRequests;




 9 



10// The number of requests that have been processed thus far...




11$batch->processedRequests();




12 



13// Indicates if the batch has finished executing...




14$batch->finished();




15 



16// Indicates if the batch has request failures...




17$batch->hasFailures();




// The number of requests assigned to the batch...
$batch->totalRequests;

// The number of requests that have not been processed yet...
$batch->pendingRequests;

// The number of requests that have failed...
$batch->failedRequests;

// The number of requests that have been processed thus far...
$batch->processedRequests();

// Indicates if the batch has finished executing...
$batch->finished();

// Indicates if the batch has request failures...
$batch->hasFailures();

```

#### [Deferring Batches](https://laravel.com/docs/12.x/http-client#deferring-batches)
When the `defer` method is invoked, the batch of requests is not executed immediately. Instead, Laravel will execute the batch after the current application request's HTTP response has been sent to the user, keeping your application feeling fast and responsive:
```


 1use Illuminate\Http\Client\Batch;




 2use Illuminate\Support\Facades\Http;




 3 



 4$responses = Http::batch(fn (Batch $batch) => [




 5    $batch->get('http://localhost/first'),




 6    $batch->get('http://localhost/second'),




 7    $batch->get('http://localhost/third'),




 8])->then(function (Batch $batch, array $results) {




 9    // All requests completed successfully...




10})->defer();




use Illuminate\Http\Client\Batch;
use Illuminate\Support\Facades\Http;

$responses = Http::batch(fn (Batch $batch) => [
    $batch->get('http://localhost/first'),
    $batch->get('http://localhost/second'),
    $batch->get('http://localhost/third'),
])->then(function (Batch $batch, array $results) {
    // All requests completed successfully...
})->defer();

```
