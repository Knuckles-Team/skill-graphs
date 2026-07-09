## [Model Broadcasting](https://laravel.com/docs/12.x/broadcasting#model-broadcasting)
Before reading the following documentation about model broadcasting, we recommend you become familiar with the general concepts of Laravel's model broadcasting services as well as how to manually create and listen to broadcast events.
It is common to broadcast events when your application's [Eloquent models](https://laravel.com/docs/12.x/eloquent) are created, updated, or deleted. Of course, this can easily be accomplished by manually [defining custom events for Eloquent model state changes](https://laravel.com/docs/12.x/eloquent#events) and marking those events with the `ShouldBroadcast` interface.
However, if you are not using these events for any other purposes in your application, it can be cumbersome to create event classes for the sole purpose of broadcasting them. To remedy this, Laravel allows you to indicate that an Eloquent model should automatically broadcast its state changes.
To get started, your Eloquent model should use the `Illuminate\Database\Eloquent\BroadcastsEvents` trait. In addition, the model should define a `broadcastOn` method, which will return an array of channels that the model's events should broadcast on:
```


 1<?php




 2 



 3namespace App\Models;




 4 



 5use Illuminate\Broadcasting\Channel;




 6use Illuminate\Broadcasting\PrivateChannel;




 7use Illuminate\Database\Eloquent\BroadcastsEvents;




 8use Illuminate\Database\Eloquent\Factories\HasFactory;




 9use Illuminate\Database\Eloquent\Model;




10use Illuminate\Database\Eloquent\Relations\BelongsTo;




11 



12class Post extends Model




13{




14    use BroadcastsEvents, HasFactory;




15 



16    /**




17     * Get the user that the post belongs to.




18     */




19    public function user(): BelongsTo




20    {




21        return $this->belongsTo(User::class);




22    }




23 



24    /**




25     * Get the channels that model events should broadcast on.




26     *




27     * @return array<int, \Illuminate\Broadcasting\Channel|\Illuminate\Database\Eloquent\Model>




28     */




29    public function broadcastOn(string $event): array




30    {




31        return [$this, $this->user];




32    }




33}




<?php

namespace App\Models;

use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Database\Eloquent\BroadcastsEvents;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Post extends Model
{
    use BroadcastsEvents, HasFactory;

    /**
     * Get the user that the post belongs to.
     */
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    /**
     * Get the channels that model events should broadcast on.
     *
     * @return array<int, \Illuminate\Broadcasting\Channel|\Illuminate\Database\Eloquent\Model>
     */
    public function broadcastOn(string $event): array
    {
        return [$this, $this->user];
    }
}

```

Once your model includes this trait and defines its broadcast channels, it will begin automatically broadcasting events when a model instance is created, updated, deleted, trashed, or restored.
In addition, you may have noticed that the `broadcastOn` method receives a string `$event` argument. This argument contains the type of event that has occurred on the model and will have a value of `created`, `updated`, `deleted`, `trashed`, or `restored`. By inspecting the value of this variable, you may determine which channels (if any) the model should broadcast to for a particular event:
```


 1/**




 2 * Get the channels that model events should broadcast on.




 3 *




 4 * @return array<string, array<int, \Illuminate\Broadcasting\Channel|\Illuminate\Database\Eloquent\Model>>




 5 */




 6public function broadcastOn(string $event): array




 7{




 8    return match ($event) {




 9        'deleted' => [],




10        default => [$this, $this->user],




11    };




12}




/**
 * Get the channels that model events should broadcast on.
 *
 * @return array<string, array<int, \Illuminate\Broadcasting\Channel|\Illuminate\Database\Eloquent\Model>>
 */
public function broadcastOn(string $event): array
{
    return match ($event) {
        'deleted' => [],
        default => [$this, $this->user],
    };
}

```

