## [Client Side Installation](https://laravel.com/docs/12.x/broadcasting#client-side-installation)
### [Reverb](https://laravel.com/docs/12.x/broadcasting#client-reverb)
When installing Laravel Reverb via the `install:broadcasting` Artisan command, Reverb and Echo's scaffolding and configuration will be injected into your application automatically. However, if you wish to manually configure Laravel Echo, you may do so by following the instructions below.
#### [Manual Installation](https://laravel.com/docs/12.x/broadcasting#reverb-client-manual-installation)
To manually configure Laravel Echo for your application's frontend, first install the `pusher-js` package since Reverb utilizes the Pusher protocol for WebSocket subscriptions, channels, and messages:
```


1npm install --save-dev laravel-echo pusher-js




npm install --save-dev laravel-echo pusher-js

```

Once Echo is installed, you are ready to create a fresh Echo instance in your application's JavaScript. A great place to do this is at the bottom of the `resources/js/bootstrap.js` file that is included with the Laravel framework:
JavaScript React Vue
```


 1import Echo from 'laravel-echo';




 2 



 3import Pusher from 'pusher-js';




 4window.Pusher = Pusher;




 5 



 6window.Echo = new Echo({




 7    broadcaster: 'reverb',




 8    key: import.meta.env.VITE_REVERB_APP_KEY,




 9    wsHost: import.meta.env.VITE_REVERB_HOST,




10    wsPort: import.meta.env.VITE_REVERB_PORT ?? 80,




11    wssPort: import.meta.env.VITE_REVERB_PORT ?? 443,




12    forceTLS: (import.meta.env.VITE_REVERB_SCHEME ?? 'https') === 'https',




13    enabledTransports: ['ws', 'wss'],




14});




import Echo from 'laravel-echo';

import Pusher from 'pusher-js';
window.Pusher = Pusher;

window.Echo = new Echo({
    broadcaster: 'reverb',
    key: import.meta.env.VITE_REVERB_APP_KEY,
    wsHost: import.meta.env.VITE_REVERB_HOST,
    wsPort: import.meta.env.VITE_REVERB_PORT ?? 80,
    wssPort: import.meta.env.VITE_REVERB_PORT ?? 443,
    forceTLS: (import.meta.env.VITE_REVERB_SCHEME ?? 'https') === 'https',
    enabledTransports: ['ws', 'wss'],
});

```

```


 1import { configureEcho } from "@laravel/echo-react";




 2 



 3configureEcho({




 4    broadcaster: "reverb",




 5    // key: import.meta.env.VITE_REVERB_APP_KEY,




 6    // wsHost: import.meta.env.VITE_REVERB_HOST,




 7    // wsPort: import.meta.env.VITE_REVERB_PORT,




 8    // wssPort: import.meta.env.VITE_REVERB_PORT,




 9    // forceTLS: (import.meta.env.VITE_REVERB_SCHEME ?? 'https') === 'https',




10    // enabledTransports: ['ws', 'wss'],




11});




import { configureEcho } from "@laravel/echo-react";

configureEcho({
    broadcaster: "reverb",
    // key: import.meta.env.VITE_REVERB_APP_KEY,
    // wsHost: import.meta.env.VITE_REVERB_HOST,
    // wsPort: import.meta.env.VITE_REVERB_PORT,
    // wssPort: import.meta.env.VITE_REVERB_PORT,
    // forceTLS: (import.meta.env.VITE_REVERB_SCHEME ?? 'https') === 'https',
    // enabledTransports: ['ws', 'wss'],
});

```

