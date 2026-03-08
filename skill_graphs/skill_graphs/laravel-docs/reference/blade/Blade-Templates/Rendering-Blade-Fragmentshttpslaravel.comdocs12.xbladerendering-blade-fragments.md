## [Rendering Blade Fragments](https://laravel.com/docs/12.x/blade#rendering-blade-fragments)
When using frontend frameworks such as `@fragment` and `@endfragment` directives:
```


1@fragment('user-list')




2    <ul>




3        @foreach ($users as $user)




4            <li>{{ $user->name }}</li>




5        @endforeach




6    </ul>




7@endfragment




@fragment('user-list')
    <ul>
        @foreach ($users as $user)
            <li>{{ $user->name }}</li>
        @endforeach
    </ul>
@endfragment

```

Then, when rendering the view that utilizes this template, you may invoke the `fragment` method to specify that only the specified fragment should be included in the outgoing HTTP response:
```


1return view('dashboard', ['users' => $users])->fragment('user-list');




return view('dashboard', ['users' => $users])->fragment('user-list');

```

The `fragmentIf` method allows you to conditionally return a fragment of a view based on a given condition. Otherwise, the entire view will be returned:
```


1return view('dashboard', ['users' => $users])




2    ->fragmentIf($request->hasHeader('HX-Request'), 'user-list');




return view('dashboard', ['users' => $users])
    ->fragmentIf($request->hasHeader('HX-Request'), 'user-list');

```

The `fragments` and `fragmentsIf` methods allow you to return multiple view fragments in the response. The fragments will be concatenated together:
```


1view('dashboard', ['users' => $users])




2    ->fragments(['user-list', 'comment-list']);




3 



4view('dashboard', ['users' => $users])




5    ->fragmentsIf(




6        $request->hasHeader('HX-Request'),




7        ['user-list', 'comment-list']




8    );




view('dashboard', ['users' => $users])
    ->fragments(['user-list', 'comment-list']);

view('dashboard', ['users' => $users])
    ->fragmentsIf(
        $request->hasHeader('HX-Request'),
        ['user-list', 'comment-list']
    );

```
