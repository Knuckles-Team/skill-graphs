## [Writing Mailables](https://laravel.com/docs/12.x/mail#writing-mailables)
Once you have generated a mailable class, open it up so we can explore its contents. Mailable class configuration is done in several methods, including the `envelope`, `content`, and `attachments` methods.
The `envelope` method returns an `Illuminate\Mail\Mailables\Envelope` object that defines the subject and, sometimes, the recipients of the message. The `content` method returns an `Illuminate\Mail\Mailables\Content` object that defines the [Blade template](https://laravel.com/docs/12.x/blade) that will be used to generate the message content.
### [Configuring the Sender](https://laravel.com/docs/12.x/mail#configuring-the-sender)
#### [Using the Envelope](https://laravel.com/docs/12.x/mail#using-the-envelope)
First, let's explore configuring the sender of the email. Or, in other words, who the email is going to be "from". There are two ways to configure the sender. First, you may specify the "from" address on your message's envelope:
```


 1use Illuminate\Mail\Mailables\Address;




 2use Illuminate\Mail\Mailables\Envelope;




 3 



 4/**




 5 * Get the message envelope.




 6 */




 7public function envelope(): Envelope




 8{




 9    return new Envelope(




10        from: new Address('jeffrey@example.com', 'Jeffrey Way'),




11        subject: 'Order Shipped',




12    );




13}




use Illuminate\Mail\Mailables\Address;
use Illuminate\Mail\Mailables\Envelope;

/**
 * Get the message envelope.
 */
public function envelope(): Envelope
{
    return new Envelope(
        from: new Address('jeffrey@example.com', 'Jeffrey Way'),
        subject: 'Order Shipped',
    );
}

```

If you would like, you may also specify a `replyTo` address:
```


1return new Envelope(




2    from: new Address('jeffrey@example.com', 'Jeffrey Way'),




3    replyTo: [




4        new Address('taylor@example.com', 'Taylor Otwell'),




5    ],




6    subject: 'Order Shipped',




7);




return new Envelope(
    from: new Address('jeffrey@example.com', 'Jeffrey Way'),
    replyTo: [
        new Address('taylor@example.com', 'Taylor Otwell'),
    ],
    subject: 'Order Shipped',
);

```

#### [Using a Global `from` Address](https://laravel.com/docs/12.x/mail#using-a-global-from-address)
However, if your application uses the same "from" address for all of its emails, it can become cumbersome to add it to each mailable class you generate. Instead, you may specify a global "from" address in your `config/mail.php` configuration file. This address will be used if no other "from" address is specified within the mailable class:
```


1'from' => [




2    'address' => env('MAIL_FROM_ADDRESS', 'hello@example.com'),




3    'name' => env('MAIL_FROM_NAME', 'Example'),




4],




'from' => [
    'address' => env('MAIL_FROM_ADDRESS', 'hello@example.com'),
    'name' => env('MAIL_FROM_NAME', 'Example'),
],

```

In addition, you may define a global "reply_to" address within your `config/mail.php` configuration file:
```


1'reply_to' => [




2    'address' => 'example@example.com',




3    'name' => 'App Name',




4],




'reply_to' => [
    'address' => 'example@example.com',
    'name' => 'App Name',
],

```

### [Configuring the View](https://laravel.com/docs/12.x/mail#configuring-the-view)
Within a mailable class's `content` method, you may define the `view`, or which template should be used when rendering the email's contents. Since each email typically uses a [Blade template](https://laravel.com/docs/12.x/blade) to render its contents, you have the full power and convenience of the Blade templating engine when building your email's HTML:
```


1/**




2 * Get the message content definition.




3 */




4public function content(): Content




5{




6    return new Content(




7        view: 'mail.orders.shipped',




8    );




9}




/**
 * Get the message content definition.
 */
public function content(): Content
{
    return new Content(
        view: 'mail.orders.shipped',
    );
}

```

You may wish to create a `resources/views/mail` directory to house all of your email templates; however, you are free to place them wherever you wish within your `resources/views` directory.
#### [Plain Text Emails](https://laravel.com/docs/12.x/mail#plain-text-emails)
If you would like to define a plain-text version of your email, you may specify the plain-text template when creating the message's `Content` definition. Like the `view` parameter, the `text` parameter should be a template name which will be used to render the contents of the email. You are free to define both an HTML and plain-text version of your message:
```


 1/**




 2 * Get the message content definition.




 3 */




 4public function content(): Content




 5{




 6    return new Content(




 7        view: 'mail.orders.shipped',




 8        text: 'mail.orders.shipped-text'




 9    );




10}




/**
 * Get the message content definition.
 */
public function content(): Content
{
    return new Content(
        view: 'mail.orders.shipped',
        text: 'mail.orders.shipped-text'
    );
}

```

For clarity, the `html` parameter may be used as an alias of the `view` parameter:
```


1return new Content(




2    html: 'mail.orders.shipped',




3    text: 'mail.orders.shipped-text'




4);




return new Content(
    html: 'mail.orders.shipped',
    text: 'mail.orders.shipped-text'
);

```

### [View Data](https://laravel.com/docs/12.x/mail#view-data)
#### [Via Public Properties](https://laravel.com/docs/12.x/mail#via-public-properties)
Typically, you will want to pass some data to your view that you can utilize when rendering the email's HTML. There are two ways you may make data available to your view. First, any public property defined on your mailable class will automatically be made available to the view. So, for example, you may pass data into your mailable class's constructor and set that data to public properties defined on the class:
```


 1<?php




 2 



 3namespace App\Mail;




 4 



 5use App\Models\Order;




 6use Illuminate\Bus\Queueable;




 7use Illuminate\Mail\Mailable;




 8use Illuminate\Mail\Mailables\Content;




 9use Illuminate\Queue\SerializesModels;




10 



11class OrderShipped extends Mailable




12{




13    use Queueable, SerializesModels;




14 



15    /**




16     * Create a new message instance.




17     */




18    public function __construct(




19        public Order $order,




20    ) {}




21 



22    /**




23     * Get the message content definition.




24     */




25    public function content(): Content




26    {




27        return new Content(




28            view: 'mail.orders.shipped',




29        );




30    }




31}




<?php

namespace App\Mail;

use App\Models\Order;
use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Queue\SerializesModels;

class OrderShipped extends Mailable
{
    use Queueable, SerializesModels;

    /**
     * Create a new message instance.
     */
    public function __construct(
        public Order $order,
    ) {}

    /**
     * Get the message content definition.
     */
    public function content(): Content
    {
        return new Content(
            view: 'mail.orders.shipped',
        );
    }
}

```

Once the data has been set to a public property, it will automatically be available in your view, so you may access it like you would access any other data in your Blade templates:
```


1<div>




2    Price: {{ $order->price }}




3</div>




<div>
    Price: {{ $order->price }}
</div>

```

#### [Via the `with` Parameter:](https://laravel.com/docs/12.x/mail#via-the-with-parameter)
If you would like to customize the format of your email's data before it is sent to the template, you may manually pass your data to the view via the `Content` definition's `with` parameter. Typically, you will still pass data via the mailable class's constructor; however, you should set this data to `protected` or `private` properties so the data is not automatically made available to the template:
```


 1<?php




 2 



 3namespace App\Mail;




 4 



 5use App\Models\Order;




 6use Illuminate\Bus\Queueable;




 7use Illuminate\Mail\Mailable;




 8use Illuminate\Mail\Mailables\Content;




 9use Illuminate\Queue\SerializesModels;




10 



11class OrderShipped extends Mailable




12{




13    use Queueable, SerializesModels;




14 



15    /**




16     * Create a new message instance.




17     */




18    public function __construct(




19        protected Order $order,




20    ) {}




21 



22    /**




23     * Get the message content definition.




24     */




25    public function content(): Content




26    {




27        return new Content(




28            view: 'mail.orders.shipped',




29            with: [




30                'orderName' => $this->order->name,




31                'orderPrice' => $this->order->price,




32            ],




33        );




34    }




35}




<?php

namespace App\Mail;

use App\Models\Order;
use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Queue\SerializesModels;

class OrderShipped extends Mailable
{
    use Queueable, SerializesModels;

    /**
     * Create a new message instance.
     */
    public function __construct(
        protected Order $order,
    ) {}

    /**
     * Get the message content definition.
     */
    public function content(): Content
    {
        return new Content(
            view: 'mail.orders.shipped',
            with: [
                'orderName' => $this->order->name,
                'orderPrice' => $this->order->price,
            ],
        );
    }
}

```

Once the data has been passed via the `with` parameter, it will automatically be available in your view, so you may access it like you would access any other data in your Blade templates:
```


1<div>




2    Price: {{ $orderPrice }}




3</div>




<div>
    Price: {{ $orderPrice }}
</div>

```

### [Attachments](https://laravel.com/docs/12.x/mail#attachments)
To add attachments to an email, you will add attachments to the array returned by the message's `attachments` method. First, you may add an attachment by providing a file path to the `fromPath` method provided by the `Attachment` class:
```


 1use Illuminate\Mail\Mailables\Attachment;




 2 



 3/**




 4 * Get the attachments for the message.




 5 *




 6 * @return array<int, \Illuminate\Mail\Mailables\Attachment>




 7 */




 8public function attachments(): array




 9{




10    return [




11        Attachment::fromPath('/path/to/file'),




12    ];




13}




use Illuminate\Mail\Mailables\Attachment;

/**
 * Get the attachments for the message.
 *
 * @return array<int, \Illuminate\Mail\Mailables\Attachment>
 */
public function attachments(): array
{
    return [
        Attachment::fromPath('/path/to/file'),
    ];
}

```

When attaching files to a message, you may also specify the display name and / or MIME type for the attachment using the `as` and `withMime` methods:
```


 1/**




 2 * Get the attachments for the message.




 3 *




 4 * @return array<int, \Illuminate\Mail\Mailables\Attachment>




 5 */




 6public function attachments(): array




 7{




 8    return [




 9        Attachment::fromPath('/path/to/file')




10            ->as('name.pdf')




11            ->withMime('application/pdf'),




12    ];




13}




/**
 * Get the attachments for the message.
 *
 * @return array<int, \Illuminate\Mail\Mailables\Attachment>
 */
public function attachments(): array
{
    return [
        Attachment::fromPath('/path/to/file')
            ->as('name.pdf')
            ->withMime('application/pdf'),
    ];
}

```

#### [Attaching Files From Disk](https://laravel.com/docs/12.x/mail#attaching-files-from-disk)
If you have stored a file on one of your [filesystem disks](https://laravel.com/docs/12.x/filesystem), you may attach it to the email using the `fromStorage` attachment method:
```


 1/**




 2 * Get the attachments for the message.




 3 *




 4 * @return array<int, \Illuminate\Mail\Mailables\Attachment>




 5 */




 6public function attachments(): array




 7{




 8    return [




 9        Attachment::fromStorage('/path/to/file'),




10    ];




11}




/**
 * Get the attachments for the message.
 *
 * @return array<int, \Illuminate\Mail\Mailables\Attachment>
 */
public function attachments(): array
{
    return [
        Attachment::fromStorage('/path/to/file'),
    ];
}

```

Of course, you may also specify the attachment's name and MIME type:
```


 1/**




 2 * Get the attachments for the message.




 3 *




 4 * @return array<int, \Illuminate\Mail\Mailables\Attachment>




 5 */




 6public function attachments(): array




 7{




 8    return [




 9        Attachment::fromStorage('/path/to/file')




10            ->as('name.pdf')




11            ->withMime('application/pdf'),




12    ];




13}




/**
 * Get the attachments for the message.
 *
 * @return array<int, \Illuminate\Mail\Mailables\Attachment>
 */
public function attachments(): array
{
    return [
        Attachment::fromStorage('/path/to/file')
            ->as('name.pdf')
            ->withMime('application/pdf'),
    ];
}

```

The `fromStorageDisk` method may be used if you need to specify a storage disk other than your default disk:
```


 1/**




 2 * Get the attachments for the message.




 3 *




 4 * @return array<int, \Illuminate\Mail\Mailables\Attachment>




 5 */




 6public function attachments(): array




 7{




 8    return [




 9        Attachment::fromStorageDisk('s3', '/path/to/file')




10            ->as('name.pdf')




11            ->withMime('application/pdf'),




12    ];




13}




/**
 * Get the attachments for the message.
 *
 * @return array<int, \Illuminate\Mail\Mailables\Attachment>
 */
public function attachments(): array
{
    return [
        Attachment::fromStorageDisk('s3', '/path/to/file')
            ->as('name.pdf')
            ->withMime('application/pdf'),
    ];
}

```

#### [Raw Data Attachments](https://laravel.com/docs/12.x/mail#raw-data-attachments)
The `fromData` attachment method may be used to attach a raw string of bytes as an attachment. For example, you might use this method if you have generated a PDF in memory and want to attach it to the email without writing it to disk. The `fromData` method accepts a closure which resolves the raw data bytes as well as the name that the attachment should be assigned:
```


 1/**




 2 * Get the attachments for the message.




 3 *




 4 * @return array<int, \Illuminate\Mail\Mailables\Attachment>




 5 */




 6public function attachments(): array




 7{




 8    return [




 9        Attachment::fromData(fn () => $this->pdf, 'Report.pdf')




10            ->withMime('application/pdf'),




11    ];




12}




/**
 * Get the attachments for the message.
 *
 * @return array<int, \Illuminate\Mail\Mailables\Attachment>
 */
public function attachments(): array
{
    return [
        Attachment::fromData(fn () => $this->pdf, 'Report.pdf')
            ->withMime('application/pdf'),
    ];
}

```

### [Inline Attachments](https://laravel.com/docs/12.x/mail#inline-attachments)
Embedding inline images into your emails is typically cumbersome; however, Laravel provides a convenient way to attach images to your emails. To embed an inline image, use the `embed` method on the `$message` variable within your email template. Laravel automatically makes the `$message` variable available to all of your email templates, so you don't need to worry about passing it in manually:
```


1<body>




2    Here is an image:




3 



4    <img src="{{ $message->embed($pathToImage) }}">




5</body>




<body>
    Here is an image:

    <img src="{{ $message->embed($pathToImage) }}">
</body>

```

The `$message` variable is not available in plain-text message templates since plain-text messages do not utilize inline attachments.
#### [Embedding Raw Data Attachments](https://laravel.com/docs/12.x/mail#embedding-raw-data-attachments)
If you already have a raw image data string you wish to embed into an email template, you may call the `embedData` method on the `$message` variable. When calling the `embedData` method, you will need to provide a filename that should be assigned to the embedded image:
```


1<body>




2    Here is an image from raw data:




3 



4    <img src="{{ $message->embedData($data, 'example-image.jpg') }}">




5</body>




<body>
    Here is an image from raw data:

    <img src="{{ $message->embedData($data, 'example-image.jpg') }}">
</body>

```

### [Attachable Objects](https://laravel.com/docs/12.x/mail#attachable-objects)
While attaching files to messages via simple string paths is often sufficient, in many cases the attachable entities within your application are represented by classes. For example, if your application is attaching a photo to a message, your application may also have a `Photo` model that represents that photo. When that is the case, wouldn't it be convenient to simply pass the `Photo` model to the `attach` method? Attachable objects allow you to do just that.
To get started, implement the `Illuminate\Contracts\Mail\Attachable` interface on the object that will be attachable to messages. This interface dictates that your class defines a `toMailAttachment` method that returns an `Illuminate\Mail\Attachment` instance:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Contracts\Mail\Attachable;




 6use Illuminate\Database\Eloquent\Model;




 7use Illuminate\Mail\Attachment;




 8 



 9class Photo extends Model implements Attachable




10{




11    /**




12     * Get the attachable representation of the model.




13     */




14    public function toMailAttachment(): Attachment




15    {




16        return Attachment::fromPath('/path/to/file');




17    }




18}




<?php

namespace App\Models;

use Illuminate\Contracts\Mail\Attachable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Mail\Attachment;

class Photo extends Model implements Attachable
{
    /**
     * Get the attachable representation of the model.
     */
    public function toMailAttachment(): Attachment
    {
        return Attachment::fromPath('/path/to/file');
    }
}

```

Once you have defined your attachable object, you may return an instance of that object from the `attachments` method when building an email message:
```


1/**




2 * Get the attachments for the message.




3 *




4 * @return array<int, \Illuminate\Mail\Mailables\Attachment>




5 */




6public function attachments(): array




7{




8    return [$this->photo];




9}




/**
 * Get the attachments for the message.
 *
 * @return array<int, \Illuminate\Mail\Mailables\Attachment>
 */
public function attachments(): array
{
    return [$this->photo];
}

```

Of course, attachment data may be stored on a remote file storage service such as Amazon S3. So, Laravel also allows you to generate attachment instances from data that is stored on one of your application's [filesystem disks](https://laravel.com/docs/12.x/filesystem):
```


1// Create an attachment from a file on your default disk...




2return Attachment::fromStorage($this->path);




3 



4// Create an attachment from a file on a specific disk...




5return Attachment::fromStorageDisk('backblaze', $this->path);




// Create an attachment from a file on your default disk...
return Attachment::fromStorage($this->path);

// Create an attachment from a file on a specific disk...
return Attachment::fromStorageDisk('backblaze', $this->path);

```

In addition, you may create attachment instances via data that you have in memory. To accomplish this, provide a closure to the `fromData` method. The closure should return the raw data that represents the attachment:
```


1return Attachment::fromData(fn () => $this->content, 'Photo Name');




return Attachment::fromData(fn () => $this->content, 'Photo Name');

```

Laravel also provides additional methods that you may use to customize your attachments. For example, you may use the `as` and `withMime` methods to customize the file's name and MIME type:
```


1return Attachment::fromPath('/path/to/file')




2    ->as('Photo Name')




3    ->withMime('image/jpeg');




return Attachment::fromPath('/path/to/file')
    ->as('Photo Name')
    ->withMime('image/jpeg');

```

### [Headers](https://laravel.com/docs/12.x/mail#headers)
Sometimes you may need to attach additional headers to the outgoing message. For instance, you may need to set a custom `Message-Id` or other arbitrary text headers.
To accomplish this, define a `headers` method on your mailable. The `headers` method should return an `Illuminate\Mail\Mailables\Headers` instance. This class accepts `messageId`, `references`, and `text` parameters. Of course, you may provide only the parameters you need for your particular message:
```


 1use Illuminate\Mail\Mailables\Headers;




 2 



 3/**




 4 * Get the message headers.




 5 */




 6public function headers(): Headers




 7{




 8    return new Headers(




 9        messageId: 'custom-message-id@example.com',




10        references: ['previous-message@example.com'],




11        text: [




12            'X-Custom-Header' => 'Custom Value',




13        ],




14    );




15}




use Illuminate\Mail\Mailables\Headers;

/**
 * Get the message headers.
 */
public function headers(): Headers
{
    return new Headers(
        messageId: 'custom-message-id@example.com',
        references: ['previous-message@example.com'],
        text: [
            'X-Custom-Header' => 'Custom Value',
        ],
    );
}

```

### [Tags and Metadata](https://laravel.com/docs/12.x/mail#tags-and-metadata)
Some third-party email providers such as Mailgun and Postmark support message "tags" and "metadata", which may be used to group and track emails sent by your application. You may add tags and metadata to an email message via your `Envelope` definition:
```


 1use Illuminate\Mail\Mailables\Envelope;




 2 



 3/**




 4 * Get the message envelope.




 5 *




 6 * @return \Illuminate\Mail\Mailables\Envelope




 7 */




 8public function envelope(): Envelope




 9{




10    return new Envelope(




11        subject: 'Order Shipped',




12        tags: ['shipment'],




13        metadata: [




14            'order_id' => $this->order->id,




15        ],




16    );




17}




use Illuminate\Mail\Mailables\Envelope;

/**
 * Get the message envelope.
 *
 * @return \Illuminate\Mail\Mailables\Envelope
 */
public function envelope(): Envelope
{
    return new Envelope(
        subject: 'Order Shipped',
        tags: ['shipment'],
        metadata: [
            'order_id' => $this->order->id,
        ],
    );
}

```

If your application is using the Mailgun driver, you may consult Mailgun's documentation for more information on
If your application is using Amazon SES to send emails, you should use the `metadata` method to attach
### [Customizing the Symfony Message](https://laravel.com/docs/12.x/mail#customizing-the-symfony-message)
Laravel's mail capabilities are powered by Symfony Mailer. Laravel allows you to register custom callbacks that will be invoked with the Symfony Message instance before sending the message. This gives you an opportunity to deeply customize the message before it is sent. To accomplish this, define a `using` parameter on your `Envelope` definition:
```


 1use Illuminate\Mail\Mailables\Envelope;




 2use Symfony\Component\Mime\Email;




 3 



 4/**




 5 * Get the message envelope.




 6 */




 7public function envelope(): Envelope




 8{




 9    return new Envelope(




10        subject: 'Order Shipped',




11        using: [




12            function (Email $message) {




13                // ...




14            },




15        ]




16    );




17}




use Illuminate\Mail\Mailables\Envelope;
use Symfony\Component\Mime\Email;

/**
 * Get the message envelope.
 */
public function envelope(): Envelope
{
    return new Envelope(
        subject: 'Order Shipped',
        using: [
            function (Email $message) {
                // ...
            },
        ]
    );
}

```
