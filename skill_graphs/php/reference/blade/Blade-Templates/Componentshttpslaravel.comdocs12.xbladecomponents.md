## [Components](https://laravel.com/docs/12.x/blade#components)
Components and slots provide similar benefits to sections, layouts, and includes; however, some may find the mental model of components and slots easier to understand. There are two approaches to writing components: class-based components and anonymous components.
To create a class-based component, you may use the `make:component` Artisan command. To illustrate how to use components, we will create a simple `Alert` component. The `make:component` command will place the component in the `app/View/Components` directory:
```


1php artisan make:component Alert




php artisan make:component Alert

```

The `make:component` command will also create a view template for the component. The view will be placed in the `resources/views/components` directory. When writing components for your own application, components are automatically discovered within the `app/View/Components` directory and `resources/views/components` directory, so no further component registration is typically required.
You may also create components within subdirectories:
```


1php artisan make:component Forms/Input




php artisan make:component Forms/Input

```

The command above will create an `Input` component in the `app/View/Components/Forms` directory and the view will be placed in the `resources/views/components/forms` directory.
#### [Manually Registering Package Components](https://laravel.com/docs/12.x/blade#manually-registering-package-components)
When writing components for your own application, components are automatically discovered within the `app/View/Components` directory and `resources/views/components` directory.
However, if you are building a package that utilizes Blade components, you will need to manually register your component class and its HTML tag alias. You should typically register your components in the `boot` method of your package's service provider:
```


1use Illuminate\Support\Facades\Blade;




2 



3/**




4 * Bootstrap your package's services.




5 */




6public function boot(): void




7{




8    Blade::component('package-alert', Alert::class);




9}




use Illuminate\Support\Facades\Blade;

/**
 * Bootstrap your package's services.
 */
public function boot(): void
{
    Blade::component('package-alert', Alert::class);
}

```

Once your component has been registered, it may be rendered using its tag alias:
```


1<x-package-alert/>




<x-package-alert/>

```

Alternatively, you may use the `componentNamespace` method to autoload component classes by convention. For example, a `Nightshade` package might have `Calendar` and `ColorPicker` components that reside within the `Package\Views\Components` namespace:
```


1use Illuminate\Support\Facades\Blade;




2 



3/**




4 * Bootstrap your package's services.




5 */




6public function boot(): void




7{




8    Blade::componentNamespace('Nightshade\\Views\\Components', 'nightshade');




9}




use Illuminate\Support\Facades\Blade;

/**
 * Bootstrap your package's services.
 */
public function boot(): void
{
    Blade::componentNamespace('Nightshade\\Views\\Components', 'nightshade');
}

```

This will allow the usage of package components by their vendor namespace using the `package-name::` syntax:
```


1<x-nightshade::calendar />




2<x-nightshade::color-picker />




<x-nightshade::calendar />
<x-nightshade::color-picker />

```

Blade will automatically detect the class that's linked to this component by pascal-casing the component name. Subdirectories are also supported using "dot" notation.
### [Rendering Components](https://laravel.com/docs/12.x/blade#rendering-components)
To display a component, you may use a Blade component tag within one of your Blade templates. Blade component tags start with the string `x-` followed by the kebab case name of the component class:
```


1<x-alert/>




2 



3<x-user-profile/>




<x-alert/>

<x-user-profile/>

```

If the component class is nested deeper within the `app/View/Components` directory, you may use the `.` character to indicate directory nesting. For example, if we assume a component is located at `app/View/Components/Inputs/Button.php`, we may render it like so:
```


1<x-inputs.button/>




<x-inputs.button/>

```

If you would like to conditionally render your component, you may define a `shouldRender` method on your component class. If the `shouldRender` method returns `false` the component will not be rendered:
```


1use Illuminate\Support\Str;




2 



3/**




4 * Whether the component should be rendered




5 */




6public function shouldRender(): bool




7{




8    return Str::length($this->message) > 0;




9}




use Illuminate\Support\Str;

/**
 * Whether the component should be rendered
 */
public function shouldRender(): bool
{
    return Str::length($this->message) > 0;
}

```

