## Laravel Framework 12.x
### Add Support for `temporaryUploadUrl` to the `local` Filesystem
Pull request by
You can now generate [temporary upload URLs](https://laravel.com/docs/filesystem#temporary-upload-urls) even when you're using the `local` driver, making it much easier to build consistent upload flows across local, staging, and production environments.
```


1use Illuminate\Support\Facades\Storage;




2 



3$url = Storage::disk('local')->temporaryUploadUrl(




4    'uploads/incoming/video.mp4',




5    now()->addMinutes(10),




6    ['Content-Type' => 'video/mp4']




7);




use Illuminate\Support\Facades\Storage;

$url = Storage::disk('local')->temporaryUploadUrl(
    'uploads/incoming/video.mp4',
    now()->addMinutes(10),
    ['Content-Type' => 'video/mp4']
);

```

### [12.x] Add `makeMany` Method to Factory
Pull request by
`makeMany()` gives you a clean, expressive way to generate multiple in-memory model instances without persisting anything. It's ideal for tests, previews, and shaping data before a write.
```


1$users = User::factory()->makeMany(3);




2 



3$payload = $users->map->only(['name', 'email']);




$users = User::factory()->makeMany(3);

$payload = $users->map->only(['name', 'email']);

```

### [12.x] Allow Closures for Values in `firstOrCreate` and `createOrFirst`
Pull request by
You can now lazily compute attribute values only when a record is actually being created. That means fewer unnecessary queries and less wasted work when the model already exists.
```


1$location = Location::firstOrCreate(




2    ['address' => $address],




3    fn () => ['coordinates' => Geocoder::resolve($address)],




4);




$location = Location::firstOrCreate(
    ['address' => $address],
    fn () => ['coordinates' => Geocoder::resolve($address)],
);

```

### [12.x] Support `afterSending` Method on Notification
Pull request by
`afterSending()` lets you hook into the lifecycle after a [notification](https://laravel.com/docs/notifications) is dispatched, which is perfect for audit logging, metrics, or cleanup work without cluttering your notification channels.
```


 1class BookingNotification extends Notification




 2{




 3    public function __construct(




 4        public Booking $booking;




 5    ) {




 6        //




 7    }




 8 



 9    public function via()




10    {




11        return ['mail'];




12    }




13 



14    public function toMail()




15    {




16        // ...




17    }




18 



19    public function afterSending($notifiable, $channel, $response)




20    {




21        $this->booking->update(['notified_at' => now()]);




22    }




23}




class BookingNotification extends Notification
{
    public function __construct(
        public Booking $booking;
    ) {
        //
    }

    public function via()
    {
        return ['mail'];
    }

    public function toMail()
    {
        // ...
    }

    public function afterSending($notifiable, $channel, $response)
    {
        $this->booking->update(['notified_at' => now()]);
    }
}

```

### [12.x] Add `whenFails` and `whenPasses` Methods on `Validator`
Pull request by
These helpers are particularly useful when you use the validator to validate data outside the request cycle where the error would not get picked up automatically by the HTTP handler.
```


1Validator::make(




2    ['file' => $file],




3    ['file' => 'required|image|dimensions:min_width=100,min_height=200']




4)->whenFails(function () {




5    throw new InvalidArgumentException('Provided file is invalid');




6});




Validator::make(
    ['file' => $file],
    ['file' => 'required|image|dimensions:min_width=100,min_height=200']
)->whenFails(function () {
    throw new InvalidArgumentException('Provided file is invalid');
});

```

### [12.x] Add `withoutheader` Method to Response
Pull request by
Removing headers is now straightforward with `withoutHeader()`, which is handy when you need to strip inherited headers (like caching or debug headers) before returning a [response](https://laravel.com/docs/responses).
```


1return response($content)->withoutHeader('X-Debug');




return response($content)->withoutHeader('X-Debug');

```

### [12.x] Exclude Decorative ASCII Art SVG from Exception Page in Non-Browser Contexts
Pull request by
Console and non-browser contexts no longer receive the decorative ASCII SVG payload, keeping error output cleaner in logs, CI, agent, and API responses. Furthermore...
### [12.x] Use JS to Create the Laravel ASCII SVG Logo on the Fly
Pull request by
The exception page ASCII SVG is now generated on the fly with JavaScript, keeping output leaner and better suited to different rendering contexts.
### [12.x] Add Typed Getters on Cache
Pull request by
Typed cache getters reduce repetitive casting and make intent obvious when reading cached values, helping you avoid subtle bugs from unexpected types.
```


1$count = Cache::integer('downloads.count', 0);




2$enabled = Cache::boolean('features.new_checkout', false);




$count = Cache::integer('downloads.count', 0);
$enabled = Cache::boolean('features.new_checkout', false);

```

### [12.x] Add `InteractsWithData::clamp()`
Pull request by
A `clamp()` method has been added to the `InteractsWithData` trait, giving you a tidy way to bound numeric input values, which is great for pagination, limits, sliders, and any user-controlled numbers.
```


1// Instead of:




2/** @var int<PHP_INT_MIN, PHP_INT_MAX> $perPage */




3$perPage = request()->integer('per_page', 50);




4 



5// You can now do:




6/** @var int<1, 100> $perPage */




7$perPage = request()->clamp('per_page', 1, 100, 50);




// Instead of:
/** @var int<PHP_INT_MIN, PHP_INT_MAX> $perPage */
$perPage = request()->integer('per_page', 50);

// You can now do:
/** @var int<1, 100> $perPage */
$perPage = request()->clamp('per_page', 1, 100, 50);

```

## Laravel Framework 12.x
### [12.x] Add `@includeIsolated` Directive for Isolated Blade Includes
Pull request by
When you need to reuse a partial without accidentally leaking variables in (or out), `@includeIsolated` gives you a clean, predictable boundary - great for shared UI components and emails where "mystery data" can be costly to debug.
```


1{{-- Only receives what you pass explicitly --}}




2@includeIsolated("partials.alert", ["type" => "success", "message" => $message])




{{-- Only receives what you pass explicitly --}}
@includeIsolated("partials.alert", ["type" => "success", "message" => $message])

```

### [12.x] Add `Cache::withoutOverlapping()` to Wrap `Cache::lock()->block()`
Pull request by
This adds a tidy, expressive wrapper around cache locks, so you can prevent overlapping work with less boilerplate. Perfect for cron jobs, report generation, and any "only one at a time" tasks.
```


1Cache::withoutOverlapping('reports:daily')




2    ->block(10, function () {




3        // This work will not run concurrently.




4        GenerateDailyReport::run();




5    });




Cache::withoutOverlapping('reports:daily')
    ->block(10, function () {
        // This work will not run concurrently.
        GenerateDailyReport::run();
    });

```

### Support for Vector Embeddings in the Database
Pull request by
This work moves Laravel's "vector" capabilities forward, helping set the stage for richer integrations and smoother workflows when dealing with embeddings and similarity search. If you're exploring AI-powered features, this one's for you.
### [12.x] Add `Collection::containsManyItems()` Method
Pull request by
A new `containsManyItems` method was added to complement the existing `containsOneItem`, enabling you to do a quick check to see if a collection contains two or more items.
```


1match (true) {




2    $collection->isEmpty() => '...',




3    $collection->containsOneItem() => '...',




4    $collection->containsManyItems() => '...',




5};




match (true) {
    $collection->isEmpty() => '...',
    $collection->containsOneItem() => '...',
    $collection->containsManyItems() => '...',
};

```

### [12.x] `JSON:API` Resource
Pull request by
This introduces JSON:API resource support, making it easier to ship standards-compliant APIs with consistent structure across teams and services. If you're standardizing responses (or integrating with clients that expect JSON:API), this helps reduce custom formatting and makes your API surface more predictable.
### [12.x] Add `BackedEnum` Support for Session Keys
Pull request by
You can now use backed enums as [session keys](https://laravel.com/docs/session), which keeps key names centralized and typo-proof, especially helpful in larger apps where session keys tend to spread over time.
```


1enum CheckoutSession: string




2{




3    case Cart = 'checkout.cart';




4    case ShippingAddress = 'checkout.shipping_address';




5    case PaymentMethod = 'checkout.payment_method';




6}




7 



8session()->put(CheckoutSession::Cart, $items);




9session()->get(CheckoutSession::Cart);




enum CheckoutSession: string
{
    case Cart = 'checkout.cart';
    case ShippingAddress = 'checkout.shipping_address';
    case PaymentMethod = 'checkout.payment_method';
}

session()->put(CheckoutSession::Cart, $items);
session()->get(CheckoutSession::Cart);

```

### [12.x] Allow `BackedEnum` for Cache Keys
Pull request by
Same productivity boost, now for cache: backed enums can be used as [cache keys](https://laravel.com/docs/cache), helping you standardize key naming and avoid subtle collisions. Great fit for teams that want a single source of truth for cache identifiers.
```


1enum CacheKey: string




2{




3    case Settings = 'settings.global';




4}




5 



6Cache::put(CacheKey::Settings, $settings, now()->addHour());




7 



8$settings = Cache::get(CacheKey::Settings);




enum CacheKey: string
{
    case Settings = 'settings.global';
}

Cache::put(CacheKey::Settings, $settings, now()->addHour());

$settings = Cache::get(CacheKey::Settings);

```

### [12.x] Add `--readable` Flag to `env:encrypt` for Visible Key Names
Pull request by
A practical quality-of-life improvement: `--readable` makes encrypted env output easier to audit by keeping key names visible, which helps during reviews and incident response while still protecting secret values. If you're hardening deployments, this pairs nicely with Laravel's [environment encryption](https://laravel.com/docs/configuration#encrypting-environment-files) workflow.
```


1php artisan env:encrypt --readable




php artisan env:encrypt --readable

```

## Laravel Framework 12.x
### [12.x] Add Ability to Run Callbacks After Building an HTTP Response
Pull request by
A new `afterResponse` method was added to the [HTTP Client](https://laravel.com/docs/http-client), which allows the user to inspect and mutate the response returned from an HTTP call:
```


 1Http::acceptJson()




 2    ->withHeader('X-Shopify-Access-Token', $credentials->token)




 3    ->baseUrl("https://{$credentials->shop_domain}.myshopify.com/admin/api/2025-10/")




 4    ->afterResponse(




 5        // Report any deprecation notices that were in the header




 6        function (Response $response) use ($credentials) {




 7            if ($header = $response->header('X-Shopify-API-Deprecated-Reason')) {




 8                event(new ShopifyDeprecationNotice($credentials->shop, $header));




 9            }




10        })




11    ->afterResponse(




12        // Map the response into our own custom response class




13        fn (Response $response) => new ShopifyResponse($response->toPsrResponse()),




14    )




15    ->afterResponse(




16        // Report the cost of the query




17        static fn (ShopifyResponse $response) => QueryCostResponse::report(




18            $response->getQueryCost(),




19            $credentials->shop




20        ),




21    );




Http::acceptJson()
    ->withHeader('X-Shopify-Access-Token', $credentials->token)
    ->baseUrl("https://{$credentials->shop_domain}.myshopify.com/admin/api/2025-10/")
    ->afterResponse(
        // Report any deprecation notices that were in the header
        function (Response $response) use ($credentials) {
            if ($header = $response->header('X-Shopify-API-Deprecated-Reason')) {
                event(new ShopifyDeprecationNotice($credentials->shop, $header));
            }
        })
    ->afterResponse(
        // Map the response into our own custom response class
        fn (Response $response) => new ShopifyResponse($response->toPsrResponse()),
    )
    ->afterResponse(
        // Report the cost of the query
        static fn (ShopifyResponse $response) => QueryCostResponse::report(
            $response->getQueryCost(),
            $credentials->shop
        ),
    );

```

### [12.x] Introduce `FluentPromise` to Allow for Cleaner Chaining in Pool
Pull request by
Userland chaining in [`Http::pool`](https://laravel.com/docs/http-client#request-pooling) is now possible with the introduction of `FluentPromise`. Previously, the chain would return the original response, limiting flexibility. With this change, users can access the underlying array and return whatever they wish:
```


 1$response = Http::pool(function (Pool $pool) {




 2    $pool->as('cosmatech')




 3        ->get('https://cosmastech.com')




 4        ->then(




 5            fn ($response) => strlen($response->body())




 6        );




 7    $pool->as('laravel')




 8        ->get('https://laravel.com')




 9        ->then(




10            fn ($response) => strlen($response->body())




11        );




12});




13 



14/*




15array:2 [




16  "cosmatech" => 9095




17  "laravel" => 1422023




18]




19*/




$response = Http::pool(function (Pool $pool) {
    $pool->as('cosmatech')
        ->get('https://cosmastech.com')
        ->then(
            fn ($response) => strlen($response->body())
        );
    $pool->as('laravel')
        ->get('https://laravel.com')
        ->then(
            fn ($response) => strlen($response->body())
        );
});

/*
array:2 [
  "cosmatech" => 9095
  "laravel" => 1422023
]
*/

```

### Introduce `lazy` Object and `proxy` Object Support Helpers
Pull request by
Two new helpers, `lazy` and `proxy`, were added to make PHP's new
```


 1<?php




 2 



 3use Illuminate\Support\Facades\Http;




 4use Vendor\Facades\ResultFactory;




 5use Vendor\Result;




 6use function Illuminate\Support\lazy;




 7use function Illuminate\Support\proxy;




 8 



 9$response = Http::get(...);




10 



11$instance = lazy(Result::class, fn () => [$response->json()]);




12$instance = proxy(Result::class, fn (): Result => ResultFactory::make($response->json()));




<?php

use Illuminate\Support\Facades\Http;
use Vendor\Facades\ResultFactory;
use Vendor\Result;
use function Illuminate\Support\lazy;
use function Illuminate\Support\proxy;

$response = Http::get(...);

$instance = lazy(Result::class, fn () => [$response->json()]);
$instance = proxy(Result::class, fn (): Result => ResultFactory::make($response->json()));

```

### [12.x] Add Reload Command and Allow Services to Register
Pull request by
A new `php artisan reload` command was introduced, allowing service providers to add their own commands for reloading. This makes it easier for services to specify one command to include in their deployment steps after the deployment is completed.
The applicable reload commands have already been added to Laravel
```


1public function boot()




2{




3    $this->reloads('reverb:restart');




4}




public function boot()
{
    $this->reloads('reverb:restart');
}

```

### Modernize Email Template
Pull request by
The default Laravel email template was cleaned up and modernized, giving it a fresh coat of paint and an elevated, professional appearance.
## Laravel Framework 12.x
### Add `daysOfMonth()` Method to Schedule Tasks on Specific Days
Pull request by
Previously, there wasn't a way to [schedule tasks](https://laravel.com/docs/scheduling#schedule-frequency-options) on multiple arbitrary days of the month (e.g., 1st, 10th). A `daysOfMonth()` method was added that allows scheduling tasks to run on multiple specific days of the month with a clean, intuitive API.
```


1$schedule->command('process-payroll')




2    ->daysOfMonth(1, 15) // 1st and 15th of each month




3    ->timezone('America/New_York');




$schedule->command('process-payroll')
    ->daysOfMonth(1, 15) // 1st and 15th of each month
    ->timezone('America/New_York');

```

### [12.x] Add `encoding` Validation Rule for Uploaded Files
Pull request by
A new `encoding` [validation rule](https://laravel.com/docs/validation#available-validation-rules) was added that checks the contents of a file or string matches a specific encoding using `mb_check_encoding()`, ensuring that uploaded files are encoded as expected before processing.
```


1Validator::validate($input, [




2    'attachment' => [




3        'required',




4        File::types(['csv'])->encoding('utf-8'),




5    ],




6]);




Validator::validate($input, [
    'attachment' => [
        'required',
        File::types(['csv'])->encoding('utf-8'),
    ],
]);

```

### Interval Helper Functions
Pull request by
New [interval helper functions](https://laravel.com/docs/helpers#interval-functions) were added for fluently getting the current time with adjustments:
```


1use Illuminate\Support\{ now, minutes }




2 



3Cache::put('name', 'Taylor', minutes(5));




4 



5Invitation::create([




6    'expires_at' => now()->plus(hours: 6),




7]);




use Illuminate\Support\{ now, minutes }

Cache::put('name', 'Taylor', minutes(5));

Invitation::create([
    'expires_at' => now()->plus(hours: 6),
]);

```

### Queue Pause/Resume
Pull request by
Sometimes you may need to temporarily prevent a queue worker from processing new jobs without stopping the worker entirely. Now you can with [newly added artisan commands](https://laravel.com/docs/queues#pausing-and-resuming-queue-workers):
```


1php artisan queue:pause database:default




2php artisan queue:continue database:default




php artisan queue:pause database:default
php artisan queue:continue database:default

```

### [12.x] New `@hasStack` Blade Directive
Pull request by
The new `@hasStack` directive can be used to wrap `@stack` directives for conditional output depending on if the stack is empty or not. This is useful if you want some markup to wrap the stack only if it is not empty.
```


1@hasStack("list")




2<ul>




3    @stack("list")




4</ul>




5@endif




@hasStack("list")
<ul>
    @stack("list")
</ul>
@endif

```

### Add `--middleware` Filter to `route:list`
Pull request by
A `--middleware` option was added to the `route:list` command to filter output by middleware. This can be a single middleware class name or a middleware group name, allowing you to easily see routes with the specified middleware applied.
```


1php artisan route:list --middleware=api




2php artisan route:list --middleware=ThrottleRequests




php artisan route:list --middleware=api
php artisan route:list --middleware=ThrottleRequests

```

### [12.x] Introduce `WithCachedRoutes` Testing Trait
Pull request by
A new testing trait called `WithCachedRoutes` was introduced. This testing trait stores the routes as a static property within a `Testing\CachedState` object during test setup, ensuring subsequent tests do not need to read from disk.
### [12.x] New `Factory@insert()` Method
Pull request by
The `insert()` method was added to Eloquent Factories, allowing you to perform a mass insert of models. This increases performance during testing with numerous of database records.
### [12.x] Add `ucwords` to `Str` and `Stringable`
Pull request by
A `ucwords` method was added to `Stringable`, allowing fluent uppercasing of the first letter of a string. Note that this differs from `title` in that the rest of the string remains untouched.
```


1// Taylor Otwell, Creator Of Laravel




2$name = $this->string('taylor otwell, creator of laravel')->ucwords();




// Taylor Otwell, Creator Of Laravel
$name = $this->string('taylor otwell, creator of laravel')->ucwords();

```

## Laravel Framework 12.x
### [12.x] Ensure HTTP Batch Results Are Returned in the Same Order as Requested
Pull request by
Previously, `Http::batch` results were sorted in the order that the responses came back, rather than the order that the requests were defined:
```


 1dump(Http::batch(fn (Batch $batch) => [




 2    $batch->get('https://httpbin.org/delay/3'),




 3    $batch->get('https://httpbin.org/delay/2'),




 4    $batch->get('https://httpbin.org/delay/1'),




 5])->send());




 6 



 7array:3 [




 8  2 => Illuminate\Http\Client\Response {#419}




 9  1 => Illuminate\Http\Client\Response {#374}




10  0 => Illuminate\Http\Client\Response {#328}




11]




dump(Http::batch(fn (Batch $batch) => [
    $batch->get('https://httpbin.org/delay/3'),
    $batch->get('https://httpbin.org/delay/2'),
    $batch->get('https://httpbin.org/delay/1'),
])->send());

array:3 [
  2 => Illuminate\Http\Client\Response {#419}
  1 => Illuminate\Http\Client\Response {#374}
  0 => Illuminate\Http\Client\Response {#328}
]

```

The results are now sorted before they are returned, respecting any requests named with the `as` method. [Learn more about request batching](https://laravel.com/docs/http-client#request-batching).
### Add Support for Additional Editors in `ResolvesDumpSource`
Pull requests by
Several PRs introduced new config values for `app.editor`, allowing dumps to link correctly for several new IDEs: `neovim`, `zed`, `kiro`, `fleet`, and `windsurf`.
### Add Clickable File Reference for Thrown Exception
Pull request by
The recently introduced new exception page now includes a new file reference and line number that opens the file directly in your IDE of choice.
### [12.x] Add SQS FIFO and Fair Queue `messagegroup()` Method Support
Pull request by
Instead of using the `onGroup()` method at the time of dispatch, you can now define a `messageGroup()` directly method on the job class, removing an inconsistency where event listeners supported the `messageGroup()` method on the class, but all the other job types required calling `onGroup()`.
### Deferred Queue
Pull request by
Using [deferred synchronous dispatching](https://laravel.com/docs/queues#deferred-dispatching), you can dispatch a job to be processed during the current process, but after the HTTP response has been sent to the user. This allows you to process "queued" jobs synchronously without slowing down your user's application experience. To defer the execution of a synchronous job, dispatch the job to the `deferred` connection:
```


1RecordDelivery::dispatch($order)->onConnection('deferred');




RecordDelivery::dispatch($order)->onConnection('deferred');

```

### Failover Cache
Pull request by
The `failover` [cache driver](https://laravel.com/docs/cache#cache-failover) provides automatic failover functionality when interacting with the cache. If the primary cache store fails for any reason, Laravel will automatically attempt to use the next configured store in the list. This is particularly useful for ensuring high availability in production environments where cache reliability is critical.
```


1'failover' => [




2    'driver' => 'failover',




3    'stores' => [




4        'database',




5        'array',




6    ],




7],




'failover' => [
    'driver' => 'failover',
    'stores' => [
        'database',
        'array',
    ],
],

```

### [12.x] PostgreSQL Virtual Columns
Pull request by
PostgreSQL 18 was recently released, along with it support for virtual generated columns. The `virtualAs` column modifier now has backwards compatible support this new PostgreSQL feature.
### Failover Queue
Pull request by
The `failover` [queue driver](https://laravel.com/docs/queues#deferred-dispatching) provides automatic failover functionality when pushing jobs to the queue. If the primary queue connection fails for any reason, Laravel will automatically attempt to push the job to the next configured connection in the list. This is particularly useful for ensuring high availability in production environments where queue reliability is critical.
```


1'failover' => [




2    'driver' => 'failover',




3    'connections' => [




4        'redis',




5        'database',




6        'sync',




7    ],




8],




'failover' => [
    'driver' => 'failover',
    'connections' => [
        'redis',
        'database',
        'sync',
    ],
],

```

### [12.x] Add Defer Method to HTTP Batch
Pull request by
When the new `defer` method is invoked on `Http::batch`, [the batch of requests is not executed immediately](https://laravel.com/docs/queues#deferred-dispatching). Instead, Laravel will execute the batch after the current application request's HTTP response has been sent to the user, keeping your application feeling fast and responsive:
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

## Laravel Framework 12.x
### [12.x] Introduce `after` Rate Limiting
Pull request by
```


 1use Illuminate\Http\Request;




 2use Illuminate\Support\Facades\RateLimiter;




 3use Symfony\Component\HttpFoundation\Response;




 4 



 5/*




 6 * Ensure a user can only hit ten 404 responses in a minute before they are




 7 * rate limited to ensure user's cannot enumerate resource IDs.




 8 */




 9RateLimiter::for('resource-not-found', function (Request $request) {




10    return Limit::perMinute(10)




11        ->by("user:{$request->user()->id}")




12 



13        // The new `after` hook...




14        ->after(function (Response $response) {




15            return $response->getStatusCode() === 404;




16        });




17});




use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;
use Symfony\Component\HttpFoundation\Response;

/*
 * Ensure a user can only hit ten 404 responses in a minute before they are
 * rate limited to ensure user's cannot enumerate resource IDs.
 */
RateLimiter::for('resource-not-found', function (Request $request) {
    return Limit::perMinute(10)
        ->by("user:{$request->user()->id}")

        // The new `after` hook...
        ->after(function (Response $response) {
            return $response->getStatusCode() === 404;
        });
});

```

The new `RateLimiter::after` hook lets you apply rate limiting based on the response as well as the request.
### [12.x] Add `Http::batch`
Pull request by
```


 1$responses = Http::batch(fn (Batch $batch) => [




 2    $batch->get('http://localhost/first'),




 3    $batch->get('http://localhost/second'),




 4    $batch->get('http://localhost/third'),




 5])->before(function (Batch $batch) {




 6    // This runs before the first HTTP request is executed.




 7})->progress(function (Batch $batch, int|string $key, Response $response) {




 8    // This runs after each successful HTTP request from the Batch.




 9})->catch(function (Batch $batch, int|string $key, Response|RequestException $response) {




10    // This runs after each failed HTTP request from the Batch.




11})->then(function (Batch $batch, array $results) {




12    // This runs ONLY IF all the HTTP requests from the Batch are successful and the batch is not cancelled.




13})->finally(function (Batch $batch, array $results) {




14    // This runs after all the HTTP requests from the Batch finish and the batch is not cancelled.




15})->send();




$responses = Http::batch(fn (Batch $batch) => [
    $batch->get('http://localhost/first'),
    $batch->get('http://localhost/second'),
    $batch->get('http://localhost/third'),
])->before(function (Batch $batch) {
    // This runs before the first HTTP request is executed.
})->progress(function (Batch $batch, int|string $key, Response $response) {
    // This runs after each successful HTTP request from the Batch.
})->catch(function (Batch $batch, int|string $key, Response|RequestException $response) {
    // This runs after each failed HTTP request from the Batch.
})->then(function (Batch $batch, array $results) {
    // This runs ONLY IF all the HTTP requests from the Batch are successful and the batch is not cancelled.
})->finally(function (Batch $batch, array $results) {
    // This runs after all the HTTP requests from the Batch finish and the batch is not cancelled.
})->send();

```

The new `Http::batch` method allows you to hook into the lifecycle of each HTTP call when making multiple requests in parallel.
### [12.x] Adds `Macroable` Trait to `Illuminate/Support/Benchmark`
Pull request by
```


1use Closure;




2use Illuminate\Support\Benchmark;




3use Illuminate\Support\Facades\Log;




4 



5Benchmark::macro('log', fn (Closure $callback) =>




6    Log::debug(Benchmark::measure($callback))




7);




8 



9Benchmark::log(fn () => sleep(1));




use Closure;
use Illuminate\Support\Benchmark;
use Illuminate\Support\Facades\Log;

Benchmark::macro('log', fn (Closure $callback) =>
    Log::debug(Benchmark::measure($callback))
);

Benchmark::log(fn () => sleep(1));

```

`Benchmark` is now updated with the `Macroable` trait to allow arbitrary macro registration.
### [12.x] Add `--whisper` Option to `schedule:work` Command
Pull request by
You can now pass a `--whisper` option to the `schedule:work` command. The option is passed through to the `schedule:run` command, which hides the "No scheduled commands are ready to run" message from the output, producing cleaner logs and terminal output and reducing noise for monitoring tools.
### [12.x]: Cache Session Driver
Pull request by
```


1$discount = $request->session()->cache()->get('discount');




2 



3$request->session()->cache()->put(




4    'discount', 10, now()->addMinutes(5)




5);




$discount = $request->session()->cache()->get('discount');

$request->session()->cache()->put(
    'discount', 10, now()->addMinutes(5)
);

```

The new session cache provides a convenient way to cache data that is scoped to an individual user session. Unlike the global application cache, session cache data is automatically isolated per session and is cleaned up when the session expires or is destroyed.
### [12.x] Add Support for #[UseResource(...)] and #[UseResourceCollection(...)] Attributes on Models
Pull request by
```


 1use App\Http\Resources\MyCustomNameResource;




 2use App\Http\Resources\MyCustomNameCollectionResource;




 3 



 4#[UseResource(MyCustomNameResource::class)]




 5#[UseResourceCollection(MyCustomNameCollectionResource::class)]




 6class MyModel extends Model {




 7    //




 8}




 9 



10// Now you can call:




11$model->toResource();




12$collection->toResourceCollection();




use App\Http\Resources\MyCustomNameResource;
use App\Http\Resources\MyCustomNameCollectionResource;

#[UseResource(MyCustomNameResource::class)]
#[UseResourceCollection(MyCustomNameCollectionResource::class)]
class MyModel extends Model {
    //
}

// Now you can call:
$model->toResource();
$collection->toResourceCollection();

```

You can now define resources classes directly on your Eloquent models using PHP attributes.
### [12.x] Add `--json` Option to `schedule:list`
Pull request by
```


 1[




 2    {




 3        "expression": "0 0 15 * *",




 4        "repeat_seconds": null,




 5        "command": "php artisan backup:run",




 6        "description": "Run daily backup process",




 7        "next_due_date": "2025-09-15 00:00:00 +00:00",




 8        "next_due_date_human": "5 days from now",




 9        "timezone": "UTC",




10        "has_mutex": false




11    }




12]




[
    {
        "expression": "0 0 15 * *",
        "repeat_seconds": null,
        "command": "php artisan backup:run",
        "description": "Run daily backup process",
        "next_due_date": "2025-09-15 00:00:00 +00:00",
        "next_due_date_human": "5 days from now",
        "timezone": "UTC",
        "has_mutex": false
    }
]

```

The `schedule:list` command now accepts a `--json` flag to allow programmatic consumption of scheduled task data for monitoring and integration purposes.
### [12.x] Add Prepend Option for `Str::plural()`
Pull request by
```


1{{-- Instead of: --}}




2We had {{ number_format($attendees->count()) . ' ' . Str::plural('attendee', $attendees->count()) }} at Laracon 2025.




3 



4{{-- Now we can: --}}




5We had {{ Str::plural('attendee', $attendees->count(), prependCount: true) }} at Laracon 2025.




{{-- Instead of: --}}
We had {{ number_format($attendees->count()) . ' ' . Str::plural('attendee', $attendees->count()) }} at Laracon 2025.

{{-- Now we can: --}}
We had {{ Str::plural('attendee', $attendees->count(), prependCount: true) }} at Laracon 2025.

```

The `Str::plural` helper now accepts a new argument, `prependCount`, that will prepend the count to the string automatically.
### [12.x] Add Support for SQS Fair Queue
Pull request by
### [12.x] Update Local Exception Page
Pull request by
![New local exception page](https://laravel.com/images/changelog/2025-09/new-exception-page.jpeg)
The exception page was given a refresh, making local errors clearer and more actionable.
## Laravel Framework 12.x
### Add `withHeartbeat` Method to `LazyCollection`
Pull request by
```


1$collection




2    ->withHeartbeat(CarbonInterval::minutes(5), function () {




3        // ...




4    })




5    ->each(function ($item) {




6        // ...




7    });




$collection
    ->withHeartbeat(CarbonInterval::minutes(5), function () {
        // ...
    })
    ->each(function ($item) {
        // ...
    });

```

The new `withHeartbeart` method allows you to run a callback at regular time intervals while the collection is being lazily enumerated, particularly useful for long-running processes.
### Add `toPrettyJson` Method
Pull request by
```


1$collection = collect([1,2,3]);




2 



3// Instead of this:




4$collection->toJson(JSON_PRETTY_PRINT);




5 



6// You can now do this:




7$collection->toPrettyJson();




$collection = collect([1,2,3]);

// Instead of this:
$collection->toJson(JSON_PRETTY_PRINT);

// You can now do this:
$collection->toPrettyJson();

```

### Add `allowedUrls` Through `preventStrayRequests`
Pull request by
```


1Http::allowStrayRequests([




2    'http://127.0.0.1:13714/*',




3]);




Http::allowStrayRequests([
    'http://127.0.0.1:13714/*',
]);

```

The `Http::allowStrayRequests` method now accepts an argument that allows you to specify URLs that tests are allowed to send requests to when using `Http::preventStrayRequests`.
### Add "Copy as Markdown" Button to Error Page
Pull request by
There is now a "Copy as Markdown" button on the Laravel exception page. When clicking this button, a markdown representation of the exception is copied to the users clipboard, which can then be used for AI agents/LLMs.
### Add New `mergeVisible`, `mergeHidden` and `mergeAppends` Methods
Pull request by
```


 1protected function initializeTwoFactorAuthentication(): void




 2{




 3    $this->mergeHidden([




 4        'app_authentication_secret',




 5        'app_authentication_recovery_codes',




 6    ]);




 7 



 8    $this->mergeCasts([




 9        'app_authentication_secret' => 'encrypted',




10        'app_authentication_recovery_codes' => 'encrypted:array',




11    ]);




12}




protected function initializeTwoFactorAuthentication(): void
{
    $this->mergeHidden([
        'app_authentication_secret',
        'app_authentication_recovery_codes',
    ]);

    $this->mergeCasts([
        'app_authentication_secret' => 'encrypted',
        'app_authentication_recovery_codes' => 'encrypted:array',
    ]);
}

```

Additional attribute helper methods added to Eloquent models for merging visibility-related arrays, bringing them in line with existing helpers like `mergeCasts`, `mergeFillable`, and `mergeGuarded`.
### Add `Arr::push()`
Pull request by
```


1if ($this->hasChanges($data)) {




2    Arr::push($result, 'pending.changes', $data);




3}




if ($this->hasChanges($data)) {
    Arr::push($result, 'pending.changes', $data);
}

```

A new `Arr` method that allows you to push something to an array if the array exists, or initialize it to an empty array and then push to it if it doesn't.
## Laravel Framework 12.x
### Added Verbose Output for `queue:work`
Pull requests by
```


1php artisan queue:work --verbose




2// App\Jobs\UrgentAction 85 high




3// App\Jobs\NormalAction 84 default




php artisan queue:work --verbose
// App\Jobs\UrgentAction 85 high
// App\Jobs\NormalAction 84 default

```

With `--verbose`, you’ll now see queue names alongside each job and job ID, making multi-queue debugging straightforward and saving you time when tracing issues.
###  `Uri` Implements `JsonSerializable`
Pull request by
```


1echo json_encode(new Uri('/path?x=1'));




2// "http://localhost:8000/path?x=1"




echo json_encode(new Uri('/path?x=1'));
// "http://localhost:8000/path?x=1"

```

This release fixes a serialization bug, properly converting the URI to a string when serializing a larger JSON object that contains the URI as a value.
### Added `doesntStartWith()` & `doesntEndWith()` `Str` Methods
Pull request by
```


1str('apple')->doesntStartWith('b'); // true




2str('apple')->doesntEndWith('e'); // false




str('apple')->doesntStartWith('b'); // true
str('apple')->doesntEndWith('e'); // false

```

The inverse of `startsWith`/`endsWith`, these new methods allow you to fluently test for starting and ending characters in your string.
### Closure Support in `pluck()`
Pull request by
```


1$users->pluck(fn($u) => $u->email, fn($u) => strtoupper($u->name));




$users->pluck(fn($u) => $u->email, fn($u) => strtoupper($u->name));

```

You can now dynamically generate keys and values via callbacks. Instead of mapping then plucking, you get a single, flexible method that reduces steps and keeps intent clear.
## Laravel Framework 12.x
### Added `encrypt()` and `decrypt()` String Helper Methods
Pull request by
You can now chain `encrypt()` and `decrypt()` directly on a `Str` instance, so instead of piping your string through separate encryption calls, you can write:
```


1$value = Str::of('secret')->encrypt()->prepend('Encrypted: ');




2$original = Str::of($value)->decrypt();




$value = Str::of('secret')->encrypt()->prepend('Encrypted: ');
$original = Str::of($value)->decrypt();

```

This keeps your string-manipulation chains concise (no need to write separate, extra code to handle encryption) and you don’t have to manually wrap a value in encryption calls each time.
Learn more about [`encrypt`](https://laravel.com/docs/12.x/helpers#method-encrypt) and [`decrypt`](https://laravel.com/docs/12.x/helpers#method-decrypt)
### Added `broadcast_if()` and `broadcast_unless()` Utilities
Pull request by
You now have two methods for conditional broadcasting in a single call:
```


1broadcast_if($order->isPaid(), new OrderShipped($order));




2broadcast_unless($user->isActive(), new InactiveUserAlert($user));




broadcast_if($order->isPaid(), new OrderShipped($order));
broadcast_unless($user->isActive(), new InactiveUserAlert($user));

```

This replaces multi-line conditionals around `broadcast()` and makes your event logic more readable, improving the overall developer experience.
Read the docs about [event broadcasting in Laravel](https://laravel.com/docs/12.x/broadcasting)
### Added `--batched` Flag to `make:job`
Pull request by
The `php artisan make:job` command now accepts a `--batched` option:
```


1php artisan make:job ProcessPodcast --batched




php artisan make:job ProcessPodcast --batched

```

This command scaffolds the job with the `Batchable` trait already applied, so you don’t have to add it manually. It saves you a manual step and ensures consistency.
Learn more about [defining batchable jobs](https://laravel.com/docs/12.x/queues#defining-batchable-jobs)
