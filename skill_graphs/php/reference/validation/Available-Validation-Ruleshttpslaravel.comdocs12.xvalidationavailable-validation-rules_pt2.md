```


1'email' => 'email:rfc,dns'




'email' => 'email:rfc,dns'

```

The example above will apply the `RFCValidation` and `DNSCheckValidation` validations. Here's a full list of validation styles you can apply:
  * `rfc`: `RFCValidation` - Validate the email address according to
  * `strict`: `NoRFCWarningsValidation` - Validate the email according to
  * `dns`: `DNSCheckValidation` - Ensure the email address's domain has a valid MX record.
  * `spoof`: `SpoofCheckValidation` - Ensure the email address does not contain homograph or deceptive Unicode characters.
  * `filter`: `FilterEmailValidation` - Ensure the email address is valid according to PHP's `filter_var` function.
  * `filter_unicode`: `FilterEmailValidation::unicode()` - Ensure the email address is valid according to PHP's `filter_var` function, allowing some Unicode characters.


For convenience, email validation rules may be built using the fluent rule builder:
```


 1use Illuminate\Validation\Rule;




 2 



 3$request->validate([




 4    'email' => [




 5        'required',




 6        Rule::email()




 7            ->rfcCompliant(strict: false)




 8            ->validateMxRecord()




 9            ->preventSpoofing()




10    ],




11]);




use Illuminate\Validation\Rule;

$request->validate([
    'email' => [
        'required',
        Rule::email()
            ->rfcCompliant(strict: false)
            ->validateMxRecord()
            ->preventSpoofing()
    ],
]);

```

The `dns` and `spoof` validators require the PHP `intl` extension.
#### [encoding:_encoding_type_](https://laravel.com/docs/12.x/validation#rule-encoding)
The field under validation must match the specified character encoding. This rule uses PHP's `mb_check_encoding` function to verify the encoding of the given file or string value. For convenience, the `encoding` rule may be constructed using Laravel's fluent file rule builder:
```


 1use Illuminate\Support\Facades\Validator;




 2use Illuminate\Validation\Rules\File;




 3 



 4Validator::validate($input, [




 5    'attachment' => [




 6        'required',




 7        File::types(['csv'])




 8            ->encoding('utf-8'),




 9    ],




10]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rules\File;

Validator::validate($input, [
    'attachment' => [
        'required',
        File::types(['csv'])
            ->encoding('utf-8'),
    ],
]);

```

#### [ends_with:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-ends-with)
The field under validation must end with one of the given values.
#### [enum](https://laravel.com/docs/12.x/validation#rule-enum)
The `Enum` rule is a class-based rule that validates whether the field under validation contains a valid enum value. The `Enum` rule accepts the name of the enum as its only constructor argument. When validating primitive values, a backed Enum should be provided to the `Enum` rule:
```


1use App\Enums\ServerStatus;




2use Illuminate\Validation\Rule;




3 



4$request->validate([




5    'status' => [Rule::enum(ServerStatus::class)],




6]);




use App\Enums\ServerStatus;
use Illuminate\Validation\Rule;

$request->validate([
    'status' => [Rule::enum(ServerStatus::class)],
]);

```

The `Enum` rule's `only` and `except` methods may be used to limit which enum cases should be considered valid:
```


1Rule::enum(ServerStatus::class)




2    ->only([ServerStatus::Pending, ServerStatus::Active]);




3 



4Rule::enum(ServerStatus::class)




5    ->except([ServerStatus::Pending, ServerStatus::Active]);




Rule::enum(ServerStatus::class)
    ->only([ServerStatus::Pending, ServerStatus::Active]);

Rule::enum(ServerStatus::class)
    ->except([ServerStatus::Pending, ServerStatus::Active]);

```

