## [Advanced Customization](https://laravel.com/docs/12.x/vite#advanced-customization)
Out of the box, Laravel's Vite plugin uses sensible conventions that should work for the majority of applications; however, sometimes you may need to customize Vite's behavior. To enable additional customization options, we offer the following methods and options which can be used in place of the `@vite` Blade directive:
```


 1<!doctype html>




 2<head>




 3    {{-- ... --}}




 4 



 5    {{




 6        Vite::useHotFile(storage_path('vite.hot')) // Customize the "hot" file...




 7            ->useBuildDirectory('bundle') // Customize the build directory...




 8            ->useManifestFilename('assets.json') // Customize the manifest filename...




 9            ->withEntryPoints(['resources/js/app.js']) // Specify the entry points...




10            ->createAssetPathsUsing(function (string $path, ?bool $secure) { // Customize the backend path generation for built assets...




11                return "https://cdn.example.com/{$path}";




12            })




13    }}




14</head>




<!doctype html>
<head>
    {{-- ... --}}

    {{
        Vite::useHotFile(storage_path('vite.hot')) // Customize the "hot" file...
            ->useBuildDirectory('bundle') // Customize the build directory...
            ->useManifestFilename('assets.json') // Customize the manifest filename...
            ->withEntryPoints(['resources/js/app.js']) // Specify the entry points...
            ->createAssetPathsUsing(function (string $path, ?bool $secure) { // Customize the backend path generation for built assets...
                return "https://cdn.example.com/{$path}";
            })
    }}
</head>

```

Within the `vite.config.js` file, you should then specify the same configuration:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel({




 7            hotFile: 'storage/vite.hot', // Customize the "hot" file...




 8            buildDirectory: 'bundle', // Customize the build directory...




 9            input: ['resources/js/app.js'], // Specify the entry points...




10        }),




11    ],




12    build: {




13      manifest: 'assets.json', // Customize the manifest filename...




14    },




15});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            hotFile: 'storage/vite.hot', // Customize the "hot" file...
            buildDirectory: 'bundle', // Customize the build directory...
            input: ['resources/js/app.js'], // Specify the entry points...
        }),
    ],
    build: {
      manifest: 'assets.json', // Customize the manifest filename...
    },
});

```

### [Dev Server Cross-Origin Resource Sharing (CORS)](https://laravel.com/docs/12.x/vite#cors)
If you are experiencing Cross-Origin Resource Sharing (CORS) issues in the browser while fetching assets from the Vite dev server, you may need to grant your custom origin access to the dev server. Vite combined with the Laravel plugin allows the following origins without any additional configuration:
  * `::1`
  * `127.0.0.1`
  * `localhost`
  * `*.test`
  * `*.localhost`
  * `APP_URL` in the project's `.env`


The easiest way to allow a custom origin for your project is to ensure that your application's `APP_URL` environment variable matches the origin you are visiting in your browser. For example, if you visiting `https://my-app.laravel`, you should update your `.env` to match:
```


1APP_URL=https://my-app.laravel




APP_URL=https://my-app.laravel

```

If you need more fine-grained control over the origins, such as supporting multiple origins, you should utilize `server.cors.origin` configuration option in the project's `vite.config.js` file:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel({




 7            input: 'resources/js/app.js',




 8            refresh: true,




 9        }),




10    ],




11    server: {




12        cors: {




13            origin: [




14                'https://backend.laravel',




15                'http://admin.laravel:8566',




16            ],




17        },




18    },




19});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            input: 'resources/js/app.js',
            refresh: true,
        }),
    ],
    server: {
        cors: {
            origin: [
                'https://backend.laravel',
                'http://admin.laravel:8566',
            ],
        },
    },
});

```

You may also include regex patterns, which can be helpful if you would like to allow all origins for a given top-level domain, such as `*.laravel`:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel({




 7            input: 'resources/js/app.js',




 8            refresh: true,




 9        }),




10    ],




11    server: {




12        cors: {




13            origin: [




14                // Supports: SCHEME://DOMAIN.laravel[:PORT]




15                /^https?:\/\/.*\.laravel(:\d+)?$/,




16            ],




17        },




18    },




19});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            input: 'resources/js/app.js',
            refresh: true,
        }),
    ],
    server: {
        cors: {
            origin: [
                // Supports: SCHEME://DOMAIN.laravel[:PORT]
                /^https?:\/\/.*\.laravel(:\d+)?$/,
            ],
        },
    },
});

```

### [Correcting Dev Server URLs](https://laravel.com/docs/12.x/vite#correcting-dev-server-urls)
Some plugins within the Vite ecosystem assume that URLs which begin with a forward-slash will always point to the Vite dev server. However, due to the nature of the Laravel integration, this is not the case.
For example, the `vite-imagetools` plugin outputs URLs like the following while Vite is serving your assets:
```


1<img src="/@imagetools/f0b2f404b13f052c604e632f2fb60381bf61a520">




<img src="/@imagetools/f0b2f404b13f052c604e632f2fb60381bf61a520">

```

