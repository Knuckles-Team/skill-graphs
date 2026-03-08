## [Available Prompts](https://laravel.com/docs/12.x/prompts#available-prompts)
### [Text](https://laravel.com/docs/12.x/prompts#text)
The `text` function will prompt the user with the given question, accept their input, and then return it:
```


1use function Laravel\Prompts\text;




2 



3$name = text('What is your name?');




use function Laravel\Prompts\text;

$name = text('What is your name?');

```

You may also include placeholder text, a default value, and an informational hint:
```


1$name = text(




2    label: 'What is your name?',




3    placeholder: 'E.g. Taylor Otwell',




4    default: $user?->name,




5    hint: 'This will be displayed on your profile.'




6);




$name = text(
    label: 'What is your name?',
    placeholder: 'E.g. Taylor Otwell',
    default: $user?->name,
    hint: 'This will be displayed on your profile.'
);

```

#### [Required Values](https://laravel.com/docs/12.x/prompts#text-required)
If you require a value to be entered, you may pass the `required` argument:
```


1$name = text(




2    label: 'What is your name?',




3    required: true




4);




$name = text(
    label: 'What is your name?',
    required: true
);

```

If you would like to customize the validation message, you may also pass a string:
```


1$name = text(




2    label: 'What is your name?',




3    required: 'Your name is required.'




4);




$name = text(
    label: 'What is your name?',
    required: 'Your name is required.'
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#text-validation)
Finally, if you would like to perform additional validation logic, you may pass a closure to the `validate` argument:
```


1$name = text(




2    label: 'What is your name?',




3    validate: fn (string $value) => match (true) {




4        strlen($value) < 3 => 'The name must be at least 3 characters.',




5        strlen($value) > 255 => 'The name must not exceed 255 characters.',




6        default => null




7    }




8);




$name = text(
    label: 'What is your name?',
    validate: fn (string $value) => match (true) {
        strlen($value) < 3 => 'The name must be at least 3 characters.',
        strlen($value) > 255 => 'The name must not exceed 255 characters.',
        default => null
    }
);

```

The closure will receive the value that has been entered and may return an error message, or `null` if the validation passes.
Alternatively, you may leverage the power of Laravel's [validator](https://laravel.com/docs/12.x/validation). To do so, provide an array containing the name of the attribute and the desired validation rules to the `validate` argument:
```


1$name = text(




2    label: 'What is your name?',




3    validate: ['name' => 'required|max:255|unique:users']




4);




$name = text(
    label: 'What is your name?',
    validate: ['name' => 'required|max:255|unique:users']
);

```

### [Textarea](https://laravel.com/docs/12.x/prompts#textarea)
The `textarea` function will prompt the user with the given question, accept their input via a multi-line textarea, and then return it:
```


1use function Laravel\Prompts\textarea;




2 



3$story = textarea('Tell me a story.');




use function Laravel\Prompts\textarea;

$story = textarea('Tell me a story.');

```

You may also include placeholder text, a default value, and an informational hint:
```


1$story = textarea(




2    label: 'Tell me a story.',




3    placeholder: 'This is a story about...',




4    hint: 'This will be displayed on your profile.'




5);




$story = textarea(
    label: 'Tell me a story.',
    placeholder: 'This is a story about...',
    hint: 'This will be displayed on your profile.'
);

```

#### [Required Values](https://laravel.com/docs/12.x/prompts#textarea-required)
If you require a value to be entered, you may pass the `required` argument:
```


1$story = textarea(




2    label: 'Tell me a story.',




3    required: true




4);




$story = textarea(
    label: 'Tell me a story.',
    required: true
);

```

If you would like to customize the validation message, you may also pass a string:
```


1$story = textarea(




2    label: 'Tell me a story.',




3    required: 'A story is required.'




4);




