```


1use Illuminate\Support\Str;




2 



3$string = Str::of('1300')->substrReplace(':', 2);




4 



5// 13:




6 



7$string = Str::of('The Framework')->substrReplace(' Laravel', 3, 0);




8 



9// The Laravel Framework




use Illuminate\Support\Str;

$string = Str::of('1300')->substrReplace(':', 2);

// 13:

$string = Str::of('The Framework')->substrReplace(' Laravel', 3, 0);

// The Laravel Framework

```

#### [`swap`](https://laravel.com/docs/12.x/strings#method-fluent-str-swap)
The `swap` method replaces multiple values in the string using PHP's `strtr` function:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('Tacos are great!')




4    ->swap([




5        'Tacos' => 'Burritos',




6        'great' => 'fantastic',




7    ]);




8 



9// Burritos are fantastic!




use Illuminate\Support\Str;

$string = Str::of('Tacos are great!')
    ->swap([
        'Tacos' => 'Burritos',
        'great' => 'fantastic',
    ]);

// Burritos are fantastic!

```

#### [`take`](https://laravel.com/docs/12.x/strings#method-fluent-str-take)
The `take` method returns a specified number of characters from the beginning of the string:
```


1use Illuminate\Support\Str;




2 



3$taken = Str::of('Build something amazing!')->take(5);




4 



5// Build




use Illuminate\Support\Str;

$taken = Str::of('Build something amazing!')->take(5);

// Build

```

#### [`tap`](https://laravel.com/docs/12.x/strings#method-fluent-str-tap)
The `tap` method passes the string to the given closure, allowing you to examine and interact with the string while not affecting the string itself. The original string is returned by the `tap` method regardless of what is returned by the closure:
```


 1use Illuminate\Support\Str;




 2use Illuminate\Support\Stringable;




 3 



 4$string = Str::of('Laravel')




 5    ->append(' Framework')




 6    ->tap(function (Stringable $string) {




 7        dump('String after append: '.$string);




 8    })




 9    ->upper();




10 



11// LARAVEL FRAMEWORK




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('Laravel')
    ->append(' Framework')
    ->tap(function (Stringable $string) {
        dump('String after append: '.$string);
    })
    ->upper();

// LARAVEL FRAMEWORK

```

#### [`test`](https://laravel.com/docs/12.x/strings#method-fluent-str-test)
The `test` method determines if a string matches the given regular expression pattern:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('Laravel Framework')->test('/Laravel/');




4 



5// true




use Illuminate\Support\Str;

$result = Str::of('Laravel Framework')->test('/Laravel/');

// true

```

#### [`title`](https://laravel.com/docs/12.x/strings#method-fluent-str-title)
The `title` method converts the given string to `Title Case`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::of('a nice title uses the correct case')->title();




4 



5// A Nice Title Uses The Correct Case




use Illuminate\Support\Str;

$converted = Str::of('a nice title uses the correct case')->title();

// A Nice Title Uses The Correct Case

```

#### [`toBase64`](https://laravel.com/docs/12.x/strings#method-fluent-str-to-base64)
The `toBase64` method converts the given string to Base64:
```


1use Illuminate\Support\Str;




2 



3$base64 = Str::of('Laravel')->toBase64();




4 



5// TGFyYXZlbA==




use Illuminate\Support\Str;

$base64 = Str::of('Laravel')->toBase64();

// TGFyYXZlbA==

```

#### [`toHtmlString`](https://laravel.com/docs/12.x/strings#method-fluent-str-to-html-string)
The `toHtmlString` method converts the given string to an instance of `Illuminate\Support\HtmlString`, which will not be escaped when rendered in Blade templates:
```


1use Illuminate\Support\Str;




2 



3$htmlString = Str::of('Nuno Maduro')->toHtmlString();




use Illuminate\Support\Str;

$htmlString = Str::of('Nuno Maduro')->toHtmlString();

```

#### [`toUri`](https://laravel.com/docs/12.x/strings#method-fluent-str-to-uri)
The `toUri` method converts the given string to an instance of [Illuminate\Support\Uri](https://laravel.com/docs/12.x/helpers#uri):
```


1use Illuminate\Support\Str;




2 



3$uri = Str::of('https://example.com')->toUri();




use Illuminate\Support\Str;

$uri = Str::of('https://example.com')->toUri();

```

#### [`transliterate`](https://laravel.com/docs/12.x/strings#method-fluent-str-transliterate)
The `transliterate` method will attempt to convert a given string into its closest ASCII representation:
```


1use Illuminate\Support\Str;




2 



3$email = Str::of('ⓣⓔⓢⓣ@ⓛⓐⓡⓐⓥⓔⓛ.ⓒⓞⓜ')->transliterate()




