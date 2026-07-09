```


 1use Illuminate\Support\Str;




 2 



 3$html = Str::markdown('# Laravel');




 4 



 5// <h1>Laravel</h1>




 6 



 7$html = Str::markdown('# Taylor <b>Otwell</b>', [




 8    'html_input' => 'strip',




 9]);




10 



11// <h1>Taylor Otwell</h1>




use Illuminate\Support\Str;

$html = Str::markdown('# Laravel');

// <h1>Laravel</h1>

$html = Str::markdown('# Taylor <b>Otwell</b>', [
    'html_input' => 'strip',
]);

// <h1>Taylor Otwell</h1>

```

#### Markdown Security
By default, Markdown supports raw HTML, which will expose Cross-Site Scripting (XSS) vulnerabilities when used with raw user input. As per the `html_input` option to either escape or strip raw HTML, and the `allow_unsafe_links` option to specify whether to allow unsafe links. If you need to allow some raw HTML, you should pass your compiled Markdown through an HTML Purifier:
```


1use Illuminate\Support\Str;




2 



3Str::markdown('Inject: <script>alert("Hello XSS!");</script>', [




4    'html_input' => 'strip',




5    'allow_unsafe_links' => false,




6]);




7 



8// <p>Inject: alert(&quot;Hello XSS!&quot;);</p>




use Illuminate\Support\Str;

Str::markdown('Inject: <script>alert("Hello XSS!");</script>', [
    'html_input' => 'strip',
    'allow_unsafe_links' => false,
]);

// <p>Inject: alert(&quot;Hello XSS!&quot;);</p>

```

#### [`Str::mask()`](https://laravel.com/docs/12.x/strings#method-str-mask)
The `Str::mask` method masks a portion of a string with a repeated character, and may be used to obfuscate segments of strings such as email addresses and phone numbers:
```


1use Illuminate\Support\Str;




2 



3$string = Str::mask('taylor@example.com', '*', 3);




4 



5// tay***************




use Illuminate\Support\Str;

$string = Str::mask('taylor@example.com', '*', 3);

// tay***************

```

If needed, you provide a negative number as the third argument to the `mask` method, which will instruct the method to begin masking at the given distance from the end of the string:
```


1$string = Str::mask('taylor@example.com', '*', -15, 3);




2 



3// tay***@example.com




$string = Str::mask('taylor@example.com', '*', -15, 3);

// tay***@example.com

```

#### [`Str::match()`](https://laravel.com/docs/12.x/strings#method-str-match)
The `Str::match` method will return the portion of a string that matches a given regular expression pattern:
```


1use Illuminate\Support\Str;




2 



3$result = Str::match('/bar/', 'foo bar');




4 



5// 'bar'




6 



7$result = Str::match('/foo (.*)/', 'foo bar');




8 



9// 'bar'




use Illuminate\Support\Str;

$result = Str::match('/bar/', 'foo bar');

// 'bar'

$result = Str::match('/foo (.*)/', 'foo bar');

// 'bar'

```

#### [`Str::matchAll()`](https://laravel.com/docs/12.x/strings#method-str-match-all)
The `Str::matchAll` method will return a collection containing the portions of a string that match a given regular expression pattern:
```


1use Illuminate\Support\Str;




2 



3$result = Str::matchAll('/bar/', 'bar foo bar');




4 



5// collect(['bar', 'bar'])




use Illuminate\Support\Str;

$result = Str::matchAll('/bar/', 'bar foo bar');

// collect(['bar', 'bar'])

```

If you specify a matching group within the expression, Laravel will return a collection of the first matching group's matches:
```


1use Illuminate\Support\Str;




2 



3$result = Str::matchAll('/f(\w*)/', 'bar fun bar fly');




4 



5// collect(['un', 'ly']);




use Illuminate\Support\Str;

$result = Str::matchAll('/f(\w*)/', 'bar fun bar fly');

// collect(['un', 'ly']);

```

If no matches are found, an empty collection will be returned.
#### [`Str::isMatch()`](https://laravel.com/docs/12.x/strings#method-str-is-match)
The `Str::isMatch` method will return `true` if the string matches a given regular expression:
```


1use Illuminate\Support\Str;




2 



3$result = Str::isMatch('/foo (.*)/', 'foo bar');




4 



5// true




6 



7$result = Str::isMatch('/foo (.*)/', 'laravel');




8 



9// false




use Illuminate\Support\Str;

$result = Str::isMatch('/foo (.*)/', 'foo bar');

// true

$result = Str::isMatch('/foo (.*)/', 'laravel');

// false

```

