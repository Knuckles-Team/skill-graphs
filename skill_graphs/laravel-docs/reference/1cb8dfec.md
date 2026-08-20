## [Script and Style Tag Attributes](https://laravel.com/docs/12.x/vite#script-and-style-attributes)
### [Content Security Policy (CSP) Nonce](https://laravel.com/docs/12.x/vite#content-security-policy-csp-nonce)
If you wish to include a `useCspNonce` method within a custom [middleware](https://laravel.com/docs/12.x/middleware):
```


 1<?php




 2 



 3namespace App\Http\Middleware;




 4 



 5use Closure;




 6use Illuminate\Http\Request;




 7use Illuminate\Support\Facades\Vite;




 8use Symfony\Component\HttpFoundation\Response;




 9 



10class AddContentSecurityPolicyHeaders




11{




12    /**




13     * Handle an incoming request.




14     *




15     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next




16     */




17    public function handle(Request $request, Closure $next): Response




18    {




19        Vite::useCspNonce();




20 



21        return $next($request)->withHeaders([




22            'Content-Security-Policy' => "script-src 'nonce-".Vite::cspNonce()."'",




23        ]);




24    }




25}




<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Vite;
use Symfony\Component\HttpFoundation\Response;

class AddContentSecurityPolicyHeaders
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        Vite::useCspNonce();

        return $next($request)->withHeaders([
            'Content-Security-Policy' => "script-src 'nonce-".Vite::cspNonce()."'",
        ]);
    }
}

```

After invoking the `useCspNonce` method, Laravel will automatically include the `nonce` attributes on all generated script and style tags.
If you need to specify the nonce elsewhere, including the [starter kits](https://laravel.com/docs/12.x/starter-kits), you may retrieve it using the `cspNonce` method:
```


1@routes(nonce: Vite::cspNonce())




@routes(nonce: Vite::cspNonce())

```

If you already have a nonce that you would like to instruct Laravel to use, you may pass the nonce to the `useCspNonce` method:
```


1Vite::useCspNonce($nonce);




Vite::useCspNonce($nonce);

```

### [Subresource Integrity (SRI)](https://laravel.com/docs/12.x/vite#subresource-integrity-sri)
If your Vite manifest includes `integrity` hashes for your assets, Laravel will automatically add the `integrity` attribute on any script and style tags it generates in order to enforce `integrity` hash in its manifest, but you may enable it by installing the
```


1npm install --save-dev vite-plugin-manifest-sri




npm install --save-dev vite-plugin-manifest-sri

```

You may then enable this plugin in your `vite.config.js` file:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3import manifestSRI from 'vite-plugin-manifest-sri';




 4 



 5export default defineConfig({




 6    plugins: [




 7        laravel({




 8            // ...




 9        }),




10        manifestSRI(),




11    ],




12});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import manifestSRI from 'vite-plugin-manifest-sri';

export default defineConfig({
    plugins: [
        laravel({
            // ...
        }),
        manifestSRI(),
    ],
});

```

If required, you may also customize the manifest key where the integrity hash can be found:
```


1use Illuminate\Support\Facades\Vite;




2 



3Vite::useIntegrityKey('custom-integrity-key');




use Illuminate\Support\Facades\Vite;

Vite::useIntegrityKey('custom-integrity-key');

```

If you would like to disable this auto-detection completely, you may pass `false` to the `useIntegrityKey` method:
```


1Vite::useIntegrityKey(false);




Vite::useIntegrityKey(false);

```

### [Arbitrary Attributes](https://laravel.com/docs/12.x/vite#arbitrary-attributes)
If you need to include additional attributes on your script and style tags, such as the `useScriptTagAttributes` and `useStyleTagAttributes` methods. Typically, this methods should be invoked from a [service provider](https://laravel.com/docs/12.x/providers):
```


 1use Illuminate\Support\Facades\Vite;




 2 



 3Vite::useScriptTagAttributes([




 4    'data-turbo-track' => 'reload', // Specify a value for the attribute...




 5    'async' => true, // Specify an attribute without a value...




 6    'integrity' => false, // Exclude an attribute that would otherwise be included...




 7]);




 8 



 9Vite::useStyleTagAttributes([




10    'data-turbo-track' => 'reload',




11]);




use Illuminate\Support\Facades\Vite;

Vite::useScriptTagAttributes([
    'data-turbo-track' => 'reload', // Specify a value for the attribute...
    'async' => true, // Specify an attribute without a value...
    'integrity' => false, // Exclude an attribute that would otherwise be included...
]);

Vite::useStyleTagAttributes([
    'data-turbo-track' => 'reload',
]);

```

If you need to conditionally add attributes, you may pass a callback that will receive the asset source path, its URL, its manifest chunk, and the entire manifest:
```


1use Illuminate\Support\Facades\Vite;




2 



3Vite::useScriptTagAttributes(fn (string $src, string $url, array|null $chunk, array|null $manifest) => [




4    'data-turbo-track' => $src === 'resources/js/app.js' ? 'reload' : false,




5]);




6 



7Vite::useStyleTagAttributes(fn (string $src, string $url, array|null $chunk, array|null $manifest) => [




8    'data-turbo-track' => $chunk && $chunk['isEntry'] ? 'reload' : false,




9]);




use Illuminate\Support\Facades\Vite;

Vite::useScriptTagAttributes(fn (string $src, string $url, array|null $chunk, array|null $manifest) => [
    'data-turbo-track' => $src === 'resources/js/app.js' ? 'reload' : false,
]);

Vite::useStyleTagAttributes(fn (string $src, string $url, array|null $chunk, array|null $manifest) => [
    'data-turbo-track' => $chunk && $chunk['isEntry'] ? 'reload' : false,
]);

```

The `$chunk` and `$manifest` arguments will be `null` while the Vite development server is running.
