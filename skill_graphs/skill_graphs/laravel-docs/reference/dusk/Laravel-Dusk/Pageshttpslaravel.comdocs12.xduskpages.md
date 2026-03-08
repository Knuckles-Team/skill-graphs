## [Pages](https://laravel.com/docs/12.x/dusk#pages)
Sometimes, tests require several complicated actions to be performed in sequence. This can make your tests harder to read and understand. Dusk Pages allow you to define expressive actions that may then be performed on a given page via a single method. Pages also allow you to define short-cuts to common selectors for your application or for a single page.
### [Generating Pages](https://laravel.com/docs/12.x/dusk#generating-pages)
To generate a page object, execute the `dusk:page` Artisan command. All page objects will be placed in your application's `tests/Browser/Pages` directory:
```


1php artisan dusk:page Login




php artisan dusk:page Login

```

### [Configuring Pages](https://laravel.com/docs/12.x/dusk#configuring-pages)
By default, pages have three methods: `url`, `assert`, and `elements`. We will discuss the `url` and `assert` methods now. The `elements` method will be [discussed in more detail below](https://laravel.com/docs/12.x/dusk#shorthand-selectors).
#### [The `url` Method](https://laravel.com/docs/12.x/dusk#the-url-method)
The `url` method should return the path of the URL that represents the page. Dusk will use this URL when navigating to the page in the browser:
```


1/**




2 * Get the URL for the page.




3 */




4public function url(): string




5{




6    return '/login';




7}




/**
 * Get the URL for the page.
 */
public function url(): string
{
    return '/login';
}

```

#### [The `assert` Method](https://laravel.com/docs/12.x/dusk#the-assert-method)
The `assert` method may make any assertions necessary to verify that the browser is actually on the given page. It is not actually necessary to place anything within this method; however, you are free to make these assertions if you wish. These assertions will be run automatically when navigating to the page:
```


1/**




2 * Assert that the browser is on the page.




3 */




4public function assert(Browser $browser): void




5{




6    $browser->assertPathIs($this->url());




7}




/**
 * Assert that the browser is on the page.
 */
public function assert(Browser $browser): void
{
    $browser->assertPathIs($this->url());
}

```

### [Navigating to Pages](https://laravel.com/docs/12.x/dusk#navigating-to-pages)
Once a page has been defined, you may navigate to it using the `visit` method:
```


1use Tests\Browser\Pages\Login;




2 



3$browser->visit(new Login);




use Tests\Browser\Pages\Login;

$browser->visit(new Login);

```

Sometimes you may already be on a given page and need to "load" the page's selectors and methods into the current test context. This is common when pressing a button and being redirected to a given page without explicitly navigating to it. In this situation, you may use the `on` method to load the page:
```


1use Tests\Browser\Pages\CreatePlaylist;




2 



3$browser->visit('/dashboard')




4    ->clickLink('Create Playlist')




5    ->on(new CreatePlaylist)




6    ->assertSee('@create');




use Tests\Browser\Pages\CreatePlaylist;

$browser->visit('/dashboard')
    ->clickLink('Create Playlist')
    ->on(new CreatePlaylist)
    ->assertSee('@create');

```

### [Shorthand Selectors](https://laravel.com/docs/12.x/dusk#shorthand-selectors)
The `elements` method within page classes allows you to define quick, easy-to-remember shortcuts for any CSS selector on your page. For example, let's define a shortcut for the "email" input field of the application's login page:
```


 1/**




 2 * Get the element shortcuts for the page.




 3 *




 4 * @return array<string, string>




 5 */




 6public function elements(): array




 7{




 8    return [




 9        '@email' => 'input[name=email]',




10    ];




11}




/**
 * Get the element shortcuts for the page.
 *
 * @return array<string, string>
 */
public function elements(): array
{
    return [
        '@email' => 'input[name=email]',
    ];
}

```

Once the shortcut has been defined, you may use the shorthand selector anywhere you would typically use a full CSS selector:
```


1$browser->type('@email', 'taylor@laravel.com');




$browser->type('@email', 'taylor@laravel.com');

```

#### [Global Shorthand Selectors](https://laravel.com/docs/12.x/dusk#global-shorthand-selectors)
After installing Dusk, a base `Page` class will be placed in your `tests/Browser/Pages` directory. This class contains a `siteElements` method which may be used to define global shorthand selectors that should be available on every page throughout your application:
```


 1/**




 2 * Get the global element shortcuts for the site.




 3 *




 4 * @return array<string, string>




 5 */




 6public static function siteElements(): array




 7{




 8    return [




 9        '@element' => '#selector',




10    ];




11}




/**
 * Get the global element shortcuts for the site.
 *
 * @return array<string, string>
 */
public static function siteElements(): array
{
    return [
        '@element' => '#selector',
    ];
}

```

### [Page Methods](https://laravel.com/docs/12.x/dusk#page-methods)
In addition to the default methods defined on pages, you may define additional methods which may be used throughout your tests. For example, let's imagine we are building a music management application. A common action for one page of the application might be to create a playlist. Instead of re-writing the logic to create a playlist in each test, you may define a `createPlaylist` method on a page class:
```


 1<?php




 2 



 3namespace Tests\Browser\Pages;




 4 



 5use Laravel\Dusk\Browser;




 6use Laravel\Dusk\Page;




 7 



 8class Dashboard extends Page




 9{




10    // Other page methods...




11 



12    /**




13     * Create a new playlist.




14     */




15    public function createPlaylist(Browser $browser, string $name): void




16    {




17        $browser->type('name', $name)




18            ->check('share')




19            ->press('Create Playlist');




20    }




21}




<?php

namespace Tests\Browser\Pages;

use Laravel\Dusk\Browser;
use Laravel\Dusk\Page;

class Dashboard extends Page
{
    // Other page methods...

    /**
     * Create a new playlist.
     */
    public function createPlaylist(Browser $browser, string $name): void
    {
        $browser->type('name', $name)
            ->check('share')
            ->press('Create Playlist');
    }
}

```

Once the method has been defined, you may use it within any test that utilizes the page. The browser instance will automatically be passed as the first argument to custom page methods:
```


1use Tests\Browser\Pages\Dashboard;




2 



3$browser->visit(new Dashboard)




4    ->createPlaylist('My Playlist')




5    ->assertSee('My Playlist');




use Tests\Browser\Pages\Dashboard;

$browser->visit(new Dashboard)
    ->createPlaylist('My Playlist')
    ->assertSee('My Playlist');

```
