## [Testing](https://laravel.com/docs/12.x/mail#testing-mailables)
### [Testing Mailable Content](https://laravel.com/docs/12.x/mail#testing-mailable-content)
Laravel provides a variety of methods for inspecting your mailable's structure. In addition, Laravel provides several convenient methods for testing that your mailable contains the content that you expect:
Pest PHPUnit
```


 1use App\Mail\InvoicePaid;




 2use App\Models\User;




 3 



 4test('mailable content', function () {




 5    $user = User::factory()->create();




 6 



 7    $mailable = new InvoicePaid($user);




 8 



 9    $mailable->assertFrom('jeffrey@example.com');




10    $mailable->assertTo('taylor@example.com');




11    $mailable->assertHasCc('abigail@example.com');




12    $mailable->assertHasBcc('victoria@example.com');




13    $mailable->assertHasReplyTo('tyler@example.com');




14    $mailable->assertHasSubject('Invoice Paid');




15    $mailable->assertHasTag('example-tag');




16    $mailable->assertHasMetadata('key', 'value');




17 



18    $mailable->assertSeeInHtml($user->email);




19    $mailable->assertDontSeeInHtml('Invoice Not Paid');




20    $mailable->assertSeeInOrderInHtml(['Invoice Paid', 'Thanks']);




21 



22    $mailable->assertSeeInText($user->email);




23    $mailable->assertDontSeeInText('Invoice Not Paid');




24    $mailable->assertSeeInOrderInText(['Invoice Paid', 'Thanks']);




25 



26    $mailable->assertHasAttachment('/path/to/file');




27    $mailable->assertHasAttachment(Attachment::fromPath('/path/to/file'));




28    $mailable->assertHasAttachedData($pdfData, 'name.pdf', ['mime' => 'application/pdf']);




29    $mailable->assertHasAttachmentFromStorage('/path/to/file', 'name.pdf', ['mime' => 'application/pdf']);




30    $mailable->assertHasAttachmentFromStorageDisk('s3', '/path/to/file', 'name.pdf', ['mime' => 'application/pdf']);




31});




use App\Mail\InvoicePaid;
use App\Models\User;

test('mailable content', function () {
    $user = User::factory()->create();

    $mailable = new InvoicePaid($user);

    $mailable->assertFrom('jeffrey@example.com');
    $mailable->assertTo('taylor@example.com');
    $mailable->assertHasCc('abigail@example.com');
    $mailable->assertHasBcc('victoria@example.com');
    $mailable->assertHasReplyTo('tyler@example.com');
    $mailable->assertHasSubject('Invoice Paid');
    $mailable->assertHasTag('example-tag');
    $mailable->assertHasMetadata('key', 'value');

    $mailable->assertSeeInHtml($user->email);
    $mailable->assertDontSeeInHtml('Invoice Not Paid');
    $mailable->assertSeeInOrderInHtml(['Invoice Paid', 'Thanks']);

    $mailable->assertSeeInText($user->email);
    $mailable->assertDontSeeInText('Invoice Not Paid');
    $mailable->assertSeeInOrderInText(['Invoice Paid', 'Thanks']);

    $mailable->assertHasAttachment('/path/to/file');
    $mailable->assertHasAttachment(Attachment::fromPath('/path/to/file'));
    $mailable->assertHasAttachedData($pdfData, 'name.pdf', ['mime' => 'application/pdf']);
    $mailable->assertHasAttachmentFromStorage('/path/to/file', 'name.pdf', ['mime' => 'application/pdf']);
    $mailable->assertHasAttachmentFromStorageDisk('s3', '/path/to/file', 'name.pdf', ['mime' => 'application/pdf']);
});

```

