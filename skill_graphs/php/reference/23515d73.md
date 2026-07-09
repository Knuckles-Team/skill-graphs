## [Forms](https://laravel.com/docs/12.x/prompts#forms)
Often, you will have multiple prompts that will be displayed in sequence to collect information before performing additional actions. You may use the `form` function to create a grouped set of prompts for the user to complete:
```


1use function Laravel\Prompts\form;




2 



3$responses = form()




4    ->text('What is your name?', required: true)




5    ->password('What is your password?', validate: ['password' => 'min:8'])




6    ->confirm('Do you accept the terms?')




7    ->submit();




use function Laravel\Prompts\form;

$responses = form()
    ->text('What is your name?', required: true)
    ->password('What is your password?', validate: ['password' => 'min:8'])
    ->confirm('Do you accept the terms?')
    ->submit();

```

The `submit` method will return a numerically indexed array containing all of the responses from the form's prompts. However, you may provide a name for each prompt via the `name` argument. When a name is provided, the named prompt's response may be accessed via that name:
```


 1use App\Models\User;




 2use function Laravel\Prompts\form;




 3 



 4$responses = form()




 5    ->text('What is your name?', required: true, name: 'name')




 6    ->password(




 7        label: 'What is your password?',




 8        validate: ['password' => 'min:8'],




 9        name: 'password'




10    )




11    ->confirm('Do you accept the terms?')




12    ->submit();




13 



14User::create([




15    'name' => $responses['name'],




16    'password' => $responses['password'],




17]);




use App\Models\User;
use function Laravel\Prompts\form;

$responses = form()
    ->text('What is your name?', required: true, name: 'name')
    ->password(
        label: 'What is your password?',
        validate: ['password' => 'min:8'],
        name: 'password'
    )
    ->confirm('Do you accept the terms?')
    ->submit();

User::create([
    'name' => $responses['name'],
    'password' => $responses['password'],
]);

```

The primary benefit of using the `form` function is the ability for the user to return to previous prompts in the form using `CTRL + U`. This allows the user to fix mistakes or alter selections without needing to cancel and restart the entire form.
If you need more granular control over a prompt in a form, you may invoke the `add` method instead of calling one of the prompt functions directly. The `add` method is passed all previous responses provided by the user:
```


 1use function Laravel\Prompts\form;




 2use function Laravel\Prompts\outro;




 3use function Laravel\Prompts\text;




 4 



 5$responses = form()




 6    ->text('What is your name?', required: true, name: 'name')




 7    ->add(function ($responses) {




 8        return text("How old are you, {$responses['name']}?");




 9    }, name: 'age')




10    ->submit();




11 



12outro("Your name is {$responses['name']} and you are {$responses['age']} years old.");




use function Laravel\Prompts\form;
use function Laravel\Prompts\outro;
use function Laravel\Prompts\text;

$responses = form()
    ->text('What is your name?', required: true, name: 'name')
    ->add(function ($responses) {
        return text("How old are you, {$responses['name']}?");
    }, name: 'age')
    ->submit();

outro("Your name is {$responses['name']} and you are {$responses['age']} years old.");

```
