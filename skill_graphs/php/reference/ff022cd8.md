## [Miscellaneous](https://laravel.com/docs/12.x/helpers#miscellaneous)
#### [`abort()`](https://laravel.com/docs/12.x/helpers#method-abort)
The `abort` function throws [an HTTP exception](https://laravel.com/docs/12.x/errors#http-exceptions) which will be rendered by the [exception handler](https://laravel.com/docs/12.x/errors#handling-exceptions):
```


1abort(403);




abort(403);

```

You may also provide the exception's message and custom HTTP response headers that should be sent to the browser:
```


1abort(403, 'Unauthorized.', $headers);




abort(403, 'Unauthorized.', $headers);

```

#### [`abort_if()`](https://laravel.com/docs/12.x/helpers#method-abort-if)
The `abort_if` function throws an HTTP exception if a given boolean expression evaluates to `true`:
```


1abort_if(! Auth::user()->isAdmin(), 403);




abort_if(! Auth::user()->isAdmin(), 403);

```

Like the `abort` method, you may also provide the exception's response text as the third argument and an array of custom response headers as the fourth argument to the function.
#### [`abort_unless()`](https://laravel.com/docs/12.x/helpers#method-abort-unless)
The `abort_unless` function throws an HTTP exception if a given boolean expression evaluates to `false`:
```


1abort_unless(Auth::user()->isAdmin(), 403);




abort_unless(Auth::user()->isAdmin(), 403);

```

Like the `abort` method, you may also provide the exception's response text as the third argument and an array of custom response headers as the fourth argument to the function.
#### [`app()`](https://laravel.com/docs/12.x/helpers#method-app)
The `app` function returns the [service container](https://laravel.com/docs/12.x/container) instance:
```


1$container = app();




$container = app();

```

You may pass a class or interface name to resolve it from the container:
```


1$api = app('HelpSpot\API');




$api = app('HelpSpot\API');

```

#### [`auth()`](https://laravel.com/docs/12.x/helpers#method-auth)
The `auth` function returns an [authenticator](https://laravel.com/docs/12.x/authentication) instance. You may use it as an alternative to the `Auth` facade:
```


1$user = auth()->user();




$user = auth()->user();

```

If needed, you may specify which guard instance you would like to access:
```


1$user = auth('admin')->user();




$user = auth('admin')->user();

```

#### [`back()`](https://laravel.com/docs/12.x/helpers#method-back)
The `back` function generates a [redirect HTTP response](https://laravel.com/docs/12.x/responses#redirects) to the user's previous location:
```


1return back($status = 302, $headers = [], $fallback = '/');




2 



3return back();




return back($status = 302, $headers = [], $fallback = '/');

return back();

```

#### [`bcrypt()`](https://laravel.com/docs/12.x/helpers#method-bcrypt)
The `bcrypt` function [hashes](https://laravel.com/docs/12.x/hashing) the given value using Bcrypt. You may use this function as an alternative to the `Hash` facade:
```


1$password = bcrypt('my-secret-password');




$password = bcrypt('my-secret-password');

```

#### [`blank()`](https://laravel.com/docs/12.x/helpers#method-blank)
The `blank` function determines whether the given value is "blank":
```


 1blank('');




 2blank('   ');




 3blank(null);




 4blank(collect());




 5 



 6// true




 7 



 8blank(0);




 9blank(true);




10blank(false);




11 



12// false




blank('');
blank('   ');
blank(null);
blank(collect());

// true

blank(0);
blank(true);
blank(false);

// false

```

For the inverse of `blank`, see the [filled](https://laravel.com/docs/12.x/helpers#method-filled) function.
#### [`broadcast()`](https://laravel.com/docs/12.x/helpers#method-broadcast)
The `broadcast` function [broadcasts](https://laravel.com/docs/12.x/broadcasting) the given [event](https://laravel.com/docs/12.x/events) to its listeners:
```


1broadcast(new UserRegistered($user));




2 



3broadcast(new UserRegistered($user))->toOthers();




broadcast(new UserRegistered($user));

broadcast(new UserRegistered($user))->toOthers();

```

#### [`broadcast_if()`](https://laravel.com/docs/12.x/helpers#method-broadcast-if)
The `broadcast_if` function [broadcasts](https://laravel.com/docs/12.x/broadcasting) the given [event](https://laravel.com/docs/12.x/events) to its listeners if a given boolean expression evaluates to `true`:
```


1broadcast_if($user->isActive(), new UserRegistered($user));




2 



3broadcast_if($user->isActive(), new UserRegistered($user))->toOthers();




broadcast_if($user->isActive(), new UserRegistered($user));

broadcast_if($user->isActive(), new UserRegistered($user))->toOthers();

```

#### [`broadcast_unless()`](https://laravel.com/docs/12.x/helpers#method-broadcast-unless)
The `broadcast_unless` function [broadcasts](https://laravel.com/docs/12.x/broadcasting) the given [event](https://laravel.com/docs/12.x/events) to its listeners if a given boolean expression evaluates to `false`:
```


1broadcast_unless($user->isBanned(), new UserRegistered($user));




2 



3broadcast_unless($user->isBanned(), new UserRegistered($user))->toOthers();




broadcast_unless($user->isBanned(), new UserRegistered($user));

broadcast_unless($user->isBanned(), new UserRegistered($user))->toOthers();

```

#### [`cache()`](https://laravel.com/docs/12.x/helpers#method-cache)
The `cache` function may be used to get values from the [cache](https://laravel.com/docs/12.x/cache). If the given key does not exist in the cache, an optional default value will be returned:
```


1$value = cache('key');




2 



3$value = cache('key', 'default');




$value = cache('key');

$value = cache('key', 'default');

```

You may add items to the cache by passing an array of key / value pairs to the function. You should also pass the number of seconds or duration the cached value should be considered valid:
```


1cache(['key' => 'value'], 300);




2 



3cache(['key' => 'value'], now()->plus(seconds: 10));




cache(['key' => 'value'], 300);

cache(['key' => 'value'], now()->plus(seconds: 10));

```

#### [`class_uses_recursive()`](https://laravel.com/docs/12.x/helpers#method-class-uses-recursive)
The `class_uses_recursive` function returns all traits used by a class, including traits used by all of its parent classes:
```


1$traits = class_uses_recursive(App\Models\User::class);




$traits = class_uses_recursive(App\Models\User::class);

```

#### [`collect()`](https://laravel.com/docs/12.x/helpers#method-collect)
The `collect` function creates a [collection](https://laravel.com/docs/12.x/collections) instance from the given value:
```


1$collection = collect(['Taylor', 'Abigail']);




$collection = collect(['Taylor', 'Abigail']);

```

#### [`config()`](https://laravel.com/docs/12.x/helpers#method-config)
The `config` function gets the value of a [configuration](https://laravel.com/docs/12.x/configuration) variable. The configuration values may be accessed using "dot" syntax, which includes the name of the file and the option you wish to access. You may also provide a default value that will be returned if the configuration option does not exist:
```


1$value = config('app.timezone');




2 



3$value = config('app.timezone', $default);




$value = config('app.timezone');

$value = config('app.timezone', $default);

```

You may set configuration variables at runtime by passing an array of key / value pairs. However, note that this function only affects the configuration value for the current request and does not update your actual configuration values:
```


1config(['app.debug' => true]);




config(['app.debug' => true]);

```

#### [`context()`](https://laravel.com/docs/12.x/helpers#method-context)
The `context` function gets the value from the current [context](https://laravel.com/docs/12.x/context). You may also provide a default value that will be returned if the context key does not exist:
```


1$value = context('trace_id');




2 



3$value = context('trace_id', $default);




$value = context('trace_id');

$value = context('trace_id', $default);

```

You may set context values by passing an array of key / value pairs:
```


1use Illuminate\Support\Str;




2 



3context(['trace_id' => Str::uuid()->toString()]);




use Illuminate\Support\Str;

context(['trace_id' => Str::uuid()->toString()]);

```

#### [`cookie()`](https://laravel.com/docs/12.x/helpers#method-cookie)
The `cookie` function creates a new [cookie](https://laravel.com/docs/12.x/requests#cookies) instance:
```


1$cookie = cookie('name', 'value', $minutes);




$cookie = cookie('name', 'value', $minutes);

```

#### [`csrf_field()`](https://laravel.com/docs/12.x/helpers#method-csrf-field)
The `csrf_field` function generates an HTML `hidden` input field containing the value of the CSRF token. For example, using [Blade syntax](https://laravel.com/docs/12.x/blade):
```


1{{ csrf_field() }}




{{ csrf_field() }}

```

#### [`csrf_token()`](https://laravel.com/docs/12.x/helpers#method-csrf-token)
The `csrf_token` function retrieves the value of the current CSRF token:
```


1$token = csrf_token();




$token = csrf_token();

```

#### [`decrypt()`](https://laravel.com/docs/12.x/helpers#method-decrypt)
The `decrypt` function [decrypts](https://laravel.com/docs/12.x/encryption) the given value. You may use this function as an alternative to the `Crypt` facade:
```


1$password = decrypt($value);




$password = decrypt($value);

```

For the inverse of `decrypt`, see the [encrypt](https://laravel.com/docs/12.x/helpers#method-encrypt) function.
#### [`dd()`](https://laravel.com/docs/12.x/helpers#method-dd)
The `dd` function dumps the given variables and ends the execution of the script:
```


1dd($value);




2 



3dd($value1, $value2, $value3, ...);




dd($value);

dd($value1, $value2, $value3, ...);

```

If you do not want to halt the execution of your script, use the [dump](https://laravel.com/docs/12.x/helpers#method-dump) function instead.
#### [`dispatch()`](https://laravel.com/docs/12.x/helpers#method-dispatch)
The `dispatch` function pushes the given [job](https://laravel.com/docs/12.x/queues#creating-jobs) onto the Laravel [job queue](https://laravel.com/docs/12.x/queues):
```


1dispatch(new App\Jobs\SendEmails);




dispatch(new App\Jobs\SendEmails);

```

#### [`dispatch_sync()`](https://laravel.com/docs/12.x/helpers#method-dispatch-sync)
The `dispatch_sync` function pushes the given job to the [sync](https://laravel.com/docs/12.x/queues#synchronous-dispatching) queue so that it is processed immediately:
```


1dispatch_sync(new App\Jobs\SendEmails);




dispatch_sync(new App\Jobs\SendEmails);

```

#### [`dump()`](https://laravel.com/docs/12.x/helpers#method-dump)
The `dump` function dumps the given variables:
```


1dump($value);




2 



3dump($value1, $value2, $value3, ...);




dump($value);

dump($value1, $value2, $value3, ...);

```

If you want to stop executing the script after dumping the variables, use the [dd](https://laravel.com/docs/12.x/helpers#method-dd) function instead.
#### [`encrypt()`](https://laravel.com/docs/12.x/helpers#method-encrypt)
The `encrypt` function [encrypts](https://laravel.com/docs/12.x/encryption) the given value. You may use this function as an alternative to the `Crypt` facade:
```


1$secret = encrypt('my-secret-value');




$secret = encrypt('my-secret-value');

```

For the inverse of `encrypt`, see the [decrypt](https://laravel.com/docs/12.x/helpers#method-decrypt) function.
#### [`env()`](https://laravel.com/docs/12.x/helpers#method-env)
The `env` function retrieves the value of an [environment variable](https://laravel.com/docs/12.x/configuration#environment-configuration) or returns a default value:
```


1$env = env('APP_ENV');




2 



3$env = env('APP_ENV', 'production');




$env = env('APP_ENV');

$env = env('APP_ENV', 'production');

```

If you execute the `config:cache` command during your deployment process, you should be sure that you are only calling the `env` function from within your configuration files. Once the configuration has been cached, the `.env` file will not be loaded and all calls to the `env` function will return external environment variables such as server-level or system-level environment variables or `null`.
#### [`event()`](https://laravel.com/docs/12.x/helpers#method-event)
The `event` function dispatches the given [event](https://laravel.com/docs/12.x/events) to its listeners:
```


1event(new UserRegistered($user));




event(new UserRegistered($user));

```

#### [`fake()`](https://laravel.com/docs/12.x/helpers#method-fake)
The `fake` function resolves a
```


1@for ($i = 0; $i < 10; $i++)




2    <dl>




3        <dt>Name</dt>




4        <dd>{{ fake()->name() }}</dd>




5 



6        <dt>Email</dt>




7        <dd>{{ fake()->unique()->safeEmail() }}</dd>




8    </dl>




9@endfor




@for ($i = 0; $i < 10; $i++)
    <dl>
        <dt>Name</dt>
        <dd>{{ fake()->name() }}</dd>

        <dt>Email</dt>
        <dd>{{ fake()->unique()->safeEmail() }}</dd>
    </dl>
@endfor

```

By default, the `fake` function will utilize the `app.faker_locale` configuration option in your `config/app.php` configuration. Typically, this configuration option is set via the `APP_FAKER_LOCALE` environment variable. You may also specify the locale by passing it to the `fake` function. Each locale will resolve an individual singleton:
```


1fake('nl_NL')->name()




fake('nl_NL')->name()

```

#### [`filled()`](https://laravel.com/docs/12.x/helpers#method-filled)
The `filled` function determines whether the given value is not "blank":
```


 1filled(0);




 2filled(true);




 3filled(false);




 4 



 5// true




 6 



 7filled('');




 8filled('   ');




 9filled(null);




10filled(collect());




11 



12// false




filled(0);
filled(true);
filled(false);

// true

filled('');
filled('   ');
filled(null);
filled(collect());

// false

```

For the inverse of `filled`, see the [blank](https://laravel.com/docs/12.x/helpers#method-blank) function.
#### [`info()`](https://laravel.com/docs/12.x/helpers#method-info)
The `info` function will write information to your application's [log](https://laravel.com/docs/12.x/logging):
```


1info('Some helpful information!');




info('Some helpful information!');

```

An array of contextual data may also be passed to the function:
```


1info('User login attempt failed.', ['id' => $user->id]);




info('User login attempt failed.', ['id' => $user->id]);

```

#### [`literal()`](https://laravel.com/docs/12.x/helpers#method-literal)
The `literal` function creates a new
```


1$obj = literal(




2    name: 'Joe',




3    languages: ['PHP', 'Ruby'],




4);




5 



6$obj->name; // 'Joe'




7$obj->languages; // ['PHP', 'Ruby']




$obj = literal(
    name: 'Joe',
    languages: ['PHP', 'Ruby'],
);

$obj->name; // 'Joe'
$obj->languages; // ['PHP', 'Ruby']

```

#### [`logger()`](https://laravel.com/docs/12.x/helpers#method-logger)
The `logger` function can be used to write a `debug` level message to the [log](https://laravel.com/docs/12.x/logging):
```


1logger('Debug message');




logger('Debug message');

```

An array of contextual data may also be passed to the function:
```


1logger('User has logged in.', ['id' => $user->id]);




logger('User has logged in.', ['id' => $user->id]);

```

A [logger](https://laravel.com/docs/12.x/logging) instance will be returned if no value is passed to the function:
```


1logger()->error('You are not allowed here.');




logger()->error('You are not allowed here.');

```

#### [`method_field()`](https://laravel.com/docs/12.x/helpers#method-method-field)
The `method_field` function generates an HTML `hidden` input field containing the spoofed value of the form's HTTP verb. For example, using [Blade syntax](https://laravel.com/docs/12.x/blade):
```


1<form method="POST">




2    {{ method_field('DELETE') }}




3</form>




<form method="POST">
    {{ method_field('DELETE') }}
</form>

```

#### [`now()`](https://laravel.com/docs/12.x/helpers#method-now)
The `now` function creates a new `Illuminate\Support\Carbon` instance for the current time:
```


1$now = now();




$now = now();

```

#### [`old()`](https://laravel.com/docs/12.x/helpers#method-old)
The `old` function [retrieves](https://laravel.com/docs/12.x/requests#retrieving-input) an [old input](https://laravel.com/docs/12.x/requests#old-input) value flashed into the session:
```


1$value = old('value');




2 



3$value = old('value', 'default');




$value = old('value');

$value = old('value', 'default');

```

Since the "default value" provided as the second argument to the `old` function is often an attribute of an Eloquent model, Laravel allows you to simply pass the entire Eloquent model as the second argument to the `old` function. When doing so, Laravel will assume the first argument provided to the `old` function is the name of the Eloquent attribute that should be considered the "default value":
```


1{{ old('name', $user->name) }}




2 



3// Is equivalent to...




4 



5{{ old('name', $user) }}




{{ old('name', $user->name) }}

// Is equivalent to...

{{ old('name', $user) }}

```

#### [`once()`](https://laravel.com/docs/12.x/helpers#method-once)
The `once` function executes the given callback and caches the result in memory for the duration of the request. Any subsequent calls to the `once` function with the same callback will return the previously cached result:
```


 1function random(): int




 2{




 3    return once(function () {




 4        return random_int(1, 1000);




 5    });




 6}




 7 



 8random(); // 123




 9random(); // 123 (cached result)




10random(); // 123 (cached result)




function random(): int
{
    return once(function () {
        return random_int(1, 1000);
    });
}

random(); // 123
random(); // 123 (cached result)
random(); // 123 (cached result)

```

When the `once` function is executed from within an object instance, the cached result will be unique to that object instance:
```


 1<?php




 2 



 3class NumberService




 4{




 5    public function all(): array




 6    {




 7        return once(fn () => [1, 2, 3]);




 8    }




 9}




10 



11$service = new NumberService;




12 



13$service->all();




14$service->all(); // (cached result)




15 



16$secondService = new NumberService;




17 



18$secondService->all();




19$secondService->all(); // (cached result)




<?php

class NumberService
{
    public function all(): array
    {
        return once(fn () => [1, 2, 3]);
    }
}

$service = new NumberService;

$service->all();
$service->all(); // (cached result)

$secondService = new NumberService;

$secondService->all();
$secondService->all(); // (cached result)

```

#### [`optional()`](https://laravel.com/docs/12.x/helpers#method-optional)
The `optional` function accepts any argument and allows you to access properties or call methods on that object. If the given object is `null`, properties and methods will return `null` instead of causing an error:
```


1return optional($user->address)->street;




2 



3{!! old('name', optional($user)->name) !!}




return optional($user->address)->street;

{!! old('name', optional($user)->name) !!}

```

The `optional` function also accepts a closure as its second argument. The closure will be invoked if the value provided as the first argument is not null:
```


1return optional(User::find($id), function (User $user) {




2    return $user->name;




3});




return optional(User::find($id), function (User $user) {
    return $user->name;
});

```

#### [`policy()`](https://laravel.com/docs/12.x/helpers#method-policy)
The `policy` method retrieves a [policy](https://laravel.com/docs/12.x/authorization#creating-policies) instance for a given class:
```


1$policy = policy(App\Models\User::class);




$policy = policy(App\Models\User::class);

```

#### [`redirect()`](https://laravel.com/docs/12.x/helpers#method-redirect)
The `redirect` function returns a [redirect HTTP response](https://laravel.com/docs/12.x/responses#redirects), or returns the redirector instance if called with no arguments:
```


1return redirect($to = null, $status = 302, $headers = [], $secure = null);




2 



3return redirect('/home');




4 



5return redirect()->route('route.name');




return redirect($to = null, $status = 302, $headers = [], $secure = null);

return redirect('/home');

return redirect()->route('route.name');

```

#### [`report()`](https://laravel.com/docs/12.x/helpers#method-report)
The `report` function will report an exception using your [exception handler](https://laravel.com/docs/12.x/errors#handling-exceptions):
```


1report($e);




report($e);

```

The `report` function also accepts a string as an argument. When a string is given to the function, the function will create an exception with the given string as its message:
```


1report('Something went wrong.');




report('Something went wrong.');

```

#### [`report_if()`](https://laravel.com/docs/12.x/helpers#method-report-if)
The `report_if` function will report an exception using your [exception handler](https://laravel.com/docs/12.x/errors#handling-exceptions) if a given boolean expression evaluates to `true`:
```


1report_if($shouldReport, $e);




2 



3report_if($shouldReport, 'Something went wrong.');




report_if($shouldReport, $e);

report_if($shouldReport, 'Something went wrong.');

```

#### [`report_unless()`](https://laravel.com/docs/12.x/helpers#method-report-unless)
The `report_unless` function will report an exception using your [exception handler](https://laravel.com/docs/12.x/errors#handling-exceptions) if a given boolean expression evaluates to `false`:
```


1report_unless($reportingDisabled, $e);




2 



3report_unless($reportingDisabled, 'Something went wrong.');




report_unless($reportingDisabled, $e);

report_unless($reportingDisabled, 'Something went wrong.');

```

#### [`request()`](https://laravel.com/docs/12.x/helpers#method-request)
The `request` function returns the current [request](https://laravel.com/docs/12.x/requests) instance or obtains an input field's value from the current request:
```


1$request = request();




2 



3$value = request('key', $default);




$request = request();

$value = request('key', $default);

```

#### [`rescue()`](https://laravel.com/docs/12.x/helpers#method-rescue)
The `rescue` function executes the given closure and catches any exceptions that occur during its execution. All exceptions that are caught will be sent to your [exception handler](https://laravel.com/docs/12.x/errors#handling-exceptions); however, the request will continue processing:
```


1return rescue(function () {




2    return $this->method();




3});




return rescue(function () {
    return $this->method();
});

```

You may also pass a second argument to the `rescue` function. This argument will be the "default" value that should be returned if an exception occurs while executing the closure:
```


1return rescue(function () {




2    return $this->method();




3}, false);




4 



5return rescue(function () {




6    return $this->method();




7}, function () {




8    return $this->failure();




9});




return rescue(function () {
    return $this->method();
}, false);

return rescue(function () {
    return $this->method();
}, function () {
    return $this->failure();
});

```

A `report` argument may be provided to the `rescue` function to determine if the exception should be reported via the `report` function:
```


1return rescue(function () {




2    return $this->method();




3}, report: function (Throwable $throwable) {




4    return $throwable instanceof InvalidArgumentException;




5});




return rescue(function () {
    return $this->method();
}, report: function (Throwable $throwable) {
    return $throwable instanceof InvalidArgumentException;
});

```

#### [`resolve()`](https://laravel.com/docs/12.x/helpers#method-resolve)
The `resolve` function resolves a given class or interface name to an instance using the [service container](https://laravel.com/docs/12.x/container):
```


1$api = resolve('HelpSpot\API');




$api = resolve('HelpSpot\API');

```

#### [`response()`](https://laravel.com/docs/12.x/helpers#method-response)
The `response` function creates a [response](https://laravel.com/docs/12.x/responses) instance or obtains an instance of the response factory:
```


1return response('Hello World', 200, $headers);




2 



3return response()->json(['foo' => 'bar'], 200, $headers);




return response('Hello World', 200, $headers);

return response()->json(['foo' => 'bar'], 200, $headers);

```

#### [`retry()`](https://laravel.com/docs/12.x/helpers#method-retry)
The `retry` function attempts to execute the given callback until the given maximum attempt threshold is met. If the callback does not throw an exception, its return value will be returned. If the callback throws an exception, it will automatically be retried. If the maximum attempt count is exceeded, the exception will be thrown:
```


1return retry(5, function () {




2    // Attempt 5 times while resting 100ms between attempts...




3}, 100);




return retry(5, function () {
    // Attempt 5 times while resting 100ms between attempts...
}, 100);

```

If you would like to manually calculate the number of milliseconds to sleep between attempts, you may pass a closure as the third argument to the `retry` function:
```


1use Exception;




2 



3return retry(5, function () {




4    // ...




5}, function (int $attempt, Exception $exception) {




6    return $attempt * 100;




7});




use Exception;

return retry(5, function () {
    // ...
}, function (int $attempt, Exception $exception) {
    return $attempt * 100;
});

```

For convenience, you may provide an array as the first argument to the `retry` function. This array will be used to determine how many milliseconds to sleep between subsequent attempts:
```


1return retry([100, 200], function () {




2    // Sleep for 100ms on first retry, 200ms on second retry...




3});




return retry([100, 200], function () {
    // Sleep for 100ms on first retry, 200ms on second retry...
});

```

To only retry under specific conditions, you may pass a closure as the fourth argument to the `retry` function:
```


1use App\Exceptions\TemporaryException;




2use Exception;




3 



4return retry(5, function () {




5    // ...




6}, 100, function (Exception $exception) {




7    return $exception instanceof TemporaryException;




8});




use App\Exceptions\TemporaryException;
use Exception;

return retry(5, function () {
    // ...
}, 100, function (Exception $exception) {
    return $exception instanceof TemporaryException;
});

```

#### [`session()`](https://laravel.com/docs/12.x/helpers#method-session)
The `session` function may be used to get or set [session](https://laravel.com/docs/12.x/session) values:
```


1$value = session('key');




$value = session('key');

```

You may set values by passing an array of key / value pairs to the function:
```


1session(['chairs' => 7, 'instruments' => 3]);




session(['chairs' => 7, 'instruments' => 3]);

```

The session store will be returned if no value is passed to the function:
```


1$value = session()->get('key');




2 



3session()->put('key', $value);




$value = session()->get('key');

session()->put('key', $value);

```

#### [`tap()`](https://laravel.com/docs/12.x/helpers#method-tap)
The `tap` function accepts two arguments: an arbitrary `$value` and a closure. The `$value` will be passed to the closure and then be returned by the `tap` function. The return value of the closure is irrelevant:
```


1$user = tap(User::first(), function (User $user) {




2    $user->name = 'Taylor';




3 



4    $user->save();




5});




$user = tap(User::first(), function (User $user) {
    $user->name = 'Taylor';

    $user->save();
});

```

If no closure is passed to the `tap` function, you may call any method on the given `$value`. The return value of the method you call will always be `$value`, regardless of what the method actually returns in its definition. For example, the Eloquent `update` method typically returns an integer. However, we can force the method to return the model itself by chaining the `update` method call through the `tap` function:
```


1$user = tap($user)->update([




2    'name' => $name,




3    'email' => $email,




4]);




$user = tap($user)->update([
    'name' => $name,
    'email' => $email,
]);

```

To add a `tap` method to a class, you may add the `Illuminate\Support\Traits\Tappable` trait to the class. The `tap` method of this trait accepts a Closure as its only argument. The object instance itself will be passed to the Closure and then be returned by the `tap` method:
```


1return $user->tap(function (User $user) {




2    // ...




3});




return $user->tap(function (User $user) {
    // ...
});

```

#### [`throw_if()`](https://laravel.com/docs/12.x/helpers#method-throw-if)
The `throw_if` function throws the given exception if a given boolean expression evaluates to `true`:
```


1throw_if(! Auth::user()->isAdmin(), AuthorizationException::class);




2 



3throw_if(




4    ! Auth::user()->isAdmin(),




5    AuthorizationException::class,




6    'You are not allowed to access this page.'




7);




throw_if(! Auth::user()->isAdmin(), AuthorizationException::class);

throw_if(
    ! Auth::user()->isAdmin(),
    AuthorizationException::class,
    'You are not allowed to access this page.'
);

```

#### [`throw_unless()`](https://laravel.com/docs/12.x/helpers#method-throw-unless)
The `throw_unless` function throws the given exception if a given boolean expression evaluates to `false`:
```


1throw_unless(Auth::user()->isAdmin(), AuthorizationException::class);




2 



3throw_unless(




4    Auth::user()->isAdmin(),




5    AuthorizationException::class,




6    'You are not allowed to access this page.'




7);




throw_unless(Auth::user()->isAdmin(), AuthorizationException::class);

throw_unless(
    Auth::user()->isAdmin(),
    AuthorizationException::class,
    'You are not allowed to access this page.'
);

```

#### [`today()`](https://laravel.com/docs/12.x/helpers#method-today)
The `today` function creates a new `Illuminate\Support\Carbon` instance for the current date:
```


1$today = today();




$today = today();

```

#### [`trait_uses_recursive()`](https://laravel.com/docs/12.x/helpers#method-trait-uses-recursive)
The `trait_uses_recursive` function returns all traits used by a trait:
```


1$traits = trait_uses_recursive(\Illuminate\Notifications\Notifiable::class);




$traits = trait_uses_recursive(\Illuminate\Notifications\Notifiable::class);

```

#### [`transform()`](https://laravel.com/docs/12.x/helpers#method-transform)
The `transform` function executes a closure on a given value if the value is not [blank](https://laravel.com/docs/12.x/helpers#method-blank) and then returns the return value of the closure:
```


1$callback = function (int $value) {




2    return $value * 2;




3};




4 



5$result = transform(5, $callback);




6 



7// 10




$callback = function (int $value) {
    return $value * 2;
};

$result = transform(5, $callback);

// 10

```

A default value or closure may be passed as the third argument to the function. This value will be returned if the given value is blank:
```


1$result = transform(null, $callback, 'The value is blank');




2 



3// The value is blank




$result = transform(null, $callback, 'The value is blank');

// The value is blank

```

#### [`validator()`](https://laravel.com/docs/12.x/helpers#method-validator)
The `validator` function creates a new [validator](https://laravel.com/docs/12.x/validation) instance with the given arguments. You may use it as an alternative to the `Validator` facade:
```


1$validator = validator($data, $rules, $messages);




$validator = validator($data, $rules, $messages);

```

#### [`value()`](https://laravel.com/docs/12.x/helpers#method-value)
The `value` function returns the value it is given. However, if you pass a closure to the function, the closure will be executed and its returned value will be returned:
```


1$result = value(true);




2 



3// true




4 



5$result = value(function () {




6    return false;




7});




8 



9// false




$result = value(true);

// true

$result = value(function () {
    return false;
});

// false

```

Additional arguments may be passed to the `value` function. If the first argument is a closure then the additional parameters will be passed to the closure as arguments, otherwise they will be ignored:
```


1$result = value(function (string $name) {




2    return $name;




3}, 'Taylor');




4 



5// 'Taylor'




$result = value(function (string $name) {
    return $name;
}, 'Taylor');

// 'Taylor'

```

#### [`view()`](https://laravel.com/docs/12.x/helpers#method-view)
The `view` function retrieves a [view](https://laravel.com/docs/12.x/views) instance:
```


1return view('auth.login');




return view('auth.login');

```

#### [`with()`](https://laravel.com/docs/12.x/helpers#method-with)
The `with` function returns the value it is given. If a closure is passed as the second argument to the function, the closure will be executed and its returned value will be returned:
```


 1$callback = function (mixed $value) {




 2    return is_numeric($value) ? $value * 2 : 0;




 3};




 4 



 5$result = with(5, $callback);




 6 



 7// 10




 8 



 9$result = with(null, $callback);




10 



11// 0




12 



13$result = with(5, null);




14 



15// 5




$callback = function (mixed $value) {
    return is_numeric($value) ? $value * 2 : 0;
};

$result = with(5, $callback);

// 10

$result = with(null, $callback);

// 0

$result = with(5, null);

// 5

```

#### [`when()`](https://laravel.com/docs/12.x/helpers#method-when)
The `when` function returns the value it is given if a given condition evaluates to `true`. Otherwise, `null` is returned. If a closure is passed as the second argument to the function, the closure will be executed and its returned value will be returned:
```


1$value = when(true, 'Hello World');




2 



3$value = when(true, fn () => 'Hello World');




$value = when(true, 'Hello World');

$value = when(true, fn () => 'Hello World');

```

The `when` function is primarily useful for conditionally rendering HTML attributes:
```


1<div {!! when($condition, 'wire:poll="calculate"') !!}>




2    ...




3</div>




<div {!! when($condition, 'wire:poll="calculate"') !!}>
    ...
</div>

```
