## [Handling Failed Payments](https://laravel.com/docs/12.x/billing#handling-failed-payments)
Sometimes, payments for subscriptions or single charges can fail. When this happens, Cashier will throw an `Laravel\Cashier\Exceptions\IncompletePayment` exception that informs you that this happened. After catching this exception, you have two options on how to proceed.
First, you could redirect your customer to the dedicated payment confirmation page which is included with Cashier. This page already has an associated named route that is registered via Cashier's service provider. So, you may catch the `IncompletePayment` exception and redirect the user to the payment confirmation page:
```


 1use Laravel\Cashier\Exceptions\IncompletePayment;




 2 



 3try {




 4    $subscription = $user->newSubscription('default', 'price_monthly')




 5        ->create($paymentMethod);




 6} catch (IncompletePayment $exception) {




 7    return redirect()->route(




 8        'cashier.payment',




 9        [$exception->payment->id, 'redirect' => route('home')]




10    );




11}




use Laravel\Cashier\Exceptions\IncompletePayment;

try {
    $subscription = $user->newSubscription('default', 'price_monthly')
        ->create($paymentMethod);
} catch (IncompletePayment $exception) {
    return redirect()->route(
        'cashier.payment',
        [$exception->payment->id, 'redirect' => route('home')]
    );
}

```

On the payment confirmation page, the customer will be prompted to enter their credit card information again and perform any additional actions required by Stripe, such as "3D Secure" confirmation. After confirming their payment, the user will be redirected to the URL provided by the `redirect` parameter specified above. Upon redirection, `message` (string) and `success` (integer) query string variables will be added to the URL. The payment page currently supports the following payment method types:
  * Credit Cards
  * Alipay
  * Bancontact
  * BECS Direct Debit
  * EPS
  * Giropay
  * iDEAL
  * SEPA Direct Debit


Alternatively, you could allow Stripe to handle the payment confirmation for you. In this case, instead of redirecting to the payment confirmation page, you may `IncompletePayment` exception is caught, you should still inform the user they will receive an email with further payment confirmation instructions.
Payment exceptions may be thrown for the following methods: `charge`, `invoiceFor`, and `invoice` on models using the `Billable` trait. When interacting with subscriptions, the `create` method on the `SubscriptionBuilder`, and the `incrementAndInvoice` and `swapAndInvoice` methods on the `Subscription` and `SubscriptionItem` models may throw incomplete payment exceptions.
Determining if an existing subscription has an incomplete payment may be accomplished using the `hasIncompletePayment` method on the billable model or a subscription instance:
```


1if ($user->hasIncompletePayment('default')) {




2    // ...




3}




4 



5if ($user->subscription('default')->hasIncompletePayment()) {




6    // ...




7}




if ($user->hasIncompletePayment('default')) {
    // ...
}

if ($user->subscription('default')->hasIncompletePayment()) {
    // ...
}

```

You can derive the specific status of an incomplete payment by inspecting the `payment` property on the exception instance:
```


 1use Laravel\Cashier\Exceptions\IncompletePayment;




 2 



 3try {




 4    $user->charge(1000, 'pm_card_threeDSecure2Required');




 5} catch (IncompletePayment $exception) {




 6    // Get the payment intent status...




 7    $exception->payment->status;




 8 



 9    // Check specific conditions...




10    if ($exception->payment->requiresPaymentMethod()) {




11        // ...




12    } elseif ($exception->payment->requiresConfirmation()) {




13        // ...




14    }




15}




use Laravel\Cashier\Exceptions\IncompletePayment;

try {
    $user->charge(1000, 'pm_card_threeDSecure2Required');
} catch (IncompletePayment $exception) {
    // Get the payment intent status...
    $exception->payment->status;

    // Check specific conditions...
    if ($exception->payment->requiresPaymentMethod()) {
        // ...
    } elseif ($exception->payment->requiresConfirmation()) {
        // ...
    }
}

```

### [Confirming Payments](https://laravel.com/docs/12.x/billing#confirming-payments)
Some payment methods require additional data in order to confirm payments. For example, SEPA payment methods require additional "mandate" data during the payment process. You may provide this data to Cashier using the `withPaymentConfirmationOptions` method:
```


1$subscription->withPaymentConfirmationOptions([




2    'mandate_data' => '...',




3])->swap('price_xxx');




$subscription->withPaymentConfirmationOptions([
    'mandate_data' => '...',
])->swap('price_xxx');

```

You may consult the
