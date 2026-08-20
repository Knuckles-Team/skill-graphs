```


1$result = Str::of('http://example.com')->isUrl(['http', 'https']);




$result = Str::of('http://example.com')->isUrl(['http', 'https']);

```

#### [`isUuid`](https://laravel.com/docs/12.x/strings#method-fluent-str-is-uuid)
The `isUuid` method determines if a given string is a UUID:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('5ace9ab9-e9cf-4ec6-a19d-5881212a452c')->isUuid();




4 



5// true




6 



7$result = Str::of('Taylor')->isUuid();




8 



9// false




use Illuminate\Support\Str;

$result = Str::of('5ace9ab9-e9cf-4ec6-a19d-5881212a452c')->isUuid();

// true

$result = Str::of('Taylor')->isUuid();

// false

```

You may also validate that the given UUID matches a UUID specification by version (1, 3, 4, 5, 6, 7, or 8):
```


1use Illuminate\Support\Str;




2 



3$isUuid = Str::of('a0a2a2d2-0b87-4a18-83f2-2529882be2de')->isUuid(version: 4);




4 



5// true




6 



7$isUuid = Str::of('a0a2a2d2-0b87-4a18-83f2-2529882be2de')->isUuid(version: 1);




8 



9// false




use Illuminate\Support\Str;

$isUuid = Str::of('a0a2a2d2-0b87-4a18-83f2-2529882be2de')->isUuid(version: 4);

// true

$isUuid = Str::of('a0a2a2d2-0b87-4a18-83f2-2529882be2de')->isUuid(version: 1);

// false

```

#### [`kebab`](https://laravel.com/docs/12.x/strings#method-fluent-str-kebab)
The `kebab` method converts the given string to `kebab-case`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::of('fooBar')->kebab();




4 



5// foo-bar




use Illuminate\Support\Str;

$converted = Str::of('fooBar')->kebab();

// foo-bar

```

#### [`lcfirst`](https://laravel.com/docs/12.x/strings#method-fluent-str-lcfirst)
The `lcfirst` method returns the given string with the first character lowercased:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('Foo Bar')->lcfirst();




4 



5// foo Bar




use Illuminate\Support\Str;

$string = Str::of('Foo Bar')->lcfirst();

// foo Bar

```

#### [`length`](https://laravel.com/docs/12.x/strings#method-fluent-str-length)
The `length` method returns the length of the given string:
```


1use Illuminate\Support\Str;




2 



3$length = Str::of('Laravel')->length();




4 



5// 7




use Illuminate\Support\Str;

$length = Str::of('Laravel')->length();

// 7

```

#### [`limit`](https://laravel.com/docs/12.x/strings#method-fluent-str-limit)
The `limit` method truncates the given string to the specified length:
```


1use Illuminate\Support\Str;




2 



3$truncated = Str::of('The quick brown fox jumps over the lazy dog')->limit(20);




4 



5// The quick brown fox...




use Illuminate\Support\Str;

$truncated = Str::of('The quick brown fox jumps over the lazy dog')->limit(20);

// The quick brown fox...

```

You may also pass a second argument to change the string that will be appended to the end of the truncated string:
```


1$truncated = Str::of('The quick brown fox jumps over the lazy dog')->limit(20, ' (...)');




2 



3// The quick brown fox (...)




$truncated = Str::of('The quick brown fox jumps over the lazy dog')->limit(20, ' (...)');

// The quick brown fox (...)

```

If you would like to preserve complete words when truncating the string, you may utilize the `preserveWords` argument. When this argument is `true`, the string will be truncated to the nearest complete word boundary:
```


1$truncated = Str::of('The quick brown fox')->limit(12, preserveWords: true);




2 



3// The quick...




$truncated = Str::of('The quick brown fox')->limit(12, preserveWords: true);

// The quick...

```

#### [`lower`](https://laravel.com/docs/12.x/strings#method-fluent-str-lower)
The `lower` method converts the given string to lowercase:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('LARAVEL')->lower();




4 



5// 'laravel'




use Illuminate\Support\Str;

$result = Str::of('LARAVEL')->lower();

// 'laravel'

```

