## [Defining Events](https://laravel.com/docs/12.x/events#defining-events)
An event class is essentially a data container which holds the information related to the event. For example, let's assume an `App\Events\OrderShipped` event receives an [Eloquent ORM](https://laravel.com/docs/12.x/eloquent) object:
```


 1<?php




 2 



 3namespace App\Events;




 4 



 5use App\Models\Order;




 6use Illuminate\Broadcasting\InteractsWithSockets;




 7use Illuminate\Foundation\Events\Dispatchable;




 8use Illuminate\Queue\SerializesModels;




 9 



10class OrderShipped




11{




12    use Dispatchable, InteractsWithSockets, SerializesModels;




13 



14    /**




15     * Create a new event instance.




16     */




17    public function __construct(




18        public Order $order,




19    ) {}




20}




<?php

namespace App\Events;

use App\Models\Order;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class OrderShipped
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    /**
     * Create a new event instance.
     */
    public function __construct(
        public Order $order,
    ) {}
}

```

As you can see, this event class contains no logic. It is a container for the `App\Models\Order` instance that was purchased. The `SerializesModels` trait used by the event will gracefully serialize any Eloquent models if the event object is serialized using PHP's `serialize` function, such as when utilizing [queued listeners](https://laravel.com/docs/12.x/events#queued-event-listeners).
