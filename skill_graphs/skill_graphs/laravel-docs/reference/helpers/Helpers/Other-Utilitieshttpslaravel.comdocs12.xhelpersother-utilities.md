## [Other Utilities](https://laravel.com/docs/12.x/helpers#other-utilities)
### [Benchmarking](https://laravel.com/docs/12.x/helpers#benchmarking)
Sometimes you may wish to quickly test the performance of certain parts of your application. On those occasions, you may utilize the `Benchmark` support class to measure the number of milliseconds it takes for the given callbacks to complete:
```


 1<?php




 2 



 3use App\Models\User;




 4use Illuminate\Support\Benchmark;




 5 



 6Benchmark::dd(fn () => User::find(1)); // 0.1 ms




 7 



 8Benchmark::dd([




 9    'Scenario 1' => fn () => User::count(), // 0.5 ms




10    'Scenario 2' => fn () => User::all()->count(), // 20.0 ms




11]);




<?php

use App\Models\User;
use Illuminate\Support\Benchmark;

Benchmark::dd(fn () => User::find(1)); // 0.1 ms

Benchmark::dd([
    'Scenario 1' => fn () => User::count(), // 0.5 ms
    'Scenario 2' => fn () => User::all()->count(), // 20.0 ms
]);

```

By default, the given callbacks will be executed once (one iteration), and their duration will be displayed in the browser / console.
To invoke a callback more than once, you may specify the number of iterations that the callback should be invoked as the second argument to the method. When executing a callback more than once, the `Benchmark` class will return the average number of milliseconds it took to execute the callback across all iterations:
```


1Benchmark::dd(fn () => User::count(), iterations: 10); // 0.5 ms




Benchmark::dd(fn () => User::count(), iterations: 10); // 0.5 ms

```

Sometimes, you may want to benchmark the execution of a callback while still obtaining the value returned by the callback. The `value` method will return a tuple containing the value returned by the callback and the number of milliseconds it took to execute the callback:
```


1[$count, $duration] = Benchmark::value(fn () => User::count());




[$count, $duration] = Benchmark::value(fn () => User::count());

```

### [Dates and Time](https://laravel.com/docs/12.x/helpers#dates)
Laravel includes `Carbon` instance, you may invoke the `now` function. This function is globally available within your Laravel application:
```


1$now = now();




$now = now();

```

Or, you may create a new `Carbon` instance using the `Illuminate\Support\Carbon` class:
```


1use Illuminate\Support\Carbon;




2 



3$now = Carbon::now();




use Illuminate\Support\Carbon;

$now = Carbon::now();

```

Laravel also augments `Carbon` instances with `plus` and `minus` methods, allowing easy manipulation of the instance's date and time:
```


1return now()->plus(minutes: 5);




2return now()->plus(hours: 8);




3return now()->plus(weeks: 4);




4 



5return now()->minus(minutes: 5);




6return now()->minus(hours: 8);




7return now()->minus(weeks: 4);




return now()->plus(minutes: 5);
return now()->plus(hours: 8);
return now()->plus(weeks: 4);

return now()->minus(minutes: 5);
return now()->minus(hours: 8);
return now()->minus(weeks: 4);

```

For a thorough discussion of Carbon and its features, please consult the
#### [Interval Functions](https://laravel.com/docs/12.x/helpers#interval-functions)
Laravel also offers `milliseconds`, `seconds`, `minutes`, `hours`, `days`, `weeks`, `months`, and `years` functions that return `CarbonInterval` instances, which extend PHP's `DateInterval` instance:
```


1use Illuminate\Support\Facades\Cache;




2 



3use function Illuminate\Support\{minutes};




4 



5Cache::put('metrics', $metrics, minutes(10));




use Illuminate\Support\Facades\Cache;

use function Illuminate\Support\{minutes};

Cache::put('metrics', $metrics, minutes(10));

```

