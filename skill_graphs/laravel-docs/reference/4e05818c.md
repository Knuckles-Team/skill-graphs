## [Notification Events](https://laravel.com/docs/12.x/notifications#notification-events)
#### [Notification Sending Event](https://laravel.com/docs/12.x/notifications#notification-sending-event)
When a notification is sending, the `Illuminate\Notifications\Events\NotificationSending` event is dispatched by the notification system. This contains the "notifiable" entity and the notification instance itself. You may create [event listeners](https://laravel.com/docs/12.x/events) for this event within your application:
```


 1use Illuminate\Notifications\Events\NotificationSending;




 2 



 3class CheckNotificationStatus




 4{




 5    /**




 6     * Handle the event.




 7     */




 8    public function handle(NotificationSending $event): void




 9    {




10        // ...




11    }




12}




use Illuminate\Notifications\Events\NotificationSending;

class CheckNotificationStatus
{
    /**
     * Handle the event.
     */
    public function handle(NotificationSending $event): void
    {
        // ...
    }
}

```

The notification will not be sent if an event listener for the `NotificationSending` event returns `false` from its `handle` method:
```


1/**




2 * Handle the event.




3 */




4public function handle(NotificationSending $event): bool




5{




6    return false;




7}




/**
 * Handle the event.
 */
public function handle(NotificationSending $event): bool
{
    return false;
}

```

Within an event listener, you may access the `notifiable`, `notification`, and `channel` properties on the event to learn more about the notification recipient or the notification itself:
```


1/**




2 * Handle the event.




3 */




4public function handle(NotificationSending $event): void




5{




6    // $event->channel




7    // $event->notifiable




8    // $event->notification




9}




/**
 * Handle the event.
 */
public function handle(NotificationSending $event): void
{
    // $event->channel
    // $event->notifiable
    // $event->notification
}

```

#### [Notification Sent Event](https://laravel.com/docs/12.x/notifications#notification-sent-event)
When a notification is sent, the `Illuminate\Notifications\Events\NotificationSent` [event](https://laravel.com/docs/12.x/events) is dispatched by the notification system. This contains the "notifiable" entity and the notification instance itself. You may create [event listeners](https://laravel.com/docs/12.x/events) for this event within your application:
```


 1use Illuminate\Notifications\Events\NotificationSent;




 2 



 3class LogNotification




 4{




 5    /**




 6     * Handle the event.




 7     */




 8    public function handle(NotificationSent $event): void




 9    {




10        // ...




11    }




12}




use Illuminate\Notifications\Events\NotificationSent;

class LogNotification
{
    /**
     * Handle the event.
     */
    public function handle(NotificationSent $event): void
    {
        // ...
    }
}

```

Within an event listener, you may access the `notifiable`, `notification`, `channel`, and `response` properties on the event to learn more about the notification recipient or the notification itself:
```


 1/**




 2 * Handle the event.




 3 */




 4public function handle(NotificationSent $event): void




 5{




 6    // $event->channel




 7    // $event->notifiable




 8    // $event->notification




 9    // $event->response




10}




/**
 * Handle the event.
 */
public function handle(NotificationSent $event): void
{
    // $event->channel
    // $event->notifiable
    // $event->notification
    // $event->response
}

```