### [Index Components](https://laravel.com/docs/12.x/blade#index-components)
Sometimes components are part of a component group and you may wish to group the related components within a single directory. For example, imagine a "card" component with the following class structure:
```


1App\Views\Components\Card\Card




2App\Views\Components\Card\Header




3App\Views\Components\Card\Body




App\Views\Components\Card\Card
App\Views\Components\Card\Header
App\Views\Components\Card\Body

```

Since the root `Card` component is nested within a `Card` directory, you might expect that you would need to render the component via `<x-card.card>`. However, when a component's file name matches the name of the component's directory, Laravel automatically assumes that component is the "root" component and allows you to render the component without repeating the directory name:
```


1<x-card>




2    <x-card.header>...</x-card.header>




3    <x-card.body>...</x-card.body>




4</x-card>




<x-card>
    <x-card.header>...</x-card.header>
    <x-card.body>...</x-card.body>
</x-card>

```

### [Passing Data to Components](https://laravel.com/docs/12.x/blade#passing-data-to-components)
You may pass data to Blade components using HTML attributes. Hard-coded, primitive values may be passed to the component using simple HTML attribute strings. PHP expressions and variables should be passed to the component via attributes that use the `:` character as a prefix:
```


1<x-alert type="error" :message="$message"/>




<x-alert type="error" :message="$message"/>

```

You should define all of the component's data attributes in its class constructor. All public properties on a component will automatically be made available to the component's view. It is not necessary to pass the data to the view from the component's `render` method:
```


 1<?php




 2 



 3namespace App\View\Components;




 4 



 5use Illuminate\View\Component;




 6use Illuminate\View\View;




 7 



 8class Alert extends Component




 9{




10    /**




11     * Create the component instance.




12     */




13    public function __construct(




14        public string $type,




15        public string $message,




16    ) {}




17 



18    /**




19     * Get the view / contents that represent the component.




20     */




21    public function render(): View




22    {




23        return view('components.alert');




24    }




25}




<?php

namespace App\View\Components;

use Illuminate\View\Component;
use Illuminate\View\View;

class Alert extends Component
{
    /**
     * Create the component instance.
     */
    public function __construct(
        public string $type,
        public string $message,
    ) {}

    /**
     * Get the view / contents that represent the component.
     */
    public function render(): View
    {
        return view('components.alert');
    }
}

```

When your component is rendered, you may display the contents of your component's public variables by echoing the variables by name:
```


1<div class="alert alert-{{ $type }}">




2    {{ $message }}




3</div>




<div class="alert alert-{{ $type }}">
    {{ $message }}
</div>

```

#### [Casing](https://laravel.com/docs/12.x/blade#casing)
Component constructor arguments should be specified using `camelCase`, while `kebab-case` should be used when referencing the argument names in your HTML attributes. For example, given the following component constructor:
```


1/**




2 * Create the component instance.




3 */




4public function __construct(




5    public string $alertType,




6) {}




/**
 * Create the component instance.
 */
public function __construct(
    public string $alertType,
) {}

```

The `$alertType` argument may be provided to the component like so:
```


1<x-alert alert-type="danger" />




<x-alert alert-type="danger" />

```

#### [Short Attribute Syntax](https://laravel.com/docs/12.x/blade#short-attribute-syntax)
When passing attributes to components, you may also use a "short attribute" syntax. This is often convenient since attribute names frequently match the variable names they correspond to:
```


1{{-- Short attribute syntax... --}}




2<x-profile :$userId :$name />




3 



4{{-- Is equivalent to... --}}




5<x-profile :user-id="$userId" :name="$name" />




{{-- Short attribute syntax... --}}
<x-profile :$userId :$name />

{{-- Is equivalent to... --}}
<x-profile :user-id="$userId" :name="$name" />

```

#### [Escaping Attribute Rendering](https://laravel.com/docs/12.x/blade#escaping-attribute-rendering)
Since some JavaScript frameworks such as Alpine.js also use colon-prefixed attributes, you may use a double colon (`::`) prefix to inform Blade that the attribute is not a PHP expression. For example, given the following component:
```


1<x-button ::class="{ danger: isDeleting }">




2    Submit




3</x-button>




<x-button ::class="{ danger: isDeleting }">
    Submit
</x-button>

```

