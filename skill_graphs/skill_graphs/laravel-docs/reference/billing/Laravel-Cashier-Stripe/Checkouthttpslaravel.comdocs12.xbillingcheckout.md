## [Checkout](https://laravel.com/docs/12.x/billing#checkout)
Cashier Stripe also provides support for
The following documentation contains information on how to get started using Stripe Checkout with Cashier. To learn more about Stripe Checkout, you should also consider reviewing
### [Product Checkouts](https://laravel.com/docs/12.x/billing#product-checkouts)
You may perform a checkout for an existing product that has been created within your Stripe dashboard using the `checkout` method on a billable model. The `checkout` method will initiate a new Stripe Checkout session. By default, you're required to pass a Stripe Price ID:
```


1use Illuminate\Http\Request;




2 



3Route::get('/product-checkout', function (Request $request) {




4    return $request->user()->checkout('price_tshirt');




5});




use Illuminate\Http\Request;

Route::get('/product-checkout', function (Request $request) {
    return $request->user()->checkout('price_tshirt');
});

```

If needed, you may also specify a product quantity:
```


1use Illuminate\Http\Request;




2 



3Route::get('/product-checkout', function (Request $request) {




4    return $request->user()->checkout(['price_tshirt' => 15]);




5});




use Illuminate\Http\Request;

Route::get('/product-checkout', function (Request $request) {
    return $request->user()->checkout(['price_tshirt' => 15]);
});

```

When a customer visits this route they will be redirected to Stripe's Checkout page. By default, when a user successfully completes or cancels a purchase they will be redirected to your `home` route location, but you may specify custom callback URLs using the `success_url` and `cancel_url` options:
```


1use Illuminate\Http\Request;




2 



3Route::get('/product-checkout', function (Request $request) {




4    return $request->user()->checkout(['price_tshirt' => 1], [




5        'success_url' => route('your-success-route'),




6        'cancel_url' => route('your-cancel-route'),




7    ]);




8});




use Illuminate\Http\Request;

Route::get('/product-checkout', function (Request $request) {
    return $request->user()->checkout(['price_tshirt' => 1], [
        'success_url' => route('your-success-route'),
        'cancel_url' => route('your-cancel-route'),
    ]);
});

```

When defining your `success_url` checkout option, you may instruct Stripe to add the checkout session ID as a query string parameter when invoking your URL. To do so, add the literal string `{CHECKOUT_SESSION_ID}` to your `success_url` query string. Stripe will replace this placeholder with the actual checkout session ID:
```


 1use Illuminate\Http\Request;




 2use Stripe\Checkout\Session;




 3use Stripe\Customer;




 4 



 5Route::get('/product-checkout', function (Request $request) {




 6    return $request->user()->checkout(['price_tshirt' => 1], [




 7        'success_url' => route('checkout-success').'?session_id={CHECKOUT_SESSION_ID}',




 8        'cancel_url' => route('checkout-cancel'),




 9    ]);




10});




11 



12Route::get('/checkout-success', function (Request $request) {




13    $checkoutSession = $request->user()->stripe()->checkout->sessions->retrieve($request->get('session_id'));




14 



15    return view('checkout.success', ['checkoutSession' => $checkoutSession]);




16})->name('checkout-success');




use Illuminate\Http\Request;
use Stripe\Checkout\Session;
use Stripe\Customer;

Route::get('/product-checkout', function (Request $request) {
    return $request->user()->checkout(['price_tshirt' => 1], [
        'success_url' => route('checkout-success').'?session_id={CHECKOUT_SESSION_ID}',
        'cancel_url' => route('checkout-cancel'),
    ]);
});

Route::get('/checkout-success', function (Request $request) {
    $checkoutSession = $request->user()->stripe()->checkout->sessions->retrieve($request->get('session_id'));

    return view('checkout.success', ['checkoutSession' => $checkoutSession]);
})->name('checkout-success');

```

#### [Promotion Codes](https://laravel.com/docs/12.x/billing#checkout-promotion-codes)
By default, Stripe Checkout does not allow `allowPromotionCodes` method:
```


1use Illuminate\Http\Request;




2 



3Route::get('/product-checkout', function (Request $request) {




4    return $request->user()




5        ->allowPromotionCodes()




6        ->checkout('price_tshirt');




7});




use Illuminate\Http\Request;

Route::get('/product-checkout', function (Request $request) {
    return $request->user()
        ->allowPromotionCodes()
        ->checkout('price_tshirt');
});

```

### [Single Charge Checkouts](https://laravel.com/docs/12.x/billing#single-charge-checkouts)
You can also perform a simple charge for an ad-hoc product that has not been created in your Stripe dashboard. To do so you may use the `checkoutCharge` method on a billable model and pass it a chargeable amount, a product name, and an optional quantity. When a customer visits this route they will be redirected to Stripe's Checkout page:
```


1use Illuminate\Http\Request;




2 



3Route::get('/charge-checkout', function (Request $request) {




4    return $request->user()->checkoutCharge(1200, 'T-Shirt', 5);




5});




use Illuminate\Http\Request;

Route::get('/charge-checkout', function (Request $request) {
    return $request->user()->checkoutCharge(1200, 'T-Shirt', 5);
});

```

When using the `checkoutCharge` method, Stripe will always create a new product and price in your Stripe dashboard. Therefore, we recommend that you create the products up front in your Stripe dashboard and use the `checkout` method instead.
### [Subscription Checkouts](https://laravel.com/docs/12.x/billing#subscription-checkouts)
Using Stripe Checkout for subscriptions requires you to enable the `customer.subscription.created` webhook in your Stripe dashboard. This webhook will create the subscription record in your database and store all of the relevant subscription items.
You may also use Stripe Checkout to initiate subscriptions. After defining your subscription with Cashier's subscription builder methods, you may call the `checkout `method. When a customer visits this route they will be redirected to Stripe's Checkout page:
```


1use Illuminate\Http\Request;




2 



3Route::get('/subscription-checkout', function (Request $request) {




4    return $request->user()




5        ->newSubscription('default', 'price_monthly')




6        ->checkout();




7});




use Illuminate\Http\Request;

Route::get('/subscription-checkout', function (Request $request) {
    return $request->user()
        ->newSubscription('default', 'price_monthly')
        ->checkout();
});

```

