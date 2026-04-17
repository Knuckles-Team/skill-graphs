## [Custom Channels](https://laravel.com/docs/12.x/notifications#custom-channels)
Laravel ships with a handful of notification channels, but you may want to write your own drivers to deliver notifications via other channels. Laravel makes it simple. To get started, define a class that contains a `send` method. The method should receive two arguments: a `$notifiable` and a `$notification`.
Within the `send` method, you may call methods on the notification to retrieve a message object understood by your channel and then send the notification to the `$notifiable` instance however you wish:
```


 1<?php




 2 



 3namespace App\Notifications;




 4 



 5use Illuminate\Notifications\Notification;




 6 



 7class VoiceChannel




 8{




 9    /**




10     * Send the given notification.




11     */




12    public function send(object $notifiable, Notification $notification): void




13    {




14        $message = $notification->toVoice($notifiable);




15 



16        // Send notification to the $notifiable instance...




17    }




18}




<?php

namespace App\Notifications;

use Illuminate\Notifications\Notification;

class VoiceChannel
{
    /**
     * Send the given notification.
     */
    public function send(object $notifiable, Notification $notification): void
    {
        $message = $notification->toVoice($notifiable);

        // Send notification to the $notifiable instance...
    }
}

```

Once your notification channel class has been defined, you may return the class name from the `via` method of any of your notifications. In this example, the `toVoice` method of your notification can return whatever object you choose to represent voice messages. For example, you might define your own `VoiceMessage` class to represent these messages:
```


 1<?php




 2 



 3namespace App\Notifications;




 4 



 5use App\Notifications\Messages\VoiceMessage;




 6use App\Notifications\VoiceChannel;




 7use Illuminate\Bus\Queueable;




 8use Illuminate\Contracts\Queue\ShouldQueue;




 9use Illuminate\Notifications\Notification;




10 



11class InvoicePaid extends Notification




12{




13    use Queueable;




14 



15    /**




16     * Get the notification channels.




17     */




18    public function via(object $notifiable): string




19    {




20        return VoiceChannel::class;




21    }




22 



23    /**




24     * Get the voice representation of the notification.




25     */




26    public function toVoice(object $notifiable): VoiceMessage




27    {




28        // ...




29    }




30}




<?php

namespace App\Notifications;

use App\Notifications\Messages\VoiceMessage;
use App\Notifications\VoiceChannel;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Notifications\Notification;

class InvoicePaid extends Notification
{
    use Queueable;

    /**
     * Get the notification channels.
     */
    public function via(object $notifiable): string
    {
        return VoiceChannel::class;
    }

    /**
     * Get the voice representation of the notification.
     */
    public function toVoice(object $notifiable): VoiceMessage
    {
        // ...
    }
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/notifications#introduction)
  * [ Generating Notifications ](https://laravel.com/docs/12.x/notifications#generating-notifications)
  * [ Sending Notifications ](https://laravel.com/docs/12.x/notifications#sending-notifications)
    * [ Using the Notifiable Trait ](https://laravel.com/docs/12.x/notifications#using-the-notifiable-trait)
    * [ Using the Notification Facade ](https://laravel.com/docs/12.x/notifications#using-the-notification-facade)
    * [ Specifying Delivery Channels ](https://laravel.com/docs/12.x/notifications#specifying-delivery-channels)
    * [ Queueing Notifications ](https://laravel.com/docs/12.x/notifications#queueing-notifications)
    * [ On-Demand Notifications ](https://laravel.com/docs/12.x/notifications#on-demand-notifications)
  * [ Mail Notifications ](https://laravel.com/docs/12.x/notifications#mail-notifications)
    * [ Formatting Mail Messages ](https://laravel.com/docs/12.x/notifications#formatting-mail-messages)
    * [ Customizing the Sender ](https://laravel.com/docs/12.x/notifications#customizing-the-sender)
    * [ Customizing the Recipient ](https://laravel.com/docs/12.x/notifications#customizing-the-recipient)
    * [ Customizing the Subject ](https://laravel.com/docs/12.x/notifications#customizing-the-subject)
    * [ Customizing the Mailer ](https://laravel.com/docs/12.x/notifications#customizing-the-mailer)
    * [ Customizing the Templates ](https://laravel.com/docs/12.x/notifications#customizing-the-templates)
    * [ Attachments ](https://laravel.com/docs/12.x/notifications#mail-attachments)
    * [ Adding Tags and Metadata ](https://laravel.com/docs/12.x/notifications#adding-tags-metadata)
    * [ Customizing the Symfony Message ](https://laravel.com/docs/12.x/notifications#customizing-the-symfony-message)
    * [ Using Mailables ](https://laravel.com/docs/12.x/notifications#using-mailables)
    * [ Previewing Mail Notifications ](https://laravel.com/docs/12.x/notifications#previewing-mail-notifications)
  * [ Markdown Mail Notifications ](https://laravel.com/docs/12.x/notifications#markdown-mail-notifications)
    * [ Generating the Message ](https://laravel.com/docs/12.x/notifications#generating-the-message)
    * [ Writing the Message ](https://laravel.com/docs/12.x/notifications#writing-the-message)
    * [ Customizing the Components ](https://laravel.com/docs/12.x/notifications#customizing-the-components)
  * [ Database Notifications ](https://laravel.com/docs/12.x/notifications#database-notifications)
    * [ Prerequisites ](https://laravel.com/docs/12.x/notifications#database-prerequisites)
    * [ Formatting Database Notifications ](https://laravel.com/docs/12.x/notifications#formatting-database-notifications)
    * [ Accessing the Notifications ](https://laravel.com/docs/12.x/notifications#accessing-the-notifications)
    * [ Marking Notifications as Read ](https://laravel.com/docs/12.x/notifications#marking-notifications-as-read)
  * [ Broadcast Notifications ](https://laravel.com/docs/12.x/notifications#broadcast-notifications)
    * [ Prerequisites ](https://laravel.com/docs/12.x/notifications#broadcast-prerequisites)
    * [ Formatting Broadcast Notifications ](https://laravel.com/docs/12.x/notifications#formatting-broadcast-notifications)
    * [ Listening for Notifications ](https://laravel.com/docs/12.x/notifications#listening-for-notifications)
  * [ SMS Notifications ](https://laravel.com/docs/12.x/notifications#sms-notifications)
    * [ Prerequisites ](https://laravel.com/docs/12.x/notifications#sms-prerequisites)
    * [ Formatting SMS Notifications ](https://laravel.com/docs/12.x/notifications#formatting-sms-notifications)
    * [ Customizing the "From" Number ](https://laravel.com/docs/12.x/notifications#customizing-the-from-number)
    * [ Adding a Client Reference ](https://laravel.com/docs/12.x/notifications#adding-a-client-reference)
    * [ Routing SMS Notifications ](https://laravel.com/docs/12.x/notifications#routing-sms-notifications)
  * [ Slack Notifications ](https://laravel.com/docs/12.x/notifications#slack-notifications)
    * [ Prerequisites ](https://laravel.com/docs/12.x/notifications#slack-prerequisites)
    * [ Formatting Slack Notifications ](https://laravel.com/docs/12.x/notifications#formatting-slack-notifications)
    * [ Slack Interactivity ](https://laravel.com/docs/12.x/notifications#slack-interactivity)
    * [ Routing Slack Notifications ](https://laravel.com/docs/12.x/notifications#routing-slack-notifications)
    * [ Notifying External Slack Workspaces ](https://laravel.com/docs/12.x/notifications#notifying-external-slack-workspaces)
  * [ Localizing Notifications ](https://laravel.com/docs/12.x/notifications#localizing-notifications)
  * [ Testing ](https://laravel.com/docs/12.x/notifications#testing)
  * [ Notification Events ](https://laravel.com/docs/12.x/notifications#notification-events)
  * [ Custom Channels ](https://laravel.com/docs/12.x/notifications#custom-channels)


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
  *   * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [ More Partners ](https://partners.laravel.com)
