## [Form Method Spoofing](https://laravel.com/docs/12.x/routing#form-method-spoofing)
HTML forms do not support `PUT`, `PATCH`, or `DELETE` actions. So, when defining `PUT`, `PATCH`, or `DELETE` routes that are called from an HTML form, you will need to add a hidden `_method` field to the form. The value sent with the `_method` field will be used as the HTTP request method:
```


1<form action="/example" method="POST">




2    <input type="hidden" name="_method" value="PUT">




3    <input type="hidden" name="_token" value="{{ csrf_token() }}">




4</form>




<form action="/example" method="POST">
    <input type="hidden" name="_method" value="PUT">
    <input type="hidden" name="_token" value="{{ csrf_token() }}">
</form>

```

For convenience, you may use the `@method` [Blade directive](https://laravel.com/docs/12.x/blade) to generate the `_method` input field:
```


1<form action="/example" method="POST">




2    @method('PUT')




3    @csrf




4</form>




<form action="/example" method="POST">
    @method('PUT')
    @csrf
</form>

```
