## [Sending Notifications](https://laravel.com/docs/12.x/notifications#sending-notifications)
### [Using the Notifiable Trait](https://laravel.com/docs/12.x/notifications#using-the-notifiable-trait)
Notifications may be sent in two ways: using the `notify` method of the `Notifiable` trait or using the `Notification` [facade](https://laravel.com/docs/12.x/facades). The `Notifiable` trait is included on your application's `App\Models\User` model by default:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Foundation\Auth\User as Authenticatable;




 6use Illuminate\Notifications\Notifiable;




 7 



 8class User extends Authenticatable




 9{




10    use Notifiable;




11}




<?php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use Notifiable;
}

```

The `notify` method that is provided by this trait expects to receive a notification instance:
```


1use App\Notifications\InvoicePaid;




2 



3$user->notify(new InvoicePaid($invoice));




use App\Notifications\InvoicePaid;

$user->notify(new InvoicePaid($invoice));

```

Remember, you may use the `Notifiable` trait on any of your models. You are not limited to only including it on your `User` model.
### [Using the Notification Facade](https://laravel.com/docs/12.x/notifications#using-the-notification-facade)
Alternatively, you may send notifications via the `Notification` [facade](https://laravel.com/docs/12.x/facades). This approach is useful when you need to send a notification to multiple notifiable entities such as a collection of users. To send notifications using the facade, pass all of the notifiable entities and the notification instance to the `send` method:
```


1use Illuminate\Support\Facades\Notification;




2 



3Notification::send($users, new InvoicePaid($invoice));




use Illuminate\Support\Facades\Notification;

Notification::send($users, new InvoicePaid($invoice));

```

You can also send notifications immediately using the `sendNow` method. This method will send the notification immediately even if the notification implements the `ShouldQueue` interface:
```


1Notification::sendNow($developers, new DeploymentCompleted($deployment));




Notification::sendNow($developers, new DeploymentCompleted($deployment));

```

### [Specifying Delivery Channels](https://laravel.com/docs/12.x/notifications#specifying-delivery-channels)
Every notification class has a `via` method that determines on which channels the notification will be delivered. Notifications may be sent on the `mail`, `database`, `broadcast`, `vonage`, and `slack` channels.
If you would like to use other delivery channels such as Telegram or Pusher, check out the community driven
The `via` method receives a `$notifiable` instance, which will be an instance of the class to which the notification is being sent. You may use `$notifiable` to determine which channels the notification should be delivered on:
```


1/**




2 * Get the notification's delivery channels.




3 *




4 * @return array<int, string>




5 */




6public function via(object $notifiable): array




7{




8    return $notifiable->prefers_sms ? ['vonage'] : ['mail', 'database'];




9}




/**
 * Get the notification's delivery channels.
 *
 * @return array<int, string>
 */
public function via(object $notifiable): array
{
    return $notifiable->prefers_sms ? ['vonage'] : ['mail', 'database'];
}

```

### [Queueing Notifications](https://laravel.com/docs/12.x/notifications#queueing-notifications)
Before queueing notifications, you should configure your queue and [start a worker](https://laravel.com/docs/12.x/queues#running-the-queue-worker).
Sending notifications can take time, especially if the channel needs to make an external API call to deliver the notification. To speed up your application's response time, let your notification be queued by adding the `ShouldQueue` interface and `Queueable` trait to your class. The interface and trait are already imported for all notifications generated using the `make:notification` command, so you may immediately add them to your notification class:
```


 1<?php




 2 



 3namespace App\Notifications;




 4 



 5use Illuminate\Bus\Queueable;




 6use Illuminate\Contracts\Queue\ShouldQueue;




 7use Illuminate\Notifications\Notification;




 8 



 9class InvoicePaid extends Notification implements ShouldQueue




10{




11    use Queueable;




12 



13    // ...




14}




<?php

namespace App\Notifications;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Notifications\Notification;

class InvoicePaid extends Notification implements ShouldQueue
{
    use Queueable;

    // ...
}

```

Once the `ShouldQueue` interface has been added to your notification, you may send the notification like normal. Laravel will detect the `ShouldQueue` interface on the class and automatically queue the delivery of the notification:
```


1$user->notify(new InvoicePaid($invoice));




$user->notify(new InvoicePaid($invoice));

```

When queueing notifications, a queued job will be created for each recipient and channel combination. For example, six jobs will be dispatched to the queue if your notification has three recipients and two channels.
#### [Delaying Notifications](https://laravel.com/docs/12.x/notifications#delaying-notifications)
If you would like to delay the delivery of the notification, you may chain the `delay` method onto your notification instantiation:
```


