## [Testing JSON APIs](https://laravel.com/docs/12.x/http-tests#testing-json-apis)
Laravel also provides several helpers for testing JSON APIs and their responses. For example, the `json`, `getJson`, `postJson`, `putJson`, `patchJson`, `deleteJson`, and `optionsJson` methods may be used to issue JSON requests with various HTTP verbs. You may also easily pass data and headers to these methods. To get started, let's write a test to make a `POST` request to `/api/user` and assert that the expected JSON data was returned:
Pest PHPUnit
```


 1<?php




 2 



 3test('making an api request', function () {




 4    $response = $this->postJson('/api/user', ['name' => 'Sally']);




 5 



 6    $response




 7        ->assertStatus(201)




 8        ->assertJson([




 9            'created' => true,




10        ]);




11});




<?php

test('making an api request', function () {
    $response = $this->postJson('/api/user', ['name' => 'Sally']);

    $response
        ->assertStatus(201)
        ->assertJson([
            'created' => true,
        ]);
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




12    public function test_making_an_api_request(): void




13    {




14        $response = $this->postJson('/api/user', ['name' => 'Sally']);




15 



16        $response




17            ->assertStatus(201)




18            ->assertJson([




19                'created' => true,




20            ]);




21    }




22}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic functional test example.
     */
    public function test_making_an_api_request(): void
    {
        $response = $this->postJson('/api/user', ['name' => 'Sally']);

        $response
            ->assertStatus(201)
            ->assertJson([
                'created' => true,
            ]);
    }
}

```

In addition, JSON response data may be accessed as array variables on the response, making it convenient for you to inspect the individual values returned within a JSON response:
Pest PHPUnit
```


1expect($response['created'])->toBeTrue();




expect($response['created'])->toBeTrue();

```

```


1$this->assertTrue($response['created']);




$this->assertTrue($response['created']);

```

The `assertJson` method converts the response to an array to verify that the given array exists within the JSON response returned by the application. So, if there are other properties in the JSON response, this test will still pass as long as the given fragment is present.
#### [Asserting Exact JSON Matches](https://laravel.com/docs/12.x/http-tests#verifying-exact-match)
As previously mentioned, the `assertJson` method may be used to assert that a fragment of JSON exists within the JSON response. If you would like to verify that a given array **exactly matches** the JSON returned by your application, you should use the `assertExactJson` method:
Pest PHPUnit
```


 1<?php




 2 



 3test('asserting an exact json match', function () {




 4    $response = $this->postJson('/user', ['name' => 'Sally']);




 5 



 6    $response




 7        ->assertStatus(201)




 8        ->assertExactJson([




 9            'created' => true,




10        ]);




11});




<?php

test('asserting an exact json match', function () {
    $response = $this->postJson('/user', ['name' => 'Sally']);

    $response
        ->assertStatus(201)
        ->assertExactJson([
            'created' => true,
        ]);
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




12    public function test_asserting_an_exact_json_match(): void




13    {




14        $response = $this->postJson('/user', ['name' => 'Sally']);




15 



16        $response




17            ->assertStatus(201)




18            ->assertExactJson([




19                'created' => true,




20            ]);




21    }




22}




<?php

namespace Tests\Feature;

use Tests\TestCase;

class ExampleTest extends TestCase
{
    /**
     * A basic functional test example.
     */
    public function test_asserting_an_exact_json_match(): void
    {
        $response = $this->postJson('/user', ['name' => 'Sally']);

        $response
            ->assertStatus(201)
            ->assertExactJson([
                'created' => true,
            ]);
    }
}

```

#### [Asserting on JSON Paths](https://laravel.com/docs/12.x/http-tests#verifying-json-paths)
If you would like to verify that the JSON response contains the given data at a specified path, you should use the `assertJsonPath` method:
Pest PHPUnit
```


1<?php




2 



3test('asserting a json path value', function () {




4    $response = $this->postJson('/user', ['name' => 'Sally']);




5 



6    $response




7        ->assertStatus(201)




8        ->assertJsonPath('team.owner.name', 'Darian');




9});




<?php

test('asserting a json path value', function () {
    $response = $this->postJson('/user', ['name' => 'Sally']);

    $response
        ->assertStatus(201)
        ->assertJsonPath('team.owner.name', 'Darian');
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




12    public function test_asserting_a_json_paths_value(): void




13    {




14        $response = $this->postJson('/user', ['name' => 'Sally']);




15 



16        $response




17            ->assertStatus(201)




18            ->assertJsonPath('team.owner.name', 'Darian');




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
    public function test_asserting_a_json_paths_value(): void
    {
        $response = $this->postJson('/user', ['name' => 'Sally']);

        $response
            ->assertStatus(201)
            ->assertJsonPath('team.owner.name', 'Darian');
    }
}

```

The `assertJsonPath` method also accepts a closure, which may be used to dynamically determine if the assertion should pass:
```


1$response->assertJsonPath('team.owner.name', fn (string $name) => strlen($name) >= 3);




$response->assertJsonPath('team.owner.name', fn (string $name) => strlen($name) >= 3);

```

