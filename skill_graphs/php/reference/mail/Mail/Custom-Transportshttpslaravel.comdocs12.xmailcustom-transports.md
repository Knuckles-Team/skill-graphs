## [Custom Transports](https://laravel.com/docs/12.x/mail#custom-transports)
Laravel includes a variety of mail transports; however, you may wish to write your own transports to deliver email via other services that Laravel does not support out of the box. To get started, define a class that extends the `Symfony\Component\Mailer\Transport\AbstractTransport` class. Then, implement the `doSend` and `__toString` methods on your transport:
```


 1<?php




 2 



 3namespace App\Mail;




 4 



 5use MailchimpTransactional\ApiClient;




 6use Symfony\Component\Mailer\SentMessage;




 7use Symfony\Component\Mailer\Transport\AbstractTransport;




 8use Symfony\Component\Mime\Address;




 9use Symfony\Component\Mime\MessageConverter;




10 



11class MailchimpTransport extends AbstractTransport




12{




13    /**




14     * Create a new Mailchimp transport instance.




15     */




16    public function __construct(




17        protected ApiClient $client,




18    ) {




19        parent::__construct();




20    }




21 



22    /**




23     * {@inheritDoc}




24     */




25    protected function doSend(SentMessage $message): void




26    {




27        $email = MessageConverter::toEmail($message->getOriginalMessage());




28 



29        $this->client->messages->send(['message' => [




30            'from_email' => $email->getFrom(),




31            'to' => collect($email->getTo())->map(function (Address $email) {




32                return ['email' => $email->getAddress(), 'type' => 'to'];




33            })->all(),




34            'subject' => $email->getSubject(),




35            'text' => $email->getTextBody(),




36        ]]);




37    }




38 



39    /**




40     * Get the string representation of the transport.




41     */




42    public function __toString(): string




43    {




44        return 'mailchimp';




45    }




46}




<?php

namespace App\Mail;

use MailchimpTransactional\ApiClient;
use Symfony\Component\Mailer\SentMessage;
use Symfony\Component\Mailer\Transport\AbstractTransport;
use Symfony\Component\Mime\Address;
use Symfony\Component\Mime\MessageConverter;

class MailchimpTransport extends AbstractTransport
{
    /**
     * Create a new Mailchimp transport instance.
     */
    public function __construct(
        protected ApiClient $client,
    ) {
        parent::__construct();
    }

    /**
     * {@inheritDoc}
     */
    protected function doSend(SentMessage $message): void
    {
        $email = MessageConverter::toEmail($message->getOriginalMessage());

        $this->client->messages->send(['message' => [
            'from_email' => $email->getFrom(),
            'to' => collect($email->getTo())->map(function (Address $email) {
                return ['email' => $email->getAddress(), 'type' => 'to'];
            })->all(),
            'subject' => $email->getSubject(),
            'text' => $email->getTextBody(),
        ]]);
    }

    /**
     * Get the string representation of the transport.
     */
    public function __toString(): string
    {
        return 'mailchimp';
    }
}

```

Once you've defined your custom transport, you may register it via the `extend` method provided by the `Mail` facade. Typically, this should be done within the `boot` method of your application's `AppServiceProvider`. A `$config` argument will be passed to the closure provided to the `extend` method. This argument will contain the configuration array defined for the mailer in the application's `config/mail.php` configuration file:
```


 1use App\Mail\MailchimpTransport;




 2use Illuminate\Support\Facades\Mail;




 3use MailchimpTransactional\ApiClient;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    Mail::extend('mailchimp', function (array $config = []) {




11        $client = new ApiClient;




12 



13        $client->setApiKey($config['key']);




14 



15        return new MailchimpTransport($client);




16    });




17}




use App\Mail\MailchimpTransport;
use Illuminate\Support\Facades\Mail;
use MailchimpTransactional\ApiClient;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Mail::extend('mailchimp', function (array $config = []) {
        $client = new ApiClient;

        $client->setApiKey($config['key']);

        return new MailchimpTransport($client);
    });
}

```

Once your custom transport has been defined and registered, you may create a mailer definition within your application's `config/mail.php` configuration file that utilizes the new transport:
```


1'mailchimp' => [




2    'transport' => 'mailchimp',




3    'key' => env('MAILCHIMP_API_KEY'),




4    // ...




5],




'mailchimp' => [
    'transport' => 'mailchimp',
    'key' => env('MAILCHIMP_API_KEY'),
    // ...
],

```

### [Additional Symfony Transports](https://laravel.com/docs/12.x/mail#additional-symfony-transports)
Laravel includes support for some existing Symfony maintained mail transports like Mailgun and Postmark. However, you may wish to extend Laravel with support for additional Symfony maintained transports. You can do so by requiring the necessary Symfony mailer via Composer and registering the transport with Laravel. For example, you may install and register the "Brevo" (formerly "Sendinblue") Symfony mailer:
```


1composer require symfony/brevo-mailer symfony/http-client




composer require symfony/brevo-mailer symfony/http-client

```

