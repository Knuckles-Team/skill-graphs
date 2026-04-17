## [Spin](https://laravel.com/docs/12.x/prompts#spin)
The `spin` function displays a spinner along with an optional message while executing a specified callback. It serves to indicate ongoing processes and returns the callback's results upon completion:
```


1use function Laravel\Prompts\spin;




2 



3$response = spin(




4    callback: fn () => Http::get('http://example.com'),




5    message: 'Fetching response...'




6);




use function Laravel\Prompts\spin;

$response = spin(
    callback: fn () => Http::get('http://example.com'),
    message: 'Fetching response...'
);

```

The `spin` function requires the
