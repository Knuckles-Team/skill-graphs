## [Interacting With Elements](https://laravel.com/docs/12.x/dusk#interacting-with-elements)
### [Dusk Selectors](https://laravel.com/docs/12.x/dusk#dusk-selectors)
Choosing good CSS selectors for interacting with elements is one of the hardest parts of writing Dusk tests. Over time, frontend changes can cause CSS selectors like the following to break your tests:
```


1// HTML...




2 



3<button>Login</button>




// HTML...

<button>Login</button>

```

```


1// Test...




2 



3$browser->click('.login-page .container div > button');




// Test...

$browser->click('.login-page .container div > button');

```

Dusk selectors allow you to focus on writing effective tests rather than remembering CSS selectors. To define a selector, add a `dusk` attribute to your HTML element. Then, when interacting with a Dusk browser, prefix the selector with `@` to manipulate the attached element within your test:
```


1// HTML...




2 



3<button dusk="login-button">Login</button>




// HTML...

<button dusk="login-button">Login</button>

```

```


1// Test...




2 



3$browser->click('@login-button');




// Test...

$browser->click('@login-button');

```

If desired, you may customize the HTML attribute that the Dusk selector utilizes via the `selectorHtmlAttribute` method. Typically, this method should be called from the `boot` method of your application's `AppServiceProvider`:
```


1use Laravel\Dusk\Dusk;




2 



3Dusk::selectorHtmlAttribute('data-dusk');




use Laravel\Dusk\Dusk;

Dusk::selectorHtmlAttribute('data-dusk');

```

### [Text, Values, and Attributes](https://laravel.com/docs/12.x/dusk#text-values-and-attributes)
#### [Retrieving and Setting Values](https://laravel.com/docs/12.x/dusk#retrieving-setting-values)
Dusk provides several methods for interacting with the current value, display text, and attributes of elements on the page. For example, to get the "value" of an element that matches a given CSS or Dusk selector, use the `value` method:
```


1// Retrieve the value...




2$value = $browser->value('selector');




3 



4// Set the value...




5$browser->value('selector', 'value');




// Retrieve the value...
$value = $browser->value('selector');

// Set the value...
$browser->value('selector', 'value');

```

You may use the `inputValue` method to get the "value" of an input element that has a given field name:
```


1$value = $browser->inputValue('field');




$value = $browser->inputValue('field');

```

#### [Retrieving Text](https://laravel.com/docs/12.x/dusk#retrieving-text)
The `text` method may be used to retrieve the display text of an element that matches the given selector:
```


1$text = $browser->text('selector');




$text = $browser->text('selector');

```

#### [Retrieving Attributes](https://laravel.com/docs/12.x/dusk#retrieving-attributes)
Finally, the `attribute` method may be used to retrieve the value of an attribute of an element matching the given selector:
```


1$attribute = $browser->attribute('selector', 'value');




$attribute = $browser->attribute('selector', 'value');

```

### [Interacting With Forms](https://laravel.com/docs/12.x/dusk#interacting-with-forms)
#### [Typing Values](https://laravel.com/docs/12.x/dusk#typing-values)
Dusk provides a variety of methods for interacting with forms and input elements. First, let's take a look at an example of typing text into an input field:
```


1$browser->type('email', 'taylor@laravel.com');




$browser->type('email', 'taylor@laravel.com');

```

Note that, although the method accepts one if necessary, we are not required to pass a CSS selector into the `type` method. If a CSS selector is not provided, Dusk will search for an `input` or `textarea` field with the given `name` attribute.
To append text to a field without clearing its content, you may use the `append` method:
```


1$browser->type('tags', 'foo')




2    ->append('tags', ', bar, baz');




$browser->type('tags', 'foo')
    ->append('tags', ', bar, baz');

```

You may clear the value of an input using the `clear` method:
```


1$browser->clear('email');




$browser->clear('email');

```

You can instruct Dusk to type slowly using the `typeSlowly` method. By default, Dusk will pause for 100 milliseconds between key presses. To customize the amount of time between key presses, you may pass the appropriate number of milliseconds as the third argument to the method:
```


1$browser->typeSlowly('mobile', '+1 (202) 555-5555');




2 



3$browser->typeSlowly('mobile', '+1 (202) 555-5555', 300);




$browser->typeSlowly('mobile', '+1 (202) 555-5555');

$browser->typeSlowly('mobile', '+1 (202) 555-5555', 300);

```

You may use the `appendSlowly` method to append text slowly:
```


1$browser->type('tags', 'foo')




2    ->appendSlowly('tags', ', bar, baz');




$browser->type('tags', 'foo')
    ->appendSlowly('tags', ', bar, baz');

```

#### [Dropdowns](https://laravel.com/docs/12.x/dusk#dropdowns)
To select a value available on a `select` element, you may use the `select` method. Like the `type` method, the `select` method does not require a full CSS selector. When passing a value to the `select` method, you should pass the underlying option value instead of the display text:
```


1$browser->select('size', 'Large');




$browser->select('size', 'Large');

```

You may select a random option by omitting the second argument:
```


1$browser->select('size');




$browser->select('size');

```

By providing an array as the second argument to the `select` method, you can instruct the method to select multiple options:
```


1$browser->select('categories', ['Art', 'Music']);




$browser->select('categories', ['Art', 'Music']);

```

#### [Checkboxes](https://laravel.com/docs/12.x/dusk#checkboxes)
To "check" a checkbox input, you may use the `check` method. Like many other input related methods, a full CSS selector is not required. If a CSS selector match can't be found, Dusk will search for a checkbox with a matching `name` attribute:
```


1$browser->check('terms');




$browser->check('terms');

```

The `uncheck` method may be used to "uncheck" a checkbox input:
```


1$browser->uncheck('terms');




$browser->uncheck('terms');

```

#### [Radio Buttons](https://laravel.com/docs/12.x/dusk#radio-buttons)
To "select" a `radio` input option, you may use the `radio` method. Like many other input related methods, a full CSS selector is not required. If a CSS selector match can't be found, Dusk will search for a `radio` input with matching `name` and `value` attributes:
```


1$browser->radio('size', 'large');




$browser->radio('size', 'large');

```

### [Attaching Files](https://laravel.com/docs/12.x/dusk#attaching-files)
The `attach` method may be used to attach a file to a `file` input element. Like many other input related methods, a full CSS selector is not required. If a CSS selector match can't be found, Dusk will search for a `file` input with a matching `name` attribute:
```


1$browser->attach('photo', __DIR__.'/photos/mountains.png');




$browser->attach('photo', __DIR__.'/photos/mountains.png');

```

The attach function requires the `Zip` PHP extension to be installed and enabled on your server.
### [Pressing Buttons](https://laravel.com/docs/12.x/dusk#pressing-buttons)
The `press` method may be used to click a button element on the page. The argument given to the `press` method may be either the display text of the button or a CSS / Dusk selector:
```


1$browser->press('Login');




$browser->press('Login');

```

When submitting forms, many applications disable the form's submission button after it is pressed and then re-enable the button when the form submission's HTTP request is complete. To press a button and wait for the button to be re-enabled, you may use the `pressAndWaitFor` method:
```


1// Press the button and wait a maximum of 5 seconds for it to be enabled...




2$browser->pressAndWaitFor('Save');




3 



4// Press the button and wait a maximum of 1 second for it to be enabled...




5$browser->pressAndWaitFor('Save', 1);




// Press the button and wait a maximum of 5 seconds for it to be enabled...
$browser->pressAndWaitFor('Save');

// Press the button and wait a maximum of 1 second for it to be enabled...
$browser->pressAndWaitFor('Save', 1);

```

### [Clicking Links](https://laravel.com/docs/12.x/dusk#clicking-links)
To click a link, you may use the `clickLink` method on the browser instance. The `clickLink` method will click the link that has the given display text:
```


1$browser->clickLink($linkText);




$browser->clickLink($linkText);

```