#### [`markdown`](https://laravel.com/docs/12.x/strings#method-fluent-str-markdown)
The `markdown` method converts GitHub flavored Markdown into HTML:
```


 1use Illuminate\Support\Str;




 2 



 3$html = Str::of('# Laravel')->markdown();




 4 



 5// <h1>Laravel</h1>




 6 



 7$html = Str::of('# Taylor <b>Otwell</b>')->markdown([




 8    'html_input' => 'strip',




 9]);




10 



11// <h1>Taylor Otwell</h1>




use Illuminate\Support\Str;

$html = Str::of('# Laravel')->markdown();

// <h1>Laravel</h1>

$html = Str::of('# Taylor <b>Otwell</b>')->markdown([
    'html_input' => 'strip',
]);

// <h1>Taylor Otwell</h1>

```

#### Markdown Security
By default, Markdown supports raw HTML, which will expose Cross-Site Scripting (XSS) vulnerabilities when used with raw user input. As per the `html_input` option to either escape or strip raw HTML, and the `allow_unsafe_links` option to specify whether to allow unsafe links. If you need to allow some raw HTML, you should pass your compiled Markdown through an HTML Purifier:
```


1use Illuminate\Support\Str;




2 



3Str::of('Inject: <script>alert("Hello XSS!");</script>')->markdown([




4    'html_input' => 'strip',




5    'allow_unsafe_links' => false,




6]);




7 



8// <p>Inject: alert(&quot;Hello XSS!&quot;);</p>




use Illuminate\Support\Str;

Str::of('Inject: <script>alert("Hello XSS!");</script>')->markdown([
    'html_input' => 'strip',
    'allow_unsafe_links' => false,
]);

// <p>Inject: alert(&quot;Hello XSS!&quot;);</p>

```

#### [`mask`](https://laravel.com/docs/12.x/strings#method-fluent-str-mask)
The `mask` method masks a portion of a string with a repeated character, and may be used to obfuscate segments of strings such as email addresses and phone numbers:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('taylor@example.com')->mask('*', 3);




4 



5// tay***************




use Illuminate\Support\Str;

$string = Str::of('taylor@example.com')->mask('*', 3);

// tay***************

```

If needed, you may provide negative numbers as the third or fourth argument to the `mask` method, which will instruct the method to begin masking at the given distance from the end of the string:
```


1$string = Str::of('taylor@example.com')->mask('*', -15, 3);




2 



3// tay***@example.com




4 



5$string = Str::of('taylor@example.com')->mask('*', 4, -4);




6 



7// tayl**********.com




$string = Str::of('taylor@example.com')->mask('*', -15, 3);

// tay***@example.com

$string = Str::of('taylor@example.com')->mask('*', 4, -4);

// tayl**********.com

```

#### [`match`](https://laravel.com/docs/12.x/strings#method-fluent-str-match)
The `match` method will return the portion of a string that matches a given regular expression pattern:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('foo bar')->match('/bar/');




4 



5// 'bar'




6 



7$result = Str::of('foo bar')->match('/foo (.*)/');




8 



9// 'bar'




use Illuminate\Support\Str;

$result = Str::of('foo bar')->match('/bar/');

// 'bar'

$result = Str::of('foo bar')->match('/foo (.*)/');

// 'bar'

```

#### [`matchAll`](https://laravel.com/docs/12.x/strings#method-fluent-str-match-all)
The `matchAll` method will return a collection containing the portions of a string that match a given regular expression pattern:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('bar foo bar')->matchAll('/bar/');




4 



5// collect(['bar', 'bar'])




use Illuminate\Support\Str;

$result = Str::of('bar foo bar')->matchAll('/bar/');

// collect(['bar', 'bar'])

```

If you specify a matching group within the expression, Laravel will return a collection of the first matching group's matches:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('bar fun bar fly')->matchAll('/f(\w*)/');




4 



5// collect(['un', 'ly']);




use Illuminate\Support\Str;

$result = Str::of('bar fun bar fly')->matchAll('/f(\w*)/');

// collect(['un', 'ly']);

```

If no matches are found, an empty collection will be returned.
#### [`isMatch`](https://laravel.com/docs/12.x/strings#method-fluent-str-is-match)
The `isMatch` method will return `true` if the string matches a given regular expression:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('foo bar')->isMatch('/foo (.*)/');




4 



5// true




6 



7$result = Str::of('laravel')->isMatch('/foo (.*)/');




8 



9// false




use Illuminate\Support\Str;

$result = Str::of('foo bar')->isMatch('/foo (.*)/');

