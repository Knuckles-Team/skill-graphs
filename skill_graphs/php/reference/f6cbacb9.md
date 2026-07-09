## [Blade Directives](https://laravel.com/docs/12.x/blade#blade-directives)
In addition to template inheritance and displaying data, Blade also provides convenient shortcuts for common PHP control structures, such as conditional statements and loops. These shortcuts provide a very clean, terse way of working with PHP control structures while also remaining familiar to their PHP counterparts.
### [If Statements](https://laravel.com/docs/12.x/blade#if-statements)
You may construct `if` statements using the `@if`, `@elseif`, `@else`, and `@endif` directives. These directives function identically to their PHP counterparts:
```


1@if (count($records) === 1)




2    I have one record!




3@elseif (count($records) > 1)




4    I have multiple records!




5@else




6    I don't have any records!




7@endif




@if (count($records) === 1)
    I have one record!
@elseif (count($records) > 1)
    I have multiple records!
@else
    I don't have any records!
@endif

```

For convenience, Blade also provides an `@unless` directive:
```


1@unless (Auth::check())




2    You are not signed in.




3@endunless




@unless (Auth::check())
    You are not signed in.
@endunless

```

In addition to the conditional directives already discussed, the `@isset` and `@empty` directives may be used as convenient shortcuts for their respective PHP functions:
```


1@isset($records)




2    // $records is defined and is not null...




3@endisset




4 



5@empty($records)




6    // $records is "empty"...




7@endempty




@isset($records)
    // $records is defined and is not null...
@endisset

@empty($records)
    // $records is "empty"...
@endempty

```

