## [Testing](https://laravel.com/docs/12.x/notifications#testing)
You may use the `Notification` facade's `fake` method to prevent notifications from being sent. Typically, sending notifications is unrelated to the code you are actually testing. Most likely, it is sufficient to simply assert that Laravel was instructed to send a given notification.
After calling the `Notification` facade's `fake` method, you may then assert that notifications were instructed to be sent to users and even inspect the data the notifications received:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Notifications\OrderShipped;




 4use Illuminate\Support\Facades\Notification;




 5 



 6test('orders can be shipped', function () {




 7    Notification::fake();




 8 



 9    // Perform order shipping...




10 



11    // Assert that no notifications were sent...




12    Notification::assertNothingSent();




13 



14    // Assert a notification was sent to the given users...




15    Notification::assertSentTo(




16        [$user], OrderShipped::class




17    );




18 



19    // Assert a notification was not sent...




20    Notification::assertNotSentTo(




21        [$user], AnotherNotification::class




22    );




23 



24    // Assert a notification was sent twice...




25    Notification::assertSentTimes(WeeklyReminder::class, 2);




26 



27    // Assert that a given number of notifications were sent...




28    Notification::assertCount(3);




29});




<?php

use App\Notifications\OrderShipped;
use Illuminate\Support\Facades\Notification;

test('orders can be shipped', function () {
    Notification::fake();

    // Perform order shipping...

    // Assert that no notifications were sent...
    Notification::assertNothingSent();

    // Assert a notification was sent to the given users...
    Notification::assertSentTo(
        [$user], OrderShipped::class
    );

    // Assert a notification was not sent...
    Notification::assertNotSentTo(
        [$user], AnotherNotification::class
    );

    // Assert a notification was sent twice...
    Notification::assertSentTimes(WeeklyReminder::class, 2);

    // Assert that a given number of notifications were sent...
    Notification::assertCount(3);
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use App\Notifications\OrderShipped;




 6use Illuminate\Support\Facades\Notification;




 7use Tests\TestCase;




 8 



 9class ExampleTest extends TestCase




10{




11    public function test_orders_can_be_shipped(): void




12    {




13        Notification::fake();




14 



15        // Perform order shipping...




16 



17        // Assert that no notifications were sent...




18        Notification::assertNothingSent();




19 



20        // Assert a notification was sent to the given users...




21        Notification::assertSentTo(




22            [$user], OrderShipped::class




23        );




24 



25        // Assert a notification was not sent...




26        Notification::assertNotSentTo(




27            [$user], AnotherNotification::class




28        );




29 



30        // Assert a notification was sent twice...




31        Notification::assertSentTimes(WeeklyReminder::class, 2);




32 



33        // Assert that a given number of notifications were sent...




34        Notification::assertCount(3);




35    }




36}




<?php

namespace Tests\Feature;

use App\Notifications\OrderShipped;
use Illuminate\Support\Facades\Notification;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_orders_can_be_shipped(): void
    {
        Notification::fake();

        // Perform order shipping...

        // Assert that no notifications were sent...
        Notification::assertNothingSent();

        // Assert a notification was sent to the given users...
        Notification::assertSentTo(
            [$user], OrderShipped::class
        );

        // Assert a notification was not sent...
        Notification::assertNotSentTo(
            [$user], AnotherNotification::class
        );

        // Assert a notification was sent twice...
        Notification::assertSentTimes(WeeklyReminder::class, 2);

        // Assert that a given number of notifications were sent...
        Notification::assertCount(3);
    }
}

```

You may pass a closure to the `assertSentTo` or `assertNotSentTo` methods in order to assert that a notification was sent that passes a given "truth test". If at least one notification was sent that passes the given truth test then the assertion will be successful:
```


1Notification::assertSentTo(




2    $user,




3    function (OrderShipped $notification, array $channels) use ($order) {




4        return $notification->order->id === $order->id;




5    }




6);




Notification::assertSentTo(
    $user,
    function (OrderShipped $notification, array $channels) use ($order) {
        return $notification->order->id === $order->id;
    }
);

```

#### [On-Demand Notifications](https://laravel.com/docs/12.x/notifications#on-demand-notifications)
If the code you are testing sends [on-demand notifications](https://laravel.com/docs/12.x/notifications#on-demand-notifications), you can test that the on-demand notification was sent via the `assertSentOnDemand` method:
```


1Notification::assertSentOnDemand(OrderShipped::class);




Notification::assertSentOnDemand(OrderShipped::class);

```

By passing a closure as the second argument to the `assertSentOnDemand` method, you may determine if an on-demand notification was sent to the correct "route" address:
```


1Notification::assertSentOnDemand(




2    OrderShipped::class,




3    function (OrderShipped $notification, array $channels, object $notifiable) use ($user) {




4        return $notifiable->routes['mail'] === $user->email;




5    }




6);




Notification::assertSentOnDemand(
    OrderShipped::class,
    function (OrderShipped $notification, array $channels, object $notifiable) use ($user) {
        return $notifiable->routes['mail'] === $user->email;
    }
);

```