The following HTML will be rendered by Blade:
```


1<button :class="{ danger: isDeleting }">




2    Submit




3</button>




<button :class="{ danger: isDeleting }">
    Submit
</button>

```

#### [Component Methods](https://laravel.com/docs/12.x/blade#component-methods)
In addition to public variables being available to your component template, any public methods on the component may be invoked. For example, imagine a component that has an `isSelected` method:
```


1/**




2 * Determine if the given option is the currently selected option.




3 */




4public function isSelected(string $option): bool




5{




6    return $option === $this->selected;




7}




/**
 * Determine if the given option is the currently selected option.
 */
public function isSelected(string $option): bool
{
    return $option === $this->selected;
}

```

You may execute this method from your component template by invoking the variable matching the name of the method:
```


1<option {{ $isSelected($value) ? 'selected' : '' }} value="{{ $value }}">




2    {{ $label }}




3</option>




<option {{ $isSelected($value) ? 'selected' : '' }} value="{{ $value }}">
    {{ $label }}
</option>

```

#### [Accessing Attributes and Slots Within Component Classes](https://laravel.com/docs/12.x/blade#using-attributes-slots-within-component-class)
Blade components also allow you to access the component name, attributes, and slot inside the class's render method. However, in order to access this data, you should return a closure from your component's `render` method:
```


 1use Closure;




 2 



 3/**




 4 * Get the view / contents that represent the component.




 5 */




 6public function render(): Closure




 7{




 8    return function () {




 9        return '<div {{ $attributes }}>Components content</div>';




10    };




11}




use Closure;

/**
 * Get the view / contents that represent the component.
 */
public function render(): Closure
{
    return function () {
        return '<div {{ $attributes }}>Components content</div>';
    };
}

```

The closure returned by your component's `render` method may also receive a `$data` array as its only argument. This array will contain several elements that provide information about the component:
```


1return function (array $data) {




2    // $data['componentName'];




3    // $data['attributes'];




4    // $data['slot'];




5 



6    return '<div {{ $attributes }}>Components content</div>';




7}




return function (array $data) {
    // $data['componentName'];
    // $data['attributes'];
    // $data['slot'];

    return '<div {{ $attributes }}>Components content</div>';
}

```

The elements in the `$data` array should never be directly embedded into the Blade string returned by your `render` method, as doing so could allow remote code execution via malicious attribute content.
The `componentName` is equal to the name used in the HTML tag after the `x-` prefix. So `<x-alert />`'s `componentName` will be `alert`. The `attributes` element will contain all of the attributes that were present on the HTML tag. The `slot` element is an `Illuminate\Support\HtmlString` instance with the contents of the component's slot.
The closure should return a string. If the returned string corresponds to an existing view, that view will be rendered; otherwise, the returned string will be evaluated as an inline Blade view.
#### [Additional Dependencies](https://laravel.com/docs/12.x/blade#additional-dependencies)
If your component requires dependencies from Laravel's [service container](https://laravel.com/docs/12.x/container), you may list them before any of the component's data attributes and they will automatically be injected by the container:
```


 1use App\Services\AlertCreator;




 2 



 3/**




 4 * Create the component instance.




 5 */




 6public function __construct(




 7    public AlertCreator $creator,




 8    public string $type,




 9    public string $message,




10) {}




use App\Services\AlertCreator;

/**
 * Create the component instance.
 */
public function __construct(
    public AlertCreator $creator,
    public string $type,
    public string $message,
) {}

```

#### [Hiding Attributes / Methods](https://laravel.com/docs/12.x/blade#hiding-attributes-and-methods)
If you would like to prevent some public methods or properties from being exposed as variables to your component template, you may add them to an `$except` array property on your component:
```


 1<?php




 2 



 3namespace App\View\Components;




 4 



 5use Illuminate\View\Component;




 6 



 7class Alert extends Component




 8{




 9    /**




10     * The properties / methods that should not be exposed to the component template.




11     *




12     * @var array




13     */




14    protected $except = ['type'];




15 



16    /**




17     * Create the component instance.




18     */




19    public function __construct(




20        public string $type,




21    ) {}




22}




<?php

namespace App\View\Components;

use Illuminate\View\Component;

class Alert extends Component
{
    /**
     * The properties / methods that should not be exposed to the component template.
     *
     * @var array
     */
    protected $except = ['type'];

    /**
     * Create the component instance.
     */
    public function __construct(
        public string $type,
    ) {}
}

```

