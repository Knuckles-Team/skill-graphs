## [Displaying Data](https://laravel.com/docs/12.x/blade#displaying-data)
You may display data that is passed to your Blade views by wrapping the variable in curly braces. For example, given the following route:
```


1Route::get('/', function () {




2    return view('welcome', ['name' => 'Samantha']);




3});




Route::get('/', function () {
    return view('welcome', ['name' => 'Samantha']);
});

```

You may display the contents of the `name` variable like so:
```


1Hello, {{ $name }}.




Hello, {{ $name }}.

```

Blade's `{{ }}` echo statements are automatically sent through PHP's `htmlspecialchars` function to prevent XSS attacks.
You are not limited to displaying the contents of the variables passed to the view. You may also echo the results of any PHP function. In fact, you can put any PHP code you wish inside of a Blade echo statement:
```


1The current UNIX timestamp is {{ time() }}.




The current UNIX timestamp is {{ time() }}.

```

### [HTML Entity Encoding](https://laravel.com/docs/12.x/blade#html-entity-encoding)
By default, Blade (and the Laravel `e` function) will double encode HTML entities. If you would like to disable double encoding, call the `Blade::withoutDoubleEncoding` method from the `boot` method of your `AppServiceProvider`:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Support\Facades\Blade;




 6use Illuminate\Support\ServiceProvider;




 7 



 8class AppServiceProvider extends ServiceProvider




 9{




10    /**




11     * Bootstrap any application services.




12     */




13    public function boot(): void




14    {




15        Blade::withoutDoubleEncoding();




16    }




17}




<?php

namespace App\Providers;

use Illuminate\Support\Facades\Blade;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Blade::withoutDoubleEncoding();
    }
}

```

#### [Displaying Unescaped Data](https://laravel.com/docs/12.x/blade#displaying-unescaped-data)
By default, Blade `{{ }}` statements are automatically sent through PHP's `htmlspecialchars` function to prevent XSS attacks. If you do not want your data to be escaped, you may use the following syntax:
```


1Hello, {!! $name !!}.




Hello, {!! $name !!}.

```

Be very careful when echoing content that is supplied by users of your application. You should typically use the escaped, double curly brace syntax to prevent XSS attacks when displaying user supplied data.
### [Blade and JavaScript Frameworks](https://laravel.com/docs/12.x/blade#blade-and-javascript-frameworks)
Since many JavaScript frameworks also use "curly" braces to indicate a given expression should be displayed in the browser, you may use the `@` symbol to inform the Blade rendering engine an expression should remain untouched. For example:
```


1<h1>Laravel</h1>




2 



3Hello, @{{ name }}.




<h1>Laravel</h1>

Hello, @{{ name }}.

```

In this example, the `@` symbol will be removed by Blade; however, the `{{ name }}` expression will remain untouched by the Blade engine, allowing it to be rendered by your JavaScript framework.
The `@` symbol may also be used to escape Blade directives:
```


1{{-- Blade template --}}




2@@if()




3 



4<!-- HTML output -->




5@if()




{{-- Blade template --}}
@@if()

<!-- HTML output -->
@if()

```

#### [Rendering JSON](https://laravel.com/docs/12.x/blade#rendering-json)
Sometimes you may pass an array to your view with the intention of rendering it as JSON in order to initialize a JavaScript variable. For example:
```


1<script>




2    var app = <?php echo json_encode($array); ?>;




3</script>




<script>
    var app = <?php echo json_encode($array); ?>;
</script>

```

However, instead of manually calling `json_encode`, you may use the `Illuminate\Support\Js::from` method. The `from` method accepts the same arguments as PHP's `json_encode` function; however, it will ensure that the resulting JSON has been properly escaped for inclusion within HTML quotes. The `from` method will return a string `JSON.parse` JavaScript statement that will convert the given object or array into a valid JavaScript object:
```


1<script>




2    var app = {{ Illuminate\Support\Js::from($array) }};




3</script>




<script>
    var app = {{ Illuminate\Support\Js::from($array) }};
</script>

```

The latest versions of the Laravel application skeleton include a `Js` facade, which provides convenient access to this functionality within your Blade templates:
```


1<script>




2    var app = {{ Js::from($array) }};




3</script>




<script>
    var app = {{ Js::from($array) }};
</script>

```

You should only use the `Js::from` method to render existing variables as JSON. The Blade templating is based on regular expressions and attempts to pass a complex expression to the directive may cause unexpected failures.
#### [The `@verbatim` Directive](https://laravel.com/docs/12.x/blade#the-at-verbatim-directive)
If you are displaying JavaScript variables in a large portion of your template, you may wrap the HTML in the `@verbatim` directive so that you do not have to prefix each Blade echo statement with an `@` symbol:
```


1@verbatim




2    <div class="container">




3        Hello, {{ name }}.




4    </div>




5@endverbatim




@verbatim
    <div class="container">
        Hello, {{ name }}.
    </div>
@endverbatim

```
