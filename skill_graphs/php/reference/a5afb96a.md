## [Introduction](https://laravel.com/docs/12.x/http-tests#introduction)
Laravel provides a very fluent API for making HTTP requests to your application and examining the responses. For example, take a look at the feature test defined below:
Pest PHPUnit
```


1<?php




2 



3test('the application returns a successful response', function () {




4    $response = $this->get('/');




5 



6    $response->assertStatus(200);




7});




<?php

test('the application returns a successful response', function () {
    $response = $this->get('/');

    $response->assertStatus(200);
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




 9    /**




10     * A basic test example.




11     */




12    public function test_the_application_returns_a_successful_response(): void




13    {




14        $response = $this->get('/');




15 



16        $response->assertStatus(200);




17    }




18}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     */
    public function test_the_application_returns_a_successful_response(): void
    {
        $response = $this->get('/');

        $response->assertStatus(200);
    }
}

```

The `get` method makes a `GET` request into the application, while the `assertStatus` method asserts that the returned response should have the given HTTP status code. In addition to this simple assertion, Laravel also contains a variety of assertions for inspecting the response headers, content, JSON structure, and more.