### [Fluent JSON Testing](https://laravel.com/docs/12.x/http-tests#fluent-json-testing)
Laravel also offers a beautiful way to fluently test your application's JSON responses. To get started, pass a closure to the `assertJson` method. This closure will be invoked with an instance of `Illuminate\Testing\Fluent\AssertableJson` which can be used to make assertions against the JSON that was returned by your application. The `where` method may be used to make assertions against a particular attribute of the JSON, while the `missing` method may be used to assert that a particular attribute is missing from the JSON:
Pest PHPUnit
```


 1use Illuminate\Testing\Fluent\AssertableJson;




 2 



 3test('fluent json', function () {




 4    $response = $this->getJson('/users/1');




 5 



 6    $response




 7        ->assertJson(fn (AssertableJson $json) =>




 8            $json->where('id', 1)




 9                ->where('name', 'Victoria Faith')




10                ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))




11                ->whereNot('status', 'pending')




12                ->missing('password')




13                ->etc()




14        );




15});




use Illuminate\Testing\Fluent\AssertableJson;

test('fluent json', function () {
    $response = $this->getJson('/users/1');

    $response
        ->assertJson(fn (AssertableJson $json) =>
            $json->where('id', 1)
                ->where('name', 'Victoria Faith')
                ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))
                ->whereNot('status', 'pending')
                ->missing('password')
                ->etc()
        );
});

```

```


 1use Illuminate\Testing\Fluent\AssertableJson;




 2 



 3/**




 4 * A basic functional test example.




 5 */




 6public function test_fluent_json(): void




 7{




 8    $response = $this->getJson('/users/1');




 9 



10    $response




11        ->assertJson(fn (AssertableJson $json) =>




12            $json->where('id', 1)




13                ->where('name', 'Victoria Faith')




14                ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))




15                ->whereNot('status', 'pending')




16                ->missing('password')




17                ->etc()




18        );




19}




use Illuminate\Testing\Fluent\AssertableJson;

/**
 * A basic functional test example.
 */
public function test_fluent_json(): void
{
    $response = $this->getJson('/users/1');

    $response
        ->assertJson(fn (AssertableJson $json) =>
            $json->where('id', 1)
                ->where('name', 'Victoria Faith')
                ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))
                ->whereNot('status', 'pending')
                ->missing('password')
                ->etc()
        );
}

```

#### Understanding the `etc` Method
In the example above, you may have noticed we invoked the `etc` method at the end of our assertion chain. This method informs Laravel that there may be other attributes present on the JSON object. If the `etc` method is not used, the test will fail if other attributes that you did not make assertions against exist on the JSON object.
The intention behind this behavior is to protect you from unintentionally exposing sensitive information in your JSON responses by forcing you to either explicitly make an assertion against the attribute or explicitly allow additional attributes via the `etc` method.
However, you should be aware that not including the `etc` method in your assertion chain does not ensure that additional attributes are not being added to arrays that are nested within your JSON object. The `etc` method only ensures that no additional attributes exist at the nesting level in which the `etc` method is invoked.
#### [Asserting Attribute Presence / Absence](https://laravel.com/docs/12.x/http-tests#asserting-json-attribute-presence-and-absence)
To assert that an attribute is present or absent, you may use the `has` and `missing` methods:
```


1$response->assertJson(fn (AssertableJson $json) =>




2    $json->has('data')




3        ->missing('message')




4);




$response->assertJson(fn (AssertableJson $json) =>
    $json->has('data')
        ->missing('message')
);

```

In addition, the `hasAll` and `missingAll` methods allow asserting the presence or absence of multiple attributes simultaneously:
```


1$response->assertJson(fn (AssertableJson $json) =>




2    $json->hasAll(['status', 'data'])




3        ->missingAll(['message', 'code'])




4);




$response->assertJson(fn (AssertableJson $json) =>
    $json->hasAll(['status', 'data'])
        ->missingAll(['message', 'code'])
);

```

You may use the `hasAny` method to determine if at least one of a given list of attributes is present:
```


1$response->assertJson(fn (AssertableJson $json) =>




2    $json->has('status')




3        ->hasAny('data', 'message', 'code')




4);




$response->assertJson(fn (AssertableJson $json) =>
    $json->has('status')
        ->hasAny('data', 'message', 'code')
);

```

#### [Asserting Against JSON Collections](https://laravel.com/docs/12.x/http-tests#asserting-against-json-collections)
Often, your route will return a JSON response that contains multiple items, such as multiple users:
```


1Route::get('/users', function () {




2    return User::all();




3});




Route::get('/users', function () {
    return User::all();
});

```

