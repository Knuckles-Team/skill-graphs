## [Notifications](https://laravel.com/docs/12.x/broadcasting#notifications)
By pairing event broadcasting with [notifications](https://laravel.com/docs/12.x/notifications), your JavaScript application may receive new notifications as they occur without needing to refresh the page. Before getting started, be sure to read over the documentation on using [the broadcast notification channel](https://laravel.com/docs/12.x/notifications#broadcast-notifications).
Once you have configured a notification to use the broadcast channel, you may listen for the broadcast events using Echo's `notification` method. Remember, the channel name should match the class name of the entity receiving the notifications:
JavaScript React Vue
```


1Echo.private(`App.Models.User.${userId}`)




2    .notification((notification) => {




3        console.log(notification.type);




4    });




Echo.private(`App.Models.User.${userId}`)
    .notification((notification) => {
        console.log(notification.type);
    });

```

```


1import { useEchoModel } from "@laravel/echo-react";




2 



3const { channel } = useEchoModel('App.Models.User', userId);




4 



5channel().notification((notification) => {




6    console.log(notification.type);




7});




import { useEchoModel } from "@laravel/echo-react";

const { channel } = useEchoModel('App.Models.User', userId);

channel().notification((notification) => {
    console.log(notification.type);
});

```

```


1<script setup lang="ts">




2import { useEchoModel } from "@laravel/echo-vue";




3 



4const { channel } = useEchoModel('App.Models.User', userId);




5 



6channel().notification((notification) => {




7    console.log(notification.type);




8});




9</script>




<script setup lang="ts">
import { useEchoModel } from "@laravel/echo-vue";

const { channel } = useEchoModel('App.Models.User', userId);

channel().notification((notification) => {
    console.log(notification.type);
});
</script>

```

In this example, all notifications sent to `App\Models\User` instances via the `broadcast` channel would be received by the callback. A channel authorization callback for the `App.Models.User.{id}` channel is included in your application's `routes/channels.php` file.
#### [Stop Listening for Notifications](https://laravel.com/docs/12.x/broadcasting#stop-listening-for-notifications)
If you would like to stop listening to notifications without [leaving the channel](https://laravel.com/docs/12.x/broadcasting#leaving-a-channel), you may use the `stopListeningForNotification` method:
```


 1const callback = (notification) => {




 2    console.log(notification.type);




 3}




 4 



 5// Start listening...




 6Echo.private(`App.Models.User.${userId}`)




 7    .notification(callback);




 8 



 9// Stop listening (callback must be the same)...




10Echo.private(`App.Models.User.${userId}`)




11    .stopListeningForNotification(callback);




const callback = (notification) => {
    console.log(notification.type);
}

// Start listening...
Echo.private(`App.Models.User.${userId}`)
    .notification(callback);

// Stop listening (callback must be the same)...
Echo.private(`App.Models.User.${userId}`)
    .stopListeningForNotification(callback);

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/broadcasting#introduction)
  * [ Quickstart ](https://laravel.com/docs/12.x/broadcasting#quickstart)
  * [ Server Side Installation ](https://laravel.com/docs/12.x/broadcasting#server-side-installation)
    * [ Reverb ](https://laravel.com/docs/12.x/broadcasting#reverb)
    * [ Pusher Channels ](https://laravel.com/docs/12.x/broadcasting#pusher-channels)
    * [ Ably ](https://laravel.com/docs/12.x/broadcasting#ably)
  * [ Client Side Installation ](https://laravel.com/docs/12.x/broadcasting#client-side-installation)
    * [ Reverb ](https://laravel.com/docs/12.x/broadcasting#client-reverb)
    * [ Pusher Channels ](https://laravel.com/docs/12.x/broadcasting#client-pusher-channels)
    * [ Ably ](https://laravel.com/docs/12.x/broadcasting#client-ably)
  * [ Concept Overview ](https://laravel.com/docs/12.x/broadcasting#concept-overview)
    * [ Using an Example Application ](https://laravel.com/docs/12.x/broadcasting#using-example-application)
  * [ Defining Broadcast Events ](https://laravel.com/docs/12.x/broadcasting#defining-broadcast-events)
    * [ Broadcast Name ](https://laravel.com/docs/12.x/broadcasting#broadcast-name)
    * [ Broadcast Data ](https://laravel.com/docs/12.x/broadcasting#broadcast-data)
    * [ Broadcast Queue ](https://laravel.com/docs/12.x/broadcasting#broadcast-queue)
    * [ Broadcast Conditions ](https://laravel.com/docs/12.x/broadcasting#broadcast-conditions)
    * [ Broadcasting and Database Transactions ](https://laravel.com/docs/12.x/broadcasting#broadcasting-and-database-transactions)
  * [ Authorizing Channels ](https://laravel.com/docs/12.x/broadcasting#authorizing-channels)
    * [ Defining Authorization Callbacks ](https://laravel.com/docs/12.x/broadcasting#defining-authorization-callbacks)
    * [ Defining Channel Classes ](https://laravel.com/docs/12.x/broadcasting#defining-channel-classes)
  * [ Broadcasting Events ](https://laravel.com/docs/12.x/broadcasting#broadcasting-events)
    * [ Only to Others ](https://laravel.com/docs/12.x/broadcasting#only-to-others)
    * [ Customizing the Connection ](https://laravel.com/docs/12.x/broadcasting#customizing-the-connection)
    * [ Anonymous Events ](https://laravel.com/docs/12.x/broadcasting#anonymous-events)
    * [ Rescuing Broadcasts ](https://laravel.com/docs/12.x/broadcasting#rescuing-broadcasts)
  * [ Receiving Broadcasts ](https://laravel.com/docs/12.x/broadcasting#receiving-broadcasts)
    * [ Listening for Events ](https://laravel.com/docs/12.x/broadcasting#listening-for-events)
    * [ Leaving a Channel ](https://laravel.com/docs/12.x/broadcasting#leaving-a-channel)
    * [ Namespaces ](https://laravel.com/docs/12.x/broadcasting#namespaces)
    * [ Using React or Vue ](https://laravel.com/docs/12.x/broadcasting#using-react-or-vue)
  * [ Presence Channels ](https://laravel.com/docs/12.x/broadcasting#presence-channels)
    * [ Authorizing Presence Channels ](https://laravel.com/docs/12.x/broadcasting#authorizing-presence-channels)
    * [ Joining Presence Channels ](https://laravel.com/docs/12.x/broadcasting#joining-presence-channels)
    * [ Broadcasting to Presence Channels ](https://laravel.com/docs/12.x/broadcasting#broadcasting-to-presence-channels)
  * [ Model Broadcasting ](https://laravel.com/docs/12.x/broadcasting#model-broadcasting)
    * [ Model Broadcasting Conventions ](https://laravel.com/docs/12.x/broadcasting#model-broadcasting-conventions)
    * [ Listening for Model Broadcasts ](https://laravel.com/docs/12.x/broadcasting#listening-for-model-broadcasts)
  * [ Client Events ](https://laravel.com/docs/12.x/broadcasting#client-events)
  * [ Notifications ](https://laravel.com/docs/12.x/broadcasting#notifications)


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
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [ More Partners ](https://partners.laravel.com)