### [Component Attributes](https://laravel.com/docs/12.x/blade#component-attributes)
We've already examined how to pass data attributes to a component; however, sometimes you may need to specify additional HTML attributes, such as `class`, that are not part of the data required for a component to function. Typically, you want to pass these additional attributes down to the root element of the component template. For example, imagine we want to render an `alert` component like so:
```


1<x-alert type="error" :message="$message" class="mt-4"/>




<x-alert type="error" :message="$message" class="mt-4"/>

```

All of the attributes that are not part of the component's constructor will automatically be added to the component's "attribute bag". This attribute bag is automatically made available to the component via the `$attributes` variable. All of the attributes may be rendered within the component by echoing this variable:
```


1<div {{ $attributes }}>




2    <!-- Component content -->




3</div>




<div {{ $attributes }}>
    <!-- Component content -->
</div>

```

Using directives such as `@env` within component tags is not supported at this time. For example, `<x-alert :live="@env('production')"/>` will not be compiled.
#### [Default / Merged Attributes](https://laravel.com/docs/12.x/blade#default-merged-attributes)
Sometimes you may need to specify default values for attributes or merge additional values into some of the component's attributes. To accomplish this, you may use the attribute bag's `merge` method. This method is particularly useful for defining a set of default CSS classes that should always be applied to a component:
```


1<div {{ $attributes->merge(['class' => 'alert alert-'.$type]) }}>




2    {{ $message }}




3</div>




<div {{ $attributes->merge(['class' => 'alert alert-'.$type]) }}>
    {{ $message }}
</div>

```

If we assume this component is utilized like so:
```


1<x-alert type="error" :message="$message" class="mb-4"/>




<x-alert type="error" :message="$message" class="mb-4"/>

```

The final, rendered HTML of the component will appear like the following:
```


1<div class="alert alert-error mb-4">




2    <!-- Contents of the $message variable -->




3</div>




<div class="alert alert-error mb-4">
    <!-- Contents of the $message variable -->
</div>

```

#### [Conditionally Merge Classes](https://laravel.com/docs/12.x/blade#conditionally-merge-classes)
Sometimes you may wish to merge classes if a given condition is `true`. You can accomplish this via the `class` method, which accepts an array of classes where the array key contains the class or classes you wish to add, while the value is a boolean expression. If the array element has a numeric key, it will always be included in the rendered class list:
```


1<div {{ $attributes->class(['p-4', 'bg-red' => $hasError]) }}>




2    {{ $message }}




3</div>




<div {{ $attributes->class(['p-4', 'bg-red' => $hasError]) }}>
    {{ $message }}
</div>

```

If you need to merge other attributes onto your component, you can chain the `merge` method onto the `class` method:
```


1<button {{ $attributes->class(['p-4'])->merge(['type' => 'button']) }}>




2    {{ $slot }}




3</button>




<button {{ $attributes->class(['p-4'])->merge(['type' => 'button']) }}>
    {{ $slot }}
</button>

```

If you need to conditionally compile classes on other HTML elements that shouldn't receive merged attributes, you can use the [@class directive](https://laravel.com/docs/12.x/blade#conditional-classes).
#### [Non-Class Attribute Merging](https://laravel.com/docs/12.x/blade#non-class-attribute-merging)
When merging attributes that are not `class` attributes, the values provided to the `merge` method will be considered the "default" values of the attribute. However, unlike the `class` attribute, these attributes will not be merged with injected attribute values. Instead, they will be overwritten. For example, a `button` component's implementation may look like the following:
```


1<button {{ $attributes->merge(['type' => 'button']) }}>




2    {{ $slot }}




3</button>




<button {{ $attributes->merge(['type' => 'button']) }}>
    {{ $slot }}
</button>

```

To render the button component with a custom `type`, it may be specified when consuming the component. If no type is specified, the `button` type will be used:
```


1<x-button type="submit">




2    Submit




3</x-button>




<x-button type="submit">
    Submit
</x-button>

```

