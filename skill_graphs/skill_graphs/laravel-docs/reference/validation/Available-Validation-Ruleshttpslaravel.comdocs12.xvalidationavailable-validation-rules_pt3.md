  * The value is `null`.
  * The value is an empty string.
  * The value is an empty array or empty `Countable` object.
  * The value is an uploaded file with an empty path.


#### [regex:_pattern_](https://laravel.com/docs/12.x/validation#rule-regex)
The field under validation must match the given regular expression.
Internally, this rule uses the PHP `preg_match` function. The pattern specified should obey the same formatting required by `preg_match` and thus also include valid delimiters. For example: `'email' => 'regex:/^.+@.+$/i'`.
When using the `regex` / `not_regex` patterns, it may be necessary to specify rules in an array instead of using `|` delimiters, especially if the regular expression contains a `|` character.
#### [required](https://laravel.com/docs/12.x/validation#rule-required)
The field under validation must be present in the input data and not empty. A field is "empty" if it meets one of the following criteria:
  * The value is `null`.
  * The value is an empty string.
  * The value is an empty array or empty `Countable` object.
  * The value is an uploaded file with no path.


#### [required_if:_anotherfield_ ,_value_ ,...](https://laravel.com/docs/12.x/validation#rule-required-if)
The field under validation must be present and not empty if the _anotherfield_ field is equal to any _value_.
If you would like to construct a more complex condition for the `required_if` rule, you may use the `Rule::requiredIf` method. This method accepts a boolean or a closure. When passed a closure, the closure should return `true` or `false` to indicate if the field under validation is required:
```


 1use Illuminate\Support\Facades\Validator;




 2use Illuminate\Validation\Rule;




 3 



 4Validator::make($request->all(), [




 5    'role_id' => Rule::requiredIf($request->user()->is_admin),




 6]);




 7 



 8Validator::make($request->all(), [




 9    'role_id' => Rule::requiredIf(fn () => $request->user()->is_admin),




10]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

Validator::make($request->all(), [
    'role_id' => Rule::requiredIf($request->user()->is_admin),
]);

Validator::make($request->all(), [
    'role_id' => Rule::requiredIf(fn () => $request->user()->is_admin),
]);

```

#### [required_if_accepted:_anotherfield_ ,...](https://laravel.com/docs/12.x/validation#rule-required-if-accepted)
The field under validation must be present and not empty if the _anotherfield_ field is equal to `"yes"`, `"on"`, `1`, `"1"`, `true`, or `"true"`.
#### [required_if_declined:_anotherfield_ ,...](https://laravel.com/docs/12.x/validation#rule-required-if-declined)
The field under validation must be present and not empty if the _anotherfield_ field is equal to `"no"`, `"off"`, `0`, `"0"`, `false`, or `"false"`.
#### [required_unless:_anotherfield_ ,_value_ ,...](https://laravel.com/docs/12.x/validation#rule-required-unless)
The field under validation must be present and not empty unless the _anotherfield_ field is equal to any _value_. This also means _anotherfield_ must be present in the request data unless _value_ is `null`. If _value_ is `null` (`required_unless:name,null`), the field under validation will be required unless the comparison field is `null` or the comparison field is missing from the request data.
#### [required_with:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-required-with)
The field under validation must be present and not empty _only if_ any of the other specified fields are present and not empty.
#### [required_with_all:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-required-with-all)
The field under validation must be present and not empty _only if_ all of the other specified fields are present and not empty.
#### [required_without:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-required-without)
The field under validation must be present and not empty _only when_ any of the other specified fields are empty or not present.
#### [required_without_all:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-required-without-all)
The field under validation must be present and not empty _only when_ all of the other specified fields are empty or not present.
#### [required_array_keys:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-required-array-keys)
The field under validation must be an array and must contain at least the specified keys.
#### [same:_field_](https://laravel.com/docs/12.x/validation#rule-same)
The given _field_ must match the field under validation.
#### [size:_value_](https://laravel.com/docs/12.x/validation#rule-size)
The field under validation must have a size matching the given _value_. For string data, _value_ corresponds to the number of characters. For numeric data, _value_ corresponds to a given integer value (the attribute must also have the `numeric` or `integer` rule). For an array, _size_ corresponds to the `count` of the array. For files, _size_ corresponds to the file size in kilobytes. Let's look at some examples:
```


 1// Validate that a string is exactly 12 characters long...




 2'title' => 'size:12';




 3 



 4// Validate that a provided integer equals 10...




 5'seats' => 'integer|size:10';




 6 



 7// Validate that an array has exactly 5 elements...




 8'tags' => 'array|size:5';




 9 



10// Validate that an uploaded file is exactly 512 kilobytes...




11'image' => 'file|size:512';




// Validate that a string is exactly 12 characters long...
'title' => 'size:12';

// Validate that a provided integer equals 10...
'seats' => 'integer|size:10';

// Validate that an array has exactly 5 elements...
'tags' => 'array|size:5';

// Validate that an uploaded file is exactly 512 kilobytes...
'image' => 'file|size:512';

```

