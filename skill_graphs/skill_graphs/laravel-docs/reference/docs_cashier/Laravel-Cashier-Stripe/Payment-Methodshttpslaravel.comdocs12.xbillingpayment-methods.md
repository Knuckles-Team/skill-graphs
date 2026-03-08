## [Payment Methods](https://laravel.com/docs/12.x/billing#payment-methods)
### [Storing Payment Methods](https://laravel.com/docs/12.x/billing#storing-payment-methods)
In order to create subscriptions or perform "one-off" charges with Stripe, you will need to store a payment method and retrieve its identifier from Stripe. The approach used to accomplish this differs based on whether you plan to use the payment method for subscriptions or single charges, so we will examine both below.
#### [Payment Methods for Subscriptions](https://laravel.com/docs/12.x/billing#payment-methods-for-subscriptions)
When storing a customer's credit card information for future use by a subscription, the Stripe "Setup Intents" API must be used to securely gather the customer's payment method details. A "Setup Intent" indicates to Stripe the intention to charge a customer's payment method. Cashier's `Billable` trait includes the `createSetupIntent` method to easily create a new Setup Intent. You should invoke this method from the route or controller that will render the form which gathers your customer's payment method details:
```


1return view('update-payment-method', [




2    'intent' => $user->createSetupIntent()




3]);




return view('update-payment-method', [
    'intent' => $user->createSetupIntent()
]);

```

After you have created the Setup Intent and passed it to the view, you should attach its secret to the element that will gather the payment method. For example, consider this "update payment method" form:
```


1<input id="card-holder-name" type="text">




2 



3<!-- Stripe Elements Placeholder -->




4<div id="card-element"></div>




5 



6<button id="card-button" data-secret="{{ $intent->client_secret }}">




7    Update Payment Method




8</button>




<input id="card-holder-name" type="text">

<!-- Stripe Elements Placeholder -->
<div id="card-element"></div>

<button id="card-button" data-secret="{{ $intent->client_secret }}">
    Update Payment Method
</button>

```

Next, the Stripe.js library may be used to attach a
```


 1<script src="https://js.stripe.com/v3/"></script>




 2 



 3<script>




 4    const stripe = Stripe('stripe-public-key');




 5 



 6    const elements = stripe.elements();




 7    const cardElement = elements.create('card');




 8 



 9    cardElement.mount('#card-element');




10</script>




<script src="https://js.stripe.com/v3/"></script>

<script>
    const stripe = Stripe('stripe-public-key');

    const elements = stripe.elements();
    const cardElement = elements.create('card');

    cardElement.mount('#card-element');
</script>

```

Next, the card can be verified and a secure "payment method identifier" can be retrieved from Stripe using
```


 1const cardHolderName = document.getElementById('card-holder-name');




 2const cardButton = document.getElementById('card-button');




 3const clientSecret = cardButton.dataset.secret;




 4 



 5cardButton.addEventListener('click', async (e) => {




 6    const { setupIntent, error } = await stripe.confirmCardSetup(




 7        clientSecret, {




 8            payment_method: {




 9                card: cardElement,




10                billing_details: { name: cardHolderName.value }




11            }




12        }




13    );




14 



15    if (error) {




16        // Display "error.message" to the user...




17    } else {




18        // The card has been verified successfully...




19    }




20});




const cardHolderName = document.getElementById('card-holder-name');
const cardButton = document.getElementById('card-button');
const clientSecret = cardButton.dataset.secret;

cardButton.addEventListener('click', async (e) => {
    const { setupIntent, error } = await stripe.confirmCardSetup(
        clientSecret, {
            payment_method: {
                card: cardElement,
                billing_details: { name: cardHolderName.value }
            }
        }
    );

    if (error) {
        // Display "error.message" to the user...
    } else {
        // The card has been verified successfully...
    }
});

```