The `vite-imagetools` plugin is expecting that the output URL will be intercepted by Vite and the plugin may then handle all URLs that start with `/@imagetools`. If you are using plugins that are expecting this behavior, you will need to manually correct the URLs. You can do this in your `vite.config.js` file by using the `transformOnServe` option.
In this particular example, we will prepend the dev server URL to all occurrences of `/@imagetools` within the generated code:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3import { imagetools } from 'vite-imagetools';




 4 



 5export default defineConfig({




 6    plugins: [




 7        laravel({




 8            // ...




 9            transformOnServe: (code, devServerUrl) => code.replaceAll('/@imagetools', devServerUrl+'/@imagetools'),




10        }),




11        imagetools(),




12    ],




13});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import { imagetools } from 'vite-imagetools';

export default defineConfig({
    plugins: [
        laravel({
            // ...
            transformOnServe: (code, devServerUrl) => code.replaceAll('/@imagetools', devServerUrl+'/@imagetools'),
        }),
        imagetools(),
    ],
});

```

Now, while Vite is serving Assets, it will output URLs that point to the Vite dev server:
```


1- <img src="/@imagetools/f0b2f404b13f052c604e632f2fb60381bf61a520">




2+ <img src="http://[::1]:5173/@imagetools/f0b2f404b13f052c604e632f2fb60381bf61a520">




- <img src="/@imagetools/f0b2f404b13f052c604e632f2fb60381bf61a520">
+ <img src="http://[::1]:5173/@imagetools/f0b2f404b13f052c604e632f2fb60381bf61a520">

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/vite#introduction)
  * [ Installation & Setup ](https://laravel.com/docs/12.x/vite#installation)
    * [ Installing Node ](https://laravel.com/docs/12.x/vite#installing-node)
    * [ Installing Vite and the Laravel Plugin ](https://laravel.com/docs/12.x/vite#installing-vite-and-laravel-plugin)
    * [ Configuring Vite ](https://laravel.com/docs/12.x/vite#configuring-vite)
    * [ Loading Your Scripts and Styles ](https://laravel.com/docs/12.x/vite#loading-your-scripts-and-styles)
  * [ Running Vite ](https://laravel.com/docs/12.x/vite#running-vite)
  * [ Working With JavaScript ](https://laravel.com/docs/12.x/vite#working-with-scripts)
    * [ Aliases ](https://laravel.com/docs/12.x/vite#aliases)
    * [ Vue ](https://laravel.com/docs/12.x/vite#vue)
    * [ React ](https://laravel.com/docs/12.x/vite#react)
    * [ Svelte ](https://laravel.com/docs/12.x/vite#svelte)
    * [ Inertia ](https://laravel.com/docs/12.x/vite#inertia)
    * [ URL Processing ](https://laravel.com/docs/12.x/vite#url-processing)
  * [ Working With Stylesheets ](https://laravel.com/docs/12.x/vite#working-with-stylesheets)
  * [ Working With Blade and Routes ](https://laravel.com/docs/12.x/vite#working-with-blade-and-routes)
    * [ Processing Static Assets With Vite ](https://laravel.com/docs/12.x/vite#blade-processing-static-assets)
    * [ Refreshing on Save ](https://laravel.com/docs/12.x/vite#blade-refreshing-on-save)
    * [ Aliases ](https://laravel.com/docs/12.x/vite#blade-aliases)
  * [ Asset Prefetching ](https://laravel.com/docs/12.x/vite#asset-prefetching)
  * [ Custom Base URLs ](https://laravel.com/docs/12.x/vite#custom-base-urls)
  * [ Environment Variables ](https://laravel.com/docs/12.x/vite#environment-variables)
  * [ Disabling Vite in Tests ](https://laravel.com/docs/12.x/vite#disabling-vite-in-tests)
  * [ Server-Side Rendering (SSR) ](https://laravel.com/docs/12.x/vite#ssr)
  * [ Script and Style Tag Attributes ](https://laravel.com/docs/12.x/vite#script-and-style-attributes)
    * [ Content Security Policy (CSP) Nonce ](https://laravel.com/docs/12.x/vite#content-security-policy-csp-nonce)
    * [ Subresource Integrity (SRI) ](https://laravel.com/docs/12.x/vite#subresource-integrity-sri)
    * [ Arbitrary Attributes ](https://laravel.com/docs/12.x/vite#arbitrary-attributes)
  * [ Advanced Customization ](https://laravel.com/docs/12.x/vite#advanced-customization)
    * [ Dev Server Cross-Origin Resource Sharing (CORS) ](https://laravel.com/docs/12.x/vite#cors)
    * [ Correcting Dev Server URLs ](https://laravel.com/docs/12.x/vite#correcting-dev-server-urls)


[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [ More Partners ](https://partners.laravel.com)
