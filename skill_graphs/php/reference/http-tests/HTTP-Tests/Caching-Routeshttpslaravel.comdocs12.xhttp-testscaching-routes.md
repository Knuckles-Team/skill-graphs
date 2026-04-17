## [Caching Routes](https://laravel.com/docs/12.x/http-tests#caching-routes)
Before a test runs, Laravel boots a fresh instance of the application, including collecting all defined routes. If your applications have many route files, you may wish to add the `Illuminate\Foundation\Testing\WithCachedRoutes` trait to your test cases. On tests which use this trait, routes are built once and stored in memory, meaning the route collection process is only run once for all tests in your suite:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Http\Controllers\UserController;




 4use Illuminate\Foundation\Testing\WithCachedRoutes;




 5 



 6pest()->use(WithCachedRoutes::class);




 7 



 8test('basic example', function () {




 9    $this->get(action([UserController::class, 'index']));




10 



11    // ...




12});




<?php

use App\Http\Controllers\UserController;
use Illuminate\Foundation\Testing\WithCachedRoutes;

pest()->use(WithCachedRoutes::class);

test('basic example', function () {
    $this->get(action([UserController::class, 'index']));

    // ...
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use App\Http\Controllers\UserController;




 6use Illuminate\Foundation\Testing\WithCachedRoutes;




 7use Tests\TestCase;




 8 



 9class BasicTest extends TestCase




10{




11    use WithCachedRoutes;




12 



13    /**




14     * A basic functional test example.




15     */




16    public function test_basic_example(): void




17    {




18        $response = $this->get(action([UserController::class, 'index']));




19 



20        // ...




21    }




22}




<?php

namespace Tests\Feature;

use App\Http\Controllers\UserController;
use Illuminate\Foundation\Testing\WithCachedRoutes;
use Tests\TestCase;

class BasicTest extends TestCase
{
    use WithCachedRoutes;

    /**
     * A basic functional test example.
     */
    public function test_basic_example(): void
    {
        $response = $this->get(action([UserController::class, 'index']));

        // ...
    }
}

```