4 



5// 'test@laravel.com'




use Illuminate\Support\Str;

$email = Str::of('ⓣⓔⓢⓣ@ⓛⓐⓡⓐⓥⓔⓛ.ⓒⓞⓜ')->transliterate()

// 'test@laravel.com'

```

#### [`trim`](https://laravel.com/docs/12.x/strings#method-fluent-str-trim)
The `trim` method trims the given string. Unlike PHP's native `trim` function, Laravel's `trim` method also removes unicode whitespace characters:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('  Laravel  ')->trim();




4 



5// 'Laravel'




6 



7$string = Str::of('/Laravel/')->trim('/');




8 



9// 'Laravel'




use Illuminate\Support\Str;

$string = Str::of('  Laravel  ')->trim();

// 'Laravel'

$string = Str::of('/Laravel/')->trim('/');

// 'Laravel'

```

#### [`ltrim`](https://laravel.com/docs/12.x/strings#method-fluent-str-ltrim)
The `ltrim` method trims the left side of the string. Unlike PHP's native `ltrim` function, Laravel's `ltrim` method also removes unicode whitespace characters:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('  Laravel  ')->ltrim();




4 



5// 'Laravel  '




6 



7$string = Str::of('/Laravel/')->ltrim('/');




8 



9// 'Laravel/'




use Illuminate\Support\Str;

$string = Str::of('  Laravel  ')->ltrim();

// 'Laravel  '

$string = Str::of('/Laravel/')->ltrim('/');

// 'Laravel/'

```

#### [`rtrim`](https://laravel.com/docs/12.x/strings#method-fluent-str-rtrim)
The `rtrim` method trims the right side of the given string. Unlike PHP's native `rtrim` function, Laravel's `rtrim` method also removes unicode whitespace characters:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('  Laravel  ')->rtrim();




4 



5// '  Laravel'




6 



7$string = Str::of('/Laravel/')->rtrim('/');




8 



9// '/Laravel'




use Illuminate\Support\Str;

$string = Str::of('  Laravel  ')->rtrim();

// '  Laravel'

$string = Str::of('/Laravel/')->rtrim('/');

// '/Laravel'

```

#### [`ucfirst`](https://laravel.com/docs/12.x/strings#method-fluent-str-ucfirst)
The `ucfirst` method returns the given string with the first character capitalized:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('foo bar')->ucfirst();




4 



5// Foo bar




use Illuminate\Support\Str;

$string = Str::of('foo bar')->ucfirst();

// Foo bar

```

#### [`ucsplit`](https://laravel.com/docs/12.x/strings#method-fluent-str-ucsplit)
The `ucsplit` method splits the given string into a collection by uppercase characters:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('Foo Bar')->ucsplit();




4 



5// collect(['Foo ', 'Bar'])




use Illuminate\Support\Str;

$string = Str::of('Foo Bar')->ucsplit();

// collect(['Foo ', 'Bar'])

```

#### [`ucwords`](https://laravel.com/docs/12.x/strings#method-fluent-str-ucwords)
The `ucwords` method converts the first character of each word in the given string to uppercase:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('laravel framework')->ucwords();




4 



5// Laravel Framework




use Illuminate\Support\Str;

$string = Str::of('laravel framework')->ucwords();

// Laravel Framework

```

#### [`unwrap`](https://laravel.com/docs/12.x/strings#method-fluent-str-unwrap)
The `unwrap` method removes the specified strings from the beginning and end of a given string:
```


1use Illuminate\Support\Str;




2 



3Str::of('-Laravel-')->unwrap('-');




4 



5// Laravel




6 



7Str::of('{framework: "Laravel"}')->unwrap('{', '}');




8 



9// framework: "Laravel"




use Illuminate\Support\Str;

Str::of('-Laravel-')->unwrap('-');

// Laravel

Str::of('{framework: "Laravel"}')->unwrap('{', '}');

// framework: "Laravel"

```

#### [`upper`](https://laravel.com/docs/12.x/strings#method-fluent-str-upper)
The `upper` method converts the given string to uppercase:
```


1use Illuminate\Support\Str;




2 



3$adjusted = Str::of('laravel')->upper();




4 



5// LARAVEL




use Illuminate\Support\Str;

$adjusted = Str::of('laravel')->upper();

// LARAVEL

```

#### [`when`](https://laravel.com/docs/12.x/strings#method-fluent-str-when)
The `when` method invokes the given closure if a given condition is `true`. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('Taylor')




5    ->when(true, function (Stringable $string) {




6        return $string->append(' Otwell');




7    });




8 



9// 'Taylor Otwell'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('Taylor')
    ->when(true, function (Stringable $string) {
        return $string->append(' Otwell');
    });

// 'Taylor Otwell'

```