The rendered HTML of the `button` component in this example would be:
```


1<button type="submit">




2    Submit




3</button>




<button type="submit">
    Submit
</button>

```

If you would like an attribute other than `class` to have its default value and injected values joined together, you may use the `prepends` method. In this example, the `data-controller` attribute will always begin with `profile-controller` and any additional injected `data-controller` values will be placed after this default value:
```


1<div {{ $attributes->merge(['data-controller' => $attributes->prepends('profile-controller')]) }}>




2    {{ $slot }}




3</div>




<div {{ $attributes->merge(['data-controller' => $attributes->prepends('profile-controller')]) }}>
    {{ $slot }}
</div>

```

#### [Retrieving and Filtering Attributes](https://laravel.com/docs/12.x/blade#filtering-attributes)
You may filter attributes using the `filter` method. This method accepts a closure which should return `true` if you wish to retain the attribute in the attribute bag:
```


1{{ $attributes->filter(fn (string $value, string $key) => $key == 'foo') }}




{{ $attributes->filter(fn (string $value, string $key) => $key == 'foo') }}

```

For convenience, you may use the `whereStartsWith` method to retrieve all attributes whose keys begin with a given string:
```


1{{ $attributes->whereStartsWith('wire:model') }}




{{ $attributes->whereStartsWith('wire:model') }}

```

Conversely, the `whereDoesntStartWith` method may be used to exclude all attributes whose keys begin with a given string:
```


1{{ $attributes->whereDoesntStartWith('wire:model') }}




{{ $attributes->whereDoesntStartWith('wire:model') }}

```

Using the `first` method, you may render the first attribute in a given attribute bag:
```


1{{ $attributes->whereStartsWith('wire:model')->first() }}




{{ $attributes->whereStartsWith('wire:model')->first() }}

```

If you would like to check if an attribute is present on the component, you may use the `has` method. This method accepts the attribute name as its only argument and returns a boolean indicating whether or not the attribute is present:
```


1@if ($attributes->has('class'))




2    <div>Class attribute is present</div>




3@endif




@if ($attributes->has('class'))
    <div>Class attribute is present</div>
@endif

```

If an array is passed to the `has` method, the method will determine if all of the given attributes are present on the component:
```


1@if ($attributes->has(['name', 'class']))




2    <div>All of the attributes are present</div>




3@endif




@if ($attributes->has(['name', 'class']))
    <div>All of the attributes are present</div>
@endif

```

The `hasAny` method may be used to determine if any of the given attributes are present on the component:
```


1@if ($attributes->hasAny(['href', ':href', 'v-bind:href']))




2    <div>One of the attributes is present</div>




3@endif




@if ($attributes->hasAny(['href', ':href', 'v-bind:href']))
    <div>One of the attributes is present</div>
@endif

```

You may retrieve a specific attribute's value using the `get` method:
```


1{{ $attributes->get('class') }}




{{ $attributes->get('class') }}

```

The `only` method may be used to retrieve only the attributes with the given keys:
```


1{{ $attributes->only(['class']) }}




{{ $attributes->only(['class']) }}

```

The `except` method may be used to retrieve all attributes except those with the given keys:
```


1{{ $attributes->except(['class']) }}




{{ $attributes->except(['class']) }}

```

### [Reserved Keywords](https://laravel.com/docs/12.x/blade#reserved-keywords)
By default, some keywords are reserved for Blade's internal use in order to render components. The following keywords cannot be defined as public properties or method names within your components:
  * `data`
  * `render`
  * `resolve`
  * `resolveView`
  * `shouldRender`
  * `view`
  * `withAttributes`
  * `withName`


### [Slots](https://laravel.com/docs/12.x/blade#slots)
You will often need to pass additional content to your component via "slots". Component slots are rendered by echoing the `$slot` variable. To explore this concept, let's imagine that an `alert` component has the following markup:
```


1<!-- /resources/views/components/alert.blade.php -->




2 



3<div class="alert alert-danger">




4    {{ $slot }}




5</div>




<!-- /resources/views/components/alert.blade.php -->

<div class="alert alert-danger">
    {{ $slot }}
</div>

```

