## [Asset Prefetching](https://laravel.com/docs/12.x/vite#asset-prefetching)
When building an SPA using Vite's code splitting feature, required assets are fetched on each page navigation. This behavior can lead to delayed UI rendering. If this is a problem for your frontend framework of choice, Laravel offers the ability to eagerly prefetch your application's JavaScript and CSS assets on initial page load.
You can instruct Laravel to eagerly prefetch your assets by invoking the `Vite::prefetch` method in the `boot` method of a [service provider](https://laravel.com/docs/12.x/providers):
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Support\Facades\Vite;




 6use Illuminate\Support\ServiceProvider;




 7 



 8class AppServiceProvider extends ServiceProvider




 9{




10    /**




11     * Register any application services.




12     */




13    public function register(): void




14    {




15        // ...




16    }




17 



18    /**




19     * Bootstrap any application services.




20     */




21    public function boot(): void




22    {




23        Vite::prefetch(concurrency: 3);




24    }




25}




<?php

namespace App\Providers;

use Illuminate\Support\Facades\Vite;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        // ...
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Vite::prefetch(concurrency: 3);
    }
}

```

In the example above, assets will be prefetched with a maximum of `3` concurrent downloads on each page load. You can modify the concurrency to suit your application's needs or specify no concurrency limit if the application should download all assets at once:
```


1/**




2 * Bootstrap any application services.




3 */




4public function boot(): void




5{




6    Vite::prefetch();




7}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Vite::prefetch();
}

```

By default, prefetching will begin when the
```


1/**




2 * Bootstrap any application services.




3 */




4public function boot(): void




5{




6    Vite::prefetch(event: 'vite:prefetch');




7}




/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Vite::prefetch(event: 'vite:prefetch');
}

```

Given the code above, prefetching will now begin when you manually dispatch the `vite:prefetch` event on the `window` object. For example, you could have prefetching begin three seconds after the page loads:
```


1<script>




2    addEventListener('load', () => setTimeout(() => {




3        dispatchEvent(new Event('vite:prefetch'))




4    }, 3000))




5</script>




<script>
    addEventListener('load', () => setTimeout(() => {
        dispatchEvent(new Event('vite:prefetch'))
    }, 3000))
</script>

```