Just as with product checkouts, you may customize the success and cancellation URLs:
```


 1use Illuminate\Http\Request;




 2 



 3Route::get('/subscription-checkout', function (Request $request) {




 4    return $request->user()




 5        ->newSubscription('default', 'price_monthly')




 6        ->checkout([




 7            'success_url' => route('your-success-route'),




 8            'cancel_url' => route('your-cancel-route'),




 9        ]);




10});




use Illuminate\Http\Request;

Route::get('/subscription-checkout', function (Request $request) {
    return $request->user()
        ->newSubscription('default', 'price_monthly')
        ->checkout([
            'success_url' => route('your-success-route'),
            'cancel_url' => route('your-cancel-route'),
        ]);
});

```

Of course, you can also enable promotion codes for subscription checkouts:
```


1use Illuminate\Http\Request;




2 



3Route::get('/subscription-checkout', function (Request $request) {




4    return $request->user()




5        ->newSubscription('default', 'price_monthly')




6        ->allowPromotionCodes()




7        ->checkout();




8});




use Illuminate\Http\Request;

Route::get('/subscription-checkout', function (Request $request) {
    return $request->user()
        ->newSubscription('default', 'price_monthly')
        ->allowPromotionCodes()
        ->checkout();
});

```

Unfortunately Stripe Checkout does not support all subscription billing options when starting subscriptions. Using the `anchorBillingCycleOn` method on the subscription builder, setting proration behavior, or setting payment behavior will not have any effect during Stripe Checkout sessions. Please consult
#### [Stripe Checkout and Trial Periods](https://laravel.com/docs/12.x/billing#stripe-checkout-trial-periods)
Of course, you can define a trial period when building a subscription that will be completed using Stripe Checkout:
```


1$checkout = Auth::user()->newSubscription('default', 'price_monthly')




2    ->trialDays(3)




3    ->checkout();




$checkout = Auth::user()->newSubscription('default', 'price_monthly')
    ->trialDays(3)
    ->checkout();

```

However, the trial period must be at least 48 hours, which is the minimum amount of trial time supported by Stripe Checkout.
#### [Subscriptions and Webhooks](https://laravel.com/docs/12.x/billing#stripe-checkout-subscriptions-and-webhooks)
Remember, Stripe and Cashier update subscription statuses via webhooks, so there's a possibility a subscription might not yet be active when the customer returns to the application after entering their payment information. To handle this scenario, you may wish to display a message informing the user that their payment or subscription is pending.
### [Collecting Tax IDs](https://laravel.com/docs/12.x/billing#collecting-tax-ids)
Checkout also supports collecting a customer's Tax ID. To enable this on a checkout session, invoke the `collectTaxIds` method when creating the session:
```


1$checkout = $user->collectTaxIds()->checkout('price_tshirt');




$checkout = $user->collectTaxIds()->checkout('price_tshirt');

```

When this method is invoked, a new checkbox will be available to the customer that allows them to indicate if they're purchasing as a company. If so, they will have the opportunity to provide their Tax ID number.
If you have already configured [automatic tax collection](https://laravel.com/docs/12.x/billing#tax-configuration) in your application's service provider then this feature will be enabled automatically and there is no need to invoke the `collectTaxIds` method.
### [Guest Checkouts](https://laravel.com/docs/12.x/billing#guest-checkouts)
Using the `Checkout::guest` method, you may initiate checkout sessions for guests of your application that do not have an "account":
```


1use Illuminate\Http\Request;




2use Laravel\Cashier\Checkout;




3 



4Route::get('/product-checkout', function (Request $request) {




5    return Checkout::guest()->create('price_tshirt', [




6        'success_url' => route('your-success-route'),




7        'cancel_url' => route('your-cancel-route'),




8    ]);




9});




use Illuminate\Http\Request;
use Laravel\Cashier\Checkout;

Route::get('/product-checkout', function (Request $request) {
    return Checkout::guest()->create('price_tshirt', [
        'success_url' => route('your-success-route'),
        'cancel_url' => route('your-cancel-route'),
    ]);
});

```

Similarly to when creating checkout sessions for existing users, you may utilize additional methods available on the `Laravel\Cashier\CheckoutBuilder` instance to customize the guest checkout session:
```


 1use Illuminate\Http\Request;




 2use Laravel\Cashier\Checkout;




 3 



 4Route::get('/product-checkout', function (Request $request) {




 5    return Checkout::guest()




 6        ->withPromotionCode('promo-code')




 7        ->create('price_tshirt', [




 8            'success_url' => route('your-success-route'),




 9            'cancel_url' => route('your-cancel-route'),




10        ]);




11});




use Illuminate\Http\Request;
use Laravel\Cashier\Checkout;

Route::get('/product-checkout', function (Request $request) {
    return Checkout::guest()
        ->withPromotionCode('promo-code')
        ->create('price_tshirt', [
            'success_url' => route('your-success-route'),
            'cancel_url' => route('your-cancel-route'),
        ]);
});

```

After a guest checkout has been completed, Stripe can dispatch a `checkout.session.completed` webhook event, so make sure to [handle the webhook with Cashier](https://laravel.com/docs/12.x/billing#handling-stripe-webhooks). The object contained in the webhook payload will be a
