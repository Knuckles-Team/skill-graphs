## [Anonymous Components](https://laravel.com/docs/12.x/blade#anonymous-components)
Similar to inline components, anonymous components provide a mechanism for managing a component via a single file. However, anonymous components utilize a single view file and have no associated class. To define an anonymous component, you only need to place a Blade template within your `resources/views/components` directory. For example, assuming you have defined a component at `resources/views/components/alert.blade.php`, you may simply render it like so:
```


1<x-alert/>




<x-alert/>

```

You may use the `.` character to indicate if a component is nested deeper inside the `components` directory. For example, assuming the component is defined at `resources/views/components/inputs/button.blade.php`, you may render it like so:
```


1<x-inputs.button/>




<x-inputs.button/>

```

To create an anonymous component via Artisan, you may use the `--view` flag when invoking the `make:component` command:
```


1php artisan make:component forms.input --view




php artisan make:component forms.input --view

```

The command above will create a Blade file at `resources/views/components/forms/input.blade.php` which can be rendered as a component via `<x-forms.input />`.
### [Anonymous Index Components](https://laravel.com/docs/12.x/blade#anonymous-index-components)
Sometimes, when a component is made up of many Blade templates, you may wish to group the given component's templates within a single directory. For example, imagine an "accordion" component with the following directory structure:
```


1/resources/views/components/accordion.blade.php




2/resources/views/components/accordion/item.blade.php




/resources/views/components/accordion.blade.php
/resources/views/components/accordion/item.blade.php

```

This directory structure allows you to render the accordion component and its item like so:
```


1<x-accordion>




2    <x-accordion.item>




3        ...




4    </x-accordion.item>




5</x-accordion>




<x-accordion>
    <x-accordion.item>
        ...
    </x-accordion.item>
</x-accordion>

```

However, in order to render the accordion component via `x-accordion`, we were forced to place the "index" accordion component template in the `resources/views/components` directory instead of nesting it within the `accordion` directory with the other accordion related templates.
Thankfully, Blade allows you to place a file matching the component's directory name within the component's directory itself. When this template exists, it can be rendered as the "root" element of the component even though it is nested within a directory. So, we can continue to use the same Blade syntax given in the example above; however, we will adjust our directory structure like so:
```


1/resources/views/components/accordion/accordion.blade.php




2/resources/views/components/accordion/item.blade.php




/resources/views/components/accordion/accordion.blade.php
/resources/views/components/accordion/item.blade.php

```

### [Data Properties / Attributes](https://laravel.com/docs/12.x/blade#data-properties-attributes)
Since anonymous components do not have any associated class, you may wonder how you may differentiate which data should be passed to the component as variables and which attributes should be placed in the component's [attribute bag](https://laravel.com/docs/12.x/blade#component-attributes).
You may specify which attributes should be considered data variables using the `@props` directive at the top of your component's Blade template. All other attributes on the component will be available via the component's attribute bag. If you wish to give a data variable a default value, you may specify the variable's name as the array key and the default value as the array value:
```


1<!-- /resources/views/components/alert.blade.php -->




2 



3@props(['type' => 'info', 'message'])




4 



5<div {{ $attributes->merge(['class' => 'alert alert-'.$type]) }}>




6    {{ $message }}




7</div>




<!-- /resources/views/components/alert.blade.php -->

@props(['type' => 'info', 'message'])

<div {{ $attributes->merge(['class' => 'alert alert-'.$type]) }}>
    {{ $message }}
</div>

```

Given the component definition above, we may render the component like so:
```


1<x-alert type="error" :message="$message" class="mb-4"/>




<x-alert type="error" :message="$message" class="mb-4"/>

```

### [Accessing Parent Data](https://laravel.com/docs/12.x/blade#accessing-parent-data)
Sometimes you may want to access data from a parent component inside a child component. In these cases, you may use the `@aware` directive. For example, imagine we are building a complex menu component consisting of a parent `<x-menu>` and child `<x-menu.item>`:
```


1<x-menu color="purple">




2    <x-menu.item>...</x-menu.item>




3    <x-menu.item>...</x-menu.item>




4</x-menu>




<x-menu color="purple">
    <x-menu.item>...</x-menu.item>
    <x-menu.item>...</x-menu.item>
</x-menu>

```

The `<x-menu>` component may have an implementation like the following:
```


1<!-- /resources/views/components/menu/index.blade.php -->




2 



3@props(['color' => 'gray'])




4 



5<ul {{ $attributes->merge(['class' => 'bg-'.$color.'-200']) }}>




6    {{ $slot }}




7</ul>




<!-- /resources/views/components/menu/index.blade.php -->

@props(['color' => 'gray'])

<ul {{ $attributes->merge(['class' => 'bg-'.$color.'-200']) }}>
    {{ $slot }}
</ul>

```

Because the `color` prop was only passed into the parent (`<x-menu>`), it won't be available inside `<x-menu.item>`. However, if we use the `@aware` directive, we can make it available inside `<x-menu.item>` as well:
```


1<!-- /resources/views/components/menu/item.blade.php -->




2 



3@aware(['color' => 'gray'])




4 



5<li {{ $attributes->merge(['class' => 'text-'.$color.'-800']) }}>




6    {{ $slot }}




7</li>




<!-- /resources/views/components/menu/item.blade.php -->

@aware(['color' => 'gray'])

<li {{ $attributes->merge(['class' => 'text-'.$color.'-800']) }}>
    {{ $slot }}
</li>

```

The `@aware` directive cannot access parent data that is not explicitly passed to the parent component via HTML attributes. Default `@props` values that are not explicitly passed to the parent component cannot be accessed by the `@aware` directive.
### [Anonymous Component Paths](https://laravel.com/docs/12.x/blade#anonymous-component-paths)
As previously discussed, anonymous components are typically defined by placing a Blade template within your `resources/views/components` directory. However, you may occasionally want to register other anonymous component paths with Laravel in addition to the default path.
The `anonymousComponentPath` method accepts the "path" to the anonymous component location as its first argument and an optional "namespace" that components should be placed under as its second argument. Typically, this method should be called from the `boot` method of one of your application's [service providers](https://laravel.com/docs/12.x/providers):
```


1/**




2 * Bootstrap any application services.




3 */




4public function boot(): void




5{




6    Blade::anonymousComponentPath(__DIR__.'/../components');




7}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Blade::anonymousComponentPath(__DIR__.'/../components');
}

```

When component paths are registered without a specified prefix as in the example above, they may be rendered in your Blade components without a corresponding prefix as well. For example, if a `panel.blade.php` component exists in the path registered above, it may be rendered like so:
```


1<x-panel />




<x-panel />

```

Prefix "namespaces" may be provided as the second argument to the `anonymousComponentPath` method:
```


1Blade::anonymousComponentPath(__DIR__.'/../components', 'dashboard');




Blade::anonymousComponentPath(__DIR__.'/../components', 'dashboard');

```

When a prefix is provided, components within that "namespace" may be rendered by prefixing the component's namespace to the component name when the component is rendered:
```


1<x-dashboard::panel />




<x-dashboard::panel />

```
