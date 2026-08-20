## [Markdown Mail Notifications](https://laravel.com/docs/12.x/notifications#markdown-mail-notifications)
Markdown mail notifications allow you to take advantage of the pre-built templates of mail notifications, while giving you more freedom to write longer, customized messages. Since the messages are written in Markdown, Laravel is able to render beautiful, responsive HTML templates for the messages while also automatically generating a plain-text counterpart.
### [Generating the Message](https://laravel.com/docs/12.x/notifications#generating-the-message)
To generate a notification with a corresponding Markdown template, you may use the `--markdown` option of the `make:notification` Artisan command:
```


1php artisan make:notification InvoicePaid --markdown=mail.invoice.paid




php artisan make:notification InvoicePaid --markdown=mail.invoice.paid

```

Like all other mail notifications, notifications that use Markdown templates should define a `toMail` method on their notification class. However, instead of using the `line` and `action` methods to construct the notification, use the `markdown` method to specify the name of the Markdown template that should be used. An array of data you wish to make available to the template may be passed as the method's second argument:
```


 1/**




 2 * Get the mail representation of the notification.




 3 */




 4public function toMail(object $notifiable): MailMessage




 5{




 6    $url = url('/invoice/'.$this->invoice->id);




 7 



 8    return (new MailMessage)




 9        ->subject('Invoice Paid')




10        ->markdown('mail.invoice.paid', ['url' => $url]);




11}




/**
 * Get the mail representation of the notification.
 */
public function toMail(object $notifiable): MailMessage
{
    $url = url('/invoice/'.$this->invoice->id);

    return (new MailMessage)
        ->subject('Invoice Paid')
        ->markdown('mail.invoice.paid', ['url' => $url]);
}

```

### [Writing the Message](https://laravel.com/docs/12.x/notifications#writing-the-message)
Markdown mail notifications use a combination of Blade components and Markdown syntax which allow you to easily construct notifications while leveraging Laravel's pre-crafted notification components:
```


 1<x-mail::message>




 2# Invoice Paid




 3 



 4Your invoice has been paid!




 5 



 6<x-mail::button :url="$url">




 7View Invoice




 8</x-mail::button>




 9 



10Thanks,<br>




11{{ config('app.name') }}




12</x-mail::message>




<x-mail::message>
# Invoice Paid

Your invoice has been paid!

<x-mail::button :url="$url">
View Invoice
</x-mail::button>

Thanks,<br>
{{ config('app.name') }}
</x-mail::message>

```

Do not use excess indentation when writing Markdown emails. Per Markdown standards, Markdown parsers will render indented content as code blocks.
#### [Button Component](https://laravel.com/docs/12.x/notifications#button-component)
The button component renders a centered button link. The component accepts two arguments, a `url` and an optional `color`. Supported colors are `primary`, `green`, and `red`. You may add as many button components to a notification as you wish:
```


1<x-mail::button :url="$url" color="green">




2View Invoice




3</x-mail::button>




<x-mail::button :url="$url" color="green">
View Invoice
</x-mail::button>

```

#### [Panel Component](https://laravel.com/docs/12.x/notifications#panel-component)
The panel component renders the given block of text in a panel that has a slightly different background color than the rest of the notification. This allows you to draw attention to a given block of text:
```


1<x-mail::panel>




2This is the panel content.




3</x-mail::panel>




<x-mail::panel>
This is the panel content.
</x-mail::panel>

```

#### [Table Component](https://laravel.com/docs/12.x/notifications#table-component)
The table component allows you to transform a Markdown table into an HTML table. The component accepts the Markdown table as its content. Table column alignment is supported using the default Markdown table alignment syntax:
```


1<x-mail::table>




2| Laravel       | Table         | Example       |




3| ------------- | :-----------: | ------------: |




4| Col 2 is      | Centered      | $10           |




5| Col 3 is      | Right-Aligned | $20           |




6</x-mail::table>




<x-mail::table>
| Laravel       | Table         | Example       |
| ------------- | :-----------: | ------------: |
| Col 2 is      | Centered      | $10           |
| Col 3 is      | Right-Aligned | $20           |
</x-mail::table>

```

### [Customizing the Components](https://laravel.com/docs/12.x/notifications#customizing-the-components)
You may export all of the Markdown notification components to your own application for customization. To export the components, use the `vendor:publish` Artisan command to publish the `laravel-mail` asset tag:
```


1php artisan vendor:publish --tag=laravel-mail




php artisan vendor:publish --tag=laravel-mail

```

This command will publish the Markdown mail components to the `resources/views/vendor/mail` directory. The `mail` directory will contain an `html` and a `text` directory, each containing their respective representations of every available component. You are free to customize these components however you like.
#### [Customizing the CSS](https://laravel.com/docs/12.x/notifications#customizing-the-css)
After exporting the components, the `resources/views/vendor/mail/html/themes` directory will contain a `default.css` file. You may customize the CSS in this file and your styles will automatically be in-lined within the HTML representations of your Markdown notifications.
If you would like to build an entirely new theme for Laravel's Markdown components, you may place a CSS file within the `html/themes` directory. After naming and saving your CSS file, update the `theme` option of the `mail` configuration file to match the name of your new theme.
To customize the theme for an individual notification, you may call the `theme` method while building the notification's mail message. The `theme` method accepts the name of the theme that should be used when sending the notification:
```


 1/**




 2 * Get the mail representation of the notification.




 3 */




 4public function toMail(object $notifiable): MailMessage




 5{




 6    return (new MailMessage)




 7        ->theme('invoice')




 8        ->subject('Invoice Paid')




 9        ->markdown('mail.invoice.paid', ['url' => $url]);




10}




/**
 * Get the mail representation of the notification.
 */
public function toMail(object $notifiable): MailMessage
{
    return (new MailMessage)
        ->theme('invoice')
        ->subject('Invoice Paid')
        ->markdown('mail.invoice.paid', ['url' => $url]);
}

```