#### [starts_with:_foo_ ,_bar_ ,...](https://laravel.com/docs/12.x/validation#rule-starts-with)
The field under validation must start with one of the given values.
#### [string](https://laravel.com/docs/12.x/validation#rule-string)
The field under validation must be a string. If you would like to allow the field to also be `null`, you should assign the `nullable` rule to the field.
#### [timezone](https://laravel.com/docs/12.x/validation#rule-timezone)
The field under validation must be a valid timezone identifier according to the `DateTimeZone::listIdentifiers` method.
The arguments
```


1'timezone' => 'required|timezone:all';




2 



3'timezone' => 'required|timezone:Africa';




4 



5'timezone' => 'required|timezone:per_country,US';




'timezone' => 'required|timezone:all';

'timezone' => 'required|timezone:Africa';

'timezone' => 'required|timezone:per_country,US';

```

#### [unique:_table_ ,_column_](https://laravel.com/docs/12.x/validation#rule-unique)
The field under validation must not exist within the given database table.
**Specifying a Custom Table / Column Name:**
Instead of specifying the table name directly, you may specify the Eloquent model which should be used to determine the table name:
```


1'email' => 'unique:App\Models\User,email_address'




'email' => 'unique:App\Models\User,email_address'

```

The `column` option may be used to specify the field's corresponding database column. If the `column` option is not specified, the name of the field under validation will be used.
```


1'email' => 'unique:users,email_address'




'email' => 'unique:users,email_address'

```

**Specifying a Custom Database Connection**
Occasionally, you may need to set a custom connection for database queries made by the Validator. To accomplish this, you may prepend the connection name to the table name:
```


1'email' => 'unique:connection.users,email_address'




'email' => 'unique:connection.users,email_address'

```

**Forcing a Unique Rule to Ignore a Given ID:**
Sometimes, you may wish to ignore a given ID during unique validation. For example, consider an "update profile" screen that includes the user's name, email address, and location. You will probably want to verify that the email address is unique. However, if the user only changes the name field and not the email field, you do not want a validation error to be thrown because the user is already the owner of the email address in question.
To instruct the validator to ignore the user's ID, we'll use the `Rule` class to fluently define the rule. In this example, we'll also specify the validation rules as an array instead of using the `|` character to delimit the rules:
```


1use Illuminate\Support\Facades\Validator;




2use Illuminate\Validation\Rule;




3 



4Validator::make($data, [




5    'email' => [




6        'required',




7        Rule::unique('users')->ignore($user->id),




8    ],




9]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;

Validator::make($data, [
    'email' => [
        'required',
        Rule::unique('users')->ignore($user->id),
    ],
]);

```

You should never pass any user controlled request input into the `ignore` method. Instead, you should only pass a system generated unique ID such as an auto-incrementing ID or UUID from an Eloquent model instance. Otherwise, your application will be vulnerable to an SQL injection attack.
Instead of passing the model key's value to the `ignore` method, you may also pass the entire model instance. Laravel will automatically extract the key from the model:
```


1Rule::unique('users')->ignore($user)




Rule::unique('users')->ignore($user)

```

If your table uses a primary key column name other than `id`, you may specify the name of the column when calling the `ignore` method:
```


1Rule::unique('users')->ignore($user->id, 'user_id')




Rule::unique('users')->ignore($user->id, 'user_id')

```

By default, the `unique` rule will check the uniqueness of the column matching the name of the attribute being validated. However, you may pass a different column name as the second argument to the `unique` method:
```


1Rule::unique('users', 'email_address')->ignore($user->id)




Rule::unique('users', 'email_address')->ignore($user->id)

```

**Adding Additional Where Clauses:**
You may specify additional query conditions by customizing the query using the `where` method. For example, let's add a query condition that scopes the query to only search records that have an `account_id` column value of `1`:
```


1'email' => Rule::unique('users')->where(fn (Builder $query) => $query->where('account_id', 1))




'email' => Rule::unique('users')->where(fn (Builder $query) => $query->where('account_id', 1))

```

**Ignoring Soft Deleted Records in Unique Checks:**
By default, the unique rule includes soft deleted records when determining uniqueness. To exclude soft deleted records from the uniqueness check, you may invoke the `withoutTrashed` method:
```


1Rule::unique('users')->withoutTrashed();




Rule::unique('users')->withoutTrashed();

```

If your model uses a column name other than `deleted_at` for soft deleted records, you may provide the column name when invoking the `withoutTrashed` method:
```


1Rule::unique('users')->withoutTrashed('was_deleted_at');




Rule::unique('users')->withoutTrashed('was_deleted_at');

```

#### [uppercase](https://laravel.com/docs/12.x/validation#rule-uppercase)
The field under validation must be uppercase.
#### [url](https://laravel.com/docs/12.x/validation#rule-url)
The field under validation must be a valid URL.
If you would like to specify the URL protocols that should be considered valid, you may pass the protocols as validation rule parameters:
```


1'url' => 'url:http,https',




2 



3'game' => 'url:minecraft,steam',




'url' => 'url:http,https',

'game' => 'url:minecraft,steam',

```

#### [ulid](https://laravel.com/docs/12.x/validation#rule-ulid)
The field under validation must be a valid
#### [uuid](https://laravel.com/docs/12.x/validation#rule-uuid)
The field under validation must be a valid RFC 9562 (version 1, 3, 4, 5, 6, 7, or 8) universally unique identifier (UUID).
You may also validate that the given UUID matches a UUID specification by version:
```


1'uuid' => 'uuid:4'




'uuid' => 'uuid:4'

```