#### [`Str::orderedUuid()`](https://laravel.com/docs/12.x/strings#method-str-ordered-uuid)
The `Str::orderedUuid` method generates a "timestamp first" UUID that may be efficiently stored in an indexed database column. Each UUID that is generated using this method will be sorted after UUIDs previously generated using the method:
```


1use Illuminate\Support\Str;




2 



3return (string) Str::orderedUuid();




use Illuminate\Support\Str;

return (string) Str::orderedUuid();

```

#### [`Str::padBoth()`](https://laravel.com/docs/12.x/strings#method-str-padboth)
The `Str::padBoth` method wraps PHP's `str_pad` function, padding both sides of a string with another string until the final string reaches a desired length:
```


1use Illuminate\Support\Str;




2 



3$padded = Str::padBoth('James', 10, '_');




4 



5// '__James___'




6 



7$padded = Str::padBoth('James', 10);




8 



9// '  James   '




use Illuminate\Support\Str;

$padded = Str::padBoth('James', 10, '_');

// '__James___'

$padded = Str::padBoth('James', 10);

// '  James   '

```

#### [`Str::padLeft()`](https://laravel.com/docs/12.x/strings#method-str-padleft)
The `Str::padLeft` method wraps PHP's `str_pad` function, padding the left side of a string with another string until the final string reaches a desired length:
```


1use Illuminate\Support\Str;




2 



3$padded = Str::padLeft('James', 10, '-=');




4 



5// '-=-=-James'




6 



7$padded = Str::padLeft('James', 10);




8 



9// '     James'




use Illuminate\Support\Str;

$padded = Str::padLeft('James', 10, '-=');

// '-=-=-James'

$padded = Str::padLeft('James', 10);

// '     James'

```

#### [`Str::padRight()`](https://laravel.com/docs/12.x/strings#method-str-padright)
The `Str::padRight` method wraps PHP's `str_pad` function, padding the right side of a string with another string until the final string reaches a desired length:
```


1use Illuminate\Support\Str;




2 



3$padded = Str::padRight('James', 10, '-');




4 



5// 'James-----'




6 



7$padded = Str::padRight('James', 10);




8 



9// 'James     '




use Illuminate\Support\Str;

$padded = Str::padRight('James', 10, '-');

// 'James-----'

$padded = Str::padRight('James', 10);

// 'James     '

```

#### [`Str::password()`](https://laravel.com/docs/12.x/strings#method-str-password)
The `Str::password` method may be used to generate a secure, random password of a given length. The password will consist of a combination of letters, numbers, symbols, and spaces. By default, passwords are 32 characters long:
```


1use Illuminate\Support\Str;




2 



3$password = Str::password();




4 



5// 'EbJo2vE-AS:U,$%_gkrV4n,q~1xy/-_4'




6 



7$password = Str::password(12);




8 



9// 'qwuar>#V|i]N'




use Illuminate\Support\Str;

$password = Str::password();

// 'EbJo2vE-AS:U,$%_gkrV4n,q~1xy/-_4'

$password = Str::password(12);

// 'qwuar>#V|i]N'

```