The `when` method may be used to conditionally modify the `Enum` rule:
```


1use Illuminate\Support\Facades\Auth;




2use Illuminate\Validation\Rule;




3 



4Rule::enum(ServerStatus::class)




5    ->when(




6        Auth::user()->isAdmin(),




7        fn ($rule) => $rule->only(...),




8        fn ($rule) => $rule->only(...),




9    );




use Illuminate\Support\Facades\Auth;
use Illuminate\Validation\Rule;

Rule::enum(ServerStatus::class)
    ->when(
        Auth::user()->isAdmin(),
        fn ($rule) => $rule->only(...),
        fn ($rule) => $rule->only(...),
    );

```

#### [exclude](https://laravel.com/docs/12.x/validation#rule-exclude)
The field under validation will be excluded from the request data returned by the `validate` and `validated` methods.
#### [exclude_if:_anotherfield_ ,_value_](https://laravel.com/docs/12.x/validation#rule-exclude-if)
The field under validation will be excluded from the request data returned by the `validate` and `validated` methods if the _anotherfield_ field is equal to _value_.
If complex conditional exclusion logic is required, you may utilize the `Rule::excludeIf` method. This method accepts a boolean or a closure. When given a closure, the closure should return `true` or `false` to indicate if the field under validation should be excluded:
```


 1use Illuminate\Support\Facades\Validator;




 2use Illuminate\Validation\Rule;




 3 



 4Validator::make($request->all(), [




 5    'role_id' => Rule::excludeIf($request->user()->is_admin),




 6]);




 7 



 8Validator::make($request->all(), [




 9    'role_id' => Rule::excludeIf(fn () => $request->user()->is_admin),




10]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

Validator::make($request->all(), [
    'role_id' => Rule::excludeIf($request->user()->is_admin),
]);

Validator::make($request->all(), [
    'role_id' => Rule::excludeIf(fn () => $request->user()->is_admin),
]);

```

#### [exclude_unless:_anotherfield_ ,_value_](https://laravel.com/docs/12.x/validation#rule-exclude-unless)
The field under validation will be excluded from the request data returned by the `validate` and `validated` methods unless _anotherfield_ 's field is equal to _value_. If _value_ is `null` (`exclude_unless:name,null`), the field under validation will be excluded unless the comparison field is `null` or the comparison field is missing from the request data.
#### [exclude_with:_anotherfield_](https://laravel.com/docs/12.x/validation#rule-exclude-with)
The field under validation will be excluded from the request data returned by the `validate` and `validated` methods if the _anotherfield_ field is present.
#### [exclude_without:_anotherfield_](https://laravel.com/docs/12.x/validation#rule-exclude-without)
The field under validation will be excluded from the request data returned by the `validate` and `validated` methods if the _anotherfield_ field is not present.
#### [exists:_table_ ,_column_](https://laravel.com/docs/12.x/validation#rule-exists)
The field under validation must exist in a given database table.
#### [Basic Usage of Exists Rule](https://laravel.com/docs/12.x/validation#basic-usage-of-exists-rule)
```


1'state' => 'exists:states'




'state' => 'exists:states'

```

If the `column` option is not specified, the field name will be used. So, in this case, the rule will validate that the `states` database table contains a record with a `state` column value matching the request's `state` attribute value.
#### [Specifying a Custom Column Name](https://laravel.com/docs/12.x/validation#specifying-a-custom-column-name)
You may explicitly specify the database column name that should be used by the validation rule by placing it after the database table name:
```


1'state' => 'exists:states,abbreviation'




'state' => 'exists:states,abbreviation'

```

Occasionally, you may need to specify a specific database connection to be used for the `exists` query. You can accomplish this by prepending the connection name to the table name:
```


1'email' => 'exists:connection.staff,email'




'email' => 'exists:connection.staff,email'

```

Instead of specifying the table name directly, you may specify the Eloquent model which should be used to determine the table name:
```


1'user_id' => 'exists:App\Models\User,id'




'user_id' => 'exists:App\Models\User,id'

```

