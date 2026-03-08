## [Introduction](https://laravel.com/docs/12.x/mail#introduction)
Sending email doesn't have to be complicated. Laravel provides a clean, simple email API powered by the popular `sendmail`, allowing you to quickly get started sending mail through a local or cloud-based service of your choice.
### [Configuration](https://laravel.com/docs/12.x/mail#configuration)
Laravel's email services may be configured via your application's `config/mail.php` configuration file. Each mailer configured within this file may have its own unique configuration and even its own unique "transport", allowing your application to use different email services to send certain email messages. For example, your application might use Postmark to send transactional emails while using Amazon SES to send bulk emails.
Within your `mail` configuration file, you will find a `mailers` configuration array. This array contains a sample configuration entry for each of the major mail drivers / transports supported by Laravel, while the `default` configuration value determines which mailer will be used by default when your application needs to send an email message.
### [Driver / Transport Prerequisites](https://laravel.com/docs/12.x/mail#driver-prerequisites)
The API based drivers such as Mailgun, Postmark, and Resend are often simpler and faster than sending mail via SMTP servers. Whenever possible, we recommend that you use one of these drivers.
#### [Mailgun Driver](https://laravel.com/docs/12.x/mail#mailgun-driver)
To use the Mailgun driver, install Symfony's Mailgun Mailer transport via Composer:
```


1composer require symfony/mailgun-mailer symfony/http-client




composer require symfony/mailgun-mailer symfony/http-client

```

Next, you will need to make two changes in your application's `config/mail.php` configuration file. First, set your default mailer to `mailgun`:
```


1'default' => env('MAIL_MAILER', 'mailgun'),




'default' => env('MAIL_MAILER', 'mailgun'),

```

Second, add the following configuration array to your array of `mailers`:
```


1'mailgun' => [




2    'transport' => 'mailgun',




3    // 'client' => [




4    //     'timeout' => 5,




5    // ],




6],




'mailgun' => [
    'transport' => 'mailgun',
    // 'client' => [
    //     'timeout' => 5,
    // ],
],

```

After configuring your application's default mailer, add the following options to your `config/services.php` configuration file:
```


1'mailgun' => [




2    'domain' => env('MAILGUN_DOMAIN'),




3    'secret' => env('MAILGUN_SECRET'),




4    'endpoint' => env('MAILGUN_ENDPOINT', 'api.mailgun.net'),




5    'scheme' => 'https',




6],




'mailgun' => [
    'domain' => env('MAILGUN_DOMAIN'),
    'secret' => env('MAILGUN_SECRET'),
    'endpoint' => env('MAILGUN_ENDPOINT', 'api.mailgun.net'),
    'scheme' => 'https',
],

```

If you are not using the United States `services` configuration file:
```


1'mailgun' => [




2    'domain' => env('MAILGUN_DOMAIN'),




3    'secret' => env('MAILGUN_SECRET'),




4    'endpoint' => env('MAILGUN_ENDPOINT', 'api.eu.mailgun.net'),




5    'scheme' => 'https',




6],




'mailgun' => [
    'domain' => env('MAILGUN_DOMAIN'),
    'secret' => env('MAILGUN_SECRET'),
    'endpoint' => env('MAILGUN_ENDPOINT', 'api.eu.mailgun.net'),
    'scheme' => 'https',
],

```

#### [Postmark Driver](https://laravel.com/docs/12.x/mail#postmark-driver)
To use the
```


1composer require symfony/postmark-mailer symfony/http-client




composer require symfony/postmark-mailer symfony/http-client

```

Next, set the `default` option in your application's `config/mail.php` configuration file to `postmark`. After configuring your application's default mailer, ensure that your `config/services.php` configuration file contains the following options:
```


1'postmark' => [




2    'key' => env('POSTMARK_API_KEY'),




3],




'postmark' => [
    'key' => env('POSTMARK_API_KEY'),
],

```

If you would like to specify the Postmark message stream that should be used by a given mailer, you may add the `message_stream_id` configuration option to the mailer's configuration array. This configuration array can be found in your application's `config/mail.php` configuration file:
```


1'postmark' => [




2    'transport' => 'postmark',




3    'message_stream_id' => env('POSTMARK_MESSAGE_STREAM_ID'),




4    // 'client' => [




5    //     'timeout' => 5,




6    // ],




7],




'postmark' => [
    'transport' => 'postmark',
    'message_stream_id' => env('POSTMARK_MESSAGE_STREAM_ID'),
    // 'client' => [
    //     'timeout' => 5,
    // ],
],

```

This way you are also able to set up multiple Postmark mailers with different message streams.
#### [Resend Driver](https://laravel.com/docs/12.x/mail#resend-driver)
To use the
```


1composer require resend/resend-php




composer require resend/resend-php

```

Next, set the `default` option in your application's `config/mail.php` configuration file to `resend`. After configuring your application's default mailer, ensure that your `config/services.php` configuration file contains the following options:
```


1'resend' => [




2    'key' => env('RESEND_API_KEY'),




3],




'resend' => [
    'key' => env('RESEND_API_KEY'),
],

```

#### [SES Driver](https://laravel.com/docs/12.x/mail#ses-driver)
To use the Amazon SES driver you must first install the Amazon AWS SDK for PHP. You may install this library via the Composer package manager:
```


1composer require aws/aws-sdk-php




composer require aws/aws-sdk-php

```

