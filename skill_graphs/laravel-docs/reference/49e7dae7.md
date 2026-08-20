## [Validating Arrays](https://laravel.com/docs/12.x/validation#validating-arrays)
As discussed in the [array validation rule documentation](https://laravel.com/docs/12.x/validation#rule-array), the `array` rule accepts a list of allowed array keys. If any additional keys are present within the array, validation will fail:
```


 1use Illuminate\Support\Facades\Validator;




 2 



 3$input = [




 4    'user' => [




 5        'name' => 'Taylor Otwell',




 6        'username' => 'taylorotwell',




 7        'admin' => true,




 8    ],




 9];




10 



11Validator::make($input, [




12    'user' => 'array:name,username',




13]);




use Illuminate\Support\Facades\Validator;

$input = [
    'user' => [
        'name' => 'Taylor Otwell',
        'username' => 'taylorotwell',
        'admin' => true,
    ],
];

Validator::make($input, [
    'user' => 'array:name,username',
]);

```

In general, you should always specify the array keys that are allowed to be present within your array. Otherwise, the validator's `validate` and `validated` methods will return all of the validated data, including the array and all of its keys, even if those keys were not validated by other nested array validation rules.
### [Validating Nested Array Input](https://laravel.com/docs/12.x/validation#validating-nested-array-input)
Validating nested array-based form input fields doesn't have to be a pain. You may use "dot notation" to validate attributes within an array. For example, if the incoming HTTP request contains a `photos[profile]` field, you may validate it like so:
```


1use Illuminate\Support\Facades\Validator;




2 



3$validator = Validator::make($request->all(), [




4    'photos.profile' => 'required|image',




5]);




use Illuminate\Support\Facades\Validator;

$validator = Validator::make($request->all(), [
    'photos.profile' => 'required|image',
]);

```

You may also validate each element of an array. For example, to validate that each email in a given array input field is unique, you may do the following:
```


1$validator = Validator::make($request->all(), [




2    'users.*.email' => 'email|unique:users',




3    'users.*.first_name' => 'required_with:users.*.last_name',




4]);




$validator = Validator::make($request->all(), [
    'users.*.email' => 'email|unique:users',
    'users.*.first_name' => 'required_with:users.*.last_name',
]);

```

Likewise, you may use the `*` character when specifying [custom validation messages in your language files](https://laravel.com/docs/12.x/validation#custom-messages-for-specific-attributes), making it a breeze to use a single validation message for array-based fields:
```


1'custom' => [




2    'users.*.email' => [




3        'unique' => 'Each user must have a unique email address',




4    ]




5],




'custom' => [
    'users.*.email' => [
        'unique' => 'Each user must have a unique email address',
    ]
],

```

#### [Accessing Nested Array Data](https://laravel.com/docs/12.x/validation#accessing-nested-array-data)
Sometimes you may need to access the value for a given nested array element when assigning validation rules to the attribute. You may accomplish this using the `Rule::forEach` method. The `forEach` method accepts a closure that will be invoked for each iteration of the array attribute under validation and will receive the attribute's value and explicit, fully-expanded attribute name. The closure should return an array of rules to assign to the array element:
```


 1use App\Rules\HasPermission;




 2use Illuminate\Support\Facades\Validator;




 3use Illuminate\Validation\Rule;




 4 



 5$validator = Validator::make($request->all(), [




 6    'companies.*.id' => Rule::forEach(function (string|null $value, string $attribute) {




 7        return [




 8            Rule::exists(Company::class, 'id'),




 9            new HasPermission('manage-company', $value),




10        ];




11    }),




12]);




use App\Rules\HasPermission;
use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

$validator = Validator::make($request->all(), [
    'companies.*.id' => Rule::forEach(function (string|null $value, string $attribute) {
        return [
            Rule::exists(Company::class, 'id'),
            new HasPermission('manage-company', $value),
        ];
    }),
]);

```

### [Error Message Indexes and Positions](https://laravel.com/docs/12.x/validation#error-message-indexes-and-positions)
When validating arrays, you may want to reference the index or position of a particular item that failed validation within the error message displayed by your application. To accomplish this, you may include the `:index` (starts from `0`), `:position` (starts from `1`), or `:ordinal-position` (starts from `1st`) placeholders within your [custom validation message](https://laravel.com/docs/12.x/validation#manual-customizing-the-error-messages):
```


 1use Illuminate\Support\Facades\Validator;




 2 



 3$input = [




 4    'photos' => [




 5        [




 6            'name' => 'BeachVacation.jpg',




 7            'description' => 'A photo of my beach vacation!',




 8        ],




 9        [




10            'name' => 'GrandCanyon.jpg',




11            'description' => '',




12        ],




13    ],




14];




15 



16Validator::validate($input, [




17    'photos.*.description' => 'required',




18], [




19    'photos.*.description.required' => 'Please describe photo #:position.',




20]);




use Illuminate\Support\Facades\Validator;

$input = [
    'photos' => [
        [
            'name' => 'BeachVacation.jpg',
            'description' => 'A photo of my beach vacation!',
        ],
        [
            'name' => 'GrandCanyon.jpg',
            'description' => '',
        ],
    ],
];

Validator::validate($input, [
    'photos.*.description' => 'required',
], [
    'photos.*.description.required' => 'Please describe photo #:position.',
]);

```

Given the example above, validation will fail and the user will be presented with the following error of _"Please describe photo #2."_
If necessary, you may reference more deeply nested indexes and positions via `second-index`, `second-position`, `third-index`, `third-position`, etc.
```


1'photos.*.attributes.*.string' => 'Invalid attribute for photo #:second-position.',




'photos.*.attributes.*.string' => 'Invalid attribute for photo #:second-position.',

```
