## [Installation & Setup](https://laravel.com/docs/12.x/vite#installation)
The following documentation discusses how to manually install and configure the Laravel Vite plugin. However, Laravel's [starter kits](https://laravel.com/docs/12.x/starter-kits) already include all of this scaffolding and are the fastest way to get started with Laravel and Vite.
### [Installing Node](https://laravel.com/docs/12.x/vite#installing-node)
You must ensure that Node.js (16+) and NPM are installed before running Vite and the Laravel plugin:
```


1node -v




2npm -v




node -v
npm -v

```

You can easily install the latest version of Node and NPM using simple graphical installers from [Laravel Sail](https://laravel.com/docs/12.x/sail), you may invoke Node and NPM through Sail:
```


1./vendor/bin/sail node -v




2./vendor/bin/sail npm -v




./vendor/bin/sail node -v
./vendor/bin/sail npm -v

```

### [Installing Vite and the Laravel Plugin](https://laravel.com/docs/12.x/vite#installing-vite-and-laravel-plugin)
Within a fresh installation of Laravel, you will find a `package.json` file in the root of your application's directory structure. The default `package.json` file already includes everything you need to get started using Vite and the Laravel plugin. You may install your application's frontend dependencies via NPM:
```


1npm install




npm install

```

### [Configuring Vite](https://laravel.com/docs/12.x/vite#configuring-vite)
Vite is configured via a `vite.config.js` file in the root of your project. You are free to customize this file based on your needs, and you may also install any other plugins your application requires, such as `@vitejs/plugin-react`, `@sveltejs/vite-plugin-svelte` or `@vitejs/plugin-vue`.
The Laravel Vite plugin requires you to specify the entry points for your application. These may be JavaScript or CSS files, and include preprocessed languages such as TypeScript, JSX, TSX, and Sass.
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel([




 7            'resources/css/app.css',




 8            'resources/js/app.js',




 9        ]),




10    ],




11});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel([
            'resources/css/app.css',
            'resources/js/app.js',
        ]),
    ],
});

```

If you are building an SPA, including applications built using Inertia, Vite works best without CSS entry points:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel([




 7            'resources/css/app.css',




 8            'resources/js/app.js',




 9        ]),




10    ],




11});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel([
            'resources/css/app.css',
            'resources/js/app.js',
        ]),
    ],
});

```

Instead, you should import your CSS via JavaScript. Typically, this would be done in your application's `resources/js/app.js` file:
```


1import './bootstrap';




2import '../css/app.css';




import './bootstrap';
import '../css/app.css';

```

The Laravel plugin also supports multiple entry points and advanced configuration options such as [SSR entry points](https://laravel.com/docs/12.x/vite#ssr).
#### [Working With a Secure Development Server](https://laravel.com/docs/12.x/vite#working-with-a-secure-development-server)
If your local development web server is serving your application via HTTPS, you may run into issues connecting to the Vite development server.
If you are using [Laravel Herd](https://herd.laravel.com) and have secured the site or you are using [Laravel Valet](https://laravel.com/docs/12.x/valet) and have run the [secure command](https://laravel.com/docs/12.x/valet#securing-sites) against your application, the Laravel Vite plugin will automatically detect and use the generated TLS certificate for you.
If you secured the site using a host that does not match the application's directory name, you may manually specify the host in your application's `vite.config.js` file:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel({




 7            // ...




 8            detectTls: 'my-app.test',




 9        }),




10    ],




11});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            // ...
            detectTls: 'my-app.test',
        }),
    ],
});

```

When using another web server, you should generate a trusted certificate and manually configure Vite to use the generated certificates:
```


 1// ...




 2import fs from 'fs';




 3 



 4const host = 'my-app.test';




 5 



 6export default defineConfig({




 7    // ...




 8    server: {




 9        host,




10        hmr: { host },




11        https: {




12            key: fs.readFileSync(`/path/to/${host}.key`),




13            cert: fs.readFileSync(`/path/to/${host}.crt`),




14        },




15    },




16});




// ...
import fs from 'fs';

const host = 'my-app.test';

export default defineConfig({
    // ...
    server: {
        host,
        hmr: { host },
        https: {
            key: fs.readFileSync(`/path/to/${host}.key`),
            cert: fs.readFileSync(`/path/to/${host}.crt`),
        },
    },
});

```

If you are unable to generate a trusted certificate for your system, you may install and configure the `npm run dev` command.
#### [Running the Development Server in Sail on WSL2](https://laravel.com/docs/12.x/vite#configuring-hmr-in-sail-on-wsl2)
When running the Vite development server within [Laravel Sail](https://laravel.com/docs/12.x/sail) on Windows Subsystem for Linux 2 (WSL2), you should add the following configuration to your `vite.config.js` file to ensure the browser can communicate with the development server:
```


 1// ...




 2 



 3export default defineConfig({




 4    // ...




 5    server: {




 6        hmr: {




 7            host: 'localhost',




 8        },




 9    },




10});




// ...

export default defineConfig({
    // ...
    server: {
        hmr: {
            host: 'localhost',
        },
    },
});

```

If your file changes are not being reflected in the browser while the development server is running, you may also need to configure Vite's
### [Loading Your Scripts and Styles](https://laravel.com/docs/12.x/vite#loading-your-scripts-and-styles)
With your Vite entry points configured, you may now reference them in a `@vite()` Blade directive that you add to the `<head>` of your application's root template:
```


1<!DOCTYPE html>




2<head>




3    {{-- ... --}}




4 



5    @vite(['resources/css/app.css', 'resources/js/app.js'])




6</head>




<!DOCTYPE html>
<head>
    {{-- ... --}}

    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>

```

If you're importing your CSS via JavaScript, you only need to include the JavaScript entry point:
```


1<!DOCTYPE html>




2<head>




3    {{-- ... --}}




4 



5    @vite('resources/js/app.js')




6</head>




<!DOCTYPE html>
<head>
    {{-- ... --}}

    @vite('resources/js/app.js')
</head>

```

The `@vite` directive will automatically detect the Vite development server and inject the Vite client to enable Hot Module Replacement. In build mode, the directive will load your compiled and versioned assets, including any imported CSS.
If needed, you may also specify the build path of your compiled assets when invoking the `@vite` directive:
```


1<!doctype html>




2<head>




3    {{-- Given build path is relative to public path. --}}




4 



5    @vite('resources/js/app.js', 'vendor/courier/build')




6</head>




<!doctype html>
<head>
    {{-- Given build path is relative to public path. --}}

    @vite('resources/js/app.js', 'vendor/courier/build')
</head>

```

#### [Inline Assets](https://laravel.com/docs/12.x/vite#inline-assets)
Sometimes it may be necessary to include the raw content of assets rather than linking to the versioned URL of the asset. For example, you may need to include asset content directly into your page when passing HTML content to a PDF generator. You may output the content of Vite assets using the `content` method provided by the `Vite` facade:
```


 1@use('Illuminate\Support\Facades\Vite')




 2 



 3<!doctype html>




 4<head>




 5    {{-- ... --}}




 6 



 7    <style>




 8        {!! Vite::content('resources/css/app.css') !!}




 9    </style>




10    <script>




11        {!! Vite::content('resources/js/app.js') !!}




12    </script>




13</head>




@use('Illuminate\Support\Facades\Vite')

<!doctype html>
<head>
    {{-- ... --}}

    <style>
        {!! Vite::content('resources/css/app.css') !!}
    </style>
    <script>
        {!! Vite::content('resources/js/app.js') !!}
    </script>
</head>

```
