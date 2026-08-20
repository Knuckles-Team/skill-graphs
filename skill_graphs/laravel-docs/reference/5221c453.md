## [Progress Bars](https://laravel.com/docs/12.x/prompts#progress)
For long running tasks, it can be helpful to show a progress bar that informs users how complete the task is. Using the `progress` function, Laravel will display a progress bar and advance its progress for each iteration over a given iterable value:
```


1use function Laravel\Prompts\progress;




2 



3$users = progress(




4    label: 'Updating users',




5    steps: User::all(),




6    callback: fn ($user) => $this->performTask($user)




7);




use function Laravel\Prompts\progress;

$users = progress(
    label: 'Updating users',
    steps: User::all(),
    callback: fn ($user) => $this->performTask($user)
);

```

The `progress` function acts like a map function and will return an array containing the return value of each iteration of your callback.
The callback may also accept the `Laravel\Prompts\Progress` instance, allowing you to modify the label and hint on each iteration:
```


 1$users = progress(




 2    label: 'Updating users',




 3    steps: User::all(),




 4    callback: function ($user, $progress) {




 5        $progress




 6            ->label("Updating {$user->name}")




 7            ->hint("Created on {$user->created_at}");




 8 



 9        return $this->performTask($user);




10    },




11    hint: 'This may take some time.'




12);




$users = progress(
    label: 'Updating users',
    steps: User::all(),
    callback: function ($user, $progress) {
        $progress
            ->label("Updating {$user->name}")
            ->hint("Created on {$user->created_at}");

        return $this->performTask($user);
    },
    hint: 'This may take some time.'
);

```

Sometimes, you may need more manual control over how a progress bar is advanced. First, define the total number of steps the process will iterate through. Then, advance the progress bar via the `advance` method after processing each item:
```


 1$progress = progress(label: 'Updating users', steps: 10);




 2 



 3$users = User::all();




 4 



 5$progress->start();




 6 



 7foreach ($users as $user) {




 8    $this->performTask($user);




 9 



10    $progress->advance();




11}




12 



13$progress->finish();




$progress = progress(label: 'Updating users', steps: 10);

$users = User::all();

$progress->start();

foreach ($users as $user) {
    $this->performTask($user);

    $progress->advance();
}

$progress->finish();

```
