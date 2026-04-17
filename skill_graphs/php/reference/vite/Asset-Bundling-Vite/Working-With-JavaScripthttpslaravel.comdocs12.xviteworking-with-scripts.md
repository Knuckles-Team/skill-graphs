## [Working With JavaScript](https://laravel.com/docs/12.x/vite#working-with-scripts)
### [Aliases](https://laravel.com/docs/12.x/vite#aliases)
By default, The Laravel plugin provides a common alias to help you hit the ground running and conveniently import your application's assets:
```


1{




2    '@' => '/resources/js'




3}




{
    '@' => '/resources/js'
}

```

You may overwrite the `'@'` alias by adding your own to the `vite.config.js` configuration file:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel(['resources/ts/app.tsx']),




 7    ],




 8    resolve: {




 9        alias: {




10            '@': '/resources/ts',




11        },




12    },




13});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel(['resources/ts/app.tsx']),
    ],
    resolve: {
        alias: {
            '@': '/resources/ts',
        },
    },
});

```

### [Vue](https://laravel.com/docs/12.x/vite#vue)
If you would like to build your frontend using the `@vitejs/plugin-vue` plugin:
```


1npm install --save-dev @vitejs/plugin-vue




npm install --save-dev @vitejs/plugin-vue

```

You may then include the plugin in your `vite.config.js` configuration file. There are a few additional options you will need when using the Vue plugin with Laravel:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3import vue from '@vitejs/plugin-vue';




 4 



 5export default defineConfig({




 6    plugins: [




 7        laravel(['resources/js/app.js']),




 8        vue({




 9            template: {




10                transformAssetUrls: {




11                    // The Vue plugin will re-write asset URLs, when referenced




12                    // in Single File Components, to point to the Laravel web




13                    // server. Setting this to `null` allows the Laravel plugin




14                    // to instead re-write asset URLs to point to the Vite




15                    // server instead.




16                    base: null,




17 



18                    // The Vue plugin will parse absolute URLs and treat them




19                    // as absolute paths to files on disk. Setting this to




20                    // `false` will leave absolute URLs un-touched so they can




21                    // reference assets in the public directory as expected.




22                    includeAbsolute: false,




23                },




24            },




25        }),




26    ],




27});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
    plugins: [
        laravel(['resources/js/app.js']),
        vue({
            template: {
                transformAssetUrls: {
                    // The Vue plugin will re-write asset URLs, when referenced
                    // in Single File Components, to point to the Laravel web
                    // server. Setting this to `null` allows the Laravel plugin
                    // to instead re-write asset URLs to point to the Vite
                    // server instead.
                    base: null,

                    // The Vue plugin will parse absolute URLs and treat them
                    // as absolute paths to files on disk. Setting this to
                    // `false` will leave absolute URLs un-touched so they can
                    // reference assets in the public directory as expected.
                    includeAbsolute: false,
                },
            },
        }),
    ],
});

```

Laravel's [starter kits](https://laravel.com/docs/12.x/starter-kits) already include the proper Laravel, Vue, and Vite configuration.These starter kits offer the fastest way to get started with Laravel, Vue, and Vite.
### [React](https://laravel.com/docs/12.x/vite#react)
If you would like to build your frontend using the `@vitejs/plugin-react` plugin:
```


1npm install --save-dev @vitejs/plugin-react




npm install --save-dev @vitejs/plugin-react

```

You may then include the plugin in your `vite.config.js` configuration file:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3import react from '@vitejs/plugin-react';




 4 



 5export default defineConfig({




 6    plugins: [




 7        laravel(['resources/js/app.jsx']),




 8        react(),




 9    ],




10});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import react from '@vitejs/plugin-react';

export default defineConfig({
    plugins: [
        laravel(['resources/js/app.jsx']),
        react(),
    ],
});

```

You will need to ensure that any files containing JSX have a `.jsx` or `.tsx` extension, remembering to update your entry point, if required, as [shown above](https://laravel.com/docs/12.x/vite#configuring-vite).
You will also need to include the additional `@viteReactRefresh` Blade directive alongside your existing `@vite` directive.
```


1@viteReactRefresh




2@vite('resources/js/app.jsx')




@viteReactRefresh
@vite('resources/js/app.jsx')

```

The `@viteReactRefresh` directive must be called before the `@vite` directive.
Laravel's [starter kits](https://laravel.com/docs/12.x/starter-kits) already include the proper Laravel, React, and Vite configuration.These starter kits offer the fastest way to get started with Laravel, React, and Vite.
### [Svelte](https://laravel.com/docs/12.x/vite#svelte)
If you would like to build your frontend using the `@sveltejs/vite-plugin-svelte` plugin:
```


1npm install --save-dev @sveltejs/vite-plugin-svelte




npm install --save-dev @sveltejs/vite-plugin-svelte

```

You may then include the plugin in your `vite.config.js` configuration file.
```


 1import { svelte } from '@sveltejs/vite-plugin-svelte';




 2import laravel from 'laravel-vite-plugin';




 3import { defineConfig } from 'vite';




 4 



 5export default defineConfig({




 6  plugins: [




 7    laravel({




 8      input: ['resources/js/app.ts'],




 9      ssr: 'resources/js/ssr.ts',




10      refresh: true,




11    }),




12    svelte(),




13  ],




14});




import { svelte } from '@sveltejs/vite-plugin-svelte';
import laravel from 'laravel-vite-plugin';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    laravel({
      input: ['resources/js/app.ts'],
      ssr: 'resources/js/ssr.ts',
      refresh: true,
    }),
    svelte(),
  ],
});

```

Laravel's [starter kits](https://laravel.com/docs/12.x/starter-kits) already include the proper Laravel, Svelte, and Vite configuration.These starter kits offer the fastest way to get started with Laravel, Svelte, and Vite.
### [Inertia](https://laravel.com/docs/12.x/vite#inertia)
The Laravel Vite plugin provides a convenient `resolvePageComponent` function to help you resolve your Inertia page components. Below is an example of the helper in use with Vue 3; however, you may also utilize the function in other frameworks such as React or Svelte:
```


 1import { createApp, h } from 'vue';




 2import { createInertiaApp } from '@inertiajs/vue3';




 3import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers';




 4 



 5createInertiaApp({




 6  resolve: (name) => resolvePageComponent(`./Pages/${name}.vue`, import.meta.glob('./Pages/**/*.vue')),




 7  setup({ el, App, props, plugin }) {




 8    createApp({ render: () => h(App, props) })




 9      .use(plugin)




10      .mount(el)




11  },




12});




import { createApp, h } from 'vue';
import { createInertiaApp } from '@inertiajs/vue3';
import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers';

createInertiaApp({
  resolve: (name) => resolvePageComponent(`./Pages/${name}.vue`, import.meta.glob('./Pages/**/*.vue')),
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .mount(el)
  },
});

```

If you are using Vite's code splitting feature with Inertia, we recommend configuring [asset prefetching](https://laravel.com/docs/12.x/vite#asset-prefetching).
Laravel's [starter kits](https://laravel.com/docs/12.x/starter-kits) already include the proper Laravel, Inertia, and Vite configuration.These starter kits offer the fastest way to get started with Laravel, Inertia, and Vite.
### [URL Processing](https://laravel.com/docs/12.x/vite#url-processing)
When using Vite and referencing assets in your application's HTML, CSS, or JS, there are a couple of caveats to consider. First, if you reference assets with an absolute path, Vite will not include the asset in the build; therefore, you should ensure that the asset is available in your public directory. You should avoid using absolute paths when using a [dedicated CSS entrypoint](https://laravel.com/docs/12.x/vite#configuring-vite) because, during development, browsers will try to load these paths from the Vite development server, where the CSS is hosted, rather than from your public directory.
When referencing relative asset paths, you should remember that the paths are relative to the file where they are referenced. Any assets referenced via a relative path will be re-written, versioned, and bundled by Vite.
Consider the following project structure:
```


1public/




2  taylor.png




3resources/




4  js/




5    Pages/




6      Welcome.vue




7  images/




8    abigail.png




public/
  taylor.png
resources/
  js/
    Pages/
      Welcome.vue
  images/
    abigail.png

```

The following example demonstrates how Vite will treat relative and absolute URLs:
```


1<!-- This asset is not handled by Vite and will not be included in the build -->




2<img src="/taylor.png">




3 



4<!-- This asset will be re-written, versioned, and bundled by Vite -->




5<img src="../../images/abigail.png">




<!-- This asset is not handled by Vite and will not be included in the build -->
<img src="/taylor.png">

<!-- This asset will be re-written, versioned, and bundled by Vite -->
<img src="../../images/abigail.png">

```
