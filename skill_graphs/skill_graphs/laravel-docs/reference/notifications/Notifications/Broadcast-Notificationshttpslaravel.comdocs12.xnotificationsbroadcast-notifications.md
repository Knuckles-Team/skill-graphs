## [Broadcast Notifications](https://laravel.com/docs/12.x/notifications#broadcast-notifications)
### [Prerequisites](https://laravel.com/docs/12.x/notifications#broadcast-prerequisites)
Before broadcasting notifications, you should configure and be familiar with Laravel's [event broadcasting](https://laravel.com/docs/12.x/broadcasting) services. Event broadcasting provides a way to react to server-side Laravel events from your JavaScript powered frontend.
### [Formatting Broadcast Notifications](https://laravel.com/docs/12.x/notifications#formatting-broadcast-notifications)
The `broadcast` channel broadcasts notifications using Laravel's [event broadcasting](https://laravel.com/docs/12.x/broadcasting) services, allowing your JavaScript powered frontend to catch notifications in realtime. If a notification supports broadcasting, you can define a `toBroadcast` method on the notification class. This method will receive a `$notifiable` entity and should return a `BroadcastMessage` instance. If the `toBroadcast` method does not exist, the `toArray` method will be used to gather the data that should be broadcast. The returned data will be encoded as JSON and broadcast to your JavaScript powered frontend. Let's take a look at an example `toBroadcast` method:
```


 1use Illuminate\Notifications\Messages\BroadcastMessage;




 2 



 3/**




 4 * Get the broadcastable representation of the notification.




 5 */




 6public function toBroadcast(object $notifiable): BroadcastMessage




 7{




 8    return new BroadcastMessage([




 9        'invoice_id' => $this->invoice->id,




10        'amount' => $this->invoice->amount,




11    ]);




12}




use Illuminate\Notifications\Messages\BroadcastMessage;

/**
 * Get the broadcastable representation of the notification.
 */
public function toBroadcast(object $notifiable): BroadcastMessage
{
    return new BroadcastMessage([
        'invoice_id' => $this->invoice->id,
        'amount' => $this->invoice->amount,
    ]);
}

```

#### [Broadcast Queue Configuration](https://laravel.com/docs/12.x/notifications#broadcast-queue-configuration)
All broadcast notifications are queued for broadcasting. If you would like to configure the queue connection or queue name that is used to queue the broadcast operation, you may use the `onConnection` and `onQueue` methods of the `BroadcastMessage`:
```


1return (new BroadcastMessage($data))




2    ->onConnection('sqs')




3    ->onQueue('broadcasts');




return (new BroadcastMessage($data))
    ->onConnection('sqs')
    ->onQueue('broadcasts');

```

#### [Customizing the Notification Type](https://laravel.com/docs/12.x/notifications#customizing-the-notification-type)
In addition to the data you specify, all broadcast notifications also have a `type` field containing the full class name of the notification. If you would like to customize the notification `type`, you may define a `broadcastType` method on the notification class:
```


1/**




2 * Get the type of the notification being broadcast.




3 */




4public function broadcastType(): string




5{




6    return 'broadcast.message';




7}




/**
 * Get the type of the notification being broadcast.
 */
public function broadcastType(): string
{
    return 'broadcast.message';
}

```

### [Listening for Notifications](https://laravel.com/docs/12.x/notifications#listening-for-notifications)
Notifications will broadcast on a private channel formatted using a `{notifiable}.{id}` convention. So, if you are sending a notification to an `App\Models\User` instance with an ID of `1`, the notification will be broadcast on the `App.Models.User.1` private channel. When using [Laravel Echo](https://laravel.com/docs/12.x/broadcasting#client-side-installation), you may easily listen for notifications on a channel using the `notification` method:
```


1Echo.private('App.Models.User.' + userId)




2    .notification((notification) => {




3        console.log(notification.type);




4    });




Echo.private('App.Models.User.' + userId)
    .notification((notification) => {
        console.log(notification.type);
    });

```

#### [Using React or Vue](https://laravel.com/docs/12.x/notifications#using-react-or-vue)
Laravel Echo includes React and Vue hooks that make it painless to listen for notifications. To get started, invoke the `useEchoNotification` hook, which is used to listen for notifications. The `useEchoNotification` hook will automatically leave channels when the consuming component is unmounted:
React Vue
```


1import { useEchoNotification } from "@laravel/echo-react";




2 



3useEchoNotification(




4    `App.Models.User.${userId}`,




5    (notification) => {




6        console.log(notification.type);




7    },




8);




import { useEchoNotification } from "@laravel/echo-react";

useEchoNotification(
    `App.Models.User.${userId}`,
    (notification) => {
        console.log(notification.type);
    },
);

```

```


 1<script setup lang="ts">




 2import { useEchoNotification } from "@laravel/echo-vue";




 3 



 4useEchoNotification(




 5    `App.Models.User.${userId}`,




 6    (notification) => {




 7        console.log(notification.type);




 8    },




 9);




10</script>




<script setup lang="ts">
import { useEchoNotification } from "@laravel/echo-vue";

useEchoNotification(
    `App.Models.User.${userId}`,
    (notification) => {
        console.log(notification.type);
    },
);
</script>

```

By default, the hook listens to all notifications. To specify the notification types you would like to listen to, you can provide either a string or array of types to `useEchoNotification`:
React Vue
```


1import { useEchoNotification } from "@laravel/echo-react";




2 



3useEchoNotification(




4    `App.Models.User.${userId}`,




5    (notification) => {




6        console.log(notification.type);




7    },




8    'App.Notifications.InvoicePaid',




9);




import { useEchoNotification } from "@laravel/echo-react";

useEchoNotification(
    `App.Models.User.${userId}`,
    (notification) => {
        console.log(notification.type);
    },
    'App.Notifications.InvoicePaid',
);

```

```


 1<script setup lang="ts">




 2import { useEchoNotification } from "@laravel/echo-vue";




 3 



 4useEchoNotification(




 5    `App.Models.User.${userId}`,




 6    (notification) => {




 7        console.log(notification.type);




 8    },




 9    'App.Notifications.InvoicePaid',




10);




11</script>




<script setup lang="ts">
import { useEchoNotification } from "@laravel/echo-vue";

useEchoNotification(
    `App.Models.User.${userId}`,
    (notification) => {
        console.log(notification.type);
    },
    'App.Notifications.InvoicePaid',
);
</script>

```

You may also specify the shape of the notification payload data, providing greater type safety and editing convenience:
```


 1type InvoicePaidNotification = {




 2    invoice_id: number;




 3    created_at: string;




 4};




 5 



 6useEchoNotification<InvoicePaidNotification>(




 7    `App.Models.User.${userId}`,




 8    (notification) => {




 9        console.log(notification.invoice_id);




10        console.log(notification.created_at);




11        console.log(notification.type);




12    },




13    'App.Notifications.InvoicePaid',




14);




type InvoicePaidNotification = {
    invoice_id: number;
    created_at: string;
};

useEchoNotification<InvoicePaidNotification>(
    `App.Models.User.${userId}`,
    (notification) => {
        console.log(notification.invoice_id);
        console.log(notification.created_at);
        console.log(notification.type);
    },
    'App.Notifications.InvoicePaid',
);

```

#### [Customizing the Notification Channel](https://laravel.com/docs/12.x/notifications#customizing-the-notification-channel)
If you would like to customize which channel that an entity's broadcast notifications are broadcast on, you may define a `receivesBroadcastNotificationsOn` method on the notifiable entity:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Broadcasting\PrivateChannel;




 6use Illuminate\Foundation\Auth\User as Authenticatable;




 7use Illuminate\Notifications\Notifiable;




 8 



 9class User extends Authenticatable




10{




11    use Notifiable;




12 



13    /**




14     * The channels the user receives notification broadcasts on.




15     */




16    public function receivesBroadcastNotificationsOn(): string




17    {




18        return 'users.'.$this->id;




19    }




20}




<?php

namespace App\Models;

use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use Notifiable;

    /**
     * The channels the user receives notification broadcasts on.
     */
    public function receivesBroadcastNotificationsOn(): string
    {
        return 'users.'.$this->id;
    }
}

```
