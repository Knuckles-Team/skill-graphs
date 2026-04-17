## [SMS Notifications](https://laravel.com/docs/12.x/notifications#sms-notifications)
### [Prerequisites](https://laravel.com/docs/12.x/notifications#sms-prerequisites)
Sending SMS notifications in Laravel is powered by `laravel/vonage-notification-channel` and `guzzlehttp/guzzle` packages:
```


1composer require laravel/vonage-notification-channel guzzlehttp/guzzle




composer require laravel/vonage-notification-channel guzzlehttp/guzzle

```

The package includes a `VONAGE_KEY` and `VONAGE_SECRET` environment variables to define your Vonage public and secret keys.
After defining your keys, you should set a `VONAGE_SMS_FROM` environment variable that defines the phone number that your SMS messages should be sent from by default. You may generate this phone number within the Vonage control panel:
```


1VONAGE_SMS_FROM=15556666666




VONAGE_SMS_FROM=15556666666

```

### [Formatting SMS Notifications](https://laravel.com/docs/12.x/notifications#formatting-sms-notifications)
If a notification supports being sent as an SMS, you should define a `toVonage` method on the notification class. This method will receive a `$notifiable` entity and should return an `Illuminate\Notifications\Messages\VonageMessage` instance:
```


 1use Illuminate\Notifications\Messages\VonageMessage;




 2 



 3/**




 4 * Get the Vonage / SMS representation of the notification.




 5 */




 6public function toVonage(object $notifiable): VonageMessage




 7{




 8    return (new VonageMessage)




 9        ->content('Your SMS message content');




10}




use Illuminate\Notifications\Messages\VonageMessage;

/**
 * Get the Vonage / SMS representation of the notification.
 */
public function toVonage(object $notifiable): VonageMessage
{
    return (new VonageMessage)
        ->content('Your SMS message content');
}

```

#### [Unicode Content](https://laravel.com/docs/12.x/notifications#unicode-content)
If your SMS message will contain unicode characters, you should call the `unicode` method when constructing the `VonageMessage` instance:
```


 1use Illuminate\Notifications\Messages\VonageMessage;




 2 



 3/**




 4 * Get the Vonage / SMS representation of the notification.




 5 */




 6public function toVonage(object $notifiable): VonageMessage




 7{




 8    return (new VonageMessage)




 9        ->content('Your unicode message')




10        ->unicode();




11}




use Illuminate\Notifications\Messages\VonageMessage;

/**
 * Get the Vonage / SMS representation of the notification.
 */
public function toVonage(object $notifiable): VonageMessage
{
    return (new VonageMessage)
        ->content('Your unicode message')
        ->unicode();
}

```

### [Customizing the "From" Number](https://laravel.com/docs/12.x/notifications#customizing-the-from-number)
If you would like to send some notifications from a phone number that is different from the phone number specified by your `VONAGE_SMS_FROM` environment variable, you may call the `from` method on a `VonageMessage` instance:
```


 1use Illuminate\Notifications\Messages\VonageMessage;




 2 



 3/**




 4 * Get the Vonage / SMS representation of the notification.




 5 */




 6public function toVonage(object $notifiable): VonageMessage




 7{




 8    return (new VonageMessage)




 9        ->content('Your SMS message content')




10        ->from('15554443333');




11}




use Illuminate\Notifications\Messages\VonageMessage;

/**
 * Get the Vonage / SMS representation of the notification.
 */
public function toVonage(object $notifiable): VonageMessage
{
    return (new VonageMessage)
        ->content('Your SMS message content')
        ->from('15554443333');
}

```

### [Adding a Client Reference](https://laravel.com/docs/12.x/notifications#adding-a-client-reference)
If you would like to keep track of costs per user, team, or client, you may add a "client reference" to the notification. Vonage will allow you to generate reports using this client reference so that you can better understand a particular customer's SMS usage. The client reference can be any string up to 40 characters:
```


 1use Illuminate\Notifications\Messages\VonageMessage;




 2 



 3/**




 4 * Get the Vonage / SMS representation of the notification.




 5 */




 6public function toVonage(object $notifiable): VonageMessage




 7{




 8    return (new VonageMessage)




 9        ->clientReference((string) $notifiable->id)




10        ->content('Your SMS message content');




11}




use Illuminate\Notifications\Messages\VonageMessage;

/**
 * Get the Vonage / SMS representation of the notification.
 */
public function toVonage(object $notifiable): VonageMessage
{
    return (new VonageMessage)
        ->clientReference((string) $notifiable->id)
        ->content('Your SMS message content');
}

```

### [Routing SMS Notifications](https://laravel.com/docs/12.x/notifications#routing-sms-notifications)
To route Vonage notifications to the proper phone number, define a `routeNotificationForVonage` method on your notifiable entity:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Foundation\Auth\User as Authenticatable;




 6use Illuminate\Notifications\Notifiable;




 7use Illuminate\Notifications\Notification;




 8 



 9class User extends Authenticatable




10{




11    use Notifiable;




12 



13    /**




14     * Route notifications for the Vonage channel.




15     */




16    public function routeNotificationForVonage(Notification $notification): string




17    {




18        return $this->phone_number;




19    }




20}




<?php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Illuminate\Notifications\Notification;

class User extends Authenticatable
{
    use Notifiable;

    /**
     * Route notifications for the Vonage channel.
     */
    public function routeNotificationForVonage(Notification $notification): string
    {
        return $this->phone_number;
    }
}

```