Next, set the `default` option in your `config/mail.php` configuration file to `ses` and verify that your `config/services.php` configuration file contains the following options:
```


1'ses' => [




2    'key' => env('AWS_ACCESS_KEY_ID'),




3    'secret' => env('AWS_SECRET_ACCESS_KEY'),




4    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),




5],




'ses' => [
    'key' => env('AWS_ACCESS_KEY_ID'),
    'secret' => env('AWS_SECRET_ACCESS_KEY'),
    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
],

```

To utilize AWS `token` key to your application's SES configuration:
```


1'ses' => [




2    'key' => env('AWS_ACCESS_KEY_ID'),




3    'secret' => env('AWS_SECRET_ACCESS_KEY'),




4    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),




5    'token' => env('AWS_SESSION_TOKEN'),




6],




'ses' => [
    'key' => env('AWS_ACCESS_KEY_ID'),
    'secret' => env('AWS_SECRET_ACCESS_KEY'),
    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
    'token' => env('AWS_SESSION_TOKEN'),
],

```

To interact with SES's `X-Ses-List-Management-Options` header in the array returned by the [headers](https://laravel.com/docs/12.x/mail#headers) method of a mail message:
```


 1/**




 2 * Get the message headers.




 3 */




 4public function headers(): Headers




 5{




 6    return new Headers(




 7        text: [




 8            'X-Ses-List-Management-Options' => 'contactListName=MyContactList;topicName=MyTopic',




 9        ],




10    );




11}




/**
 * Get the message headers.
 */
public function headers(): Headers
{
    return new Headers(
        text: [
            'X-Ses-List-Management-Options' => 'contactListName=MyContactList;topicName=MyTopic',
        ],
    );
}

```

If you would like to define `SendEmail` method when sending an email, you may define an `options` array within your `ses` configuration:
```


 1'ses' => [




 2    'key' => env('AWS_ACCESS_KEY_ID'),




 3    'secret' => env('AWS_SECRET_ACCESS_KEY'),




 4    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),




 5    'options' => [




 6        'ConfigurationSetName' => 'MyConfigurationSet',




 7        'EmailTags' => [




 8            ['Name' => 'foo', 'Value' => 'bar'],




 9        ],




10    ],




11],




'ses' => [
    'key' => env('AWS_ACCESS_KEY_ID'),
    'secret' => env('AWS_SECRET_ACCESS_KEY'),
    'region' => env('AWS_DEFAULT_REGION', 'us-east-1'),
    'options' => [
        'ConfigurationSetName' => 'MyConfigurationSet',
        'EmailTags' => [
            ['Name' => 'foo', 'Value' => 'bar'],
        ],
    ],
],

```

### [Failover Configuration](https://laravel.com/docs/12.x/mail#failover-configuration)
Sometimes, an external service you have configured to send your application's mail may be down. In these cases, it can be useful to define one or more backup mail delivery configurations that will be used in case your primary delivery driver is down.
To accomplish this, you should define a mailer within your application's `mail` configuration file that uses the `failover` transport. The configuration array for your application's `failover` mailer should contain an array of `mailers` that reference the order in which configured mailers should be chosen for delivery:
```


 1'mailers' => [




 2    'failover' => [




 3        'transport' => 'failover',




 4        'mailers' => [




 5            'postmark',




 6            'mailgun',




 7            'sendmail',




 8        ],




 9        'retry_after' => 60,




10    ],




11 



12    // ...




13],




'mailers' => [
    'failover' => [
        'transport' => 'failover',
        'mailers' => [
            'postmark',
            'mailgun',
            'sendmail',
        ],
        'retry_after' => 60,
    ],

    // ...
],

```

Once you have configured a mailer that uses the `failover` transport, you will need to set the failover mailer as your default mailer in your application's `.env` file to make use of the failover functionality:
```


1MAIL_MAILER=failover




MAIL_MAILER=failover

```

### [Round Robin Configuration](https://laravel.com/docs/12.x/mail#round-robin-configuration)
The `roundrobin` transport allows you to distribute your mailing workload across multiple mailers. To get started, define a mailer within your application's `mail` configuration file that uses the `roundrobin` transport. The configuration array for your application's `roundrobin` mailer should contain an array of `mailers` that reference which configured mailers should be used for delivery:
```


 1'mailers' => [




 2    'roundrobin' => [




 3        'transport' => 'roundrobin',




 4        'mailers' => [




 5            'ses',




 6            'postmark',




 7        ],




 8        'retry_after' => 60,




 9    ],




10 



11    // ...




12],




'mailers' => [
    'roundrobin' => [
        'transport' => 'roundrobin',
        'mailers' => [
            'ses',
            'postmark',
        ],
        'retry_after' => 60,
    ],

    // ...
],

```

Once your round robin mailer has been defined, you should set this mailer as the default mailer used by your application by specifying its name as the value of the `default` configuration key within your application's `mail` configuration file:
```


1'default' => env('MAIL_MAILER', 'roundrobin'),




'default' => env('MAIL_MAILER', 'roundrobin'),

```

The round robin transport selects a random mailer from the list of configured mailers and then switches to the next available mailer for each subsequent email. In contrast to `failover` transport, which helps to achieve `roundrobin` transport provides
