## [Stacks](https://laravel.com/docs/12.x/blade#stacks)
Blade allows you to push to named stacks which can be rendered somewhere else in another view or layout. This can be particularly useful for specifying any JavaScript libraries required by your child views:
```


1@push('scripts')




2    <script src="/example.js"></script>




3@endpush




@push('scripts')
    <script src="/example.js"></script>
@endpush

```

If you would like to `@push` content if a given boolean expression evaluates to `true`, you may use the `@pushIf` directive:
```


1@pushIf($shouldPush, 'scripts')




2    <script src="/example.js"></script>




3@endPushIf




@pushIf($shouldPush, 'scripts')
    <script src="/example.js"></script>
@endPushIf

```

You may push to a stack as many times as needed. To render the complete stack contents, pass the name of the stack to the `@stack` directive:
```


1<head>




2    <!-- Head Contents -->




3 



4    @stack('scripts')




5</head>




<head>
    <!-- Head Contents -->

    @stack('scripts')
</head>

```

If you would like to prepend content onto the beginning of a stack, you should use the `@prepend` directive:
```


1@push('scripts')




2    This will be second...




3@endpush




4 



5// Later...




6 



7@prepend('scripts')




8    This will be first...




9@endprepend




@push('scripts')
    This will be second...
@endpush

// Later...

@prepend('scripts')
    This will be first...
@endprepend

```

The `@hasstack` directive may be used to determine if a stack is empty:
```


1@hasstack('list')




2    <ul>




3        @stack('list')




4    </ul>




5@endif




@hasstack('list')
    <ul>
        @stack('list')
    </ul>
@endif

```
