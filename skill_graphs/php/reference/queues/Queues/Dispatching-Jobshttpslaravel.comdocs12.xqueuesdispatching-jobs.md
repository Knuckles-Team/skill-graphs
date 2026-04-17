## [Dispatching Jobs](https://laravel.com/docs/12.x/queues#dispatching-jobs)
Once you have written your job class, you may dispatch it using the `dispatch` method on the job itself. The arguments passed to the `dispatch` method will be given to the job's constructor:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Jobs\ProcessPodcast;




 6use App\Models\Podcast;




 7use Illuminate\Http\RedirectResponse;




 8use Illuminate\Http\Request;




 9 



10class PodcastController extends Controller




11{




12    /**




13     * Store a new podcast.




14     */




15    public function store(Request $request): RedirectResponse




16    {




17        $podcast = Podcast::create(/* ... */);




18 



19        // ...




20 



21        ProcessPodcast::dispatch($podcast);




22 



23        return redirect('/podcasts');




24    }




25}




<?php

namespace App\Http\Controllers;

use App\Jobs\ProcessPodcast;
use App\Models\Podcast;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class PodcastController extends Controller
{
    /**
     * Store a new podcast.
     */
    public function store(Request $request): RedirectResponse
    {
        $podcast = Podcast::create(/* ... */);

        // ...

        ProcessPodcast::dispatch($podcast);

        return redirect('/podcasts');
    }
}

```

If you would like to conditionally dispatch a job, you may use the `dispatchIf` and `dispatchUnless` methods:
```


1ProcessPodcast::dispatchIf($accountActive, $podcast);




2 



3ProcessPodcast::dispatchUnless($accountSuspended, $podcast);




ProcessPodcast::dispatchIf($accountActive, $podcast);

ProcessPodcast::dispatchUnless($accountSuspended, $podcast);

```

In new Laravel applications, the `database` connection is defined as the default queue. You may specify a different default queue connection by changing the `QUEUE_CONNECTION` environment variable in your application's `.env` file.
### [Delayed Dispatching](https://laravel.com/docs/12.x/queues#delayed-dispatching)
If you would like to specify that a job should not be immediately available for processing by a queue worker, you may use the `delay` method when dispatching the job. For example, let's specify that a job should not be available for processing until 10 minutes after it has been dispatched:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Jobs\ProcessPodcast;




 6use App\Models\Podcast;




 7use Illuminate\Http\RedirectResponse;




 8use Illuminate\Http\Request;




 9 



10class PodcastController extends Controller




11{




12    /**




13     * Store a new podcast.




14     */




15    public function store(Request $request): RedirectResponse




16    {




17        $podcast = Podcast::create(/* ... */);




18 



19        // ...




20 



21        ProcessPodcast::dispatch($podcast)




22            ->delay(now()->plus(minutes: 10));




23 



24        return redirect('/podcasts');




25    }




26}




<?php

namespace App\Http\Controllers;

use App\Jobs\ProcessPodcast;
use App\Models\Podcast;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class PodcastController extends Controller
{
    /**
     * Store a new podcast.
     */
    public function store(Request $request): RedirectResponse
    {
        $podcast = Podcast::create(/* ... */);

        // ...

        ProcessPodcast::dispatch($podcast)
            ->delay(now()->plus(minutes: 10));

        return redirect('/podcasts');
    }
}

```

In some cases, jobs may have a default delay configured. If you need to bypass this delay and dispatch a job for immediate processing, you may use the `withoutDelay` method:
```


1ProcessPodcast::dispatch($podcast)->withoutDelay();




ProcessPodcast::dispatch($podcast)->withoutDelay();

```

The Amazon SQS queue service has a maximum delay time of 15 minutes.
### [Synchronous Dispatching](https://laravel.com/docs/12.x/queues#synchronous-dispatching)
If you would like to dispatch a job immediately (synchronously), you may use the `dispatchSync` method. When using this method, the job will not be queued and will be executed immediately within the current process:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Jobs\ProcessPodcast;




 6use App\Models\Podcast;




 7use Illuminate\Http\RedirectResponse;




 8use Illuminate\Http\Request;




 9 



10class PodcastController extends Controller




11{




12    /**




13     * Store a new podcast.




14     */




15    public function store(Request $request): RedirectResponse




16    {




17        $podcast = Podcast::create(/* ... */);




18 



19        // Create podcast...




20 



21        ProcessPodcast::dispatchSync($podcast);




22 



23        return redirect('/podcasts');




24    }




25}




