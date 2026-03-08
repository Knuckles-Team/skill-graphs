## [Running the Queue Worker](https://laravel.com/docs/12.x/queues#running-the-queue-worker)
### [The `queue:work` Command](https://laravel.com/docs/12.x/queues#the-queue-work-command)
Laravel includes an Artisan command that will start a queue worker and process new jobs as they are pushed onto the queue. You may run the worker using the `queue:work` Artisan command. Note that once the `queue:work` command has started, it will continue to run until it is manually stopped or you close your terminal:
```


1php artisan queue:work




php artisan queue:work

```

To keep the `queue:work` process running permanently in the background, you should use a process monitor such as [Supervisor](https://laravel.com/docs/12.x/queues#supervisor-configuration) to ensure that the queue worker does not stop running.
You may include the `-v` flag when invoking the `queue:work` command if you would like the processed job IDs, connection names, and queue names to be included in the command's output:
```


1php artisan queue:work -v




php artisan queue:work -v

```

Remember, queue workers are long-lived processes and store the booted application state in memory. As a result, they will not notice changes in your code base after they have been started. So, during your deployment process, be sure to [restart your queue workers](https://laravel.com/docs/12.x/queues#queue-workers-and-deployment). In addition, remember that any static state created or modified by your application will not be automatically reset between jobs.
Alternatively, you may run the `queue:listen` command. When using the `queue:listen` command, you don't have to manually restart the worker when you want to reload your updated code or reset the application state; however, this command is significantly less efficient than the `queue:work` command:
```


1php artisan queue:listen




php artisan queue:listen

```

#### [Running Multiple Queue Workers](https://laravel.com/docs/12.x/queues#running-multiple-queue-workers)
To assign multiple workers to a queue and process jobs concurrently, you should simply start multiple `queue:work` processes. This can either be done locally via multiple tabs in your terminal or in production using your process manager's configuration settings. [When using Supervisor](https://laravel.com/docs/12.x/queues#supervisor-configuration), you may use the `numprocs` configuration value.
#### [Specifying the Connection and Queue](https://laravel.com/docs/12.x/queues#specifying-the-connection-queue)
You may also specify which queue connection the worker should utilize. The connection name passed to the `work` command should correspond to one of the connections defined in your `config/queue.php` configuration file:
```


1php artisan queue:work redis




php artisan queue:work redis

```

By default, the `queue:work` command only processes jobs for the default queue on a given connection. However, you may customize your queue worker even further by only processing particular queues for a given connection. For example, if all of your emails are processed in an `emails` queue on your `redis` queue connection, you may issue the following command to start a worker that only processes that queue:
```


1php artisan queue:work redis --queue=emails




php artisan queue:work redis --queue=emails

```

#### [Processing a Specified Number of Jobs](https://laravel.com/docs/12.x/queues#processing-a-specified-number-of-jobs)
The `--once` option may be used to instruct the worker to only process a single job from the queue:
```


1php artisan queue:work --once




php artisan queue:work --once

```

The `--max-jobs` option may be used to instruct the worker to process the given number of jobs and then exit. This option may be useful when combined with [Supervisor](https://laravel.com/docs/12.x/queues#supervisor-configuration) so that your workers are automatically restarted after processing a given number of jobs, releasing any memory they may have accumulated:
```


1php artisan queue:work --max-jobs=1000




php artisan queue:work --max-jobs=1000

```

#### [Processing All Queued Jobs and Then Exiting](https://laravel.com/docs/12.x/queues#processing-all-queued-jobs-then-exiting)
The `--stop-when-empty` option may be used to instruct the worker to process all jobs and then exit gracefully. This option can be useful when processing Laravel queues within a Docker container if you wish to shutdown the container after the queue is empty:
```


1php artisan queue:work --stop-when-empty




php artisan queue:work --stop-when-empty

```

#### [Processing Jobs for a Given Number of Seconds](https://laravel.com/docs/12.x/queues#processing-jobs-for-a-given-number-of-seconds)
The `--max-time` option may be used to instruct the worker to process jobs for the given number of seconds and then exit. This option may be useful when combined with [Supervisor](https://laravel.com/docs/12.x/queues#supervisor-configuration) so that your workers are automatically restarted after processing jobs for a given amount of time, releasing any memory they may have accumulated:
```


1# Process jobs for one hour and then exit...




2php artisan queue:work --max-time=3600




# Process jobs for one hour and then exit...
php artisan queue:work --max-time=3600

```

#### [Worker Sleep Duration](https://laravel.com/docs/12.x/queues#worker-sleep-duration)
When jobs are available on the queue, the worker will keep processing jobs with no delay in between jobs. However, the `sleep` option determines how many seconds the worker will "sleep" if there are no jobs available. Of course, while sleeping, the worker will not process any new jobs:
```


1php artisan queue:work --sleep=3




php artisan queue:work --sleep=3

```

#### [Maintenance Mode and Queues](https://laravel.com/docs/12.x/queues#maintenance-mode-queues)
While your application is in [maintenance mode](https://laravel.com/docs/12.x/configuration#maintenance-mode), no queued jobs will be handled. The jobs will continue to be handled as normal once the application is out of maintenance mode.
To force your queue workers to process jobs even if maintenance mode is enabled, you may use `--force` option:
```


1php artisan queue:work --force




php artisan queue:work --force

```

#### [Resource Considerations](https://laravel.com/docs/12.x/queues#resource-considerations)
Daemon queue workers do not "reboot" the framework before processing each job. Therefore, you should release any heavy resources after each job completes. For example, if you are doing image manipulation with the `imagedestroy` when you are done processing the image.
### [Queue Priorities](https://laravel.com/docs/12.x/queues#queue-priorities)
Sometimes you may wish to prioritize how your queues are processed. For example, in your `config/queue.php` configuration file, you may set the default `queue` for your `redis` connection to `low`. However, occasionally you may wish to push a job to a `high` priority queue like so:
```


1dispatch((new Job)->onQueue('high'));




dispatch((new Job)->onQueue('high'));

```

To start a worker that verifies that all of the `high` queue jobs are processed before continuing to any jobs on the `low` queue, pass a comma-delimited list of queue names to the `work` command:
```


1php artisan queue:work --queue=high,low




php artisan queue:work --queue=high,low

```

### [Queue Workers and Deployment](https://laravel.com/docs/12.x/queues#queue-workers-and-deployment)
Since queue workers are long-lived processes, they will not notice changes to your code without being restarted. So, the simplest way to deploy an application using queue workers is to restart the workers during your deployment process. You may gracefully restart all of the workers by issuing the `queue:restart` command:
```


1php artisan queue:restart




php artisan queue:restart

```

This command will instruct all queue workers to gracefully exit after they finish processing their current job so that no existing jobs are lost. Since the queue workers will exit when the `queue:restart` command is executed, you should be running a process manager such as [Supervisor](https://laravel.com/docs/12.x/queues#supervisor-configuration) to automatically restart the queue workers.
The queue uses the [cache](https://laravel.com/docs/12.x/cache) to store restart signals, so you should verify that a cache driver is properly configured for your application before using this feature.
### [Job Expirations and Timeouts](https://laravel.com/docs/12.x/queues#job-expirations-and-timeouts)
#### [Job Expiration](https://laravel.com/docs/12.x/queues#job-expiration)
In your `config/queue.php` configuration file, each queue connection defines a `retry_after` option. This option specifies how many seconds the queue connection should wait before retrying a job that is being processed. For example, if the value of `retry_after` is set to `90`, the job will be released back onto the queue if it has been processing for 90 seconds without being released or deleted. Typically, you should set the `retry_after` value to the maximum number of seconds your jobs should reasonably take to complete processing.
The only queue connection which does not contain a `retry_after` value is Amazon SQS. SQS will retry the job based on the
#### [Worker Timeouts](https://laravel.com/docs/12.x/queues#worker-timeouts)
The `queue:work` Artisan command exposes a `--timeout` option. By default, the `--timeout` value is 60 seconds. If a job is processing for longer than the number of seconds specified by the timeout value, the worker processing the job will exit with an error. Typically, the worker will be restarted automatically by a [process manager configured on your server](https://laravel.com/docs/12.x/queues#supervisor-configuration):
```


1php artisan queue:work --timeout=60




php artisan queue:work --timeout=60

```

The `retry_after` configuration option and the `--timeout` CLI option are different, but work together to ensure that jobs are not lost and that jobs are only successfully processed once.
The `--timeout` value should always be at least several seconds shorter than your `retry_after` configuration value. This will ensure that a worker processing a frozen job is always terminated before the job is retried. If your `--timeout` option is longer than your `retry_after` configuration value, your jobs may be processed twice.
### [Pausing and Resuming Queue Workers](https://laravel.com/docs/12.x/queues#pausing-and-resuming-queue-workers)
Sometimes you may need to temporarily prevent a queue worker from processing new jobs without stopping the worker entirely. For example, you may want to pause job processing during system maintenance. Laravel provides the `queue:pause` and `queue:continue` Artisan commands to pause and resume queue workers.
To pause a specific queue, provide the queue connection name and the queue name:
```


1php artisan queue:pause database:default




php artisan queue:pause database:default

```

In this example, `database` is the queue connection name and `default` is the queue name. Once a queue is paused, any workers processing jobs from that queue will continue to finish their current job, but will not pick up any new jobs until the queue is resumed.
To resume processing jobs on a paused queue, use the `queue:continue` command:
```


1php artisan queue:continue database:default




php artisan queue:continue database:default

```

After resuming a queue, workers will begin processing new jobs from that queue immediately. Note that pausing a queue does not stop the worker process itself - it only prevents the worker from processing new jobs from the specified queue.
#### [Worker Restart and Pause Signals](https://laravel.com/docs/12.x/queues#worker-restart-and-pause-signals)
By default, queue workers poll the cache driver for restart and pause signals on each job iteration. While this polling is essential for responding to `queue:restart` and `queue:pause` commands, it does introduce a small performance overhead.
If you need to optimize performance and don't require these interruption features, you may disable this polling globally by calling the `withoutInterruptionPolling` method on the `Queue` facade. This should typically be done in the `boot` method of your `AppServiceProvider`:
```


1use Illuminate\Support\Facades\Queue;




2 



3/**




4 * Bootstrap any application services.




5 */




6public function boot(): void




7{




8    Queue::withoutInterruptionPolling();




9}




use Illuminate\Support\Facades\Queue;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Queue::withoutInterruptionPolling();
}

```

Alternatively, you may disable restart or pause polling individually by setting the static `$restartable` or `$pausable` properties on the `Illuminate\Queue\Worker` class:
```


 1use Illuminate\Queue\Worker;




 2 



 3/**




 4 * Bootstrap any application services.




 5 */




 6public function boot(): void




 7{




 8    Worker::$restartable = false;




 9    Worker::$pausable = false;




10}




use Illuminate\Queue\Worker;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Worker::$restartable = false;
    Worker::$pausable = false;
}

```

When interruption polling is disabled, workers will not respond to `queue:restart` or `queue:pause` commands (depending on which features are disabled).