#### [`Str::plural()`](https://laravel.com/docs/12.x/strings#method-str-plural)
The `Str::plural` method converts a singular word string to its plural form. This function supports [any of the languages supported by Laravel's pluralizer](https://laravel.com/docs/12.x/localization#pluralization-language):
```


1use Illuminate\Support\Str;




2 



3$plural = Str::plural('car');




4 



5// cars




6 



7$plural = Str::plural('child');




8 



9// children




use Illuminate\Support\Str;

$plural = Str::plural('car');

// cars

$plural = Str::plural('child');

// children

```

You may provide an integer as a second argument to the function to retrieve the singular or plural form of the string:
```


1use Illuminate\Support\Str;




2 



3$plural = Str::plural('child', 2);




4 



5// children




6 



7$singular = Str::plural('child', 1);




8 



9// child




use Illuminate\Support\Str;

$plural = Str::plural('child', 2);

// children

$singular = Str::plural('child', 1);

// child

```

The `prependCount` argument may be provided to prefix the pluralized string with the formatted `$count`:
```


1use Illuminate\Support\Str;




2 



3$label = Str::plural('car', 1000, prependCount: true);




4 



5// 1,000 cars




use Illuminate\Support\Str;

$label = Str::plural('car', 1000, prependCount: true);

// 1,000 cars

```

#### [`Str::pluralStudly()`](https://laravel.com/docs/12.x/strings#method-str-plural-studly)
The `Str::pluralStudly` method converts a singular word string formatted in studly caps case to its plural form. This function supports [any of the languages supported by Laravel's pluralizer](https://laravel.com/docs/12.x/localization#pluralization-language):
```


1use Illuminate\Support\Str;




2 



3$plural = Str::pluralStudly('VerifiedHuman');




4 



5// VerifiedHumans




6 



7$plural = Str::pluralStudly('UserFeedback');




8 



9// UserFeedback




use Illuminate\Support\Str;

$plural = Str::pluralStudly('VerifiedHuman');

// VerifiedHumans

$plural = Str::pluralStudly('UserFeedback');

// UserFeedback

```

You may provide an integer as a second argument to the function to retrieve the singular or plural form of the string:
```


1use Illuminate\Support\Str;




2 



3$plural = Str::pluralStudly('VerifiedHuman', 2);




4 



5// VerifiedHumans




6 



7$singular = Str::pluralStudly('VerifiedHuman', 1);




8 



9// VerifiedHuman




use Illuminate\Support\Str;

$plural = Str::pluralStudly('VerifiedHuman', 2);

// VerifiedHumans

$singular = Str::pluralStudly('VerifiedHuman', 1);

// VerifiedHuman

```

#### [`Str::position()`](https://laravel.com/docs/12.x/strings#method-str-position)
The `Str::position` method returns the position of the first occurrence of a substring in a string. If the substring does not exist in the given string, `false` is returned:
```


1use Illuminate\Support\Str;




2 



3$position = Str::position('Hello, World!', 'Hello');




4 



5// 0




6 



7$position = Str::position('Hello, World!', 'W');




8 



9// 7




use Illuminate\Support\Str;

$position = Str::position('Hello, World!', 'Hello');

// 0

$position = Str::position('Hello, World!', 'W');

// 7

```

#### [`Str::random()`](https://laravel.com/docs/12.x/strings#method-str-random)
The `Str::random` method generates a random string of the specified length. This function uses PHP's `random_bytes` function:
```


1use Illuminate\Support\Str;




2 



3$random = Str::random(40);




use Illuminate\Support\Str;

$random = Str::random(40);

```

During testing, it may be useful to "fake" the value that is returned by the `Str::random` method. To accomplish this, you may use the `createRandomStringsUsing` method:
```


1Str::createRandomStringsUsing(function () {




2    return 'fake-random-string';




3});




Str::createRandomStringsUsing(function () {
    return 'fake-random-string';
});

```

To instruct the `random` method to return to generating random strings normally, you may invoke the `createRandomStringsNormally` method:
```


1Str::createRandomStringsNormally();




Str::createRandomStringsNormally();

```

#### [`Str::remove()`](https://laravel.com/docs/12.x/strings#method-str-remove)
The `Str::remove` method removes the given value or array of values from the string:
```


1use Illuminate\Support\Str;




2 



3$string = 'Peter Piper picked a peck of pickled peppers.';




4 



5$removed = Str::remove('e', $string);




6 



7// Ptr Pipr pickd a pck of pickld ppprs.




use Illuminate\Support\Str;

$string = 'Peter Piper picked a peck of pickled peppers.';

$removed = Str::remove('e', $string);

// Ptr Pipr pickd a pck of pickld ppprs.

```

You may also pass `false` as a third argument to the `remove` method to ignore case when removing strings.
#### [`Str::repeat()`](https://laravel.com/docs/12.x/strings#method-str-repeat)
The `Str::repeat` method repeats the given string:
```


1use Illuminate\Support\Str;




2 



3$string = 'a';




4 



5$repeat = Str::repeat($string, 5);




6 



7// aaaaa




use Illuminate\Support\Str;

$string = 'a';

$repeat = Str::repeat($string, 5);

// aaaaa

```

#### [`Str::replace()`](https://laravel.com/docs/12.x/strings#method-str-replace)
The `Str::replace` method replaces a given string within the string:
```


1use Illuminate\Support\Str;




2 



3$string = 'Laravel 11.x';




4 



5$replaced = Str::replace('11.x', '12.x', $string);




6 



7// Laravel 12.x




use Illuminate\Support\Str;

$string = 'Laravel 11.x';

$replaced = Str::replace('11.x', '12.x', $string);

// Laravel 12.x

```

The `replace` method also accepts a `caseSensitive` argument. By default, the `replace` method is case sensitive:
```


1$replaced = Str::replace(




2    'php',




3    'Laravel',




4    'PHP Framework for Web Artisans',




5    caseSensitive: false




6);




7 



8// Laravel Framework for Web Artisans




$replaced = Str::replace(
    'php',
    'Laravel',
    'PHP Framework for Web Artisans',
    caseSensitive: false
);

// Laravel Framework for Web Artisans

```

#### [`Str::replaceArray()`](https://laravel.com/docs/12.x/strings#method-str-replace-array)
The `Str::replaceArray` method replaces a given value in the string sequentially using an array:
```


1use Illuminate\Support\Str;




2 



3$string = 'The event will take place between ? and ?';




4 



5$replaced = Str::replaceArray('?', ['8:30', '9:00'], $string);




6 



7// The event will take place between 8:30 and 9:00




use Illuminate\Support\Str;

$string = 'The event will take place between ? and ?';

$replaced = Str::replaceArray('?', ['8:30', '9:00'], $string);

// The event will take place between 8:30 and 9:00

```

#### [`Str::replaceFirst()`](https://laravel.com/docs/12.x/strings#method-str-replace-first)
The `Str::replaceFirst` method replaces the first occurrence of a given value in a string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::replaceFirst('the', 'a', 'the quick brown fox jumps over the lazy dog');




4 



5// a quick brown fox jumps over the lazy dog




use Illuminate\Support\Str;

$replaced = Str::replaceFirst('the', 'a', 'the quick brown fox jumps over the lazy dog');

// a quick brown fox jumps over the lazy dog

```

#### [`Str::replaceLast()`](https://laravel.com/docs/12.x/strings#method-str-replace-last)
The `Str::replaceLast` method replaces the last occurrence of a given value in a string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::replaceLast('the', 'a', 'the quick brown fox jumps over the lazy dog');




4 



5// the quick brown fox jumps over a lazy dog




use Illuminate\Support\Str;

$replaced = Str::replaceLast('the', 'a', 'the quick brown fox jumps over the lazy dog');

// the quick brown fox jumps over a lazy dog

```

#### [`Str::replaceMatches()`](https://laravel.com/docs/12.x/strings#method-str-replace-matches)
The `Str::replaceMatches` method replaces all portions of a string matching a pattern with the given replacement string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::replaceMatches(




4    pattern: '/[^A-Za-z0-9]++/',




5    replace: '',




6    subject: '(+1) 501-555-1000'




7)




8 



9// '15015551000'




use Illuminate\Support\Str;

$replaced = Str::replaceMatches(
    pattern: '/[^A-Za-z0-9]++/',
    replace: '',
    subject: '(+1) 501-555-1000'
)

// '15015551000'

```

The `replaceMatches` method also accepts a closure that will be invoked with each portion of the string matching the given pattern, allowing you to perform the replacement logic within the closure and return the replaced value:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::replaceMatches('/\d/', function (array $matches) {




4    return '['.$matches[0].']';




5}, '123');




6 



7// '[1][2][3]'




use Illuminate\Support\Str;

$replaced = Str::replaceMatches('/\d/', function (array $matches) {
    return '['.$matches[0].']';
}, '123');

// '[1][2][3]'

```

#### [`Str::replaceStart()`](https://laravel.com/docs/12.x/strings#method-str-replace-start)
The `Str::replaceStart` method replaces the first occurrence of the given value only if the value appears at the start of the string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::replaceStart('Hello', 'Laravel', 'Hello World');




4 



5// Laravel World




6 



7$replaced = Str::replaceStart('World', 'Laravel', 'Hello World');




8 



9// Hello World




use Illuminate\Support\Str;

$replaced = Str::replaceStart('Hello', 'Laravel', 'Hello World');

// Laravel World

$replaced = Str::replaceStart('World', 'Laravel', 'Hello World');

// Hello World

```

#### [`Str::replaceEnd()`](https://laravel.com/docs/12.x/strings#method-str-replace-end)
The `Str::replaceEnd` method replaces the last occurrence of the given value only if the value appears at the end of the string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::replaceEnd('World', 'Laravel', 'Hello World');




4 



5// Hello Laravel




6 



7$replaced = Str::replaceEnd('Hello', 'Laravel', 'Hello World');




8 



9// Hello World




use Illuminate\Support\Str;

$replaced = Str::replaceEnd('World', 'Laravel', 'Hello World');

// Hello Laravel

$replaced = Str::replaceEnd('Hello', 'Laravel', 'Hello World');

// Hello World

```

#### [`Str::reverse()`](https://laravel.com/docs/12.x/strings#method-str-reverse)
The `Str::reverse` method reverses the given string:
```


1use Illuminate\Support\Str;




2 



3$reversed = Str::reverse('Hello World');




4 



5// dlroW olleH




use Illuminate\Support\Str;

$reversed = Str::reverse('Hello World');

// dlroW olleH

```

#### [`Str::singular()`](https://laravel.com/docs/12.x/strings#method-str-singular)
The `Str::singular` method converts a string to its singular form. This function supports [any of the languages supported by Laravel's pluralizer](https://laravel.com/docs/12.x/localization#pluralization-language):
```


1use Illuminate\Support\Str;




2 



3$singular = Str::singular('cars');




4 



5// car




6 



7$singular = Str::singular('children');




8 



9// child




use Illuminate\Support\Str;

$singular = Str::singular('cars');

// car

$singular = Str::singular('children');

// child

```

#### [`Str::slug()`](https://laravel.com/docs/12.x/strings#method-str-slug)
The `Str::slug` method generates a URL friendly "slug" from the given string:
```


1use Illuminate\Support\Str;




2 



3$slug = Str::slug('Laravel 5 Framework', '-');




4 



5// laravel-5-framework




use Illuminate\Support\Str;

$slug = Str::slug('Laravel 5 Framework', '-');

// laravel-5-framework

```

#### [`Str::snake()`](https://laravel.com/docs/12.x/strings#method-snake-case)
The `Str::snake` method converts the given string to `snake_case`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::snake('fooBar');




4 



5// foo_bar




6 



7$converted = Str::snake('fooBar', '-');




8 



9// foo-bar




use Illuminate\Support\Str;

$converted = Str::snake('fooBar');

// foo_bar

$converted = Str::snake('fooBar', '-');

// foo-bar

```

#### [`Str::squish()`](https://laravel.com/docs/12.x/strings#method-str-squish)
The `Str::squish` method removes all extraneous white space from a string, including extraneous white space between words:
```


1use Illuminate\Support\Str;




2 



3$string = Str::squish('    laravel    framework    ');




4 



5// laravel framework




use Illuminate\Support\Str;

$string = Str::squish('    laravel    framework    ');

// laravel framework

```

#### [`Str::start()`](https://laravel.com/docs/12.x/strings#method-str-start)
The `Str::start` method adds a single instance of the given value to a string if it does not already start with that value:
```


1use Illuminate\Support\Str;




2 



3$adjusted = Str::start('this/string', '/');




4 



5// /this/string




6 



7$adjusted = Str::start('/this/string', '/');




8 



9// /this/string




use Illuminate\Support\Str;

$adjusted = Str::start('this/string', '/');

// /this/string

$adjusted = Str::start('/this/string', '/');

// /this/string

```

#### [`Str::startsWith()`](https://laravel.com/docs/12.x/strings#method-starts-with)
The `Str::startsWith` method determines if the given string begins with the given value:
```


1use Illuminate\Support\Str;




2 



3$result = Str::startsWith('This is my name', 'This');




4 



5// true




use Illuminate\Support\Str;

$result = Str::startsWith('This is my name', 'This');

// true

```

If an array of possible values is passed, the `startsWith` method will return `true` if the string begins with any of the given values:
```


1$result = Str::startsWith('This is my name', ['This', 'That', 'There']);




2 



3// true




$result = Str::startsWith('This is my name', ['This', 'That', 'There']);

// true

```

#### [`Str::studly()`](https://laravel.com/docs/12.x/strings#method-studly-case)
The `Str::studly` method converts the given string to `StudlyCase`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::studly('foo_bar');




4 



5// FooBar




use Illuminate\Support\Str;

$converted = Str::studly('foo_bar');

// FooBar

```

#### [`Str::substr()`](https://laravel.com/docs/12.x/strings#method-str-substr)
The `Str::substr` method returns the portion of string specified by the start and length parameters:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::substr('The Laravel Framework', 4, 7);




4 



5// Laravel




use Illuminate\Support\Str;

$converted = Str::substr('The Laravel Framework', 4, 7);

// Laravel

```

#### [`Str::substrCount()`](https://laravel.com/docs/12.x/strings#method-str-substrcount)
The `Str::substrCount` method returns the number of occurrences of a given value in the given string:
```


1use Illuminate\Support\Str;




2 



3$count = Str::substrCount('If you like ice cream, you will like snow cones.', 'like');




4 



5// 2




use Illuminate\Support\Str;

$count = Str::substrCount('If you like ice cream, you will like snow cones.', 'like');

// 2

```

#### [`Str::substrReplace()`](https://laravel.com/docs/12.x/strings#method-str-substrreplace)
The `Str::substrReplace` method replaces text within a portion of a string, starting at the position specified by the third argument and replacing the number of characters specified by the fourth argument. Passing `0` to the method's fourth argument will insert the string at the specified position without replacing any of the existing characters in the string:
```


1use Illuminate\Support\Str;




2 



3$result = Str::substrReplace('1300', ':', 2);




4// 13:




5 



6$result = Str::substrReplace('1300', ':', 2, 0);




7// 13:00




use Illuminate\Support\Str;

$result = Str::substrReplace('1300', ':', 2);
// 13:

$result = Str::substrReplace('1300', ':', 2, 0);
// 13:00

```

#### [`Str::swap()`](https://laravel.com/docs/12.x/strings#method-str-swap)
The `Str::swap` method replaces multiple values in the given string using PHP's `strtr` function:
```


1use Illuminate\Support\Str;




2 



3$string = Str::swap([




4    'Tacos' => 'Burritos',




5    'great' => 'fantastic',




6], 'Tacos are great!');




7 



8// Burritos are fantastic!




use Illuminate\Support\Str;

$string = Str::swap([
    'Tacos' => 'Burritos',
    'great' => 'fantastic',
], 'Tacos are great!');

// Burritos are fantastic!

```

#### [`Str::take()`](https://laravel.com/docs/12.x/strings#method-take)
The `Str::take` method returns a specified number of characters from the beginning of a string:
```


1use Illuminate\Support\Str;




2 



3$taken = Str::take('Build something amazing!', 5);




4 



5// Build




use Illuminate\Support\Str;

$taken = Str::take('Build something amazing!', 5);

// Build

```

#### [`Str::title()`](https://laravel.com/docs/12.x/strings#method-title-case)
The `Str::title` method converts the given string to `Title Case`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::title('a nice title uses the correct case');




4 



5// A Nice Title Uses The Correct Case




use Illuminate\Support\Str;

$converted = Str::title('a nice title uses the correct case');

// A Nice Title Uses The Correct Case

```

#### [`Str::toBase64()`](https://laravel.com/docs/12.x/strings#method-str-to-base64)
The `Str::toBase64` method converts the given string to Base64:
```


1use Illuminate\Support\Str;




2 



3$base64 = Str::toBase64('Laravel');




4 



5// TGFyYXZlbA==




use Illuminate\Support\Str;

$base64 = Str::toBase64('Laravel');

// TGFyYXZlbA==

```

#### [`Str::transliterate()`](https://laravel.com/docs/12.x/strings#method-str-transliterate)
The `Str::transliterate` method will attempt to convert a given string into its closest ASCII representation:
```


1use Illuminate\Support\Str;




2 



3$email = Str::transliterate('ⓣⓔⓢⓣ@ⓛⓐⓡⓐⓥⓔⓛ.ⓒⓞⓜ');




4 



5// 'test@laravel.com'




use Illuminate\Support\Str;

$email = Str::transliterate('ⓣⓔⓢⓣ@ⓛⓐⓡⓐⓥⓔⓛ.ⓒⓞⓜ');

// 'test@laravel.com'

```

#### [`Str::trim()`](https://laravel.com/docs/12.x/strings#method-str-trim)
The `Str::trim` method strips whitespace (or other characters) from the beginning and end of the given string. Unlike PHP's native `trim` function, the `Str::trim` method also removes unicode whitespace characters:
