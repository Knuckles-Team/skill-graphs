## [Forms](https://laravel.com/docs/12.x/blade#forms)
### [CSRF Field](https://laravel.com/docs/12.x/blade#csrf-field)
Anytime you define an HTML form in your application, you should include a hidden CSRF token field in the form so that [the CSRF protection](https://laravel.com/docs/12.x/csrf) middleware can validate the request. You may use the `@csrf` Blade directive to generate the token field:
```


1<form method="POST" action="/profile">




2    @csrf




3 



4    ...




5</form>




<form method="POST" action="/profile">
    @csrf

    ...
</form>

```

### [Method Field](https://laravel.com/docs/12.x/blade#method-field)
Since HTML forms can't make `PUT`, `PATCH`, or `DELETE` requests, you will need to add a hidden `_method` field to spoof these HTTP verbs. The `@method` Blade directive can create this field for you:
```


1<form action="/foo/bar" method="POST">




2    @method('PUT')




3 



4    ...




5</form>




<form action="/foo/bar" method="POST">
    @method('PUT')

    ...
</form>

```

### [Validation Errors](https://laravel.com/docs/12.x/blade#validation-errors)
The `@error` directive may be used to quickly check if [validation error messages](https://laravel.com/docs/12.x/validation#quick-displaying-the-validation-errors) exist for a given attribute. Within an `@error` directive, you may echo the `$message` variable to display the error message:
```


 1<!-- /resources/views/post/create.blade.php -->




 2 



 3<label for="title">Post Title</label>




 4 



 5<input




 6    id="title"




 7    type="text"




 8    class="@error('title') is-invalid @enderror"




 9/>




10 



11@error('title')




12    <div class="alert alert-danger">{{ $message }}</div>




13@enderror




<!-- /resources/views/post/create.blade.php -->

<label for="title">Post Title</label>

<input
    id="title"
    type="text"
    class="@error('title') is-invalid @enderror"
/>

@error('title')
    <div class="alert alert-danger">{{ $message }}</div>
@enderror

```

Since the `@error` directive compiles to an "if" statement, you may use the `@else` directive to render content when there is not an error for an attribute:
```


1<!-- /resources/views/auth.blade.php -->




2 



3<label for="email">Email address</label>




4 



5<input




6    id="email"




7    type="email"




8    class="@error('email') is-invalid @else is-valid @enderror"




9/>




<!-- /resources/views/auth.blade.php -->

<label for="email">Email address</label>

<input
    id="email"
    type="email"
    class="@error('email') is-invalid @else is-valid @enderror"
/>

```

You may pass [the name of a specific error bag](https://laravel.com/docs/12.x/validation#named-error-bags) as the second parameter to the `@error` directive to retrieve validation error messages on pages containing multiple forms:
```


 1<!-- /resources/views/auth.blade.php -->




 2 



 3<label for="email">Email address</label>




 4 



 5<input




 6    id="email"




 7    type="email"




 8    class="@error('email', 'login') is-invalid @enderror"




 9/>




10 



11@error('email', 'login')




12    <div class="alert alert-danger">{{ $message }}</div>




13@enderror




<!-- /resources/views/auth.blade.php -->

<label for="email">Email address</label>

<input
    id="email"
    type="email"
    class="@error('email', 'login') is-invalid @enderror"
/>

@error('email', 'login')
    <div class="alert alert-danger">{{ $message }}</div>
@enderror

```
