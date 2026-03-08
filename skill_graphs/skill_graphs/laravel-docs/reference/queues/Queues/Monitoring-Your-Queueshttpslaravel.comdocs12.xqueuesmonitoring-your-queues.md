## [Monitoring Your Queues](https://laravel.com/docs/12.x/queues#monitoring-your-queues)
If your queue receives a sudden influx of jobs, it could become overwhelmed, leading to a long wait time for jobs to complete. If you wish, Laravel can alert you when your queue job count exceeds a specified threshold.
To get started, you should schedule the `queue:monitor` command to [run every minute](https://laravel.com/docs/12.x/scheduling). The command accepts the names of the queues you wish to monitor as well as your desired job count threshold:
```


1php artisan queue:monitor redis:default,redis:deployments --max=100




php artisan queue:monitor redis:default,redis:deployments --max=100

```

Scheduling this command alone is not enough to trigger a notification alerting you of the queue's overwhelmed status. When the command encounters a queue that has a job count exceeding your threshold, an `Illuminate\Queue\Events\QueueBusy` event will be dispatched. You may listen for this event within your application's `AppServiceProvider` in order to send a notification to you or your development team:
```


 1use App\Notifications\QueueHasLongWaitTime;




 2use Illuminate\Queue\Events\QueueBusy;




 3use Illuminate\Support\Facades\Event;




 4use Illuminate\Support\Facades\Notification;




 5 



 6/**




 7 * Bootstrap any application services.




 8 */




 9public function boot(): void




10{




11    Event::listen(function (QueueBusy $event) {




12        Notification::route('mail', 'dev@example.com')




13            ->notify(new QueueHasLongWaitTime(




14                $event->connection,




15                $event->queue,




16                $event->size




17            ));




18    });




19}




use App\Notifications\QueueHasLongWaitTime;
use Illuminate\Queue\Events\QueueBusy;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Notification;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Event::listen(function (QueueBusy $event) {
        Notification::route('mail', 'dev@example.com')
            ->notify(new QueueHasLongWaitTime(
                $event->connection,
                $event->queue,
                $event->size
            ));
    });
}

```
