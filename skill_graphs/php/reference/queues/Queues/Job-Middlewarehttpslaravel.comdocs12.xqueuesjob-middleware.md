## [Job Middleware](https://laravel.com/docs/12.x/queues#job-middleware)
Job middleware allow you to wrap custom logic around the execution of queued jobs, reducing boilerplate in the jobs themselves. For example, consider the following `handle` method which leverages Laravel's Redis rate limiting features to allow only one job to process every five seconds:
```


 1use Illuminate\Support\Facades\Redis;




 2 



 3/**




 4 * Execute the job.




 5 */




 6public function handle(): void




 7{




 8    Redis::throttle('key')->block(0)->allow(1)->every(5)->then(function () {




 9        info('Lock obtained...');




10 



11        // Handle job...




12    }, function () {




13        // Could not obtain lock...




14 



15        return $this->release(5);




16    });




17}




use Illuminate\Support\Facades\Redis;

/**
 * Execute the job.
 */
public function handle(): void
{
    Redis::throttle('key')->block(0)->allow(1)->every(5)->then(function () {
        info('Lock obtained...');

        // Handle job...
    }, function () {
        // Could not obtain lock...

        return $this->release(5);
    });
}

```

While this code is valid, the implementation of the `handle` method becomes noisy since it is cluttered with Redis rate limiting logic. In addition, this rate limiting logic must be duplicated for any other jobs that we want to rate limit. Instead of rate limiting in the handle method, we could define a job middleware that handles rate limiting:
```


 1<?php




 2 



 3namespace App\Jobs\Middleware;




 4 



 5use Closure;




 6use Illuminate\Support\Facades\Redis;




 7 



 8class RateLimited




 9{




10    /**




11     * Process the queued job.




12     *




13     * @param  \Closure(object): void  $next




14     */




15    public function handle(object $job, Closure $next): void




16    {




17        Redis::throttle('key')




18            ->block(0)->allow(1)->every(5)




19            ->then(function () use ($job, $next) {




20                // Lock obtained...




21 



22                $next($job);




23            }, function () use ($job) {




24                // Could not obtain lock...




25 



26                $job->release(5);




27            });




28    }




29}




<?php

namespace App\Jobs\Middleware;

use Closure;
use Illuminate\Support\Facades\Redis;

class RateLimited
{
    /**
     * Process the queued job.
     *
     * @param  \Closure(object): void  $next
     */
    public function handle(object $job, Closure $next): void
    {
        Redis::throttle('key')
            ->block(0)->allow(1)->every(5)
            ->then(function () use ($job, $next) {
                // Lock obtained...

                $next($job);
            }, function () use ($job) {
                // Could not obtain lock...

                $job->release(5);
            });
    }
}

```

