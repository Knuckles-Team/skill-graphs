## [Disabling Vite in Tests](https://laravel.com/docs/12.x/vite#disabling-vite-in-tests)
Laravel's Vite integration will attempt to resolve your assets while running your tests, which requires you to either run the Vite development server or build your assets.
If you would prefer to mock Vite during testing, you may call the `withoutVite` method, which is available for any tests that extend Laravel's `TestCase` class:
Pest PHPUnit
```


1test('without vite example', function () {




2    $this->withoutVite();




3 



4    // ...




5});




test('without vite example', function () {
    $this->withoutVite();

    // ...
});

```

```


 1use Tests\TestCase;




 2 



 3class ExampleTest extends TestCase




 4{




 5    public function test_without_vite_example(): void




 6    {




 7        $this->withoutVite();




 8 



 9        // ...




10    }




11}




use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_without_vite_example(): void
    {
        $this->withoutVite();

        // ...
    }
}

```

If you would like to disable Vite for all tests, you may call the `withoutVite` method from the `setUp` method on your base `TestCase` class:
```


 1<?php




 2 



 3namespace Tests;




 4 



 5use Illuminate\Foundation\Testing\TestCase as BaseTestCase;




 6 



 7abstract class TestCase extends BaseTestCase




 8{




 9    protected function setUp(): void




10    {




11        parent::setUp();




12 



13        $this->withoutVite();




14    }




15}




<?php

namespace Tests;

use Illuminate\Foundation\Testing\TestCase as BaseTestCase;

abstract class TestCase extends BaseTestCase
{
    protected function setUp(): void
    {
        parent::setUp();

        $this->withoutVite();
    }
}

```