$story = textarea(
    label: 'Tell me a story.',
    required: 'A story is required.'
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#textarea-validation)
Finally, if you would like to perform additional validation logic, you may pass a closure to the `validate` argument:
```


1$story = textarea(




2    label: 'Tell me a story.',




3    validate: fn (string $value) => match (true) {




4        strlen($value) < 250 => 'The story must be at least 250 characters.',




5        strlen($value) > 10000 => 'The story must not exceed 10,000 characters.',




6        default => null




7    }




8);




$story = textarea(
    label: 'Tell me a story.',
    validate: fn (string $value) => match (true) {
        strlen($value) < 250 => 'The story must be at least 250 characters.',
        strlen($value) > 10000 => 'The story must not exceed 10,000 characters.',
        default => null
    }
);

```

The closure will receive the value that has been entered and may return an error message, or `null` if the validation passes.
Alternatively, you may leverage the power of Laravel's [validator](https://laravel.com/docs/12.x/validation). To do so, provide an array containing the name of the attribute and the desired validation rules to the `validate` argument:
```


1$story = textarea(




2    label: 'Tell me a story.',




3    validate: ['story' => 'required|max:10000']




4);




$story = textarea(
    label: 'Tell me a story.',
    validate: ['story' => 'required|max:10000']
);

```

### [Number](https://laravel.com/docs/12.x/prompts#number)
The `number` function will prompt the user with the given question, accept their numeric input, and then return it. The `number` function allows the user to use the up and down arrow keys to manipulate the number:
```


1use function Laravel\Prompts\number;




2 



3$number = number('How many copies would you like?');




use function Laravel\Prompts\number;

$number = number('How many copies would you like?');

```

You may also include placeholder text, a default value, and an informational hint:
```


1$name = number(




2    label: 'How many copies would you like?',




3    placeholder: '5',




4    default: 1,




5    hint: 'This will be determine how many copies to create.'




6);




$name = number(
    label: 'How many copies would you like?',
    placeholder: '5',
    default: 1,
    hint: 'This will be determine how many copies to create.'
);

```

#### [Required Values](https://laravel.com/docs/12.x/prompts#number-required)
If you require a value to be entered, you may pass the `required` argument:
```


1$copies = number(




2    label: 'How many copies would you like?',




3    required: true




4);




$copies = number(
    label: 'How many copies would you like?',
    required: true
);

```

If you would like to customize the validation message, you may also pass a string:
```


1$copies = number(




2    label: 'How many copies would you like?',




3    required: 'A number of copies is required.'




4);




$copies = number(
    label: 'How many copies would you like?',
    required: 'A number of copies is required.'
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#number-validation)
Finally, if you would like to perform additional validation logic, you may pass a closure to the `validate` argument:
```


1$copies = number(




2    label: 'How many copies would you like?',




3    validate: fn (?int $value) => match (true) {




4        $value < 1 => 'At least one copy is required.',




5        $value > 100 => 'You may not create more than 100 copies.',




6        default => null




7    }




8);




$copies = number(
    label: 'How many copies would you like?',
    validate: fn (?int $value) => match (true) {
        $value < 1 => 'At least one copy is required.',
        $value > 100 => 'You may not create more than 100 copies.',
        default => null
    }
);

```

The closure will receive the value that has been entered and may return an error message, or `null` if the validation passes.
Alternatively, you may leverage the power of Laravel's [validator](https://laravel.com/docs/12.x/validation). To do so, provide an array containing the name of the attribute and the desired validation rules to the `validate` argument:
```


1$copies = number(




2    label: 'How many copies would you like?',




3    validate: ['copies' => 'required|integer|min:1|max:100']




4);




$copies = number(
    label: 'How many copies would you like?',
    validate: ['copies' => 'required|integer|min:1|max:100']
);

```

### [Password](https://laravel.com/docs/12.x/prompts#password)
The `password` function is similar to the `text` function, but the user's input will be masked as they type in the console. This is useful when asking for sensitive information such as passwords:
```


1use function Laravel\Prompts\password;




2 



3$password = password('What is your password?');




use function Laravel\Prompts\password;

$password = password('What is your password?');

```

You may also include placeholder text and an informational hint:
```


1$password = password(




2    label: 'What is your password?',




3    placeholder: 'password',




4    hint: 'Minimum 8 characters.'




5);




$password = password(
    label: 'What is your password?',
    placeholder: 'password',
    hint: 'Minimum 8 characters.'
);

```

#### [Required Values](https://laravel.com/docs/12.x/prompts#password-required)
If you require a value to be entered, you may pass the `required` argument:
```


1$password = password(




2    label: 'What is your password?',




3    required: true




4);




$password = password(
    label: 'What is your password?',
    required: true
);

```

If you would like to customize the validation message, you may also pass a string:
```


1$password = password(




2    label: 'What is your password?',




3    required: 'The password is required.'




4);




$password = password(
    label: 'What is your password?',
    required: 'The password is required.'
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#password-validation)
Finally, if you would like to perform additional validation logic, you may pass a closure to the `validate` argument:
```


1$password = password(




2    label: 'What is your password?',




3    validate: fn (string $value) => match (true) {




4        strlen($value) < 8 => 'The password must be at least 8 characters.',




5        default => null




6    }




7);




$password = password(
    label: 'What is your password?',
    validate: fn (string $value) => match (true) {
        strlen($value) < 8 => 'The password must be at least 8 characters.',
        default => null
    }
);

```

The closure will receive the value that has been entered and may return an error message, or `null` if the validation passes.
Alternatively, you may leverage the power of Laravel's [validator](https://laravel.com/docs/12.x/validation). To do so, provide an array containing the name of the attribute and the desired validation rules to the `validate` argument:
```


1$password = password(




2    label: 'What is your password?',




3    validate: ['password' => 'min:8']




4);




$password = password(
    label: 'What is your password?',
    validate: ['password' => 'min:8']
);

```

### [Confirm](https://laravel.com/docs/12.x/prompts#confirm)
If you need to ask the user for a "yes or no" confirmation, you may use the `confirm` function. Users may use the arrow keys or press `y` or `n` to select their response. This function will return either `true` or `false`.
```


1use function Laravel\Prompts\confirm;




2 



3$confirmed = confirm('Do you accept the terms?');




use function Laravel\Prompts\confirm;

$confirmed = confirm('Do you accept the terms?');

```

You may also include a default value, customized wording for the "Yes" and "No" labels, and an informational hint:
```


1$confirmed = confirm(




2    label: 'Do you accept the terms?',




3    default: false,




4    yes: 'I accept',




5    no: 'I decline',




6    hint: 'The terms must be accepted to continue.'




7);




$confirmed = confirm(
    label: 'Do you accept the terms?',
    default: false,
    yes: 'I accept',
    no: 'I decline',
    hint: 'The terms must be accepted to continue.'
);

```

#### [Requiring "Yes"](https://laravel.com/docs/12.x/prompts#confirm-required)
If necessary, you may require your users to select "Yes" by passing the `required` argument:
```


1$confirmed = confirm(




2    label: 'Do you accept the terms?',




3    required: true




4);




$confirmed = confirm(
    label: 'Do you accept the terms?',
    required: true
);

```

If you would like to customize the validation message, you may also pass a string:
```


1$confirmed = confirm(




2    label: 'Do you accept the terms?',




3    required: 'You must accept the terms to continue.'




4);




$confirmed = confirm(
    label: 'Do you accept the terms?',
    required: 'You must accept the terms to continue.'
);

```

### [Select](https://laravel.com/docs/12.x/prompts#select)
If you need the user to select from a predefined set of choices, you may use the `select` function:
```


1use function Laravel\Prompts\select;




2 



3$role = select(




4    label: 'What role should the user have?',




5    options: ['Member', 'Contributor', 'Owner']




6);




use function Laravel\Prompts\select;

$role = select(
    label: 'What role should the user have?',
    options: ['Member', 'Contributor', 'Owner']
);

```

You may also specify the default choice and an informational hint:
```


1$role = select(




2    label: 'What role should the user have?',




3    options: ['Member', 'Contributor', 'Owner'],




4    default: 'Owner',




5    hint: 'The role may be changed at any time.'




6);




$role = select(
    label: 'What role should the user have?',
    options: ['Member', 'Contributor', 'Owner'],
    default: 'Owner',
    hint: 'The role may be changed at any time.'
);

```

You may also pass an associative array to the `options` argument to have the selected key returned instead of its value:
```


1$role = select(




2    label: 'What role should the user have?',




3    options: [




4        'member' => 'Member',




5        'contributor' => 'Contributor',




6        'owner' => 'Owner',




7    ],




8    default: 'owner'




9);




$role = select(
    label: 'What role should the user have?',
    options: [
        'member' => 'Member',
        'contributor' => 'Contributor',
        'owner' => 'Owner',
    ],
    default: 'owner'
);

```

Up to five options will be displayed before the list begins to scroll. You may customize this by passing the `scroll` argument:
```


1$role = select(




2    label: 'Which category would you like to assign?',




3    options: Category::pluck('name', 'id'),




4    scroll: 10




5);




$role = select(
    label: 'Which category would you like to assign?',
    options: Category::pluck('name', 'id'),
    scroll: 10
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#select-validation)
Unlike other prompt functions, the `select` function doesn't accept the `required` argument because it is not possible to select nothing. However, you may pass a closure to the `validate` argument if you need to present an option but prevent it from being selected:
```


 1$role = select(




 2    label: 'What role should the user have?',




 3    options: [




 4        'member' => 'Member',




 5        'contributor' => 'Contributor',




 6        'owner' => 'Owner',




 7    ],




 8    validate: fn (string $value) =>




 9        $value === 'owner' && User::where('role', 'owner')->exists()




10            ? 'An owner already exists.'




11            : null




12);




$role = select(
    label: 'What role should the user have?',
    options: [
        'member' => 'Member',
        'contributor' => 'Contributor',
        'owner' => 'Owner',
    ],
    validate: fn (string $value) =>
        $value === 'owner' && User::where('role', 'owner')->exists()
            ? 'An owner already exists.'
            : null
);

```

If the `options` argument is an associative array, then the closure will receive the selected key, otherwise it will receive the selected value. The closure may return an error message, or `null` if the validation passes.
### [Multi-select](https://laravel.com/docs/12.x/prompts#multiselect)
If you need the user to be able to select multiple options, you may use the `multiselect` function:
```


1use function Laravel\Prompts\multiselect;




2 



3$permissions = multiselect(




4    label: 'What permissions should be assigned?',




5    options: ['Read', 'Create', 'Update', 'Delete']




6);




use function Laravel\Prompts\multiselect;

$permissions = multiselect(
    label: 'What permissions should be assigned?',
    options: ['Read', 'Create', 'Update', 'Delete']
);

```

You may also specify default choices and an informational hint:
```


1use function Laravel\Prompts\multiselect;




2 



3$permissions = multiselect(




4    label: 'What permissions should be assigned?',




5    options: ['Read', 'Create', 'Update', 'Delete'],




6    default: ['Read', 'Create'],




7    hint: 'Permissions may be updated at any time.'




8);




use function Laravel\Prompts\multiselect;

$permissions = multiselect(
    label: 'What permissions should be assigned?',
    options: ['Read', 'Create', 'Update', 'Delete'],
    default: ['Read', 'Create'],
    hint: 'Permissions may be updated at any time.'
);

```

You may also pass an associative array to the `options` argument to return the selected options' keys instead of their values:
```


 1$permissions = multiselect(




 2    label: 'What permissions should be assigned?',




 3    options: [




 4        'read' => 'Read',




 5        'create' => 'Create',




 6        'update' => 'Update',




 7        'delete' => 'Delete',




 8    ],




 9    default: ['read', 'create']




10);




$permissions = multiselect(
    label: 'What permissions should be assigned?',
    options: [
        'read' => 'Read',
        'create' => 'Create',
        'update' => 'Update',
        'delete' => 'Delete',
    ],
    default: ['read', 'create']
);

```

Up to five options will be displayed before the list begins to scroll. You may customize this by passing the `scroll` argument:
```


1$categories = multiselect(




2    label: 'What categories should be assigned?',




3    options: Category::pluck('name', 'id'),




4    scroll: 10




5);




$categories = multiselect(
    label: 'What categories should be assigned?',
    options: Category::pluck('name', 'id'),
    scroll: 10
);

```

#### [Requiring a Value](https://laravel.com/docs/12.x/prompts#multiselect-required)
By default, the user may select zero or more options. You may pass the `required` argument to enforce one or more options instead:
```


1$categories = multiselect(




2    label: 'What categories should be assigned?',




3    options: Category::pluck('name', 'id'),




4    required: true




5);




$categories = multiselect(
    label: 'What categories should be assigned?',
    options: Category::pluck('name', 'id'),
    required: true
);

```

If you would like to customize the validation message, you may provide a string to the `required` argument:
```


1$categories = multiselect(




2    label: 'What categories should be assigned?',




3    options: Category::pluck('name', 'id'),




4    required: 'You must select at least one category'




5);




$categories = multiselect(
    label: 'What categories should be assigned?',
    options: Category::pluck('name', 'id'),
    required: 'You must select at least one category'
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#multiselect-validation)
You may pass a closure to the `validate` argument if you need to present an option but prevent it from being selected:
```


 1$permissions = multiselect(




 2    label: 'What permissions should the user have?',




 3    options: [




 4        'read' => 'Read',




 5        'create' => 'Create',




 6        'update' => 'Update',




 7        'delete' => 'Delete',




 8    ],




 9    validate: fn (array $values) => ! in_array('read', $values)




10        ? 'All users require the read permission.'




11        : null




12);




$permissions = multiselect(
    label: 'What permissions should the user have?',
    options: [
        'read' => 'Read',
        'create' => 'Create',
        'update' => 'Update',
        'delete' => 'Delete',
    ],
    validate: fn (array $values) => ! in_array('read', $values)
        ? 'All users require the read permission.'
        : null
);

```

If the `options` argument is an associative array then the closure will receive the selected keys, otherwise it will receive the selected values. The closure may return an error message, or `null` if the validation passes.
### [Suggest](https://laravel.com/docs/12.x/prompts#suggest)
The `suggest` function can be used to provide auto-completion for possible choices. The user can still provide any answer, regardless of the auto-completion hints:
```


1use function Laravel\Prompts\suggest;




2 



3$name = suggest('What is your name?', ['Taylor', 'Dayle']);




use function Laravel\Prompts\suggest;

$name = suggest('What is your name?', ['Taylor', 'Dayle']);

```

Alternatively, you may pass a closure as the second argument to the `suggest` function. The closure will be called each time the user types an input character. The closure should accept a string parameter containing the user's input so far and return an array of options for auto-completion:
```


1$name = suggest(




2    label: 'What is your name?',




3    options: fn ($value) => collect(['Taylor', 'Dayle'])




4        ->filter(fn ($name) => Str::contains($name, $value, ignoreCase: true))




5)




$name = suggest(
    label: 'What is your name?',
    options: fn ($value) => collect(['Taylor', 'Dayle'])
        ->filter(fn ($name) => Str::contains($name, $value, ignoreCase: true))
)

```

You may also include placeholder text, a default value, and an informational hint:
```


1$name = suggest(




2    label: 'What is your name?',




3    options: ['Taylor', 'Dayle'],




4    placeholder: 'E.g. Taylor',




5    default: $user?->name,




6    hint: 'This will be displayed on your profile.'




7);




$name = suggest(
    label: 'What is your name?',
    options: ['Taylor', 'Dayle'],
    placeholder: 'E.g. Taylor',
    default: $user?->name,
    hint: 'This will be displayed on your profile.'
);

```

#### [Required Values](https://laravel.com/docs/12.x/prompts#suggest-required)
If you require a value to be entered, you may pass the `required` argument:
```


1$name = suggest(




2    label: 'What is your name?',




3    options: ['Taylor', 'Dayle'],




4    required: true




5);




$name = suggest(
    label: 'What is your name?',
    options: ['Taylor', 'Dayle'],
    required: true
);

```

If you would like to customize the validation message, you may also pass a string:
```


1$name = suggest(




2    label: 'What is your name?',




3    options: ['Taylor', 'Dayle'],




4    required: 'Your name is required.'




5);




$name = suggest(
    label: 'What is your name?',
    options: ['Taylor', 'Dayle'],
    required: 'Your name is required.'
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#suggest-validation)
Finally, if you would like to perform additional validation logic, you may pass a closure to the `validate` argument:
```


1$name = suggest(




2    label: 'What is your name?',




3    options: ['Taylor', 'Dayle'],




4    validate: fn (string $value) => match (true) {




5        strlen($value) < 3 => 'The name must be at least 3 characters.',




6        strlen($value) > 255 => 'The name must not exceed 255 characters.',




7        default => null




8    }




9);




$name = suggest(
    label: 'What is your name?',
    options: ['Taylor', 'Dayle'],
    validate: fn (string $value) => match (true) {
        strlen($value) < 3 => 'The name must be at least 3 characters.',
        strlen($value) > 255 => 'The name must not exceed 255 characters.',
        default => null
    }
);

```

The closure will receive the value that has been entered and may return an error message, or `null` if the validation passes.
Alternatively, you may leverage the power of Laravel's [validator](https://laravel.com/docs/12.x/validation). To do so, provide an array containing the name of the attribute and the desired validation rules to the `validate` argument:
```


1$name = suggest(




2    label: 'What is your name?',




3    options: ['Taylor', 'Dayle'],




4    validate: ['name' => 'required|min:3|max:255']




5);




$name = suggest(
    label: 'What is your name?',
    options: ['Taylor', 'Dayle'],
    validate: ['name' => 'required|min:3|max:255']
);

```

### [Search](https://laravel.com/docs/12.x/prompts#search)
If you have a lot of options for the user to select from, the `search` function allows the user to type a search query to filter the results before using the arrow keys to select an option:
```


1use function Laravel\Prompts\search;




2 



3$id = search(




4    label: 'Search for the user that should receive the mail',




5    options: fn (string $value) => strlen($value) > 0




6        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




7        : []




8);




use function Laravel\Prompts\search;

$id = search(
    label: 'Search for the user that should receive the mail',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : []
);

```

The closure will receive the text that has been typed by the user so far and must return an array of options. If you return an associative array then the selected option's key will be returned, otherwise its value will be returned instead.
When filtering an array where you intend to return the value, you should use the `array_values` function or the `values` Collection method to ensure the array doesn't become associative:
```


1$names = collect(['Taylor', 'Abigail']);




2 



3$selected = search(




4    label: 'Search for the user that should receive the mail',




5    options: fn (string $value) => $names




6        ->filter(fn ($name) => Str::contains($name, $value, ignoreCase: true))




7        ->values()




8        ->all(),




9);




$names = collect(['Taylor', 'Abigail']);

$selected = search(
    label: 'Search for the user that should receive the mail',
    options: fn (string $value) => $names
        ->filter(fn ($name) => Str::contains($name, $value, ignoreCase: true))
        ->values()
        ->all(),
);

```

You may also include placeholder text and an informational hint:
```


1$id = search(




2    label: 'Search for the user that should receive the mail',




3    placeholder: 'E.g. Taylor Otwell',




4    options: fn (string $value) => strlen($value) > 0




5        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




6        : [],




7    hint: 'The user will receive an email immediately.'




8);




$id = search(
    label: 'Search for the user that should receive the mail',
    placeholder: 'E.g. Taylor Otwell',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : [],
    hint: 'The user will receive an email immediately.'
);

```

Up to five options will be displayed before the list begins to scroll. You may customize this by passing the `scroll` argument:
```


1$id = search(




2    label: 'Search for the user that should receive the mail',




3    options: fn (string $value) => strlen($value) > 0




4        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




5        : [],




6    scroll: 10




7);




$id = search(
    label: 'Search for the user that should receive the mail',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : [],
    scroll: 10
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#search-validation)
If you would like to perform additional validation logic, you may pass a closure to the `validate` argument:
```


 1$id = search(




 2    label: 'Search for the user that should receive the mail',




 3    options: fn (string $value) => strlen($value) > 0




 4        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




 5        : [],




 6    validate: function (int|string $value) {




 7        $user = User::findOrFail($value);




 8 



 9        if ($user->opted_out) {




10            return 'This user has opted-out of receiving mail.';




11        }




12    }




13);




$id = search(
    label: 'Search for the user that should receive the mail',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : [],
    validate: function (int|string $value) {
        $user = User::findOrFail($value);

        if ($user->opted_out) {
            return 'This user has opted-out of receiving mail.';
        }
    }
);

```

If the `options` closure returns an associative array, then the closure will receive the selected key, otherwise, it will receive the selected value. The closure may return an error message, or `null` if the validation passes.
### [Multi-search](https://laravel.com/docs/12.x/prompts#multisearch)
If you have a lot of searchable options and need the user to be able to select multiple items, the `multisearch` function allows the user to type a search query to filter the results before using the arrow keys and space-bar to select options:
```


1use function Laravel\Prompts\multisearch;




2 



3$ids = multisearch(




4    'Search for the users that should receive the mail',




5    fn (string $value) => strlen($value) > 0




6        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




7        : []




8);




use function Laravel\Prompts\multisearch;

$ids = multisearch(
    'Search for the users that should receive the mail',
    fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : []
);

```

The closure will receive the text that has been typed by the user so far and must return an array of options. If you return an associative array then the selected options' keys will be returned; otherwise, their values will be returned instead.
When filtering an array where you intend to return the value, you should use the `array_values` function or the `values` Collection method to ensure the array doesn't become associative:
```


1$names = collect(['Taylor', 'Abigail']);




2 



3$selected = multisearch(




4    label: 'Search for the users that should receive the mail',




5    options: fn (string $value) => $names




6        ->filter(fn ($name) => Str::contains($name, $value, ignoreCase: true))




7        ->values()




8        ->all(),




9);




$names = collect(['Taylor', 'Abigail']);

$selected = multisearch(
    label: 'Search for the users that should receive the mail',
    options: fn (string $value) => $names
        ->filter(fn ($name) => Str::contains($name, $value, ignoreCase: true))
        ->values()
        ->all(),
);

```

You may also include placeholder text and an informational hint:
```


1$ids = multisearch(




2    label: 'Search for the users that should receive the mail',




3    placeholder: 'E.g. Taylor Otwell',




4    options: fn (string $value) => strlen($value) > 0




5        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




6        : [],




7    hint: 'The user will receive an email immediately.'




8);




$ids = multisearch(
    label: 'Search for the users that should receive the mail',
    placeholder: 'E.g. Taylor Otwell',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : [],
    hint: 'The user will receive an email immediately.'
);

```

Up to five options will be displayed before the list begins to scroll. You may customize this by providing the `scroll` argument:
```


1$ids = multisearch(




2    label: 'Search for the users that should receive the mail',




3    options: fn (string $value) => strlen($value) > 0




4        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




5        : [],




6    scroll: 10




7);




$ids = multisearch(
    label: 'Search for the users that should receive the mail',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : [],
    scroll: 10
);

```

#### [Requiring a Value](https://laravel.com/docs/12.x/prompts#multisearch-required)
By default, the user may select zero or more options. You may pass the `required` argument to enforce one or more options instead:
```


1$ids = multisearch(




2    label: 'Search for the users that should receive the mail',




3    options: fn (string $value) => strlen($value) > 0




4        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




5        : [],




6    required: true




7);




$ids = multisearch(
    label: 'Search for the users that should receive the mail',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : [],
    required: true
);

```

If you would like to customize the validation message, you may also provide a string to the `required` argument:
```


1$ids = multisearch(




2    label: 'Search for the users that should receive the mail',




3    options: fn (string $value) => strlen($value) > 0




4        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




5        : [],




6    required: 'You must select at least one user.'




7);




$ids = multisearch(
    label: 'Search for the users that should receive the mail',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : [],
    required: 'You must select at least one user.'
);

```

#### [Additional Validation](https://laravel.com/docs/12.x/prompts#multisearch-validation)
If you would like to perform additional validation logic, you may pass a closure to the `validate` argument:
```


 1$ids = multisearch(




 2    label: 'Search for the users that should receive the mail',




 3    options: fn (string $value) => strlen($value) > 0




 4        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()




 5        : [],




 6    validate: function (array $values) {




 7        $optedOut = User::whereLike('name', '%a%')->findMany($values);




 8 



 9        if ($optedOut->isNotEmpty()) {




10            return $optedOut->pluck('name')->join(', ', ', and ').' have opted out.';




11        }




12    }




13);




$ids = multisearch(
    label: 'Search for the users that should receive the mail',
    options: fn (string $value) => strlen($value) > 0
        ? User::whereLike('name', "%{$value}%")->pluck('name', 'id')->all()
        : [],
    validate: function (array $values) {
        $optedOut = User::whereLike('name', '%a%')->findMany($values);

        if ($optedOut->isNotEmpty()) {
            return $optedOut->pluck('name')->join(', ', ', and ').' have opted out.';
        }
    }
);

```

If the `options` closure returns an associative array, then the closure will receive the selected keys; otherwise, it will receive the selected values. The closure may return an error message, or `null` if the validation passes.
### [Pause](https://laravel.com/docs/12.x/prompts#pause)
The `pause` function may be used to display informational text to the user and wait for them to confirm their desire to proceed by pressing the Enter / Return key:
```


1use function Laravel\Prompts\pause;




2 



3pause('Press ENTER to continue.');




use function Laravel\Prompts\pause;

pause('Press ENTER to continue.');

```
