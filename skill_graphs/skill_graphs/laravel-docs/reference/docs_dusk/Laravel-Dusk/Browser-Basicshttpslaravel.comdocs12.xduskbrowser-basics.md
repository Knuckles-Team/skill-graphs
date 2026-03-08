## [Browser Basics](https://laravel.com/docs/12.x/dusk#browser-basics)
### [Creating Browsers](https://laravel.com/docs/12.x/dusk#creating-browsers)
To get started, let's write a test that verifies we can log into our application. After generating a test, we can modify it to navigate to the login page, enter some credentials, and click the "Login" button. To create a browser instance, you may call the `browse` method from within your Dusk test:
Pest PHPUnit
```


 1<?php




 2 



 3use App\Models\User;




 4use Illuminate\Foundation\Testing\DatabaseMigrations;




 5use Laravel\Dusk\Browser;




 6 



 7pest()->use(DatabaseMigrations::class);




 8 



 9test('basic example', function () {




10    $user = User::factory()->create([




11        'email' => 'taylor@laravel.com',




12    ]);




13 



14    $this->browse(function (Browser $browser) use ($user) {




15        $browser->visit('/login')




16            ->type('email', $user->email)




17            ->type('password', 'password')




18            ->press('Login')




19            ->assertPathIs('/home');




20    });




21});




<?php

use App\Models\User;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Laravel\Dusk\Browser;

pest()->use(DatabaseMigrations::class);

test('basic example', function () {
    $user = User::factory()->create([
        'email' => 'taylor@laravel.com',
    ]);

    $this->browse(function (Browser $browser) use ($user) {
        $browser->visit('/login')
            ->type('email', $user->email)
            ->type('password', 'password')
            ->press('Login')
            ->assertPathIs('/home');
    });
});

```

```


 1<?php




 2 



 3namespace Tests\Browser;




 4 



 5use App\Models\User;




 6use Illuminate\Foundation\Testing\DatabaseMigrations;




 7use Laravel\Dusk\Browser;




 8use Tests\DuskTestCase;




 9 



10class ExampleTest extends DuskTestCase




11{




12    use DatabaseMigrations;




13 



14    /**




15     * A basic browser test example.




16     */




17    public function test_basic_example(): void




18    {




19        $user = User::factory()->create([




20            'email' => 'taylor@laravel.com',




21        ]);




22 



23        $this->browse(function (Browser $browser) use ($user) {




24            $browser->visit('/login')




25                ->type('email', $user->email)




26                ->type('password', 'password')




27                ->press('Login')




28                ->assertPathIs('/home');




29        });




30    }




31}




<?php

namespace Tests\Browser;

use App\Models\User;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Laravel\Dusk\Browser;
use Tests\DuskTestCase;

class ExampleTest extends DuskTestCase
{
    use DatabaseMigrations;

    /**
     * A basic browser test example.
     */
    public function test_basic_example(): void
    {
        $user = User::factory()->create([
            'email' => 'taylor@laravel.com',
        ]);

        $this->browse(function (Browser $browser) use ($user) {
            $browser->visit('/login')
                ->type('email', $user->email)
                ->type('password', 'password')
                ->press('Login')
                ->assertPathIs('/home');
        });
    }
}

```

As you can see in the example above, the `browse` method accepts a closure. A browser instance will automatically be passed to this closure by Dusk and is the main object used to interact with and make assertions against your application.
#### [Creating Multiple Browsers](https://laravel.com/docs/12.x/dusk#creating-multiple-browsers)
Sometimes you may need multiple browsers in order to properly carry out a test. For example, multiple browsers may be needed to test a chat screen that interacts with websockets. To create multiple browsers, simply add more browser arguments to the signature of the closure given to the `browse` method:
```


 1$this->browse(function (Browser $first, Browser $second) {




 2    $first->loginAs(User::find(1))




 3        ->visit('/home')




 4        ->waitForText('Message');




 5 



 6    $second->loginAs(User::find(2))




 7        ->visit('/home')




 8        ->waitForText('Message')




 9        ->type('message', 'Hey Taylor')




10        ->press('Send');




11 



12    $first->waitForText('Hey Taylor')




13        ->assertSee('Jeffrey Way');




14});




$this->browse(function (Browser $first, Browser $second) {
    $first->loginAs(User::find(1))
        ->visit('/home')
        ->waitForText('Message');

    $second->loginAs(User::find(2))
        ->visit('/home')
        ->waitForText('Message')
        ->type('message', 'Hey Taylor')
        ->press('Send');

    $first->waitForText('Hey Taylor')
        ->assertSee('Jeffrey Way');
});

```

### [Navigation](https://laravel.com/docs/12.x/dusk#navigation)
The `visit` method may be used to navigate to a given URI within your application:
```


1$browser->visit('/login');




$browser->visit('/login');

```