We may pass content to the `slot` by injecting content into the component:
```


1<x-alert>




2    <strong>Whoops!</strong> Something went wrong!




3</x-alert>




<x-alert>
    <strong>Whoops!</strong> Something went wrong!
</x-alert>

```

Sometimes a component may need to render multiple different slots in different locations within the component. Let's modify our alert component to allow for the injection of a "title" slot:
```


1<!-- /resources/views/components/alert.blade.php -->




2 



3<span class="alert-title">{{ $title }}</span>




4 



5<div class="alert alert-danger">




6    {{ $slot }}




7</div>




<!-- /resources/views/components/alert.blade.php -->

<span class="alert-title">{{ $title }}</span>

<div class="alert alert-danger">
    {{ $slot }}
</div>

```

You may define the content of the named slot using the `x-slot` tag. Any content not within an explicit `x-slot` tag will be passed to the component in the `$slot` variable:
```


1<x-alert>




2    <x-slot:title>




3        Server Error




4    </x-slot>




5 



6    <strong>Whoops!</strong> Something went wrong!




7</x-alert>




<x-alert>
    <x-slot:title>
        Server Error
    </x-slot>

    <strong>Whoops!</strong> Something went wrong!
</x-alert>

```

You may invoke a slot's `isEmpty` method to determine if the slot contains content:
```


1<span class="alert-title">{{ $title }}</span>




2 



3<div class="alert alert-danger">




4    @if ($slot->isEmpty())




5        This is default content if the slot is empty.




6    @else




7        {{ $slot }}




8    @endif




9</div>




<span class="alert-title">{{ $title }}</span>

<div class="alert alert-danger">
    @if ($slot->isEmpty())
        This is default content if the slot is empty.
    @else
        {{ $slot }}
    @endif
</div>

```

Additionally, the `hasActualContent` method may be used to determine if the slot contains any "actual" content that is not an HTML comment:
```


1@if ($slot->hasActualContent())




2    The scope has non-comment content.




3@endif




@if ($slot->hasActualContent())
    The scope has non-comment content.
@endif

```

#### [Scoped Slots](https://laravel.com/docs/12.x/blade#scoped-slots)
If you have used a JavaScript framework such as Vue, you may be familiar with "scoped slots", which allow you to access data or methods from the component within your slot. You may achieve similar behavior in Laravel by defining public methods or properties on your component and accessing the component within your slot via the `$component` variable. In this example, we will assume that the `x-alert` component has a public `formatAlert` method defined on its component class:
```


1<x-alert>




2    <x-slot:title>




3        {{ $component->formatAlert('Server Error') }}




4    </x-slot>




5 



6    <strong>Whoops!</strong> Something went wrong!




7</x-alert>




<x-alert>
    <x-slot:title>
        {{ $component->formatAlert('Server Error') }}
    </x-slot>

    <strong>Whoops!</strong> Something went wrong!
</x-alert>

```

