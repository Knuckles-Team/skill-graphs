## [Transforming Input Before Validation](https://laravel.com/docs/12.x/prompts#transforming-input-before-validation)
Sometimes you may want to transform the prompt input before validation takes place. For example, you may wish to remove white space from any provided strings. To accomplish this, many of the prompt functions provide a `transform` argument, which accepts a closure:
```


1$name = text(




2    label: 'What is your name?',




3    transform: fn (string $value) => trim($value),




4    validate: fn (string $value) => match (true) {




5        strlen($value) < 3 => 'The name must be at least 3 characters.',




6        strlen($value) > 255 => 'The name must not exceed 255 characters.',




7        default => null




8    }




9);




$name = text(
    label: 'What is your name?',
    transform: fn (string $value) => trim($value),
    validate: fn (string $value) => match (true) {
        strlen($value) < 3 => 'The name must be at least 3 characters.',
        strlen($value) > 255 => 'The name must not exceed 255 characters.',
        default => null
    }
);

```
