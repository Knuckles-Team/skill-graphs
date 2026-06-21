## [Presence Channels](https://laravel.com/docs/12.x/broadcasting#presence-channels)
Presence channels build on the security of private channels while exposing the additional feature of awareness of who is subscribed to the channel. This makes it easy to build powerful, collaborative application features such as notifying users when another user is viewing the same page or listing the inhabitants of a chat room.
### [Authorizing Presence Channels](https://laravel.com/docs/12.x/broadcasting#authorizing-presence-channels)
All presence channels are also private channels; therefore, users must be [authorized to access them](https://laravel.com/docs/12.x/broadcasting#authorizing-channels). However, when defining authorization callbacks for presence channels, you will not return `true` if the user is authorized to join the channel. Instead, you should return an array of data about the user.
The data returned by the authorization callback will be made available to the presence channel event listeners in your JavaScript application. If the user is not authorized to join the presence channel, you should return `false` or `null`:
```


1use App\Models\User;




2 



3Broadcast::channel('chat.{roomId}', function (User $user, int $roomId) {




4    if ($user->canJoinRoom($roomId)) {




5        return ['id' => $user->id, 'name' => $user->name];




6    }




7});




use App\Models\User;

Broadcast::channel('chat.{roomId}', function (User $user, int $roomId) {
    if ($user->canJoinRoom($roomId)) {
        return ['id' => $user->id, 'name' => $user->name];
    }
});

```

### [Joining Presence Channels](https://laravel.com/docs/12.x/broadcasting#joining-presence-channels)
To join a presence channel, you may use Echo's `join` method. The `join` method will return a `PresenceChannel` implementation which, along with exposing the `listen` method, allows you to subscribe to the `here`, `joining`, and `leaving` events.
```


 1Echo.join(`chat.${roomId}`)




 2    .here((users) => {




 3        // ...




 4    })




 5    .joining((user) => {




 6        console.log(user.name);




 7    })




 8    .leaving((user) => {




 9        console.log(user.name);




10    })




11    .error((error) => {




12        console.error(error);




13    });




Echo.join(`chat.${roomId}`)
    .here((users) => {
        // ...
    })
    .joining((user) => {
        console.log(user.name);
    })
    .leaving((user) => {
        console.log(user.name);
    })
    .error((error) => {
        console.error(error);
    });

```

The `here` callback will be executed immediately once the channel is joined successfully, and will receive an array containing the user information for all of the other users currently subscribed to the channel. The `joining` method will be executed when a new user joins a channel, while the `leaving` method will be executed when a user leaves the channel. The `error` method will be executed when the authentication endpoint returns an HTTP status code other than 200 or if there is a problem parsing the returned JSON.
### [Broadcasting to Presence Channels](https://laravel.com/docs/12.x/broadcasting#broadcasting-to-presence-channels)
Presence channels may receive events just like public or private channels. Using the example of a chatroom, we may want to broadcast `NewMessage` events to the room's presence channel. To do so, we'll return an instance of `PresenceChannel` from the event's `broadcastOn` method:
```


 1/**




 2 * Get the channels the event should broadcast on.




 3 *




 4 * @return array<int, \Illuminate\Broadcasting\Channel>




 5 */




 6public function broadcastOn(): array




 7{




 8    return [




 9        new PresenceChannel('chat.'.$this->message->room_id),




10    ];




11}




/**
 * Get the channels the event should broadcast on.
 *
 * @return array<int, \Illuminate\Broadcasting\Channel>
 */
public function broadcastOn(): array
{
    return [
        new PresenceChannel('chat.'.$this->message->room_id),
    ];
}

```

As with other events, you may use the `broadcast` helper and the `toOthers` method to exclude the current user from receiving the broadcast:
```


1broadcast(new NewMessage($message));




2 



3broadcast(new NewMessage($message))->toOthers();




broadcast(new NewMessage($message));

broadcast(new NewMessage($message))->toOthers();

```

As typical of other types of events, you may listen for events sent to presence channels using Echo's `listen` method:
```


1Echo.join(`chat.${roomId}`)




2    .here(/* ... */)




3    .joining(/* ... */)




4    .leaving(/* ... */)




5    .listen('NewMessage', (e) => {




6        // ...




7    });




Echo.join(`chat.${roomId}`)
    .here(/* ... */)
    .joining(/* ... */)
    .leaving(/* ... */)
    .listen('NewMessage', (e) => {
        // ...
    });

```