```


 1use App\Mail\InvoicePaid;




 2use App\Models\User;




 3 



 4public function test_mailable_content(): void




 5{




 6    $user = User::factory()->create();




 7 



 8    $mailable = new InvoicePaid($user);




 9 



10    $mailable->assertFrom('jeffrey@example.com');




11    $mailable->assertTo('taylor@example.com');




12    $mailable->assertHasCc('abigail@example.com');




13    $mailable->assertHasBcc('victoria@example.com');




14    $mailable->assertHasReplyTo('tyler@example.com');




15    $mailable->assertHasSubject('Invoice Paid');




16    $mailable->assertHasTag('example-tag');




17    $mailable->assertHasMetadata('key', 'value');




18 



19    $mailable->assertSeeInHtml($user->email);




20    $mailable->assertDontSeeInHtml('Invoice Not Paid');




21    $mailable->assertSeeInOrderInHtml(['Invoice Paid', 'Thanks']);




22 



23    $mailable->assertSeeInText($user->email);




24    $mailable->assertDontSeeInText('Invoice Not Paid');




25    $mailable->assertSeeInOrderInText(['Invoice Paid', 'Thanks']);




26 



27    $mailable->assertHasAttachment('/path/to/file');




28    $mailable->assertHasAttachment(Attachment::fromPath('/path/to/file'));




29    $mailable->assertHasAttachedData($pdfData, 'name.pdf', ['mime' => 'application/pdf']);




30    $mailable->assertHasAttachmentFromStorage('/path/to/file', 'name.pdf', ['mime' => 'application/pdf']);




31    $mailable->assertHasAttachmentFromStorageDisk('s3', '/path/to/file', 'name.pdf', ['mime' => 'application/pdf']);




32}




use App\Mail\InvoicePaid;
use App\Models\User;

public function test_mailable_content(): void
{
    $user = User::factory()->create();

    $mailable = new InvoicePaid($user);

    $mailable->assertFrom('jeffrey@example.com');
    $mailable->assertTo('taylor@example.com');
    $mailable->assertHasCc('abigail@example.com');
    $mailable->assertHasBcc('victoria@example.com');
    $mailable->assertHasReplyTo('tyler@example.com');
    $mailable->assertHasSubject('Invoice Paid');
    $mailable->assertHasTag('example-tag');
    $mailable->assertHasMetadata('key', 'value');

    $mailable->assertSeeInHtml($user->email);
    $mailable->assertDontSeeInHtml('Invoice Not Paid');
    $mailable->assertSeeInOrderInHtml(['Invoice Paid', 'Thanks']);

    $mailable->assertSeeInText($user->email);
    $mailable->assertDontSeeInText('Invoice Not Paid');
    $mailable->assertSeeInOrderInText(['Invoice Paid', 'Thanks']);

    $mailable->assertHasAttachment('/path/to/file');
    $mailable->assertHasAttachment(Attachment::fromPath('/path/to/file'));
    $mailable->assertHasAttachedData($pdfData, 'name.pdf', ['mime' => 'application/pdf']);
    $mailable->assertHasAttachmentFromStorage('/path/to/file', 'name.pdf', ['mime' => 'application/pdf']);
    $mailable->assertHasAttachmentFromStorageDisk('s3', '/path/to/file', 'name.pdf', ['mime' => 'application/pdf']);
}

```

As you might expect, the "HTML" assertions assert that the HTML version of your mailable contains a given string, while the "text" assertions assert that the plain-text version of your mailable contains a given string.
### [Testing Mailable Sending](https://laravel.com/docs/12.x/mail#testing-mailable-sending)
We suggest testing the content of your mailables separately from your tests that assert that a given mailable was "sent" to a specific user. Typically, the content of mailables is not relevant to the code you are testing, and it is sufficient to simply assert that Laravel was instructed to send a given mailable.
You may use the `Mail` facade's `fake` method to prevent mail from being sent. After calling the `Mail` facade's `fake` method, you may then assert that mailables were instructed to be sent to users and even inspect the data the mailables received:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Mail\OrderShipped;




 4use Illuminate\Support\Facades\Mail;




 5 



 6test('orders can be shipped', function () {




 7    Mail::fake();




 8 



 9    // Perform order shipping...




10 



11    // Assert that no mailables were sent...




12    Mail::assertNothingSent();




13 



14    // Assert that a mailable was sent...




15    Mail::assertSent(OrderShipped::class);




16 



17    // Assert a mailable was sent twice...




18    Mail::assertSent(OrderShipped::class, 2);




19 



20    // Assert a mailable was sent to an email address...




21    Mail::assertSent(OrderShipped::class, 'example@laravel.com');




22 



23    // Assert a mailable was sent to multiple email addresses...




24    Mail::assertSent(OrderShipped::class, ['example@laravel.com', '...']);




25 



26    // Assert a mailable was not sent...




27    Mail::assertNotSent(AnotherMailable::class);




28 



29    // Assert a mailable was sent twice...




30    Mail::assertSentTimes(OrderShipped::class, 2);




31 



32    // Assert 3 total mailables were sent...




33    Mail::assertSentCount(3);




34});




