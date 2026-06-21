## [Validating Passwords](https://laravel.com/docs/12.x/validation#validating-passwords)
To ensure that passwords have an adequate level of complexity, you may use Laravel's `Password` rule object:
```


1use Illuminate\Support\Facades\Validator;




2use Illuminate\Validation\Rules\Password;




3 



4$validator = Validator::make($request->all(), [




5    'password' => ['required', 'confirmed', Password::min(8)],




6]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rules\Password;

$validator = Validator::make($request->all(), [
    'password' => ['required', 'confirmed', Password::min(8)],
]);

```

The `Password` rule object allows you to easily customize the password complexity requirements for your application, such as specifying that passwords require at least one letter, number, symbol, or characters with mixed casing:
```


 1// Require at least 8 characters...




 2Password::min(8)




 3 



 4// Require at least one letter...




 5Password::min(8)->letters()




 6 



 7// Require at least one uppercase and one lowercase letter...




 8Password::min(8)->mixedCase()




 9 



10// Require at least one number...




11Password::min(8)->numbers()




12 



13// Require at least one symbol...




14Password::min(8)->symbols()




// Require at least 8 characters...
Password::min(8)

// Require at least one letter...
Password::min(8)->letters()

// Require at least one uppercase and one lowercase letter...
Password::min(8)->mixedCase()

// Require at least one number...
Password::min(8)->numbers()

// Require at least one symbol...
Password::min(8)->symbols()

```

In addition, you may ensure that a password has not been compromised in a public password data breach leak using the `uncompromised` method:
```


1Password::min(8)->uncompromised()




Password::min(8)->uncompromised()

```

Internally, the `Password` rule object uses the
By default, if a password appears at least once in a data leak, it will be considered compromised. You can customize this threshold using the first argument of the `uncompromised` method:
```


1// Ensure the password appears less than 3 times in the same data leak...




2Password::min(8)->uncompromised(3);




// Ensure the password appears less than 3 times in the same data leak...
Password::min(8)->uncompromised(3);

```

Of course, you may chain all the methods in the examples above:
```


1Password::min(8)




2    ->letters()




3    ->mixedCase()




4    ->numbers()




5    ->symbols()




6    ->uncompromised()




Password::min(8)
    ->letters()
    ->mixedCase()
    ->numbers()
    ->symbols()
    ->uncompromised()

```

#### [Defining Default Password Rules](https://laravel.com/docs/12.x/validation#defining-default-password-rules)
You may find it convenient to specify the default validation rules for passwords in a single location of your application. You can easily accomplish this using the `Password::defaults` method, which accepts a closure. The closure given to the `defaults` method should return the default configuration of the Password rule. Typically, the `defaults` rule should be called within the `boot` method of one of your application's service providers:
```


 1use Illuminate\Validation\Rules\Password;




 2 



 3/**




 4 * Bootstrap any application services.




 5 */




 6public function boot(): void




 7{




 8    Password::defaults(function () {




 9        $rule = Password::min(8);




10 



11        return $this->app->isProduction()




12            ? $rule->mixedCase()->uncompromised()




13            : $rule;




14    });




15}




use Illuminate\Validation\Rules\Password;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Password::defaults(function () {
        $rule = Password::min(8);

        return $this->app->isProduction()
            ? $rule->mixedCase()->uncompromised()
            : $rule;
    });
}

```

Then, when you would like to apply the default rules to a particular password undergoing validation, you may invoke the `defaults` method with no arguments:
```


1'password' => ['required', Password::defaults()],




'password' => ['required', Password::defaults()],

```

Occasionally, you may want to attach additional validation rules to your default password validation rules. You may use the `rules` method to accomplish this:
```


1use App\Rules\ZxcvbnRule;




2 



3Password::defaults(function () {




4    $rule = Password::min(8)->rules([new ZxcvbnRule]);




5 



6    // ...




7});




use App\Rules\ZxcvbnRule;

Password::defaults(function () {
    $rule = Password::min(8)->rules([new ZxcvbnRule]);

    // ...
});

```
