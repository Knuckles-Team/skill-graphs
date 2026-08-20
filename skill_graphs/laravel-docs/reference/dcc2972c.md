## [Manually Creating Validators](https://laravel.com/docs/12.x/validation#manually-creating-validators)
If you do not want to use the `validate` method on the request, you may create a validator instance manually using the `Validator` [facade](https://laravel.com/docs/12.x/facades). The `make` method on the facade generates a new validator instance:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Http\RedirectResponse;




 6use Illuminate\Http\Request;




 7use Illuminate\Support\Facades\Validator;




 8 



 9class PostController extends Controller




10{




11    /**




12     * Store a new blog post.




13     */




14    public function store(Request $request): RedirectResponse




15    {




16        $validator = Validator::make($request->all(), [




17            'title' => 'required|unique:posts|max:255',




18            'body' => 'required',




19        ]);




20 



21        if ($validator->fails()) {




22            return redirect('/post/create')




23                ->withErrors($validator)




24                ->withInput();




25        }




26 



27        // Retrieve the validated input...




28        $validated = $validator->validated();




29 



30        // Retrieve a portion of the validated input...




31        $validated = $validator->safe()->only(['name', 'email']);




32        $validated = $validator->safe()->except(['name', 'email']);




33 



34        // Store the blog post...




35 



36        return redirect('/posts');




37    }




38}




<?php

namespace App\Http\Controllers;

use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class PostController extends Controller
{
    /**
     * Store a new blog post.
     */
    public function store(Request $request): RedirectResponse
    {
        $validator = Validator::make($request->all(), [
            'title' => 'required|unique:posts|max:255',
            'body' => 'required',
        ]);

        if ($validator->fails()) {
            return redirect('/post/create')
                ->withErrors($validator)
                ->withInput();
        }

        // Retrieve the validated input...
        $validated = $validator->validated();

        // Retrieve a portion of the validated input...
        $validated = $validator->safe()->only(['name', 'email']);
        $validated = $validator->safe()->except(['name', 'email']);

        // Store the blog post...

        return redirect('/posts');
    }
}

```

The first argument passed to the `make` method is the data under validation. The second argument is an array of the validation rules that should be applied to the data.
After determining whether the request validation failed, you may use the `withErrors` method to flash the error messages to the session. When using this method, the `$errors` variable will automatically be shared with your views after redirection, allowing you to easily display them back to the user. The `withErrors` method accepts a validator, a `MessageBag`, or a PHP `array`.
#### Stopping on First Validation Failure
The `stopOnFirstFailure` method will inform the validator that it should stop validating all attributes once a single validation failure has occurred:
```


1if ($validator->stopOnFirstFailure()->fails()) {




2    // ...




3}




if ($validator->stopOnFirstFailure()->fails()) {
    // ...
}

```

### [Automatic Redirection](https://laravel.com/docs/12.x/validation#automatic-redirection)
If you would like to create a validator instance manually but still take advantage of the automatic redirection offered by the HTTP request's `validate` method, you may call the `validate` method on an existing validator instance. If validation fails, the user will automatically be redirected or, in the case of an XHR request, a [JSON response will be returned](https://laravel.com/docs/12.x/validation#validation-error-response-format):
```


1Validator::make($request->all(), [




2    'title' => 'required|unique:posts|max:255',




3    'body' => 'required',




4])->validate();




Validator::make($request->all(), [
    'title' => 'required|unique:posts|max:255',
    'body' => 'required',
])->validate();

```

You may use the `validateWithBag` method to store the error messages in a [named error bag](https://laravel.com/docs/12.x/validation#named-error-bags) if validation fails:
```


1Validator::make($request->all(), [




2    'title' => 'required|unique:posts|max:255',




3    'body' => 'required',




4])->validateWithBag('post');




Validator::make($request->all(), [
    'title' => 'required|unique:posts|max:255',
    'body' => 'required',
])->validateWithBag('post');

```

### [Named Error Bags](https://laravel.com/docs/12.x/validation#named-error-bags)
If you have multiple forms on a single page, you may wish to name the `MessageBag` containing the validation errors, allowing you to retrieve the error messages for a specific form. To achieve this, pass a name as the second argument to `withErrors`:
```


1return redirect('/register')->withErrors($validator, 'login');




return redirect('/register')->withErrors($validator, 'login');

```

You may then access the named `MessageBag` instance from the `$errors` variable:
```


1{{ $errors->login->first('email') }}




{{ $errors->login->first('email') }}

```

### [Customizing the Error Messages](https://laravel.com/docs/12.x/validation#manual-customizing-the-error-messages)
If needed, you may provide custom error messages that a validator instance should use instead of the default error messages provided by Laravel. There are several ways to specify custom messages. First, you may pass the custom messages as the third argument to the `Validator::make` method:
```


1$validator = Validator::make($input, $rules, $messages = [




2    'required' => 'The :attribute field is required.',




3]);




$validator = Validator::make($input, $rules, $messages = [
    'required' => 'The :attribute field is required.',
]);

```

In this example, the `:attribute` placeholder will be replaced by the actual name of the field under validation. You may also utilize other placeholders in validation messages. For example:
```


1$messages = [




2    'same' => 'The :attribute and :other must match.',




3    'size' => 'The :attribute must be exactly :size.',




4    'between' => 'The :attribute value :input is not between :min - :max.',




5    'in' => 'The :attribute must be one of the following types: :values',




6];




$messages = [
    'same' => 'The :attribute and :other must match.',
    'size' => 'The :attribute must be exactly :size.',
    'between' => 'The :attribute value :input is not between :min - :max.',
    'in' => 'The :attribute must be one of the following types: :values',
];

```

#### [Specifying a Custom Message for a Given Attribute](https://laravel.com/docs/12.x/validation#specifying-a-custom-message-for-a-given-attribute)
Sometimes you may wish to specify a custom error message only for a specific attribute. You may do so using "dot" notation. Specify the attribute's name first, followed by the rule:
```


1$messages = [




2    'email.required' => 'We need to know your email address!',




3];




$messages = [
    'email.required' => 'We need to know your email address!',
];

```

#### [Specifying Custom Attribute Values](https://laravel.com/docs/12.x/validation#specifying-custom-attribute-values)
Many of Laravel's built-in error messages include an `:attribute` placeholder that is replaced with the name of the field or attribute under validation. To customize the values used to replace these placeholders for specific fields, you may pass an array of custom attributes as the fourth argument to the `Validator::make` method:
```


1$validator = Validator::make($input, $rules, $messages, [




2    'email' => 'email address',




3]);




$validator = Validator::make($input, $rules, $messages, [
    'email' => 'email address',
]);

```

### [Performing Additional Validation](https://laravel.com/docs/12.x/validation#performing-additional-validation)
Sometimes you need to perform additional validation after your initial validation is complete. You can accomplish this using the validator's `after` method. The `after` method accepts a closure or an array of callables which will be invoked after validation is complete. The given callables will receive an `Illuminate\Validation\Validator` instance, allowing you to raise additional error messages if necessary:
```


 1use Illuminate\Support\Facades\Validator;




 2 



 3$validator = Validator::make(/* ... */);




 4 



 5$validator->after(function ($validator) {




 6    if ($this->somethingElseIsInvalid()) {




 7        $validator->errors()->add(




 8            'field', 'Something is wrong with this field!'




 9        );




10    }




11});




12 



13if ($validator->fails()) {




14    // ...




15}




use Illuminate\Support\Facades\Validator;

$validator = Validator::make(/* ... */);

$validator->after(function ($validator) {
    if ($this->somethingElseIsInvalid()) {
        $validator->errors()->add(
            'field', 'Something is wrong with this field!'
        );
    }
});

if ($validator->fails()) {
    // ...
}

```

As noted, the `after` method also accepts an array of callables, which is particularly convenient if your "after validation" logic is encapsulated in invocable classes, which will receive an `Illuminate\Validation\Validator` instance via their `__invoke` method:
```


 1use App\Validation\ValidateShippingTime;




 2use App\Validation\ValidateUserStatus;




 3 



 4$validator->after([




 5    new ValidateUserStatus,




 6    new ValidateShippingTime,




 7    function ($validator) {




 8        // ...




 9    },




10]);




use App\Validation\ValidateShippingTime;
use App\Validation\ValidateUserStatus;

$validator->after([
    new ValidateUserStatus,
    new ValidateShippingTime,
    function ($validator) {
        // ...
    },
]);

```
