## [Installation](https://laravel.com/docs/12.x/dusk#installation)
To get started, you should install `laravel/dusk` Composer dependency to your project:
```


1composer require laravel/dusk --dev




composer require laravel/dusk --dev

```

If you are manually registering Dusk's service provider, you should **never** register it in your production environment, as doing so could lead to arbitrary users being able to authenticate with your application.
After installing the Dusk package, execute the `dusk:install` Artisan command. The `dusk:install` command will create a `tests/Browser` directory, an example Dusk test, and install the Chrome Driver binary for your operating system:
```


1php artisan dusk:install




php artisan dusk:install

```

Next, set the `APP_URL` environment variable in your application's `.env` file. This value should match the URL you use to access your application in a browser.
If you are using [Laravel Sail](https://laravel.com/docs/12.x/sail) to manage your local development environment, please also consult the Sail documentation on [configuring and running Dusk tests](https://laravel.com/docs/12.x/sail#laravel-dusk).
### [Managing ChromeDriver Installations](https://laravel.com/docs/12.x/dusk#managing-chromedriver-installations)
If you would like to install a different version of ChromeDriver than what is installed by Laravel Dusk via the `dusk:install` command, you may use the `dusk:chrome-driver` command:
```


 1# Install the latest version of ChromeDriver for your OS...




 2php artisan dusk:chrome-driver




 3 



 4# Install a given version of ChromeDriver for your OS...




 5php artisan dusk:chrome-driver 86




 6 



 7# Install a given version of ChromeDriver for all supported OSs...




 8php artisan dusk:chrome-driver --all




 9 



10# Install the version of ChromeDriver that matches the detected version of Chrome / Chromium for your OS...




11php artisan dusk:chrome-driver --detect




# Install the latest version of ChromeDriver for your OS...
php artisan dusk:chrome-driver

# Install a given version of ChromeDriver for your OS...
php artisan dusk:chrome-driver 86

# Install a given version of ChromeDriver for all supported OSs...
php artisan dusk:chrome-driver --all

# Install the version of ChromeDriver that matches the detected version of Chrome / Chromium for your OS...
php artisan dusk:chrome-driver --detect

```

Dusk requires the `chromedriver` binaries to be executable. If you're having problems running Dusk, you should ensure the binaries are executable using the following command: `chmod -R 0755 vendor/laravel/dusk/bin/`.
### [Using Other Browsers](https://laravel.com/docs/12.x/dusk#using-other-browsers)
By default, Dusk uses Google Chrome and a standalone
To get started, open your `tests/DuskTestCase.php` file, which is the base Dusk test case for your application. Within this file, you can remove the call to the `startChromeDriver` method. This will stop Dusk from automatically starting the ChromeDriver:
```


1/**




2 * Prepare for Dusk test execution.




3 *




4 * @beforeClass




5 */




6public static function prepare(): void




7{




8    // static::startChromeDriver();




9}




/**
 * Prepare for Dusk test execution.
 *
 * @beforeClass
 */
public static function prepare(): void
{
    // static::startChromeDriver();
}

```

Next, you may modify the `driver` method to connect to the URL and port of your choice. In addition, you may modify the "desired capabilities" that should be passed to the WebDriver:
```


 1use Facebook\WebDriver\Remote\RemoteWebDriver;




 2 



 3/**




 4 * Create the RemoteWebDriver instance.




 5 */




 6protected function driver(): RemoteWebDriver




 7{




 8    return RemoteWebDriver::create(




 9        'http://localhost:4444/wd/hub', DesiredCapabilities::phantomjs()




10    );




11}




use Facebook\WebDriver\Remote\RemoteWebDriver;

/**
 * Create the RemoteWebDriver instance.
 */
protected function driver(): RemoteWebDriver
{
    return RemoteWebDriver::create(
        'http://localhost:4444/wd/hub', DesiredCapabilities::phantomjs()
    );
}

```
