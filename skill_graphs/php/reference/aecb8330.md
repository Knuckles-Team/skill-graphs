## [Subscription Trials](https://laravel.com/docs/12.x/billing#subscription-trials)
### [With Payment Method Up Front](https://laravel.com/docs/12.x/billing#with-payment-method-up-front)
If you would like to offer trial periods to your customers while still collecting payment method information up front, you should use the `trialDays` method when creating your subscriptions:
```


1use Illuminate\Http\Request;




2 



3Route::post('/user/subscribe', function (Request $request) {




4    $request->user()->newSubscription('default', 'price_monthly')




5        ->trialDays(10)




6        ->create($request->paymentMethodId);




7 



8    // ...




9});




use Illuminate\Http\Request;

Route::post('/user/subscribe', function (Request $request) {
    $request->user()->newSubscription('default', 'price_monthly')
        ->trialDays(10)
        ->create($request->paymentMethodId);

    // ...
});

```

This method will set the trial period ending date on the subscription record within the database and instruct Stripe to not begin billing the customer until after this date. When using the `trialDays` method, Cashier will overwrite any default trial period configured for the price in Stripe.
If the customer's subscription is not canceled before the trial ending date they will be charged as soon as the trial expires, so you should be sure to notify your users of their trial ending date.
The `trialUntil` method allows you to provide a `DateTime` instance that specifies when the trial period should end:
```


1use Illuminate\Support\Carbon;




2 



3$user->newSubscription('default', 'price_monthly')




4    ->trialUntil(Carbon::now()->plus(days: 10))




5    ->create($paymentMethod);




use Illuminate\Support\Carbon;

$user->newSubscription('default', 'price_monthly')
    ->trialUntil(Carbon::now()->plus(days: 10))
    ->create($paymentMethod);

```

You may determine if a user is within their trial period using either the `onTrial` method of the user instance or the `onTrial` method of the subscription instance. The two examples below are equivalent:
```


1if ($user->onTrial('default')) {




2    // ...




3}




4 



5if ($user->subscription('default')->onTrial()) {




6    // ...




7}




if ($user->onTrial('default')) {
    // ...
}

if ($user->subscription('default')->onTrial()) {
    // ...
}

```

You may use the `endTrial` method to immediately end a subscription trial:
```


1$user->subscription('default')->endTrial();




$user->subscription('default')->endTrial();

```

To determine if an existing trial has expired, you may use the `hasExpiredTrial` methods:
```


1if ($user->hasExpiredTrial('default')) {




2    // ...




3}




4 



5if ($user->subscription('default')->hasExpiredTrial()) {




6    // ...




7}




if ($user->hasExpiredTrial('default')) {
    // ...
}

if ($user->subscription('default')->hasExpiredTrial()) {
    // ...
}

```

#### [Defining Trial Days in Stripe / Cashier](https://laravel.com/docs/12.x/billing#defining-trial-days-in-stripe-cashier)
You may choose to define how many trial days your price's receive in the Stripe dashboard or always pass them explicitly using Cashier. If you choose to define your price's trial days in Stripe you should be aware that new subscriptions, including new subscriptions for a customer that had a subscription in the past, will always receive a trial period unless you explicitly call the `skipTrial()` method.
### [Without Payment Method Up Front](https://laravel.com/docs/12.x/billing#without-payment-method-up-front)
If you would like to offer trial periods without collecting the user's payment method information up front, you may set the `trial_ends_at` column on the user record to your desired trial ending date. This is typically done during user registration:
```


1use App\Models\User;




2 



3$user = User::create([




4    // ...




5    'trial_ends_at' => now()->plus(days: 10),




6]);




use App\Models\User;

$user = User::create([
    // ...
    'trial_ends_at' => now()->plus(days: 10),
]);

```

Be sure to add a [date cast](https://laravel.com/docs/12.x/eloquent-mutators#date-casting) for the `trial_ends_at` attribute within your billable model's class definition.
Cashier refers to this type of trial as a "generic trial", since it is not attached to any existing subscription. The `onTrial` method on the billable model instance will return `true` if the current date is not past the value of `trial_ends_at`:
```


1if ($user->onTrial()) {




2    // User is within their trial period...




3}




if ($user->onTrial()) {
    // User is within their trial period...
}

```

Once you are ready to create an actual subscription for the user, you may use the `newSubscription` method as usual:
```


1$user = User::find(1);




2 



3$user->newSubscription('default', 'price_monthly')->create($paymentMethod);




$user = User::find(1);

$user->newSubscription('default', 'price_monthly')->create($paymentMethod);

```

To retrieve the user's trial ending date, you may use the `trialEndsAt` method. This method will return a Carbon date instance if a user is on a trial or `null` if they aren't. You may also pass an optional subscription type parameter if you would like to get the trial ending date for a specific subscription other than the default one:
```


1if ($user->onTrial()) {




2    $trialEndsAt = $user->trialEndsAt('main');




3}




if ($user->onTrial()) {
    $trialEndsAt = $user->trialEndsAt('main');
}

```

You may also use the `onGenericTrial` method if you wish to know specifically that the user is within their "generic" trial period and has not yet created an actual subscription:
```


1if ($user->onGenericTrial()) {




2    // User is within their "generic" trial period...




3}




if ($user->onGenericTrial()) {
    // User is within their "generic" trial period...
}

```

### [Extending Trials](https://laravel.com/docs/12.x/billing#extending-trials)
The `extendTrial` method allows you to extend the trial period of a subscription after the subscription has been created. If the trial has already expired and the customer is already being billed for the subscription, you can still offer them an extended trial. The time spent within the trial period will be deducted from the customer's next invoice:
```


 1use App\Models\User;




 2 



 3$subscription = User::find(1)->subscription('default');




 4 



 5// End the trial 7 days from now...




 6$subscription->extendTrial(




 7    now()->plus(days: 7)




 8);




 9 



10// Add an additional 5 days to the trial...




11$subscription->extendTrial(




12    $subscription->trial_ends_at->plus(days: 5)




13);




use App\Models\User;

$subscription = User::find(1)->subscription('default');

// End the trial 7 days from now...
$subscription->extendTrial(
    now()->plus(days: 7)
);

// Add an additional 5 days to the trial...
$subscription->extendTrial(
    $subscription->trial_ends_at->plus(days: 5)
);

```