// true

$result = Str::of('laravel')->isMatch('/foo (.*)/');

// false

```

#### [`newLine`](https://laravel.com/docs/12.x/strings#method-fluent-str-new-line)
The `newLine` method appends an "end of line" character to a string:
```


1use Illuminate\Support\Str;




2 



3$padded = Str::of('Laravel')->newLine()->append('Framework');




4 



5// 'Laravel




6//  Framework'




use Illuminate\Support\Str;

$padded = Str::of('Laravel')->newLine()->append('Framework');

// 'Laravel
//  Framework'

```

#### [`padBoth`](https://laravel.com/docs/12.x/strings#method-fluent-str-padboth)
The `padBoth` method wraps PHP's `str_pad` function, padding both sides of a string with another string until the final string reaches the desired length:
```


1use Illuminate\Support\Str;




2 



3$padded = Str::of('James')->padBoth(10, '_');




4 



5// '__James___'




6 



7$padded = Str::of('James')->padBoth(10);




8 



9// '  James   '




use Illuminate\Support\Str;

$padded = Str::of('James')->padBoth(10, '_');

// '__James___'

$padded = Str::of('James')->padBoth(10);

// '  James   '

```

#### [`padLeft`](https://laravel.com/docs/12.x/strings#method-fluent-str-padleft)
The `padLeft` method wraps PHP's `str_pad` function, padding the left side of a string with another string until the final string reaches the desired length:
```


1use Illuminate\Support\Str;




2 



3$padded = Str::of('James')->padLeft(10, '-=');




4 



5// '-=-=-James'




6 



7$padded = Str::of('James')->padLeft(10);




8 



9// '     James'




use Illuminate\Support\Str;

$padded = Str::of('James')->padLeft(10, '-=');

// '-=-=-James'

$padded = Str::of('James')->padLeft(10);

// '     James'

```

#### [`padRight`](https://laravel.com/docs/12.x/strings#method-fluent-str-padright)
The `padRight` method wraps PHP's `str_pad` function, padding the right side of a string with another string until the final string reaches the desired length:
```


1use Illuminate\Support\Str;




2 



3$padded = Str::of('James')->padRight(10, '-');




4 



5// 'James-----'




6 



7$padded = Str::of('James')->padRight(10);




8 



9// 'James     '




use Illuminate\Support\Str;

$padded = Str::of('James')->padRight(10, '-');

// 'James-----'

$padded = Str::of('James')->padRight(10);

// 'James     '

```

#### [`pipe`](https://laravel.com/docs/12.x/strings#method-fluent-str-pipe)
The `pipe` method allows you to transform the string by passing its current value to the given callable:
```


 1use Illuminate\Support\Str;




 2use Illuminate\Support\Stringable;




 3 



 4$hash = Str::of('Laravel')->pipe('md5')->prepend('Checksum: ');




 5 



 6// 'Checksum: a5c95b86291ea299fcbe64458ed12702'




 7 



 8$closure = Str::of('foo')->pipe(function (Stringable $str) {




 9    return 'bar';




10});




11 



12// 'bar'




use Illuminate\Support\Str;
use Illuminate\Support\Stringable;

$hash = Str::of('Laravel')->pipe('md5')->prepend('Checksum: ');

// 'Checksum: a5c95b86291ea299fcbe64458ed12702'

$closure = Str::of('foo')->pipe(function (Stringable $str) {
    return 'bar';
});

// 'bar'

```

#### [`plural`](https://laravel.com/docs/12.x/strings#method-fluent-str-plural)
The `plural` method converts a singular word string to its plural form. This function supports [any of the languages supported by Laravel's pluralizer](https://laravel.com/docs/12.x/localization#pluralization-language):
```


1use Illuminate\Support\Str;




2 



3$plural = Str::of('car')->plural();




4 



5// cars




6 



7$plural = Str::of('child')->plural();




8 



9// children




use Illuminate\Support\Str;

$plural = Str::of('car')->plural();

// cars

$plural = Str::of('child')->plural();

// children

```

You may provide an integer argument to the function to retrieve the singular or plural form of the string:
```


1use Illuminate\Support\Str;




2 



3$plural = Str::of('child')->plural(2);




4 



5// children




6 



7$plural = Str::of('child')->plural(1);




8 



9// child




use Illuminate\Support\Str;

