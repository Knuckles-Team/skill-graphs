## [Markdown Mailables](https://laravel.com/docs/12.x/mail#markdown-mailables)
Markdown mailable messages allow you to take advantage of the pre-built templates and components of [mail notifications](https://laravel.com/docs/12.x/notifications#mail-notifications) in your mailables. Since the messages are written in Markdown, Laravel is able to render beautiful, responsive HTML templates for the messages while also automatically generating a plain-text counterpart.
### [Generating Markdown Mailables](https://laravel.com/docs/12.x/mail#generating-markdown-mailables)
To generate a mailable with a corresponding Markdown template, you may use the `--markdown` option of the `make:mail` Artisan command:
```


1php artisan make:mail OrderShipped --markdown=mail.orders.shipped




php artisan make:mail OrderShipped --markdown=mail.orders.shipped

```

Then, when configuring the mailable `Content` definition within its `content` method, use the `markdown` parameter instead of the `view` parameter:
```


 1use Illuminate\Mail\Mailables\Content;




 2 



 3/**




 4 * Get the message content definition.




 5 */




 6public function content(): Content




 7{




 8    return new Content(




 9        markdown: 'mail.orders.shipped',




10        with: [




11            'url' => $this->orderUrl,




12        ],




13    );




14}




use Illuminate\Mail\Mailables\Content;

/**
 * Get the message content definition.
 */
public function content(): Content
{
    return new Content(
        markdown: 'mail.orders.shipped',
        with: [
            'url' => $this->orderUrl,
        ],
    );
}

```

### [Writing Markdown Messages](https://laravel.com/docs/12.x/mail#writing-markdown-messages)
Markdown mailables use a combination of Blade components and Markdown syntax which allow you to easily construct mail messages while leveraging Laravel's pre-built email UI components:
```


 1<x-mail::message>




 2# Order Shipped




 3 



 4Your order has been shipped!




 5 



 6<x-mail::button :url="$url">




 7View Order




 8</x-mail::button>




 9 



10Thanks,<br>




11{{ config('app.name') }}




12</x-mail::message>




<x-mail::message>
# Order Shipped

Your order has been shipped!

<x-mail::button :url="$url">
View Order
</x-mail::button>

Thanks,<br>
{{ config('app.name') }}
</x-mail::message>

```

Do not use excess indentation when writing Markdown emails. Per Markdown standards, Markdown parsers will render indented content as code blocks.
#### [Button Component](https://laravel.com/docs/12.x/mail#button-component)
The button component renders a centered button link. The component accepts two arguments, a `url` and an optional `color`. Supported colors are `primary`, `success`, and `error`. You may add as many button components to a message as you wish:
```


1<x-mail::button :url="$url" color="success">




2View Order




3</x-mail::button>




<x-mail::button :url="$url" color="success">
View Order
</x-mail::button>

```

#### [Panel Component](https://laravel.com/docs/12.x/mail#panel-component)
The panel component renders the given block of text in a panel that has a slightly different background color than the rest of the message. This allows you to draw attention to a given block of text:
```


1<x-mail::panel>




2This is the panel content.




3</x-mail::panel>




<x-mail::panel>
This is the panel content.
</x-mail::panel>

```

#### [Table Component](https://laravel.com/docs/12.x/mail#table-component)
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

### [Customizing the Components](https://laravel.com/docs/12.x/mail#customizing-the-components)
You may export all of the Markdown mail components to your own application for customization. To export the components, use the `vendor:publish` Artisan command to publish the `laravel-mail` asset tag:
```


1php artisan vendor:publish --tag=laravel-mail




php artisan vendor:publish --tag=laravel-mail

```

This command will publish the Markdown mail components to the `resources/views/vendor/mail` directory. The `mail` directory will contain an `html` and a `text` directory, each containing their respective representations of every available component. You are free to customize these components however you like.
#### [Customizing the CSS](https://laravel.com/docs/12.x/mail#customizing-the-css)
After exporting the components, the `resources/views/vendor/mail/html/themes` directory will contain a `default.css` file. You may customize the CSS in this file and your styles will automatically be converted to inline CSS styles within the HTML representations of your Markdown mail messages.
If you would like to build an entirely new theme for Laravel's Markdown components, you may place a CSS file within the `html/themes` directory. After naming and saving your CSS file, update the `theme` option of your application's `config/mail.php` configuration file to match the name of your new theme.
To customize the theme for an individual mailable, you may set the `$theme` property of the mailable class to the name of the theme that should be used when sending that mailable.
