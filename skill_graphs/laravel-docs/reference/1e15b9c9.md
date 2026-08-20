## [Testing Views](https://laravel.com/docs/12.x/http-tests#testing-views)
Laravel also allows you to render a view without making a simulated HTTP request to the application. To accomplish this, you may call the `view` method within your test. The `view` method accepts the view name and an optional array of data. The method returns an instance of `Illuminate\Testing\TestView`, which offers several methods to conveniently make assertions about the view's contents:
Pest PHPUnit
```


1<?php




2 



3test('a welcome view can be rendered', function () {




4    $view = $this->view('welcome', ['name' => 'Taylor']);




5 



6    $view->assertSee('Taylor');




7});




<?php

test('a welcome view can be rendered', function () {
    $view = $this->view('welcome', ['name' => 'Taylor']);

    $view->assertSee('Taylor');
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use Tests\TestCase;




 6 



 7class ExampleTest extends TestCase




 8{




 9    public function test_a_welcome_view_can_be_rendered(): void




10    {




11        $view = $this->view('welcome', ['name' => 'Taylor']);




12 



13        $view->assertSee('Taylor');




14    }




15}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_a_welcome_view_can_be_rendered(): void
    {
        $view = $this->view('welcome', ['name' => 'Taylor']);

        $view->assertSee('Taylor');
    }
}

```

The `TestView` class provides the following assertion methods: `assertSee`, `assertSeeInOrder`, `assertSeeText`, `assertSeeTextInOrder`, `assertDontSee`, and `assertDontSeeText`.
If needed, you may get the raw, rendered view contents by casting the `TestView` instance to a string:
```


1$contents = (string) $this->view('welcome');




$contents = (string) $this->view('welcome');

```

#### [Sharing Errors](https://laravel.com/docs/12.x/http-tests#sharing-errors)
Some views may depend on errors shared in the [global error bag provided by Laravel](https://laravel.com/docs/12.x/validation#quick-displaying-the-validation-errors). To hydrate the error bag with error messages, you may use the `withViewErrors` method:
```


1$view = $this->withViewErrors([




2    'name' => ['Please provide a valid name.']




3])->view('form');




4 



5$view->assertSee('Please provide a valid name.');




$view = $this->withViewErrors([
    'name' => ['Please provide a valid name.']
])->view('form');

$view->assertSee('Please provide a valid name.');

```

### [Rendering Blade and Components](https://laravel.com/docs/12.x/http-tests#rendering-blade-and-components)
If necessary, you may use the `blade` method to evaluate and render a raw [Blade](https://laravel.com/docs/12.x/blade) string. Like the `view` method, the `blade` method returns an instance of `Illuminate\Testing\TestView`:
```


1$view = $this->blade(




2    '<x-component :name="$name" />',




3    ['name' => 'Taylor']




4);




5 



6$view->assertSee('Taylor');




$view = $this->blade(
    '<x-component :name="$name" />',
    ['name' => 'Taylor']
);

$view->assertSee('Taylor');

```

You may use the `component` method to evaluate and render a [Blade component](https://laravel.com/docs/12.x/blade#components). The `component` method returns an instance of `Illuminate\Testing\TestComponent`:
```


1$view = $this->component(Profile::class, ['name' => 'Taylor']);




2 



3$view->assertSee('Taylor');




$view = $this->component(Profile::class, ['name' => 'Taylor']);

$view->assertSee('Taylor');

```