<?php

namespace App\Http\Controllers;

use App\Jobs\ProcessPodcast;
use App\Models\Podcast;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class PodcastController extends Controller
{
    /**
     * Store a new podcast.
     */
    public function store(Request $request): RedirectResponse
    {
        $podcast = Podcast::create(/* ... */);

        // Create podcast...

        ProcessPodcast::dispatchSync($podcast);

        return redirect('/podcasts');
    }
}

```

#### [Deferred Dispatching](https://laravel.com/docs/12.x/queues#deferred-dispatching)
Using deferred synchronous dispatching, you can dispatch a job to be processed during the current process, but after the HTTP response has been sent to the user. This allows you to process "queued" jobs synchronously without slowing down your user's application experience. To defer the execution of a synchronous job, dispatch the job to the `deferred` connection:
```


1RecordDelivery::dispatch($order)->onConnection('deferred');




RecordDelivery::dispatch($order)->onConnection('deferred');

```

The `deferred` connection also serves as the default [failover queue](https://laravel.com/docs/12.x/queues#queue-failover).
Similarly, the `background` connection processes jobs after the HTTP response has been sent to the user; however, the job is processed in a separately spawned PHP process, allowing the PHP-FPM / application worker to be available to handle another incoming HTTP request:
```


1RecordDelivery::dispatch($order)->onConnection('background');




RecordDelivery::dispatch($order)->onConnection('background');

```

### [Jobs & Database Transactions](https://laravel.com/docs/12.x/queues#jobs-and-database-transactions)
While it is perfectly fine to dispatch jobs within database transactions, you should take special care to ensure that your job will actually be able to execute successfully. When dispatching a job within a transaction, it is possible that the job will be processed by a worker before the parent transaction has committed. When this happens, any updates you have made to models or database records during the database transaction(s) may not yet be reflected in the database. In addition, any models or database records created within the transaction(s) may not exist in the database.
Thankfully, Laravel provides several methods of working around this problem. First, you may set the `after_commit` connection option in your queue connection's configuration array:
```


1'redis' => [




2    'driver' => 'redis',




3    // ...




4    'after_commit' => true,




5],




'redis' => [
    'driver' => 'redis',
    // ...
    'after_commit' => true,
],

```

When the `after_commit` option is `true`, you may dispatch jobs within database transactions; however, Laravel will wait until the open parent database transactions have been committed before actually dispatching the job. Of course, if no database transactions are currently open, the job will be dispatched immediately.
If a transaction is rolled back due to an exception that occurs during the transaction, the jobs that were dispatched during that transaction will be discarded.
Setting the `after_commit` configuration option to `true` will also cause any queued event listeners, mailables, notifications, and broadcast events to be dispatched after all open database transactions have been committed.
#### [Specifying Commit Dispatch Behavior Inline](https://laravel.com/docs/12.x/queues#specifying-commit-dispatch-behavior-inline)
If you do not set the `after_commit` queue connection configuration option to `true`, you may still indicate that a specific job should be dispatched after all open database transactions have been committed. To accomplish this, you may chain the `afterCommit` method onto your dispatch operation:
```


1use App\Jobs\ProcessPodcast;




2 



3ProcessPodcast::dispatch($podcast)->afterCommit();




use App\Jobs\ProcessPodcast;

ProcessPodcast::dispatch($podcast)->afterCommit();

```

Likewise, if the `after_commit` configuration option is set to `true`, you may indicate that a specific job should be dispatched immediately without waiting for any open database transactions to commit:
```


1ProcessPodcast::dispatch($podcast)->beforeCommit();




ProcessPodcast::dispatch($podcast)->beforeCommit();

```

### [Job Chaining](https://laravel.com/docs/12.x/queues#job-chaining)
Job chaining allows you to specify a list of queued jobs that should be run in sequence after the primary job has executed successfully. If one job in the sequence fails, the rest of the jobs will not be run. To execute a queued job chain, you may use the `chain` method provided by the `Bus` facade. Laravel's command bus is a lower-level component that queued job dispatching is built on top of:
```


 1use App\Jobs\OptimizePodcast;




 2use App\Jobs\ProcessPodcast;




 3use App\Jobs\ReleasePodcast;




 4use Illuminate\Support\Facades\Bus;




 5 



 6Bus::chain([




 7    new ProcessPodcast,




 8    new OptimizePodcast,




 9    new ReleasePodcast,




10])->dispatch();




