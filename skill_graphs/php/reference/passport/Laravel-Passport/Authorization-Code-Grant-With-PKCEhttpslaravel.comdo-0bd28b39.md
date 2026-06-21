## [Authorization Code Grant With PKCE](https://laravel.com/docs/12.x/passport#code-grant-pkce)
The Authorization Code grant with "Proof Key for Code Exchange" (PKCE) is a secure way to authenticate single page applications or mobile applications to access your API. This grant should be used when you can't guarantee that the client secret will be stored confidentially or in order to mitigate the threat of having the authorization code intercepted by an attacker. A combination of a "code verifier" and a "code challenge" replaces the client secret when exchanging the authorization code for an access token.
### [Creating the Client](https://laravel.com/docs/12.x/passport#creating-a-auth-pkce-grant-client)
Before your application can issue tokens via the authorization code grant with PKCE, you will need to create a PKCE-enabled client. You may do this using the `passport:client` Artisan command with the `--public` option:
```


1php artisan passport:client --public




php artisan passport:client --public

```

### [Requesting Tokens](https://laravel.com/docs/12.x/passport#requesting-auth-pkce-grant-tokens)
#### [Code Verifier and Code Challenge](https://laravel.com/docs/12.x/passport#code-verifier-code-challenge)
As this authorization grant does not provide a client secret, developers will need to generate a combination of a code verifier and a code challenge in order to request a token.
The code verifier should be a random string of between 43 and 128 characters containing letters, numbers, and `"-"`, `"."`, `"_"`, `"~"` characters, as defined in the
The code challenge should be a Base64 encoded string with URL and filename-safe characters. The trailing `'='` characters should be removed and no line breaks, whitespace, or other additional characters should be present.
```


1$encoded = base64_encode(hash('sha256', $codeVerifier, true));




2 



3$codeChallenge = strtr(rtrim($encoded, '='), '+/', '-_');




$encoded = base64_encode(hash('sha256', $codeVerifier, true));

$codeChallenge = strtr(rtrim($encoded, '='), '+/', '-_');

```

#### [Redirecting for Authorization](https://laravel.com/docs/12.x/passport#code-grant-pkce-redirecting-for-authorization)
Once a client has been created, you may use the client ID and the generated code verifier and code challenge to request an authorization code and access token from your application. First, the consuming application should make a redirect request to your application's `/oauth/authorize` route:
```


 1use Illuminate\Http\Request;




 2use Illuminate\Support\Str;




 3 



 4Route::get('/redirect', function (Request $request) {




 5    $request->session()->put('state', $state = Str::random(40));




 6 



 7    $request->session()->put(




 8        'code_verifier', $codeVerifier = Str::random(128)




 9    );




10 



11    $codeChallenge = strtr(rtrim(




12        base64_encode(hash('sha256', $codeVerifier, true))




13    , '='), '+/', '-_');




14 



15    $query = http_build_query([




16        'client_id' => 'your-client-id',




17        'redirect_uri' => 'https://third-party-app.com/callback',




18        'response_type' => 'code',




19        'scope' => 'user:read orders:create',




20        'state' => $state,




21        'code_challenge' => $codeChallenge,




22        'code_challenge_method' => 'S256',




23        // 'prompt' => '', // "none", "consent", or "login"




24    ]);




25 



26    return redirect('https://passport-app.test/oauth/authorize?'.$query);




27});




use Illuminate\Http\Request;
use Illuminate\Support\Str;

Route::get('/redirect', function (Request $request) {
    $request->session()->put('state', $state = Str::random(40));

    $request->session()->put(
        'code_verifier', $codeVerifier = Str::random(128)
    );

    $codeChallenge = strtr(rtrim(
        base64_encode(hash('sha256', $codeVerifier, true))
    , '='), '+/', '-_');

    $query = http_build_query([
        'client_id' => 'your-client-id',
        'redirect_uri' => 'https://third-party-app.com/callback',
        'response_type' => 'code',
        'scope' => 'user:read orders:create',
        'state' => $state,
        'code_challenge' => $codeChallenge,
        'code_challenge_method' => 'S256',
        // 'prompt' => '', // "none", "consent", or "login"
    ]);

    return redirect('https://passport-app.test/oauth/authorize?'.$query);
});

```

#### [Converting Authorization Codes to Access Tokens](https://laravel.com/docs/12.x/passport#code-grant-pkce-converting-authorization-codes-to-access-tokens)
If the user approves the authorization request, they will be redirected back to the consuming application. The consumer should verify the `state` parameter against the value that was stored prior to the redirect, as in the standard Authorization Code Grant.
If the state parameter matches, the consumer should issue a `POST` request to your application to request an access token. The request should include the authorization code that was issued by your application when the user approved the authorization request along with the originally generated code verifier:
```


 1use Illuminate\Http\Request;




 2use Illuminate\Support\Facades\Http;




 3 



 4Route::get('/callback', function (Request $request) {




 5    $state = $request->session()->pull('state');




 6 



 7    $codeVerifier = $request->session()->pull('code_verifier');




 8 



 9    throw_unless(




10        strlen($state) > 0 && $state === $request->state,




11        InvalidArgumentException::class




12    );




13 



14    $response = Http::asForm()->post('https://passport-app.test/oauth/token', [




15        'grant_type' => 'authorization_code',




16        'client_id' => 'your-client-id',




17        'redirect_uri' => 'https://third-party-app.com/callback',




18        'code_verifier' => $codeVerifier,




19        'code' => $request->code,




20    ]);




21 



22    return $response->json();




23});




use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

Route::get('/callback', function (Request $request) {
    $state = $request->session()->pull('state');

    $codeVerifier = $request->session()->pull('code_verifier');

    throw_unless(
        strlen($state) > 0 && $state === $request->state,
        InvalidArgumentException::class
    );

    $response = Http::asForm()->post('https://passport-app.test/oauth/token', [
        'grant_type' => 'authorization_code',
        'client_id' => 'your-client-id',
        'redirect_uri' => 'https://third-party-app.com/callback',
        'code_verifier' => $codeVerifier,
        'code' => $request->code,
    ]);

    return $response->json();
});

```
