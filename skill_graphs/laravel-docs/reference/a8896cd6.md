## [Making Requests](https://laravel.com/docs/12.x/http-tests#making-requests)
To make a request to your application, you may invoke the `get`, `post`, `put`, `patch`, or `delete` methods within your test. These methods do not actually issue a "real" HTTP request to your application. Instead, the entire network request is simulated internally.
Instead of returning an `Illuminate\Http\Response` instance, test request methods return an instance of `Illuminate\Testing\TestResponse`, which provides a [variety of helpful assertions](https://laravel.com/docs/12.x/http-tests#available-assertions) that allow you to inspect your application's responses:
Pest PHPUnit
```


1<?php




2 



3test('basic request', function () {




4    $response = $this->get('/');




5 



6    $response->assertStatus(200);




7});




<?php

test('basic request', function () {
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




12    public function test_a_basic_request(): void




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
    public function test_a_basic_request(): void
    {
        $response = $this->get('/');

        $response->assertStatus(200);
    }
}

```

In general, each of your tests should only make one request to your application. Unexpected behavior may occur if multiple requests are executed within a single test method.
For convenience, the CSRF middleware is automatically disabled when running tests.
### [Customizing Request Headers](https://laravel.com/docs/12.x/http-tests#customizing-request-headers)
You may use the `withHeaders` method to customize the request's headers before it is sent to the application. This method allows you to add any custom headers you would like to the request:
Pest PHPUnit
```


1<?php




2 



3test('interacting with headers', function () {




4    $response = $this->withHeaders([




5        'X-Header' => 'Value',




6    ])->post('/user', ['name' => 'Sally']);




7 



8    $response->assertStatus(201);




9});




<?php

test('interacting with headers', function () {
    $response = $this->withHeaders([
        'X-Header' => 'Value',
    ])->post('/user', ['name' => 'Sally']);

    $response->assertStatus(201);
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




10     * A basic functional test example.




11     */




12    public function test_interacting_with_headers(): void




13    {




14        $response = $this->withHeaders([




15            'X-Header' => 'Value',




16        ])->post('/user', ['name' => 'Sally']);




17 



18        $response->assertStatus(201);




19    }




20}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic functional test example.
     */
    public function test_interacting_with_headers(): void
    {
        $response = $this->withHeaders([
            'X-Header' => 'Value',
        ])->post('/user', ['name' => 'Sally']);

        $response->assertStatus(201);
    }
}

```

### [Cookies](https://laravel.com/docs/12.x/http-tests#cookies)
You may use the `withCookie` or `withCookies` methods to set cookie values before making a request. The `withCookie` method accepts a cookie name and value as its two arguments, while the `withCookies` method accepts an array of name / value pairs:
Pest PHPUnit
```


 1<?php




 2 



 3test('interacting with cookies', function () {




 4    $response = $this->withCookie('color', 'blue')->get('/');




 5 



 6    $response = $this->withCookies([




 7        'color' => 'blue',




 8        'name' => 'Taylor',




 9    ])->get('/');




10 



11    //




12});




<?php

test('interacting with cookies', function () {
    $response = $this->withCookie('color', 'blue')->get('/');

    $response = $this->withCookies([
        'color' => 'blue',
        'name' => 'Taylor',
    ])->get('/');

    //
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




 9    public function test_interacting_with_cookies(): void




10    {




11        $response = $this->withCookie('color', 'blue')->get('/');




12 



13        $response = $this->withCookies([




14            'color' => 'blue',




15            'name' => 'Taylor',




16        ])->get('/');




17 



18        //




19    }




20}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_interacting_with_cookies(): void
    {
        $response = $this->withCookie('color', 'blue')->get('/');

        $response = $this->withCookies([
            'color' => 'blue',
            'name' => 'Taylor',
        ])->get('/');

        //
    }
}

```

### [Session / Authentication](https://laravel.com/docs/12.x/http-tests#session-and-authentication)
Laravel provides several helpers for interacting with the session during HTTP testing. First, you may set the session data to a given array using the `withSession` method. This is useful for loading the session with data before issuing a request to your application:
Pest PHPUnit
```


1<?php




2 



3test('interacting with the session', function () {




4    $response = $this->withSession(['banned' => false])->get('/');




5 



6    //




7});




<?php

test('interacting with the session', function () {
    $response = $this->withSession(['banned' => false])->get('/');

    //
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




 9    public function test_interacting_with_the_session(): void




10    {




11        $response = $this->withSession(['banned' => false])->get('/');




12 



13        //




14    }




15}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_interacting_with_the_session(): void
    {
        $response = $this->withSession(['banned' => false])->get('/');

        //
    }
}

```

Laravel's session is typically used to maintain state for the currently authenticated user. Therefore, the `actingAs` helper method provides a simple way to authenticate a given user as the current user. For example, we may use a [model factory](https://laravel.com/docs/12.x/eloquent-factories) to generate and authenticate a user:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Models\User;




 4 



 5test('an action that requires authentication', function () {




 6    $user = User::factory()->create();




 7 



 8    $response = $this->actingAs($user)




 9        ->withSession(['banned' => false])




10        ->get('/');




11 



12    //




13});




<?php

use App\Models\User;

test('an action that requires authentication', function () {
    $user = User::factory()->create();

    $response = $this->actingAs($user)
        ->withSession(['banned' => false])
        ->get('/');

    //
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use App\Models\User;




 6use Tests\TestCase;




 7 



 8class ExampleTest extends TestCase




 9{




10    public function test_an_action_that_requires_authentication(): void




11    {




12        $user = User::factory()->create();




13 



14        $response = $this->actingAs($user)




15            ->withSession(['banned' => false])




16            ->get('/');




17 



18        //




19    }




20}




<?php

namespace Tests\Feature;

use App\Models\User;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    public function test_an_action_that_requires_authentication(): void
    {
        $user = User::factory()->create();

        $response = $this->actingAs($user)
            ->withSession(['banned' => false])
            ->get('/');

        //
    }
}

```

You may also specify which guard should be used to authenticate the given user by passing the guard name as the second argument to the `actingAs` method. The guard that is provided to the `actingAs` method will also become the default guard for the duration of the test:
```


1$this->actingAs($user, 'web');




$this->actingAs($user, 'web');

```

If you would like to ensure the request is unauthenticated, you may use the `actingAsGuest` method:
```


1$this->actingAsGuest();




$this->actingAsGuest();

```

### [Debugging Responses](https://laravel.com/docs/12.x/http-tests#debugging-responses)
After making a test request to your application, the `dump`, `dumpHeaders`, and `dumpSession` methods may be used to examine and debug the response contents:
Pest PHPUnit
```


1<?php




2 



3test('basic test', function () {




4    $response = $this->get('/');




5 



6    $response->dump();




7    $response->dumpHeaders();




8    $response->dumpSession();




9});




<?php

test('basic test', function () {
    $response = $this->get('/');

    $response->dump();
    $response->dumpHeaders();
    $response->dumpSession();
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




12    public function test_basic_test(): void




13    {




14        $response = $this->get('/');




15 



16        $response->dump();




17        $response->dumpHeaders();




18        $response->dumpSession();




19    }




20}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     */
    public function test_basic_test(): void
    {
        $response = $this->get('/');

        $response->dump();
        $response->dumpHeaders();
        $response->dumpSession();
    }
}

```

Alternatively, you may use the `dd`, `ddHeaders`, `ddBody`, `ddJson`, and `ddSession` methods to dump information about the response and then stop execution:
Pest PHPUnit
```


 1<?php




 2 



 3test('basic test', function () {




 4    $response = $this->get('/');




 5 



 6    $response->dd();




 7    $response->ddHeaders();




 8    $response->ddBody();




 9    $response->ddJson();




10    $response->ddSession();




11});




<?php

test('basic test', function () {
    $response = $this->get('/');

    $response->dd();
    $response->ddHeaders();
    $response->ddBody();
    $response->ddJson();
    $response->ddSession();
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




12    public function test_basic_test(): void




13    {




14        $response = $this->get('/');




15 



16        $response->dd();




17        $response->ddHeaders();




18        $response->ddBody();




19        $response->ddJson();




20        $response->ddSession();




21    }




22}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     */
    public function test_basic_test(): void
    {
        $response = $this->get('/');

        $response->dd();
        $response->ddHeaders();
        $response->ddBody();
        $response->ddJson();
        $response->ddSession();
    }
}

```

### [Exception Handling](https://laravel.com/docs/12.x/http-tests#exception-handling)
Sometimes you may need to test that your application is throwing a specific exception. To accomplish this, you may "fake" the exception handler via the `Exceptions` facade. Once the exception handler has been faked, you may utilize the `assertReported` and `assertNotReported` methods to make assertions against exceptions that were thrown during the request:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Exceptions\InvalidOrderException;




 4use Illuminate\Support\Facades\Exceptions;




 5 



 6test('exception is thrown', function () {




 7    Exceptions::fake();




 8 



 9    $response = $this->get('/order/1');




10 



11    // Assert an exception was thrown...




12    Exceptions::assertReported(InvalidOrderException::class);




13 



14    // Assert against the exception...




15    Exceptions::assertReported(function (InvalidOrderException $e) {




16        return $e->getMessage() === 'The order was invalid.';




17    });




18});




<?php

use App\Exceptions\InvalidOrderException;
use Illuminate\Support\Facades\Exceptions;

test('exception is thrown', function () {
    Exceptions::fake();

    $response = $this->get('/order/1');

    // Assert an exception was thrown...
    Exceptions::assertReported(InvalidOrderException::class);

    // Assert against the exception...
    Exceptions::assertReported(function (InvalidOrderException $e) {
        return $e->getMessage() === 'The order was invalid.';
    });
});

```

```


 1<?php




 2 



 3namespace Tests\Feature;




 4 



 5use App\Exceptions\InvalidOrderException;




 6use Illuminate\Support\Facades\Exceptions;




 7use Tests\TestCase;




 8 



 9class ExampleTest extends TestCase




10{




11    /**




12     * A basic test example.




13     */




14    public function test_exception_is_thrown(): void




15    {




16        Exceptions::fake();




17 



18        $response = $this->get('/');




19 



20        // Assert an exception was thrown...




21        Exceptions::assertReported(InvalidOrderException::class);




22 



23        // Assert against the exception...




24        Exceptions::assertReported(function (InvalidOrderException $e) {




25            return $e->getMessage() === 'The order was invalid.';




26        });




27    }




28}




<?php

namespace Tests\Feature;

use App\Exceptions\InvalidOrderException;
use Illuminate\Support\Facades\Exceptions;
use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     */
    public function test_exception_is_thrown(): void
    {
        Exceptions::fake();

        $response = $this->get('/');

        // Assert an exception was thrown...
        Exceptions::assertReported(InvalidOrderException::class);

        // Assert against the exception...
        Exceptions::assertReported(function (InvalidOrderException $e) {
            return $e->getMessage() === 'The order was invalid.';
        });
    }
}

```

The `assertNotReported` and `assertNothingReported` methods may be used to assert that a given exception was not thrown during the request or that no exceptions were thrown:
```


1Exceptions::assertNotReported(InvalidOrderException::class);




2 



3Exceptions::assertNothingReported();




Exceptions::assertNotReported(InvalidOrderException::class);

Exceptions::assertNothingReported();

```

You may totally disable exception handling for a given request by invoking the `withoutExceptionHandling` method before making your request:
```


1$response = $this->withoutExceptionHandling()->get('/');




$response = $this->withoutExceptionHandling()->get('/');

```

In addition, if you would like to ensure that your application is not utilizing features that have been deprecated by the PHP language or the libraries your application is using, you may invoke the `withoutDeprecationHandling` method before making your request. When deprecation handling is disabled, deprecation warnings will be converted to exceptions, thus causing your test to fail:
```


1$response = $this->withoutDeprecationHandling()->get('/');




$response = $this->withoutDeprecationHandling()->get('/');

```

The `assertThrows` method may be used to assert that code within a given closure throws an exception of the specified type:
```


1$this->assertThrows(




2    fn () => (new ProcessOrder)->execute(),




3    OrderInvalid::class




4);




$this->assertThrows(
    fn () => (new ProcessOrder)->execute(),
    OrderInvalid::class
);

```

If you would like to inspect and make assertions against the exception that is thrown, you may provide a closure as the second argument to the `assertThrows` method:
```


1$this->assertThrows(




2    fn () => (new ProcessOrder)->execute(),




3    fn (OrderInvalid $e) => $e->orderId() === 123;




4);




$this->assertThrows(
    fn () => (new ProcessOrder)->execute(),
    fn (OrderInvalid $e) => $e->orderId() === 123;
);

```

The `assertDoesntThrow` method may be used to assert that the code within a given closure does not throw any exceptions:
```


1$this->assertDoesntThrow(fn () => (new ProcessOrder)->execute());




$this->assertDoesntThrow(fn () => (new ProcessOrder)->execute());

```