Once the Brevo mailer package has been installed, you may add an entry for your Brevo API credentials to your application's `services` configuration file:
```


1'brevo' => [




2    'key' => env('BREVO_API_KEY'),




3],




'brevo' => [
    'key' => env('BREVO_API_KEY'),
],

```

Next, you may use the `Mail` facade's `extend` method to register the transport with Laravel. Typically, this should be done within the `boot` method of a service provider:
```


 1use Illuminate\Support\Facades\Mail;




 2use Symfony\Component\Mailer\Bridge\Brevo\Transport\BrevoTransportFactory;




 3use Symfony\Component\Mailer\Transport\Dsn;




 4 



 5/**




 6 * Bootstrap any application services.




 7 */




 8public function boot(): void




 9{




10    Mail::extend('brevo', function () {




11        return (new BrevoTransportFactory)->create(




12            new Dsn(




13                'brevo+api',




14                'default',




15                config('services.brevo.key')




16            )




17        );




18    });




19}




use Illuminate\Support\Facades\Mail;
use Symfony\Component\Mailer\Bridge\Brevo\Transport\BrevoTransportFactory;
use Symfony\Component\Mailer\Transport\Dsn;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Mail::extend('brevo', function () {
        return (new BrevoTransportFactory)->create(
            new Dsn(
                'brevo+api',
                'default',
                config('services.brevo.key')
            )
        );
    });
}

```

Once your transport has been registered, you may create a mailer definition within your application's `config/mail.php` configuration file that utilizes the new transport:
```


1'brevo' => [




2    'transport' => 'brevo',




3    // ...




4],




'brevo' => [
    'transport' => 'brevo',
    // ...
],

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/mail#introduction)
    * [ Configuration ](https://laravel.com/docs/12.x/mail#configuration)
    * [ Driver Prerequisites ](https://laravel.com/docs/12.x/mail#driver-prerequisites)
    * [ Failover Configuration ](https://laravel.com/docs/12.x/mail#failover-configuration)
    * [ Round Robin Configuration ](https://laravel.com/docs/12.x/mail#round-robin-configuration)
  * [ Generating Mailables ](https://laravel.com/docs/12.x/mail#generating-mailables)
  * [ Writing Mailables ](https://laravel.com/docs/12.x/mail#writing-mailables)
    * [ Configuring the Sender ](https://laravel.com/docs/12.x/mail#configuring-the-sender)
    * [ Configuring the View ](https://laravel.com/docs/12.x/mail#configuring-the-view)
    * [ View Data ](https://laravel.com/docs/12.x/mail#view-data)
    * [ Attachments ](https://laravel.com/docs/12.x/mail#attachments)
    * [ Inline Attachments ](https://laravel.com/docs/12.x/mail#inline-attachments)
    * [ Attachable Objects ](https://laravel.com/docs/12.x/mail#attachable-objects)
    * [ Headers ](https://laravel.com/docs/12.x/mail#headers)
    * [ Tags and Metadata ](https://laravel.com/docs/12.x/mail#tags-and-metadata)
    * [ Customizing the Symfony Message ](https://laravel.com/docs/12.x/mail#customizing-the-symfony-message)
  * [ Markdown Mailables ](https://laravel.com/docs/12.x/mail#markdown-mailables)
    * [ Generating Markdown Mailables ](https://laravel.com/docs/12.x/mail#generating-markdown-mailables)
    * [ Writing Markdown Messages ](https://laravel.com/docs/12.x/mail#writing-markdown-messages)
    * [ Customizing the Components ](https://laravel.com/docs/12.x/mail#customizing-the-components)
  * [ Sending Mail ](https://laravel.com/docs/12.x/mail#sending-mail)
    * [ Queueing Mail ](https://laravel.com/docs/12.x/mail#queueing-mail)
  * [ Rendering Mailables ](https://laravel.com/docs/12.x/mail#rendering-mailables)
    * [ Previewing Mailables in the Browser ](https://laravel.com/docs/12.x/mail#previewing-mailables-in-the-browser)
  * [ Localizing Mailables ](https://laravel.com/docs/12.x/mail#localizing-mailables)
  * [ Testing ](https://laravel.com/docs/12.x/mail#testing-mailables)
    * [ Testing Mailable Content ](https://laravel.com/docs/12.x/mail#testing-mailable-content)
    * [ Testing Mailable Sending ](https://laravel.com/docs/12.x/mail#testing-mailable-sending)
  * [ Mail and Local Development ](https://laravel.com/docs/12.x/mail#mail-and-local-development)
  * [ Events ](https://laravel.com/docs/12.x/mail#events)
  * [ Custom Transports ](https://laravel.com/docs/12.x/mail#custom-transports)
    * [ Additional Symfony Transports ](https://laravel.com/docs/12.x/mail#additional-symfony-transports)


[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [ More Partners ](https://partners.laravel.com)
