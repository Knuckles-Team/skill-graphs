## [Concept Overview](https://laravel.com/docs/12.x/broadcasting#concept-overview)
Laravel's event broadcasting allows you to broadcast your server-side Laravel events to your client-side JavaScript application using a driver-based approach to WebSockets. Currently, Laravel ships with [Laravel Reverb](https://reverb.laravel.com), [Laravel Echo](https://laravel.com/docs/12.x/broadcasting#client-side-installation) JavaScript package.
Events are broadcast over "channels", which may be specified as public or private. Any visitor to your application may subscribe to a public channel without any authentication or authorization; however, in order to subscribe to a private channel, a user must be authenticated and authorized to listen on that channel.
### [Using an Example Application](https://laravel.com/docs/12.x/broadcasting#using-example-application)
Before diving into each component of event broadcasting, let's take a high level overview using an e-commerce store as an example.
In our application, let's assume we have a page that allows users to view the shipping status for their orders. Let's also assume that an `OrderShipmentStatusUpdated` event is fired when a shipping status update is processed by the application:
```


1use App\Events\OrderShipmentStatusUpdated;




2 



3OrderShipmentStatusUpdated::dispatch($order);




use App\Events\OrderShipmentStatusUpdated;

OrderShipmentStatusUpdated::dispatch($order);

```

#### [The `ShouldBroadcast` Interface](https://laravel.com/docs/12.x/broadcasting#the-shouldbroadcast-interface)
When a user is viewing one of their orders, we don't want them to have to refresh the page to view status updates. Instead, we want to broadcast the updates to the application as they are created. So, we need to mark the `OrderShipmentStatusUpdated` event with the `ShouldBroadcast` interface. This will instruct Laravel to broadcast the event when it is fired:
```


 1<?php




 2 



 3namespace App\Events;




 4 



 5use App\Models\Order;




 6use Illuminate\Broadcasting\Channel;




 7use Illuminate\Broadcasting\InteractsWithSockets;




 8use Illuminate\Broadcasting\PresenceChannel;




 9use Illuminate\Contracts\Broadcasting\ShouldBroadcast;




10use Illuminate\Queue\SerializesModels;




11 



12class OrderShipmentStatusUpdated implements ShouldBroadcast




13{




14    /**




15     * The order instance.




16     *




17     * @var \App\Models\Order




18     */




19    public $order;




20}




<?php

namespace App\Events;

use App\Models\Order;
use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Queue\SerializesModels;

class OrderShipmentStatusUpdated implements ShouldBroadcast
{
    /**
     * The order instance.
     *
     * @var \App\Models\Order
     */
    public $order;
}

```

The `ShouldBroadcast` interface requires our event to define a `broadcastOn` method. This method is responsible for returning the channels that the event should broadcast on. An empty stub of this method is already defined on generated event classes, so we only need to fill in its details. We only want the creator of the order to be able to view status updates, so we will broadcast the event on a private channel that is tied to the order:
```


 1use Illuminate\Broadcasting\Channel;




 2use Illuminate\Broadcasting\PrivateChannel;




 3 



 4/**




 5 * Get the channel the event should broadcast on.




 6 */




 7public function broadcastOn(): Channel




 8{




 9    return new PrivateChannel('orders.'.$this->order->id);




10}




use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\PrivateChannel;

/**
 * Get the channel the event should broadcast on.
 */
public function broadcastOn(): Channel
{
    return new PrivateChannel('orders.'.$this->order->id);
}

```

If you wish the event to broadcast on multiple channels, you may return an `array` instead:
```


 1use Illuminate\Broadcasting\PrivateChannel;




 2 



 3/**




 4 * Get the channels the event should broadcast on.




 5 *




 6 * @return array<int, \Illuminate\Broadcasting\Channel>




 7 */




 8public function broadcastOn(): array




 9{




10    return [




11        new PrivateChannel('orders.'.$this->order->id),




12        // ...




13    ];




14}




use Illuminate\Broadcasting\PrivateChannel;

/**
 * Get the channels the event should broadcast on.
 *
 * @return array<int, \Illuminate\Broadcasting\Channel>
 */
public function broadcastOn(): array
{
    return [
        new PrivateChannel('orders.'.$this->order->id),
        // ...
    ];
}

```

#### [Authorizing Channels](https://laravel.com/docs/12.x/broadcasting#example-application-authorizing-channels)
Remember, users must be authorized to listen on private channels. We may define our channel authorization rules in our application's `routes/channels.php` file. In this example, we need to verify that any user attempting to listen on the private `orders.1` channel is actually the creator of the order:
```


1use App\Models\Order;




2use App\Models\User;




3 



4Broadcast::channel('orders.{orderId}', function (User $user, int $orderId) {




5    return $user->id === Order::findOrNew($orderId)->user_id;




6});




use App\Models\Order;
use App\Models\User;

Broadcast::channel('orders.{orderId}', function (User $user, int $orderId) {
    return $user->id === Order::findOrNew($orderId)->user_id;
});

```

The `channel` method accepts two arguments: the name of the channel and a callback which returns `true` or `false` indicating whether the user is authorized to listen on the channel.
All authorization callbacks receive the currently authenticated user as their first argument and any additional wildcard parameters as their subsequent arguments. In this example, we are using the `{orderId}` placeholder to indicate that the "ID" portion of the channel name is a wildcard.
#### [Listening for Event Broadcasts](https://laravel.com/docs/12.x/broadcasting#listening-for-event-broadcasts)
Next, all that remains is to listen for the event in our JavaScript application. We can do this using [Laravel Echo](https://laravel.com/docs/12.x/broadcasting#client-side-installation). Laravel Echo's built-in React and Vue hooks make it simple to get started, and, by default, all of the event's public properties will be included on the broadcast event:
React Vue
```


1import { useEcho } from "@laravel/echo-react";




2 



3useEcho(




4    `orders.${orderId}`,




5    "OrderShipmentStatusUpdated",




6    (e) => {




7        console.log(e.order);




8    },




9);




import { useEcho } from "@laravel/echo-react";

useEcho(
    `orders.${orderId}`,
    "OrderShipmentStatusUpdated",
    (e) => {
        console.log(e.order);
    },
);

```

```


 1<script setup lang="ts">




 2import { useEcho } from "@laravel/echo-vue";




 3 



 4useEcho(




 5    `orders.${orderId}`,




 6    "OrderShipmentStatusUpdated",




 7    (e) => {




 8        console.log(e.order);




 9    },




10);




11</script>




<script setup lang="ts">
import { useEcho } from "@laravel/echo-vue";

useEcho(
    `orders.${orderId}`,
    "OrderShipmentStatusUpdated",
    (e) => {
        console.log(e.order);
    },
);
</script>

```
