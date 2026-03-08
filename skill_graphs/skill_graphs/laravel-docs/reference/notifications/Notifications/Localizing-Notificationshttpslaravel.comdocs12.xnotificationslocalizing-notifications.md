## [Localizing Notifications](https://laravel.com/docs/12.x/notifications#localizing-notifications)
Laravel allows you to send notifications in a locale other than the HTTP request's current locale, and will even remember this locale if the notification is queued.
To accomplish this, the `Illuminate\Notifications\Notification` class offers a `locale` method to set the desired language. The application will change into this locale when the notification is being evaluated and then revert back to the previous locale when evaluation is complete:
```


1$user->notify((new InvoicePaid($invoice))->locale('es'));




$user->notify((new InvoicePaid($invoice))->locale('es'));

```

Localization of multiple notifiable entries may also be achieved via the `Notification` facade:
```


1Notification::locale('es')->send(




2    $users, new InvoicePaid($invoice)




3);




Notification::locale('es')->send(
    $users, new InvoicePaid($invoice)
);

```

#### [User Preferred Locales](https://laravel.com/docs/12.x/notifications#user-preferred-locales)
Sometimes, applications store each user's preferred locale. By implementing the `HasLocalePreference` contract on your notifiable model, you may instruct Laravel to use this stored locale when sending a notification:
```


 1use Illuminate\Contracts\Translation\HasLocalePreference;




 2 



 3class User extends Model implements HasLocalePreference




 4{




 5    /**




 6     * Get the user's preferred locale.




 7     */




 8    public function preferredLocale(): string




 9    {




10        return $this->locale;




11    }




12}




use Illuminate\Contracts\Translation\HasLocalePreference;

class User extends Model implements HasLocalePreference
{
    /**
     * Get the user's preferred locale.
     */
    public function preferredLocale(): string
    {
        return $this->locale;
    }
}

```

Once you have implemented the interface, Laravel will automatically use the preferred locale when sending notifications and mailables to the model. Therefore, there is no need to call the `locale` method when using this interface:
```


1$user->notify(new InvoicePaid($invoice));




$user->notify(new InvoicePaid($invoice));

```