#### [Slot Attributes](https://laravel.com/docs/12.x/blade#slot-attributes)
Like Blade components, you may assign additional [attributes](https://laravel.com/docs/12.x/blade#component-attributes) to slots such as CSS class names:
```


 1<x-card class="shadow-sm">




 2    <x-slot:heading class="font-bold">




 3        Heading




 4    </x-slot>




 5 



 6    Content




 7 



 8    <x-slot:footer class="text-sm">




 9        Footer




10    </x-slot>




11</x-card>




<x-card class="shadow-sm">
    <x-slot:heading class="font-bold">
        Heading
    </x-slot>

    Content

    <x-slot:footer class="text-sm">
        Footer
    </x-slot>
</x-card>

```

To interact with slot attributes, you may access the `attributes` property of the slot's variable. For more information on how to interact with attributes, please consult the documentation on [component attributes](https://laravel.com/docs/12.x/blade#component-attributes):
```


 1@props([




 2    'heading',




 3    'footer',




 4])




 5 



 6<div {{ $attributes->class(['border']) }}>




 7    <h1 {{ $heading->attributes->class(['text-lg']) }}>




 8        {{ $heading }}




 9    </h1>




10 



11    {{ $slot }}




12 



13    <footer {{ $footer->attributes->class(['text-gray-700']) }}>




14        {{ $footer }}




15    </footer>




16</div>




@props([
    'heading',
    'footer',
])

<div {{ $attributes->class(['border']) }}>
    <h1 {{ $heading->attributes->class(['text-lg']) }}>
        {{ $heading }}
    </h1>

    {{ $slot }}

    <footer {{ $footer->attributes->class(['text-gray-700']) }}>
        {{ $footer }}
    </footer>
</div>

```

### [Inline Component Views](https://laravel.com/docs/12.x/blade#inline-component-views)
For very small components, it may feel cumbersome to manage both the component class and the component's view template. For this reason, you may return the component's markup directly from the `render` method:
```


 1/**




 2 * Get the view / contents that represent the component.




 3 */




 4public function render(): string




 5{




 6    return <<<'blade'




 7        <div class="alert alert-danger">




 8            {{ $slot }}




 9        </div>




10    blade;




11}




/**
 * Get the view / contents that represent the component.
 */
public function render(): string
{
    return <<<'blade'
        <div class="alert alert-danger">
            {{ $slot }}
        </div>
    blade;
}

```

#### [Generating Inline View Components](https://laravel.com/docs/12.x/blade#generating-inline-view-components)
To create a component that renders an inline view, you may use the `inline` option when executing the `make:component` command:
```


1php artisan make:component Alert --inline




php artisan make:component Alert --inline

```

### [Dynamic Components](https://laravel.com/docs/12.x/blade#dynamic-components)
Sometimes you may need to render a component but not know which component should be rendered until runtime. In this situation, you may use Laravel's built-in `dynamic-component` component to render the component based on a runtime value or variable:
```


1// $componentName = "secondary-button";




2 



3<x-dynamic-component :component="$componentName" class="mt-4" />




// $componentName = "secondary-button";

<x-dynamic-component :component="$componentName" class="mt-4" />

```

### [Manually Registering Components](https://laravel.com/docs/12.x/blade#manually-registering-components)
The following documentation on manually registering components is primarily applicable to those who are writing Laravel packages that include view components. If you are not writing a package, this portion of the component documentation may not be relevant to you.
When writing components for your own application, components are automatically discovered within the `app/View/Components` directory and `resources/views/components` directory.
However, if you are building a package that utilizes Blade components or placing components in non-conventional directories, you will need to manually register your component class and its HTML tag alias so that Laravel knows where to find the component. You should typically register your components in the `boot` method of your package's service provider:
```


 1use Illuminate\Support\Facades\Blade;




 2use VendorPackage\View\Components\AlertComponent;




 3 



 4/**




 5 * Bootstrap your package's services.




 6 */




 7public function boot(): void




 8{




 9    Blade::component('package-alert', AlertComponent::class);




10}




use Illuminate\Support\Facades\Blade;
use VendorPackage\View\Components\AlertComponent;

/**
 * Bootstrap your package's services.
 */
public function boot(): void
{
    Blade::component('package-alert', AlertComponent::class);
}

```

Once your component has been registered, it may be rendered using its tag alias:
```


1<x-package-alert/>




<x-package-alert/>

```

#### Autoloading Package Components
Alternatively, you may use the `componentNamespace` method to autoload component classes by convention. For example, a `Nightshade` package might have `Calendar` and `ColorPicker` components that reside within the `Package\Views\Components` namespace:
```


1use Illuminate\Support\Facades\Blade;




2 



3/**




4 * Bootstrap your package's services.




5 */




6public function boot(): void




7{




8    Blade::componentNamespace('Nightshade\\Views\\Components', 'nightshade');




9}




use Illuminate\Support\Facades\Blade;

/**
 * Bootstrap your package's services.
 */
public function boot(): void
{
    Blade::componentNamespace('Nightshade\\Views\\Components', 'nightshade');
}

```

This will allow the usage of package components by their vendor namespace using the `package-name::` syntax:
```


1<x-nightshade::calendar />




2<x-nightshade::color-picker />




<x-nightshade::calendar />
<x-nightshade::color-picker />

```

Blade will automatically detect the class that's linked to this component by pascal-casing the component name. Subdirectories are also supported using "dot" notation.