use App\Jobs\OptimizePodcast;
use App\Jobs\ProcessPodcast;
use App\Jobs\ReleasePodcast;
use Illuminate\Support\Facades\Bus;

Bus::chain([
    new ProcessPodcast,
    new OptimizePodcast,
    new ReleasePodcast,
])->dispatch();

```

In addition to chaining job class instances, you may also chain closures:
```


1Bus::chain([




2    new ProcessPodcast,




3    new OptimizePodcast,




4    function () {




5        Podcast::update(/* ... */);




6    },




7])->dispatch();




Bus::chain([
    new ProcessPodcast,
    new OptimizePodcast,
    function () {
        Podcast::update(/* ... */);
    },
])->dispatch();

```

Deleting jobs using the `$this->delete()` method within the job will not prevent chained jobs from being processed. The chain will only stop executing if a job in the chain fails.
#### [Chain Connection and Queue](https://laravel.com/docs/12.x/queues#chain-connection-queue)
If you would like to specify the connection and queue that should be used for the chained jobs, you may use the `onConnection` and `onQueue` methods. These methods specify the queue connection and queue name that should be used unless the queued job is explicitly assigned a different connection / queue:
```


1Bus::chain([




2    new ProcessPodcast,




3    new OptimizePodcast,




4    new ReleasePodcast,




5])->onConnection('redis')->onQueue('podcasts')->dispatch();




Bus::chain([
    new ProcessPodcast,
    new OptimizePodcast,
    new ReleasePodcast,
])->onConnection('redis')->onQueue('podcasts')->dispatch();

```

#### [Adding Jobs to the Chain](https://laravel.com/docs/12.x/queues#adding-jobs-to-the-chain)
Occasionally, you may need to prepend or append a job to an existing job chain from within another job in that chain. You may accomplish this using the `prependToChain` and `appendToChain` methods:
```


 1/**




 2 * Execute the job.




 3 */




 4public function handle(): void




 5{




 6    // ...




 7 



 8    // Prepend to the current chain, run job immediately after current job...




 9    $this->prependToChain(new TranscribePodcast);




10 



11    // Append to the current chain, run job at end of chain...




12    $this->appendToChain(new TranscribePodcast);




13}




/**
 * Execute the job.
 */
public function handle(): void
{
    // ...

    // Prepend to the current chain, run job immediately after current job...
    $this->prependToChain(new TranscribePodcast);

    // Append to the current chain, run job at end of chain...
    $this->appendToChain(new TranscribePodcast);
}

```

#### [Chain Failures](https://laravel.com/docs/12.x/queues#chain-failures)
When chaining jobs, you may use the `catch` method to specify a closure that should be invoked if a job within the chain fails. The given callback will receive the `Throwable` instance that caused the job failure:
```


 1use Illuminate\Support\Facades\Bus;




 2use Throwable;




 3 



 4Bus::chain([




 5    new ProcessPodcast,




 6    new OptimizePodcast,




 7    new ReleasePodcast,




 8])->catch(function (Throwable $e) {




 9    // A job within the chain has failed...




10})->dispatch();




use Illuminate\Support\Facades\Bus;
use Throwable;

Bus::chain([
    new ProcessPodcast,
    new OptimizePodcast,
    new ReleasePodcast,
])->catch(function (Throwable $e) {
    // A job within the chain has failed...
})->dispatch();

```

Since chain callbacks are serialized and executed at a later time by the Laravel queue, you should not use the `$this` variable within chain callbacks.
### [Customizing the Queue and Connection](https://laravel.com/docs/12.x/queues#customizing-the-queue-and-connection)
#### [Dispatching to a Particular Queue](https://laravel.com/docs/12.x/queues#dispatching-to-a-particular-queue)
By pushing jobs to different queues, you may "categorize" your queued jobs and even prioritize how many workers you assign to various queues. Keep in mind, this does not push jobs to different queue "connections" as defined by your queue configuration file, but only to specific queues within a single connection. To specify the queue, use the `onQueue` method when dispatching the job:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Jobs\ProcessPodcast;




 6use App\Models\Podcast;




 7use Illuminate\Http\RedirectResponse;




 8use Illuminate\Http\Request;




 9 



10class PodcastController extends Controller




11{




12    /**




13     * Store a new podcast.




14     */




15    public function store(Request $request): RedirectResponse




16    {




17        $podcast = Podcast::create(/* ... */);




18 



19        // Create podcast...




20 



21        ProcessPodcast::dispatch($podcast)->onQueue('processing');




22 



23        return redirect('/podcasts');




24    }




25}




<?php

namespace App\Http\Controllers;

use App\Jobs\ProcessPodcast;
use App\Models\Podcast;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class PodcastController extends Controller
{
    /**
     * Store a new podcast.
     */
    public function store(Request $request): RedirectResponse
    {
        $podcast = Podcast::create(/* ... */);

        // Create podcast...

        ProcessPodcast::dispatch($podcast)->onQueue('processing');

        return redirect('/podcasts');
    }
}

```

Alternatively, you may specify the job's queue by calling the `onQueue` method within the job's constructor:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use Illuminate\Contracts\Queue\ShouldQueue;




 6use Illuminate\Foundation\Queue\Queueable;




 7 



 8class ProcessPodcast implements ShouldQueue




 9{




10    use Queueable;




11 



12    /**




13     * Create a new job instance.




14     */




15    public function __construct()




16    {




17        $this->onQueue('processing');




18    }




19}




<?php

namespace App\Jobs;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;

class ProcessPodcast implements ShouldQueue
{
    use Queueable;

    /**
     * Create a new job instance.
     */
    public function __construct()
    {
        $this->onQueue('processing');
    }
}

```

#### [Dispatching to a Particular Connection](https://laravel.com/docs/12.x/queues#dispatching-to-a-particular-connection)
If your application interacts with multiple queue connections, you may specify which connection to push a job to using the `onConnection` method:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Jobs\ProcessPodcast;




 6use App\Models\Podcast;




 7use Illuminate\Http\RedirectResponse;




 8use Illuminate\Http\Request;




 9 



10class PodcastController extends Controller




11{




12    /**




13     * Store a new podcast.




14     */




15    public function store(Request $request): RedirectResponse




16    {




17        $podcast = Podcast::create(/* ... */);




18 



19        // Create podcast...




20 



21        ProcessPodcast::dispatch($podcast)->onConnection('sqs');




22 



23        return redirect('/podcasts');




24    }




25}




<?php

namespace App\Http\Controllers;

use App\Jobs\ProcessPodcast;
use App\Models\Podcast;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class PodcastController extends Controller
{
    /**
     * Store a new podcast.
     */
    public function store(Request $request): RedirectResponse
    {
        $podcast = Podcast::create(/* ... */);

        // Create podcast...

        ProcessPodcast::dispatch($podcast)->onConnection('sqs');

        return redirect('/podcasts');
    }
}

```

You may chain the `onConnection` and `onQueue` methods together to specify the connection and the queue for a job:
```


1ProcessPodcast::dispatch($podcast)




2    ->onConnection('sqs')




3    ->onQueue('processing');




ProcessPodcast::dispatch($podcast)
    ->onConnection('sqs')
    ->onQueue('processing');

```

Alternatively, you may specify the job's connection by calling the `onConnection` method within the job's constructor:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use Illuminate\Contracts\Queue\ShouldQueue;




 6use Illuminate\Foundation\Queue\Queueable;




 7 



 8class ProcessPodcast implements ShouldQueue




 9{




10    use Queueable;




11 



12    /**




13     * Create a new job instance.




14     */




15    public function __construct()




16    {




17        $this->onConnection('sqs');




18    }




19}




<?php

namespace App\Jobs;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;

class ProcessPodcast implements ShouldQueue
{
    use Queueable;

    /**
     * Create a new job instance.
     */
    public function __construct()
    {
        $this->onConnection('sqs');
    }
}

```

### [Specifying Max Job Attempts / Timeout Values](https://laravel.com/docs/12.x/queues#max-job-attempts-and-timeout)
#### [Max Attempts](https://laravel.com/docs/12.x/queues#max-attempts)
Job attempts are a core concept of Laravel's queue system and power many advanced features. While they may seem confusing at first, it's important to understand how they work before modifying the default configuration.
When a job is dispatched, it is pushed onto the queue. A worker then picks it up and attempts to execute it. This is a job attempt.
However, an attempt does not necessarily mean the job's `handle` method was executed. Attempts can also be "consumed" in several ways:
  * The job encounters an unhandled exception during execution.
  * The job is manually released back to the queue using `$this->release()`.
  * Middleware such as `WithoutOverlapping` or `RateLimited` fails to acquire a lock and releases the job.
  * The job timed out.
  * The job's `handle` method runs and completes without throwing an exception.


You likely do not want to keep attempting a job indefinitely. Therefore, Laravel provides various ways to specify how many times or for how long a job may be attempted.
By default, Laravel will only attempt a job once. If your job uses middleware like `WithoutOverlapping` or `RateLimited`, or if you're manually releasing jobs, you will likely need to increase the number of allowed attempts via the `tries` option.
One approach to specifying the maximum number of times a job may be attempted is via the `--tries` switch on the Artisan command line. This will apply to all jobs processed by the worker unless the job being processed specifies the number of times it may be attempted:
```