#### [Customizing Model Broadcasting Event Creation](https://laravel.com/docs/12.x/broadcasting#customizing-model-broadcasting-event-creation)
Occasionally, you may wish to customize how Laravel creates the underlying model broadcasting event. You may accomplish this by defining a `newBroadcastableEvent` method on your Eloquent model. This method should return an `Illuminate\Database\Eloquent\BroadcastableModelEventOccurred` instance:
```


 1use Illuminate\Database\Eloquent\BroadcastableModelEventOccurred;




 2 



 3/**




 4 * Create a new broadcastable model event for the model.




 5 */




 6protected function newBroadcastableEvent(string $event): BroadcastableModelEventOccurred




 7{




 8    return (new BroadcastableModelEventOccurred(




 9        $this, $event




10    ))->dontBroadcastToCurrentUser();




11}




use Illuminate\Database\Eloquent\BroadcastableModelEventOccurred;

/**
 * Create a new broadcastable model event for the model.
 */
protected function newBroadcastableEvent(string $event): BroadcastableModelEventOccurred
{
    return (new BroadcastableModelEventOccurred(
        $this, $event
    ))->dontBroadcastToCurrentUser();
}

```

### [Model Broadcasting Conventions](https://laravel.com/docs/12.x/broadcasting#model-broadcasting-conventions)
#### [Channel Conventions](https://laravel.com/docs/12.x/broadcasting#model-broadcasting-channel-conventions)
As you may have noticed, the `broadcastOn` method in the model example above did not return `Channel` instances. Instead, Eloquent models were returned directly. If an Eloquent model instance is returned by your model's `broadcastOn` method (or is contained in an array returned by the method), Laravel will automatically instantiate a private channel instance for the model using the model's class name and primary key identifier as the channel name.
So, an `App\Models\User` model with an `id` of `1` would be converted into an `Illuminate\Broadcasting\PrivateChannel` instance with a name of `App.Models.User.1`. Of course, in addition to returning Eloquent model instances from your model's `broadcastOn` method, you may return complete `Channel` instances in order to have full control over the model's channel names:
```


 1use Illuminate\Broadcasting\PrivateChannel;




 2 



 3/**




 4 * Get the channels that model events should broadcast on.




 5 *




 6 * @return array<int, \Illuminate\Broadcasting\Channel>




 7 */




 8public function broadcastOn(string $event): array




 9{




10    return [




11        new PrivateChannel('user.'.$this->id)




12    ];




13}




use Illuminate\Broadcasting\PrivateChannel;

/**
 * Get the channels that model events should broadcast on.
 *
 * @return array<int, \Illuminate\Broadcasting\Channel>
 */
public function broadcastOn(string $event): array
{
    return [
        new PrivateChannel('user.'.$this->id)
    ];
}

```

If you plan to explicitly return a channel instance from your model's `broadcastOn` method, you may pass an Eloquent model instance to the channel's constructor. When doing so, Laravel will use the model channel conventions discussed above to convert the Eloquent model into a channel name string:
```


1return [new Channel($this->user)];




return [new Channel($this->user)];

```

If you need to determine the channel name of a model, you may call the `broadcastChannel` method on any model instance. For example, this method returns the string `App.Models.User.1` for an `App\Models\User` model with an `id` of `1`:
```


1$user->broadcastChannel();




$user->broadcastChannel();

```

#### [Event Conventions](https://laravel.com/docs/12.x/broadcasting#model-broadcasting-event-conventions)
Since model broadcast events are not associated with an "actual" event within your application's `App\Events` directory, they are assigned a name and a payload based on conventions. Laravel's convention is to broadcast the event using the class name of the model (not including the namespace) and the name of the model event that triggered the broadcast.
So, for example, an update to the `App\Models\Post` model would broadcast an event to your client-side application as `PostUpdated` with the following payload:
```


1{




2    "model": {




3        "id": 1,




4        "title": "My first post"




5        ...




6    },




7    ...




8    "socket": "someSocketId"




9}




{
    "model": {
        "id": 1,
        "title": "My first post"
        ...
    },
    ...
    "socket": "someSocketId"
}

```

