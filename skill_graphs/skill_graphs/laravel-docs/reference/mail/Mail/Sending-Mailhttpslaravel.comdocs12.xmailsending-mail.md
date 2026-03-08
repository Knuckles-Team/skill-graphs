## [Sending Mail](https://laravel.com/docs/12.x/mail#sending-mail)
To send a message, use the `to` method on the `Mail` [facade](https://laravel.com/docs/12.x/facades). The `to` method accepts an email address, a user instance, or a collection of users. If you pass an object or collection of objects, the mailer will automatically use their `email` and `name` properties when determining the email's recipients, so make sure these attributes are available on your objects. Once you have specified your recipients, you may pass an instance of your mailable class to the `send` method:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use App\Mail\OrderShipped;




 6use App\Models\Order;




 7use Illuminate\Http\RedirectResponse;




 8use Illuminate\Http\Request;




 9use Illuminate\Support\Facades\Mail;




10 



11class OrderShipmentController extends Controller




12{




13    /**




14     * Ship the given order.




15     */




16    public function store(Request $request): RedirectResponse




17    {




18        $order = Order::findOrFail($request->order_id);




19 



20        // Ship the order...




21 



22        Mail::to($request->user())->send(new OrderShipped($order));




23 



24        return redirect('/orders');




25    }




26}




<?php

namespace App\Http\Controllers;

use App\Mail\OrderShipped;
use App\Models\Order;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

class OrderShipmentController extends Controller
{
    /**
     * Ship the given order.
     */
    public function store(Request $request): RedirectResponse
    {
        $order = Order::findOrFail($request->order_id);

        // Ship the order...

        Mail::to($request->user())->send(new OrderShipped($order));

        return redirect('/orders');
    }
}

```

You are not limited to just specifying the "to" recipients when sending a message. You are free to set "to", "cc", and "bcc" recipients by chaining their respective methods together:
```


1Mail::to($request->user())




2    ->cc($moreUsers)




3    ->bcc($evenMoreUsers)




4    ->send(new OrderShipped($order));




Mail::to($request->user())
    ->cc($moreUsers)
    ->bcc($evenMoreUsers)
    ->send(new OrderShipped($order));

```

#### [Looping Over Recipients](https://laravel.com/docs/12.x/mail#looping-over-recipients)
Occasionally, you may need to send a mailable to a list of recipients by iterating over an array of recipients / email addresses. However, since the `to` method appends email addresses to the mailable's list of recipients, each iteration through the loop will send another email to every previous recipient. Therefore, you should always re-create the mailable instance for each recipient:
```


1foreach (['taylor@example.com', 'dries@example.com'] as $recipient) {




2    Mail::to($recipient)->send(new OrderShipped($order));




3}




foreach (['taylor@example.com', 'dries@example.com'] as $recipient) {
    Mail::to($recipient)->send(new OrderShipped($order));
}

```

#### [Sending Mail via a Specific Mailer](https://laravel.com/docs/12.x/mail#sending-mail-via-a-specific-mailer)
By default, Laravel will send email using the mailer configured as the `default` mailer in your application's `mail` configuration file. However, you may use the `mailer` method to send a message using a specific mailer configuration:
```


1Mail::mailer('postmark')




2    ->to($request->user())




3    ->send(new OrderShipped($order));




Mail::mailer('postmark')
    ->to($request->user())
    ->send(new OrderShipped($order));

```

### [Queueing Mail](https://laravel.com/docs/12.x/mail#queueing-mail)
#### [Queueing a Mail Message](https://laravel.com/docs/12.x/mail#queueing-a-mail-message)
Since sending email messages can negatively impact the response time of your application, many developers choose to queue email messages for background sending. Laravel makes this easy using its built-in [unified queue API](https://laravel.com/docs/12.x/queues). To queue a mail message, use the `queue` method on the `Mail` facade after specifying the message's recipients:
```


1Mail::to($request->user())




2    ->cc($moreUsers)




3    ->bcc($evenMoreUsers)




4    ->queue(new OrderShipped($order));




Mail::to($request->user())
    ->cc($moreUsers)
    ->bcc($evenMoreUsers)
    ->queue(new OrderShipped($order));

```

This method will automatically take care of pushing a job onto the queue so the message is sent in the background. You will need to [configure your queues](https://laravel.com/docs/12.x/queues) before using this feature.
#### [Delayed Message Queueing](https://laravel.com/docs/12.x/mail#delayed-message-queueing)
If you wish to delay the delivery of a queued email message, you may use the `later` method. As its first argument, the `later` method accepts a `DateTime` instance indicating when the message should be sent:
```


1Mail::to($request->user())




2    ->cc($moreUsers)




3    ->bcc($evenMoreUsers)




4    ->later(now()->plus(minutes: 10), new OrderShipped($order));




Mail::to($request->user())
    ->cc($moreUsers)
    ->bcc($evenMoreUsers)
    ->later(now()->plus(minutes: 10), new OrderShipped($order));

```

#### [Pushing to Specific Queues](https://laravel.com/docs/12.x/mail#pushing-to-specific-queues)
Since all mailable classes generated using the `make:mail` command make use of the `Illuminate\Bus\Queueable` trait, you may call the `onQueue` and `onConnection` methods on any mailable class instance, allowing you to specify the connection and queue name for the message:
```


1$message = (new OrderShipped($order))




2    ->onConnection('sqs')




3    ->onQueue('emails');




4 



5Mail::to($request->user())




6    ->cc($moreUsers)




7    ->bcc($evenMoreUsers)




8    ->queue($message);




$message = (new OrderShipped($order))
    ->onConnection('sqs')
    ->onQueue('emails');

Mail::to($request->user())
    ->cc($moreUsers)
    ->bcc($evenMoreUsers)
    ->queue($message);

```

#### [Queueing by Default](https://laravel.com/docs/12.x/mail#queueing-by-default)
If you have mailable classes that you want to always be queued, you may implement the `ShouldQueue` contract on the class. Now, even if you call the `send` method when mailing, the mailable will still be queued since it implements the contract:
```


1use Illuminate\Contracts\Queue\ShouldQueue;




2 



3class OrderShipped extends Mailable implements ShouldQueue




4{




5    // ...




6}




use Illuminate\Contracts\Queue\ShouldQueue;

class OrderShipped extends Mailable implements ShouldQueue
{
    // ...
}

```

#### [Queued Mailables and Database Transactions](https://laravel.com/docs/12.x/mail#queued-mailables-and-database-transactions)
When queued mailables are dispatched within database transactions, they may be processed by the queue before the database transaction has committed. When this happens, any updates you have made to models or database records during the database transaction may not yet be reflected in the database. In addition, any models or database records created within the transaction may not exist in the database. If your mailable depends on these models, unexpected errors can occur when the job that sends the queued mailable is processed.
If your queue connection's `after_commit` configuration option is set to `false`, you may still indicate that a particular queued mailable should be dispatched after all open database transactions have been committed by calling the `afterCommit` method when sending the mail message:
```


1Mail::to($request->user())->send(




2    (new OrderShipped($order))->afterCommit()




3);




Mail::to($request->user())->send(
    (new OrderShipped($order))->afterCommit()
);

```

Alternatively, you may call the `afterCommit` method from your mailable's constructor:
```


 1<?php




 2 



 3namespace App\Mail;




 4 



 5use Illuminate\Bus\Queueable;




 6use Illuminate\Contracts\Queue\ShouldQueue;




 7use Illuminate\Mail\Mailable;




 8use Illuminate\Queue\SerializesModels;




 9 



10class OrderShipped extends Mailable implements ShouldQueue




11{




12    use Queueable, SerializesModels;




13 



14    /**




15     * Create a new message instance.




16     */




17    public function __construct()




18    {




19        $this->afterCommit();




20    }




21}




<?php

namespace App\Mail;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;

class OrderShipped extends Mailable implements ShouldQueue
{
    use Queueable, SerializesModels;

    /**
     * Create a new message instance.
     */
    public function __construct()
    {
        $this->afterCommit();
    }
}

```

To learn more about working around these issues, please review the documentation regarding [queued jobs and database transactions](https://laravel.com/docs/12.x/queues#jobs-and-database-transactions).
#### [Queued Email Failures](https://laravel.com/docs/12.x/mail#queued-email-failures)
When a queued email fails, the `failed` method on the queued mailable class will be invoked if it has been defined. The `Throwable` instance that caused the queued email to fail will be passed to the `failed` method:
```


 1<?php




 2 



 3namespace App\Mail;




 4 



 5use Illuminate\Contracts\Queue\ShouldQueue;




 6use Illuminate\Mail\Mailable;




 7use Illuminate\Queue\SerializesModels;




 8use Throwable;




 9 



10class OrderDelayed extends Mailable implements ShouldQueue




11{




12    use SerializesModels;




13 



14    /**




15     * Handle a queued email's failure.




16     */




17    public function failed(Throwable $exception): void




18    {




19        // ...




20    }




21}




<?php

namespace App\Mail;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;
use Throwable;

class OrderDelayed extends Mailable implements ShouldQueue
{
    use SerializesModels;

    /**
     * Handle a queued email's failure.
     */
    public function failed(Throwable $exception): void
    {
        // ...
    }
}

```