You may use the `visitRoute` method to navigate to a [named route](https://laravel.com/docs/12.x/routing#named-routes):
```


1$browser->visitRoute($routeName, $parameters);




$browser->visitRoute($routeName, $parameters);

```

You may navigate "back" and "forward" using the `back` and `forward` methods:
```


1$browser->back();




2 



3$browser->forward();




$browser->back();

$browser->forward();

```

You may use the `refresh` method to refresh the page:
```


1$browser->refresh();




$browser->refresh();

```

### [Resizing Browser Windows](https://laravel.com/docs/12.x/dusk#resizing-browser-windows)
You may use the `resize` method to adjust the size of the browser window:
```


1$browser->resize(1920, 1080);




$browser->resize(1920, 1080);

```

The `maximize` method may be used to maximize the browser window:
```


1$browser->maximize();




$browser->maximize();

```

The `fitContent` method will resize the browser window to match the size of its content:
```


1$browser->fitContent();




$browser->fitContent();

```

When a test fails, Dusk will automatically resize the browser to fit the content prior to taking a screenshot. You may disable this feature by calling the `disableFitOnFailure` method within your test:
```


1$browser->disableFitOnFailure();




$browser->disableFitOnFailure();

```

You may use the `move` method to move the browser window to a different position on your screen:
```


1$browser->move($x = 100, $y = 100);




$browser->move($x = 100, $y = 100);

```

### [Browser Macros](https://laravel.com/docs/12.x/dusk#browser-macros)
If you would like to define a custom browser method that you can reuse in a variety of your tests, you may use the `macro` method on the `Browser` class. Typically, you should call this method from a [service provider's](https://laravel.com/docs/12.x/providers) `boot` method:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Illuminate\Support\ServiceProvider;




 6use Laravel\Dusk\Browser;




 7 



 8class DuskServiceProvider extends ServiceProvider




 9{




10    /**




11     * Register Dusk's browser macros.




12     */




13    public function boot(): void




14    {




15        Browser::macro('scrollToElement', function (string $element = null) {




16            $this->script("$('html, body').animate({ scrollTop: $('$element').offset().top }, 0);");




17 



18            return $this;




19        });




20    }




21}




<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Laravel\Dusk\Browser;

class DuskServiceProvider extends ServiceProvider
{
    /**
     * Register Dusk's browser macros.
     */
    public function boot(): void
    {
        Browser::macro('scrollToElement', function (string $element = null) {
            $this->script("$('html, body').animate({ scrollTop: $('$element').offset().top }, 0);");

            return $this;
        });
    }
}

```

The `macro` function accepts a name as its first argument, and a closure as its second. The macro's closure will be executed when calling the macro as a method on a `Browser` instance:
```


1$this->browse(function (Browser $browser) use ($user) {




2    $browser->visit('/pay')




3        ->scrollToElement('#credit-card-details')




4        ->assertSee('Enter Credit Card Details');




5});




$this->browse(function (Browser $browser) use ($user) {
    $browser->visit('/pay')
        ->scrollToElement('#credit-card-details')
        ->assertSee('Enter Credit Card Details');
});

```

### [Authentication](https://laravel.com/docs/12.x/dusk#authentication)
Often, you will be testing pages that require authentication. You can use Dusk's `loginAs` method in order to avoid interacting with your application's login screen during every test. The `loginAs` method accepts a primary key associated with your authenticatable model or an authenticatable model instance:
```


1use App\Models\User;




2use Laravel\Dusk\Browser;




3 



4$this->browse(function (Browser $browser) {




5    $browser->loginAs(User::find(1))




6        ->visit('/home');




7});




use App\Models\User;
use Laravel\Dusk\Browser;

$this->browse(function (Browser $browser) {
    $browser->loginAs(User::find(1))
        ->visit('/home');
});

```

After using the `loginAs` method, the user session will be maintained for all tests within the file.
### [Cookies](https://laravel.com/docs/12.x/dusk#cookies)
You may use the `cookie` method to get or set an encrypted cookie's value. By default, all of the cookies created by Laravel are encrypted:
```


1$browser->cookie('name');




2 



3$browser->cookie('name', 'Taylor');




$browser->cookie('name');

$browser->cookie('name', 'Taylor');

```

You may use the `plainCookie` method to get or set an unencrypted cookie's value:
```


1$browser->plainCookie('name');




2 



3$browser->plainCookie('name', 'Taylor');




$browser->plainCookie('name');

$browser->plainCookie('name', 'Taylor');

```

You may use the `deleteCookie` method to delete the given cookie:
```


1$browser->deleteCookie('name');




$browser->deleteCookie('name');

```

### [Executing JavaScript](https://laravel.com/docs/12.x/dusk#executing-javascript)
You may use the `script` method to execute arbitrary JavaScript statements within the browser:
```


1$browser->script('document.documentElement.scrollTop = 0');




2 



3$browser->script([




4    'document.body.scrollTop = 0',




5    'document.documentElement.scrollTop = 0',




6]);




7 



8$output = $browser->script('return window.location.pathname');




$browser->script('document.documentElement.scrollTop = 0');

$browser->script([
    'document.body.scrollTop = 0',
    'document.documentElement.scrollTop = 0',
]);

$output = $browser->script('return window.location.pathname');

```

### [Taking a Screenshot](https://laravel.com/docs/12.x/dusk#taking-a-screenshot)
You may use the `screenshot` method to take a screenshot and store it with the given filename. All screenshots will be stored within the `tests/Browser/screenshots` directory:
```


1$browser->screenshot('filename');




$browser->screenshot('filename');

```

The `responsiveScreenshots` method may be used to take a series of screenshots at various breakpoints:
```


1$browser->responsiveScreenshots('filename');




$browser->responsiveScreenshots('filename');

```

The `screenshotElement` method may be used to take a screenshot of a specific element on the page:
```


1$browser->screenshotElement('#selector', 'filename');




$browser->screenshotElement('#selector', 'filename');

```

### [Storing Console Output to Disk](https://laravel.com/docs/12.x/dusk#storing-console-output-to-disk)
You may use the `storeConsoleLog` method to write the current browser's console output to disk with the given filename. Console output will be stored within the `tests/Browser/console` directory:
```


1$browser->storeConsoleLog('filename');




$browser->storeConsoleLog('filename');

```

### [Storing Page Source to Disk](https://laravel.com/docs/12.x/dusk#storing-page-source-to-disk)
You may use the `storeSource` method to write the current page's source to disk with the given filename. The page source will be stored within the `tests/Browser/source` directory:
```


1$browser->storeSource('filename');




$browser->storeSource('filename');

```