```


 1import { configureEcho } from "@laravel/echo-vue";




 2 



 3configureEcho({




 4    broadcaster: "reverb",




 5    // key: import.meta.env.VITE_REVERB_APP_KEY,




 6    // wsHost: import.meta.env.VITE_REVERB_HOST,




 7    // wsPort: import.meta.env.VITE_REVERB_PORT,




 8    // wssPort: import.meta.env.VITE_REVERB_PORT,




 9    // forceTLS: (import.meta.env.VITE_REVERB_SCHEME ?? 'https') === 'https',




10    // enabledTransports: ['ws', 'wss'],




11});




import { configureEcho } from "@laravel/echo-vue";

configureEcho({
    broadcaster: "reverb",
    // key: import.meta.env.VITE_REVERB_APP_KEY,
    // wsHost: import.meta.env.VITE_REVERB_HOST,
    // wsPort: import.meta.env.VITE_REVERB_PORT,
    // wssPort: import.meta.env.VITE_REVERB_PORT,
    // forceTLS: (import.meta.env.VITE_REVERB_SCHEME ?? 'https') === 'https',
    // enabledTransports: ['ws', 'wss'],
});

```

Next, you should compile your application's assets:
```


1npm run build




npm run build

```

The Laravel Echo `reverb` broadcaster requires laravel-echo v1.16.0+.
### [Pusher Channels](https://laravel.com/docs/12.x/broadcasting#client-pusher-channels)
When installing broadcasting support via the `install:broadcasting --pusher` Artisan command, Pusher and Echo's scaffolding and configuration will be injected into your application automatically. However, if you wish to manually configure Laravel Echo, you may do so by following the instructions below.
#### [Manual Installation](https://laravel.com/docs/12.x/broadcasting#pusher-client-manual-installation)
To manually configure Laravel Echo for your application's frontend, first install the `laravel-echo` and `pusher-js` packages which utilize the Pusher protocol for WebSocket subscriptions, channels, and messages:
```


1npm install --save-dev laravel-echo pusher-js




npm install --save-dev laravel-echo pusher-js

```

Once Echo is installed, you are ready to create a fresh Echo instance in your application's `resources/js/bootstrap.js` file:
JavaScript React Vue
```


 1import Echo from 'laravel-echo';




 2 



 3import Pusher from 'pusher-js';




 4window.Pusher = Pusher;




 5 



 6window.Echo = new Echo({




 7    broadcaster: 'pusher',




 8    key: import.meta.env.VITE_PUSHER_APP_KEY,




 9    cluster: import.meta.env.VITE_PUSHER_APP_CLUSTER,




10    forceTLS: true




11});




import Echo from 'laravel-echo';

import Pusher from 'pusher-js';
window.Pusher = Pusher;

window.Echo = new Echo({
    broadcaster: 'pusher',
    key: import.meta.env.VITE_PUSHER_APP_KEY,
    cluster: import.meta.env.VITE_PUSHER_APP_CLUSTER,
    forceTLS: true
});

```

```


 1import { configureEcho } from "@laravel/echo-react";




 2 



 3configureEcho({




 4    broadcaster: "pusher",




 5    // key: import.meta.env.VITE_PUSHER_APP_KEY,




 6    // cluster: import.meta.env.VITE_PUSHER_APP_CLUSTER,




 7    // forceTLS: true,




 8    // wsHost: import.meta.env.VITE_PUSHER_HOST,




 9    // wsPort: import.meta.env.VITE_PUSHER_PORT,




10    // wssPort: import.meta.env.VITE_PUSHER_PORT,




11    // enabledTransports: ["ws", "wss"],




12});




import { configureEcho } from "@laravel/echo-react";

configureEcho({
    broadcaster: "pusher",
    // key: import.meta.env.VITE_PUSHER_APP_KEY,
    // cluster: import.meta.env.VITE_PUSHER_APP_CLUSTER,
    // forceTLS: true,
    // wsHost: import.meta.env.VITE_PUSHER_HOST,
    // wsPort: import.meta.env.VITE_PUSHER_PORT,
    // wssPort: import.meta.env.VITE_PUSHER_PORT,
    // enabledTransports: ["ws", "wss"],
});

```