$plural = Str::of('child')->plural(2);

// children

$plural = Str::of('child')->plural(1);

// child

```

You may provide the `prependCount` argument to prefix the pluralized string with the formatted `$count`:
```


1use Illuminate\Support\Str;




2 



3$label = Str::of('car')->plural(1000, prependCount: true);




4 



5// 1,000 cars




use Illuminate\Support\Str;

$label = Str::of('car')->plural(1000, prependCount: true);

// 1,000 cars

```

#### [`position`](https://laravel.com/docs/12.x/strings#method-fluent-str-position)
The `position` method returns the position of the first occurrence of a substring in a string. If the substring does not exist within the string, `false` is returned:
```


1use Illuminate\Support\Str;




2 



3$position = Str::of('Hello, World!')->position('Hello');




4 



5// 0




6 



7$position = Str::of('Hello, World!')->position('W');




8 



9// 7




use Illuminate\Support\Str;

$position = Str::of('Hello, World!')->position('Hello');

// 0

$position = Str::of('Hello, World!')->position('W');

// 7

```

#### [`prepend`](https://laravel.com/docs/12.x/strings#method-fluent-str-prepend)
The `prepend` method prepends the given values onto the string:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('Framework')->prepend('Laravel ');




4 



5// Laravel Framework




use Illuminate\Support\Str;

$string = Str::of('Framework')->prepend('Laravel ');

// Laravel Framework

```

#### [`remove`](https://laravel.com/docs/12.x/strings#method-fluent-str-remove)
The `remove` method removes the given value or array of values from the string:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('Arkansas is quite beautiful!')->remove('quite ');




4 



5// Arkansas is beautiful!




use Illuminate\Support\Str;

$string = Str::of('Arkansas is quite beautiful!')->remove('quite ');

// Arkansas is beautiful!

```

You may also pass `false` as a second parameter to ignore case when removing strings.
#### [`repeat`](https://laravel.com/docs/12.x/strings#method-fluent-str-repeat)
The `repeat` method repeats the given string:
```


1use Illuminate\Support\Str;




2 



3$repeated = Str::of('a')->repeat(5);




4 



5// aaaaa




use Illuminate\Support\Str;

$repeated = Str::of('a')->repeat(5);

// aaaaa

```

#### [`replace`](https://laravel.com/docs/12.x/strings#method-fluent-str-replace)
The `replace` method replaces a given string within the string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::of('Laravel 6.x')->replace('6.x', '7.x');




4 



5// Laravel 7.x




use Illuminate\Support\Str;

$replaced = Str::of('Laravel 6.x')->replace('6.x', '7.x');

// Laravel 7.x

```

The `replace` method also accepts a `caseSensitive` argument. By default, the `replace` method is case sensitive:
```


1$replaced = Str::of('macOS 13.x')->replace(




2    'macOS', 'iOS', caseSensitive: false




3);




$replaced = Str::of('macOS 13.x')->replace(
    'macOS', 'iOS', caseSensitive: false
);

```

#### [`replaceArray`](https://laravel.com/docs/12.x/strings#method-fluent-str-replace-array)
The `replaceArray` method replaces a given value in the string sequentially using an array:
```


1use Illuminate\Support\Str;




2 



3$string = 'The event will take place between ? and ?';




4 



5$replaced = Str::of($string)->replaceArray('?', ['8:30', '9:00']);




6 



7// The event will take place between 8:30 and 9:00




use Illuminate\Support\Str;

$string = 'The event will take place between ? and ?';

$replaced = Str::of($string)->replaceArray('?', ['8:30', '9:00']);

// The event will take place between 8:30 and 9:00

```

#### [`replaceFirst`](https://laravel.com/docs/12.x/strings#method-fluent-str-replace-first)
The `replaceFirst` method replaces the first occurrence of a given value in a string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::of('the quick brown fox jumps over the lazy dog')->replaceFirst('the', 'a');




4 



5// a quick brown fox jumps over the lazy dog




use Illuminate\Support\Str;

$replaced = Str::of('the quick brown fox jumps over the lazy dog')->replaceFirst('the', 'a');

// a quick brown fox jumps over the lazy dog

