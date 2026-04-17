## [Dealing With Failed Jobs](https://laravel.com/docs/12.x/queues#dealing-with-failed-jobs)
Sometimes your queued jobs will fail. Don't worry, things don't always go as planned! Laravel includes a convenient way to [specify the maximum number of times a job should be attempted](https://laravel.com/docs/12.x/queues#max-job-attempts-and-timeout). After an asynchronous job has exceeded this number of attempts, it will be inserted into the `failed_jobs` database table. [Synchronously dispatched jobs](https://laravel.com/docs/12.x/queues#synchronous-dispatching) that fail are not stored in this table and their exceptions are immediately handled by the application.
A migration to create the `failed_jobs` table is typically already present in new Laravel applications. However, if your application does not contain a migration for this table, you may use the `make:queue-failed-table` command to create the migration:
```


1php artisan make:queue-failed-table




2 



3php artisan migrate




php artisan make:queue-failed-table

php artisan migrate

```

When running a [queue worker](https://laravel.com/docs/12.x/queues#running-the-queue-worker) process, you may specify the maximum number of times a job should be attempted using the `--tries` switch on the `queue:work` command. If you do not specify a value for the `--tries` option, jobs will only be attempted once or as many times as specified by the job class' `$tries` property:
```


1php artisan queue:work redis --tries=3




php artisan queue:work redis --tries=3

```

Using the `--backoff` option, you may specify how many seconds Laravel should wait before retrying a job that has encountered an exception. By default, a job is immediately released back onto the queue so that it may be attempted again:
```


1php artisan queue:work redis --tries=3 --backoff=3




php artisan queue:work redis --tries=3 --backoff=3

```

If you would like to configure how many seconds Laravel should wait before retrying a job that has encountered an exception on a per-job basis, you may do so by defining a `backoff` property on your job class:
```


1/**




2 * The number of seconds to wait before retrying the job.




3 *




4 * @var int




5 */




6public $backoff = 3;




/**
 * The number of seconds to wait before retrying the job.
 *
 * @var int
 */
public $backoff = 3;

```

If you require more complex logic for determining the job's backoff time, you may define a `backoff` method on your job class:
```


1/**




2 * Calculate the number of seconds to wait before retrying the job.




3 */




4public function backoff(): int




5{




6    return 3;




7}




/**
 * Calculate the number of seconds to wait before retrying the job.
 */
public function backoff(): int
{
    return 3;
}

```

You may easily configure "exponential" backoffs by returning an array of backoff values from the `backoff` method. In this example, the retry delay will be 1 second for the first retry, 5 seconds for the second retry, 10 seconds for the third retry, and 10 seconds for every subsequent retry if there are more attempts remaining:
```


1/**




2 * Calculate the number of seconds to wait before retrying the job.




3 *




4 * @return array<int, int>




5 */




6public function backoff(): array




7{




8    return [1, 5, 10];




9}




/**
 * Calculate the number of seconds to wait before retrying the job.
 *
 * @return array<int, int>
 */
public function backoff(): array
{
    return [1, 5, 10];
}

```

### [Cleaning Up After Failed Jobs](https://laravel.com/docs/12.x/queues#cleaning-up-after-failed-jobs)
When a particular job fails, you may want to send an alert to your users or revert any actions that were partially completed by the job. To accomplish this, you may define a `failed` method on your job class. The `Throwable` instance that caused the job to fail will be passed to the `failed` method:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use App\Models\Podcast;




 6use App\Services\AudioProcessor;




 7use Illuminate\Contracts\Queue\ShouldQueue;




 8use Illuminate\Foundation\Queue\Queueable;




 9use Throwable;




10 



11class ProcessPodcast implements ShouldQueue




12{




13    use Queueable;




14 



15    /**




16     * Create a new job instance.




17     */




18    public function __construct(




19        public Podcast $podcast,




20    ) {}




21 



22    /**




23     * Execute the job.




24     */




25    public function handle(AudioProcessor $processor): void




26    {




27        // Process uploaded podcast...




28    }




29 



30    /**




31     * Handle a job failure.




32     */




33    public function failed(?Throwable $exception): void




34    {




35        // Send user notification of failure, etc...




36    }




37}




<?php

namespace App\Jobs;

use App\Models\Podcast;
use App\Services\AudioProcessor;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;
use Throwable;

class ProcessPodcast implements ShouldQueue
{
    use Queueable;

    /**
     * Create a new job instance.
     */
    public function __construct(
        public Podcast $podcast,
    ) {}

    /**
     * Execute the job.
     */
    public function handle(AudioProcessor $processor): void
    {
        // Process uploaded podcast...
    }

    /**
     * Handle a job failure.
     */
    public function failed(?Throwable $exception): void
    {
        // Send user notification of failure, etc...
    }
}

```

A new instance of the job is instantiated before invoking the `failed` method; therefore, any class property modifications that may have occurred within the `handle` method will be lost.
A failed job is not necessarily one that encountered an unhandled exception. A job may also be considered failed when it has exhausted all of its allowed attempts. These attempts can be consumed in several ways:
  * The job timed out.
  * The job encounters an unhandled exception during execution.
  * The job is released back to the queue either manually or by a middleware.


If the final attempt fails due to an exception thrown during job execution, that exception will be passed to the job's `failed` method. However, if the job fails because it has reached the maximum number of allowed attempts, the `$exception` will be an instance of `Illuminate\Queue\MaxAttemptsExceededException`. Similarly, if the job fails due to exceeding the configured timeout, the `$exception` will be an instance of `Illuminate\Queue\TimeoutExceededException`.
### [Retrying Failed Jobs](https://laravel.com/docs/12.x/queues#retrying-failed-jobs)
To view all of the failed jobs that have been inserted into your `failed_jobs` database table, you may use the `queue:failed` Artisan command:
```


1php artisan queue:failed




php artisan queue:failed

```

The `queue:failed` command will list the job ID, connection, queue, failure time, and other information about the job. The job ID may be used to retry the failed job. For instance, to retry a failed job that has an ID of `ce7bb17c-cdd8-41f0-a8ec-7b4fef4e5ece`, issue the following command:
```


1php artisan queue:retry ce7bb17c-cdd8-41f0-a8ec-7b4fef4e5ece




php artisan queue:retry ce7bb17c-cdd8-41f0-a8ec-7b4fef4e5ece

```

If necessary, you may pass multiple IDs to the command:
```


1php artisan queue:retry ce7bb17c-cdd8-41f0-a8ec-7b4fef4e5ece 91401d2c-0784-4f43-824c-34f94a33c24d




php artisan queue:retry ce7bb17c-cdd8-41f0-a8ec-7b4fef4e5ece 91401d2c-0784-4f43-824c-34f94a33c24d

```

You may also retry all of the failed jobs for a particular queue:
```


1php artisan queue:retry --queue=name




php artisan queue:retry --queue=name

```

To retry all of your failed jobs, execute the `queue:retry` command and pass `all` as the ID:
```


1php artisan queue:retry all




php artisan queue:retry all

```

If you would like to delete a failed job, you may use the `queue:forget` command:
```


1php artisan queue:forget 91401d2c-0784-4f43-824c-34f94a33c24d




php artisan queue:forget 91401d2c-0784-4f43-824c-34f94a33c24d

```

When using [Horizon](https://laravel.com/docs/12.x/horizon), you should use the `horizon:forget` command to delete a failed job instead of the `queue:forget` command.
To delete all of your failed jobs from the `failed_jobs` table, you may use the `queue:flush` command:
```


1php artisan queue:flush




php artisan queue:flush

```

The `queue:flush` command removes all failed job records from your queue, no matter how old the failed job is. You may use the `--hours` option to only delete jobs that failed a certain number of hours ago or earlier:
```


1php artisan queue:flush --hours=48




php artisan queue:flush --hours=48

```

### [Ignoring Missing Models](https://laravel.com/docs/12.x/queues#ignoring-missing-models)
When injecting an Eloquent model into a job, the model is automatically serialized before being placed on the queue and re-retrieved from the database when the job is processed. However, if the model has been deleted while the job was waiting to be processed by a worker, your job may fail with a `ModelNotFoundException`.
For convenience, you may choose to automatically delete jobs with missing models by setting your job's `deleteWhenMissingModels` property to `true`. When this property is set to `true`, Laravel will quietly discard the job without raising an exception:
```


1/**




2 * Delete the job if its models no longer exist.




3 *




4 * @var bool




5 */




6public $deleteWhenMissingModels = true;




/**
 * Delete the job if its models no longer exist.
 *
 * @var bool
 */
public $deleteWhenMissingModels = true;

```

### [Pruning Failed Jobs](https://laravel.com/docs/12.x/queues#pruning-failed-jobs)
You may prune the records in your application's `failed_jobs` table by invoking the `queue:prune-failed` Artisan command:
```


1php artisan queue:prune-failed




php artisan queue:prune-failed

```

By default, all the failed job records that are more than 24 hours old will be pruned. If you provide the `--hours` option to the command, only the failed job records that were inserted within the last N number of hours will be retained. For example, the following command will delete all the failed job records that were inserted more than 48 hours ago:
```


1php artisan queue:prune-failed --hours=48




php artisan queue:prune-failed --hours=48

```

### [Storing Failed Jobs in DynamoDB](https://laravel.com/docs/12.x/queues#storing-failed-jobs-in-dynamodb)
Laravel also provides support for storing your failed job records in `failed_jobs`, but you should name the table based on the value of the `queue.failed.table` configuration value within your application's `queue` configuration file.
The `failed_jobs` table should have a string primary partition key named `application` and a string primary sort key named `uuid`. The `application` portion of the key will contain your application's name as defined by the `name` configuration value within your application's `app` configuration file. Since the application name is part of the DynamoDB table's key, you can use the same table to store failed jobs for multiple Laravel applications.
In addition, ensure that you install the AWS SDK so that your Laravel application can communicate with Amazon DynamoDB:
```


1composer require aws/aws-sdk-php




composer require aws/aws-sdk-php

```

Next, set the `queue.failed.driver` configuration option's value to `dynamodb`. In addition, you should define `key`, `secret`, and `region` configuration options within the failed job configuration array. These options will be used to authenticate with AWS. When using the `dynamodb` driver, the `queue.failed.database` configuration option is unnecessary:
```


1'failed' => [




2    'driver' => env('QUEUE_FAILED_DRIVER', 'dynamodb'),




3    'key' => env('AWS_ACCESS_KEY_ID'),




4    'secret' => env('AWS_SECRET_ACCESS_KEY'),




5    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),




6    'table' => 'failed_jobs',




7],




'failed' => [
    'driver' => env('QUEUE_FAILED_DRIVER', 'dynamodb'),
    'key' => env('AWS_ACCESS_KEY_ID'),
    'secret' => env('AWS_SECRET_ACCESS_KEY'),
    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
    'table' => 'failed_jobs',
],

```

### [Disabling Failed Job Storage](https://laravel.com/docs/12.x/queues#disabling-failed-job-storage)
You may instruct Laravel to discard failed jobs without storing them by setting the `queue.failed.driver` configuration option's value to `null`. Typically, this may be accomplished via the `QUEUE_FAILED_DRIVER` environment variable:
```


1QUEUE_FAILED_DRIVER=null




QUEUE_FAILED_DRIVER=null

```

### [Failed Job Events](https://laravel.com/docs/12.x/queues#failed-job-events)
If you would like to register an event listener that will be invoked when a job fails, you may use the `Queue` facade's `failing` method. For example, we may attach a closure to this event from the `boot` method of the `AppServiceProvider` that is included with Laravel:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Support\Facades\Queue;




 6use Illuminate\Support\ServiceProvider;




 7use Illuminate\Queue\Events\JobFailed;




 8 



 9class AppServiceProvider extends ServiceProvider




10{




11    /**




12     * Register any application services.




13     */




14    public function register(): void




15    {




16        // ...




17    }




18 



19    /**




20     * Bootstrap any application services.




21     */




22    public function boot(): void




23    {




24        Queue::failing(function (JobFailed $event) {




25            // $event->connectionName




26            // $event->job




27            // $event->exception




28        });




29    }




30}




<?php

namespace App\Providers;

use Illuminate\Support\Facades\Queue;
use Illuminate\Support\ServiceProvider;
use Illuminate\Queue\Events\JobFailed;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        // ...
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Queue::failing(function (JobFailed $event) {
            // $event->connectionName
            // $event->job
            // $event->exception
        });
    }
}

```