1$delay = now()->plus(minutes: 10);




2 



3$user->notify((new InvoicePaid($invoice))->delay($delay));




$delay = now()->plus(minutes: 10);

$user->notify((new InvoicePaid($invoice))->delay($delay));

```

You may pass an array to the `delay` method to specify the delay amount for specific channels:
```


1$user->notify((new InvoicePaid($invoice))->delay([




2    'mail' => now()->plus(minutes: 5),




3    'sms' => now()->plus(minutes: 10),




4]));




$user->notify((new InvoicePaid($invoice))->delay([
    'mail' => now()->plus(minutes: 5),
    'sms' => now()->plus(minutes: 10),
]));

```

Alternatively, you may define a `withDelay` method on the notification class itself. The `withDelay` method should return an array of channel names and delay values:
```


 1/**




 2 * Determine the notification's delivery delay.




 3 *




 4 * @return array<string, \Illuminate\Support\Carbon>




 5 */




 6public function withDelay(object $notifiable): array




 7{




 8    return [




 9        'mail' => now()->plus(minutes: 5),




10        'sms' => now()->plus(minutes: 10),




11    ];




12}




/**
 * Determine the notification's delivery delay.
 *
 * @return array<string, \Illuminate\Support\Carbon>
 */
public function withDelay(object $notifiable): array
{
    return [
        'mail' => now()->plus(minutes: 5),
        'sms' => now()->plus(minutes: 10),
    ];
}

```

#### [Customizing the Notification Queue Connection](https://laravel.com/docs/12.x/notifications#customizing-the-notification-queue-connection)
By default, queued notifications will be queued using your application's default queue connection. If you would like to specify a different connection that should be used for a particular notification, you may call the `onConnection` method from your notification's constructor:
```


 1<?php




 2 



 3namespace App\Notifications;




 4 



 5use Illuminate\Bus\Queueable;




 6use Illuminate\Contracts\Queue\ShouldQueue;




 7use Illuminate\Notifications\Notification;




 8 



 9class InvoicePaid extends Notification implements ShouldQueue




10{




11    use Queueable;




12 



13    /**




14     * Create a new notification instance.




15     */




16    public function __construct()




17    {




18        $this->onConnection('redis');




19    }




20}




<?php

namespace App\Notifications;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Notifications\Notification;

class InvoicePaid extends Notification implements ShouldQueue
{
    use Queueable;

    /**
     * Create a new notification instance.
     */
    public function __construct()
    {
        $this->onConnection('redis');
    }
}

```

Or, if you would like to specify a specific queue connection that should be used for each notification channel supported by the notification, you may define a `viaConnections` method on your notification. This method should return an array of channel name / queue connection name pairs:
```


 1/**




 2 * Determine which connections should be used for each notification channel.




 3 *




 4 * @return array<string, string>




 5 */




 6public function viaConnections(): array




 7{




 8    return [




 9        'mail' => 'redis',




10        'database' => 'sync',




11    ];




12}




/**
 * Determine which connections should be used for each notification channel.
 *
 * @return array<string, string>
 */
public function viaConnections(): array
{
    return [
        'mail' => 'redis',
        'database' => 'sync',
    ];
}

```

#### [Customizing Notification Channel Queues](https://laravel.com/docs/12.x/notifications#customizing-notification-channel-queues)
If you would like to specify a specific queue that should be used for each notification channel supported by the notification, you may define a `viaQueues` method on your notification. This method should return an array of channel name / queue name pairs:
```


 1/**




 2 * Determine which queues should be used for each notification channel.




 3 *




 4 * @return array<string, string>




 5 */




 6public function viaQueues(): array




 7{




 8    return [




 9        'mail' => 'mail-queue',




10        'slack' => 'slack-queue',




11    ];




12}




/**
 * Determine which queues should be used for each notification channel.
 *
 * @return array<string, string>
 */
public function viaQueues(): array
{
    return [
        'mail' => 'mail-queue',
        'slack' => 'slack-queue',
    ];
}

```

#### [Customizing Queued Notification Job Properties](https://laravel.com/docs/12.x/notifications#customizing-queued-notification-job-properties)
You may customize the behavior of the underlying queued job by defining properties on your notification class. These properties will be inherited by the queued job that sends the notification:
```


 1<?php




 2 



 3namespace App\Notifications;




 4 



 5use Illuminate\Bus\Queueable;




 6use Illuminate\Contracts\Queue\ShouldQueue;




 7use Illuminate\Notifications\Notification;




 8 



 9class InvoicePaid extends Notification implements ShouldQueue