You may use the `seeLink` method to determine if a link with the given display text is visible on the page:
```


1if ($browser->seeLink($linkText)) {




2    // ...




3}




if ($browser->seeLink($linkText)) {
    // ...
}

```

These methods interact with jQuery. If jQuery is not available on the page, Dusk will automatically inject it into the page so it is available for the test's duration.
### [Using the Keyboard](https://laravel.com/docs/12.x/dusk#using-the-keyboard)
The `keys` method allows you to provide more complex input sequences to a given element than normally allowed by the `type` method. For example, you may instruct Dusk to hold modifier keys while entering values. In this example, the `shift` key will be held while `taylor` is entered into the element matching the given selector. After `taylor` is typed, `swift` will be typed without any modifier keys:
```


1$browser->keys('selector', ['{shift}', 'taylor'], 'swift');




$browser->keys('selector', ['{shift}', 'taylor'], 'swift');

```

Another valuable use case for the `keys` method is sending a "keyboard shortcut" combination to the primary CSS selector for your application:
```


1$browser->keys('.app', ['{command}', 'j']);




$browser->keys('.app', ['{command}', 'j']);

```

All modifier keys such as `{command}` are wrapped in `{}` characters, and match the constants defined in the `Facebook\WebDriver\WebDriverKeys` class, which can be
#### [Fluent Keyboard Interactions](https://laravel.com/docs/12.x/dusk#fluent-keyboard-interactions)
Dusk also provides a `withKeyboard` method, allowing you to fluently perform complex keyboard interactions via the `Laravel\Dusk\Keyboard` class. The `Keyboard` class provides `press`, `release`, `type`, and `pause` methods:
```


1use Laravel\Dusk\Keyboard;




2 



3$browser->withKeyboard(function (Keyboard $keyboard) {




4    $keyboard->press('c')




5        ->pause(1000)




6        ->release('c')




7        ->type(['c', 'e', 'o']);




8});




use Laravel\Dusk\Keyboard;

$browser->withKeyboard(function (Keyboard $keyboard) {
    $keyboard->press('c')
        ->pause(1000)
        ->release('c')
        ->type(['c', 'e', 'o']);
});

```

