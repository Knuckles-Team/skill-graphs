## [Building Layouts](https://laravel.com/docs/12.x/blade#building-layouts)
### [Layouts Using Components](https://laravel.com/docs/12.x/blade#layouts-using-components)
Most web applications maintain the same general layout across various pages. It would be incredibly cumbersome and hard to maintain our application if we had to repeat the entire layout HTML in every view we create. Thankfully, it's convenient to define this layout as a single [Blade component](https://laravel.com/docs/12.x/blade#components) and then use it throughout our application.
#### [Defining the Layout Component](https://laravel.com/docs/12.x/blade#defining-the-layout-component)
For example, imagine we are building a "todo" list application. We might define a `layout` component that looks like the following:
```


 1<!-- resources/views/components/layout.blade.php -->




 2 



 3<html>




 4    <head>




 5        <title>{{ $title ?? 'Todo Manager' }}</title>




 6    </head>




 7    <body>




 8        <h1>Todos</h1>




 9        <hr/>




10        {{ $slot }}




11    </body>




12</html>




<!-- resources/views/components/layout.blade.php -->

<html>
    <head>
        <title>{{ $title ?? 'Todo Manager' }}</title>
    </head>
    <body>
        <h1>Todos</h1>
        <hr/>
        {{ $slot }}
    </body>
</html>

```

#### [Applying the Layout Component](https://laravel.com/docs/12.x/blade#applying-the-layout-component)
Once the `layout` component has been defined, we may create a Blade view that utilizes the component. In this example, we will define a simple view that displays our task list:
```


1<!-- resources/views/tasks.blade.php -->




2 



3<x-layout>




4    @foreach ($tasks as $task)




5        <div>{{ $task }}</div>




6    @endforeach




7</x-layout>




<!-- resources/views/tasks.blade.php -->

<x-layout>
    @foreach ($tasks as $task)
        <div>{{ $task }}</div>
    @endforeach
</x-layout>

```

Remember, content that is injected into a component will be supplied to the default `$slot` variable within our `layout` component. As you may have noticed, our `layout` also respects a `$title` slot if one is provided; otherwise, a default title is shown. We may inject a custom title from our task list view using the standard slot syntax discussed in the [component documentation](https://laravel.com/docs/12.x/blade#components):
```


 1<!-- resources/views/tasks.blade.php -->




 2 



 3<x-layout>




 4    <x-slot:title>




 5        Custom Title




 6    </x-slot>




 7 



 8    @foreach ($tasks as $task)




 9        <div>{{ $task }}</div>




10    @endforeach




11</x-layout>




<!-- resources/views/tasks.blade.php -->

<x-layout>
    <x-slot:title>
        Custom Title
    </x-slot>

    @foreach ($tasks as $task)
        <div>{{ $task }}</div>
    @endforeach
</x-layout>

```

Now that we have defined our layout and task list views, we just need to return the `task` view from a route:
```


1use App\Models\Task;




2 



3Route::get('/tasks', function () {




4    return view('tasks', ['tasks' => Task::all()]);




5});




use App\Models\Task;

Route::get('/tasks', function () {
    return view('tasks', ['tasks' => Task::all()]);
});

```

### [Layouts Using Template Inheritance](https://laravel.com/docs/12.x/blade#layouts-using-template-inheritance)
#### [Defining a Layout](https://laravel.com/docs/12.x/blade#defining-a-layout)
Layouts may also be created via "template inheritance". This was the primary way of building applications prior to the introduction of [components](https://laravel.com/docs/12.x/blade#components).
To get started, let's take a look at a simple example. First, we will examine a page layout. Since most web applications maintain the same general layout across various pages, it's convenient to define this layout as a single Blade view:
```


 1<!-- resources/views/layouts/app.blade.php -->




 2 



 3<html>




 4    <head>




 5        <title>App Name - @yield('title')</title>




 6    </head>




 7    <body>




 8        @section('sidebar')




 9            This is the master sidebar.




10        @show




11 



12        <div class="container">




13            @yield('content')




14        </div>




15    </body>




16</html>




<!-- resources/views/layouts/app.blade.php -->

<html>
    <head>
        <title>App Name - @yield('title')</title>
    </head>
    <body>
        @section('sidebar')
            This is the master sidebar.
        @show

        <div class="container">
            @yield('content')
        </div>
    </body>
</html>

```

As you can see, this file contains typical HTML mark-up. However, take note of the `@section` and `@yield` directives. The `@section` directive, as the name implies, defines a section of content, while the `@yield` directive is used to display the contents of a given section.
Now that we have defined a layout for our application, let's define a child page that inherits the layout.
#### [Extending a Layout](https://laravel.com/docs/12.x/blade#extending-a-layout)
When defining a child view, use the `@extends` Blade directive to specify which layout the child view should "inherit". Views which extend a Blade layout may inject content into the layout's sections using `@section` directives. Remember, as seen in the example above, the contents of these sections will be displayed in the layout using `@yield`:
```


 1<!-- resources/views/child.blade.php -->




 2 



 3@extends('layouts.app')




 4 



 5@section('title', 'Page Title')




 6 



 7@section('sidebar')




 8    @@parent




 9 



10    <p>This is appended to the master sidebar.</p>




11@endsection




12 



13@section('content')




14    <p>This is my body content.</p>




15@endsection




<!-- resources/views/child.blade.php -->

@extends('layouts.app')

@section('title', 'Page Title')

@section('sidebar')
    @@parent

    <p>This is appended to the master sidebar.</p>
@endsection

@section('content')
    <p>This is my body content.</p>
@endsection

```

In this example, the `sidebar` section is utilizing the `@@parent` directive to append (rather than overwriting) content to the layout's sidebar. The `@@parent` directive will be replaced by the content of the layout when the view is rendered.
Contrary to the previous example, this `sidebar` section ends with `@endsection` instead of `@show`. The `@endsection` directive will only define a section while `@show` will define and **immediately yield** the section.
The `@yield` directive also accepts a default value as its second parameter. This value will be rendered if the section being yielded is undefined:
```


1@yield('content', 'Default content')




@yield('content', 'Default content')

```