```

#### [`replaceLast`](https://laravel.com/docs/12.x/strings#method-fluent-str-replace-last)
The `replaceLast` method replaces the last occurrence of a given value in a string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::of('the quick brown fox jumps over the lazy dog')->replaceLast('the', 'a');




4 



5// the quick brown fox jumps over a lazy dog




use Illuminate\Support\Str;

$replaced = Str::of('the quick brown fox jumps over the lazy dog')->replaceLast('the', 'a');

// the quick brown fox jumps over a lazy dog

```

#### [`replaceMatches`](https://laravel.com/docs/12.x/strings#method-fluent-str-replace-matches)
The `replaceMatches` method replaces all portions of a string matching a pattern with the given replacement string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::of('(+1) 501-555-1000')->replaceMatches('/[^A-Za-z0-9]++/', '')




4 



5// '15015551000'




use Illuminate\Support\Str;

$replaced = Str::of('(+1) 501-555-1000')->replaceMatches('/[^A-Za-z0-9]++/', '')

// '15015551000'

```

The `replaceMatches` method also accepts a closure that will be invoked with each portion of the string matching the given pattern, allowing you to perform the replacement logic within the closure and return the replaced value:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::of('123')->replaceMatches('/\d/', function (array $matches) {




4    return '['.$matches[0].']';




5});




6 



7// '[1][2][3]'




use Illuminate\Support\Str;

$replaced = Str::of('123')->replaceMatches('/\d/', function (array $matches) {
    return '['.$matches[0].']';
});

// '[1][2][3]'

```

#### [`replaceStart`](https://laravel.com/docs/12.x/strings#method-fluent-str-replace-start)
The `replaceStart` method replaces the first occurrence of the given value only if the value appears at the start of the string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::of('Hello World')->replaceStart('Hello', 'Laravel');




4 



5// Laravel World




6 



7$replaced = Str::of('Hello World')->replaceStart('World', 'Laravel');




8 



9// Hello World




use Illuminate\Support\Str;

$replaced = Str::of('Hello World')->replaceStart('Hello', 'Laravel');

// Laravel World

$replaced = Str::of('Hello World')->replaceStart('World', 'Laravel');

// Hello World

```

#### [`replaceEnd`](https://laravel.com/docs/12.x/strings#method-fluent-str-replace-end)
The `replaceEnd` method replaces the last occurrence of the given value only if the value appears at the end of the string:
```


1use Illuminate\Support\Str;




2 



3$replaced = Str::of('Hello World')->replaceEnd('World', 'Laravel');




4 



5// Hello Laravel




6 



7$replaced = Str::of('Hello World')->replaceEnd('Hello', 'Laravel');




8 



9// Hello World




use Illuminate\Support\Str;

$replaced = Str::of('Hello World')->replaceEnd('World', 'Laravel');

// Hello Laravel

$replaced = Str::of('Hello World')->replaceEnd('Hello', 'Laravel');

// Hello World

```

#### [`scan`](https://laravel.com/docs/12.x/strings#method-fluent-str-scan)
The `scan` method parses input from a string into a collection according to a format supported by the
```


1use Illuminate\Support\Str;




2 



3$collection = Str::of('filename.jpg')->scan('%[^.].%s');




4 



5// collect(['filename', 'jpg'])




use Illuminate\Support\Str;

$collection = Str::of('filename.jpg')->scan('%[^.].%s');

// collect(['filename', 'jpg'])

```

#### [`singular`](https://laravel.com/docs/12.x/strings#method-fluent-str-singular)
The `singular` method converts a string to its singular form. This function supports [any of the languages supported by Laravel's pluralizer](https://laravel.com/docs/12.x/localization#pluralization-language):
```


1use Illuminate\Support\Str;




2 



3$singular = Str::of('cars')->singular();




4 



5// car




6 



7$singular = Str::of('children')->singular();




8 



9// child




use Illuminate\Support\Str;

$singular = Str::of('cars')->singular();

// car

$singular = Str::of('children')->singular();

// child

```

#### [`slug`](https://laravel.com/docs/12.x/strings#method-fluent-str-slug)
The `slug` method generates a URL friendly "slug" from the given string:
```


1use Illuminate\Support\Str;




2 



3$slug = Str::of('Laravel Framework')->slug('-');




4 



5// laravel-framework




use Illuminate\Support\Str;

$slug = Str::of('Laravel Framework')->slug('-');

// laravel-framework

