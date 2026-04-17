## [Broadcasting Events](https://laravel.com/docs/12.x/broadcasting#broadcasting-events)
Once you have defined an event and marked it with the `ShouldBroadcast` interface, you only need to fire the event using the event's dispatch method. The event dispatcher will notice that the event is marked with the `ShouldBroadcast` interface and will queue the event for broadcasting:
```


1use App\Events\OrderShipmentStatusUpdated;




2 



3OrderShipmentStatusUpdated::dispatch($order);




use App\Events\OrderShipmentStatusUpdated;

OrderShipmentStatusUpdated::dispatch($order);

```

### [Only to Others](https://laravel.com/docs/12.x/broadcasting#only-to-others)
When building an application that utilizes event broadcasting, you may occasionally need to broadcast an event to all subscribers to a given channel except for the current user. You may accomplish this using the `broadcast` helper and the `toOthers` method:
```


1use App\Events\OrderShipmentStatusUpdated;




2 



3broadcast(new OrderShipmentStatusUpdated($update))->toOthers();




use App\Events\OrderShipmentStatusUpdated;

broadcast(new OrderShipmentStatusUpdated($update))->toOthers();

```

To better understand when you may want to use the `toOthers` method, let's imagine a task list application where a user may create a new task by entering a task name. To create a task, your application might make a request to a `/task` URL which broadcasts the task's creation and returns a JSON representation of the new task. When your JavaScript application receives the response from the end-point, it might directly insert the new task into its task list like so:
```


1axios.post('/task', task)




2    .then((response) => {




3        this.tasks.push(response.data);




4    });




axios.post('/task', task)
    .then((response) => {
        this.tasks.push(response.data);
    });

```

However, remember that we also broadcast the task's creation. If your JavaScript application is also listening for this event in order to add tasks to the task list, you will have duplicate tasks in your list: one from the end-point and one from the broadcast. You may solve this by using the `toOthers` method to instruct the broadcaster to not broadcast the event to the current user.
Your event must use the `Illuminate\Broadcasting\InteractsWithSockets` trait in order to call the `toOthers` method.
#### [Configuration](https://laravel.com/docs/12.x/broadcasting#only-to-others-configuration)
When you initialize a Laravel Echo instance, a socket ID is assigned to the connection. If you are using a global `X-Socket-ID` header. Then, when you call the `toOthers` method, Laravel will extract the socket ID from the header and instruct the broadcaster to not broadcast to any connections with that socket ID.
If you are not using a global Axios instance, you will need to manually configure your JavaScript application to send the `X-Socket-ID` header with all outgoing requests. You may retrieve the socket ID using the `Echo.socketId` method:
```


1var socketId = Echo.socketId();




var socketId = Echo.socketId();

```

### [Customizing the Connection](https://laravel.com/docs/12.x/broadcasting#customizing-the-connection)
If your application interacts with multiple broadcast connections and you want to broadcast an event using a broadcaster other than your default, you may specify which connection to push an event to using the `via` method:
```


1use App\Events\OrderShipmentStatusUpdated;




2 



3broadcast(new OrderShipmentStatusUpdated($update))->via('pusher');




use App\Events\OrderShipmentStatusUpdated;

broadcast(new OrderShipmentStatusUpdated($update))->via('pusher');

```

Alternatively, you may specify the event's broadcast connection by calling the `broadcastVia` method within the event's constructor. However, before doing so, you should ensure that the event class uses the `InteractsWithBroadcasting` trait:
```


 1<?php




 2 



 3namespace App\Events;




 4 



 5use Illuminate\Broadcasting\Channel;




 6use Illuminate\Broadcasting\InteractsWithBroadcasting;




 7use Illuminate\Broadcasting\InteractsWithSockets;




 8use Illuminate\Broadcasting\PresenceChannel;




 9use Illuminate\Broadcasting\PrivateChannel;




10use Illuminate\Contracts\Broadcasting\ShouldBroadcast;




11use Illuminate\Queue\SerializesModels;




12 



13class OrderShipmentStatusUpdated implements ShouldBroadcast




14{




15    use InteractsWithBroadcasting;




16 



17    /**




18     * Create a new event instance.




19     */




20    public function __construct()




21    {




22        $this->broadcastVia('pusher');




23    }




24}




<?php

namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithBroadcasting;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Queue\SerializesModels;

class OrderShipmentStatusUpdated implements ShouldBroadcast
{
    use InteractsWithBroadcasting;

    /**
     * Create a new event instance.
     */
    public function __construct()
    {
        $this->broadcastVia('pusher');
    }
}

```

### [Anonymous Events](https://laravel.com/docs/12.x/broadcasting#anonymous-events)
Sometimes, you may want to broadcast a simple event to your application's frontend without creating a dedicated event class. To accommodate this, the `Broadcast` facade allows you to broadcast "anonymous events":
```


1Broadcast::on('orders.'.$order->id)->send();




Broadcast::on('orders.'.$order->id)->send();

```

The example above will broadcast the following event:
```


1{




2    "event": "AnonymousEvent",




3    "data": "[]",




4    "channel": "orders.1"




5}




{
    "event": "AnonymousEvent",
    "data": "[]",
    "channel": "orders.1"
}

```

Using the `as` and `with` methods, you may customize the event's name and data:
```


1Broadcast::on('orders.'.$order->id)




2    ->as('OrderPlaced')




3    ->with($order)




4    ->send();




Broadcast::on('orders.'.$order->id)
    ->as('OrderPlaced')
    ->with($order)
    ->send();

```

The example above will broadcast an event like the following:
```


1{




2    "event": "OrderPlaced",




3    "data": "{ id: 1, total: 100 }",




4    "channel": "orders.1"




5}




{
    "event": "OrderPlaced",
    "data": "{ id: 1, total: 100 }",
    "channel": "orders.1"
}

```

If you would like to broadcast the anonymous event on a private or presence channel, you may utilize the `private` and `presence` methods:
```


1Broadcast::private('orders.'.$order->id)->send();




2Broadcast::presence('channels.'.$channel->id)->send();




Broadcast::private('orders.'.$order->id)->send();
Broadcast::presence('channels.'.$channel->id)->send();

```

Broadcasting an anonymous event using the `send` method dispatches the event to your application's [queue](https://laravel.com/docs/12.x/queues) for processing. However, if you would like to broadcast the event immediately, you may use the `sendNow` method:
```


1Broadcast::on('orders.'.$order->id)->sendNow();




Broadcast::on('orders.'.$order->id)->sendNow();

```

To broadcast the event to all channel subscribers except the currently authenticated user, you can invoke the `toOthers` method:
```


1Broadcast::on('orders.'.$order->id)




2    ->toOthers()




3    ->send();




Broadcast::on('orders.'.$order->id)
    ->toOthers()
    ->send();

```

### [Rescuing Broadcasts](https://laravel.com/docs/12.x/broadcasting#rescuing-broadcasts)
When your application's queue server is unavailable or Laravel encounters an error while broadcasting an event, an exception is thrown that typically causes the end user to see an application error. Since event broadcasting is often supplementary to your application's core functionality, you can prevent these exceptions from disrupting the user experience by implementing the `ShouldRescue` interface on your events.
Events that implement the `ShouldRescue` interface automatically utilize Laravel's [rescue helper function](https://laravel.com/docs/12.x/helpers#method-rescue) during broadcast attempts. This helper catches any exceptions, reports them to your application's exception handler for logging, and allows the application to continue executing normally without interrupting the user's workflow:
```


 1<?php




 2 



 3namespace App\Events;




 4 



 5use Illuminate\Contracts\Broadcasting\ShouldBroadcast;




 6use Illuminate\Contracts\Broadcasting\ShouldRescue;




 7 



 8class ServerCreated implements ShouldBroadcast, ShouldRescue




 9{




10    // ...




11}




<?php

namespace App\Events;

use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Contracts\Broadcasting\ShouldRescue;

class ServerCreated implements ShouldBroadcast, ShouldRescue
{
    // ...
}

```