If you would like to customize the query executed by the validation rule, you may use the `Rule` class to fluently define the rule. In this example, we'll also specify the validation rules as an array instead of using the `|` character to delimit them:
```


 1use Illuminate\Database\Query\Builder;




 2use Illuminate\Support\Facades\Validator;




 3use Illuminate\Validation\Rule;




 4 



 5Validator::make($data, [




 6    'email' => [




 7        'required',




 8        Rule::exists('staff')->where(function (Builder $query) {




 9            $query->where('account_id', 1);




10        }),




11    ],




12]);




use Illuminate\Database\Query\Builder;
use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

Validator::make($data, [
    'email' => [
        'required',
        Rule::exists('staff')->where(function (Builder $query) {
            $query->where('account_id', 1);
        }),
    ],
]);

```

You may explicitly specify the database column name that should be used by the `exists` rule generated by the `Rule::exists` method by providing the column name as the second argument to the `exists` method:
```


1'state' => Rule::exists('states', 'abbreviation'),




'state' => Rule::exists('states', 'abbreviation'),

```

Sometimes, you may wish to validate whether an array of values exists in the database. You can do so by adding both the `exists` and [array](https://laravel.com/docs/12.x/validation#rule-array) rules to the field being validated:
```


1'states' => ['array', Rule::exists('states', 'abbreviation')],




'states' => ['array', Rule::exists('states', 'abbreviation')],

```

When both of these rules are assigned to a field, Laravel will automatically build a single query to determine if all of the given values exist in the specified table.
#### [extensions:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-extensions)
The file under validation must have a user-assigned extension corresponding to one of the listed extensions:
```


1'photo' => ['required', 'extensions:jpg,png'],




'photo' => ['required', 'extensions:jpg,png'],

```

You should never rely on validating a file by its user-assigned extension alone. This rule should typically always be used in combination with the [mimes](https://laravel.com/docs/12.x/validation#rule-mimes) or [mimetypes](https://laravel.com/docs/12.x/validation#rule-mimetypes) rules.
#### [file](https://laravel.com/docs/12.x/validation#rule-file)
The field under validation must be a successfully uploaded file.
#### [filled](https://laravel.com/docs/12.x/validation#rule-filled)
The field under validation must not be empty when it is present.
#### [gt:_field_](https://laravel.com/docs/12.x/validation#rule-gt)
The field under validation must be greater than the given _field_ or _value_. The two fields must be of the same type. Strings, numerics, arrays, and files are evaluated using the same conventions as the [size](https://laravel.com/docs/12.x/validation#rule-size) rule.
#### [gte:_field_](https://laravel.com/docs/12.x/validation#rule-gte)
The field under validation must be greater than or equal to the given _field_ or _value_. The two fields must be of the same type. Strings, numerics, arrays, and files are evaluated using the same conventions as the [size](https://laravel.com/docs/12.x/validation#rule-size) rule.
#### [hex_color](https://laravel.com/docs/12.x/validation#rule-hex-color)
The field under validation must contain a valid color value in
#### [image](https://laravel.com/docs/12.x/validation#rule-image)
The file under validation must be an image (jpg, jpeg, png, bmp, gif, or webp).
By default, the image rule does not allow SVG files due to the possibility of XSS vulnerabilities. If you need to allow SVG files, you may provide the `allow_svg` directive to the `image` rule (`image:allow_svg`).
#### [in:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-in)
The field under validation must be included in the given list of values. Since this rule often requires you to `implode` an array, the `Rule::in` method may be used to fluently construct the rule:
```


1use Illuminate\Support\Facades\Validator;




2use Illuminate\Validation\Rule;




3 



4Validator::make($data, [




5    'zones' => [




6        'required',




7        Rule::in(['first-zone', 'second-zone']),




8    ],




9]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

Validator::make($data, [
    'zones' => [
        'required',
        Rule::in(['first-zone', 'second-zone']),
    ],
]);

```

When the `in` rule is combined with the `array` rule, each value in the input array must be present within the list of values provided to the `in` rule. In the following example, the `LAS` airport code in the input array is invalid since it is not contained in the list of airports provided to the `in` rule:
```


 1use Illuminate\Support\Facades\Validator;




 2use Illuminate\Validation\Rule;




 3 



 4$input = [




 5    'airports' => ['NYC', 'LAS'],




 6];




 7 



 8Validator::make($input, [




 9    'airports' => [




10        'required',




11        'array',




12    ],




13    'airports.*' => Rule::in(['NYC', 'LIT']),




14]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

$input = [
    'airports' => ['NYC', 'LAS'],
];

Validator::make($input, [
    'airports' => [
        'required',
        'array',
    ],
    'airports.*' => Rule::in(['NYC', 'LIT']),
]);

```

#### [in_array:_anotherfield_.*](https://laravel.com/docs/12.x/validation#rule-in-array)
The field under validation must exist in _anotherfield_ 's values.
#### [in_array_keys:_value_.*](https://laravel.com/docs/12.x/validation#rule-in-array-keys)
The field under validation must be an array having at least one of the given _values_ as a key within the array:
```


1'config' => 'array|in_array_keys:timezone'




'config' => 'array|in_array_keys:timezone'

```

#### [integer](https://laravel.com/docs/12.x/validation#rule-integer)
The field under validation must be an integer.
You may use the `strict` parameter to only consider the field valid if its type is `integer`. Strings with integer values will be considered invalid:
```


1'age' => 'integer:strict'




'age' => 'integer:strict'

```

This validation rule does not verify that the input is of the "integer" variable type, only that the input is of a type accepted by PHP's `FILTER_VALIDATE_INT` rule. If you need to validate the input as being a number please use this rule in combination with [the `numeric` validation rule](https://laravel.com/docs/12.x/validation#rule-numeric).
#### [ip](https://laravel.com/docs/12.x/validation#rule-ip)
The field under validation must be an IP address.
#### [ipv4](https://laravel.com/docs/12.x/validation#ipv4)
The field under validation must be an IPv4 address.
#### [ipv6](https://laravel.com/docs/12.x/validation#ipv6)
The field under validation must be an IPv6 address.
#### [json](https://laravel.com/docs/12.x/validation#rule-json)
The field under validation must be a valid JSON string.
#### [lt:_field_](https://laravel.com/docs/12.x/validation#rule-lt)
The field under validation must be less than the given _field_. The two fields must be of the same type. Strings, numerics, arrays, and files are evaluated using the same conventions as the [size](https://laravel.com/docs/12.x/validation#rule-size) rule.
#### [lte:_field_](https://laravel.com/docs/12.x/validation#rule-lte)
The field under validation must be less than or equal to the given _field_. The two fields must be of the same type. Strings, numerics, arrays, and files are evaluated using the same conventions as the [size](https://laravel.com/docs/12.x/validation#rule-size) rule.
#### [lowercase](https://laravel.com/docs/12.x/validation#rule-lowercase)
The field under validation must be lowercase.
#### [list](https://laravel.com/docs/12.x/validation#rule-list)
The field under validation must be an array that is a list. An array is considered a list if its keys consist of consecutive numbers from 0 to `count($array) - 1`.
#### [mac_address](https://laravel.com/docs/12.x/validation#rule-mac)
The field under validation must be a MAC address.
#### [max:_value_](https://laravel.com/docs/12.x/validation#rule-max)
The field under validation must be less than or equal to a maximum _value_. Strings, numerics, arrays, and files are evaluated in the same fashion as the [size](https://laravel.com/docs/12.x/validation#rule-size) rule.
#### [max_digits:_value_](https://laravel.com/docs/12.x/validation#rule-max-digits)
The integer under validation must have a maximum length of _value_.
#### [mimetypes:_text/plain_ ,...](https://laravel.com/docs/12.x/validation#rule-mimetypes)
The file under validation must match one of the given MIME types:
```


1'video' => 'mimetypes:video/avi,video/mpeg,video/quicktime',




2 



3'media' => 'mimetypes:image/*,video/*',




'video' => 'mimetypes:video/avi,video/mpeg,video/quicktime',

'media' => 'mimetypes:image/*,video/*',

```

To determine the MIME type of the uploaded file, the file's contents will be read and the framework will attempt to guess the MIME type, which may be different from the client's provided MIME type.
#### [mimes:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-mimes)
The file under validation must have a MIME type corresponding to one of the listed extensions:
```


1'photo' => 'mimes:jpg,bmp,png'




'photo' => 'mimes:jpg,bmp,png'

```

Even though you only need to specify the extensions, this rule actually validates the MIME type of the file by reading the file's contents and guessing its MIME type. A full listing of MIME types and their corresponding extensions may be found at the following location:
#### [MIME Types and Extensions](https://laravel.com/docs/12.x/validation#mime-types-and-extensions)
This validation rule does not verify agreement between the MIME type and the extension the user assigned to the file. For example, the `mimes:png` validation rule would consider a file containing valid PNG content to be a valid PNG image, even if the file is named `photo.txt`. If you would like to validate the user-assigned extension of the file, you may use the [extensions](https://laravel.com/docs/12.x/validation#rule-extensions) rule.
#### [min:_value_](https://laravel.com/docs/12.x/validation#rule-min)
The field under validation must have a minimum _value_. Strings, numerics, arrays, and files are evaluated in the same fashion as the [size](https://laravel.com/docs/12.x/validation#rule-size) rule.
#### [min_digits:_value_](https://laravel.com/docs/12.x/validation#rule-min-digits)
The integer under validation must have a minimum length of _value_.
#### [multiple_of:_value_](https://laravel.com/docs/12.x/validation#rule-multiple-of)
The field under validation must be a multiple of _value_.
#### [missing](https://laravel.com/docs/12.x/validation#rule-missing)
The field under validation must not be present in the input data.
#### [missing_if:_anotherfield_ ,_value_ ,...](https://laravel.com/docs/12.x/validation#rule-missing-if)
The field under validation must not be present if the _anotherfield_ field is equal to any _value_.
#### [missing_unless:_anotherfield_ ,_value_](https://laravel.com/docs/12.x/validation#rule-missing-unless)
The field under validation must not be present unless the _anotherfield_ field is equal to any _value_.
#### [missing_with:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-missing-with)
The field under validation must not be present _only if_ any of the other specified fields are present.
#### [missing_with_all:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-missing-with-all)
The field under validation must not be present _only if_ all of the other specified fields are present.
#### [not_in:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-not-in)
The field under validation must not be included in the given list of values. The `Rule::notIn` method may be used to fluently construct the rule:
```


1use Illuminate\Validation\Rule;




2 



3Validator::make($data, [




4    'toppings' => [




5        'required',




6        Rule::notIn(['sprinkles', 'cherries']),




7    ],




8]);




use Illuminate\Validation\Rule;

Validator::make($data, [
    'toppings' => [
        'required',
        Rule::notIn(['sprinkles', 'cherries']),
    ],
]);

```

#### [not_regex:_pattern_](https://laravel.com/docs/12.x/validation#rule-not-regex)
The field under validation must not match the given regular expression.
Internally, this rule uses the PHP `preg_match` function. The pattern specified should obey the same formatting required by `preg_match` and thus also include valid delimiters. For example: `'email' => 'not_regex:/^.+$/i'`.
When using the `regex` / `not_regex` patterns, it may be necessary to specify your validation rules using an array instead of using `|` delimiters, especially if the regular expression contains a `|` character.
#### [nullable](https://laravel.com/docs/12.x/validation#rule-nullable)
The field under validation may be `null`.
#### [numeric](https://laravel.com/docs/12.x/validation#rule-numeric)
The field under validation must be
You may use the `strict` parameter to only consider the field valid if its value is an integer or float type. Numeric strings will be considered invalid:
```


1'amount' => 'numeric:strict'




'amount' => 'numeric:strict'

```

#### [present](https://laravel.com/docs/12.x/validation#rule-present)
The field under validation must exist in the input data.
#### [present_if:_anotherfield_ ,_value_ ,...](https://laravel.com/docs/12.x/validation#rule-present-if)
The field under validation must be present if the _anotherfield_ field is equal to any _value_.
#### [present_unless:_anotherfield_ ,_value_](https://laravel.com/docs/12.x/validation#rule-present-unless)
The field under validation must be present unless the _anotherfield_ field is equal to any _value_.
#### [present_with:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-present-with)
The field under validation must be present _only if_ any of the other specified fields are present.
#### [present_with_all:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-present-with-all)
The field under validation must be present _only if_ all of the other specified fields are present.
#### [prohibited](https://laravel.com/docs/12.x/validation#rule-prohibited)
The field under validation must be missing or empty. A field is "empty" if it meets one of the following criteria:
  * The value is `null`.
  * The value is an empty string.
  * The value is an empty array or empty `Countable` object.
  * The value is an uploaded file with an empty path.


#### [prohibited_if:_anotherfield_ ,_value_ ,...](https://laravel.com/docs/12.x/validation#rule-prohibited-if)
The field under validation must be missing or empty if the _anotherfield_ field is equal to any _value_. A field is "empty" if it meets one of the following criteria:
  * The value is `null`.
  * The value is an empty string.
  * The value is an empty array or empty `Countable` object.
  * The value is an uploaded file with an empty path.


If complex conditional prohibition logic is required, you may utilize the `Rule::prohibitedIf` method. This method accepts a boolean or a closure. When given a closure, the closure should return `true` or `false` to indicate if the field under validation should be prohibited:
```


 1use Illuminate\Support\Facades\Validator;




 2use Illuminate\Validation\Rule;




 3 



 4Validator::make($request->all(), [




 5    'role_id' => Rule::prohibitedIf($request->user()->is_admin),




 6]);




 7 



 8Validator::make($request->all(), [




 9    'role_id' => Rule::prohibitedIf(fn () => $request->user()->is_admin),




10]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

Validator::make($request->all(), [
    'role_id' => Rule::prohibitedIf($request->user()->is_admin),
]);

Validator::make($request->all(), [
    'role_id' => Rule::prohibitedIf(fn () => $request->user()->is_admin),
]);

```

#### [prohibited_if_accepted:_anotherfield_ ,...](https://laravel.com/docs/12.x/validation#rule-prohibited-if-accepted)
The field under validation must be missing or empty if the _anotherfield_ field is equal to `"yes"`, `"on"`, `1`, `"1"`, `true`, or `"true"`.
#### [prohibited_if_declined:_anotherfield_ ,...](https://laravel.com/docs/12.x/validation#rule-prohibited-if-declined)
The field under validation must be missing or empty if the _anotherfield_ field is equal to `"no"`, `"off"`, `0`, `"0"`, `false`, or `"false"`.
#### [prohibited_unless:_anotherfield_ ,_value_ ,...](https://laravel.com/docs/12.x/validation#rule-prohibited-unless)
The field under validation must be missing or empty unless the _anotherfield_ field is equal to any _value_. A field is "empty" if it meets one of the following criteria:
  * The value is `null`.
  * The value is an empty string.
  * The value is an empty array or empty `Countable` object.
  * The value is an uploaded file with an empty path.


#### [prohibits:_anotherfield_ ,...](https://laravel.com/docs/12.x/validation#rule-prohibits)
If the field under validation is not missing or empty, all fields in _anotherfield_ must be missing or empty. A field is "empty" if it meets one of the following criteria:
