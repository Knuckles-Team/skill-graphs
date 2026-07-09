## [Checkout Sessions](https://laravel.com/docs/12.x/cashier-paddle#checkout-sessions)
Most operations to bill customers are performed using "checkouts" via Paddle's
Before processing checkout payments using Paddle, you should define your application's
### [Overlay Checkout](https://laravel.com/docs/12.x/cashier-paddle#overlay-checkout)
Before displaying the Checkout Overlay widget, you must generate a checkout session using Cashier. A checkout session will inform the checkout widget of the billing operation that should be performed:
```


1use Illuminate\Http\Request;




2 



3Route::get('/buy', function (Request $request) {




4    $checkout = $user->checkout('pri_34567')




5        ->returnTo(route('dashboard'));




6 



7    return view('billing', ['checkout' => $checkout]);




8});




use Illuminate\Http\Request;

Route::get('/buy', function (Request $request) {
    $checkout = $user->checkout('pri_34567')
        ->returnTo(route('dashboard'));

    return view('billing', ['checkout' => $checkout]);
});

```

Cashier includes a `paddle-button` [Blade component](https://laravel.com/docs/12.x/blade#components). You may pass the checkout session to this component as a "prop". Then, when this button is clicked, Paddle's checkout widget will be displayed:
```


1<x-paddle-button :checkout="$checkout" class="px-8 py-4">




2    Subscribe




3</x-paddle-button>




<x-paddle-button :checkout="$checkout" class="px-8 py-4">
    Subscribe
</x-paddle-button>

```

By default, this will display the widget using Paddle's default styling. You can customize the widget by adding `data-theme='light'` attribute to the component:
```


1<x-paddle-button :checkout="$checkout" class="px-8 py-4" data-theme="light">




2    Subscribe




3</x-paddle-button>




<x-paddle-button :checkout="$checkout" class="px-8 py-4" data-theme="light">
    Subscribe
</x-paddle-button>

```

The Paddle checkout widget is asynchronous. Once the user creates a subscription within the widget, Paddle will send your application a webhook so that you may properly update the subscription state in your application's database. Therefore, it's important that you properly [set up webhooks](https://laravel.com/docs/12.x/cashier-paddle#handling-paddle-webhooks) to accommodate for state changes from Paddle.
After a subscription state change, the delay for receiving the corresponding webhook is typically minimal but you should account for this in your application by considering that your user's subscription might not be immediately available after completing the checkout.
#### [Manually Rendering an Overlay Checkout](https://laravel.com/docs/12.x/cashier-paddle#manually-rendering-an-overlay-checkout)
You may also manually render an overlay checkout without using Laravel's built-in Blade components. To get started, generate the checkout session [as demonstrated in previous examples](https://laravel.com/docs/12.x/cashier-paddle#overlay-checkout):
```


1use Illuminate\Http\Request;




2 



3Route::get('/buy', function (Request $request) {




4    $checkout = $user->checkout('pri_34567')




5        ->returnTo(route('dashboard'));




6 



7    return view('billing', ['checkout' => $checkout]);




8});




use Illuminate\Http\Request;

Route::get('/buy', function (Request $request) {
    $checkout = $user->checkout('pri_34567')
        ->returnTo(route('dashboard'));

    return view('billing', ['checkout' => $checkout]);
});

```

Next, you may use Paddle.js to initialize the checkout. In this example, we will create a link that is assigned the `paddle_button` class. Paddle.js will detect this class and display the overlay checkout when the link is clicked:
```


 1<?php




 2$items = $checkout->getItems();




 3$customer = $checkout->getCustomer();




 4$custom = $checkout->getCustomData();




 5?>




 6 



 7<a




 8    href='#!'




 9    class='paddle_button'




10    data-items='{!! json_encode($items) !!}'




11    @if ($customer) data-customer-id='{{ $customer->paddle_id }}' @endif




12    @if ($custom) data-custom-data='{{ json_encode($custom) }}' @endif




13    @if ($returnUrl = $checkout->getReturnUrl()) data-success-url='{{ $returnUrl }}' @endif




14>




15    Buy Product




16</a>




<?php
$items = $checkout->getItems();
$customer = $checkout->getCustomer();
$custom = $checkout->getCustomData();
?>

<a
    href='#!'
    class='paddle_button'
    data-items='{!! json_encode($items) !!}'
    @if ($customer) data-customer-id='{{ $customer->paddle_id }}' @endif
    @if ($custom) data-custom-data='{{ json_encode($custom) }}' @endif
    @if ($returnUrl = $checkout->getReturnUrl()) data-success-url='{{ $returnUrl }}' @endif
>
    Buy Product
</a>

```

### [Inline Checkout](https://laravel.com/docs/12.x/cashier-paddle#inline-checkout)
If you don't want to make use of Paddle's "overlay" style checkout widget, Paddle also provides the option to display the widget inline. While this approach does not allow you to adjust any of the checkout's HTML fields, it allows you to embed the widget within your application.
To make it easy for you to get started with inline checkout, Cashier includes a `paddle-checkout` Blade component. To get started, you should [generate a checkout session](https://laravel.com/docs/12.x/cashier-paddle#overlay-checkout):
```


1use Illuminate\Http\Request;




2 



3Route::get('/buy', function (Request $request) {




4    $checkout = $user->checkout('pri_34567')




5        ->returnTo(route('dashboard'));




6 



7    return view('billing', ['checkout' => $checkout]);




8});




use Illuminate\Http\Request;

Route::get('/buy', function (Request $request) {
    $checkout = $user->checkout('pri_34567')
        ->returnTo(route('dashboard'));

    return view('billing', ['checkout' => $checkout]);
});

```

Then, you may pass the checkout session to the component's `checkout` attribute:
```


1<x-paddle-checkout :checkout="$checkout" class="w-full" />




<x-paddle-checkout :checkout="$checkout" class="w-full" />

```

To adjust the height of the inline checkout component, you may pass the `height` attribute to the Blade component:
```


1<x-paddle-checkout :checkout="$checkout" class="w-full" height="500" />




<x-paddle-checkout :checkout="$checkout" class="w-full" height="500" />

```

Please consult Paddle's
#### [Manually Rendering an Inline Checkout](https://laravel.com/docs/12.x/cashier-paddle#manually-rendering-an-inline-checkout)
You may also manually render an inline checkout without using Laravel's built-in Blade components. To get started, generate the checkout session [as demonstrated in previous examples](https://laravel.com/docs/12.x/cashier-paddle#inline-checkout):
```


1use Illuminate\Http\Request;




2 



3Route::get('/buy', function (Request $request) {




4    $checkout = $user->checkout('pri_34567')




5        ->returnTo(route('dashboard'));




6 



7    return view('billing', ['checkout' => $checkout]);




8});




use Illuminate\Http\Request;

Route::get('/buy', function (Request $request) {
    $checkout = $user->checkout('pri_34567')
        ->returnTo(route('dashboard'));

    return view('billing', ['checkout' => $checkout]);
});

```

Next, you may use Paddle.js to initialize the checkout. In this example, we will demonstrate this using
```


 1<?php




 2$options = $checkout->options();




 3 



 4$options['settings']['frameTarget'] = 'paddle-checkout';




 5$options['settings']['frameInitialHeight'] = 366;




 6?>




 7 



 8<div class="paddle-checkout" x-data="{}" x-init="




 9    Paddle.Checkout.open(@json($options));




10">




11</div>




<?php
$options = $checkout->options();

$options['settings']['frameTarget'] = 'paddle-checkout';
$options['settings']['frameInitialHeight'] = 366;
?>

<div class="paddle-checkout" x-data="{}" x-init="
    Paddle.Checkout.open(@json($options));
">
</div>

```

### [Guest Checkouts](https://laravel.com/docs/12.x/cashier-paddle#guest-checkouts)
Sometimes, you may need to create a checkout session for users that do not need an account with your application. To do so, you may use the `guest` method:
```


1use Illuminate\Http\Request;




2use Laravel\Paddle\Checkout;




3 



4Route::get('/buy', function (Request $request) {




5    $checkout = Checkout::guest(['pri_34567'])




6        ->returnTo(route('home'));




7 



8    return view('billing', ['checkout' => $checkout]);




9});




use Illuminate\Http\Request;
use Laravel\Paddle\Checkout;

Route::get('/buy', function (Request $request) {
    $checkout = Checkout::guest(['pri_34567'])
        ->returnTo(route('home'));

    return view('billing', ['checkout' => $checkout]);
});

```

Then, you may provide the checkout session to the [Paddle button](https://laravel.com/docs/12.x/cashier-paddle#overlay-checkout) or [inline checkout](https://laravel.com/docs/12.x/cashier-paddle#inline-checkout) Blade components.
