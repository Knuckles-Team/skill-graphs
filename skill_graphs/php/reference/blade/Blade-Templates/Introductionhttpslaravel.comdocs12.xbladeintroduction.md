## [Introduction](https://laravel.com/docs/12.x/blade#introduction)
Blade is the simple, yet powerful templating engine that is included with Laravel. Unlike some PHP templating engines, Blade does not restrict you from using plain PHP code in your templates. In fact, all Blade templates are compiled into plain PHP code and cached until they are modified, meaning Blade adds essentially zero overhead to your application. Blade template files use the `.blade.php` file extension and are typically stored in the `resources/views` directory.
Blade views may be returned from routes or controllers using the global `view` helper. Of course, as mentioned in the documentation on [views](https://laravel.com/docs/12.x/views), data may be passed to the Blade view using the `view` helper's second argument:
```


1Route::get('/', function () {




2    return view('greeting', ['name' => 'Finn']);




3});




Route::get('/', function () {
    return view('greeting', ['name' => 'Finn']);
});

```

### [Supercharging Blade With Livewire](https://laravel.com/docs/12.x/blade#supercharging-blade-with-livewire)
Want to take your Blade templates to the next level and build dynamic interfaces with ease? Check out [Laravel Livewire](https://livewire.laravel.com). Livewire allows you to write Blade components that are augmented with dynamic functionality that would typically only be possible via frontend frameworks like React, Svelte, or Vue, providing a great approach to building modern, reactive frontends without the complexities, client-side rendering, or build steps of many JavaScript frameworks.