In these situations, we may use the fluent JSON object's `has` method to make assertions against the users included in the response. For example, let's assert that the JSON response contains three users. Next, we'll make some assertions about the first user in the collection using the `first` method. The `first` method accepts a closure which receives another assertable JSON string that we can use to make assertions about the first object in the JSON collection:
```


 1$response




 2    ->assertJson(fn (AssertableJson $json) =>




 3        $json->has(3)




 4            ->first(fn (AssertableJson $json) =>




 5                $json->where('id', 1)




 6                    ->where('name', 'Victoria Faith')




 7                    ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))




 8                    ->missing('password')




 9                    ->etc()




10            )




11    );




$response
    ->assertJson(fn (AssertableJson $json) =>
        $json->has(3)
            ->first(fn (AssertableJson $json) =>
                $json->where('id', 1)
                    ->where('name', 'Victoria Faith')
                    ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))
                    ->missing('password')
                    ->etc()
            )
    );

```

If you would like to make the same assertions against every item in a JSON collection, you may use the `each` method:
```


 1$response




 2  ->assertJson(fn (AssertableJson $json) =>




 3      $json->has(3)




 4          ->each(fn (AssertableJson $json) =>




 5              $json->whereType('id', 'integer')




 6                  ->whereType('name', 'string')




 7                  ->whereType('email', 'string')




 8                  ->missing('password')




 9                  ->etc()




10          )




11  );




$response
  ->assertJson(fn (AssertableJson $json) =>
      $json->has(3)
          ->each(fn (AssertableJson $json) =>
              $json->whereType('id', 'integer')
                  ->whereType('name', 'string')
                  ->whereType('email', 'string')
                  ->missing('password')
                  ->etc()
          )
  );

```

#### [Scoping JSON Collection Assertions](https://laravel.com/docs/12.x/http-tests#scoping-json-collection-assertions)
Sometimes, your application's routes will return JSON collections that are assigned named keys:
```


1Route::get('/users', function () {




2    return [




3        'meta' => [...],




4        'users' => User::all(),




5    ];




6})




Route::get('/users', function () {
    return [
        'meta' => [...],
        'users' => User::all(),
    ];
})

```

When testing these routes, you may use the `has` method to assert against the number of items in the collection. In addition, you may use the `has` method to scope a chain of assertions:
```


 1$response




 2    ->assertJson(fn (AssertableJson $json) =>




 3        $json->has('meta')




 4            ->has('users', 3)




 5            ->has('users.0', fn (AssertableJson $json) =>




 6                $json->where('id', 1)




 7                    ->where('name', 'Victoria Faith')




 8                    ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))




 9                    ->missing('password')




10                    ->etc()




11            )




12    );




$response
    ->assertJson(fn (AssertableJson $json) =>
        $json->has('meta')
            ->has('users', 3)
            ->has('users.0', fn (AssertableJson $json) =>
                $json->where('id', 1)
                    ->where('name', 'Victoria Faith')
                    ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))
                    ->missing('password')
                    ->etc()
            )
    );

```

However, instead of making two separate calls to the `has` method to assert against the `users` collection, you may make a single call which provides a closure as its third parameter. When doing so, the closure will automatically be invoked and scoped to the first item in the collection:
```


 1$response




 2    ->assertJson(fn (AssertableJson $json) =>




 3        $json->has('meta')




 4            ->has('users', 3, fn (AssertableJson $json) =>




 5                $json->where('id', 1)




 6                    ->where('name', 'Victoria Faith')




 7                    ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))




 8                    ->missing('password')




 9                    ->etc()




10            )




11    );




$response
    ->assertJson(fn (AssertableJson $json) =>
        $json->has('meta')
            ->has('users', 3, fn (AssertableJson $json) =>
                $json->where('id', 1)
                    ->where('name', 'Victoria Faith')
                    ->where('email', fn (string $email) => str($email)->is('victoria@gmail.com'))
                    ->missing('password')
                    ->etc()
            )
    );

```

#### [Asserting JSON Types](https://laravel.com/docs/12.x/http-tests#asserting-json-types)
You may only want to assert that the properties in the JSON response are of a certain type. The `Illuminate\Testing\Fluent\AssertableJson` class provides the `whereType` and `whereAllType` methods for doing just that:
```


1$response->assertJson(fn (AssertableJson $json) =>




2    $json->whereType('id', 'integer')




3        ->whereAllType([




4            'users.0.name' => 'string',




5            'meta' => 'array'




6        ])




7);




$response->assertJson(fn (AssertableJson $json) =>
    $json->whereType('id', 'integer')
        ->whereAllType([
            'users.0.name' => 'string',
            'meta' => 'array'
        ])
);

```

You may specify multiple types using the `|` character, or passing an array of types as the second parameter to the `whereType` method. The assertion will be successful if the response value is any of the listed types:
```


1$response->assertJson(fn (AssertableJson $json) =>




2    $json->whereType('name', 'string|null')




3        ->whereType('id', ['string', 'integer'])




4);




$response->assertJson(fn (AssertableJson $json) =>
    $json->whereType('name', 'string|null')
        ->whereType('id', ['string', 'integer'])
);

```

The `whereType` and `whereAllType` methods recognize the following types: `string`, `integer`, `double`, `boolean`, `array`, and `null`.
