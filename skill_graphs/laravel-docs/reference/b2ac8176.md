## [Mail and Local Development](https://laravel.com/docs/12.x/mail#mail-and-local-development)
When developing an application that sends email, you probably don't want to actually send emails to live email addresses. Laravel provides several ways to "disable" the actual sending of emails during local development.
#### [Log Driver](https://laravel.com/docs/12.x/mail#log-driver)
Instead of sending your emails, the `log` mail driver will write all email messages to your log files for inspection. Typically, this driver would only be used during local development. For more information on configuring your application per environment, check out the [configuration documentation](https://laravel.com/docs/12.x/configuration#environment-configuration).
#### [HELO / Mailtrap / Mailpit](https://laravel.com/docs/12.x/mail#mailtrap)
Alternatively, you may use a service like `smtp` driver to send your email messages to a "dummy" mailbox where you may view them in a true email client. This approach has the benefit of allowing you to actually inspect the final emails in Mailtrap's message viewer.
If you are using [Laravel Sail](https://laravel.com/docs/12.x/sail), you may preview your messages using `http://localhost:8025`.
#### [Using a Global `to` Address](https://laravel.com/docs/12.x/mail#using-a-global-to-address)
Finally, you may specify a global "to" address by invoking the `alwaysTo` method offered by the `Mail` facade. Typically, this method should be called from the `boot` method of one of your application's service providers:
```


 1use Illuminate\Support\Facades\Mail;




 2 



 3/**




 4 * Bootstrap any application services.




 5 */




 6public function boot(): void




 7{




 8    if ($this->app->environment('local')) {




 9        Mail::alwaysTo('taylor@example.com');




10    }




11}




use Illuminate\Support\Facades\Mail;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    if ($this->app->environment('local')) {
        Mail::alwaysTo('taylor@example.com');
    }
}

```

When using the `alwaysTo` method, any additional "cc" or "bcc" addresses on mail messages will be removed.
