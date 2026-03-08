## [Receiving Broadcasts](https://laravel.com/docs/12.x/broadcasting#receiving-broadcasts)
### [Listening for Events](https://laravel.com/docs/12.x/broadcasting#listening-for-events)
Once you have [installed and instantiated Laravel Echo](https://laravel.com/docs/12.x/broadcasting#client-side-installation), you are ready to start listening for events that are broadcast from your Laravel application. First, use the `channel` method to retrieve an instance of a channel, then call the `listen` method to listen for a specified event:
```


1Echo.channel(`orders.${this.order.id}`)




2    .listen('OrderShipmentStatusUpdated', (e) => {




3        console.log(e.order.name);




4    });




Echo.channel(`orders.${this.order.id}`)
    .listen('OrderShipmentStatusUpdated', (e) => {
        console.log(e.order.name);
    });

```

If you would like to listen for events on a private channel, use the `private` method instead. You may continue to chain calls to the `listen` method to listen for multiple events on a single channel:
```


1Echo.private(`orders.${this.order.id}`)




2    .listen(/* ... */)




3    .listen(/* ... */)




4    .listen(/* ... */);




Echo.private(`orders.${this.order.id}`)
    .listen(/* ... */)
    .listen(/* ... */)
    .listen(/* ... */);

```

#### [Stop Listening for Events](https://laravel.com/docs/12.x/broadcasting#stop-listening-for-events)
If you would like to stop listening to a given event without [leaving the channel](https://laravel.com/docs/12.x/broadcasting#leaving-a-channel), you may use the `stopListening` method:
```


1Echo.private(`orders.${this.order.id}`)




2    .stopListening('OrderShipmentStatusUpdated');




Echo.private(`orders.${this.order.id}`)
    .stopListening('OrderShipmentStatusUpdated');

```

### [Leaving a Channel](https://laravel.com/docs/12.x/broadcasting#leaving-a-channel)
To leave a channel, you may call the `leaveChannel` method on your Echo instance:
```


1Echo.leaveChannel(`orders.${this.order.id}`);




Echo.leaveChannel(`orders.${this.order.id}`);

```

If you would like to leave a channel and also its associated private and presence channels, you may call the `leave` method:
```


1Echo.leave(`orders.${this.order.id}`);




Echo.leave(`orders.${this.order.id}`);

```

### [Namespaces](https://laravel.com/docs/12.x/broadcasting#namespaces)
You may have noticed in the examples above that we did not specify the full `App\Events` namespace for the event classes. This is because Echo will automatically assume the events are located in the `App\Events` namespace. However, you may configure the root namespace when you instantiate Echo by passing a `namespace` configuration option:
```


1window.Echo = new Echo({




2    broadcaster: 'pusher',




3    // ...




4    namespace: 'App.Other.Namespace'




5});




window.Echo = new Echo({
    broadcaster: 'pusher',
    // ...
    namespace: 'App.Other.Namespace'
});

```

Alternatively, you may prefix event classes with a `.` when subscribing to them using Echo. This will allow you to always specify the fully-qualified class name:
```


1Echo.channel('orders')




2    .listen('.Namespace\\Event\\Class', (e) => {




3        // ...




4    });




Echo.channel('orders')
    .listen('.Namespace\\Event\\Class', (e) => {
        // ...
    });

```

### [Using React or Vue](https://laravel.com/docs/12.x/broadcasting#using-react-or-vue)
Laravel Echo includes React and Vue hooks that make it painless to listen for events. To get started, invoke the `useEcho` hook, which is used to listen for private events. The `useEcho` hook will automatically leave channels when the consuming component is unmounted:
React Vue
```


1import { useEcho } from "@laravel/echo-react";




2 



3useEcho(




4    `orders.${orderId}`,




5    "OrderShipmentStatusUpdated",




6    (e) => {




7        console.log(e.order);




8    },




9);




import { useEcho } from "@laravel/echo-react";

useEcho(
    `orders.${orderId}`,
    "OrderShipmentStatusUpdated",
    (e) => {
        console.log(e.order);
    },
);

```

```


 1<script setup lang="ts">




 2import { useEcho } from "@laravel/echo-vue";




 3 



 4useEcho(




 5    `orders.${orderId}`,




 6    "OrderShipmentStatusUpdated",




 7    (e) => {




 8        console.log(e.order);




 9    },




10);




11</script>




<script setup lang="ts">
import { useEcho } from "@laravel/echo-vue";

useEcho(
    `orders.${orderId}`,
    "OrderShipmentStatusUpdated",
    (e) => {
        console.log(e.order);
    },
);
</script>

```

You may listen to multiple events by providing an array of events to `useEcho`:
```


1useEcho(




2    `orders.${orderId}`,




3    ["OrderShipmentStatusUpdated", "OrderShipped"],




4    (e) => {




5        console.log(e.order);




6    },




7);




useEcho(
    `orders.${orderId}`,
    ["OrderShipmentStatusUpdated", "OrderShipped"],
    (e) => {
        console.log(e.order);
    },
);

```

You may also specify the shape of the broadcast event payload data, providing greater type safety and editing convenience:
```


 1type OrderData = {




 2    order: {




 3        id: number;




 4        user: {




 5            id: number;




 6            name: string;




 7        };




 8        created_at: string;




 9    };




10};




11 



12useEcho<OrderData>(`orders.${orderId}`, "OrderShipmentStatusUpdated", (e) => {




13    console.log(e.order.id);




14    console.log(e.order.user.id);




15});




type OrderData = {
    order: {
        id: number;
        user: {
            id: number;
            name: string;
        };
        created_at: string;
    };
};

useEcho<OrderData>(`orders.${orderId}`, "OrderShipmentStatusUpdated", (e) => {
    console.log(e.order.id);
    console.log(e.order.user.id);
});

```

The `useEcho` hook will automatically leave channels when the consuming component is unmounted; however, you may utilize the returned functions to manually stop / start listening to channels programmatically when necessary:
React Vue
```


 1import { useEcho } from "@laravel/echo-react";




 2 



 3const { leaveChannel, leave, stopListening, listen } = useEcho(




 4    `orders.${orderId}`,




 5    "OrderShipmentStatusUpdated",




 6    (e) => {




 7        console.log(e.order);




 8    },




 9);




10 



11// Stop listening without leaving channel...




12stopListening();




13 



14// Start listening again...




15listen();




16 



17// Leave channel...




18leaveChannel();




19 



20// Leave a channel and also its associated private and presence channels...




21leave();




import { useEcho } from "@laravel/echo-react";

const { leaveChannel, leave, stopListening, listen } = useEcho(
    `orders.${orderId}`,
    "OrderShipmentStatusUpdated",
    (e) => {
        console.log(e.order);
    },
);

// Stop listening without leaving channel...
stopListening();

// Start listening again...
listen();

// Leave channel...
leaveChannel();

// Leave a channel and also its associated private and presence channels...
leave();

```

```


 1<script setup lang="ts">




 2import { useEcho } from "@laravel/echo-vue";




 3 



 4const { leaveChannel, leave, stopListening, listen } = useEcho(




 5    `orders.${orderId}`,




 6    "OrderShipmentStatusUpdated",




 7    (e) => {




 8        console.log(e.order);




 9    },




10);




11 



12// Stop listening without leaving channel...




13stopListening();




14 



15// Start listening again...




16listen();




17 



18// Leave channel...




19leaveChannel();




20 



21// Leave a channel and also its associated private and presence channels...




22leave();




23</script>




<script setup lang="ts">
import { useEcho } from "@laravel/echo-vue";

const { leaveChannel, leave, stopListening, listen } = useEcho(
    `orders.${orderId}`,
    "OrderShipmentStatusUpdated",
    (e) => {
        console.log(e.order);
    },
);

// Stop listening without leaving channel...
stopListening();

// Start listening again...
listen();

// Leave channel...
leaveChannel();

// Leave a channel and also its associated private and presence channels...
leave();
</script>

```

#### [Connecting to Public Channels](https://laravel.com/docs/12.x/broadcasting#react-vue-connecting-to-public-channels)
To connect to a public channel, you may use the `useEchoPublic` hook:
React Vue
```


1import { useEchoPublic } from "@laravel/echo-react";




2 



3useEchoPublic("posts", "PostPublished", (e) => {




4    console.log(e.post);




5});




import { useEchoPublic } from "@laravel/echo-react";

useEchoPublic("posts", "PostPublished", (e) => {
    console.log(e.post);
});

```

```


1<script setup lang="ts">




2import { useEchoPublic } from "@laravel/echo-vue";




3 



4useEchoPublic("posts", "PostPublished", (e) => {




5    console.log(e.post);




6});




7</script>




<script setup lang="ts">
import { useEchoPublic } from "@laravel/echo-vue";

useEchoPublic("posts", "PostPublished", (e) => {
    console.log(e.post);
});
</script>

```

#### [Connecting to Presence Channels](https://laravel.com/docs/12.x/broadcasting#react-vue-connecting-to-presence-channels)
To connect to a presence channel, you may use the `useEchoPresence` hook:
React Vue
```


1import { useEchoPresence } from "@laravel/echo-react";




2 



3useEchoPresence("posts", "PostPublished", (e) => {




4    console.log(e.post);




5});




import { useEchoPresence } from "@laravel/echo-react";

useEchoPresence("posts", "PostPublished", (e) => {
    console.log(e.post);
});

```

```


1<script setup lang="ts">




2import { useEchoPresence } from "@laravel/echo-vue";




3 



4useEchoPresence("posts", "PostPublished", (e) => {




5    console.log(e.post);




6});




7</script>




<script setup lang="ts">
import { useEchoPresence } from "@laravel/echo-vue";

useEchoPresence("posts", "PostPublished", (e) => {
    console.log(e.post);
});
</script>

```

#### [Connection Status](https://laravel.com/docs/12.x/broadcasting#react-vue-connection-status)
You may retrieve the current WebSocket connection status using the `useConnectionStatus` hook, which provides reactive status that automatically updates when the connection state changes:
React Vue
```


1import { useConnectionStatus } from "@laravel/echo-react";




2 



3function ConnectionIndicator() {




4    const status = useConnectionStatus();




5 



6    return <div>Connection: {status}</div>;




7}




import { useConnectionStatus } from "@laravel/echo-react";

function ConnectionIndicator() {
    const status = useConnectionStatus();

    return <div>Connection: {status}</div>;
}

```

```


1<script setup lang="ts">




2import { useConnectionStatus } from "@laravel/echo-vue";




3 



4const status = useConnectionStatus();




5</script>




6 



7<template>




8    <div>Connection: {{ status }}</div>




9</template>




<script setup lang="ts">
import { useConnectionStatus } from "@laravel/echo-vue";

const status = useConnectionStatus();
</script>

<template>
    <div>Connection: {{ status }}</div>
</template>

```

The possible status values are:
  * `connected` - Successfully connected to the WebSocket server.
  * `connecting` - Initial connection attempt in progress.
  * `reconnecting` - Attempting to reconnect after a disconnection.
  * `disconnected` - Not connected and not attempting to reconnect.
  * `failed` - Connection failed and won't retry.
