## [Localizing Mailables](https://laravel.com/docs/12.x/mail#localizing-mailables)
Laravel allows you to send mailables in a locale other than the request's current locale, and will even remember this locale if the mail is queued.
To accomplish this, the `Mail` facade offers a `locale` method to set the desired language. The application will change into this locale when the mailable's template is being evaluated and then revert back to the previous locale when evaluation is complete:
```


1Mail::to($request->user())->locale('es')->send(




2    new OrderShipped($order)




3);




Mail::to($request->user())->locale('es')->send(
    new OrderShipped($order)
);

```

#### [User Preferred Locales](https://laravel.com/docs/12.x/mail#user-preferred-locales)
Sometimes, applications store each user's preferred locale. By implementing the `HasLocalePreference` contract on one or more of your models, you may instruct Laravel to use this stored locale when sending mail:
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

Once you have implemented the interface, Laravel will automatically use the preferred locale when sending mailables and notifications to the model. Therefore, there is no need to call the `locale` method when using this interface:
```


1Mail::to($request->user())->send(new OrderShipped($order));




Mail::to($request->user())->send(new OrderShipped($order));

```
