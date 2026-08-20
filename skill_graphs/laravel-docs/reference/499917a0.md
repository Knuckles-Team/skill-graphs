## [Job Batching](https://laravel.com/docs/12.x/queues#job-batching)
Laravel's job batching feature allows you to easily execute a batch of jobs and then perform some action when the batch of jobs has completed executing. Before getting started, you should create a database migration to build a table which will contain meta information about your job batches, such as their completion percentage. This migration may be generated using the `make:queue-batches-table` Artisan command:
```


1php artisan make:queue-batches-table




2 



3php artisan migrate




php artisan make:queue-batches-table

php artisan migrate

```

### [Defining Batchable Jobs](https://laravel.com/docs/12.x/queues#defining-batchable-jobs)
To define a batchable job, you should [create a queueable job](https://laravel.com/docs/12.x/queues#creating-jobs) as normal; however, you should add the `Illuminate\Bus\Batchable` trait to the job class. This trait provides access to a `batch` method which may be used to retrieve the current batch that the job is executing within:
```


 1<?php




 2 



 3namespace App\Jobs;




 4 



 5use Illuminate\Bus\Batchable;




 6use Illuminate\Contracts\Queue\ShouldQueue;




 7use Illuminate\Foundation\Queue\Queueable;




 8 



 9class ImportCsv implements ShouldQueue




10{




11    use Batchable, Queueable;




12 



13    /**




14     * Execute the job.




15     */




16    public function handle(): void




17    {




18        if ($this->batch()->cancelled()) {




19            // Determine if the batch has been cancelled...




20 



21            return;




22        }




23 



24        // Import a portion of the CSV file...




25    }




26}




<?php

namespace App\Jobs;

use Illuminate\Bus\Batchable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Queue\Queueable;

class ImportCsv implements ShouldQueue
{
    use Batchable, Queueable;

    /**
     * Execute the job.
     */
    public function handle(): void
    {
        if ($this->batch()->cancelled()) {
            // Determine if the batch has been cancelled...

            return;
        }

        // Import a portion of the CSV file...
    }
}

```

### [Dispatching Batches](https://laravel.com/docs/12.x/queues#dispatching-batches)
To dispatch a batch of jobs, you should use the `batch` method of the `Bus` facade. Of course, batching is primarily useful when combined with completion callbacks. So, you may use the `then`, `catch`, and `finally` methods to define completion callbacks for the batch. Each of these callbacks will receive an `Illuminate\Bus\Batch` instance when they are invoked.
When running multiple queue workers, the jobs in the batch will be processed in parallel. Therefore, the order in which the jobs complete may not be the same as the order in which they were added to the batch. Consult our documentation on [job chains and batches](https://laravel.com/docs/12.x/queues#chains-and-batches) for information on how to run a series of jobs in sequence.
In this example, we will imagine we are queueing a batch of jobs that each process a given number of rows from a CSV file:
```


 1use App\Jobs\ImportCsv;




 2use Illuminate\Bus\Batch;




 3use Illuminate\Support\Facades\Bus;




 4use Throwable;




 5 



 6$batch = Bus::batch([




 7    new ImportCsv(1, 100),




 8    new ImportCsv(101, 200),




 9    new ImportCsv(201, 300),




10    new ImportCsv(301, 400),




11    new ImportCsv(401, 500),




12])->before(function (Batch $batch) {




13    // The batch has been created but no jobs have been added...




14})->progress(function (Batch $batch) {




15    // A single job has completed successfully...




16})->then(function (Batch $batch) {




17    // All jobs completed successfully...




18})->catch(function (Batch $batch, Throwable $e) {




19    // Batch job failure detected...




20})->finally(function (Batch $batch) {




21    // The batch has finished executing...




22})->dispatch();




23 



24return $batch->id;




use App\Jobs\ImportCsv;
use Illuminate\Bus\Batch;
use Illuminate\Support\Facades\Bus;
use Throwable;

$batch = Bus::batch([
    new ImportCsv(1, 100),
    new ImportCsv(101, 200),
    new ImportCsv(201, 300),
    new ImportCsv(301, 400),
    new ImportCsv(401, 500),
])->before(function (Batch $batch) {
    // The batch has been created but no jobs have been added...
})->progress(function (Batch $batch) {
    // A single job has completed successfully...
})->then(function (Batch $batch) {
    // All jobs completed successfully...
})->catch(function (Batch $batch, Throwable $e) {
    // Batch job failure detected...
})->finally(function (Batch $batch) {
    // The batch has finished executing...
})->dispatch();

return $batch->id;

```

The batch's ID, which may be accessed via the `$batch->id` property, may be used to [query the Laravel command bus](https://laravel.com/docs/12.x/queues#inspecting-batches) for information about the batch after it has been dispatched.
Since batch callbacks are serialized and executed at a later time by the Laravel queue, you should not use the `$this` variable within the callbacks. In addition, since batched jobs are wrapped within database transactions, database statements that trigger implicit commits should not be executed within the jobs.
#### [Naming Batches](https://laravel.com/docs/12.x/queues#naming-batches)
Some tools such as [Laravel Horizon](https://laravel.com/docs/12.x/horizon) and [Laravel Telescope](https://laravel.com/docs/12.x/telescope) may provide more user-friendly debug information for batches if batches are named. To assign an arbitrary name to a batch, you may call the `name` method while defining the batch:
```


1$batch = Bus::batch([




2    // ...




3])->then(function (Batch $batch) {




4    // All jobs completed successfully...




5})->name('Import CSV')->dispatch();




$batch = Bus::batch([
    // ...
])->then(function (Batch $batch) {
    // All jobs completed successfully...
})->name('Import CSV')->dispatch();

```

#### [Batch Connection and Queue](https://laravel.com/docs/12.x/queues#batch-connection-queue)
If you would like to specify the connection and queue that should be used for the batched jobs, you may use the `onConnection` and `onQueue` methods. All batched jobs must execute within the same connection and queue:
```


1$batch = Bus::batch([




2    // ...




3])->then(function (Batch $batch) {




4    // All jobs completed successfully...




5})->onConnection('redis')->onQueue('imports')->dispatch();




$batch = Bus::batch([
    // ...
])->then(function (Batch $batch) {
    // All jobs completed successfully...
})->onConnection('redis')->onQueue('imports')->dispatch();

```

### [Chains and Batches](https://laravel.com/docs/12.x/queues#chains-and-batches)
You may define a set of [chained jobs](https://laravel.com/docs/12.x/queues#job-chaining) within a batch by placing the chained jobs within an array. For example, we may execute two job chains in parallel and execute a callback when both job chains have finished processing:
```


 1use App\Jobs\ReleasePodcast;




 2use App\Jobs\SendPodcastReleaseNotification;




 3use Illuminate\Bus\Batch;




 4use Illuminate\Support\Facades\Bus;




 5 



 6Bus::batch([




 7    [




 8        new ReleasePodcast(1),




 9        new SendPodcastReleaseNotification(1),




10    ],




11    [




12        new ReleasePodcast(2),




13        new SendPodcastReleaseNotification(2),




14    ],




15])->then(function (Batch $batch) {




16    // All jobs completed successfully...




17})->dispatch();




use App\Jobs\ReleasePodcast;
use App\Jobs\SendPodcastReleaseNotification;
use Illuminate\Bus\Batch;
use Illuminate\Support\Facades\Bus;

Bus::batch([
    [
        new ReleasePodcast(1),
        new SendPodcastReleaseNotification(1),
    ],
    [
        new ReleasePodcast(2),
        new SendPodcastReleaseNotification(2),
    ],
])->then(function (Batch $batch) {
    // All jobs completed successfully...
})->dispatch();

```

Conversely, you may run batches of jobs within a [chain](https://laravel.com/docs/12.x/queues#job-chaining) by defining batches within the chain. For example, you could first run a batch of jobs to release multiple podcasts then a batch of jobs to send the release notifications:
```


 1use App\Jobs\FlushPodcastCache;




 2use App\Jobs\ReleasePodcast;




 3use App\Jobs\SendPodcastReleaseNotification;




 4use Illuminate\Support\Facades\Bus;




 5 



 6Bus::chain([




 7    new FlushPodcastCache,




 8    Bus::batch([




 9        new ReleasePodcast(1),




10        new ReleasePodcast(2),




11    ]),




12    Bus::batch([




13        new SendPodcastReleaseNotification(1),




14        new SendPodcastReleaseNotification(2),




15    ]),




16])->dispatch();




use App\Jobs\FlushPodcastCache;
use App\Jobs\ReleasePodcast;
use App\Jobs\SendPodcastReleaseNotification;
use Illuminate\Support\Facades\Bus;

Bus::chain([
    new FlushPodcastCache,
    Bus::batch([
        new ReleasePodcast(1),
        new ReleasePodcast(2),
    ]),
    Bus::batch([
        new SendPodcastReleaseNotification(1),
        new SendPodcastReleaseNotification(2),
    ]),
])->dispatch();

```

### [Adding Jobs to Batches](https://laravel.com/docs/12.x/queues#adding-jobs-to-batches)
Sometimes it may be useful to add additional jobs to a batch from within a batched job. This pattern can be useful when you need to batch thousands of jobs which may take too long to dispatch during a web request. So, instead, you may wish to dispatch an initial batch of "loader" jobs that hydrate the batch with even more jobs:
```


1$batch = Bus::batch([




2    new LoadImportBatch,




3    new LoadImportBatch,




4    new LoadImportBatch,




5])->then(function (Batch $batch) {




6    // All jobs completed successfully...




7})->name('Import Contacts')->dispatch();




$batch = Bus::batch([
    new LoadImportBatch,
    new LoadImportBatch,
    new LoadImportBatch,
])->then(function (Batch $batch) {
    // All jobs completed successfully...
})->name('Import Contacts')->dispatch();

```

In this example, we will use the `LoadImportBatch` job to hydrate the batch with additional jobs. To accomplish this, we may use the `add` method on the batch instance that may be accessed via the job's `batch` method:
```


 1use App\Jobs\ImportContacts;




 2use Illuminate\Support\Collection;




 3 



 4/**




 5 * Execute the job.




 6 */




 7public function handle(): void




 8{




 9    if ($this->batch()->cancelled()) {




10        return;




11    }




12 



13    $this->batch()->add(Collection::times(1000, function () {




14        return new ImportContacts;




15    }));




16}




use App\Jobs\ImportContacts;
use Illuminate\Support\Collection;

/**
 * Execute the job.
 */
public function handle(): void
{
    if ($this->batch()->cancelled()) {
        return;
    }

    $this->batch()->add(Collection::times(1000, function () {
        return new ImportContacts;
    }));
}

```

You may only add jobs to a batch from within a job that belongs to the same batch.
### [Inspecting Batches](https://laravel.com/docs/12.x/queues#inspecting-batches)
The `Illuminate\Bus\Batch` instance that is provided to batch completion callbacks has a variety of properties and methods to assist you in interacting with and inspecting a given batch of jobs:
```


 1// The UUID of the batch...




 2$batch->id;




 3 



 4// The name of the batch (if applicable)...




 5$batch->name;




 6 



 7// The number of jobs assigned to the batch...




 8$batch->totalJobs;




 9 



10// The number of jobs that have not been processed by the queue...




11$batch->pendingJobs;




12 



13// The number of jobs that have failed...




14$batch->failedJobs;




15 



16// The number of jobs that have been processed thus far...




17$batch->processedJobs();




18 



19// The completion percentage of the batch (0-100)...




20$batch->progress();




21 



22// Indicates if the batch has finished executing...




23$batch->finished();




24 



25// Cancel the execution of the batch...




26$batch->cancel();




27 



28// Indicates if the batch has been cancelled...




29$batch->cancelled();




// The UUID of the batch...
$batch->id;

// The name of the batch (if applicable)...
$batch->name;

// The number of jobs assigned to the batch...
$batch->totalJobs;

// The number of jobs that have not been processed by the queue...
$batch->pendingJobs;

// The number of jobs that have failed...
$batch->failedJobs;

// The number of jobs that have been processed thus far...
$batch->processedJobs();

// The completion percentage of the batch (0-100)...
$batch->progress();

// Indicates if the batch has finished executing...
$batch->finished();

// Cancel the execution of the batch...
$batch->cancel();

// Indicates if the batch has been cancelled...
$batch->cancelled();

```

#### [Returning Batches From Routes](https://laravel.com/docs/12.x/queues#returning-batches-from-routes)
All `Illuminate\Bus\Batch` instances are JSON serializable, meaning you can return them directly from one of your application's routes to retrieve a JSON payload containing information about the batch, including its completion progress. This makes it convenient to display information about the batch's completion progress in your application's UI.
To retrieve a batch by its ID, you may use the `Bus` facade's `findBatch` method:
```


1use Illuminate\Support\Facades\Bus;




2use Illuminate\Support\Facades\Route;




3 



4Route::get('/batch/{batchId}', function (string $batchId) {




5    return Bus::findBatch($batchId);




6});




use Illuminate\Support\Facades\Bus;
use Illuminate\Support\Facades\Route;

Route::get('/batch/{batchId}', function (string $batchId) {
    return Bus::findBatch($batchId);
});

```

### [Cancelling Batches](https://laravel.com/docs/12.x/queues#cancelling-batches)
Sometimes you may need to cancel a given batch's execution. This can be accomplished by calling the `cancel` method on the `Illuminate\Bus\Batch` instance:
```


 1/**




 2 * Execute the job.




 3 */




 4public function handle(): void




 5{




 6    if ($this->user->exceedsImportLimit()) {




 7        $this->batch()->cancel();




 8 



 9        return;




10    }




11 



12    if ($this->batch()->cancelled()) {




13        return;




14    }




15}




/**
 * Execute the job.
 */
public function handle(): void
{
    if ($this->user->exceedsImportLimit()) {
        $this->batch()->cancel();

        return;
    }

    if ($this->batch()->cancelled()) {
        return;
    }
}

```

As you may have noticed in the previous examples, batched jobs should typically determine if their corresponding batch has been cancelled before continuing execution. However, for convenience, you may assign the `SkipIfBatchCancelled` [middleware](https://laravel.com/docs/12.x/queues#job-middleware) to the job instead. As its name indicates, this middleware will instruct Laravel to not process the job if its corresponding batch has been cancelled:
```


1use Illuminate\Queue\Middleware\SkipIfBatchCancelled;




2 



3/**




4 * Get the middleware the job should pass through.




5 */




6public function middleware(): array




7{




8    return [new SkipIfBatchCancelled];




9}




use Illuminate\Queue\Middleware\SkipIfBatchCancelled;

/**
 * Get the middleware the job should pass through.
 */
public function middleware(): array
{
    return [new SkipIfBatchCancelled];
}

```

### [Batch Failures](https://laravel.com/docs/12.x/queues#batch-failures)
When a batched job fails, the `catch` callback (if assigned) will be invoked. This callback is only invoked for the first job that fails within the batch.
#### [Allowing Failures](https://laravel.com/docs/12.x/queues#allowing-failures)
When a job within a batch fails, Laravel will automatically mark the batch as "cancelled". If you wish, you may disable this behavior so that a job failure does not automatically mark the batch as cancelled. This may be accomplished by calling the `allowFailures` method while dispatching the batch:
```


1$batch = Bus::batch([




2    // ...




3])->then(function (Batch $batch) {




4    // All jobs completed successfully...




5})->allowFailures()->dispatch();




$batch = Bus::batch([
    // ...
])->then(function (Batch $batch) {
    // All jobs completed successfully...
})->allowFailures()->dispatch();

```

You may optionally provide a closure to the `allowFailures` method, which will be executed on each job failure:
```


1$batch = Bus::batch([




2    // ...




3])->allowFailures(function (Batch $batch, $exception) {




4    // Handle individual job failures...




5})->dispatch();




$batch = Bus::batch([
    // ...
])->allowFailures(function (Batch $batch, $exception) {
    // Handle individual job failures...
})->dispatch();

```

#### [Retrying Failed Batch Jobs](https://laravel.com/docs/12.x/queues#retrying-failed-batch-jobs)
For convenience, Laravel provides a `queue:retry-batch` Artisan command that allows you to easily retry all of the failed jobs for a given batch. This command accepts the UUID of the batch whose failed jobs should be retried:
```


1php artisan queue:retry-batch 32dbc76c-4f82-4749-b610-a639fe0099b5




php artisan queue:retry-batch 32dbc76c-4f82-4749-b610-a639fe0099b5

```

### [Pruning Batches](https://laravel.com/docs/12.x/queues#pruning-batches)
Without pruning, the `job_batches` table can accumulate records very quickly. To mitigate this, you should [schedule](https://laravel.com/docs/12.x/scheduling) the `queue:prune-batches` Artisan command to run daily:
```


1use Illuminate\Support\Facades\Schedule;




2 



3Schedule::command('queue:prune-batches')->daily();




use Illuminate\Support\Facades\Schedule;

Schedule::command('queue:prune-batches')->daily();

```

By default, all finished batches that are more than 24 hours old will be pruned. You may use the `hours` option when calling the command to determine how long to retain batch data. For example, the following command will delete all batches that finished over 48 hours ago:
```


1use Illuminate\Support\Facades\Schedule;




2 



3Schedule::command('queue:prune-batches --hours=48')->daily();




use Illuminate\Support\Facades\Schedule;

Schedule::command('queue:prune-batches --hours=48')->daily();

```

Sometimes, your `jobs_batches` table may accumulate batch records for batches that never completed successfully, such as batches where a job failed and that job was never retried successfully. You may instruct the `queue:prune-batches` command to prune these unfinished batch records using the `unfinished` option:
```


1use Illuminate\Support\Facades\Schedule;




2 



3Schedule::command('queue:prune-batches --hours=48 --unfinished=72')->daily();




use Illuminate\Support\Facades\Schedule;

Schedule::command('queue:prune-batches --hours=48 --unfinished=72')->daily();

```

Likewise, your `jobs_batches` table may also accumulate batch records for cancelled batches. You may instruct the `queue:prune-batches` command to prune these cancelled batch records using the `cancelled` option:
```


1use Illuminate\Support\Facades\Schedule;




2 



3Schedule::command('queue:prune-batches --hours=48 --cancelled=72')->daily();




use Illuminate\Support\Facades\Schedule;

Schedule::command('queue:prune-batches --hours=48 --cancelled=72')->daily();

```

### [Storing Batches in DynamoDB](https://laravel.com/docs/12.x/queues#storing-batches-in-dynamodb)
Laravel also provides support for storing batch meta information in
Typically, this table should be named `job_batches`, but you should name the table based on the value of the `queue.batching.table` configuration value within your application's `queue` configuration file.
#### [DynamoDB Batch Table Configuration](https://laravel.com/docs/12.x/queues#dynamodb-batch-table-configuration)
The `job_batches` table should have a string primary partition key named `application` and a string primary sort key named `id`. The `application` portion of the key will contain your application's name as defined by the `name` configuration value within your application's `app` configuration file. Since the application name is part of the DynamoDB table's key, you can use the same table to store job batches for multiple Laravel applications.
In addition, you may define `ttl` attribute for your table if you would like to take advantage of [automatic batch pruning](https://laravel.com/docs/12.x/queues#pruning-batches-in-dynamodb).
#### [DynamoDB Configuration](https://laravel.com/docs/12.x/queues#dynamodb-configuration)
Next, install the AWS SDK so that your Laravel application can communicate with Amazon DynamoDB:
```


1composer require aws/aws-sdk-php




composer require aws/aws-sdk-php

```

Then, set the `queue.batching.driver` configuration option's value to `dynamodb`. In addition, you should define `key`, `secret`, and `region` configuration options within the `batching` configuration array. These options will be used to authenticate with AWS. When using the `dynamodb` driver, the `queue.batching.database` configuration option is unnecessary:
```


1'batching' => [




2    'driver' => env('QUEUE_BATCHING_DRIVER', 'dynamodb'),




3    'key' => env('AWS_ACCESS_KEY_ID'),




4    'secret' => env('AWS_SECRET_ACCESS_KEY'),




5    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),




6    'table' => 'job_batches',




7],




'batching' => [
    'driver' => env('QUEUE_BATCHING_DRIVER', 'dynamodb'),
    'key' => env('AWS_ACCESS_KEY_ID'),
    'secret' => env('AWS_SECRET_ACCESS_KEY'),
    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
    'table' => 'job_batches',
],

```

#### [Pruning Batches in DynamoDB](https://laravel.com/docs/12.x/queues#pruning-batches-in-dynamodb)
When utilizing
If you defined your DynamoDB table with a `ttl` attribute, you may define configuration parameters to instruct Laravel how to prune batch records. The `queue.batching.ttl_attribute` configuration value defines the name of the attribute holding the TTL, while the `queue.batching.ttl` configuration value defines the number of seconds after which a batch record can be removed from the DynamoDB table, relative to the last time the record was updated:
```


1'batching' => [




2    'driver' => env('QUEUE_FAILED_DRIVER', 'dynamodb'),




3    'key' => env('AWS_ACCESS_KEY_ID'),




4    'secret' => env('AWS_SECRET_ACCESS_KEY'),




5    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),




6    'table' => 'job_batches',




7    'ttl_attribute' => 'ttl',




8    'ttl' => 60 * 60 * 24 * 7, // 7 days...




9],




'batching' => [
    'driver' => env('QUEUE_FAILED_DRIVER', 'dynamodb'),
    'key' => env('AWS_ACCESS_KEY_ID'),
    'secret' => env('AWS_SECRET_ACCESS_KEY'),
    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
    'table' => 'job_batches',
    'ttl_attribute' => 'ttl',
    'ttl' => 60 * 60 * 24 * 7, // 7 days...
],

```