If necessary, you may pass another closure as the third parameter to the `when` method. This closure will execute if the condition parameter evaluates to `false`.
#### [`whenContains`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-contains)
The `whenContains` method invokes the given closure if the string contains the given value. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('tony stark')




5    ->whenContains('tony', function (Stringable $string) {




6        return $string->title();




7    });




8 



9// 'Tony Stark'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('tony stark')
    ->whenContains('tony', function (Stringable $string) {
        return $string->title();
    });

// 'Tony Stark'

```

If necessary, you may pass another closure as the third parameter. The closure will be invoked if the string does not contain the given value.
You may also pass an array of values to determine if the given string contains any of the values in the array:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('tony stark')




5    ->whenContains(['tony', 'hulk'], function (Stringable $string) {




6        return $string->title();




7    });




8 



9// Tony Stark




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('tony stark')
    ->whenContains(['tony', 'hulk'], function (Stringable $string) {
        return $string->title();
    });

// Tony Stark

```

#### [`whenContainsAll`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-contains-all)
The `whenContainsAll` method invokes the given closure if the string contains all of the given sub-strings. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('tony stark')




5    ->whenContainsAll(['tony', 'stark'], function (Stringable $string) {




6        return $string->title();




7    });




8 



9// 'Tony Stark'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('tony stark')
    ->whenContainsAll(['tony', 'stark'], function (Stringable $string) {
        return $string->title();
    });

// 'Tony Stark'

```

If necessary, you may pass another closure as the third parameter. The closure will be invoked if the condition parameter evaluates to `false`.
#### [`whenDoesntEndWith`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-doesnt-end-with)
The `whenDoesntEndWith` method invokes the given closure if the string doesn't end with the given sub-string. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('disney world')->whenDoesntEndWith('land', function (Stringable $string) {




5    return $string->title();




6});




7 



8// 'Disney World'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('disney world')->whenDoesntEndWith('land', function (Stringable $string) {
    return $string->title();
});

// 'Disney World'

```

#### [`whenDoesntStartWith`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-doesnt-start-with)
The `whenDoesntStartWith` method invokes the given closure if the string doesn't start with the given sub-string. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('disney world')->whenDoesntStartWith('sea', function (Stringable $string) {




5    return $string->title();




6});




7 



8// 'Disney World'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('disney world')->whenDoesntStartWith('sea', function (Stringable $string) {
    return $string->title();
});

// 'Disney World'

```

#### [`whenEmpty`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-empty)
The `whenEmpty` method invokes the given closure if the string is empty. If the closure returns a value, that value will also be returned by the `whenEmpty` method. If the closure does not return a value, the fluent string instance will be returned:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('  ')->trim()->whenEmpty(function (Stringable $string) {




5    return $string->prepend('Laravel');




6});




7 



8// 'Laravel'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('  ')->trim()->whenEmpty(function (Stringable $string) {
    return $string->prepend('Laravel');
});

// 'Laravel'

```

#### [`whenNotEmpty`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-not-empty)
The `whenNotEmpty` method invokes the given closure if the string is not empty. If the closure returns a value, that value will also be returned by the `whenNotEmpty` method. If the closure does not return a value, the fluent string instance will be returned:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('Framework')->whenNotEmpty(function (Stringable $string) {




5    return $string->prepend('Laravel ');




6});




7 



8// 'Laravel Framework'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('Framework')->whenNotEmpty(function (Stringable $string) {
    return $string->prepend('Laravel ');
});

// 'Laravel Framework'

```

#### [`whenStartsWith`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-starts-with)
The `whenStartsWith` method invokes the given closure if the string starts with the given sub-string. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('disney world')->whenStartsWith('disney', function (Stringable $string) {




5    return $string->title();




6});




7 



8// 'Disney World'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('disney world')->whenStartsWith('disney', function (Stringable $string) {
    return $string->title();
});

// 'Disney World'

```

#### [`whenEndsWith`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-ends-with)
The `whenEndsWith` method invokes the given closure if the string ends with the given sub-string. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('disney world')->whenEndsWith('world', function (Stringable $string) {




5    return $string->title();




6});




7 



8// 'Disney World'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('disney world')->whenEndsWith('world', function (Stringable $string) {
    return $string->title();
});

// 'Disney World'

```

#### [`whenExactly`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-exactly)
The `whenExactly` method invokes the given closure if the string exactly matches the given string. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('laravel')->whenExactly('laravel', function (Stringable $string) {




5    return $string->title();




6});




7 



8// 'Laravel'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('laravel')->whenExactly('laravel', function (Stringable $string) {
    return $string->title();
});

// 'Laravel'

```

#### [`whenNotExactly`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-not-exactly)
The `whenNotExactly` method invokes the given closure if the string does not exactly match the given string. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('framework')->whenNotExactly('laravel', function (Stringable $string) {




5    return $string->title();




6});




7 



8// 'Framework'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('framework')->whenNotExactly('laravel', function (Stringable $string) {
    return $string->title();
});

// 'Framework'

```

#### [`whenIs`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-is)
The `whenIs` method invokes the given closure if the string matches a given pattern. Asterisks may be used as wildcard values. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('foo/bar')->whenIs('foo/*', function (Stringable $string) {




5    return $string->append('/baz');




6});




7 



8// 'foo/bar/baz'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('foo/bar')->whenIs('foo/*', function (Stringable $string) {
    return $string->append('/baz');
});

// 'foo/bar/baz'

```

#### [`whenIsAscii`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-is-ascii)
The `whenIsAscii` method invokes the given closure if the string is 7 bit ASCII. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('laravel')->whenIsAscii(function (Stringable $string) {




5    return $string->title();




6});




7 



8// 'Laravel'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('laravel')->whenIsAscii(function (Stringable $string) {
    return $string->title();
});

// 'Laravel'

```

#### [`whenIsUlid`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-is-ulid)
The `whenIsUlid` method invokes the given closure if the string is a valid ULID. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('01gd6r360bp37zj17nxb55yv40')->whenIsUlid(function (Stringable $string) {




4    return $string->substr(0, 8);




5});




6 



7// '01gd6r36'




use Illuminate\Support\Str;

$string = Str::of('01gd6r360bp37zj17nxb55yv40')->whenIsUlid(function (Stringable $string) {
    return $string->substr(0, 8);
});

// '01gd6r36'

```

#### [`whenIsUuid`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-is-uuid)
The `whenIsUuid` method invokes the given closure if the string is a valid UUID. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('a0a2a2d2-0b87-4a18-83f2-2529882be2de')->whenIsUuid(function (Stringable $string) {




5    return $string->substr(0, 8);




6});




7 



8// 'a0a2a2d2'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('a0a2a2d2-0b87-4a18-83f2-2529882be2de')->whenIsUuid(function (Stringable $string) {
    return $string->substr(0, 8);
});

// 'a0a2a2d2'

```

#### [`whenTest`](https://laravel.com/docs/12.x/strings#method-fluent-str-when-test)
The `whenTest` method invokes the given closure if the string matches the given regular expression. The closure will receive the fluent string instance:
```


1use Illuminate\Support\Str;




2use Illuminate\Support\Stringable;




3 



4$string = Str::of('laravel framework')->whenTest('/laravel/', function (Stringable $string) {




5    return $string->title();




6});




7 



8// 'Laravel Framework'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$string = Str::of('laravel framework')->whenTest('/laravel/', function (Stringable $string) {
    return $string->title();
});

// 'Laravel Framework'

```

#### [`wordCount`](https://laravel.com/docs/12.x/strings#method-fluent-str-word-count)
The `wordCount` method returns the number of words that a string contains:
```


1use Illuminate\Support\Str;




2 



3Str::of('Hello, world!')->wordCount(); // 2




use Illuminate\Support\Str;

Str::of('Hello, world!')->wordCount(); // 2

```

#### [`words`](https://laravel.com/docs/12.x/strings#method-fluent-str-words)
The `words` method limits the number of words in a string. If necessary, you may specify an additional string that will be appended to the truncated string:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('Perfectly balanced, as all things should be.')->words(3, ' >>>');




4 



5// Perfectly balanced, as >>>




use Illuminate\Support\Str;

$string = Str::of('Perfectly balanced, as all things should be.')->words(3, ' >>>');

// Perfectly balanced, as >>>

```

#### [`wrap`](https://laravel.com/docs/12.x/strings#method-fluent-str-wrap)
The `wrap` method wraps the given string with an additional string or pair of strings:
```


1use Illuminate\Support\Str;




2 



3Str::of('Laravel')->wrap('"');




4 



5// "Laravel"




6 



7Str::is('is')->wrap(before: 'This ', after: ' Laravel!');




8 



9// This is Laravel!




use Illuminate\Support\Str;

Str::of('Laravel')->wrap('"');

// "Laravel"

Str::is('is')->wrap(before: 'This ', after: ' Laravel!');

// This is Laravel!

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/strings#introduction)
  * [ Available Methods ](https://laravel.com/docs/12.x/strings#available-methods)


[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
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
  *   * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Jump24](https://partners.laravel.com/partners/jump24)