<?php

use App\Mail\OrderShipped;
use Illuminate\Support\Facades\Mail;

test('orders can be shipped', function () {
    Mail::fake();

    // Perform order shipping...

    // Assert that no mailables were sent...
    Mail::assertNothingSent();

    // Assert that a mailable was sent...
    Mail::assertSent(OrderShipped::class);

    // Assert a mailable was sent twice...
    Mail::assertSent(OrderShipped::class, 2);

    // Assert a mailable was sent to an email address...
    Mail::assertSent(OrderShipped::class, 'example@laravel.com');

    // Assert a mailable was sent to multiple email addresses...
    Mail::assertSent(OrderShipped::class, ['example@laravel.com', '...']);

    // Assert a mailable was not sent...
    Mail::assertNotSent(AnotherMailable::class);

    // Assert a mailable was sent twice...
    Mail::assertSentTimes(OrderShipped::class, 2);

    // Assert 3 total mailables were sent...
    Mail::assertSentCount(3);
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use App\Mail\OrderShipped;




 6use Illuminate\Support\Facades\Mail;




 7use Tests\TestCase;




 8 



 9class ExampleTest extends TestCase




10{




11    public function test_orders_can_be_shipped(): void




12    {




13        Mail::fake();




14 



15        // Perform order shipping...




16 



17        // Assert that no mailables were sent...




18        Mail::assertNothingSent();




19 



20        // Assert that a mailable was sent...




21        Mail::assertSent(OrderShipped::class);




22 



23        // Assert a mailable was sent twice...




24        Mail::assertSent(OrderShipped::class, 2);




25 



26        // Assert a mailable was sent to an email address...




27        Mail::assertSent(OrderShipped::class, 'example@laravel.com');




28 



29        // Assert a mailable was sent to multiple email addresses...




30        Mail::assertSent(OrderShipped::class, ['example@laravel.com', '...']);




31 



32        // Assert a mailable was not sent...




33        Mail::assertNotSent(AnotherMailable::class);




34 



35        // Assert a mailable was sent twice...




36        Mail::assertSentTimes(OrderShipped::class, 2);




37 



38        // Assert 3 total mailables were sent...




39        Mail::assertSentCount(3);




40    }




41}




<?php

namespace Tests\Feature;

use App\Mail\OrderShipped;
use Illuminate\Support\Facades\Mail;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_orders_can_be_shipped(): void
    {
        Mail::fake();

        // Perform order shipping...

        // Assert that no mailables were sent...
        Mail::assertNothingSent();

        // Assert that a mailable was sent...
        Mail::assertSent(OrderShipped::class);

        // Assert a mailable was sent twice...
        Mail::assertSent(OrderShipped::class, 2);

        // Assert a mailable was sent to an email address...
        Mail::assertSent(OrderShipped::class, 'example@laravel.com');

        // Assert a mailable was sent to multiple email addresses...
        Mail::assertSent(OrderShipped::class, ['example@laravel.com', '...']);

        // Assert a mailable was not sent...
        Mail::assertNotSent(AnotherMailable::class);

        // Assert a mailable was sent twice...
        Mail::assertSentTimes(OrderShipped::class, 2);

        // Assert 3 total mailables were sent...
        Mail::assertSentCount(3);
    }
}

```

If you are queueing mailables for delivery in the background, you should use the `assertQueued` method instead of `assertSent`:
```


1Mail::assertQueued(OrderShipped::class);




2Mail::assertNotQueued(OrderShipped::class);




3Mail::assertNothingQueued();




4Mail::assertQueuedCount(3);




Mail::assertQueued(OrderShipped::class);
Mail::assertNotQueued(OrderShipped::class);
Mail::assertNothingQueued();
Mail::assertQueuedCount(3);

```

You can also assert the total number of mailables that have been sent or queued using the `assertOutgoingCount` method:
```


1Mail::assertOutgoingCount(3);




Mail::assertOutgoingCount(3);

```

You may pass a closure to the `assertSent`, `assertNotSent`, `assertQueued`, or `assertNotQueued` methods in order to assert that a mailable was sent that passes a given "truth test". If at least one mailable was sent that passes the given truth test then the assertion will be successful:
```


1Mail::assertSent(function (OrderShipped $mail) use ($order) {




2    return $mail->order->id === $order->id;




3});




Mail::assertSent(function (OrderShipped $mail) use ($order) {
    return $mail->order->id === $order->id;
});

```

When calling the `Mail` facade's assertion methods, the mailable instance accepted by the provided closure exposes helpful methods for examining the mailable:
```


 1Mail::assertSent(OrderShipped::class, function (OrderShipped $mail) use ($user) {




 2    return $mail->hasTo($user->email) &&




 3           $mail->hasCc('...') &&




 4           $mail->hasBcc('...') &&




 5           $mail->hasReplyTo('...') &&




 6           $mail->hasFrom('...') &&




 7           $mail->hasSubject('...') &&




 8           $mail->hasMetadata('order_id', $mail->order->id);




 9           $mail->usesMailer('ses');




10});




Mail::assertSent(OrderShipped::class, function (OrderShipped $mail) use ($user) {
    return $mail->hasTo($user->email) &&
           $mail->hasCc('...') &&
           $mail->hasBcc('...') &&
           $mail->hasReplyTo('...') &&
           $mail->hasFrom('...') &&
           $mail->hasSubject('...') &&
           $mail->hasMetadata('order_id', $mail->order->id);
           $mail->usesMailer('ses');
});

```

The mailable instance also includes several helpful methods for examining the attachments on a mailable:
```


 1use Illuminate\Mail\Mailables\Attachment;




 2 



 3Mail::assertSent(OrderShipped::class, function (OrderShipped $mail) {




 4    return $mail->hasAttachment(




 5        Attachment::fromPath('/path/to/file')




 6            ->as('name.pdf')




 7            ->withMime('application/pdf')




 8    );




 9});




10 



11Mail::assertSent(OrderShipped::class, function (OrderShipped $mail) {




12    return $mail->hasAttachment(




13        Attachment::fromStorageDisk('s3', '/path/to/file')




14    );




15});




16 



17Mail::assertSent(OrderShipped::class, function (OrderShipped $mail) use ($pdfData) {




18    return $mail->hasAttachment(




19        Attachment::fromData(fn () => $pdfData, 'name.pdf')




20    );




21});




use Illuminate\Mail\Mailables\Attachment;

Mail::assertSent(OrderShipped::class, function (OrderShipped $mail) {
    return $mail->hasAttachment(
        Attachment::fromPath('/path/to/file')
            ->as('name.pdf')
            ->withMime('application/pdf')
    );
});

Mail::assertSent(OrderShipped::class, function (OrderShipped $mail) {
    return $mail->hasAttachment(
        Attachment::fromStorageDisk('s3', '/path/to/file')
    );
});

Mail::assertSent(OrderShipped::class, function (OrderShipped $mail) use ($pdfData) {
    return $mail->hasAttachment(
        Attachment::fromData(fn () => $pdfData, 'name.pdf')
    );
});

```

You may have noticed that there are two methods for asserting that mail was not sent: `assertNotSent` and `assertNotQueued`. Sometimes you may wish to assert that no mail was sent **or** queued. To accomplish this, you may use the `assertNothingOutgoing` and `assertNotOutgoing` methods:
```


1Mail::assertNothingOutgoing();




2 



3Mail::assertNotOutgoing(function (OrderShipped $mail) use ($order) {




4    return $mail->order->id === $order->id;




5});




Mail::assertNothingOutgoing();

Mail::assertNotOutgoing(function (OrderShipped $mail) use ($order) {
    return $mail->order->id === $order->id;
});

```
