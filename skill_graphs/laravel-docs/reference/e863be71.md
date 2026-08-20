## [Rendering Inline Blade Templates](https://laravel.com/docs/12.x/blade#rendering-inline-blade-templates)
Sometimes you may need to transform a raw Blade template string into valid HTML. You may accomplish this using the `render` method provided by the `Blade` facade. The `render` method accepts the Blade template string and an optional array of data to provide to the template:
```


1use Illuminate\Support\Facades\Blade;




2 



3return Blade::render('Hello, {{ $name }}', ['name' => 'Julian Bashir']);




use Illuminate\Support\Facades\Blade;

return Blade::render('Hello, {{ $name }}', ['name' => 'Julian Bashir']);

```

Laravel renders inline Blade templates by writing them to the `storage/framework/views` directory. If you would like Laravel to remove these temporary files after rendering the Blade template, you may provide the `deleteCachedView` argument to the method:
```


1return Blade::render(




2    'Hello, {{ $name }}',




3    ['name' => 'Julian Bashir'],




4    deleteCachedView: true




5);




return Blade::render(
    'Hello, {{ $name }}',
    ['name' => 'Julian Bashir'],
    deleteCachedView: true
);

```