10{




11    use Queueable;




12 



13    /**




14     * The number of times the notification may be attempted.




15     *




16     * @var int




17     */




18    public $tries = 5;




19 



20    /**




21     * The number of seconds the notification can run before timing out.




22     *




23     * @var int




24     */




25    public $timeout = 120;




26 



27    /**




28     * The maximum number of unhandled exceptions to allow before failing.




29     *




30     * @var int




31     */




32    public $maxExceptions = 3;




33 



34    // ...




35}




<?php

namespace App\Notifications;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Notifications\Notification;

class InvoicePaid extends Notification implements ShouldQueue
{
    use Queueable;

    /**
     * The number of times the notification may be attempted.
     *
     * @var int
     */
    public $tries = 5;

    /**
     * The number of seconds the notification can run before timing out.
     *
     * @var int
     */
    public $timeout = 120;

    /**
     * The maximum number of unhandled exceptions to allow before failing.
     *
     * @var int
     */
    public $maxExceptions = 3;

    // ...
}

```

If you would like to ensure the privacy and integrity of a queued notification's data via [encryption](https://laravel.com/docs/12.x/encryption), add the `ShouldBeEncrypted` interface to your notification class:
```


 1<?php




 2 



 3namespace App\Notifications;




 4 



 5use Illuminate\Bus\Queueable;




 6use Illuminate\Contracts\Queue\ShouldBeEncrypted;




 7use Illuminate\Contracts\Queue\ShouldQueue;




 8use Illuminate\Notifications\Notification;




 9 



10class InvoicePaid extends Notification implements ShouldQueue, ShouldBeEncrypted




11{




12    use Queueable;




13 



14    // ...




15}




<?php

namespace App\Notifications;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldBeEncrypted;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Notifications\Notification;

class InvoicePaid extends Notification implements ShouldQueue, ShouldBeEncrypted
{
    use Queueable;

    // ...
}

```

In addition to defining these properties directly on your notification class, you may also define `backoff` and `retryUntil` methods to specify the backoff strategy and retry timeout for the queued notification job:
```


 1use DateTime;




 2 



 3/**




 4 * Calculate the number of seconds to wait before retrying the notification.




 5 */




 6public function backoff(): int




 7{




 8    return 3;




 9}




10 



11/**




12 * Determine the time at which the notification should timeout.




13 */




14public function retryUntil(): DateTime




15{




16    return now()->plus(minutes: 5);




17}




use DateTime;

/**
 * Calculate the number of seconds to wait before retrying the notification.
 */
public function backoff(): int
{
    return 3;
}

/**
 * Determine the time at which the notification should timeout.
 */
public function retryUntil(): DateTime
{
    return now()->plus(minutes: 5);
}

```

For more information on these job properties and methods, please review the documentation on [queued jobs](https://laravel.com/docs/12.x/queues#max-job-attempts-and-timeout).
#### [Queued Notification Middleware](https://laravel.com/docs/12.x/notifications#queued-notification-middleware)
Queued notifications may define middleware [just like queued jobs](https://laravel.com/docs/12.x/queues#job-middleware). To get started, define a `middleware` method on your notification class. The `middleware` method will receive `$notifiable` and `$channel` variables, which allow you to customize the returned middleware based on the notification's destination:
```


 1use Illuminate\Queue\Middleware\RateLimited;




 2 



 3/**




 4 * Get the middleware the notification job should pass through.




 5 *




 6 * @return array<int, object>




 7 */




 8public function middleware(object $notifiable, string $channel)




 9{




10    return match ($channel) {




11        'mail' => [new RateLimited('postmark')],




12        'slack' => [new RateLimited('slack')],




13        default => [],




14    };




15}




use Illuminate\Queue\Middleware\RateLimited;

/**
 * Get the middleware the notification job should pass through.
 *
 * @return array<int, object>
 */
public function middleware(object $notifiable, string $channel)
{
    return match ($channel) {
        'mail' => [new RateLimited('postmark')],
        'slack' => [new RateLimited('slack')],
        default => [],
    };
}

```

#### [Queued Notifications and Database Transactions](https://laravel.com/docs/12.x/notifications#queued-notifications-and-database-transactions)
When queued notifications are dispatched within database transactions, they may be processed by the queue before the database transaction has committed. When this happens, any updates you have made to models or database records during the database transaction may not yet be reflected in the database. In addition, any models or database records created within the transaction may not exist in the database. If your notification depends on these models, unexpected errors can occur when the job that sends the queued notification is processed.
If your queue connection's `after_commit` configuration option is set to `false`, you may still indicate that a particular queued notification should be dispatched after all open database transactions have been committed by calling the `afterCommit` method when sending the notification:
```


