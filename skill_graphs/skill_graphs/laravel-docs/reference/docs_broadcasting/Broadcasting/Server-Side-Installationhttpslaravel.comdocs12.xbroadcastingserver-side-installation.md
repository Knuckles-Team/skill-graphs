## [Server Side Installation](https://laravel.com/docs/12.x/broadcasting#server-side-installation)
To get started using Laravel's event broadcasting, we need to do some configuration within the Laravel application as well as install a few packages.
Event broadcasting is accomplished by a server-side broadcasting driver that broadcasts your Laravel events so that Laravel Echo (a JavaScript library) can receive them within the browser client. Don't worry - we'll walk through each part of the installation process step-by-step.
### [Reverb](https://laravel.com/docs/12.x/broadcasting#reverb)
To quickly enable support for Laravel's broadcasting features while using Reverb as your event broadcaster, invoke the `install:broadcasting` Artisan command with the `--reverb` option. This Artisan command will install Reverb's required Composer and NPM packages and update your application's `.env` file with the appropriate variables:
```


1php artisan install:broadcasting --reverb




php artisan install:broadcasting --reverb

```

#### [Manual Installation](https://laravel.com/docs/12.x/broadcasting#reverb-manual-installation)
When running the `install:broadcasting` command, you will be prompted to install [Laravel Reverb](https://laravel.com/docs/12.x/reverb). Of course, you may also install Reverb manually using the Composer package manager:
```


1composer require laravel/reverb




composer require laravel/reverb

```

Once the package is installed, you may run Reverb's installation command to publish the configuration, add Reverb's required environment variables, and enable event broadcasting in your application:
```


1php artisan reverb:install




php artisan reverb:install

```

You can find detailed Reverb installation and usage instructions in the [Reverb documentation](https://laravel.com/docs/12.x/reverb).
### [Pusher Channels](https://laravel.com/docs/12.x/broadcasting#pusher-channels)
To quickly enable support for Laravel's broadcasting features while using Pusher as your event broadcaster, invoke the `install:broadcasting` Artisan command with the `--pusher` option. This Artisan command will prompt you for your Pusher credentials, install the Pusher PHP and JavaScript SDKs, and update your application's `.env` file with the appropriate variables:
```


1php artisan install:broadcasting --pusher




php artisan install:broadcasting --pusher

```

#### [Manual Installation](https://laravel.com/docs/12.x/broadcasting#pusher-manual-installation)
To install Pusher support manually, you should install the Pusher Channels PHP SDK using the Composer package manager:
```


1composer require pusher/pusher-php-server




composer require pusher/pusher-php-server

```

Next, you should configure your Pusher Channels credentials in the `config/broadcasting.php` configuration file. An example Pusher Channels configuration is already included in this file, allowing you to quickly specify your key, secret, and application ID. Typically, you should configure your Pusher Channels credentials in your application's `.env` file:
```


1PUSHER_APP_ID="your-pusher-app-id"




2PUSHER_APP_KEY="your-pusher-key"




3PUSHER_APP_SECRET="your-pusher-secret"




4PUSHER_HOST=




5PUSHER_PORT=443




6PUSHER_SCHEME="https"




7PUSHER_APP_CLUSTER="mt1"




PUSHER_APP_ID="your-pusher-app-id"
PUSHER_APP_KEY="your-pusher-key"
PUSHER_APP_SECRET="your-pusher-secret"
PUSHER_HOST=
PUSHER_PORT=443
PUSHER_SCHEME="https"
PUSHER_APP_CLUSTER="mt1"

```

The `config/broadcasting.php` file's `pusher` configuration also allows you to specify additional `options` that are supported by Channels, such as the cluster.
Then, set the `BROADCAST_CONNECTION` environment variable to `pusher` in your application's `.env` file:
```


1BROADCAST_CONNECTION=pusher




BROADCAST_CONNECTION=pusher

```

Finally, you are ready to install and configure [Laravel Echo](https://laravel.com/docs/12.x/broadcasting#client-side-installation), which will receive the broadcast events on the client-side.
### [Ably](https://laravel.com/docs/12.x/broadcasting#ably)
The documentation below discusses how to use Ably in "Pusher compatibility" mode. However, the Ably team recommends and maintains a broadcaster and Echo client that is able to take advantage of the unique capabilities offered by Ably. For more information on using the Ably maintained drivers, please
To quickly enable support for Laravel's broadcasting features while using `install:broadcasting` Artisan command with the `--ably` option. This Artisan command will prompt you for your Ably credentials, install the Ably PHP and JavaScript SDKs, and update your application's `.env` file with the appropriate variables:
```


1php artisan install:broadcasting --ably




php artisan install:broadcasting --ably

```

**Before continuing, you should enable Pusher protocol support in your Ably application settings. You may enable this feature within the "Protocol Adapter Settings" portion of your Ably application's settings dashboard.**
#### [Manual Installation](https://laravel.com/docs/12.x/broadcasting#ably-manual-installation)
To install Ably support manually, you should install the Ably PHP SDK using the Composer package manager:
```


1composer require ably/ably-php




composer require ably/ably-php

```

Next, you should configure your Ably credentials in the `config/broadcasting.php` configuration file. An example Ably configuration is already included in this file, allowing you to quickly specify your key. Typically, this value should be set via the `ABLY_KEY` [environment variable](https://laravel.com/docs/12.x/configuration#environment-configuration):
```


1ABLY_KEY=your-ably-key




ABLY_KEY=your-ably-key

```

Then, set the `BROADCAST_CONNECTION` environment variable to `ably` in your application's `.env` file:
```


1BROADCAST_CONNECTION=ably




BROADCAST_CONNECTION=ably

```

Finally, you are ready to install and configure [Laravel Echo](https://laravel.com/docs/12.x/broadcasting#client-side-installation), which will receive the broadcast events on the client-side.