```


 1import { configureEcho } from "@laravel/echo-vue";




 2 



 3configureEcho({




 4    broadcaster: "pusher",




 5    // key: import.meta.env.VITE_PUSHER_APP_KEY,




 6    // cluster: import.meta.env.VITE_PUSHER_APP_CLUSTER,




 7    // forceTLS: true,




 8    // wsHost: import.meta.env.VITE_PUSHER_HOST,




 9    // wsPort: import.meta.env.VITE_PUSHER_PORT,




10    // wssPort: import.meta.env.VITE_PUSHER_PORT,




11    // enabledTransports: ["ws", "wss"],




12});




import { configureEcho } from "@laravel/echo-vue";

configureEcho({
    broadcaster: "pusher",
    // key: import.meta.env.VITE_PUSHER_APP_KEY,
    // cluster: import.meta.env.VITE_PUSHER_APP_CLUSTER,
    // forceTLS: true,
    // wsHost: import.meta.env.VITE_PUSHER_HOST,
    // wsPort: import.meta.env.VITE_PUSHER_PORT,
    // wssPort: import.meta.env.VITE_PUSHER_PORT,
    // enabledTransports: ["ws", "wss"],
});

```

Next, you should define the appropriate values for the Pusher environment variables in your application's `.env` file. If these variables do not already exist in your `.env` file, you should add them:
```


 1PUSHER_APP_ID="your-pusher-app-id"




 2PUSHER_APP_KEY="your-pusher-key"




 3PUSHER_APP_SECRET="your-pusher-secret"




 4PUSHER_HOST=




 5PUSHER_PORT=443




 6PUSHER_SCHEME="https"




 7PUSHER_APP_CLUSTER="mt1"




 8 



 9VITE_APP_NAME="${APP_NAME}"




10VITE_PUSHER_APP_KEY="${PUSHER_APP_KEY}"




11VITE_PUSHER_HOST="${PUSHER_HOST}"




12VITE_PUSHER_PORT="${PUSHER_PORT}"




13VITE_PUSHER_SCHEME="${PUSHER_SCHEME}"




14VITE_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"




PUSHER_APP_ID="your-pusher-app-id"
PUSHER_APP_KEY="your-pusher-key"
PUSHER_APP_SECRET="your-pusher-secret"
PUSHER_HOST=
PUSHER_PORT=443
PUSHER_SCHEME="https"
PUSHER_APP_CLUSTER="mt1"

VITE_APP_NAME="${APP_NAME}"
VITE_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
VITE_PUSHER_HOST="${PUSHER_HOST}"
VITE_PUSHER_PORT="${PUSHER_PORT}"
VITE_PUSHER_SCHEME="${PUSHER_SCHEME}"
VITE_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"

```

Once you have adjusted the Echo configuration according to your application's needs, you may compile your application's assets:
```


1npm run build




npm run build

```

To learn more about compiling your application's JavaScript assets, please consult the documentation on [Vite](https://laravel.com/docs/12.x/vite).
#### [Using an Existing Client Instance](https://laravel.com/docs/12.x/broadcasting#using-an-existing-client-instance)
If you already have a pre-configured Pusher Channels client instance that you would like Echo to utilize, you may pass it to Echo via the `client` configuration option:
```


 1import Echo from 'laravel-echo';




 2import Pusher from 'pusher-js';




 3 



 4const options = {




 5    broadcaster: 'pusher',




 6    key: import.meta.env.VITE_PUSHER_APP_KEY




 7}




 8 



 9window.Echo = new Echo({




10    ...options,




11    client: new Pusher(options.key, options)




12});




import Echo from 'laravel-echo';
import Pusher from 'pusher-js';

const options = {
    broadcaster: 'pusher',
    key: import.meta.env.VITE_PUSHER_APP_KEY
}

window.Echo = new Echo({
    ...options,
    client: new Pusher(options.key, options)
});

```