1php artisan queue:work --tries=3




php artisan queue:work --tries=3

```

If a job exceeds its maximum number of attempts, it will be considered a "failed" job. For more information on handling failed jobs, consult the [failed job documentation](https://laravel.com/docs/12.x/queues#dealing-with-failed-jobs). If `--tries=0` is provided to the `queue:work` command, the job will be retried indefinitely.
You may take a more granular approach by defining the maximum number of times a job may be attempted on the job class itself. If the maximum number of attempts is specified on the job, it will take precedence over the `--tries` value provided on the command line:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5class ProcessPodcast implements ShouldQueue




 6{




 7    /**




 8     * The number of times the job may be attempted.




 9     *




10     * @var int




11     */




12    public $tries = 5;




13}




<?php

namespace App\Jobs;

class ProcessPodcast implements ShouldQueue
{
    /**
     * The number of times the job may be attempted.
     *
     * @var int
     */
    public $tries = 5;
}

```

If you need dynamic control over a particular job's maximum attempts, you may define a `tries` method on the job:
```


1/**




2 * Determine number of times the job may be attempted.




3 */




4public function tries(): int




5{




6    return 5;




7}




/**
 * Determine number of times the job may be attempted.
 */
public function tries(): int
{
    return 5;
}

```

#### [Time Based Attempts](https://laravel.com/docs/12.x/queues#time-based-attempts)
As an alternative to defining how many times a job may be attempted before it fails, you may define a time at which the job should no longer be attempted. This allows a job to be attempted any number of times within a given time frame. To define the time at which a job should no longer be attempted, add a `retryUntil` method to your job class. This method should return a `DateTime` instance:
```


1use DateTime;




2 



3/**




4 * Determine the time at which the job should timeout.




5 */




6public function retryUntil(): DateTime




7{




8    return now()->plus(minutes: 10);




9}




use DateTime;

/**
 * Determine the time at which the job should timeout.
 */
public function retryUntil(): DateTime
{
    return now()->plus(minutes: 10);
}

```

