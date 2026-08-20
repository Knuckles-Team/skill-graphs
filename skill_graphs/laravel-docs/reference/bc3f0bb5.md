## [Introduction](https://laravel.com/docs/12.x/queues#introduction)
While building your web application, you may have some tasks, such as parsing and storing an uploaded CSV file, that take too long to perform during a typical web request. Thankfully, Laravel allows you to easily create queued jobs that may be processed in the background. By moving time intensive tasks to a queue, your application can respond to web requests with blazing speed and provide a better user experience to your customers.
Laravel queues provide a unified queueing API across a variety of different queue backends, such as
Laravel's queue configuration options are stored in your application's `config/queue.php` configuration file. In this file, you will find connection configurations for each of the queue drivers that are included with the framework, including the database, `null` queue driver is also included which discards queued jobs.
Laravel Horizon is a beautiful dashboard and configuration system for your Redis powered queues. Check out the full [Horizon documentation](https://laravel.com/docs/12.x/horizon) for more information.
### [Connections vs. Queues](https://laravel.com/docs/12.x/queues#connections-vs-queues)
Before getting started with Laravel queues, it is important to understand the distinction between "connections" and "queues". In your `config/queue.php` configuration file, there is a `connections` configuration array. This option defines the connections to backend queue services such as Amazon SQS, Beanstalk, or Redis. However, any given queue connection may have multiple "queues" which may be thought of as different stacks or piles of queued jobs.
Note that each connection configuration example in the `queue` configuration file contains a `queue` attribute. This is the default queue that jobs will be dispatched to when they are sent to a given connection. In other words, if you dispatch a job without explicitly defining which queue it should be dispatched to, the job will be placed on the queue that is defined in the `queue` attribute of the connection configuration:
```


1use App\Jobs\ProcessPodcast;




2 



3// This job is sent to the default connection's default queue...




4ProcessPodcast::dispatch();




5 



6// This job is sent to the default connection's "emails" queue...




7ProcessPodcast::dispatch()->onQueue('emails');




use App\Jobs\ProcessPodcast;

// This job is sent to the default connection's default queue...
ProcessPodcast::dispatch();

// This job is sent to the default connection's "emails" queue...
ProcessPodcast::dispatch()->onQueue('emails');

```

Some applications may not need to ever push jobs onto multiple queues, instead preferring to have one simple queue. However, pushing jobs to multiple queues can be especially useful for applications that wish to prioritize or segment how jobs are processed, since the Laravel queue worker allows you to specify which queues it should process by priority. For example, if you push jobs to a `high` queue, you may run a worker that gives them higher processing priority:
```


1php artisan queue:work --queue=high,default




php artisan queue:work --queue=high,default

```

### [Driver Notes and Prerequisites](https://laravel.com/docs/12.x/queues#driver-prerequisites)
#### [Database](https://laravel.com/docs/12.x/queues#database)
In order to use the `database` queue driver, you will need a database table to hold the jobs. Typically, this is included in Laravel's default `0001_01_01_000002_create_jobs_table.php` [database migration](https://laravel.com/docs/12.x/migrations); however, if your application does not contain this migration, you may use the `make:queue-table` Artisan command to create it:
```


1php artisan make:queue-table




2 



3php artisan migrate




php artisan make:queue-table

php artisan migrate

```

#### [Redis](https://laravel.com/docs/12.x/queues#redis)
In order to use the `redis` queue driver, you should configure a Redis database connection in your `config/database.php` configuration file.
The `serializer` and `compression` Redis options are not supported by the `redis` queue driver.
##### [Redis Cluster](https://laravel.com/docs/12.x/queues#redis-cluster)
If your Redis queue connection uses a
```


1'redis' => [




2    'driver' => 'redis',




3    'connection' => env('REDIS_QUEUE_CONNECTION', 'default'),




4    'queue' => env('REDIS_QUEUE', '{default}'),




5    'retry_after' => env('REDIS_QUEUE_RETRY_AFTER', 90),




6    'block_for' => null,




7    'after_commit' => false,




8],




'redis' => [
    'driver' => 'redis',
    'connection' => env('REDIS_QUEUE_CONNECTION', 'default'),
    'queue' => env('REDIS_QUEUE', '{default}'),
    'retry_after' => env('REDIS_QUEUE_RETRY_AFTER', 90),
    'block_for' => null,
    'after_commit' => false,
],

```

##### [Blocking](https://laravel.com/docs/12.x/queues#blocking)
When using the Redis queue, you may use the `block_for` configuration option to specify how long the driver should wait for a job to become available before iterating through the worker loop and re-polling the Redis database.
Adjusting this value based on your queue load can be more efficient than continually polling the Redis database for new jobs. For instance, you may set the value to `5` to indicate that the driver should block for five seconds while waiting for a job to become available:
```


1'redis' => [




2    'driver' => 'redis',




3    'connection' => env('REDIS_QUEUE_CONNECTION', 'default'),




4    'queue' => env('REDIS_QUEUE', 'default'),




5    'retry_after' => env('REDIS_QUEUE_RETRY_AFTER', 90),




6    'block_for' => 5,




7    'after_commit' => false,




8],




'redis' => [
    'driver' => 'redis',
    'connection' => env('REDIS_QUEUE_CONNECTION', 'default'),
    'queue' => env('REDIS_QUEUE', 'default'),
    'retry_after' => env('REDIS_QUEUE_RETRY_AFTER', 90),
    'block_for' => 5,
    'after_commit' => false,
],

```

Setting `block_for` to `0` will cause queue workers to block indefinitely until a job is available. This will also prevent signals such as `SIGTERM` from being handled until the next job has been processed.
#### [Other Driver Prerequisites](https://laravel.com/docs/12.x/queues#other-driver-prerequisites)
The following dependencies are needed for the listed queue drivers. These dependencies may be installed via the Composer package manager:
  * Amazon SQS: `aws/aws-sdk-php ~3.0`
  * Beanstalkd: `pda/pheanstalk ~5.0`
  * Redis: `predis/predis ~2.0` or phpredis PHP extension
  * `mongodb/laravel-mongodb`
