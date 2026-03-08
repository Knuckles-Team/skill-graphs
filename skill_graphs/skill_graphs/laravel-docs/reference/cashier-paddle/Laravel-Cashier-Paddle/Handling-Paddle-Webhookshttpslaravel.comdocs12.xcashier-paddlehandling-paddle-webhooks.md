## [Handling Paddle Webhooks](https://laravel.com/docs/12.x/cashier-paddle#handling-paddle-webhooks)
Paddle can notify your application of a variety of events via webhooks. By default, a route that points to Cashier's webhook controller is registered by the Cashier service provider. This controller will handle all incoming webhook requests.
By default, this controller will automatically handle canceling subscriptions that have too many failed charges, subscription updates, and payment method changes; however, as we'll soon discover, you can extend this controller to handle any Paddle webhook event you like.
To ensure your application can handle Paddle webhooks, be sure to `/paddle/webhook` URL path. The full list of all webhooks you should enable in the Paddle control panel are:
  * Customer Updated
  * Transaction Completed
  * Transaction Updated
  * Subscription Created
  * Subscription Updated
  * Subscription Paused
  * Subscription Canceled


Make sure you protect incoming requests with Cashier's included [webhook signature verification](https://laravel.com/docs/12.x/cashier-paddle#verifying-webhook-signatures) middleware.
#### [Webhooks and CSRF Protection](https://laravel.com/docs/12.x/cashier-paddle#webhooks-csrf-protection)
Since Paddle webhooks need to bypass Laravel's [CSRF protection](https://laravel.com/docs/12.x/csrf), you should ensure that Laravel does not attempt to verify the CSRF token for incoming Paddle webhooks. To accomplish this, you should exclude `paddle/*` from CSRF protection in your application's `bootstrap/app.php` file:
```


1->withMiddleware(function (Middleware $middleware): void {




2    $middleware->validateCsrfTokens(except: [




3        'paddle/*',




4    ]);




5})




->withMiddleware(function (Middleware $middleware): void {
    $middleware->validateCsrfTokens(except: [
        'paddle/*',
    ]);
})

```

#### [Webhooks and Local Development](https://laravel.com/docs/12.x/cashier-paddle#webhooks-local-development)
For Paddle to be able to send your application webhooks during local development, you will need to expose your application via a site sharing service such as [Laravel Sail](https://laravel.com/docs/12.x/sail), you may use Sail's [site sharing command](https://laravel.com/docs/12.x/sail#sharing-your-site).
### [Defining Webhook Event Handlers](https://laravel.com/docs/12.x/cashier-paddle#defining-webhook-event-handlers)
Cashier automatically handles subscription cancellation on failed charges and other common Paddle webhooks. However, if you have additional webhook events you would like to handle, you may do so by listening to the following events that are dispatched by Cashier:
  * `Laravel\Paddle\Events\WebhookReceived`
  * `Laravel\Paddle\Events\WebhookHandled`


Both events contain the full payload of the Paddle webhook. For example, if you wish to handle the `transaction.billed` webhook, you may register a [listener](https://laravel.com/docs/12.x/events#defining-listeners) that will handle the event:
```


 1<?php




 2 



 3namespace App\Listeners;




 4 



 5use Laravel\Paddle\Events\WebhookReceived;




 6 



 7class PaddleEventListener




 8{




 9    /**




10     * Handle received Paddle webhooks.




11     */




12    public function handle(WebhookReceived $event): void




13    {




14        if ($event->payload['event_type'] === 'transaction.billed') {




15            // Handle the incoming event...




16        }




17    }




18}




<?php

namespace App\Listeners;

use Laravel\Paddle\Events\WebhookReceived;

class PaddleEventListener
{
    /**
     * Handle received Paddle webhooks.
     */
    public function handle(WebhookReceived $event): void
    {
        if ($event->payload['event_type'] === 'transaction.billed') {
            // Handle the incoming event...
        }
    }
}

```

Cashier also emit events dedicated to the type of the received webhook. In addition to the full payload from Paddle, they also contain the relevant models that were used to process the webhook such as the billable model, the subscription, or the receipt:
  * `Laravel\Paddle\Events\CustomerUpdated`
  * `Laravel\Paddle\Events\TransactionCompleted`
  * `Laravel\Paddle\Events\TransactionUpdated`
  * `Laravel\Paddle\Events\SubscriptionCreated`
  * `Laravel\Paddle\Events\SubscriptionUpdated`
  * `Laravel\Paddle\Events\SubscriptionPaused`
  * `Laravel\Paddle\Events\SubscriptionCanceled`


You can also override the default, built-in webhook route by defining the `CASHIER_WEBHOOK` environment variable in your application's `.env` file. This value should be the full URL to your webhook route and needs to match the URL set in your Paddle control panel:
```


1CASHIER_WEBHOOK=https://example.com/my-paddle-webhook-url




CASHIER_WEBHOOK=https://example.com/my-paddle-webhook-url

```

### [Verifying Webhook Signatures](https://laravel.com/docs/12.x/cashier-paddle#verifying-webhook-signatures)
To secure your webhooks, you may use
To enable webhook verification, ensure that the `PADDLE_WEBHOOK_SECRET` environment variable is defined in your application's `.env` file. The webhook secret may be retrieved from your Paddle account dashboard.