If both `retryUntil` and `tries` are defined, Laravel gives precedence to the `retryUntil` method.
You may also define a `tries` property or `retryUntil` method on your [queued event listeners](https://laravel.com/docs/12.x/events#queued-event-listeners) and [queued notifications](https://laravel.com/docs/12.x/notifications#queueing-notifications).
#### [Max Exceptions](https://laravel.com/docs/12.x/queues#max-exceptions)
Sometimes you may wish to specify that a job may be attempted many times, but should fail if the retries are triggered by a given number of unhandled exceptions (as opposed to being released by the `release` method directly). To accomplish this, you may define a `maxExceptions` property on your job class:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use Illuminate\Contracts\Queue\ShouldQueue;




 6use Illuminate\Foundation\Queue\Queueable;




 7use Illuminate\Support\Facades\Redis;




 8 



 9class ProcessPodcast implements ShouldQueue




10{




11    use Queueable;




12 



13    /**




14     * The number of times the job may be attempted.




15     *




16     * @var int




17     */




18    public $tries = 25;




19 



20    /**




21     * The maximum number of unhandled exceptions to allow before failing.




22     *




23     * @var int




24     */




25    public $maxExceptions = 3;




26 



27    /**




28     * Execute the job.




29     */




30    public function handle(): void




31    {




32        Redis::throttle('key')->allow(10)->every(60)->then(function () {




33            // Lock obtained, process the podcast...




34        }, function () {




35            // Unable to obtain lock...




36            return $this->release(10);




37        });




38    }




39}




<?php

namespace App\Jobs;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;
use Illuminate\Support\Facades\Redis;

class ProcessPodcast implements ShouldQueue
{
    use Queueable;

    /**
     * The number of times the job may be attempted.
     *
     * @var int
     */
    public $tries = 25;

    /**
     * The maximum number of unhandled exceptions to allow before failing.
     *
     * @var int
     */
    public $maxExceptions = 3;

    /**
     * Execute the job.
     */
    public function handle(): void
    {
        Redis::throttle('key')->allow(10)->every(60)->then(function () {
            // Lock obtained, process the podcast...
        }, function () {
            // Unable to obtain lock...
            return $this->release(10);
        });
    }
}

```

In this example, the job is released for ten seconds if the application is unable to obtain a Redis lock and will continue to be retried up to 25 times. However, the job will fail if three unhandled exceptions are thrown by the job.
#### [Timeout](https://laravel.com/docs/12.x/queues#timeout)
Often, you know roughly how long you expect your queued jobs to take. For this reason, Laravel allows you to specify a "timeout" value. By default, the timeout value is 60 seconds. If a job is processing for longer than the number of seconds specified by the timeout value, the worker processing the job will exit with an error. Typically, the worker will be restarted automatically by a [process manager configured on your server](https://laravel.com/docs/12.x/queues#supervisor-configuration).
The maximum number of seconds that jobs can run may be specified using the `--timeout` switch on the Artisan command line:
```


1php artisan queue:work --timeout=30




php artisan queue:work --timeout=30

```

If the job exceeds its maximum attempts by continually timing out, it will be marked as failed.
You may also define the maximum number of seconds a job should be allowed to run on the job class itself. If the timeout is specified on the job, it will take precedence over any timeout specified on the command line:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5class ProcessPodcast implements ShouldQueue




 6{




 7    /**




 8     * The number of seconds the job can run before timing out.




 9     *




10     * @var int




11     */




12    public $timeout = 120;




13}




<?php

namespace App\Jobs;

class ProcessPodcast implements ShouldQueue
{
    /**
     * The number of seconds the job can run before timing out.
     *
     * @var int
     */
    public $timeout = 120;
}

```

Sometimes, IO blocking processes such as sockets or outgoing HTTP connections may not respect your specified timeout. Therefore, when using these features, you should always attempt to specify a timeout using their APIs as well. For example, when using
The ["retry after"](https://laravel.com/docs/12.x/queues#job-expiration) value. Otherwise, the job may be re-attempted before it has actually finished executing or timed out.
#### [Failing on Timeout](https://laravel.com/docs/12.x/queues#failing-on-timeout)
If you would like to indicate that a job should be marked as [failed](https://laravel.com/docs/12.x/queues#dealing-with-failed-jobs) on timeout, you may define the `$failOnTimeout` property on the job class:
```


1/**




2 * Indicate if the job should be marked as failed on timeout.




3 *




4 * @var bool




5 */




6public $failOnTimeout = true;




/**
 * Indicate if the job should be marked as failed on timeout.
 *
 * @var bool
 */
public $failOnTimeout = true;

```

By default, when a job times out, it consumes one attempt and is released back to the queue (if retries are allowed). However, if you configure the job to fail on timeout, it will not be retried, regardless of the value set for tries.
### [SQS FIFO and Fair Queues](https://laravel.com/docs/12.x/queues#sqs-fifo-and-fair-queues)
Laravel supports
FIFO queues require a message group ID to determine which jobs can be processed in parallel. Jobs with the same group ID are processed sequentially, while messages with different group IDs can be processed concurrently.
Laravel provides a fluent `onGroup` method to specify the message group ID when dispatching jobs:
```


1ProcessOrder::dispatch($order)




2    ->onGroup("customer-{$order->customer_id}");




ProcessOrder::dispatch($order)
    ->onGroup("customer-{$order->customer_id}");

```

SQS FIFO queues support message deduplication to ensure exactly-once processing. Implement a `deduplicationId` method in your job class to provide a custom deduplication ID:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use Illuminate\Contracts\Queue\ShouldQueue;




 6use Illuminate\Foundation\Queue\Queueable;




 7 



 8class ProcessSubscriptionRenewal implements ShouldQueue




 9{




10    use Queueable;




11 



12    // ...




13 



14    /**




15     * Get the job's deduplication ID.




16     */




17    public function deduplicationId(): string




18    {




19        return "renewal-{$this->subscription->id}";




20    }




21}




<?php

namespace App\Jobs;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;

class ProcessSubscriptionRenewal implements ShouldQueue
{
    use Queueable;

    // ...

    /**
     * Get the job's deduplication ID.
     */
    public function deduplicationId(): string
    {
        return "renewal-{$this->subscription->id}";
    }
}

```

#### [FIFO Listeners, Mail, and Notifications](https://laravel.com/docs/12.x/queues#fifo-listeners-mail-and-notifications)
When utilizing FIFO queues, you will also need to define message groups on listeners, mail, and notifications. Alternatively, you can dispatch queued instances of these objects to a non-FIFO queue.
To define the message group for a [queued event listener](https://laravel.com/docs/12.x/events#queued-event-listeners), define a `messageGroup` method on the listener. You may also optionally define a `deduplicationId` method:
```


 1<?php




 2 



 3namespace App\Listeners;




 4 



 5class SendShipmentNotification




 6{




 7    // ...




 8 



 9    /**




10     * Get the job's message group.




11     */




12    public function messageGroup(): string




13    {




14        return 'shipments';




15    }




16 



17    /**




18     * Get the job's deduplication ID.




19     */




20    public function deduplicationId(): string




21    {




22        return "shipment-notification-{$this->shipment->id}";




23    }




24}




<?php

namespace App\Listeners;

class SendShipmentNotification
{
    // ...

    /**
     * Get the job's message group.
     */
    public function messageGroup(): string
    {
        return 'shipments';
    }

    /**
     * Get the job's deduplication ID.
     */
    public function deduplicationId(): string
    {
        return "shipment-notification-{$this->shipment->id}";
    }
}

```

When sending a [mail message](https://laravel.com/docs/12.x/mail) that is going to be queued on a FIFO queue, you should invoke the `onGroup` method and optionally the `withDeduplicator` method when sending the notification:
```


1use App\Mail\InvoicePaid;




2use Illuminate\Support\Facades\Mail;




3 



4$invoicePaid = (new InvoicePaid($invoice))




5    ->onGroup('invoices')




6    ->withDeduplicator(fn () => 'invoices-'.$invoice->id);




7 



8Mail::to($request->user())->send($invoicePaid);




use App\Mail\InvoicePaid;
use Illuminate\Support\Facades\Mail;

$invoicePaid = (new InvoicePaid($invoice))
    ->onGroup('invoices')
    ->withDeduplicator(fn () => 'invoices-'.$invoice->id);

Mail::to($request->user())->send($invoicePaid);

```

When sending a [notification](https://laravel.com/docs/12.x/notifications) that is going to be queued on a FIFO queue, you should invoke the `onGroup` method and optionally the `withDeduplicator` method when sending the notification:
```


1use App\Notifications\InvoicePaid;




2 



3$invoicePaid = (new InvoicePaid($invoice))




4    ->onGroup('invoices')




5    ->withDeduplicator(fn () => 'invoices-'.$invoice->id);




6 



7$user->notify($invoicePaid);




use App\Notifications\InvoicePaid;

$invoicePaid = (new InvoicePaid($invoice))
    ->onGroup('invoices')
    ->withDeduplicator(fn () => 'invoices-'.$invoice->id);

$user->notify($invoicePaid);

```

### [Queue Failover](https://laravel.com/docs/12.x/queues#queue-failover)
The `failover` queue driver provides automatic failover functionality when pushing jobs to the queue. If the primary queue connection of the `failover` configuration fails for any reason, Laravel will automatically attempt to push the job to the next configured connection in the list. This is particularly useful for ensuring high availability in production environments where queue reliability is critical.
To configure a failover queue connection, specify the `failover` driver and provide an array of connection names to attempt in order. By default, Laravel includes an example failover configuration in your application's `config/queue.php` configuration file:
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

Once you have configured a connection that uses the `failover` driver, you will need to set the failover connection as your default queue connection in your application's `.env` file to make use of the failover functionality:
```


1QUEUE_CONNECTION=failover




QUEUE_CONNECTION=failover

```

Next, start at least one worker for each connection in your failover connection list:
```


1php artisan queue:work redis




2php artisan queue:work database




php artisan queue:work redis
php artisan queue:work database

```

You do not need to run a worker for connections using the `sync`, `background`, or `deferred` queue drivers since those drivers process jobs within the current PHP process.
When a queue connection operation fails and failover is activated, Laravel will dispatch the `Illuminate\Queue\Events\QueueFailedOver` event, allowing you to report or log that a queue connection has failed.
If you use Laravel Horizon, remember that Horizon manages Redis queues only. If your failover list includes `database`, you should run a regular `php artisan queue:work database` process alongside Horizon.
### [Error Handling](https://laravel.com/docs/12.x/queues#error-handling)
If an exception is thrown while the job is being processed, the job will automatically be released back onto the queue so it may be attempted again. The job will continue to be released until it has been attempted the maximum number of times allowed by your application. The maximum number of attempts is defined by the `--tries` switch used on the `queue:work` Artisan command. Alternatively, the maximum number of attempts may be defined on the job class itself. More information on running the queue worker [can be found below](https://laravel.com/docs/12.x/queues#running-the-queue-worker).
#### [Manually Releasing a Job](https://laravel.com/docs/12.x/queues#manually-releasing-a-job)
Sometimes you may wish to manually release a job back onto the queue so that it can be attempted again at a later time. You may accomplish this by calling the `release` method:
```


1/**




2 * Execute the job.




3 */




4public function handle(): void




5{




6    // ...




7 



8    $this->release();




9}




/**
 * Execute the job.
 */
public function handle(): void
{
    // ...

    $this->release();
}

```

By default, the `release` method will release the job back onto the queue for immediate processing. However, you may instruct the queue to not make the job available for processing until a given number of seconds has elapsed by passing an integer or date instance to the `release` method:
```


1$this->release(10);




2 



3$this->release(now()->plus(seconds: 10));




$this->release(10);

$this->release(now()->plus(seconds: 10));

```

#### [Manually Failing a Job](https://laravel.com/docs/12.x/queues#manually-failing-a-job)
Occasionally you may need to manually mark a job as "failed". To do so, you may call the `fail` method:
```


1/**




2 * Execute the job.




3 */




4public function handle(): void




5{




6    // ...




7 



8    $this->fail();




9}




/**
 * Execute the job.
 */
public function handle(): void
{
    // ...

    $this->fail();
}

```

If you would like to mark your job as failed because of an exception that you have caught, you may pass the exception to the `fail` method. Or, for convenience, you may pass a string error message which will be converted to an exception for you:
```


1$this->fail($exception);




2 



3$this->fail('Something went wrong.');




$this->fail($exception);

$this->fail('Something went wrong.');

```

For more information on failed jobs, check out the [documentation on dealing with job failures](https://laravel.com/docs/12.x/queues#dealing-with-failed-jobs).
#### [Failing Jobs on Specific Exceptions](https://laravel.com/docs/12.x/queues#fail-jobs-on-exceptions)
The `FailOnException` [job middleware](https://laravel.com/docs/12.x/queues#job-middleware) allows you to short-circuit retries when specific exceptions are thrown. This allows retrying on transient exceptions such as external API errors, but failing the job permanently on persistent exceptions, such as a user's permissions being revoked:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use App\Models\User;




 6use Illuminate\Auth\Access\AuthorizationException;




 7use Illuminate\Contracts\Queue\ShouldQueue;




 8use Illuminate\Foundation\Queue\Queueable;




 9use Illuminate\Queue\Middleware\FailOnException;




10use Illuminate\Support\Facades\Http;




11 



12class SyncChatHistory implements ShouldQueue




13{




14    use Queueable;




15 



16    public $tries = 3;




17 



18    /**




19     * Create a new job instance.




20     */




21    public function __construct(




22        public User $user,




23    ) {}




24 



25    /**




26     * Execute the job.




27     */




28    public function handle(): void




29    {




30        $this->user->authorize('sync-chat-history');




31 



32        $response = Http::throw()->get(




33            "https://chat.laravel.test/?user={$this->user->uuid}"




34        );




35 



36        // ...




37    }




38 



39    /**




40     * Get the middleware the job should pass through.




41     */




42    public function middleware(): array




43    {




44        return [




45            new FailOnException([AuthorizationException::class])




46        ];




47    }




48}




<?php

namespace App\Jobs;

use App\Models\User;
use Illuminate\Auth\Access\AuthorizationException;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;
use Illuminate\Queue\Middleware\FailOnException;
use Illuminate\Support\Facades\Http;

class SyncChatHistory implements ShouldQueue
{
    use Queueable;

    public $tries = 3;

    /**
     * Create a new job instance.
     */
    public function __construct(
        public User $user,
    ) {}

    /**
     * Execute the job.
     */
    public function handle(): void
    {
        $this->user->authorize('sync-chat-history');

        $response = Http::throw()->get(
            "https://chat.laravel.test/?user={$this->user->uuid}"
        );

        // ...
    }

    /**
     * Get the middleware the job should pass through.
     */
    public function middleware(): array
    {
        return [
            new FailOnException([AuthorizationException::class])
        ];
    }
}

```