After the card has been verified by Stripe, you may pass the resulting `setupIntent.payment_method` identifier to your Laravel application, where it can be attached to the customer. The payment method can either be [added as a new payment method](https://laravel.com/docs/12.x/billing#adding-payment-methods) or [used to update the default payment method](https://laravel.com/docs/12.x/billing#updating-the-default-payment-method). You can also immediately use the payment method identifier to [create a new subscription](https://laravel.com/docs/12.x/billing#creating-subscriptions).
If you would like more information about Setup Intents and gathering customer payment details please
#### [Payment Methods for Single Charges](https://laravel.com/docs/12.x/billing#payment-methods-for-single-charges)
Of course, when making a single charge against a customer's payment method, we will only need to use a payment method identifier once. Due to Stripe limitations, you may not use the stored default payment method of a customer for single charges. You must allow the customer to enter their payment method details using the Stripe.js library. For example, consider the following form:
```


1<input id="card-holder-name" type="text">




2 



3<!-- Stripe Elements Placeholder -->




4<div id="card-element"></div>




5 



6<button id="card-button">




7    Process Payment




8</button>




<input id="card-holder-name" type="text">

<!-- Stripe Elements Placeholder -->
<div id="card-element"></div>

<button id="card-button">
    Process Payment
</button>

```

After defining such a form, the Stripe.js library may be used to attach a
```


 1<script src="https://js.stripe.com/v3/"></script>




 2 



 3<script>




 4    const stripe = Stripe('stripe-public-key');




 5 



 6    const elements = stripe.elements();




 7    const cardElement = elements.create('card');




 8 



 9    cardElement.mount('#card-element');




10</script>




<script src="https://js.stripe.com/v3/"></script>

<script>
    const stripe = Stripe('stripe-public-key');

    const elements = stripe.elements();
    const cardElement = elements.create('card');

    cardElement.mount('#card-element');
</script>

```

Next, the card can be verified and a secure "payment method identifier" can be retrieved from Stripe using
```


 1const cardHolderName = document.getElementById('card-holder-name');




 2const cardButton = document.getElementById('card-button');




 3 



 4cardButton.addEventListener('click', async (e) => {




 5    const { paymentMethod, error } = await stripe.createPaymentMethod(




 6        'card', cardElement, {




 7            billing_details: { name: cardHolderName.value }




 8        }




 9    );




10 



11    if (error) {




12        // Display "error.message" to the user...




13    } else {




14        // The card has been verified successfully...




15    }




16});




const cardHolderName = document.getElementById('card-holder-name');
const cardButton = document.getElementById('card-button');

cardButton.addEventListener('click', async (e) => {
    const { paymentMethod, error } = await stripe.createPaymentMethod(
        'card', cardElement, {
            billing_details: { name: cardHolderName.value }
        }
    );

    if (error) {
        // Display "error.message" to the user...
    } else {
        // The card has been verified successfully...
    }
});

```

If the card is verified successfully, you may pass the `paymentMethod.id` to your Laravel application and process a [single charge](https://laravel.com/docs/12.x/billing#simple-charge).
### [Retrieving Payment Methods](https://laravel.com/docs/12.x/billing#retrieving-payment-methods)
The `paymentMethods` method on the billable model instance returns a collection of `Laravel\Cashier\PaymentMethod` instances:
```


1$paymentMethods = $user->paymentMethods();




$paymentMethods = $user->paymentMethods();

```

By default, this method will return payment methods of every type. To retrieve payment methods of a specific type, you may pass the `type` as an argument to the method:
```


1$paymentMethods = $user->paymentMethods('sepa_debit');




$paymentMethods = $user->paymentMethods('sepa_debit');

```

To retrieve the customer's default payment method, the `defaultPaymentMethod` method may be used:
```


1$paymentMethod = $user->defaultPaymentMethod();




$paymentMethod = $user->defaultPaymentMethod();

```

You can retrieve a specific payment method that is attached to the billable model using the `findPaymentMethod` method:
```


1$paymentMethod = $user->findPaymentMethod($paymentMethodId);




$paymentMethod = $user->findPaymentMethod($paymentMethodId);

```

### [Payment Method Presence](https://laravel.com/docs/12.x/billing#payment-method-presence)
To determine if a billable model has a default payment method attached to their account, invoke the `hasDefaultPaymentMethod` method:
```


1if ($user->hasDefaultPaymentMethod()) {




2    // ...




3}




if ($user->hasDefaultPaymentMethod()) {
    // ...
}

```

You may use the `hasPaymentMethod` method to determine if a billable model has at least one payment method attached to their account:
```


1if ($user->hasPaymentMethod()) {




2    // ...




3}




if ($user->hasPaymentMethod()) {
    // ...
}

```

This method will determine if the billable model has any payment method at all. To determine if a payment method of a specific type exists for the model, you may pass the `type` as an argument to the method:
```


1if ($user->hasPaymentMethod('sepa_debit')) {




2    // ...




3}




if ($user->hasPaymentMethod('sepa_debit')) {
    // ...
}

```

### [Updating the Default Payment Method](https://laravel.com/docs/12.x/billing#updating-the-default-payment-method)
The `updateDefaultPaymentMethod` method may be used to update a customer's default payment method information. This method accepts a Stripe payment method identifier and will assign the new payment method as the default billing payment method:
```


1$user->updateDefaultPaymentMethod($paymentMethod);




$user->updateDefaultPaymentMethod($paymentMethod);

```

To sync your default payment method information with the customer's default payment method information in Stripe, you may use the `updateDefaultPaymentMethodFromStripe` method:
```


1$user->updateDefaultPaymentMethodFromStripe();




$user->updateDefaultPaymentMethodFromStripe();

```

The default payment method on a customer can only be used for invoicing and creating new subscriptions. Due to limitations imposed by Stripe, it may not be used for single charges.
### [Adding Payment Methods](https://laravel.com/docs/12.x/billing#adding-payment-methods)
To add a new payment method, you may call the `addPaymentMethod` method on the billable model, passing the payment method identifier:
```


1$user->addPaymentMethod($paymentMethod);




$user->addPaymentMethod($paymentMethod);

```

To learn how to retrieve payment method identifiers please review the [payment method storage documentation](https://laravel.com/docs/12.x/billing#storing-payment-methods).
### [Deleting Payment Methods](https://laravel.com/docs/12.x/billing#deleting-payment-methods)
To delete a payment method, you may call the `delete` method on the `Laravel\Cashier\PaymentMethod` instance you wish to delete:
```


1$paymentMethod->delete();




$paymentMethod->delete();

```

The `deletePaymentMethod` method will delete a specific payment method from the billable model:
```


1$user->deletePaymentMethod('pm_visa');




$user->deletePaymentMethod('pm_visa');

```

The `deletePaymentMethods` method will delete all of the payment method information for the billable model:
```


1$user->deletePaymentMethods();




$user->deletePaymentMethods();

```

By default, this method will delete payment methods of every type. To delete payment methods of a specific type you can pass the `type` as an argument to the method:
```


1$user->deletePaymentMethods('sepa_debit');




$user->deletePaymentMethods('sepa_debit');

```

If a user has an active subscription, your application should not allow them to delete their default payment method.
