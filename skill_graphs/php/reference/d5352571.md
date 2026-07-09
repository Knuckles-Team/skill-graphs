## Echo
### Resolve Performance Issues and Stale Closure Bugs in `useEcho`
Pull request by
This improves hook reliability and performance by addressing stale closure issues, meaning fewer head-scratching realtime UI bugs and smoother rendering under heavy event traffic. If you're building reactive dashboards or chat experiences, this makes your client-side behavior more dependable.
### Add a Connection Status Hook
Pull request by
A connection status hook is a big UX unlock: you can clearly reflect "connected / reconnecting / offline" states and handle them gracefully in your UI. Great for realtime-heavy apps where user trust depends on knowing whether updates are truly live.
### Events Overloading
Pull request by
Event overloading expands how you can map and handle events, making advanced realtime patterns easier to express without workaround code. Useful when you're consolidating many event types into a cleaner, more maintainable client-side layer.
## Echo
### Event Payload Type Inference
Pull request by
Event payloads are now automatically inferred from the [broadcast event](https://laravel.com/docs/broadcasting#defining-broadcast-events) if the user provides a module override file, resulting in a cleaner `useEcho` experience and less type management for the user.
```


 1import { App } from "./types";




 2 



 3declare module "@laravel/echo-react" {




 4    interface Events {




 5        ".App.Events.UserCreated": {




 6            user: App.Models.User;




 7        };




 8        ".App.Events.OrderShipped": {




 9            order: App.Models.Order;




10            user: App.Models.User;




11        };




12    }




13}




import { App } from "./types";

declare module "@laravel/echo-react" {
    interface Events {
        ".App.Events.UserCreated": {
            user: App.Models.User;
        };
        ".App.Events.OrderShipped": {
            order: App.Models.Order;
            user: App.Models.User;
        };
    }
}

```

## Echo
### Add `stopListeningForNotification`
Pull request by
```


 1const callback = (notification) => {




 2    console.log(notification.type);




 3};




 4 



 5// Start listening...




 6Echo.private(`App.Models.User.${userId}`).notification(callback);




 7 



 8// Stop listening (callback must be the same)...




 9Echo.private(`App.Models.User.${userId}`).stopListeningForNotification(




10    callback




11);




const callback = (notification) => {
    console.log(notification.type);
};

// Start listening...
Echo.private(`App.Models.User.${userId}`).notification(callback);

// Stop listening (callback must be the same)...
Echo.private(`App.Models.User.${userId}`).stopListeningForNotification(
    callback
);

```

A new `stopListeningForNotification` method was added to stop listening for notifications without leaving the channel.
