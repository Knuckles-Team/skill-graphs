## [Working With Error Messages](https://laravel.com/docs/12.x/validation#working-with-error-messages)
After calling the `errors` method on a `Validator` instance, you will receive an `Illuminate\Support\MessageBag` instance, which has a variety of convenient methods for working with error messages. The `$errors` variable that is automatically made available to all views is also an instance of the `MessageBag` class.
#### [Retrieving the First Error Message for a Field](https://laravel.com/docs/12.x/validation#retrieving-the-first-error-message-for-a-field)
To retrieve the first error message for a given field, use the `first` method:
```


1$errors = $validator->errors();




2 



3echo $errors->first('email');




$errors = $validator->errors();

echo $errors->first('email');

```

#### [Retrieving All Error Messages for a Field](https://laravel.com/docs/12.x/validation#retrieving-all-error-messages-for-a-field)
If you need to retrieve an array of all the messages for a given field, use the `get` method:
```


1foreach ($errors->get('email') as $message) {




2    // ...




3}




foreach ($errors->get('email') as $message) {
    // ...
}

```

If you are validating an array form field, you may retrieve all of the messages for each of the array elements using the `*` character:
```


1foreach ($errors->get('attachments.*') as $message) {




2    // ...




3}




foreach ($errors->get('attachments.*') as $message) {
    // ...
}

```

#### [Retrieving All Error Messages for All Fields](https://laravel.com/docs/12.x/validation#retrieving-all-error-messages-for-all-fields)
To retrieve an array of all messages for all fields, use the `all` method:
```


1foreach ($errors->all() as $message) {




2    // ...




3}




foreach ($errors->all() as $message) {
    // ...
}

```

#### [Determining if Messages Exist for a Field](https://laravel.com/docs/12.x/validation#determining-if-messages-exist-for-a-field)
The `has` method may be used to determine if any error messages exist for a given field:
```


1if ($errors->has('email')) {




2    // ...




3}




if ($errors->has('email')) {
    // ...
}

```

### [Specifying Custom Messages in Language Files](https://laravel.com/docs/12.x/validation#specifying-custom-messages-in-language-files)
Laravel's built-in validation rules each have an error message that is located in your application's `lang/en/validation.php` file. If your application does not have a `lang` directory, you may instruct Laravel to create it using the `lang:publish` Artisan command.
Within the `lang/en/validation.php` file, you will find a translation entry for each validation rule. You are free to change or modify these messages based on the needs of your application.
In addition, you may copy this file to another language directory to translate the messages for your application's language. To learn more about Laravel localization, check out the complete [localization documentation](https://laravel.com/docs/12.x/localization).
By default, the Laravel application skeleton does not include the `lang` directory. If you would like to customize Laravel's language files, you may publish them via the `lang:publish` Artisan command.
#### [Custom Messages for Specific Attributes](https://laravel.com/docs/12.x/validation#custom-messages-for-specific-attributes)
You may customize the error messages used for specified attribute and rule combinations within your application's validation language files. To do so, add your message customizations to the `custom` array of your application's `lang/xx/validation.php` language file:
```


1'custom' => [




2    'email' => [




3        'required' => 'We need to know your email address!',




4        'max' => 'Your email address is too long!'




5    ],




6],




'custom' => [
    'email' => [
        'required' => 'We need to know your email address!',
        'max' => 'Your email address is too long!'
    ],
],

```

### [Specifying Attributes in Language Files](https://laravel.com/docs/12.x/validation#specifying-attribute-in-language-files)
Many of Laravel's built-in error messages include an `:attribute` placeholder that is replaced with the name of the field or attribute under validation. If you would like the `:attribute` portion of your validation message to be replaced with a custom value, you may specify the custom attribute name in the `attributes` array of your `lang/xx/validation.php` language file:
```


1'attributes' => [




2    'email' => 'email address',




3],




'attributes' => [
    'email' => 'email address',
],

```

By default, the Laravel application skeleton does not include the `lang` directory. If you would like to customize Laravel's language files, you may publish them via the `lang:publish` Artisan command.
### [Specifying Values in Language Files](https://laravel.com/docs/12.x/validation#specifying-values-in-language-files)
Some of Laravel's built-in validation rule error messages contain a `:value` placeholder that is replaced with the current value of the request attribute. However, you may occasionally need the `:value` portion of your validation message to be replaced with a custom representation of the value. For example, consider the following rule that specifies that a credit card number is required if the `payment_type` has a value of `cc`:
```


1Validator::make($request->all(), [




2    'credit_card_number' => 'required_if:payment_type,cc'




3]);




Validator::make($request->all(), [
    'credit_card_number' => 'required_if:payment_type,cc'
]);

```

If this validation rule fails, it will produce the following error message:
```


1The credit card number field is required when payment type is cc.




The credit card number field is required when payment type is cc.

```

Instead of displaying `cc` as the payment type value, you may specify a more user-friendly value representation in your `lang/xx/validation.php` language file by defining a `values` array:
```


1'values' => [




2    'payment_type' => [




3        'cc' => 'credit card'




4    ],




5],




'values' => [
    'payment_type' => [
        'cc' => 'credit card'
    ],
],

```

By default, the Laravel application skeleton does not include the `lang` directory. If you would like to customize Laravel's language files, you may publish them via the `lang:publish` Artisan command.
After defining this value, the validation rule will produce the following error message:
```


1The credit card number field is required when payment type is credit card.




The credit card number field is required when payment type is credit card.

```