#### [Keyboard Macros](https://laravel.com/docs/12.x/dusk#keyboard-macros)
If you would like to define custom keyboard interactions that you can easily reuse throughout your test suite, you may use the `macro` method provided by the `Keyboard` class. Typically, you should call this method from a [service provider's](https://laravel.com/docs/12.x/providers) `boot` method:
```


 1<?php




 2 



 3namespace App\Providers;




 4 



 5use Facebook\WebDriver\WebDriverKeys;




 6use Illuminate\Support\ServiceProvider;




 7use Laravel\Dusk\Keyboard;




 8use Laravel\Dusk\OperatingSystem;




 9 



10class DuskServiceProvider extends ServiceProvider




11{




12    /**




13     * Register Dusk's browser macros.




14     */




15    public function boot(): void




16    {




17        Keyboard::macro('copy', function (string $element = null) {




18            $this->type([




19                OperatingSystem::onMac() ? WebDriverKeys::META : WebDriverKeys::CONTROL, 'c',




20            ]);




21 



22            return $this;




23        });




24 



25        Keyboard::macro('paste', function (string $element = null) {




26            $this->type([




27                OperatingSystem::onMac() ? WebDriverKeys::META : WebDriverKeys::CONTROL, 'v',




28            ]);




29 



30            return $this;




31        });




32    }




33}




<?php

namespace App\Providers;

use Facebook\WebDriver\WebDriverKeys;
use Illuminate\Support\ServiceProvider;
use Laravel\Dusk\Keyboard;
use Laravel\Dusk\OperatingSystem;

class DuskServiceProvider extends ServiceProvider
{
    /**
     * Register Dusk's browser macros.
     */
    public function boot(): void
    {
        Keyboard::macro('copy', function (string $element = null) {
            $this->type([
                OperatingSystem::onMac() ? WebDriverKeys::META : WebDriverKeys::CONTROL, 'c',
            ]);

            return $this;
        });

        Keyboard::macro('paste', function (string $element = null) {
            $this->type([
                OperatingSystem::onMac() ? WebDriverKeys::META : WebDriverKeys::CONTROL, 'v',
            ]);

            return $this;
        });
    }
}

```

The `macro` function accepts a name as its first argument and a closure as its second. The macro's closure will be executed when calling the macro as a method on a `Keyboard` instance:
```


1$browser->click('@textarea')




2    ->withKeyboard(fn (Keyboard $keyboard) => $keyboard->copy())




3    ->click('@another-textarea')




4    ->withKeyboard(fn (Keyboard $keyboard) => $keyboard->paste());




$browser->click('@textarea')
    ->withKeyboard(fn (Keyboard $keyboard) => $keyboard->copy())
    ->click('@another-textarea')
    ->withKeyboard(fn (Keyboard $keyboard) => $keyboard->paste());

```

### [Using the Mouse](https://laravel.com/docs/12.x/dusk#using-the-mouse)
#### [Clicking on Elements](https://laravel.com/docs/12.x/dusk#clicking-on-elements)
The `click` method may be used to click on an element matching the given CSS or Dusk selector:
```


1$browser->click('.selector');




$browser->click('.selector');

```

The `clickAtXPath` method may be used to click on an element matching the given XPath expression:
```


1$browser->clickAtXPath('//div[@class = "selector"]');




$browser->clickAtXPath('//div[@class = "selector"]');

```

The `clickAtPoint` method may be used to click on the topmost element at a given pair of coordinates relative to the viewable area of the browser:
```


1$browser->clickAtPoint($x = 0, $y = 0);




$browser->clickAtPoint($x = 0, $y = 0);

```

The `double-click` method may be used to simulate the double click of a mouse:
```


1$browser->double-click();




2 



3$browser->double-click('.selector');




$browser->double-click();

$browser->double-click('.selector');

```

The `rightClick` method may be used to simulate the right click of a mouse:
```


1$browser->rightClick();




2 



3$browser->rightClick('.selector');




$browser->rightClick();

$browser->rightClick('.selector');

```

The `clickAndHold` method may be used to simulate a mouse button being clicked and held down. A subsequent call to the `releaseMouse` method will undo this behavior and release the mouse button:
```


1$browser->clickAndHold('.selector');




2 



3$browser->clickAndHold()




4    ->pause(1000)




5    ->releaseMouse();




$browser->clickAndHold('.selector');

$browser->clickAndHold()
    ->pause(1000)
    ->releaseMouse();

```

The `controlClick` method may be used to simulate the `ctrl+click` event within the browser:
```


1$browser->controlClick();




2 



3$browser->controlClick('.selector');




$browser->controlClick();

$browser->controlClick('.selector');

```

#### [Mouseover](https://laravel.com/docs/12.x/dusk#mouseover)
The `mouseover` method may be used when you need to move the mouse over an element matching the given CSS or Dusk selector:
```


1$browser->mouseover('.selector');




$browser->mouseover('.selector');

```

#### [Drag and Drop](https://laravel.com/docs/12.x/dusk#drag-drop)
The `drag` method may be used to drag an element matching the given selector to another element:
```


1$browser->drag('.from-selector', '.to-selector');




$browser->drag('.from-selector', '.to-selector');

```

Or, you may drag an element in a single direction:
```


1$browser->dragLeft('.selector', $pixels = 10);




2$browser->dragRight('.selector', $pixels = 10);




3$browser->dragUp('.selector', $pixels = 10);




4$browser->dragDown('.selector', $pixels = 10);




$browser->dragLeft('.selector', $pixels = 10);
$browser->dragRight('.selector', $pixels = 10);
$browser->dragUp('.selector', $pixels = 10);
$browser->dragDown('.selector', $pixels = 10);

```

Finally, you may drag an element by a given offset:
```


1$browser->dragOffset('.selector', $x = 10, $y = 10);




$browser->dragOffset('.selector', $x = 10, $y = 10);

```

### [JavaScript Dialogs](https://laravel.com/docs/12.x/dusk#javascript-dialogs)
Dusk provides various methods to interact with JavaScript Dialogs. For example, you may use the `waitForDialog` method to wait for a JavaScript dialog to appear. This method accepts an optional argument indicating how many seconds to wait for the dialog to appear:
```


1$browser->waitForDialog($seconds = null);




$browser->waitForDialog($seconds = null);

```

The `assertDialogOpened` method may be used to assert that a dialog has been displayed and contains the given message:
```


1$browser->assertDialogOpened('Dialog message');




$browser->assertDialogOpened('Dialog message');

```

If the JavaScript dialog contains a prompt, you may use the `typeInDialog` method to type a value into the prompt:
```


1$browser->typeInDialog('Hello World');




$browser->typeInDialog('Hello World');

```

To close an open JavaScript dialog by clicking the "OK" button, you may invoke the `acceptDialog` method:
```


1$browser->acceptDialog();




$browser->acceptDialog();

```

To close an open JavaScript dialog by clicking the "Cancel" button, you may invoke the `dismissDialog` method:
```


1$browser->dismissDialog();




$browser->dismissDialog();

```

### [Interacting With Inline Frames](https://laravel.com/docs/12.x/dusk#interacting-with-iframes)
If you need to interact with elements within an iframe, you may use the `withinFrame` method. All element interactions that take place within the closure provided to the `withinFrame` method will be scoped to the context of the specified iframe:
```


1$browser->withinFrame('#credit-card-details', function ($browser) {




2    $browser->type('input[name="cardnumber"]', '4242424242424242')




3        ->type('input[name="exp-date"]', '1224')




4        ->type('input[name="cvc"]', '123')




5        ->press('Pay');




6});




$browser->withinFrame('#credit-card-details', function ($browser) {
    $browser->type('input[name="cardnumber"]', '4242424242424242')
        ->type('input[name="exp-date"]', '1224')
        ->type('input[name="cvc"]', '123')
        ->press('Pay');
});

```

### [Scoping Selectors](https://laravel.com/docs/12.x/dusk#scoping-selectors)
Sometimes you may wish to perform several operations while scoping all of the operations within a given selector. For example, you may wish to assert that some text exists only within a table and then click a button within that table. You may use the `with` method to accomplish this. All operations performed within the closure given to the `with` method will be scoped to the original selector:
```


1$browser->with('.table', function (Browser $table) {




2    $table->assertSee('Hello World')




3        ->clickLink('Delete');




4});




$browser->with('.table', function (Browser $table) {
    $table->assertSee('Hello World')
        ->clickLink('Delete');
});

```

You may occasionally need to execute assertions outside of the current scope. You may use the `elsewhere` and `elsewhereWhenAvailable` methods to accomplish this:
```


 1$browser->with('.table', function (Browser $table) {




 2    // Current scope is `body .table`...




 3 



 4    $browser->elsewhere('.page-title', function (Browser $title) {




 5        // Current scope is `body .page-title`...




 6        $title->assertSee('Hello World');




 7    });




 8 



 9    $browser->elsewhereWhenAvailable('.page-title', function (Browser $title) {




10        // Current scope is `body .page-title`...




11        $title->assertSee('Hello World');




12    });




13});




$browser->with('.table', function (Browser $table) {
    // Current scope is `body .table`...

    $browser->elsewhere('.page-title', function (Browser $title) {
        // Current scope is `body .page-title`...
        $title->assertSee('Hello World');
    });

    $browser->elsewhereWhenAvailable('.page-title', function (Browser $title) {
        // Current scope is `body .page-title`...
        $title->assertSee('Hello World');
    });
});

```

### [Waiting for Elements](https://laravel.com/docs/12.x/dusk#waiting-for-elements)
When testing applications that use JavaScript extensively, it often becomes necessary to "wait" for certain elements or data to be available before proceeding with a test. Dusk makes this a cinch. Using a variety of methods, you may wait for elements to become visible on the page or even wait until a given JavaScript expression evaluates to `true`.
#### [Waiting](https://laravel.com/docs/12.x/dusk#waiting)
If you just need to pause the test for a given number of milliseconds, use the `pause` method:
```


1$browser->pause(1000);




$browser->pause(1000);

```

If you need to pause the test only if a given condition is `true`, use the `pauseIf` method:
```


1$browser->pauseIf(App::environment('production'), 1000);




$browser->pauseIf(App::environment('production'), 1000);

```

Likewise, if you need to pause the test unless a given condition is `true`, you may use the `pauseUnless` method:
```


1$browser->pauseUnless(App::environment('testing'), 1000);




$browser->pauseUnless(App::environment('testing'), 1000);

```

#### [Waiting for Selectors](https://laravel.com/docs/12.x/dusk#waiting-for-selectors)
The `waitFor` method may be used to pause the execution of the test until the element matching the given CSS or Dusk selector is displayed on the page. By default, this will pause the test for a maximum of five seconds before throwing an exception. If necessary, you may pass a custom timeout threshold as the second argument to the method:
```


1// Wait a maximum of five seconds for the selector...




2$browser->waitFor('.selector');




3 



4// Wait a maximum of one second for the selector...




5$browser->waitFor('.selector', 1);




// Wait a maximum of five seconds for the selector...
$browser->waitFor('.selector');

// Wait a maximum of one second for the selector...
$browser->waitFor('.selector', 1);

```

You may also wait until the element matching the given selector contains the given text:
```


1// Wait a maximum of five seconds for the selector to contain the given text...




2$browser->waitForTextIn('.selector', 'Hello World');




3 



4// Wait a maximum of one second for the selector to contain the given text...




5$browser->waitForTextIn('.selector', 'Hello World', 1);




// Wait a maximum of five seconds for the selector to contain the given text...
$browser->waitForTextIn('.selector', 'Hello World');

// Wait a maximum of one second for the selector to contain the given text...
$browser->waitForTextIn('.selector', 'Hello World', 1);

```

You may also wait until the element matching the given selector is missing from the page:
```


1// Wait a maximum of five seconds until the selector is missing...




2$browser->waitUntilMissing('.selector');




3 



4// Wait a maximum of one second until the selector is missing...




5$browser->waitUntilMissing('.selector', 1);




// Wait a maximum of five seconds until the selector is missing...
$browser->waitUntilMissing('.selector');

// Wait a maximum of one second until the selector is missing...
$browser->waitUntilMissing('.selector', 1);

```

Or, you may wait until the element matching the given selector is enabled or disabled:
```


 1// Wait a maximum of five seconds until the selector is enabled...




 2$browser->waitUntilEnabled('.selector');




 3 



 4// Wait a maximum of one second until the selector is enabled...




 5$browser->waitUntilEnabled('.selector', 1);




 6 



 7// Wait a maximum of five seconds until the selector is disabled...




 8$browser->waitUntilDisabled('.selector');




 9 



10// Wait a maximum of one second until the selector is disabled...




11$browser->waitUntilDisabled('.selector', 1);




// Wait a maximum of five seconds until the selector is enabled...
$browser->waitUntilEnabled('.selector');

// Wait a maximum of one second until the selector is enabled...
$browser->waitUntilEnabled('.selector', 1);

// Wait a maximum of five seconds until the selector is disabled...
$browser->waitUntilDisabled('.selector');

// Wait a maximum of one second until the selector is disabled...
$browser->waitUntilDisabled('.selector', 1);

```

#### [Scoping Selectors When Available](https://laravel.com/docs/12.x/dusk#scoping-selectors-when-available)
Occasionally, you may wish to wait for an element to appear that matches a given selector and then interact with the element. For example, you may wish to wait until a modal window is available and then press the "OK" button within the modal. The `whenAvailable` method may be used to accomplish this. All element operations performed within the given closure will be scoped to the original selector:
```


1$browser->whenAvailable('.modal', function (Browser $modal) {




2    $modal->assertSee('Hello World')




3        ->press('OK');




4});




$browser->whenAvailable('.modal', function (Browser $modal) {
    $modal->assertSee('Hello World')
        ->press('OK');
});

```

#### [Waiting for Text](https://laravel.com/docs/12.x/dusk#waiting-for-text)
The `waitForText` method may be used to wait until the given text is displayed on the page:
```


1// Wait a maximum of five seconds for the text...




2$browser->waitForText('Hello World');




3 



4// Wait a maximum of one second for the text...




5$browser->waitForText('Hello World', 1);




// Wait a maximum of five seconds for the text...
$browser->waitForText('Hello World');

// Wait a maximum of one second for the text...
$browser->waitForText('Hello World', 1);

```

You may use the `waitUntilMissingText` method to wait until the displayed text has been removed from the page:
```


1// Wait a maximum of five seconds for the text to be removed...




2$browser->waitUntilMissingText('Hello World');




3 



4// Wait a maximum of one second for the text to be removed...




5$browser->waitUntilMissingText('Hello World', 1);




// Wait a maximum of five seconds for the text to be removed...
$browser->waitUntilMissingText('Hello World');

// Wait a maximum of one second for the text to be removed...
$browser->waitUntilMissingText('Hello World', 1);

```

#### [Waiting for Links](https://laravel.com/docs/12.x/dusk#waiting-for-links)
The `waitForLink` method may be used to wait until the given link text is displayed on the page:
```


1// Wait a maximum of five seconds for the link...




2$browser->waitForLink('Create');




3 



4// Wait a maximum of one second for the link...




5$browser->waitForLink('Create', 1);




// Wait a maximum of five seconds for the link...
$browser->waitForLink('Create');

// Wait a maximum of one second for the link...
$browser->waitForLink('Create', 1);

```

#### [Waiting for Inputs](https://laravel.com/docs/12.x/dusk#waiting-for-inputs)
The `waitForInput` method may be used to wait until the given input field is visible on the page:
```


1// Wait a maximum of five seconds for the input...




2$browser->waitForInput($field);




3 



4// Wait a maximum of one second for the input...




5$browser->waitForInput($field, 1);




// Wait a maximum of five seconds for the input...
$browser->waitForInput($field);

// Wait a maximum of one second for the input...
$browser->waitForInput($field, 1);

```

#### [Waiting on the Page Location](https://laravel.com/docs/12.x/dusk#waiting-on-the-page-location)
When making a path assertion such as `$browser->assertPathIs('/home')`, the assertion can fail if `window.location.pathname` is being updated asynchronously. You may use the `waitForLocation` method to wait for the location to be a given value:
```


1$browser->waitForLocation('/secret');




$browser->waitForLocation('/secret');

```

The `waitForLocation` method can also be used to wait for the current window location to be a fully qualified URL:
```


1$browser->waitForLocation('https://example.com/path');




$browser->waitForLocation('https://example.com/path');

```

You may also wait for a [named route's](https://laravel.com/docs/12.x/routing#named-routes) location:
```


1$browser->waitForRoute($routeName, $parameters);




$browser->waitForRoute($routeName, $parameters);

```

#### [Waiting for Page Reloads](https://laravel.com/docs/12.x/dusk#waiting-for-page-reloads)
If you need to wait for a page to reload after performing an action, use the `waitForReload` method:
```


1use Laravel\Dusk\Browser;




2 



3$browser->waitForReload(function (Browser $browser) {




4    $browser->press('Submit');




5})




6->assertSee('Success!');




use Laravel\Dusk\Browser;

$browser->waitForReload(function (Browser $browser) {
    $browser->press('Submit');
})
->assertSee('Success!');

```

Since the need to wait for the page to reload typically occurs after clicking a button, you may use the `clickAndWaitForReload` method for convenience:
```


1$browser->clickAndWaitForReload('.selector')




2    ->assertSee('something');




$browser->clickAndWaitForReload('.selector')
    ->assertSee('something');

```

#### [Waiting on JavaScript Expressions](https://laravel.com/docs/12.x/dusk#waiting-on-javascript-expressions)
Sometimes you may wish to pause the execution of a test until a given JavaScript expression evaluates to `true`. You may easily accomplish this using the `waitUntil` method. When passing an expression to this method, you do not need to include the `return` keyword or an ending semi-colon:
```


1// Wait a maximum of five seconds for the expression to be true...




2$browser->waitUntil('App.data.servers.length > 0');




3 



4// Wait a maximum of one second for the expression to be true...




5$browser->waitUntil('App.data.servers.length > 0', 1);




// Wait a maximum of five seconds for the expression to be true...
$browser->waitUntil('App.data.servers.length > 0');

// Wait a maximum of one second for the expression to be true...
$browser->waitUntil('App.data.servers.length > 0', 1);

```

#### [Waiting on Vue Expressions](https://laravel.com/docs/12.x/dusk#waiting-on-vue-expressions)
The `waitUntilVue` and `waitUntilVueIsNot` methods may be used to wait until a
```


1// Wait until the component attribute contains the given value...




2$browser->waitUntilVue('user.name', 'Taylor', '@user');




3 



4// Wait until the component attribute doesn't contain the given value...




5$browser->waitUntilVueIsNot('user.name', null, '@user');




// Wait until the component attribute contains the given value...
$browser->waitUntilVue('user.name', 'Taylor', '@user');

// Wait until the component attribute doesn't contain the given value...
$browser->waitUntilVueIsNot('user.name', null, '@user');

```

#### [Waiting for JavaScript Events](https://laravel.com/docs/12.x/dusk#waiting-for-javascript-events)
The `waitForEvent` method can be used to pause the execution of a test until a JavaScript event occurs:
```


1$browser->waitForEvent('load');




$browser->waitForEvent('load');

```

The event listener is attached to the current scope, which is the `body` element by default. When using a scoped selector, the event listener will be attached to the matching element:
```


1$browser->with('iframe', function (Browser $iframe) {




2    // Wait for the iframe's load event...




3    $iframe->waitForEvent('load');




4});




$browser->with('iframe', function (Browser $iframe) {
    // Wait for the iframe's load event...
    $iframe->waitForEvent('load');
});

```

You may also provide a selector as the second argument to the `waitForEvent` method to attach the event listener to a specific element:
```


1$browser->waitForEvent('load', '.selector');




$browser->waitForEvent('load', '.selector');

```

You may also wait for events on the `document` and `window` objects:
```


1// Wait until the document is scrolled...




2$browser->waitForEvent('scroll', 'document');




3 



4// Wait a maximum of five seconds until the window is resized...




5$browser->waitForEvent('resize', 'window', 5);




// Wait until the document is scrolled...
$browser->waitForEvent('scroll', 'document');

// Wait a maximum of five seconds until the window is resized...
$browser->waitForEvent('resize', 'window', 5);

```

#### [Waiting With a Callback](https://laravel.com/docs/12.x/dusk#waiting-with-a-callback)
Many of the "wait" methods in Dusk rely on the underlying `waitUsing` method. You may use this method directly to wait for a given closure to return `true`. The `waitUsing` method accepts the maximum number of seconds to wait, the interval at which the closure should be evaluated, the closure, and an optional failure message:
```


1$browser->waitUsing(10, 1, function () use ($something) {




2    return $something->isReady();




3}, "Something wasn't ready in time.");




$browser->waitUsing(10, 1, function () use ($something) {
    return $something->isReady();
}, "Something wasn't ready in time.");

```

### [Scrolling an Element Into View](https://laravel.com/docs/12.x/dusk#scrolling-an-element-into-view)
Sometimes you may not be able to click on an element because it is outside of the viewable area of the browser. The `scrollIntoView` method will scroll the browser window until the element at the given selector is within the view:
```


1$browser->scrollIntoView('.selector')




2    ->click('.selector');




$browser->scrollIntoView('.selector')
    ->click('.selector');

```
