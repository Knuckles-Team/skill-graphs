## [Stripe SDK](https://laravel.com/docs/12.x/billing#stripe-sdk)
Many of Cashier's objects are wrappers around Stripe SDK objects. If you would like to interact with the Stripe objects directly, you may conveniently retrieve them using the `asStripe` method:
```


1$stripeSubscription = $subscription->asStripeSubscription();




2 



3$stripeSubscription->application_fee_percent = 5;




4 



5$stripeSubscription->save();




$stripeSubscription = $subscription->asStripeSubscription();

$stripeSubscription->application_fee_percent = 5;

$stripeSubscription->save();

```

You may also use the `updateStripeSubscription` method to update a Stripe subscription directly:
```


1$subscription->updateStripeSubscription(['application_fee_percent' => 5]);




$subscription->updateStripeSubscription(['application_fee_percent' => 5]);

```

You may invoke the `stripe` method on the `Cashier` class if you would like to use the `Stripe\StripeClient` client directly. For example, you could use this method to access the `StripeClient` instance and retrieve a list of prices from your Stripe account:
```


1use Laravel\Cashier\Cashier;




2 



3$prices = Cashier::stripe()->prices->all();




use Laravel\Cashier\Cashier;

$prices = Cashier::stripe()->prices->all();

```