#### [Authentication Directives](https://laravel.com/docs/12.x/blade#authentication-directives)
The `@auth` and `@guest` directives may be used to quickly determine if the current user is [authenticated](https://laravel.com/docs/12.x/authentication) or is a guest:
```


1@auth




2    // The user is authenticated...




3@endauth




4 



5@guest




6    // The user is not authenticated...




7@endguest




@auth
    // The user is authenticated...
@endauth

@guest
    // The user is not authenticated...
@endguest

```

If needed, you may specify the authentication guard that should be checked when using the `@auth` and `@guest` directives:
```


1@auth('admin')




2    // The user is authenticated...




3@endauth




4 



5@guest('admin')




6    // The user is not authenticated...




7@endguest




@auth('admin')
    // The user is authenticated...
@endauth

@guest('admin')
    // The user is not authenticated...
@endguest

```

#### [Environment Directives](https://laravel.com/docs/12.x/blade#environment-directives)
You may check if the application is running in the production environment using the `@production` directive:
```


1@production




2    // Production specific content...




3@endproduction




@production
    // Production specific content...
@endproduction

```

Or, you may determine if the application is running in a specific environment using the `@env` directive:
```


1@env('staging')




2    // The application is running in "staging"...




3@endenv




4 



5@env(['staging', 'production'])




6    // The application is running in "staging" or "production"...




7@endenv




@env('staging')
    // The application is running in "staging"...
@endenv

@env(['staging', 'production'])
    // The application is running in "staging" or "production"...
@endenv

```

#### [Section Directives](https://laravel.com/docs/12.x/blade#section-directives)
You may determine if a template inheritance section has content using the `@hasSection` directive:
```


1@hasSection('navigation')




2    <div class="pull-right">




3        @yield('navigation')




4    </div>




5 



6    <div class="clearfix"></div>




7@endif




@hasSection('navigation')
    <div class="pull-right">
        @yield('navigation')
    </div>

    <div class="clearfix"></div>
@endif

```

You may use the `sectionMissing` directive to determine if a section does not have content:
```


1@sectionMissing('navigation')




2    <div class="pull-right">




3        @include('default-navigation')




4    </div>




5@endif




@sectionMissing('navigation')
    <div class="pull-right">
        @include('default-navigation')
    </div>
@endif

```

#### [Session Directives](https://laravel.com/docs/12.x/blade#session-directives)
The `@session` directive may be used to determine if a [session](https://laravel.com/docs/12.x/session) value exists. If the session value exists, the template contents within the `@session` and `@endsession` directives will be evaluated. Within the `@session` directive's contents, you may echo the `$value` variable to display the session value:
```


1@session('status')




2    <div class="p-4 bg-green-100">




3        {{ $value }}




4    </div>




5@endsession




@session('status')
    <div class="p-4 bg-green-100">
        {{ $value }}
    </div>
@endsession

```

#### [Context Directives](https://laravel.com/docs/12.x/blade#context-directives)
The `@context` directive may be used to determine if a [context](https://laravel.com/docs/12.x/context) value exists. If the context value exists, the template contents within the `@context` and `@endcontext` directives will be evaluated. Within the `@context` directive's contents, you may echo the `$value` variable to display the context value:
```


1@context('canonical')




2    <link href="{{ $value }}" rel="canonical">




3@endcontext




@context('canonical')
    <link href="{{ $value }}" rel="canonical">
@endcontext

```

### [Switch Statements](https://laravel.com/docs/12.x/blade#switch-statements)
Switch statements can be constructed using the `@switch`, `@case`, `@break`, `@default` and `@endswitch` directives:
```


 1@switch($i)




 2    @case(1)




 3        First case...




 4        @break




 5 



 6    @case(2)




 7        Second case...




 8        @break




 9 



10    @default




11        Default case...




12@endswitch




@switch($i)
    @case(1)
        First case...
        @break

    @case(2)
        Second case...
        @break

    @default
        Default case...
@endswitch

```

### [Loops](https://laravel.com/docs/12.x/blade#loops)
In addition to conditional statements, Blade provides simple directives for working with PHP's loop structures. Again, each of these directives functions identically to their PHP counterparts:
```


 1@for ($i = 0; $i < 10; $i++)




 2    The current value is {{ $i }}




 3@endfor




 4 



 5@foreach ($users as $user)




 6    <p>This is user {{ $user->id }}</p>




 7@endforeach




 8 



 9@forelse ($users as $user)




10    <li>{{ $user->name }}</li>




11@empty




12    <p>No users</p>




13@endforelse




14 



15@while (true)




16    <p>I'm looping forever.</p>




17@endwhile




@for ($i = 0; $i < 10; $i++)
    The current value is {{ $i }}
@endfor

@foreach ($users as $user)
    <p>This is user {{ $user->id }}</p>
@endforeach

@forelse ($users as $user)
    <li>{{ $user->name }}</li>
@empty
    <p>No users</p>
@endforelse

@while (true)
    <p>I'm looping forever.</p>
@endwhile

```

While iterating through a `foreach` loop, you may use the [loop variable](https://laravel.com/docs/12.x/blade#the-loop-variable) to gain valuable information about the loop, such as whether you are in the first or last iteration through the loop.
When using loops you may also skip the current iteration or end the loop using the `@continue` and `@break` directives:
```


 1@foreach ($users as $user)




 2    @if ($user->type == 1)




 3        @continue




 4    @endif




 5 



 6    <li>{{ $user->name }}</li>




 7 



 8    @if ($user->number == 5)




 9        @break




10    @endif




11@endforeach




@foreach ($users as $user)
    @if ($user->type == 1)
        @continue
    @endif

    <li>{{ $user->name }}</li>

    @if ($user->number == 5)
        @break
    @endif
@endforeach

```

You may also include the continuation or break condition within the directive declaration:
```


1@foreach ($users as $user)




2    @continue($user->type == 1)




3 



4    <li>{{ $user->name }}</li>




5 



6    @break($user->number == 5)




7@endforeach




@foreach ($users as $user)
    @continue($user->type == 1)

    <li>{{ $user->name }}</li>

    @break($user->number == 5)
@endforeach

```

### [The Loop Variable](https://laravel.com/docs/12.x/blade#the-loop-variable)
While iterating through a `foreach` loop, a `$loop` variable will be available inside of your loop. This variable provides access to some useful bits of information such as the current loop index and whether this is the first or last iteration through the loop:
```


 1@foreach ($users as $user)




 2    @if ($loop->first)




 3        This is the first iteration.




 4    @endif




 5 



 6    @if ($loop->last)




 7        This is the last iteration.




 8    @endif




 9 



10    <p>This is user {{ $user->id }}</p>




11@endforeach




@foreach ($users as $user)
    @if ($loop->first)
        This is the first iteration.
    @endif

    @if ($loop->last)
        This is the last iteration.
    @endif

    <p>This is user {{ $user->id }}</p>
@endforeach

```

If you are in a nested loop, you may access the parent loop's `$loop` variable via the `parent` property:
```


1@foreach ($users as $user)




2    @foreach ($user->posts as $post)




3        @if ($loop->parent->first)




4            This is the first iteration of the parent loop.




5        @endif




6    @endforeach




7@endforeach




@foreach ($users as $user)
    @foreach ($user->posts as $post)
        @if ($loop->parent->first)
            This is the first iteration of the parent loop.
        @endif
    @endforeach
@endforeach

```

The `$loop` variable also contains a variety of other useful properties:
Property | Description
---|---
`$loop->index` | The index of the current loop iteration (starts at 0).
`$loop->iteration` | The current loop iteration (starts at 1).
`$loop->remaining` | The iterations remaining in the loop.
`$loop->count` | The total number of items in the array being iterated.
`$loop->first` | Whether this is the first iteration through the loop.
`$loop->last` | Whether this is the last iteration through the loop.
`$loop->even` | Whether this is an even iteration through the loop.
`$loop->odd` | Whether this is an odd iteration through the loop.
`$loop->depth` | The nesting level of the current loop.
`$loop->parent` | When in a nested loop, the parent's loop variable.
### [Conditional Classes & Styles](https://laravel.com/docs/12.x/blade#conditional-classes)
The `@class` directive conditionally compiles a CSS class string. The directive accepts an array of classes where the array key contains the class or classes you wish to add, while the value is a boolean expression. If the array element has a numeric key, it will always be included in the rendered class list:
```


 1@php




 2    $isActive = false;




 3    $hasError = true;




 4@endphp




 5 



 6<span @class([




 7    'p-4',




 8    'font-bold' => $isActive,




 9    'text-gray-500' => ! $isActive,




10    'bg-red' => $hasError,




11])></span>




12 



13<span class="p-4 text-gray-500 bg-red"></span>




@php
    $isActive = false;
    $hasError = true;
@endphp

<span @class([
    'p-4',
    'font-bold' => $isActive,
    'text-gray-500' => ! $isActive,
    'bg-red' => $hasError,
])></span>

<span class="p-4 text-gray-500 bg-red"></span>

```

Likewise, the `@style` directive may be used to conditionally add inline CSS styles to an HTML element:
```


 1@php




 2    $isActive = true;




 3@endphp




 4 



 5<span @style([




 6    'background-color: red',




 7    'font-weight: bold' => $isActive,




 8])></span>




 9 



10<span style="background-color: red; font-weight: bold;"></span>




@php
    $isActive = true;
@endphp

<span @style([
    'background-color: red',
    'font-weight: bold' => $isActive,
])></span>

<span style="background-color: red; font-weight: bold;"></span>

```

### [Additional Attributes](https://laravel.com/docs/12.x/blade#additional-attributes)
For convenience, you may use the `@checked` directive to easily indicate if a given HTML checkbox input is "checked". This directive will echo `checked` if the provided condition evaluates to `true`:
```


1<input




2    type="checkbox"




3    name="active"




4    value="active"




5    @checked(old('active', $user->active))




6/>




<input
    type="checkbox"
    name="active"
    value="active"
    @checked(old('active', $user->active))
/>

```

Likewise, the `@selected` directive may be used to indicate if a given select option should be "selected":
```


1<select name="version">




2    @foreach ($product->versions as $version)




3        <option value="{{ $version }}" @selected(old('version') == $version)>




4            {{ $version }}




5        </option>




6    @endforeach




7</select>




<select name="version">
    @foreach ($product->versions as $version)
        <option value="{{ $version }}" @selected(old('version') == $version)>
            {{ $version }}
        </option>
    @endforeach
</select>

```

Additionally, the `@disabled` directive may be used to indicate if a given element should be "disabled":
```


1<button type="submit" @disabled($errors->isNotEmpty())>Submit</button>




<button type="submit" @disabled($errors->isNotEmpty())>Submit</button>

```

Moreover, the `@readonly` directive may be used to indicate if a given element should be "readonly":
```


1<input




2    type="email"




3    name="email"




4    value="email@laravel.com"




5    @readonly($user->isNotAdmin())




6/>




<input
    type="email"
    name="email"
    value="email@laravel.com"
    @readonly($user->isNotAdmin())
/>

```

In addition, the `@required` directive may be used to indicate if a given element should be "required":
```


1<input




2    type="text"




3    name="title"




4    value="title"




5    @required($user->isAdmin())




6/>




<input
    type="text"
    name="title"
    value="title"
    @required($user->isAdmin())
/>

```

### [Including Subviews](https://laravel.com/docs/12.x/blade#including-subviews)
While you're free to use the `@include` directive, Blade [components](https://laravel.com/docs/12.x/blade#components) provide similar functionality and offer several benefits over the `@include` directive such as data and attribute binding.
Blade's `@include` directive allows you to include a Blade view from within another view. All variables that are available to the parent view will be made available to the included view:
```


1<div>




2    @include('shared.errors')




3 



4    <form>




5        <!-- Form Contents -->




6    </form>




7</div>




<div>
    @include('shared.errors')

    <form>
        <!-- Form Contents -->
    </form>
</div>

```

Even though the included view will inherit all data available in the parent view, you may also pass an array of additional data that should be made available to the included view:
```


1@include('view.name', ['status' => 'complete'])




@include('view.name', ['status' => 'complete'])

```

If you attempt to `@include` a view which does not exist, Laravel will throw an error. If you would like to include a view that may or may not be present, you should use the `@includeIf` directive:
```


1@includeIf('view.name', ['status' => 'complete'])




@includeIf('view.name', ['status' => 'complete'])

```

If you would like to `@include` a view if a given boolean expression evaluates to `true` or `false`, you may use the `@includeWhen` and `@includeUnless` directives:
```


1@includeWhen($boolean, 'view.name', ['status' => 'complete'])




2 



3@includeUnless($boolean, 'view.name', ['status' => 'complete'])




@includeWhen($boolean, 'view.name', ['status' => 'complete'])

@includeUnless($boolean, 'view.name', ['status' => 'complete'])

```

To include the first view that exists from a given array of views, you may use the `includeFirst` directive:
```


1@includeFirst(['custom.admin', 'admin'], ['status' => 'complete'])




@includeFirst(['custom.admin', 'admin'], ['status' => 'complete'])

```

If you would like to include a view without inheriting any variables from the parent view, you may use the `@includeIsolated` directive. The included view will only have access to variables you explicitly pass:
```


1@includeIsolated('view.name', ['user' => $user])




@includeIsolated('view.name', ['user' => $user])

```

You should avoid using the `__DIR__` and `__FILE__` constants in your Blade views, since they will refer to the location of the cached, compiled view.
#### [Rendering Views for Collections](https://laravel.com/docs/12.x/blade#rendering-views-for-collections)
You may combine loops and includes into one line with Blade's `@each` directive:
```


1@each('view.name', $jobs, 'job')




@each('view.name', $jobs, 'job')

```

The `@each` directive's first argument is the view to render for each element in the array or collection. The second argument is the array or collection you wish to iterate over, while the third argument is the variable name that will be assigned to the current iteration within the view. So, for example, if you are iterating over an array of `jobs`, typically you will want to access each job as a `job` variable within the view. The array key for the current iteration will be available as the `key` variable within the view.
You may also pass a fourth argument to the `@each` directive. This argument determines the view that will be rendered if the given array is empty.
```


1@each('view.name', $jobs, 'job', 'view.empty')




@each('view.name', $jobs, 'job', 'view.empty')

```

Views rendered via `@each` do not inherit the variables from the parent view. If the child view requires these variables, you should use the `@foreach` and `@include` directives instead.
### [The `@once` Directive](https://laravel.com/docs/12.x/blade#the-once-directive)
The `@once` directive allows you to define a portion of the template that will only be evaluated once per rendering cycle. This may be useful for pushing a given piece of JavaScript into the page's header using [stacks](https://laravel.com/docs/12.x/blade#stacks). For example, if you are rendering a given [component](https://laravel.com/docs/12.x/blade#components) within a loop, you may wish to only push the JavaScript to the header the first time the component is rendered:
```


1@once




2    @push('scripts')




3        <script>




4            // Your custom JavaScript...




5        </script>




6    @endpush




7@endonce




@once
    @push('scripts')
        <script>
            // Your custom JavaScript...
        </script>
    @endpush
@endonce

```

Since the `@once` directive is often used in conjunction with the `@push` or `@prepend` directives, the `@pushOnce` and `@prependOnce` directives are available for your convenience:
```


1@pushOnce('scripts')




2    <script>




3        // Your custom JavaScript...




4    </script>




5@endPushOnce




@pushOnce('scripts')
    <script>
        // Your custom JavaScript...
    </script>
@endPushOnce

```

If you are pushing duplicate content from two separate Blade templates, you should provide a unique identifier as the second argument to the `@pushOnce` directive to ensure the content is only rendered once:
```


1<!-- pie-chart.blade.php -->




2@pushOnce('scripts', 'chart.js')




3    <script src="/chart.js"></script>




4@endPushOnce




5 



6<!-- line-chart.blade.php -->




7@pushOnce('scripts', 'chart.js')




8    <script src="/chart.js"></script>




9@endPushOnce




<!-- pie-chart.blade.php -->
@pushOnce('scripts', 'chart.js')
    <script src="/chart.js"></script>
@endPushOnce

<!-- line-chart.blade.php -->
@pushOnce('scripts', 'chart.js')
    <script src="/chart.js"></script>
@endPushOnce

```

### [Raw PHP](https://laravel.com/docs/12.x/blade#raw-php)
In some situations, it's useful to embed PHP code into your views. You can use the Blade `@php` directive to execute a block of plain PHP within your template:
```


1@php




2    $counter = 1;




3@endphp




@php
    $counter = 1;
@endphp

```

Or, if you only need to use PHP to import a class, you may use the `@use` directive:
```


1@use('App\Models\Flight')




@use('App\Models\Flight')

```

A second argument may be provided to the `@use` directive to alias the imported class:
```


1@use('App\Models\Flight', 'FlightModel')




@use('App\Models\Flight', 'FlightModel')

```

If you have multiple classes within the same namespace, you may group the imports of those classes:
```


1@use('App\Models\{Flight, Airport}')




@use('App\Models\{Flight, Airport}')

```

The `@use` directive also supports importing PHP functions and constants by prefixing the import path with the `function` or `const` modifiers:
```


1@use(function App\Helpers\format_currency)




2@use(const App\Constants\MAX_ATTEMPTS)




@use(function App\Helpers\format_currency)
@use(const App\Constants\MAX_ATTEMPTS)

```

Just like class imports, aliases are supported for functions and constants as well:
```


1@use(function App\Helpers\format_currency, 'formatMoney')




2@use(const App\Constants\MAX_ATTEMPTS, 'MAX_TRIES')




@use(function App\Helpers\format_currency, 'formatMoney')
@use(const App\Constants\MAX_ATTEMPTS, 'MAX_TRIES')

```

Grouped imports are also supported with both function and const modifiers, allowing you to import multiple symbols from the same namespace in a single directive:
```


1@use(function App\Helpers\{format_currency, format_date})




2@use(const App\Constants\{MAX_ATTEMPTS, DEFAULT_TIMEOUT})




@use(function App\Helpers\{format_currency, format_date})
@use(const App\Constants\{MAX_ATTEMPTS, DEFAULT_TIMEOUT})

```

### [Comments](https://laravel.com/docs/12.x/blade#comments)
Blade also allows you to define comments in your views. However, unlike HTML comments, Blade comments are not included in the HTML returned by your application:
```


1{{-- This comment will not be present in the rendered HTML --}}




{{-- This comment will not be present in the rendered HTML --}}

```
