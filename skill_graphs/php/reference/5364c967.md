## [Available Assertions](https://laravel.com/docs/12.x/http-tests#available-assertions)
### [Response Assertions](https://laravel.com/docs/12.x/http-tests#response-assertions)
Laravel's `Illuminate\Testing\TestResponse` class provides a variety of custom assertion methods that you may utilize when testing your application. These assertions may be accessed on the response that is returned by the `json`, `get`, `post`, `put`, and `delete` test methods:
[assertAccepted](https://laravel.com/docs/12.x/http-tests#assert-accepted) [assertBadRequest](https://laravel.com/docs/12.x/http-tests#assert-bad-request) [assertClientError](https://laravel.com/docs/12.x/http-tests#assert-client-error) [assertConflict](https://laravel.com/docs/12.x/http-tests#assert-conflict) [assertCookie](https://laravel.com/docs/12.x/http-tests#assert-cookie) [assertCookieExpired](https://laravel.com/docs/12.x/http-tests#assert-cookie-expired) [assertCookieNotExpired](https://laravel.com/docs/12.x/http-tests#assert-cookie-not-expired) [assertCookieMissing](https://laravel.com/docs/12.x/http-tests#assert-cookie-missing) [assertCreated](https://laravel.com/docs/12.x/http-tests#assert-created) [assertDontSee](https://laravel.com/docs/12.x/http-tests#assert-dont-see) [assertDontSeeText](https://laravel.com/docs/12.x/http-tests#assert-dont-see-text) [assertDownload](https://laravel.com/docs/12.x/http-tests#assert-download) [assertExactJson](https://laravel.com/docs/12.x/http-tests#assert-exact-json) [assertExactJsonStructure](https://laravel.com/docs/12.x/http-tests#assert-exact-json-structure) [assertForbidden](https://laravel.com/docs/12.x/http-tests#assert-forbidden) [assertFound](https://laravel.com/docs/12.x/http-tests#assert-found) [assertGone](https://laravel.com/docs/12.x/http-tests#assert-gone) [assertHeader](https://laravel.com/docs/12.x/http-tests#assert-header) [assertHeaderContains](https://laravel.com/docs/12.x/http-tests#assert-header-contains) [assertHeaderMissing](https://laravel.com/docs/12.x/http-tests#assert-header-missing) [assertInternalServerError](https://laravel.com/docs/12.x/http-tests#assert-internal-server-error) [assertJson](https://laravel.com/docs/12.x/http-tests#assert-json) [assertJsonCount](https://laravel.com/docs/12.x/http-tests#assert-json-count) [assertJsonFragment](https://laravel.com/docs/12.x/http-tests#assert-json-fragment) [assertJsonIsArray](https://laravel.com/docs/12.x/http-tests#assert-json-is-array) [assertJsonIsObject](https://laravel.com/docs/12.x/http-tests#assert-json-is-object) [assertJsonMissing](https://laravel.com/docs/12.x/http-tests#assert-json-missing) [assertJsonMissingExact](https://laravel.com/docs/12.x/http-tests#assert-json-missing-exact) [assertJsonMissingValidationErrors](https://laravel.com/docs/12.x/http-tests#assert-json-missing-validation-errors) [assertJsonPath](https://laravel.com/docs/12.x/http-tests#assert-json-path) [assertJsonMissingPath](https://laravel.com/docs/12.x/http-tests#assert-json-missing-path) [assertJsonStructure](https://laravel.com/docs/12.x/http-tests#assert-json-structure) [assertJsonValidationErrors](https://laravel.com/docs/12.x/http-tests#assert-json-validation-errors) [assertJsonValidationErrorFor](https://laravel.com/docs/12.x/http-tests#assert-json-validation-error-for) [assertLocation](https://laravel.com/docs/12.x/http-tests#assert-location) [assertMethodNotAllowed](https://laravel.com/docs/12.x/http-tests#assert-method-not-allowed) [assertMovedPermanently](https://laravel.com/docs/12.x/http-tests#assert-moved-permanently) [assertContent](https://laravel.com/docs/12.x/http-tests#assert-content) [assertNoContent](https://laravel.com/docs/12.x/http-tests#assert-no-content) [assertStreamed](https://laravel.com/docs/12.x/http-tests#assert-streamed) [assertStreamedContent](https://laravel.com/docs/12.x/http-tests#assert-streamed-content) [assertNotFound](https://laravel.com/docs/12.x/http-tests#assert-not-found) [assertOk](https://laravel.com/docs/12.x/http-tests#assert-ok) [assertPaymentRequired](https://laravel.com/docs/12.x/http-tests#assert-payment-required) [assertPlainCookie](https://laravel.com/docs/12.x/http-tests#assert-plain-cookie) [assertRedirect](https://laravel.com/docs/12.x/http-tests#assert-redirect) [assertRedirectBack](https://laravel.com/docs/12.x/http-tests#assert-redirect-back) [assertRedirectBackWithErrors](https://laravel.com/docs/12.x/http-tests#assert-redirect-back-with-errors) [assertRedirectBackWithoutErrors](https://laravel.com/docs/12.x/http-tests#assert-redirect-back-without-errors) [assertRedirectContains](https://laravel.com/docs/12.x/http-tests#assert-redirect-contains) [assertRedirectToRoute](https://laravel.com/docs/12.x/http-tests#assert-redirect-to-route) [assertRedirectToSignedRoute](https://laravel.com/docs/12.x/http-tests#assert-redirect-to-signed-route) [assertRequestTimeout](https://laravel.com/docs/12.x/http-tests#assert-request-timeout) [assertSee](https://laravel.com/docs/12.x/http-tests#assert-see) [assertSeeInOrder](https://laravel.com/docs/12.x/http-tests#assert-see-in-order) [assertSeeText](https://laravel.com/docs/12.x/http-tests#assert-see-text) [assertSeeTextInOrder](https://laravel.com/docs/12.x/http-tests#assert-see-text-in-order) [assertServerError](https://laravel.com/docs/12.x/http-tests#assert-server-error) [assertServiceUnavailable](https://laravel.com/docs/12.x/http-tests#assert-service-unavailable) [assertSessionHas](https://laravel.com/docs/12.x/http-tests#assert-session-has) [assertSessionHasInput](https://laravel.com/docs/12.x/http-tests#assert-session-has-input) [assertSessionHasAll](https://laravel.com/docs/12.x/http-tests#assert-session-has-all) [assertSessionHasErrors](https://laravel.com/docs/12.x/http-tests#assert-session-has-errors) [assertSessionHasErrorsIn](https://laravel.com/docs/12.x/http-tests#assert-session-has-errors-in) [assertSessionHasNoErrors](https://laravel.com/docs/12.x/http-tests#assert-session-has-no-errors) [assertSessionDoesntHaveErrors](https://laravel.com/docs/12.x/http-tests#assert-session-doesnt-have-errors) [assertSessionMissing](https://laravel.com/docs/12.x/http-tests#assert-session-missing) [assertStatus](https://laravel.com/docs/12.x/http-tests#assert-status) [assertSuccessful](https://laravel.com/docs/12.x/http-tests#assert-successful) [assertTooManyRequests](https://laravel.com/docs/12.x/http-tests#assert-too-many-requests) [assertUnauthorized](https://laravel.com/docs/12.x/http-tests#assert-unauthorized) [assertUnprocessable](https://laravel.com/docs/12.x/http-tests#assert-unprocessable) [assertUnsupportedMediaType](https://laravel.com/docs/12.x/http-tests#assert-unsupported-media-type) [assertValid](https://laravel.com/docs/12.x/http-tests#assert-valid) [assertInvalid](https://laravel.com/docs/12.x/http-tests#assert-invalid) [assertViewHas](https://laravel.com/docs/12.x/http-tests#assert-view-has) [assertViewHasAll](https://laravel.com/docs/12.x/http-tests#assert-view-has-all) [assertViewIs](https://laravel.com/docs/12.x/http-tests#assert-view-is) [assertViewMissing](https://laravel.com/docs/12.x/http-tests#assert-view-missing)
#### [assertAccepted](https://laravel.com/docs/12.x/http-tests#assert-accepted)
Assert that the response has an accepted (202) HTTP status code:
```


1$response->assertAccepted();




$response->assertAccepted();

```

#### [assertBadRequest](https://laravel.com/docs/12.x/http-tests#assert-bad-request)
Assert that the response has a bad request (400) HTTP status code:
```


1$response->assertBadRequest();




$response->assertBadRequest();

```

#### [assertClientError](https://laravel.com/docs/12.x/http-tests#assert-client-error)
Assert that the response has a client error (>= 400, < 500) HTTP status code:
```


1$response->assertClientError();




$response->assertClientError();

```

#### [assertConflict](https://laravel.com/docs/12.x/http-tests#assert-conflict)
Assert that the response has a conflict (409) HTTP status code:
```


1$response->assertConflict();




$response->assertConflict();

```

#### [assertCookie](https://laravel.com/docs/12.x/http-tests#assert-cookie)
Assert that the response contains the given cookie:
```


1$response->assertCookie($cookieName, $value = null);




$response->assertCookie($cookieName, $value = null);

```

#### [assertCookieExpired](https://laravel.com/docs/12.x/http-tests#assert-cookie-expired)
Assert that the response contains the given cookie and it is expired:
```


1$response->assertCookieExpired($cookieName);




$response->assertCookieExpired($cookieName);

```

#### [assertCookieNotExpired](https://laravel.com/docs/12.x/http-tests#assert-cookie-not-expired)
Assert that the response contains the given cookie and it is not expired:
```


1$response->assertCookieNotExpired($cookieName);




$response->assertCookieNotExpired($cookieName);

```

#### [assertCookieMissing](https://laravel.com/docs/12.x/http-tests#assert-cookie-missing)
Assert that the response does not contain the given cookie:
```


1$response->assertCookieMissing($cookieName);




$response->assertCookieMissing($cookieName);

```

#### [assertCreated](https://laravel.com/docs/12.x/http-tests#assert-created)
Assert that the response has a 201 HTTP status code:
```


1$response->assertCreated();




$response->assertCreated();

```

#### [assertDontSee](https://laravel.com/docs/12.x/http-tests#assert-dont-see)
Assert that the given string is not contained within the response returned by the application. This assertion will automatically escape the given string unless you pass a second argument of `false`:
```


1$response->assertDontSee($value, $escape = true);




$response->assertDontSee($value, $escape = true);

```

#### [assertDontSeeText](https://laravel.com/docs/12.x/http-tests#assert-dont-see-text)
Assert that the given string is not contained within the response text. This assertion will automatically escape the given string unless you pass a second argument of `false`. This method will pass the response content to the `strip_tags` PHP function before making the assertion:
```


1$response->assertDontSeeText($value, $escape = true);




$response->assertDontSeeText($value, $escape = true);

```

#### [assertDownload](https://laravel.com/docs/12.x/http-tests#assert-download)
Assert that the response is a "download". Typically, this means the invoked route that returned the response returned a `Response::download` response, `BinaryFileResponse`, or `Storage::download` response:
```


1$response->assertDownload();




$response->assertDownload();

```

If you wish, you may assert that the downloadable file was assigned a given file name:
```


1$response->assertDownload('image.jpg');




$response->assertDownload('image.jpg');

```

#### [assertExactJson](https://laravel.com/docs/12.x/http-tests#assert-exact-json)
Assert that the response contains an exact match of the given JSON data:
```


1$response->assertExactJson(array $data);




$response->assertExactJson(array $data);

```

#### [assertExactJsonStructure](https://laravel.com/docs/12.x/http-tests#assert-exact-json-structure)
Assert that the response contains an exact match of the given JSON structure:
```


1$response->assertExactJsonStructure(array $data);




$response->assertExactJsonStructure(array $data);

```

This method is a more strict variant of [assertJsonStructure](https://laravel.com/docs/12.x/http-tests#assert-json-structure). In contrast with `assertJsonStructure`, this method will fail if the response contains any keys that aren't explicitly included in the expected JSON structure.
#### [assertForbidden](https://laravel.com/docs/12.x/http-tests#assert-forbidden)
Assert that the response has a forbidden (403) HTTP status code:
```


1$response->assertForbidden();




$response->assertForbidden();

```

#### [assertFound](https://laravel.com/docs/12.x/http-tests#assert-found)
Assert that the response has a found (302) HTTP status code:
```


1$response->assertFound();




$response->assertFound();

```

#### [assertGone](https://laravel.com/docs/12.x/http-tests#assert-gone)
Assert that the response has a gone (410) HTTP status code:
```


1$response->assertGone();




$response->assertGone();

```

#### [assertHeader](https://laravel.com/docs/12.x/http-tests#assert-header)
Assert that the given header and value is present on the response:
```


1$response->assertHeader($headerName, $value = null);




$response->assertHeader($headerName, $value = null);

```

#### [assertHeaderContains](https://laravel.com/docs/12.x/http-tests#assert-header-contains)
Assert that the given header contains a given substring value:
```


1$response->assertHeaderContains($headerName, $value);




$response->assertHeaderContains($headerName, $value);

```

#### [assertHeaderMissing](https://laravel.com/docs/12.x/http-tests#assert-header-missing)
Assert that the given header is not present on the response:
```


1$response->assertHeaderMissing($headerName);




$response->assertHeaderMissing($headerName);

```

#### [assertInternalServerError](https://laravel.com/docs/12.x/http-tests#assert-internal-server-error)
Assert that the response has an "Internal Server Error" (500) HTTP status code:
```


1$response->assertInternalServerError();




$response->assertInternalServerError();

```

#### [assertJson](https://laravel.com/docs/12.x/http-tests#assert-json)
Assert that the response contains the given JSON data:
```


1$response->assertJson(array $data, $strict = false);




$response->assertJson(array $data, $strict = false);

```

The `assertJson` method converts the response to an array to verify that the given array exists within the JSON response returned by the application. So, if there are other properties in the JSON response, this test will still pass as long as the given fragment is present.
#### [assertJsonCount](https://laravel.com/docs/12.x/http-tests#assert-json-count)
Assert that the response JSON has an array with the expected number of items at the given key:
```


1$response->assertJsonCount($count, $key = null);




$response->assertJsonCount($count, $key = null);

```

#### [assertJsonFragment](https://laravel.com/docs/12.x/http-tests#assert-json-fragment)
Assert that the response contains the given JSON data anywhere in the response:
```


 1Route::get('/users', function () {




 2    return [




 3        'users' => [




 4            [




 5                'name' => 'Taylor Otwell',




 6            ],




 7        ],




 8    ];




 9});




10 



11$response->assertJsonFragment(['name' => 'Taylor Otwell']);




Route::get('/users', function () {
    return [
        'users' => [
            [
                'name' => 'Taylor Otwell',
            ],
        ],
    ];
});

$response->assertJsonFragment(['name' => 'Taylor Otwell']);

```

#### [assertJsonIsArray](https://laravel.com/docs/12.x/http-tests#assert-json-is-array)
Assert that the response JSON is an array:
```


1$response->assertJsonIsArray();




$response->assertJsonIsArray();

```

#### [assertJsonIsObject](https://laravel.com/docs/12.x/http-tests#assert-json-is-object)
Assert that the response JSON is an object:
```


1$response->assertJsonIsObject();




$response->assertJsonIsObject();

```

#### [assertJsonMissing](https://laravel.com/docs/12.x/http-tests#assert-json-missing)
Assert that the response does not contain the given JSON data:
```


1$response->assertJsonMissing(array $data);




$response->assertJsonMissing(array $data);

```

#### [assertJsonMissingExact](https://laravel.com/docs/12.x/http-tests#assert-json-missing-exact)
Assert that the response does not contain the exact JSON data:
```


1$response->assertJsonMissingExact(array $data);




$response->assertJsonMissingExact(array $data);

```

#### [assertJsonMissingValidationErrors](https://laravel.com/docs/12.x/http-tests#assert-json-missing-validation-errors)
Assert that the response has no JSON validation errors for the given keys:
```


1$response->assertJsonMissingValidationErrors($keys);




$response->assertJsonMissingValidationErrors($keys);

```

The more generic [assertValid](https://laravel.com/docs/12.x/http-tests#assert-valid) method may be used to assert that a response does not have validation errors that were returned as JSON **and** that no errors were flashed to session storage.
#### [assertJsonPath](https://laravel.com/docs/12.x/http-tests#assert-json-path)
Assert that the response contains the given data at the specified path:
```


1$response->assertJsonPath($path, $expectedValue);




$response->assertJsonPath($path, $expectedValue);

```

For example, if the following JSON response is returned by your application:
```


1{




2    "user": {




3        "name": "Steve Schoger"




4    }




5}




{
    "user": {
        "name": "Steve Schoger"
    }
}

```

You may assert that the `name` property of the `user` object matches a given value like so:
```


1$response->assertJsonPath('user.name', 'Steve Schoger');




$response->assertJsonPath('user.name', 'Steve Schoger');

```

#### [assertJsonMissingPath](https://laravel.com/docs/12.x/http-tests#assert-json-missing-path)
Assert that the response does not contain the given path:
```


1$response->assertJsonMissingPath($path);




$response->assertJsonMissingPath($path);

```

For example, if the following JSON response is returned by your application:
```


1{




2    "user": {




3        "name": "Steve Schoger"




4    }




5}




{
    "user": {
        "name": "Steve Schoger"
    }
}

```

You may assert that it does not contain the `email` property of the `user` object:
```


1$response->assertJsonMissingPath('user.email');




$response->assertJsonMissingPath('user.email');

```

#### [assertJsonStructure](https://laravel.com/docs/12.x/http-tests#assert-json-structure)
Assert that the response has a given JSON structure:
```


1$response->assertJsonStructure(array $structure);




$response->assertJsonStructure(array $structure);

```

For example, if the JSON response returned by your application contains the following data:
```


1{




2    "user": {




3        "name": "Steve Schoger"




4    }




5}




{
    "user": {
        "name": "Steve Schoger"
    }
}

```

You may assert that the JSON structure matches your expectations like so:
```


1$response->assertJsonStructure([




2    'user' => [




3        'name',




4    ]




5]);




$response->assertJsonStructure([
    'user' => [
        'name',
    ]
]);

```

Sometimes, JSON responses returned by your application may contain arrays of objects:
```


 1{




 2    "user": [




 3        {




 4            "name": "Steve Schoger",




 5            "age": 55,




 6            "location": "Earth"




 7        },




 8        {




 9            "name": "Mary Schoger",




10            "age": 60,




11            "location": "Earth"




12        }




13    ]




14}




{
    "user": [
        {
            "name": "Steve Schoger",
            "age": 55,
            "location": "Earth"
        },
        {
            "name": "Mary Schoger",
            "age": 60,
            "location": "Earth"
        }
    ]
}

```

In this situation, you may use the `*` character to assert against the structure of all of the objects in the array:
```


1$response->assertJsonStructure([




2    'user' => [




3        '*' => [




4             'name',




5             'age',




6             'location'




7        ]




8    ]




9]);




$response->assertJsonStructure([
    'user' => [
        '*' => [
             'name',
             'age',
             'location'
        ]
    ]
]);

```

#### [assertJsonValidationErrors](https://laravel.com/docs/12.x/http-tests#assert-json-validation-errors)
Assert that the response has the given JSON validation errors for the given keys. This method should be used when asserting against responses where the validation errors are returned as a JSON structure instead of being flashed to the session:
```


1$response->assertJsonValidationErrors(array $data, $responseKey = 'errors');




$response->assertJsonValidationErrors(array $data, $responseKey = 'errors');

```

The more generic [assertInvalid](https://laravel.com/docs/12.x/http-tests#assert-invalid) method may be used to assert that a response has validation errors returned as JSON **or** that errors were flashed to session storage.
#### [assertJsonValidationErrorFor](https://laravel.com/docs/12.x/http-tests#assert-json-validation-error-for)
Assert the response has any JSON validation errors for the given key:
```


1$response->assertJsonValidationErrorFor(string $key, $responseKey = 'errors');




$response->assertJsonValidationErrorFor(string $key, $responseKey = 'errors');

```

#### [assertMethodNotAllowed](https://laravel.com/docs/12.x/http-tests#assert-method-not-allowed)
Assert that the response has a method not allowed (405) HTTP status code:
```


1$response->assertMethodNotAllowed();




$response->assertMethodNotAllowed();

```

#### [assertMovedPermanently](https://laravel.com/docs/12.x/http-tests#assert-moved-permanently)
Assert that the response has a moved permanently (301) HTTP status code:
```


1$response->assertMovedPermanently();




$response->assertMovedPermanently();

```

#### [assertLocation](https://laravel.com/docs/12.x/http-tests#assert-location)
Assert that the response has the given URI value in the `Location` header:
```


1$response->assertLocation($uri);




$response->assertLocation($uri);

```

#### [assertContent](https://laravel.com/docs/12.x/http-tests#assert-content)
Assert that the given string matches the response content:
```


1$response->assertContent($value);




$response->assertContent($value);

```

#### [assertNoContent](https://laravel.com/docs/12.x/http-tests#assert-no-content)
Assert that the response has the given HTTP status code and no content:
```


1$response->assertNoContent($status = 204);




$response->assertNoContent($status = 204);

```

#### [assertStreamed](https://laravel.com/docs/12.x/http-tests#assert-streamed)
Assert that the response was a streamed response:
```


1$response->assertStreamed();




$response->assertStreamed();

```

#### [assertStreamedContent](https://laravel.com/docs/12.x/http-tests#assert-streamed-content)
Assert that the given string matches the streamed response content:
```


1$response->assertStreamedContent($value);




$response->assertStreamedContent($value);

```

#### [assertNotFound](https://laravel.com/docs/12.x/http-tests#assert-not-found)
Assert that the response has a not found (404) HTTP status code:
```


1$response->assertNotFound();




$response->assertNotFound();

```

#### [assertOk](https://laravel.com/docs/12.x/http-tests#assert-ok)
Assert that the response has a 200 HTTP status code:
```


1$response->assertOk();




$response->assertOk();

```

#### [assertPaymentRequired](https://laravel.com/docs/12.x/http-tests#assert-payment-required)
Assert that the response has a payment required (402) HTTP status code:
```


1$response->assertPaymentRequired();




$response->assertPaymentRequired();

```

#### [assertPlainCookie](https://laravel.com/docs/12.x/http-tests#assert-plain-cookie)
Assert that the response contains the given unencrypted cookie:
```


1$response->assertPlainCookie($cookieName, $value = null);




$response->assertPlainCookie($cookieName, $value = null);

```

#### [assertRedirect](https://laravel.com/docs/12.x/http-tests#assert-redirect)
Assert that the response is a redirect to the given URI:
```


1$response->assertRedirect($uri = null);




$response->assertRedirect($uri = null);

```

#### [assertRedirectBack](https://laravel.com/docs/12.x/http-tests#assert-redirect-back)
Assert whether the response is redirecting back to the previous page:
```


1$response->assertRedirectBack();




$response->assertRedirectBack();

```

#### [assertRedirectBackWithErrors](https://laravel.com/docs/12.x/http-tests#assert-redirect-back-with-errors)
Assert whether the response is redirecting back to the previous page and the [session has the given errors](https://laravel.com/docs/12.x/http-tests#assert-session-has-errors):
```


1$response->assertRedirectBackWithErrors(




2    array $keys = [], $format = null, $errorBag = 'default'




3);




$response->assertRedirectBackWithErrors(
    array $keys = [], $format = null, $errorBag = 'default'
);

```

#### [assertRedirectBackWithoutErrors](https://laravel.com/docs/12.x/http-tests#assert-redirect-back-without-errors)
Assert whether the response is redirecting back to the previous page and the session does not contain any error messages:
```


1$response->assertRedirectBackWithoutErrors();




$response->assertRedirectBackWithoutErrors();

```

#### [assertRedirectContains](https://laravel.com/docs/12.x/http-tests#assert-redirect-contains)
Assert whether the response is redirecting to a URI that contains the given string:
```


1$response->assertRedirectContains($string);




$response->assertRedirectContains($string);

```

#### [assertRedirectToRoute](https://laravel.com/docs/12.x/http-tests#assert-redirect-to-route)
Assert that the response is a redirect to the given [named route](https://laravel.com/docs/12.x/routing#named-routes):
```


1$response->assertRedirectToRoute($name, $parameters = []);




$response->assertRedirectToRoute($name, $parameters = []);

```

#### [assertRedirectToSignedRoute](https://laravel.com/docs/12.x/http-tests#assert-redirect-to-signed-route)
Assert that the response is a redirect to the given [signed route](https://laravel.com/docs/12.x/urls#signed-urls):
```


1$response->assertRedirectToSignedRoute($name = null, $parameters = []);




$response->assertRedirectToSignedRoute($name = null, $parameters = []);

```

#### [assertRequestTimeout](https://laravel.com/docs/12.x/http-tests#assert-request-timeout)
Assert that the response has a request timeout (408) HTTP status code:
```


1$response->assertRequestTimeout();




$response->assertRequestTimeout();

```

#### [assertSee](https://laravel.com/docs/12.x/http-tests#assert-see)
Assert that the given string is contained within the response. This assertion will automatically escape the given string unless you pass a second argument of `false`:
```


1$response->assertSee($value, $escape = true);




$response->assertSee($value, $escape = true);

```

#### [assertSeeInOrder](https://laravel.com/docs/12.x/http-tests#assert-see-in-order)
Assert that the given strings are contained in order within the response. This assertion will automatically escape the given strings unless you pass a second argument of `false`:
```


1$response->assertSeeInOrder(array $values, $escape = true);




$response->assertSeeInOrder(array $values, $escape = true);

```

#### [assertSeeText](https://laravel.com/docs/12.x/http-tests#assert-see-text)
Assert that the given string is contained within the response text. This assertion will automatically escape the given string unless you pass a second argument of `false`. The response content will be passed to the `strip_tags` PHP function before the assertion is made:
```


1$response->assertSeeText($value, $escape = true);




$response->assertSeeText($value, $escape = true);

```

#### [assertSeeTextInOrder](https://laravel.com/docs/12.x/http-tests#assert-see-text-in-order)
Assert that the given strings are contained in order within the response text. This assertion will automatically escape the given strings unless you pass a second argument of `false`. The response content will be passed to the `strip_tags` PHP function before the assertion is made:
```


1$response->assertSeeTextInOrder(array $values, $escape = true);




$response->assertSeeTextInOrder(array $values, $escape = true);

```

#### [assertServerError](https://laravel.com/docs/12.x/http-tests#assert-server-error)
Assert that the response has a server error (>= 500 , < 600) HTTP status code:
```


1$response->assertServerError();




$response->assertServerError();

```

#### [assertServiceUnavailable](https://laravel.com/docs/12.x/http-tests#assert-service-unavailable)
Assert that the response has a "Service Unavailable" (503) HTTP status code:
```


1$response->assertServiceUnavailable();




$response->assertServiceUnavailable();

```

#### [assertSessionHas](https://laravel.com/docs/12.x/http-tests#assert-session-has)
Assert that the session contains the given piece of data:
```


1$response->assertSessionHas($key, $value = null);




$response->assertSessionHas($key, $value = null);

```

If needed, a closure can be provided as the second argument to the `assertSessionHas` method. The assertion will pass if the closure returns `true`:
```


1$response->assertSessionHas($key, function (User $value) {




2    return $value->name === 'Taylor Otwell';




3});




$response->assertSessionHas($key, function (User $value) {
    return $value->name === 'Taylor Otwell';
});

```

#### [assertSessionHasInput](https://laravel.com/docs/12.x/http-tests#assert-session-has-input)
Assert that the session has a given value in the [flashed input array](https://laravel.com/docs/12.x/responses#redirecting-with-flashed-session-data):
```


1$response->assertSessionHasInput($key, $value = null);




$response->assertSessionHasInput($key, $value = null);

```

If needed, a closure can be provided as the second argument to the `assertSessionHasInput` method. The assertion will pass if the closure returns `true`:
```


1use Illuminate\Support\Facades\Crypt;




2 



3$response->assertSessionHasInput($key, function (string $value) {




4    return Crypt::decryptString($value) === 'secret';




5});




use Illuminate\Support\Facades\Crypt;

$response->assertSessionHasInput($key, function (string $value) {
    return Crypt::decryptString($value) === 'secret';
});

```

#### [assertSessionHasAll](https://laravel.com/docs/12.x/http-tests#assert-session-has-all)
Assert that the session contains a given array of key / value pairs:
```


1$response->assertSessionHasAll(array $data);




$response->assertSessionHasAll(array $data);

```

For example, if your application's session contains `name` and `status` keys, you may assert that both exist and have the specified values like so:
```


1$response->assertSessionHasAll([




2    'name' => 'Taylor Otwell',




3    'status' => 'active',




4]);




$response->assertSessionHasAll([
    'name' => 'Taylor Otwell',
    'status' => 'active',
]);

```

#### [assertSessionHasErrors](https://laravel.com/docs/12.x/http-tests#assert-session-has-errors)
Assert that the session contains an error for the given `$keys`. If `$keys` is an associative array, assert that the session contains a specific error message (value) for each field (key). This method should be used when testing routes that flash validation errors to the session instead of returning them as a JSON structure:
```


1$response->assertSessionHasErrors(




2    array $keys = [], $format = null, $errorBag = 'default'




3);




$response->assertSessionHasErrors(
    array $keys = [], $format = null, $errorBag = 'default'
);

```

For example, to assert that the `name` and `email` fields have validation error messages that were flashed to the session, you may invoke the `assertSessionHasErrors` method like so:
```


1$response->assertSessionHasErrors(['name', 'email']);




$response->assertSessionHasErrors(['name', 'email']);

```

Or, you may assert that a given field has a particular validation error message:
```


1$response->assertSessionHasErrors([




2    'name' => 'The given name was invalid.'




3]);




$response->assertSessionHasErrors([
    'name' => 'The given name was invalid.'
]);

```

The more generic [assertInvalid](https://laravel.com/docs/12.x/http-tests#assert-invalid) method may be used to assert that a response has validation errors returned as JSON **or** that errors were flashed to session storage.
#### [assertSessionHasErrorsIn](https://laravel.com/docs/12.x/http-tests#assert-session-has-errors-in)
Assert that the session contains an error for the given `$keys` within a specific [error bag](https://laravel.com/docs/12.x/validation#named-error-bags). If `$keys` is an associative array, assert that the session contains a specific error message (value) for each field (key), within the error bag:
```


1$response->assertSessionHasErrorsIn($errorBag, $keys = [], $format = null);




$response->assertSessionHasErrorsIn($errorBag, $keys = [], $format = null);

```

#### [assertSessionHasNoErrors](https://laravel.com/docs/12.x/http-tests#assert-session-has-no-errors)
Assert that the session has no validation errors:
```


1$response->assertSessionHasNoErrors();




$response->assertSessionHasNoErrors();

```

#### [assertSessionDoesntHaveErrors](https://laravel.com/docs/12.x/http-tests#assert-session-doesnt-have-errors)
Assert that the session has no validation errors for the given keys:
```


1$response->assertSessionDoesntHaveErrors($keys = [], $format = null, $errorBag = 'default');




$response->assertSessionDoesntHaveErrors($keys = [], $format = null, $errorBag = 'default');

```

The more generic [assertValid](https://laravel.com/docs/12.x/http-tests#assert-valid) method may be used to assert that a response does not have validation errors that were returned as JSON **and** that no errors were flashed to session storage.
#### [assertSessionMissing](https://laravel.com/docs/12.x/http-tests#assert-session-missing)
Assert that the session does not contain the given key:
```


1$response->assertSessionMissing($key);




$response->assertSessionMissing($key);

```

#### [assertStatus](https://laravel.com/docs/12.x/http-tests#assert-status)
Assert that the response has a given HTTP status code:
```


1$response->assertStatus($code);




$response->assertStatus($code);

```

#### [assertSuccessful](https://laravel.com/docs/12.x/http-tests#assert-successful)
Assert that the response has a successful (>= 200 and < 300) HTTP status code:
```


1$response->assertSuccessful();




$response->assertSuccessful();

```

#### [assertTooManyRequests](https://laravel.com/docs/12.x/http-tests#assert-too-many-requests)
Assert that the response has a too many requests (429) HTTP status code:
```


1$response->assertTooManyRequests();




$response->assertTooManyRequests();

```

#### [assertUnauthorized](https://laravel.com/docs/12.x/http-tests#assert-unauthorized)
Assert that the response has an unauthorized (401) HTTP status code:
```


1$response->assertUnauthorized();




$response->assertUnauthorized();

```

#### [assertUnprocessable](https://laravel.com/docs/12.x/http-tests#assert-unprocessable)
Assert that the response has an unprocessable entity (422) HTTP status code:
```


1$response->assertUnprocessable();




$response->assertUnprocessable();

```

#### [assertUnsupportedMediaType](https://laravel.com/docs/12.x/http-tests#assert-unsupported-media-type)
Assert that the response has an unsupported media type (415) HTTP status code:
```


1$response->assertUnsupportedMediaType();




$response->assertUnsupportedMediaType();

```

#### [assertValid](https://laravel.com/docs/12.x/http-tests#assert-valid)
Assert that the response has no validation errors for the given keys. This method may be used for asserting against responses where the validation errors are returned as a JSON structure or where the validation errors have been flashed to the session:
```


1// Assert that no validation errors are present...




2$response->assertValid();




3 



4// Assert that the given keys do not have validation errors...




5$response->assertValid(['name', 'email']);




// Assert that no validation errors are present...
$response->assertValid();

// Assert that the given keys do not have validation errors...
$response->assertValid(['name', 'email']);

```

#### [assertInvalid](https://laravel.com/docs/12.x/http-tests#assert-invalid)
Assert that the response has validation errors for the given keys. This method may be used for asserting against responses where the validation errors are returned as a JSON structure or where the validation errors have been flashed to the session:
```


1$response->assertInvalid(['name', 'email']);




$response->assertInvalid(['name', 'email']);

```

You may also assert that a given key has a particular validation error message. When doing so, you may provide the entire message or only a small portion of the message:
```


1$response->assertInvalid([




2    'name' => 'The name field is required.',




3    'email' => 'valid email address',




4]);




$response->assertInvalid([
    'name' => 'The name field is required.',
    'email' => 'valid email address',
]);

```

If you would like to assert that the given fields are the only fields with validation errors, you may use the `assertOnlyInvalid` method:
```


1$response->assertOnlyInvalid(['name', 'email']);




$response->assertOnlyInvalid(['name', 'email']);

```

#### [assertViewHas](https://laravel.com/docs/12.x/http-tests#assert-view-has)
Assert that the response view contains a given piece of data:
```


1$response->assertViewHas($key, $value = null);




$response->assertViewHas($key, $value = null);

```

Passing a closure as the second argument to the `assertViewHas` method will allow you to inspect and make assertions against a particular piece of view data:
```


1$response->assertViewHas('user', function (User $user) {




2    return $user->name === 'Taylor';




3});




$response->assertViewHas('user', function (User $user) {
    return $user->name === 'Taylor';
});

```

In addition, view data may be accessed as array variables on the response, allowing you to conveniently inspect it:
Pest PHPUnit
```


1expect($response['name'])->toBe('Taylor');




expect($response['name'])->toBe('Taylor');

```

```


1$this->assertEquals('Taylor', $response['name']);




$this->assertEquals('Taylor', $response['name']);

```

#### [assertViewHasAll](https://laravel.com/docs/12.x/http-tests#assert-view-has-all)
Assert that the response view has a given list of data:
```


1$response->assertViewHasAll(array $data);




$response->assertViewHasAll(array $data);

```

This method may be used to assert that the view simply contains data matching the given keys:
```


1$response->assertViewHasAll([




2    'name',




3    'email',




4]);




$response->assertViewHasAll([
    'name',
    'email',
]);

```

Or, you may assert that the view data is present and has specific values:
```


1$response->assertViewHasAll([




2    'name' => 'Taylor Otwell',




3    'email' => 'taylor@example.com,',




4]);




$response->assertViewHasAll([
    'name' => 'Taylor Otwell',
    'email' => 'taylor@example.com,',
]);

```

#### [assertViewIs](https://laravel.com/docs/12.x/http-tests#assert-view-is)
Assert that the given view was returned by the route:
```


1$response->assertViewIs($value);




$response->assertViewIs($value);

```

#### [assertViewMissing](https://laravel.com/docs/12.x/http-tests#assert-view-missing)
Assert that the given data key was not made available to the view returned in the application's response:
```


1$response->assertViewMissing($key);




$response->assertViewMissing($key);

```

### [Authentication Assertions](https://laravel.com/docs/12.x/http-tests#authentication-assertions)
Laravel also provides a variety of authentication related assertions that you may utilize within your application's feature tests. Note that these methods are invoked on the test class itself and not the `Illuminate\Testing\TestResponse` instance returned by methods such as `get` and `post`.
#### [assertAuthenticated](https://laravel.com/docs/12.x/http-tests#assert-authenticated)
Assert that a user is authenticated:
```


1$this->assertAuthenticated($guard = null);




$this->assertAuthenticated($guard = null);

```

#### [assertGuest](https://laravel.com/docs/12.x/http-tests#assert-guest)
Assert that a user is not authenticated:
```


1$this->assertGuest($guard = null);




$this->assertGuest($guard = null);

```

#### [assertAuthenticatedAs](https://laravel.com/docs/12.x/http-tests#assert-authenticated-as)
Assert that a specific user is authenticated:
```


1$this->assertAuthenticatedAs($user, $guard = null);




$this->assertAuthenticatedAs($user, $guard = null);

```