As you can see, like [route middleware](https://laravel.com/docs/12.x/middleware), job middleware receive the job being processed and a callback that should be invoked to continue processing the job.
You can generate a new job middleware class using the `make:job-middleware` Artisan command. After creating job middleware, they may be attached to a job by returning them from the job's `middleware` method. This method does not exist on jobs scaffolded by the `make:job` Artisan command, so you will need to manually add it to your job class:
```


 1use App\Jobs\Middleware\RateLimited;




 2 



 3/**




 4 * Get the middleware the job should pass through.




 5 *




 6 * @return array<int, object>




 7 */




 8public function middleware(): array




 9{




10    return [new RateLimited];




11}




use App\Jobs\Middleware\RateLimited;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [new RateLimited];
}

```

Job middleware can also be assigned to [queueable event listeners](https://laravel.com/docs/12.x/events#queued-event-listeners), [mailables](https://laravel.com/docs/12.x/mail#queueing-mail), and [notifications](https://laravel.com/docs/12.x/notifications#queueing-notifications).
### [Rate Limiting](https://laravel.com/docs/12.x/queues#rate-limiting)
Although we just demonstrated how to write your own rate limiting job middleware, Laravel actually includes a rate limiting middleware that you may utilize to rate limit jobs. Like [route rate limiters](https://laravel.com/docs/12.x/routing#defining-rate-limiters), job rate limiters are defined using the `RateLimiter` facade's `for` method.
For example, you may wish to allow users to backup their data once per hour while imposing no such limit on premium customers. To accomplish this, you may define a `RateLimiter` in the `boot` method of your `AppServiceProvider`:
```


 1use Illuminate\Cache\RateLimiting\Limit;




 2use Illuminate\Support\Facades\RateLimiter;




 3 



 4/**




 5 * Bootstrap any application services.




 6 */




 7public function boot(): void




 8{




 9    RateLimiter::for('backups', function (object $job) {




10        return $job->user->vipCustomer()




11            ? Limit::none()




12            : Limit::perHour(1)->by($job->user->id);




13    });




14}




use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Support\Facades\RateLimiter;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    RateLimiter::for('backups', function (object $job) {
        return $job->user->vipCustomer()
            ? Limit::none()
            : Limit::perHour(1)->by($job->user->id);
    });
}

```

In the example above, we defined an hourly rate limit; however, you may easily define a rate limit based on minutes using the `perMinute` method. In addition, you may pass any value you wish to the `by` method of the rate limit; however, this value is most often used to segment rate limits by customer:
```


1return Limit::perMinute(50)->by($job->user->id);




return Limit::perMinute(50)->by($job->user->id);

```

Once you have defined your rate limit, you may attach the rate limiter to your job using the `Illuminate\Queue\Middleware\RateLimited` middleware. Each time the job exceeds the rate limit, this middleware will release the job back to the queue with an appropriate delay based on the rate limit duration:
```


 1use Illuminate\Queue\Middleware\RateLimited;




 2 



 3/**




 4 * Get the middleware the job should pass through.




 5 *




 6 * @return array<int, object>




 7 */




 8public function middleware(): array




 9{




10    return [new RateLimited('backups')];




11}




use Illuminate\Queue\Middleware\RateLimited;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [new RateLimited('backups')];
}

```

Releasing a rate limited job back onto the queue will still increment the job's total number of `attempts`. You may wish to tune your `tries` and `maxExceptions` properties on your job class accordingly. Or, you may wish to use the [retryUntil method](https://laravel.com/docs/12.x/queues#time-based-attempts) to define the amount of time until the job should no longer be attempted.
Using the `releaseAfter` method, you may also specify the number of seconds that must elapse before the released job will be attempted again:
```


1/**




2 * Get the middleware the job should pass through.




3 *




4 * @return array<int, object>




5 */




6public function middleware(): array




7{




8    return [(new RateLimited('backups'))->releaseAfter(60)];




9}




/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new RateLimited('backups'))->releaseAfter(60)];
}

```

If you do not want a job to be retried when it is rate limited, you may use the `dontRelease` method:
```


1/**




2 * Get the middleware the job should pass through.




3 *




4 * @return array<int, object>




5 */




6public function middleware(): array




7{




8    return [(new RateLimited('backups'))->dontRelease()];




9}




/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new RateLimited('backups'))->dontRelease()];
}

```

#### [Rate Limiting With Redis](https://laravel.com/docs/12.x/queues#rate-limiting-with-redis)
If you are using Redis, you may use the `Illuminate\Queue\Middleware\RateLimitedWithRedis` middleware, which is fine-tuned for Redis and more efficient than the basic rate limiting middleware:
```


1use Illuminate\Queue\Middleware\RateLimitedWithRedis;




2 



3public function middleware(): array




4{




5    return [new RateLimitedWithRedis('backups')];




6}




use Illuminate\Queue\Middleware\RateLimitedWithRedis;

public function middleware(): array
{
    return [new RateLimitedWithRedis('backups')];
}

```

The `connection` method may be used to specify which Redis connection the middleware should use:
```


1return [(new RateLimitedWithRedis('backups'))->connection('limiter')];




return [(new RateLimitedWithRedis('backups'))->connection('limiter')];

```

### [Preventing Job Overlaps](https://laravel.com/docs/12.x/queues#preventing-job-overlaps)
Laravel includes an `Illuminate\Queue\Middleware\WithoutOverlapping` middleware that allows you to prevent job overlaps based on an arbitrary key. This can be helpful when a queued job is modifying a resource that should only be modified by one job at a time.
For example, let's imagine you have a queued job that updates a user's credit score and you want to prevent credit score update job overlaps for the same user ID. To accomplish this, you can return the `WithoutOverlapping` middleware from your job's `middleware` method:
```


 1use Illuminate\Queue\Middleware\WithoutOverlapping;




 2 



 3/**




 4 * Get the middleware the job should pass through.




 5 *




 6 * @return array<int, object>




 7 */




 8public function middleware(): array




 9{




10    return [new WithoutOverlapping($this->user->id)];




11}




use Illuminate\Queue\Middleware\WithoutOverlapping;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [new WithoutOverlapping($this->user->id)];
}

```

Releasing an overlapping job back onto the queue will still increment the job's total number of attempts. You may wish to tune your `tries` and `maxExceptions` properties on your job class accordingly. For example, leaving the `tries` property to 1 as it is by default would prevent any overlapping job from being retried later.
Any overlapping jobs of the same type will be released back to the queue. You may also specify the number of seconds that must elapse before the released job will be attempted again:
```


1/**




2 * Get the middleware the job should pass through.




3 *




4 * @return array<int, object>




5 */




6public function middleware(): array




7{




8    return [(new WithoutOverlapping($this->order->id))->releaseAfter(60)];




9}




/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new WithoutOverlapping($this->order->id))->releaseAfter(60)];
}

```

If you wish to immediately delete any overlapping jobs so that they will not be retried, you may use the `dontRelease` method:
```


1/**




2 * Get the middleware the job should pass through.




3 *




4 * @return array<int, object>




5 */




6public function middleware(): array




7{




8    return [(new WithoutOverlapping($this->order->id))->dontRelease()];




9}




/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new WithoutOverlapping($this->order->id))->dontRelease()];
}

```

The `WithoutOverlapping` middleware is powered by Laravel's atomic lock feature. Sometimes, your job may unexpectedly fail or timeout in such a way that the lock is not released. Therefore, you may explicitly define a lock expiration time using the `expireAfter` method. For example, the example below will instruct Laravel to release the `WithoutOverlapping` lock three minutes after the job has started processing:
```


1/**




2 * Get the middleware the job should pass through.




3 *




4 * @return array<int, object>




5 */




6public function middleware(): array




7{




8    return [(new WithoutOverlapping($this->order->id))->expireAfter(180)];




9}




/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new WithoutOverlapping($this->order->id))->expireAfter(180)];
}

```

The `WithoutOverlapping` middleware requires a cache driver that supports [locks](https://laravel.com/docs/12.x/cache#atomic-locks). Currently, the `memcached`, `redis`, `dynamodb`, `database`, `file`, and `array` cache drivers support atomic locks.
#### [Sharing Lock Keys Across Job Classes](https://laravel.com/docs/12.x/queues#sharing-lock-keys)
By default, the `WithoutOverlapping` middleware will only prevent overlapping jobs of the same class. So, although two different job classes may use the same lock key, they will not be prevented from overlapping. However, you can instruct Laravel to apply the key across job classes using the `shared` method:
```


 1use Illuminate\Queue\Middleware\WithoutOverlapping;




 2 



 3class ProviderIsDown




 4{




 5    // ...




 6 



 7    public function middleware(): array




 8    {




 9        return [




10            (new WithoutOverlapping("status:{$this->provider}"))->shared(),




11        ];




12    }




13}




14 



15class ProviderIsUp




16{




17    // ...




18 



19    public function middleware(): array




20    {




21        return [




22            (new WithoutOverlapping("status:{$this->provider}"))->shared(),




23        ];




24    }




25}




use Illuminate\Queue\Middleware\WithoutOverlapping;

class ProviderIsDown
{
    // ...

    public function middleware(): array
    {
        return [
            (new WithoutOverlapping("status:{$this->provider}"))->shared(),
        ];
    }
}

class ProviderIsUp
{
    // ...

    public function middleware(): array
    {
        return [
            (new WithoutOverlapping("status:{$this->provider}"))->shared(),
        ];
    }
}

```

### [Throttling Exceptions](https://laravel.com/docs/12.x/queues#throttling-exceptions)
Laravel includes a `Illuminate\Queue\Middleware\ThrottlesExceptions` middleware that allows you to throttle exceptions. Once the job throws a given number of exceptions, all further attempts to execute the job are delayed until a specified time interval lapses. This middleware is particularly useful for jobs that interact with third-party services that are unstable.
For example, let's imagine a queued job that interacts with a third-party API that begins throwing exceptions. To throttle exceptions, you can return the `ThrottlesExceptions` middleware from your job's `middleware` method. Typically, this middleware should be paired with a job that implements [time based attempts](https://laravel.com/docs/12.x/queues#time-based-attempts):
```


 1use DateTime;




 2use Illuminate\Queue\Middleware\ThrottlesExceptions;




 3 



 4/**




 5 * Get the middleware the job should pass through.




 6 *




 7 * @return array<int, object>




 8 */




 9public function middleware(): array




10{




11    return [new ThrottlesExceptions(10, 5 * 60)];




12}




13 



14/**




15 * Determine the time at which the job should timeout.




16 */




17public function retryUntil(): DateTime




18{




19    return now()->plus(minutes: 30);




20}




use DateTime;
use Illuminate\Queue\Middleware\ThrottlesExceptions;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [new ThrottlesExceptions(10, 5 * 60)];
}

/**
 * Determine the time at which the job should timeout.
 */
public function retryUntil(): DateTime
{
    return now()->plus(minutes: 30);
}

```

The first constructor argument accepted by the middleware is the number of exceptions the job can throw before being throttled, while the second constructor argument is the number of seconds that should elapse before the job is attempted again once it has been throttled. In the code example above, if the job throws 10 consecutive exceptions, we will wait 5 minutes before attempting the job again, constrained by the 30-minute time limit.
When a job throws an exception but the exception threshold has not yet been reached, the job will typically be retried immediately. However, you may specify the number of minutes such a job should be delayed by calling the `backoff` method when attaching the middleware to the job:
```


 1use Illuminate\Queue\Middleware\ThrottlesExceptions;




 2 



 3/**




 4 * Get the middleware the job should pass through.




 5 *




 6 * @return array<int, object>




 7 */




 8public function middleware(): array




 9{




10    return [(new ThrottlesExceptions(10, 5 * 60))->backoff(5)];




11}




use Illuminate\Queue\Middleware\ThrottlesExceptions;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new ThrottlesExceptions(10, 5 * 60))->backoff(5)];
}

```

Internally, this middleware uses Laravel's cache system to implement rate limiting, and the job's class name is utilized as the cache "key". You may override this key by calling the `by` method when attaching the middleware to your job. This may be useful if you have multiple jobs interacting with the same third-party service and you would like them to share a common throttling "bucket" ensuring they respect a single shared limit:
```


 1use Illuminate\Queue\Middleware\ThrottlesExceptions;




 2 



 3/**




 4 * Get the middleware the job should pass through.




 5 *




 6 * @return array<int, object>




 7 */




 8public function middleware(): array




 9{




10    return [(new ThrottlesExceptions(10, 10 * 60))->by('key')];




11}




use Illuminate\Queue\Middleware\ThrottlesExceptions;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new ThrottlesExceptions(10, 10 * 60))->by('key')];
}

```

By default, this middleware will throttle every exception. You can modify this behavior by invoking the `when` method when attaching the middleware to your job. The exception will then only be throttled if the closure provided to the `when` method returns `true`:
```


 1use Illuminate\Http\Client\HttpClientException;




 2use Illuminate\Queue\Middleware\ThrottlesExceptions;




 3 



 4/**




 5 * Get the middleware the job should pass through.




 6 *




 7 * @return array<int, object>




 8 */




 9public function middleware(): array




10{




11    return [(new ThrottlesExceptions(10, 10 * 60))->when(




12        fn (Throwable $throwable) => $throwable instanceof HttpClientException




13    )];




14}




use Illuminate\Http\Client\HttpClientException;
use Illuminate\Queue\Middleware\ThrottlesExceptions;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new ThrottlesExceptions(10, 10 * 60))->when(
        fn (Throwable $throwable) => $throwable instanceof HttpClientException
    )];
}

```

Unlike the `when` method, which releases the job back onto the queue or throws an exception, the `deleteWhen` method allows you to delete the job entirely when a given exception occurs:
```


 1use App\Exceptions\CustomerDeletedException;




 2use Illuminate\Queue\Middleware\ThrottlesExceptions;




 3 



 4/**




 5 * Get the middleware the job should pass through.




 6 *




 7 * @return array<int, object>




 8 */




 9public function middleware(): array




10{




11    return [(new ThrottlesExceptions(2, 10 * 60))->deleteWhen(CustomerDeletedException::class)];




12}




use App\Exceptions\CustomerDeletedException;
use Illuminate\Queue\Middleware\ThrottlesExceptions;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new ThrottlesExceptions(2, 10 * 60))->deleteWhen(CustomerDeletedException::class)];
}

```

If you would like to have the throttled exceptions reported to your application's exception handler, you can do so by invoking the `report` method when attaching the middleware to your job. Optionally, you may provide a closure to the `report` method and the exception will only be reported if the given closure returns `true`:
```


 1use Illuminate\Http\Client\HttpClientException;




 2use Illuminate\Queue\Middleware\ThrottlesExceptions;




 3 



 4/**




 5 * Get the middleware the job should pass through.




 6 *




 7 * @return array<int, object>




 8 */




 9public function middleware(): array




10{




11    return [(new ThrottlesExceptions(10, 10 * 60))->report(




12        fn (Throwable $throwable) => $throwable instanceof HttpClientException




13    )];




14}




use Illuminate\Http\Client\HttpClientException;
use Illuminate\Queue\Middleware\ThrottlesExceptions;

/**
 * Get the middleware the job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(): array
{
    return [(new ThrottlesExceptions(10, 10 * 60))->report(
        fn (Throwable $throwable) => $throwable instanceof HttpClientException
    )];
}

```

#### [Throttling Exceptions With Redis](https://laravel.com/docs/12.x/queues#throttling-exceptions-with-redis)
If you are using Redis, you may use the `Illuminate\Queue\Middleware\ThrottlesExceptionsWithRedis` middleware, which is fine-tuned for Redis and more efficient than the basic exception throttling middleware:
```


1use Illuminate\Queue\Middleware\ThrottlesExceptionsWithRedis;




2 



3public function middleware(): array




4{




5    return [new ThrottlesExceptionsWithRedis(10, 10 * 60)];




6}




use Illuminate\Queue\Middleware\ThrottlesExceptionsWithRedis;

public function middleware(): array
{
    return [new ThrottlesExceptionsWithRedis(10, 10 * 60)];
}

```

The `connection` method may be used to specify which Redis connection the middleware should use:
```


1return [(new ThrottlesExceptionsWithRedis(10, 10 * 60))->connection('limiter')];




return [(new ThrottlesExceptionsWithRedis(10, 10 * 60))->connection('limiter')];

```

### [Skipping Jobs](https://laravel.com/docs/12.x/queues#skipping-jobs)
The `Skip` middleware allows you to specify that a job should be skipped / deleted without needing to modify the job's logic. The `Skip::when` method will delete the job if the given condition evaluates to `true`, while the `Skip::unless` method will delete the job if the condition evaluates to `false`:
```


 1use Illuminate\Queue\Middleware\Skip;




 2 



 3/**




 4 * Get the middleware the job should pass through.




 5 */




 6public function middleware(): array




 7{




 8    return [




 9        Skip::when($condition),




10    ];




11}




use Illuminate\Queue\Middleware\Skip;

/**
 * Get the middleware the job should pass through.
 */
public function middleware(): array
{
    return [
        Skip::when($condition),
    ];
}

```

You can also pass a `Closure` to the `when` and `unless` methods for more complex conditional evaluation:
```


 1use Illuminate\Queue\Middleware\Skip;




 2 



 3/**




 4 * Get the middleware the job should pass through.




 5 */




 6public function middleware(): array




 7{




 8    return [




 9        Skip::when(function (): bool {




10            return $this->shouldSkip();




11        }),




12    ];




13}




use Illuminate\Queue\Middleware\Skip;

/**
 * Get the middleware the job should pass through.
 */
public function middleware(): array
{
    return [
        Skip::when(function (): bool {
            return $this->shouldSkip();
        }),
    ];
}

```
