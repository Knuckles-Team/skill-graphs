## [Database Notifications](https://laravel.com/docs/12.x/notifications#database-notifications)
### [Prerequisites](https://laravel.com/docs/12.x/notifications#database-prerequisites)
The `database` notification channel stores the notification information in a database table. This table will contain information such as the notification type as well as a JSON data structure that describes the notification.
You can query the table to display the notifications in your application's user interface. But, before you can do that, you will need to create a database table to hold your notifications. You may use the `make:notifications-table` command to generate a [migration](https://laravel.com/docs/12.x/migrations) with the proper table schema:
```


1php artisan make:notifications-table




2 



3php artisan migrate




php artisan make:notifications-table

php artisan migrate

```

If your notifiable models are using [UUID or ULID primary keys](https://laravel.com/docs/12.x/eloquent#uuid-and-ulid-keys), you should replace the `morphs` method with [uuidMorphs](https://laravel.com/docs/12.x/migrations#column-method-uuidMorphs) or [ulidMorphs](https://laravel.com/docs/12.x/migrations#column-method-ulidMorphs) in the notification table migration.
### [Formatting Database Notifications](https://laravel.com/docs/12.x/notifications#formatting-database-notifications)
If a notification supports being stored in a database table, you should define a `toDatabase` or `toArray` method on the notification class. This method will receive a `$notifiable` entity and should return a plain PHP array. The returned array will be encoded as JSON and stored in the `data` column of your `notifications` table. Let's take a look at an example `toArray` method:
```


 1/**




 2 * Get the array representation of the notification.




 3 *




 4 * @return array<string, mixed>




 5 */




 6public function toArray(object $notifiable): array




 7{




 8    return [




 9        'invoice_id' => $this->invoice->id,




10        'amount' => $this->invoice->amount,




11    ];




12}




/**
 * Get the array representation of the notification.
 *
 * @return array<string, mixed>
 */
public function toArray(object $notifiable): array
{
    return [
        'invoice_id' => $this->invoice->id,
        'amount' => $this->invoice->amount,
    ];
}

```

When a notification is stored in your application's database, the `type` column will be set to the notification's class name by default, and the `read_at` column will be `null`. However, you can customize this behavior by defining the `databaseType` and `initialDatabaseReadAtValue` methods in your notification class:
```


 1use Illuminate\Support\Carbon;




 2 



 3/**




 4 * Get the notification's database type.




 5 */




 6public function databaseType(object $notifiable): string




 7{




 8    return 'invoice-paid';




 9}




10 



11/**




12 * Get the initial value for the "read_at" column.




13 */




14public function initialDatabaseReadAtValue(): ?Carbon




15{




16    return null;




17}




use Illuminate\Support\Carbon;

/**
 * Get the notification's database type.
 */
public function databaseType(object $notifiable): string
{
    return 'invoice-paid';
}

/**
 * Get the initial value for the "read_at" column.
 */
public function initialDatabaseReadAtValue(): ?Carbon
{
    return null;
}

```

#### [`toDatabase` vs. `toArray`](https://laravel.com/docs/12.x/notifications#todatabase-vs-toarray)
The `toArray` method is also used by the `broadcast` channel to determine which data to broadcast to your JavaScript powered frontend. If you would like to have two different array representations for the `database` and `broadcast` channels, you should define a `toDatabase` method instead of a `toArray` method.
### [Accessing the Notifications](https://laravel.com/docs/12.x/notifications#accessing-the-notifications)
Once notifications are stored in the database, you need a convenient way to access them from your notifiable entities. The `Illuminate\Notifications\Notifiable` trait, which is included on Laravel's default `App\Models\User` model, includes a `notifications` [Eloquent relationship](https://laravel.com/docs/12.x/eloquent-relationships) that returns the notifications for the entity. To fetch notifications, you may access this method like any other Eloquent relationship. By default, notifications will be sorted by the `created_at` timestamp with the most recent notifications at the beginning of the collection:
```


1$user = App\Models\User::find(1);




2 



3foreach ($user->notifications as $notification) {




4    echo $notification->type;




5}




$user = App\Models\User::find(1);

foreach ($user->notifications as $notification) {
    echo $notification->type;
}

```

If you want to retrieve only the "unread" notifications, you may use the `unreadNotifications` relationship. Again, these notifications will be sorted by the `created_at` timestamp with the most recent notifications at the beginning of the collection:
```


1$user = App\Models\User::find(1);




2 



3foreach ($user->unreadNotifications as $notification) {




4    echo $notification->type;




5}




$user = App\Models\User::find(1);

foreach ($user->unreadNotifications as $notification) {
    echo $notification->type;
}

```

If you want to retrieve only the "read" notifications, you may use the `readNotifications` relationship:
```


1$user = App\Models\User::find(1);




2 



3foreach ($user->readNotifications as $notification) {




4    echo $notification->type;




5}




$user = App\Models\User::find(1);

foreach ($user->readNotifications as $notification) {
    echo $notification->type;
}

```

To access your notifications from your JavaScript client, you should define a notification controller for your application which returns the notifications for a notifiable entity, such as the current user. You may then make an HTTP request to that controller's URL from your JavaScript client.
### [Marking Notifications as Read](https://laravel.com/docs/12.x/notifications#marking-notifications-as-read)
Typically, you will want to mark a notification as "read" when a user views it. The `Illuminate\Notifications\Notifiable` trait provides a `markAsRead` method, which updates the `read_at` column on the notification's database record:
```


1$user = App\Models\User::find(1);




2 



3foreach ($user->unreadNotifications as $notification) {




4    $notification->markAsRead();




5}




$user = App\Models\User::find(1);

foreach ($user->unreadNotifications as $notification) {
    $notification->markAsRead();
}

```

However, instead of looping through each notification, you may use the `markAsRead` method directly on a collection of notifications:
```


1$user->unreadNotifications->markAsRead();




$user->unreadNotifications->markAsRead();

```

You may also use a mass-update query to mark all of the notifications as read without retrieving them from the database:
```


1$user = App\Models\User::find(1);




2 



3$user->unreadNotifications()->update(['read_at' => now()]);




$user = App\Models\User::find(1);

$user->unreadNotifications()->update(['read_at' => now()]);

```

You may `delete` the notifications to remove them from the table entirely:
```


1$user->notifications()->delete();




$user->notifications()->delete();

```
