## [Server-Side Rendering (SSR)](https://laravel.com/docs/12.x/vite#ssr)
The Laravel Vite plugin makes it painless to set up server-side rendering with Vite. To get started, create an SSR entry point at `resources/js/ssr.js` and specify the entry point by passing a configuration option to the Laravel plugin:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel({




 7            input: 'resources/js/app.js',




 8            ssr: 'resources/js/ssr.js',




 9        }),




10    ],




11});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            input: 'resources/js/app.js',
            ssr: 'resources/js/ssr.js',
        }),
    ],
});

```

To ensure you don't forget to rebuild the SSR entry point, we recommend augmenting the "build" script in your application's `package.json` to create your SSR build:
```


1"scripts": {




2     "dev": "vite",




3     "build": "vite build"




4     "build": "vite build && vite build --ssr"




5}




"scripts": {
     "dev": "vite",
     "build": "vite build"
     "build": "vite build && vite build --ssr"
}

```

Then, to build and start the SSR server, you may run the following commands:
```


1npm run build




2node bootstrap/ssr/ssr.js




npm run build
node bootstrap/ssr/ssr.js

```

If you are using `inertia:start-ssr` Artisan command to start the SSR server:
```


1php artisan inertia:start-ssr




php artisan inertia:start-ssr

```

Laravel's [starter kits](https://laravel.com/docs/12.x/starter-kits) already include the proper Laravel, Inertia SSR, and Vite configuration.These starter kits offer the fastest way to get started with Laravel, Inertia SSR, and Vite.
