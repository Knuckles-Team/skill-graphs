## [Conditionally Adding Rules](https://laravel.com/docs/12.x/validation#conditionally-adding-rules)
#### [Skipping Validation When Fields Have Certain Values](https://laravel.com/docs/12.x/validation#skipping-validation-when-fields-have-certain-values)
You may occasionally wish to not validate a given field if another field has a given value. You may accomplish this using the `exclude_if` validation rule. In this example, the `appointment_date` and `doctor_name` fields will not be validated if the `has_appointment` field has a value of `false`:
```


1use Illuminate\Support\Facades\Validator;




2 



3$validator = Validator::make($data, [




4    'has_appointment' => 'required|boolean',




5    'appointment_date' => 'exclude_if:has_appointment,false|required|date',




6    'doctor_name' => 'exclude_if:has_appointment,false|required|string',




7]);




use Illuminate\Support\Facades\Validator;

$validator = Validator::make($data, [
    'has_appointment' => 'required|boolean',
    'appointment_date' => 'exclude_if:has_appointment,false|required|date',
    'doctor_name' => 'exclude_if:has_appointment,false|required|string',
]);

```

Alternatively, you may use the `exclude_unless` rule to not validate a given field unless another field has a given value:
```


1$validator = Validator::make($data, [




2    'has_appointment' => 'required|boolean',




3    'appointment_date' => 'exclude_unless:has_appointment,true|required|date',




4    'doctor_name' => 'exclude_unless:has_appointment,true|required|string',




5]);




$validator = Validator::make($data, [
    'has_appointment' => 'required|boolean',
    'appointment_date' => 'exclude_unless:has_appointment,true|required|date',
    'doctor_name' => 'exclude_unless:has_appointment,true|required|string',
]);

```

#### [Validating When Present](https://laravel.com/docs/12.x/validation#validating-when-present)
In some situations, you may wish to run validation checks against a field **only** if that field is present in the data being validated. To quickly accomplish this, add the `sometimes` rule to your rule list:
```


1$validator = Validator::make($data, [




2    'email' => 'sometimes|required|email',




3]);




$validator = Validator::make($data, [
    'email' => 'sometimes|required|email',
]);

```

In the example above, the `email` field will only be validated if it is present in the `$data` array.
If you are attempting to validate a field that should always be present but may be empty, check out [this note on optional fields](https://laravel.com/docs/12.x/validation#a-note-on-optional-fields).
#### [Complex Conditional Validation](https://laravel.com/docs/12.x/validation#complex-conditional-validation)
Sometimes you may wish to add validation rules based on more complex conditional logic. For example, you may wish to require a given field only if another field has a greater value than 100. Or, you may need two fields to have a given value only when another field is present. Adding these validation rules doesn't have to be a pain. First, create a `Validator` instance with your _static rules_ that never change:
```


1use Illuminate\Support\Facades\Validator;




2 



3$validator = Validator::make($request->all(), [




4    'email' => 'required|email',




5    'games' => 'required|integer|min:0',




6]);




use Illuminate\Support\Facades\Validator;

$validator = Validator::make($request->all(), [
    'email' => 'required|email',
    'games' => 'required|integer|min:0',
]);

```

Let's assume our web application is for game collectors. If a game collector registers with our application and they own more than 100 games, we want them to explain why they own so many games. For example, perhaps they run a game resale shop, or maybe they just enjoy collecting games. To conditionally add this requirement, we can use the `sometimes` method on the `Validator` instance.
```


1use Illuminate\Support\Fluent;




2 



3$validator->sometimes('reason', 'required|max:500', function (Fluent $input) {




4    return $input->games >= 100;




5});




use Illuminate\Support\Fluent;

$validator->sometimes('reason', 'required|max:500', function (Fluent $input) {
    return $input->games >= 100;
});

```

The first argument passed to the `sometimes` method is the name of the field we are conditionally validating. The second argument is a list of the rules we want to add. If the closure passed as the third argument returns `true`, the rules will be added. This method makes it a breeze to build complex conditional validations. You may even add conditional validations for several fields at once:
```


1$validator->sometimes(['reason', 'cost'], 'required', function (Fluent $input) {




2    return $input->games >= 100;




3});




$validator->sometimes(['reason', 'cost'], 'required', function (Fluent $input) {
    return $input->games >= 100;
});

```

The `$input` parameter passed to your closure will be an instance of `Illuminate\Support\Fluent` and may be used to access your input and files under validation.
#### [Complex Conditional Array Validation](https://laravel.com/docs/12.x/validation#complex-conditional-array-validation)
Sometimes you may want to validate a field based on another field in the same nested array whose index you do not know. In these situations, you may allow your closure to receive a second argument which will be the current individual item in the array being validated:
```


 1$input = [




 2    'channels' => [




 3        [




 4            'type' => 'email',




 5            'address' => 'abigail@example.com',




 6        ],




 7        [




 8            'type' => 'url',




 9            'address' => 'https://example.com',




10        ],




11    ],




12];




13 



14$validator->sometimes('channels.*.address', 'email', function (Fluent $input, Fluent $item) {




15    return $item->type === 'email';




16});




17 



18$validator->sometimes('channels.*.address', 'url', function (Fluent $input, Fluent $item) {




19    return $item->type !== 'email';




20});




$input = [
    'channels' => [
        [
            'type' => 'email',
            'address' => 'abigail@example.com',
        ],
        [
            'type' => 'url',
            'address' => 'https://example.com',
        ],
    ],
];

$validator->sometimes('channels.*.address', 'email', function (Fluent $input, Fluent $item) {
    return $item->type === 'email';
});

$validator->sometimes('channels.*.address', 'url', function (Fluent $input, Fluent $item) {
    return $item->type !== 'email';
});

```

Like the `$input` parameter passed to the closure, the `$item` parameter is an instance of `Illuminate\Support\Fluent` when the attribute data is an array; otherwise, it is a string.
