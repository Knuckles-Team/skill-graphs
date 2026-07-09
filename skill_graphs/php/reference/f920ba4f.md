## [Defining Listeners](https://laravel.com/docs/12.x/events#defining-listeners)
Next, let's take a look at the listener for our example event. Event listeners receive event instances in their `handle` method. The `make:listener` Artisan command, when invoked with the `--event` option, will automatically import the proper event class and type-hint the event in the `handle` method. Within the `handle` method, you may perform any actions necessary to respond to the event:
```


 1<?php




 2 



 3namespace App\Listeners;




 4 



 5use App\Events\OrderShipped;




 6 



 7class SendShipmentNotification




 8{




 9    /**




10     * Create the event listener.




11     */




12    public function __construct() {}




13 



14    /**




15     * Handle the event.




16     */




17    public function handle(OrderShipped $event): void




18    {




19        // Access the order using $event->order...




20    }




21}




<?php

namespace App\Listeners;

use App\Events\OrderShipped;

class SendShipmentNotification
{
    /**
     * Create the event listener.
     */
    public function __construct() {}

    /**
     * Handle the event.
     */
    public function handle(OrderShipped $event): void
    {
        // Access the order using $event->order...
    }
}

```

Your event listeners may also type-hint any dependencies they need on their constructors. All event listeners are resolved via the Laravel [service container](https://laravel.com/docs/12.x/container), so dependencies will be injected automatically.
#### [Stopping The Propagation Of An Event](https://laravel.com/docs/12.x/events#stopping-the-propagation-of-an-event)
Sometimes, you may wish to stop the propagation of an event to other listeners. You may do so by returning `false` from your listener's `handle` method.
