## [Custom Filesystems](https://laravel.com/docs/12.x/filesystem#custom-filesystems)
Laravel's Flysystem integration provides support for several "drivers" out of the box; however, Flysystem is not limited to these and has adapters for many other storage systems. You can create a custom driver if you want to use one of these additional adapters in your Laravel application.
In order to define a custom filesystem you will need a Flysystem adapter. Let's add a community maintained Dropbox adapter to our project:
```


1composer require spatie/flysystem-dropbox




composer require spatie/flysystem-dropbox

```

Next, you can register the driver within the `boot` method of one of your application's [service providers](https://laravel.com/docs/12.x/providers). To accomplish this, you should use the `extend` method of the `Storage` facade:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Contracts\Foundation\Application;




 6use Illuminate\Filesystem\FilesystemAdapter;




 7use Illuminate\Support\Facades\Storage;




 8use Illuminate\Support\ServiceProvider;




 9use League\Flysystem\Filesystem;




10use Spatie\Dropbox\Client as DropboxClient;




11use Spatie\FlysystemDropbox\DropboxAdapter;




12 



13class AppServiceProvider extends ServiceProvider




14{




15    /**




16     * Register any application services.




17     */




18    public function register(): void




19    {




20        // ...




21    }




22 



23    /**




24     * Bootstrap any application services.




25     */




26    public function boot(): void




27    {




28        Storage::extend('dropbox', function (Application $app, array $config) {




29            $adapter = new DropboxAdapter(new DropboxClient(




30                $config['authorization_token']




31            ));




32 



33            return new FilesystemAdapter(




34                new Filesystem($adapter, $config),




35                $adapter,




36                $config




37            );




38        });




39    }




40}




<?php

namespace App\Providers;

use Illuminate\Contracts\Foundation\Application;
use Illuminate\Filesystem\FilesystemAdapter;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\ServiceProvider;
use League\Flysystem\Filesystem;
use Spatie\Dropbox\Client as DropboxClient;
use Spatie\FlysystemDropbox\DropboxAdapter;

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
        Storage::extend('dropbox', function (Application $app, array $config) {
            $adapter = new DropboxAdapter(new DropboxClient(
                $config['authorization_token']
            ));

            return new FilesystemAdapter(
                new Filesystem($adapter, $config),
                $adapter,
                $config
            );
        });
    }
}

```

The first argument of the `extend` method is the name of the driver and the second is a closure that receives the `$app` and `$config` variables. The closure must return an instance of `Illuminate\Filesystem\FilesystemAdapter`. The `$config` variable contains the values defined in `config/filesystems.php` for the specified disk.
Once you have created and registered the extension's service provider, you may use the `dropbox` driver in your `config/filesystems.php` configuration file.
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/filesystem#introduction)
  * [ Configuration ](https://laravel.com/docs/12.x/filesystem#configuration)
    * [ The Local Driver ](https://laravel.com/docs/12.x/filesystem#the-local-driver)
    * [ The Public Disk ](https://laravel.com/docs/12.x/filesystem#the-public-disk)
    * [ Driver Prerequisites ](https://laravel.com/docs/12.x/filesystem#driver-prerequisites)
    * [ Scoped and Read-Only Filesystems ](https://laravel.com/docs/12.x/filesystem#scoped-and-read-only-filesystems)
    * [ Amazon S3 Compatible Filesystems ](https://laravel.com/docs/12.x/filesystem#amazon-s3-compatible-filesystems)
  * [ Obtaining Disk Instances ](https://laravel.com/docs/12.x/filesystem#obtaining-disk-instances)
    * [ On-Demand Disks ](https://laravel.com/docs/12.x/filesystem#on-demand-disks)
  * [ Retrieving Files ](https://laravel.com/docs/12.x/filesystem#retrieving-files)
    * [ Downloading Files ](https://laravel.com/docs/12.x/filesystem#downloading-files)
    * [ File URLs ](https://laravel.com/docs/12.x/filesystem#file-urls)
    * [ Temporary URLs ](https://laravel.com/docs/12.x/filesystem#temporary-urls)
    * [ File Metadata ](https://laravel.com/docs/12.x/filesystem#file-metadata)
  * [ Storing Files ](https://laravel.com/docs/12.x/filesystem#storing-files)
    * [ Prepending and Appending To Files ](https://laravel.com/docs/12.x/filesystem#prepending-appending-to-files)
    * [ Copying and Moving Files ](https://laravel.com/docs/12.x/filesystem#copying-moving-files)
    * [ Automatic Streaming ](https://laravel.com/docs/12.x/filesystem#automatic-streaming)
    * [ File Uploads ](https://laravel.com/docs/12.x/filesystem#file-uploads)
    * [ File Visibility ](https://laravel.com/docs/12.x/filesystem#file-visibility)
  * [ Deleting Files ](https://laravel.com/docs/12.x/filesystem#deleting-files)
  * [ Directories ](https://laravel.com/docs/12.x/filesystem#directories)
  * [ Testing ](https://laravel.com/docs/12.x/filesystem#testing)
  * [ Custom Filesystems ](https://laravel.com/docs/12.x/filesystem#custom-filesystems)


[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
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
  *   * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [ More Partners ](https://partners.laravel.com)