1use App\Notifications\InvoicePaid;




2 



3$user->notify((new InvoicePaid($invoice))->afterCommit());




use App\Notifications\InvoicePaid;

$user->notify((new InvoicePaid($invoice))->afterCommit());

```

Alternatively, you may call the `afterCommit` method from your notification's constructor:
```


 1<?php




 2 



 3namespace App\Notifications;




 4 



 5use Illuminate\Bus\Queueable;




 6use Illuminate\Contracts\Queue\ShouldQueue;




 7use Illuminate\Notifications\Notification;




 8 



 9class InvoicePaid extends Notification implements ShouldQueue




10{




11    use Queueable;




12 



13    /**




14     * Create a new notification instance.




15     */




16    public function __construct()




17    {




18        $this->afterCommit();




19    }




20}




<?php

namespace App\Notifications;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Notifications\Notification;

class InvoicePaid extends Notification implements ShouldQueue
{
    use Queueable;

    /**
     * Create a new notification instance.
     */
    public function __construct()
    {
        $this->afterCommit();
    }
}

```

To learn more about working around these issues, please review the documentation regarding [queued jobs and database transactions](https://laravel.com/docs/12.x/queues#jobs-and-database-transactions).
#### [Determining if a Queued Notification Should Be Sent](https://laravel.com/docs/12.x/notifications#determining-if-the-queued-notification-should-be-sent)
After a queued notification has been dispatched for the queue for background processing, it will typically be accepted by a queue worker and sent to its intended recipient.
However, if you would like to make the final determination on whether the queued notification should be sent after it is being processed by a queue worker, you may define a `shouldSend` method on the notification class. If this method returns `false`, the notification will not be sent:
```


1/**




2 * Determine if the notification should be sent.




3 */




4public function shouldSend(object $notifiable, string $channel): bool




5{




6    return $this->invoice->isPaid();




7}




/**
 * Determine if the notification should be sent.
 */
public function shouldSend(object $notifiable, string $channel): bool
{
    return $this->invoice->isPaid();
}

```

#### [After Sending Notifications](https://laravel.com/docs/12.x/notifications#after-sending-notifications)
If you would like to execute code after a notification has been sent, you may define an `afterSending` method on the notification class. This method will receive the notifiable entity, the channel name, and the response from the channel:
```


1/**




2 * Handle the notification after it has been sent.




3 */




4public function afterSending(object $notifiable, string $channel, mixed $response): void




5{




6    // ...




7}




/**
 * Handle the notification after it has been sent.
 */
public function afterSending(object $notifiable, string $channel, mixed $response): void
{
    // ...
}

```

### [On-Demand Notifications](https://laravel.com/docs/12.x/notifications#on-demand-notifications)
Sometimes you may need to send a notification to someone who is not stored as a "user" of your application. Using the `Notification` facade's `route` method, you may specify ad-hoc notification routing information before sending the notification:
```


1use Illuminate\Broadcasting\Channel;




2use Illuminate\Support\Facades\Notification;




3 



4Notification::route('mail', 'taylor@example.com')




5    ->route('vonage', '5555555555')




6    ->route('slack', '#slack-channel')




7    ->route('broadcast', [new Channel('channel-name')])




8    ->notify(new InvoicePaid($invoice));




use Illuminate\Broadcasting\Channel;
use Illuminate\Support\Facades\Notification;

Notification::route('mail', 'taylor@example.com')
    ->route('vonage', '5555555555')
    ->route('slack', '#slack-channel')
    ->route('broadcast', [new Channel('channel-name')])
    ->notify(new InvoicePaid($invoice));

```

If you would like to provide the recipient's name when sending an on-demand notification to the `mail` route, you may provide an array that contains the email address as the key and the name as the value of the first element in the array:
```


1Notification::route('mail', [




2    'barrett@example.com' => 'Barrett Blair',




3])->notify(new InvoicePaid($invoice));




Notification::route('mail', [
    'barrett@example.com' => 'Barrett Blair',
])->notify(new InvoicePaid($invoice));

```

Using the `routes` method, you may provide ad-hoc routing information for multiple notification channels at once:
```


1Notification::routes([




2    'mail' => ['barrett@example.com' => 'Barrett Blair'],




3    'vonage' => '5555555555',




4])->notify(new InvoicePaid($invoice));




Notification::routes([
    'mail' => ['barrett@example.com' => 'Barrett Blair'],
    'vonage' => '5555555555',
])->notify(new InvoicePaid($invoice));

```
