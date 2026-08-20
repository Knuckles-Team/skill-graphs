## [Working With Blade and Routes](https://laravel.com/docs/12.x/vite#working-with-blade-and-routes)
### [Processing Static Assets With Vite](https://laravel.com/docs/12.x/vite#blade-processing-static-assets)
When referencing assets in your JavaScript or CSS, Vite automatically processes and versions them. In addition, when building Blade based applications, Vite can also process and version static assets that you reference solely in Blade templates.
However, in order to accomplish this, you need to make Vite aware of your assets by importing the static assets into the application's entry point. For example, if you want to process and version all images stored in `resources/images` and all fonts stored in `resources/fonts`, you should add the following in your application's `resources/js/app.js` entry point:
```


1import.meta.glob([




2  '../images/**',




3  '../fonts/**',




4]);




import.meta.glob([
  '../images/**',
  '../fonts/**',
]);

```

These assets will now be processed by Vite when running `npm run build`. You can then reference these assets in Blade templates using the `Vite::asset` method, which will return the versioned URL for a given asset:
```


1<img src="{{ Vite::asset('resources/images/logo.png') }}">




<img src="{{ Vite::asset('resources/images/logo.png') }}">

```

### [Refreshing on Save](https://laravel.com/docs/12.x/vite#blade-refreshing-on-save)
When your application is built using traditional server-side rendering with Blade, Vite can improve your development workflow by automatically refreshing the browser when you make changes to view files in your application. To get started, you can simply specify the `refresh` option as `true`.
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel({




 7            // ...




 8            refresh: true,




 9        }),




10    ],




11});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            // ...
            refresh: true,
        }),
    ],
});

```

When the `refresh` option is `true`, saving files in the following directories will trigger the browser to perform a full page refresh while you are running `npm run dev`:
  * `app/Livewire/**`
  * `app/View/Components/**`
  * `lang/**`
  * `resources/lang/**`
  * `resources/views/**`
  * `routes/**`


Watching the `routes/**` directory is useful if you are utilizing
If these default paths do not suit your needs, you can specify your own list of paths to watch:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel({




 7            // ...




 8            refresh: ['resources/views/**'],




 9        }),




10    ],




11});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            // ...
            refresh: ['resources/views/**'],
        }),
    ],
});

```

Under the hood, the Laravel Vite plugin uses the `config` definition:
```


 1import { defineConfig } from 'vite';




 2import laravel from 'laravel-vite-plugin';




 3 



 4export default defineConfig({




 5    plugins: [




 6        laravel({




 7            // ...




 8            refresh: [{




 9                paths: ['path/to/watch/**'],




10                config: { delay: 300 }




11            }],




12        }),




13    ],




14});




import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    plugins: [
        laravel({
            // ...
            refresh: [{
                paths: ['path/to/watch/**'],
                config: { delay: 300 }
            }],
        }),
    ],
});

```

### [Aliases](https://laravel.com/docs/12.x/vite#blade-aliases)
It is common in JavaScript applications to [create aliases](https://laravel.com/docs/12.x/vite#aliases) to regularly referenced directories. But, you may also create aliases to use in Blade by using the `macro` method on the `Illuminate\Support\Facades\Vite` class. Typically, "macros" should be defined within the `boot` method of a [service provider](https://laravel.com/docs/12.x/providers):
```


1/**




2 * Bootstrap any application services.




3 */




4public function boot(): void




5{




6    Vite::macro('image', fn (string $asset) => $this->asset("resources/images/{$asset}"));




7}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Vite::macro('image', fn (string $asset) => $this->asset("resources/images/{$asset}"));
}

```

Once a macro has been defined, it can be invoked within your templates. For example, we can use the `image` macro defined above to reference an asset located at `resources/images/logo.png`:
```


1<img src="{{ Vite::image('logo.png') }}" alt="Laravel Logo">




<img src="{{ Vite::image('logo.png') }}" alt="Laravel Logo">

```