### [Ably](https://laravel.com/docs/12.x/broadcasting#client-ably)
The documentation below discusses how to use Ably in "Pusher compatibility" mode. However, the Ably team recommends and maintains a broadcaster and Echo client that is able to take advantage of the unique capabilities offered by Ably. For more information on using the Ably maintained drivers, please
When installing broadcasting support via the `install:broadcasting --ably` Artisan command, Ably and Echo's scaffolding and configuration will be injected into your application automatically. However, if you wish to manually configure Laravel Echo, you may do so by following the instructions below.
#### [Manual Installation](https://laravel.com/docs/12.x/broadcasting#ably-client-manual-installation)
To manually configure Laravel Echo for your application's frontend, first install the `laravel-echo` and `pusher-js` packages which utilize the Pusher protocol for WebSocket subscriptions, channels, and messages:
```


1npm install --save-dev laravel-echo pusher-js




npm install --save-dev laravel-echo pusher-js

```

**Before continuing, you should enable Pusher protocol support in your Ably application settings. You may enable this feature within the "Protocol Adapter Settings" portion of your Ably application's settings dashboard.**
Once Echo is installed, you are ready to create a fresh Echo instance in your application's `resources/js/bootstrap.js` file:
JavaScript React Vue
```


 1import Echo from 'laravel-echo';




 2 



 3import Pusher from 'pusher-js';




 4window.Pusher = Pusher;




 5 



 6window.Echo = new Echo({




 7    broadcaster: 'pusher',




 8    key: import.meta.env.VITE_ABLY_PUBLIC_KEY,




 9    wsHost: 'realtime-pusher.ably.io',




10    wsPort: 443,




11    disableStats: true,




12    encrypted: true,




13});




import Echo from 'laravel-echo';

import Pusher from 'pusher-js';
window.Pusher = Pusher;

window.Echo = new Echo({
    broadcaster: 'pusher',
    key: import.meta.env.VITE_ABLY_PUBLIC_KEY,
    wsHost: 'realtime-pusher.ably.io',
    wsPort: 443,
    disableStats: true,
    encrypted: true,
});

```

```


 1import { configureEcho } from "@laravel/echo-react";




 2 



 3configureEcho({




 4    broadcaster: "ably",




 5    // key: import.meta.env.VITE_ABLY_PUBLIC_KEY,




 6    // wsHost: "realtime-pusher.ably.io",




 7    // wsPort: 443,




 8    // disableStats: true,




 9    // encrypted: true,




10});




import { configureEcho } from "@laravel/echo-react";

configureEcho({
    broadcaster: "ably",
    // key: import.meta.env.VITE_ABLY_PUBLIC_KEY,
    // wsHost: "realtime-pusher.ably.io",
    // wsPort: 443,
    // disableStats: true,
    // encrypted: true,
});

```

```


 1import { configureEcho } from "@laravel/echo-vue";




 2 



 3configureEcho({




 4    broadcaster: "ably",




 5    // key: import.meta.env.VITE_ABLY_PUBLIC_KEY,




 6    // wsHost: "realtime-pusher.ably.io",




 7    // wsPort: 443,




 8    // disableStats: true,




 9    // encrypted: true,




10});




import { configureEcho } from "@laravel/echo-vue";

configureEcho({
    broadcaster: "ably",
    // key: import.meta.env.VITE_ABLY_PUBLIC_KEY,
    // wsHost: "realtime-pusher.ably.io",
    // wsPort: 443,
    // disableStats: true,
    // encrypted: true,
});

```

You may have noticed our Ably Echo configuration references a `VITE_ABLY_PUBLIC_KEY` environment variable. This variable's value should be your Ably public key. Your public key is the portion of your Ably key that occurs before the `:` character.
Once you have adjusted the Echo configuration according to your needs, you may compile your application's assets:
```


1npm run dev




npm run dev

```

To learn more about compiling your application's JavaScript assets, please consult the documentation on [Vite](https://laravel.com/docs/12.x/vite).
