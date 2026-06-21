## [Authorizing Channels](https://laravel.com/docs/12.x/broadcasting#authorizing-channels)
Private channels require you to authorize that the currently authenticated user can actually listen on the channel. This is accomplished by making an HTTP request to your Laravel application with the channel name and allowing your application to determine if the user can listen on that channel. When using [Laravel Echo](https://laravel.com/docs/12.x/broadcasting#client-side-installation), the HTTP request to authorize subscriptions to private channels will be made automatically.
When broadcasting is installed Laravel attempts to automatically register the `/broadcasting/auth` route to handle authorization requests. If Laravel fails to automatically register these routes, you may register them manually in your application's `/bootstrap/app.php` file:
```


1->withRouting(




2    web: __DIR__.'/../routes/web.php',




3    channels: __DIR__.'/../routes/channels.php',




4    health: '/up',




5)




->withRouting(
    web: __DIR__.'/../routes/web.php',
    channels: __DIR__.'/../routes/channels.php',
    health: '/up',
)

```

### [Defining Authorization Callbacks](https://laravel.com/docs/12.x/broadcasting#defining-authorization-callbacks)
Next, we need to define the logic that will actually determine if the currently authenticated user can listen to a given channel. This is done in the `routes/channels.php` file that was created by the `install:broadcasting` Artisan command. In this file, you may use the `Broadcast::channel` method to register channel authorization callbacks:
```


1use App\Models\User;




2 



3Broadcast::channel('orders.{orderId}', function (User $user, int $orderId) {




4    return $user->id === Order::findOrNew($orderId)->user_id;




5});




use App\Models\User;

Broadcast::channel('orders.{orderId}', function (User $user, int $orderId) {
    return $user->id === Order::findOrNew($orderId)->user_id;
});

```

The `channel` method accepts two arguments: the name of the channel and a callback which returns `true` or `false` indicating whether the user is authorized to listen on the channel.
All authorization callbacks receive the currently authenticated user as their first argument and any additional wildcard parameters as their subsequent arguments. In this example, we are using the `{orderId}` placeholder to indicate that the "ID" portion of the channel name is a wildcard.
You may view a list of your application's broadcast authorization callbacks using the `channel:list` Artisan command:
```


1php artisan channel:list




php artisan channel:list

```

#### [Authorization Callback Model Binding](https://laravel.com/docs/12.x/broadcasting#authorization-callback-model-binding)
Just like HTTP routes, channel routes may also take advantage of implicit and explicit [route model binding](https://laravel.com/docs/12.x/routing#route-model-binding). For example, instead of receiving a string or numeric order ID, you may request an actual `Order` model instance:
```


1use App\Models\Order;




2use App\Models\User;




3 



4Broadcast::channel('orders.{order}', function (User $user, Order $order) {




5    return $user->id === $order->user_id;




6});




use App\Models\Order;
use App\Models\User;

Broadcast::channel('orders.{order}', function (User $user, Order $order) {
    return $user->id === $order->user_id;
});

```

Unlike HTTP route model binding, channel model binding does not support automatic [implicit model binding scoping](https://laravel.com/docs/12.x/routing#implicit-model-binding-scoping). However, this is rarely a problem because most channels can be scoped based on a single model's unique, primary key.
#### [Authorization Callback Authentication](https://laravel.com/docs/12.x/broadcasting#authorization-callback-authentication)
Private and presence broadcast channels authenticate the current user via your application's default authentication guard. If the user is not authenticated, channel authorization is automatically denied and the authorization callback is never executed. However, you may assign multiple, custom guards that should authenticate the incoming request if necessary:
```


1Broadcast::channel('channel', function () {




2    // ...




3}, ['guards' => ['web', 'admin']]);




Broadcast::channel('channel', function () {
    // ...
}, ['guards' => ['web', 'admin']]);

```

### [Defining Channel Classes](https://laravel.com/docs/12.x/broadcasting#defining-channel-classes)
If your application is consuming many different channels, your `routes/channels.php` file could become bulky. So, instead of using closures to authorize channels, you may use channel classes. To generate a channel class, use the `make:channel` Artisan command. This command will place a new channel class in the `App/Broadcasting` directory.
```


1php artisan make:channel OrderChannel




php artisan make:channel OrderChannel

```

Next, register your channel in your `routes/channels.php` file:
```


1use App\Broadcasting\OrderChannel;




2 



3Broadcast::channel('orders.{order}', OrderChannel::class);




use App\Broadcasting\OrderChannel;

Broadcast::channel('orders.{order}', OrderChannel::class);

```

Finally, you may place the authorization logic for your channel in the channel class' `join` method. This `join` method will house the same logic you would have typically placed in your channel authorization closure. You may also take advantage of channel model binding:
```


 1<?php




 2 



 3namespace App\Broadcasting;




 4 



 5use App\Models\Order;




 6use App\Models\User;




 7 



 8class OrderChannel




 9{




10    /**




11     * Create a new channel instance.




12     */




13    public function __construct() {}




14 



15    /**




16     * Authenticate the user's access to the channel.




17     */




18    public function join(User $user, Order $order): array|bool




19    {




20        return $user->id === $order->user_id;




21    }




22}




<?php

namespace App\Broadcasting;

use App\Models\Order;
use App\Models\User;

class OrderChannel
{
    /**
     * Create a new channel instance.
     */
    public function __construct() {}

    /**
     * Authenticate the user's access to the channel.
     */
    public function join(User $user, Order $order): array|bool
    {
        return $user->id === $order->user_id;
    }
}

```

Like many other classes in Laravel, channel classes will automatically be resolved by the [service container](https://laravel.com/docs/12.x/container). So, you may type-hint any dependencies required by your channel in its constructor.
