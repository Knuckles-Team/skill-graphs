## [Conditional Clauses](https://laravel.com/docs/12.x/queries#conditional-clauses)
Sometimes you may want certain query clauses to apply to a query based on another condition. For instance, you may only want to apply a `where` statement if a given input value is present on the incoming HTTP request. You may accomplish this using the `when` method:
```


1$role = $request->input('role');




2 



3$users = DB::table('users')




4    ->when($role, function (Builder $query, string $role) {




5        $query->where('role_id', $role);




6    })




7    ->get();




$role = $request->input('role');

$users = DB::table('users')
    ->when($role, function (Builder $query, string $role) {
        $query->where('role_id', $role);
    })
    ->get();

```

The `when` method only executes the given closure when the first argument is `true`. If the first argument is `false`, the closure will not be executed. So, in the example above, the closure given to the `when` method will only be invoked if the `role` field is present on the incoming request and evaluates to `true`.
You may pass another closure as the third argument to the `when` method. This closure will only execute if the first argument evaluates as `false`. To illustrate how this feature may be used, we will use it to configure the default ordering of a query:
```


1$sortByVotes = $request->boolean('sort_by_votes');




2 



3$users = DB::table('users')




4    ->when($sortByVotes, function (Builder $query, bool $sortByVotes) {




5        $query->orderBy('votes');




6    }, function (Builder $query) {




7        $query->orderBy('name');




8    })




9    ->get();




$sortByVotes = $request->boolean('sort_by_votes');

$users = DB::table('users')
    ->when($sortByVotes, function (Builder $query, bool $sortByVotes) {
        $query->orderBy('votes');
    }, function (Builder $query) {
        $query->orderBy('name');
    })
    ->get();

```