### [Deferred Functions](https://laravel.com/docs/12.x/helpers#deferred-functions)
While Laravel's [queued jobs](https://laravel.com/docs/12.x/queues) allow you to queue tasks for background processing, sometimes you may have simple tasks you would like to defer without configuring or maintaining a long-running queue worker.
Deferred functions allow you to defer the execution of a closure until after the HTTP response has been sent to the user, keeping your application feeling fast and responsive. To defer the execution of a closure, simply pass the closure to the `Illuminate\Support\defer` function:
```


 1use App\Services\Metrics;




 2use Illuminate\Http\Request;




 3use Illuminate\Support\Facades\Route;




 4use function Illuminate\Support\defer;




 5 



 6Route::post('/orders', function (Request $request) {




 7    // Create order...




 8 



 9    defer(fn () => Metrics::reportOrder($order));




10 



11    return $order;




12});




use App\Services\Metrics;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use function Illuminate\Support\defer;

Route::post('/orders', function (Request $request) {
    // Create order...

    defer(fn () => Metrics::reportOrder($order));

    return $order;
});

```

By default, deferred functions will only be executed if the HTTP response, Artisan command, or queued job from which `Illuminate\Support\defer` is invoked completes successfully. This means that deferred functions will not be executed if a request results in a `4xx` or `5xx` HTTP response. If you would like a deferred function to always execute, you may chain the `always` method onto your deferred function:
```


1defer(fn () => Metrics::reportOrder($order))->always();




defer(fn () => Metrics::reportOrder($order))->always();

```

If you have the `defer` function may conflict with Swoole's own global `defer` function, leading to web server errors. Make sure you call Laravel's `defer` helper by explicitly namespacing it: `use function Illuminate\Support\defer;`
#### [Cancelling Deferred Functions](https://laravel.com/docs/12.x/helpers#cancelling-deferred-functions)
If you need to cancel a deferred function before it is executed, you can use the `forget` method to cancel the function by its name. To name a deferred function, provide a second argument to the `Illuminate\Support\defer` function:
```


1defer(fn () => Metrics::report(), 'reportMetrics');




2 



3defer()->forget('reportMetrics');




defer(fn () => Metrics::report(), 'reportMetrics');

defer()->forget('reportMetrics');

```

#### [Disabling Deferred Functions in Tests](https://laravel.com/docs/12.x/helpers#disabling-deferred-functions-in-tests)
When writing tests, it may be useful to disable deferred functions. You may call `withoutDefer` in your test to instruct Laravel to invoke all deferred functions immediately:
Pest PHPUnit
```


1test('without defer', function () {




2    $this->withoutDefer();




3 



4    // ...




5});




test('without defer', function () {
    $this->withoutDefer();

    // ...
});

```

```


 1use Tests\TestCase;




 2 



 3class ExampleTest extends TestCase




 4{




 5    public function test_without_defer(): void




 6    {




 7        $this->withoutDefer();




 8 



 9        // ...




10    }




11}




use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_without_defer(): void
    {
        $this->withoutDefer();

        // ...
    }
}

```

If you would like to disable deferred functions for all tests within a test case, you may call the `withoutDefer` method from the `setUp` method on your base `TestCase` class:
```


 1<?php




 2 



 3namespace Tests;




 4 



 5use Illuminate\Foundation\Testing\TestCase as BaseTestCase;




 6 



 7abstract class TestCase extends BaseTestCase




 8{




 9    protected function setUp(): void




10    {




11        parent::setUp();




12 



13        $this->withoutDefer();




14    }




15}




<?php

namespace Tests;

use Illuminate\Foundation\Testing\TestCase as BaseTestCase;

abstract class TestCase extends BaseTestCase
{
    protected function setUp(): void
    {
        parent::setUp();

        $this->withoutDefer();
    }
}

```

### [Lottery](https://laravel.com/docs/12.x/helpers#lottery)
Laravel's lottery class may be used to execute callbacks based on a set of given odds. This can be particularly useful when you only want to execute code for a percentage of your incoming requests:
```


1use Illuminate\Support\Lottery;




2 



3Lottery::odds(1, 20)




4    ->winner(fn () => $user->won())




5    ->loser(fn () => $user->lost())




6    ->choose();




use Illuminate\Support\Lottery;

Lottery::odds(1, 20)
    ->winner(fn () => $user->won())
    ->loser(fn () => $user->lost())
    ->choose();

```

You may combine Laravel's lottery class with other Laravel features. For example, you may wish to only report a small percentage of slow queries to your exception handler. And, since the lottery class is callable, we may pass an instance of the class into any method that accepts callables:
```


1use Carbon\CarbonInterval;




2use Illuminate\Support\Facades\DB;




3use Illuminate\Support\Lottery;




4 



5DB::whenQueryingForLongerThan(




6    CarbonInterval::seconds(2),




7    Lottery::odds(1, 100)->winner(fn () => report('Querying > 2 seconds.')),




8);




use Carbon\CarbonInterval;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Lottery;

DB::whenQueryingForLongerThan(
    CarbonInterval::seconds(2),
    Lottery::odds(1, 100)->winner(fn () => report('Querying > 2 seconds.')),
);

```

#### [Testing Lotteries](https://laravel.com/docs/12.x/helpers#testing-lotteries)
Laravel provides some simple methods to allow you to easily test your application's lottery invocations:
```


 1// Lottery will always win...




 2Lottery::alwaysWin();




 3 



 4// Lottery will always lose...




 5Lottery::alwaysLose();




 6 



 7// Lottery will win then lose, and finally return to normal behavior...




 8Lottery::fix([true, false]);




 9 



10// Lottery will return to normal behavior...




11Lottery::determineResultsNormally();




// Lottery will always win...
Lottery::alwaysWin();

// Lottery will always lose...
Lottery::alwaysLose();

// Lottery will win then lose, and finally return to normal behavior...
Lottery::fix([true, false]);

// Lottery will return to normal behavior...
Lottery::determineResultsNormally();

```

### [Pipeline](https://laravel.com/docs/12.x/helpers#pipeline)
Laravel's `Pipeline` facade provides a convenient way to "pipe" a given input through a series of invocable classes, closures, or callables, giving each class the opportunity to inspect or modify the input and invoke the next callable in the pipeline:
```


 1use Closure;




 2use App\Models\User;




 3use Illuminate\Support\Facades\Pipeline;




 4 



 5$user = Pipeline::send($user)




 6    ->through([




 7        function (User $user, Closure $next) {




 8            // ...




 9 



10            return $next($user);




11        },




12        function (User $user, Closure $next) {




13            // ...




14 



15            return $next($user);




16        },




17    ])




18    ->then(fn (User $user) => $user);




use Closure;
use App\Models\User;
use Illuminate\Support\Facades\Pipeline;

$user = Pipeline::send($user)
    ->through([
        function (User $user, Closure $next) {
            // ...

            return $next($user);
        },
        function (User $user, Closure $next) {
            // ...

            return $next($user);
        },
    ])
    ->then(fn (User $user) => $user);

```

As you can see, each invocable class or closure in the pipeline is provided the input and a `$next` closure. Invoking the `$next` closure will invoke the next callable in the pipeline. As you may have noticed, this is very similar to [middleware](https://laravel.com/docs/12.x/middleware).
When the last callable in the pipeline invokes the `$next` closure, the callable provided to the `then` method will be invoked. Typically, this callable will simply return the given input. For convenience, if you simply want to return the input after it has been processed, you may use the `thenReturn` method.
Of course, as discussed previously, you are not limited to providing closures to your pipeline. You may also provide invocable classes. If a class name is provided, the class will be instantiated via Laravel's [service container](https://laravel.com/docs/12.x/container), allowing dependencies to be injected into the invocable class:
```


1$user = Pipeline::send($user)




2    ->through([




3        GenerateProfilePhoto::class,




4        ActivateSubscription::class,




5        SendWelcomeEmail::class,




6    ])




7    ->thenReturn();




$user = Pipeline::send($user)
    ->through([
        GenerateProfilePhoto::class,
        ActivateSubscription::class,
        SendWelcomeEmail::class,
    ])
    ->thenReturn();

```

The `withinTransaction` method may be invoked on the pipeline to automatically wrap all steps of the pipeline within a single database transaction:
```


1$user = Pipeline::send($user)




2    ->withinTransaction()




3    ->through([




4        ProcessOrder::class,




5        TransferFunds::class,




6        UpdateInventory::class,




7    ])




8    ->thenReturn();




$user = Pipeline::send($user)
    ->withinTransaction()
    ->through([
        ProcessOrder::class,
        TransferFunds::class,
        UpdateInventory::class,
    ])
    ->thenReturn();

```

### [Sleep](https://laravel.com/docs/12.x/helpers#sleep)
Laravel's `Sleep` class is a light-weight wrapper around PHP's native `sleep` and `usleep` functions, offering greater testability while also exposing a developer friendly API for working with time:
```


1use Illuminate\Support\Sleep;




2 



3$waiting = true;




4 



5while ($waiting) {




6    Sleep::for(1)->second();




7 



8    $waiting = /* ... */;




9}




use Illuminate\Support\Sleep;

$waiting = true;

while ($waiting) {
    Sleep::for(1)->second();

    $waiting = /* ... */;
}

```

The `Sleep` class offers a variety of methods that allow you to work with different units of time:
```


 1// Return a value after sleeping...




 2$result = Sleep::for(1)->second()->then(fn () => 1 + 1);




 3 



 4// Sleep while a given value is true...




 5Sleep::for(1)->second()->while(fn () => shouldKeepSleeping());




 6 



 7// Pause execution for 90 seconds...




 8Sleep::for(1.5)->minutes();




 9 



10// Pause execution for 2 seconds...




11Sleep::for(2)->seconds();




12 



13// Pause execution for 500 milliseconds...




14Sleep::for(500)->milliseconds();




15 



16// Pause execution for 5,000 microseconds...




17Sleep::for(5000)->microseconds();




18 



19// Pause execution until a given time...




20Sleep::until(now()->plus(minutes: 1));




21 



22// Alias of PHP's native "sleep" function...




23Sleep::sleep(2);




24 



25// Alias of PHP's native "usleep" function...




26Sleep::usleep(5000);




// Return a value after sleeping...
$result = Sleep::for(1)->second()->then(fn () => 1 + 1);

// Sleep while a given value is true...
Sleep::for(1)->second()->while(fn () => shouldKeepSleeping());

// Pause execution for 90 seconds...
Sleep::for(1.5)->minutes();

// Pause execution for 2 seconds...
Sleep::for(2)->seconds();

// Pause execution for 500 milliseconds...
Sleep::for(500)->milliseconds();

// Pause execution for 5,000 microseconds...
Sleep::for(5000)->microseconds();

// Pause execution until a given time...
Sleep::until(now()->plus(minutes: 1));

// Alias of PHP's native "sleep" function...
Sleep::sleep(2);

// Alias of PHP's native "usleep" function...
Sleep::usleep(5000);

```

To easily combine units of time, you may use the `and` method:
```


1Sleep::for(1)->second()->and(10)->milliseconds();




Sleep::for(1)->second()->and(10)->milliseconds();

```

#### [Testing Sleep](https://laravel.com/docs/12.x/helpers#testing-sleep)
When testing code that utilizes the `Sleep` class or PHP's native sleep functions, your test will pause execution. As you might expect, this makes your test suite significantly slower. For example, imagine you are testing the following code:
```


1$waiting = /* ... */;




2 



3$seconds = 1;




4 



5while ($waiting) {




6    Sleep::for($seconds++)->seconds();




7 



8    $waiting = /* ... */;




9}




$waiting = /* ... */;

$seconds = 1;

while ($waiting) {
    Sleep::for($seconds++)->seconds();

    $waiting = /* ... */;
}

```

Typically, testing this code would take _at least_ one second. Luckily, the `Sleep` class allows us to "fake" sleeping so that our test suite stays fast:
Pest PHPUnit
```


1it('waits until ready', function () {




2    Sleep::fake();




3 



4    // ...




5});




it('waits until ready', function () {
    Sleep::fake();

    // ...
});

```

```


1public function test_it_waits_until_ready()




2{




3    Sleep::fake();




4 



5    // ...




6}




public function test_it_waits_until_ready()
{
    Sleep::fake();

    // ...
}

```

When faking the `Sleep` class, the actual execution pause is bypassed, leading to a substantially faster test.
Once the `Sleep` class has been faked, it is possible to make assertions against the expected "sleeps" that should have occurred. To illustrate this, let's imagine we are testing code that pauses execution three times, with each pause increasing by a single second. Using the `assertSequence` method, we can assert that our code "slept" for the proper amount of time while keeping our test fast:
Pest PHPUnit
```


 1it('checks if ready three times', function () {




 2    Sleep::fake();




 3 



 4    // ...




 5 



 6    Sleep::assertSequence([




 7        Sleep::for(1)->second(),




 8        Sleep::for(2)->seconds(),




 9        Sleep::for(3)->seconds(),




10    ]);




11}




it('checks if ready three times', function () {
    Sleep::fake();

    // ...

    Sleep::assertSequence([
        Sleep::for(1)->second(),
        Sleep::for(2)->seconds(),
        Sleep::for(3)->seconds(),
    ]);
}

```

```


 1public function test_it_checks_if_ready_three_times()




 2{




 3    Sleep::fake();




 4 



 5    // ...




 6 



 7    Sleep::assertSequence([




 8        Sleep::for(1)->second(),




 9        Sleep::for(2)->seconds(),




10        Sleep::for(3)->seconds(),




11    ]);




12}




public function test_it_checks_if_ready_three_times()
{
    Sleep::fake();

    // ...

    Sleep::assertSequence([
        Sleep::for(1)->second(),
        Sleep::for(2)->seconds(),
        Sleep::for(3)->seconds(),
    ]);
}

```

Of course, the `Sleep` class offers a variety of other assertions you may use when testing:
```


 1use Carbon\CarbonInterval as Duration;




 2use Illuminate\Support\Sleep;




 3 



 4// Assert that sleep was called 3 times...




 5Sleep::assertSleptTimes(3);




 6 



 7// Assert against the duration of sleep...




 8Sleep::assertSlept(function (Duration $duration): bool {




 9    return /* ... */;




10}, times: 1);




11 



12// Assert that the Sleep class was never invoked...




13Sleep::assertNeverSlept();




14 



15// Assert that, even if Sleep was called, no execution paused occurred...




16Sleep::assertInsomniac();




use Carbon\CarbonInterval as Duration;
use Illuminate\Support\Sleep;

// Assert that sleep was called 3 times...
Sleep::assertSleptTimes(3);

// Assert against the duration of sleep...
Sleep::assertSlept(function (Duration $duration): bool {
    return /* ... */;
}, times: 1);

// Assert that the Sleep class was never invoked...
Sleep::assertNeverSlept();

// Assert that, even if Sleep was called, no execution paused occurred...
Sleep::assertInsomniac();

```

Sometimes it may be useful to perform an action whenever a fake sleep occurs. To achieve this, you may provide a callback to the `whenFakingSleep` method. In the following example, we use Laravel's [time manipulation helpers](https://laravel.com/docs/12.x/mocking#interacting-with-time) to instantly progress time by the duration of each sleep:
```


 1use Carbon\CarbonInterval as Duration;




 2 



 3$this->freezeTime();




 4 



 5Sleep::fake();




 6 



 7Sleep::whenFakingSleep(function (Duration $duration) {




 8    // Progress time when faking sleep...




 9    $this->travel($duration->totalMilliseconds)->milliseconds();




10});




use Carbon\CarbonInterval as Duration;

$this->freezeTime();

Sleep::fake();

Sleep::whenFakingSleep(function (Duration $duration) {
    // Progress time when faking sleep...
    $this->travel($duration->totalMilliseconds)->milliseconds();
});

```

As progressing time is a common requirement, the `fake` method accepts a `syncWithCarbon` argument to keep Carbon in sync when sleeping within a test:
```


1Sleep::fake(syncWithCarbon: true);




2 



3$start = now();




4 



5Sleep::for(1)->second();




6 



7$start->diffForHumans(); // 1 second ago




Sleep::fake(syncWithCarbon: true);

$start = now();

Sleep::for(1)->second();

$start->diffForHumans(); // 1 second ago

```

Laravel uses the `Sleep` class internally whenever it is pausing execution. For example, the [retry](https://laravel.com/docs/12.x/helpers#method-retry) helper uses the `Sleep` class when sleeping, allowing for improved testability when using that helper.
### [Timebox](https://laravel.com/docs/12.x/helpers#timebox)
Laravel's `Timebox` class ensures that the given callback always takes a fixed amount of time to execute, even if its actual execution completes sooner. This is particularly useful for cryptographic operations and user authentication checks, where attackers might exploit variations in execution time to infer sensitive information.
If the execution exceeds the fixed duration, `Timebox` has no effect. It is up to the developer to choose a sufficiently long time as the fixed duration to account for worst-case scenarios.
The call method accepts a closure and a time limit in microseconds, and then executes the closure and waits until the time limit is reached:
```


1use Illuminate\Support\Timebox;




2 



3(new Timebox)->call(function ($timebox) {




4    // ...




5}, microseconds: 10000);




use Illuminate\Support\Timebox;

(new Timebox)->call(function ($timebox) {
    // ...
}, microseconds: 10000);

```

If an exception is thrown within the closure, this class will respect the defined delay and re-throw the exception after the delay.
### [URI](https://laravel.com/docs/12.x/helpers#uri)
Laravel's `Uri` class provides a convenient and fluent interface for creating and manipulating URIs. This class wraps the functionality provided by the underlying League URI package and integrates seamlessly with Laravel's routing system.
You can create a `Uri` instance easily using static methods:
```


 1use App\Http\Controllers\UserController;




 2use App\Http\Controllers\InvokableController;




 3use Illuminate\Support\Uri;




 4 



 5// Generate a URI instance from the given string...




 6$uri = Uri::of('https://example.com/path');




 7 



 8// Generate URI instances to paths, named routes, or controller actions...




 9$uri = Uri::to('/dashboard');




10$uri = Uri::route('users.show', ['user' => 1]);




11$uri = Uri::signedRoute('users.show', ['user' => 1]);




12$uri = Uri::temporarySignedRoute('user.index', now()->plus(minutes: 5));




13$uri = Uri::action([UserController::class, 'index']);




14$uri = Uri::action(InvokableController::class);




15 



16// Generate a URI instance from the current request URL...




17$uri = $request->uri();




use App\Http\Controllers\UserController;
use App\Http\Controllers\InvokableController;
use Illuminate\Support\Uri;

// Generate a URI instance from the given string...
$uri = Uri::of('https://example.com/path');

// Generate URI instances to paths, named routes, or controller actions...
$uri = Uri::to('/dashboard');
$uri = Uri::route('users.show', ['user' => 1]);
$uri = Uri::signedRoute('users.show', ['user' => 1]);
$uri = Uri::temporarySignedRoute('user.index', now()->plus(minutes: 5));
$uri = Uri::action([UserController::class, 'index']);
$uri = Uri::action(InvokableController::class);

// Generate a URI instance from the current request URL...
$uri = $request->uri();

```

Once you have a URI instance, you can fluently modify it:
```


1$uri = Uri::of('https://example.com')




2    ->withScheme('http')




3    ->withHost('test.com')




4    ->withPort(8000)




5    ->withPath('/users')




6    ->withQuery(['page' => 2])




7    ->withFragment('section-1');




$uri = Uri::of('https://example.com')
    ->withScheme('http')
    ->withHost('test.com')
    ->withPort(8000)
    ->withPath('/users')
    ->withQuery(['page' => 2])
    ->withFragment('section-1');

```

#### [Inspecting URIs](https://laravel.com/docs/12.x/helpers#inspecting-uris)
The `Uri` class also allows you to easily inspect the various components of the underlying URI:
```


1$scheme = $uri->scheme();




2$authority = $uri->authority();




3$host = $uri->host();




4$port = $uri->port();




5$path = $uri->path();




6$segments = $uri->pathSegments();




7$query = $uri->query();




8$fragment = $uri->fragment();




$scheme = $uri->scheme();
$authority = $uri->authority();
$host = $uri->host();
$port = $uri->port();
$path = $uri->path();
$segments = $uri->pathSegments();
$query = $uri->query();
$fragment = $uri->fragment();

```

#### [Manipulating Query Strings](https://laravel.com/docs/12.x/helpers#manipulating-query-strings)
The `Uri` class offers several methods that may be used to manipulate a URI's query string. The `withQuery` method may be used to merge additional query string parameters into the existing query string:
```


1$uri = $uri->withQuery(['sort' => 'name']);




$uri = $uri->withQuery(['sort' => 'name']);

```

The `withQueryIfMissing` method may be used to merge additional query string parameters into the existing query string if the given keys do not already exist in the query string:
```


1$uri = $uri->withQueryIfMissing(['page' => 1]);




$uri = $uri->withQueryIfMissing(['page' => 1]);

```

The `replaceQuery` method may be used to complete replace the existing query string with a new one:
```


1$uri = $uri->replaceQuery(['page' => 1]);




$uri = $uri->replaceQuery(['page' => 1]);

```

The `pushOntoQuery` method may be used to push additional parameters onto a query string parameter that has an array value:
```


1$uri = $uri->pushOntoQuery('filter', ['active', 'pending']);




$uri = $uri->pushOntoQuery('filter', ['active', 'pending']);

```

The `withoutQuery` method may be used to remove parameters from the query string:
```


1$uri = $uri->withoutQuery(['page']);




$uri = $uri->withoutQuery(['page']);

```

#### [Generating Responses From URIs](https://laravel.com/docs/12.x/helpers#generating-responses-from-uris)
The `redirect` method may be used to generate a `RedirectResponse` instance to the given URI:
```


1$uri = Uri::of('https://example.com');




2 



3return $uri->redirect();




$uri = Uri::of('https://example.com');

return $uri->redirect();

```

Or, you may simply return the `Uri` instance from a route or controller action, which will automatically generate a redirect response to the returned URI:
```


1use Illuminate\Support\Facades\Route;




2use Illuminate\Support\Uri;




3 



4Route::get('/redirect', function () {




5    return Uri::to('/index')




6        ->withQuery(['sort' => 'name']);




7});




use Illuminate\Support\Facades\Route;
use Illuminate\Support\Uri;

Route::get('/redirect', function () {
    return Uri::to('/index')
        ->withQuery(['sort' => 'name']);
});

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/helpers#introduction)
  * [ Available Methods ](https://laravel.com/docs/12.x/helpers#available-methods)
  * [ Other Utilities ](https://laravel.com/docs/12.x/helpers#other-utilities)
    * [ Benchmarking ](https://laravel.com/docs/12.x/helpers#benchmarking)
    * [ Dates and Time ](https://laravel.com/docs/12.x/helpers#dates)
    * [ Deferred Functions ](https://laravel.com/docs/12.x/helpers#deferred-functions)
    * [ Lottery ](https://laravel.com/docs/12.x/helpers#lottery)
    * [ Pipeline ](https://laravel.com/docs/12.x/helpers#pipeline)
    * [ Sleep ](https://laravel.com/docs/12.x/helpers#sleep)
    * [ Timebox ](https://laravel.com/docs/12.x/helpers#timebox)
    * [ URI ](https://laravel.com/docs/12.x/helpers#uri)


[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
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
  *   * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [ More Partners ](https://partners.laravel.com)