The deletion of the `App\Models\User` model would broadcast an event named `UserDeleted`.
If you would like, you may define a custom broadcast name and payload by adding a `broadcastAs` and `broadcastWith` method to your model. These methods receive the name of the model event / operation that is occurring, allowing you to customize the event's name and payload for each model operation. If `null` is returned from the `broadcastAs` method, Laravel will use the model broadcasting event name conventions discussed above when broadcasting the event:
```


 1/**




 2 * The model event's broadcast name.




 3 */




 4public function broadcastAs(string $event): string|null




 5{




 6    return match ($event) {




 7        'created' => 'post.created',




 8        default => null,




 9    };




10}




11 



12/**




13 * Get the data to broadcast for the model.




14 *




15 * @return array<string, mixed>




16 */




17public function broadcastWith(string $event): array




18{




19    return match ($event) {




20        'created' => ['title' => $this->title],




21        default => ['model' => $this],




22    };




23}




/**
 * The model event's broadcast name.
 */
public function broadcastAs(string $event): string|null
{
    return match ($event) {
        'created' => 'post.created',
        default => null,
    };
}

/**
 * Get the data to broadcast for the model.
 *
 * @return array<string, mixed>
 */
public function broadcastWith(string $event): array
{
    return match ($event) {
        'created' => ['title' => $this->title],
        default => ['model' => $this],
    };
}

```

### [Listening for Model Broadcasts](https://laravel.com/docs/12.x/broadcasting#listening-for-model-broadcasts)
Once you have added the `BroadcastsEvents` trait to your model and defined your model's `broadcastOn` method, you are ready to start listening for broadcasted model events within your client-side application. Before getting started, you may wish to consult the complete documentation on [listening for events](https://laravel.com/docs/12.x/broadcasting#listening-for-events).
First, use the `private` method to retrieve an instance of a channel, then call the `listen` method to listen for a specified event. Typically, the channel name given to the `private` method should correspond to Laravel's [model broadcasting conventions](https://laravel.com/docs/12.x/broadcasting#model-broadcasting-conventions).
Once you have obtained a channel instance, you may use the `listen` method to listen for a particular event. Since model broadcast events are not associated with an "actual" event within your application's `App\Events` directory, the [event name](https://laravel.com/docs/12.x/broadcasting#model-broadcasting-event-conventions) must be prefixed with a `.` to indicate it does not belong to a particular namespace. Each model broadcast event has a `model` property which contains all of the broadcastable properties of the model:
```


1Echo.private(`App.Models.User.${this.user.id}`)




2    .listen('.UserUpdated', (e) => {




3        console.log(e.model);




4    });




Echo.private(`App.Models.User.${this.user.id}`)
    .listen('.UserUpdated', (e) => {
        console.log(e.model);
    });

```

#### [Using React or Vue](https://laravel.com/docs/12.x/broadcasting#model-broadcasts-with-react-or-vue)
If you are using React or Vue, you may use Laravel Echo's included `useEchoModel` hook to easily listen for model broadcasts:
React Vue
```


1import { useEchoModel } from "@laravel/echo-react";




2 



3useEchoModel("App.Models.User", userId, ["UserUpdated"], (e) => {




4    console.log(e.model);




5});




import { useEchoModel } from "@laravel/echo-react";

useEchoModel("App.Models.User", userId, ["UserUpdated"], (e) => {
    console.log(e.model);
});

```

```


1<script setup lang="ts">




2import { useEchoModel } from "@laravel/echo-vue";




3 



4useEchoModel("App.Models.User", userId, ["UserUpdated"], (e) => {




5    console.log(e.model);




6});




7</script>




<script setup lang="ts">
import { useEchoModel } from "@laravel/echo-vue";

useEchoModel("App.Models.User", userId, ["UserUpdated"], (e) => {
    console.log(e.model);
});
</script>

```

You may also specify the shape of the model event payload data, providing greater type safety and editing convenience:
```


 1type User = {




 2    id: number;




 3    name: string;




 4    email: string;




 5};




 6 



 7useEchoModel<User, "App.Models.User">("App.Models.User", userId, ["UserUpdated"], (e) => {




 8    console.log(e.model.id);




 9    console.log(e.model.name);




10});




type User = {
    id: number;
    name: string;
    email: string;
};

useEchoModel<User, "App.Models.User">("App.Models.User", userId, ["UserUpdated"], (e) => {
    console.log(e.model.id);
    console.log(e.model.name);
});

```