```

#### [`snake`](https://laravel.com/docs/12.x/strings#method-fluent-str-snake)
The `snake` method converts the given string to `snake_case`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::of('fooBar')->snake();




4 



5// foo_bar




use Illuminate\Support\Str;

$converted = Str::of('fooBar')->snake();

// foo_bar

```

#### [`split`](https://laravel.com/docs/12.x/strings#method-fluent-str-split)
The `split` method splits a string into a collection using a regular expression:
```


1use Illuminate\Support\Str;




2 



3$segments = Str::of('one, two, three')->split('/[\s,]+/');




4 



5// collect(["one", "two", "three"])




use Illuminate\Support\Str;

$segments = Str::of('one, two, three')->split('/[\s,]+/');

// collect(["one", "two", "three"])

```

#### [`squish`](https://laravel.com/docs/12.x/strings#method-fluent-str-squish)
The `squish` method removes all extraneous white space from a string, including extraneous white space between words:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('    laravel    framework    ')->squish();




4 



5// laravel framework




use Illuminate\Support\Str;

$string = Str::of('    laravel    framework    ')->squish();

// laravel framework

```

#### [`start`](https://laravel.com/docs/12.x/strings#method-fluent-str-start)
The `start` method adds a single instance of the given value to a string if it does not already start with that value:
```


1use Illuminate\Support\Str;




2 



3$adjusted = Str::of('this/string')->start('/');




4 



5// /this/string




6 



7$adjusted = Str::of('/this/string')->start('/');




8 



9// /this/string




use Illuminate\Support\Str;

$adjusted = Str::of('this/string')->start('/');

// /this/string

$adjusted = Str::of('/this/string')->start('/');

// /this/string

```

#### [`startsWith`](https://laravel.com/docs/12.x/strings#method-fluent-str-starts-with)
The `startsWith` method determines if the given string begins with the given value:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('This is my name')->startsWith('This');




4 



5// true




use Illuminate\Support\Str;

$result = Str::of('This is my name')->startsWith('This');

// true

```

You may also pass an array of values to determine if the given string starts with any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('This is my name')->startsWith(['This', 'That']);




4 



5// true




use Illuminate\Support\Str;

$result = Str::of('This is my name')->startsWith(['This', 'That']);

// true

```

#### [`stripTags`](https://laravel.com/docs/12.x/strings#method-fluent-str-strip-tags)
The `stripTags` method removes all HTML and PHP tags from a string:
```


1use Illuminate\Support\Str;




2 



3$result = Str::of('<a href="https://laravel.com">Taylor <b>Otwell</b></a>')->stripTags();




4 



5// Taylor Otwell




6 



7$result = Str::of('<a href="https://laravel.com">Taylor <b>Otwell</b></a>')->stripTags('<b>');




8 



9// Taylor <b>Otwell</b>




use Illuminate\Support\Str;

$result = Str::of('<a href="https://laravel.com">Taylor <b>Otwell</b></a>')->stripTags();

// Taylor Otwell

$result = Str::of('<a href="https://laravel.com">Taylor <b>Otwell</b></a>')->stripTags('<b>');

// Taylor <b>Otwell</b>

```

#### [`studly`](https://laravel.com/docs/12.x/strings#method-fluent-str-studly)
The `studly` method converts the given string to `StudlyCase`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::of('foo_bar')->studly();




4 



5// FooBar




use Illuminate\Support\Str;

$converted = Str::of('foo_bar')->studly();

// FooBar

```

#### [`substr`](https://laravel.com/docs/12.x/strings#method-fluent-str-substr)
The `substr` method returns the portion of the string specified by the given start and length parameters:
```


1use Illuminate\Support\Str;




2 



3$string = Str::of('Laravel Framework')->substr(8);




4 



5// Framework




6 



7$string = Str::of('Laravel Framework')->substr(8, 5);




8 



9// Frame




use Illuminate\Support\Str;

$string = Str::of('Laravel Framework')->substr(8);

// Framework

$string = Str::of('Laravel Framework')->substr(8, 5);

// Frame

```

#### [`substrReplace`](https://laravel.com/docs/12.x/strings#method-fluent-str-substrreplace)
The `substrReplace` method replaces text within a portion of a string, starting at the position specified by the second argument and replacing the number of characters specified by the third argument. Passing `0` to the method's third argument will insert the string at the specified position without replacing any of the existing characters in the string:
