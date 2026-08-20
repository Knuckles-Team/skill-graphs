## [Dispatching Events](https://laravel.com/docs/12.x/events#dispatching-events)
To dispatch an event, you may call the static `dispatch` method on the event. This method is made available on the event by the `Illuminate\Foundation\Events\Dispatchable` trait. Any arguments passed to the `dispatch` method will be passed to the event's constructor:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Events\OrderShipped;




 6use App\Models\Order;




 7use Illuminate\Http\RedirectResponse;




 8use Illuminate\Http\Request;




 9 



10class OrderShipmentController extends Controller




11{




12    /**




13     * Ship the given order.




14     */




15    public function store(Request $request): RedirectResponse




16    {




17        $order = Order::findOrFail($request->order_id);




18 



19        // Order shipment logic...




20 



21        OrderShipped::dispatch($order);




22 



23        return redirect('/orders');




24    }




25}




<?php

namespace App\Http\Controllers;

use App\Events\OrderShipped;
use App\Models\Order;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class OrderShipmentController extends Controller
{
    /**
     * Ship the given order.
     */
    public function store(Request $request): RedirectResponse
    {
        $order = Order::findOrFail($request->order_id);

        // Order shipment logic...

        OrderShipped::dispatch($order);

        return redirect('/orders');
    }
}

```

If you would like to conditionally dispatch an event, you may use the `dispatchIf` and `dispatchUnless` methods:
```


1OrderShipped::dispatchIf($condition, $order);




2 



3OrderShipped::dispatchUnless($condition, $order);




OrderShipped::dispatchIf($condition, $order);

OrderShipped::dispatchUnless($condition, $order);

```

When testing, it can be helpful to assert that certain events were dispatched without actually triggering their listeners. Laravel's [built-in testing helpers](https://laravel.com/docs/12.x/events#testing) make it a cinch.
### [Dispatching Events After Database Transactions](https://laravel.com/docs/12.x/events#dispatching-events-after-database-transactions)
Sometimes, you may want to instruct Laravel to only dispatch an event after the active database transaction has committed. To do so, you may implement the `ShouldDispatchAfterCommit` interface on the event class.
This interface instructs Laravel to not dispatch the event until the current database transaction is committed. If the transaction fails, the event will be discarded. If no database transaction is in progress when the event is dispatched, the event will be dispatched immediately:
```


 1<?php




 2 



 3namespace App\Events;




 4 



 5use App\Models\Order;




 6use Illuminate\Broadcasting\InteractsWithSockets;




 7use Illuminate\Contracts\Events\ShouldDispatchAfterCommit;




 8use Illuminate\Foundation\Events\Dispatchable;




 9use Illuminate\Queue\SerializesModels;




10 



11class OrderShipped implements ShouldDispatchAfterCommit




12{




13    use Dispatchable, InteractsWithSockets, SerializesModels;




14 



15    /**




16     * Create a new event instance.




17     */




18    public function __construct(




19        public Order $order,




20    ) {}




21}




<?php

namespace App\Events;

use App\Models\Order;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Contracts\Events\ShouldDispatchAfterCommit;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class OrderShipped implements ShouldDispatchAfterCommit
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

### [Deferring Events](https://laravel.com/docs/12.x/events#deferring-events)
Deferred events allow you to delay the dispatching of model events and execution of event listeners until after a specific block of code has completed. This is particularly useful when you need to ensure that all related records are created before event listeners are triggered.
To defer events, provide a closure to the `Event::defer()` method:
```


1use App\Models\User;




2use Illuminate\Support\Facades\Event;




3 



4Event::defer(function () {




5    $user = User::create(['name' => 'Victoria Otwell']);




6 



7    $user->posts()->create(['title' => 'My first post!']);




8});




use App\Models\User;
use Illuminate\Support\Facades\Event;

Event::defer(function () {
    $user = User::create(['name' => 'Victoria Otwell']);

    $user->posts()->create(['title' => 'My first post!']);
});

```

All events triggered within the closure will be dispatched after the closure is executed. This ensures that event listeners have access to all related records that were created during the deferred execution. If an exception occurs within the closure, the deferred events will not be dispatched.
To defer only specific events, pass an array of events as the second argument to the `defer` method:
```


1use App\Models\User;




2use Illuminate\Support\Facades\Event;




3 



4Event::defer(function () {




5    $user = User::create(['name' => 'Victoria Otwell']);




6 



7    $user->posts()->create(['title' => 'My first post!']);




8}, ['eloquent.created: '.User::class]);




use App\Models\User;
use Illuminate\Support\Facades\Event;

Event::defer(function () {
    $user = User::create(['name' => 'Victoria Otwell']);

    $user->posts()->create(['title' => 'My first post!']);
}, ['eloquent.created: '.User::class]);

```
