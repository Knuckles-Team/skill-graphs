## [Strings](https://laravel.com/docs/12.x/strings#strings)
#### [`__()`](https://laravel.com/docs/12.x/strings#method-__)
The `__` function translates the given translation string or translation key using your [language files](https://laravel.com/docs/12.x/localization):
```


1echo __('Welcome to our application');




2 



3echo __('messages.welcome');




echo __('Welcome to our application');

echo __('messages.welcome');

```

If the specified translation string or key does not exist, the `__` function will return the given value. So, using the example above, the `__` function would return `messages.welcome` if that translation key does not exist.
#### [`class_basename()`](https://laravel.com/docs/12.x/strings#method-class-basename)
The `class_basename` function returns the class name of the given class with the class's namespace removed:
```


1$class = class_basename('Foo\Bar\Baz');




2 



3// Baz




$class = class_basename('Foo\Bar\Baz');

// Baz

```

#### [`e()`](https://laravel.com/docs/12.x/strings#method-e)
The `e` function runs PHP's `htmlspecialchars` function with the `double_encode` option set to `true` by default:
```


1echo e('<html>foo</html>');




2 



3// &lt;html&gt;foo&lt;/html&gt;




echo e('<html>foo</html>');

// &lt;html&gt;foo&lt;/html&gt;

```

#### [`preg_replace_array()`](https://laravel.com/docs/12.x/strings#method-preg-replace-array)
The `preg_replace_array` function replaces a given pattern in the string sequentially using an array:
```


1$string = 'The event will take place between :start and :end';




2 



3$replaced = preg_replace_array('/:[a-z_]+/', ['8:30', '9:00'], $string);




4 



5// The event will take place between 8:30 and 9:00




$string = 'The event will take place between :start and :end';

$replaced = preg_replace_array('/:[a-z_]+/', ['8:30', '9:00'], $string);

// The event will take place between 8:30 and 9:00

```

#### [`Str::after()`](https://laravel.com/docs/12.x/strings#method-str-after)
The `Str::after` method returns everything after the given value in a string. The entire string will be returned if the value does not exist within the string:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::after('This is my name', 'This is');




4 



5// ' my name'




use Illuminate\Support\Str;

$slice = Str::after('This is my name', 'This is');

// ' my name'

```

#### [`Str::afterLast()`](https://laravel.com/docs/12.x/strings#method-str-after-last)
The `Str::afterLast` method returns everything after the last occurrence of the given value in a string. The entire string will be returned if the value does not exist within the string:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::afterLast('App\Http\Controllers\Controller', '\\');




4 



5// 'Controller'




use Illuminate\Support\Str;

$slice = Str::afterLast('App\Http\Controllers\Controller', '\\');

// 'Controller'

```

#### [`Str::apa()`](https://laravel.com/docs/12.x/strings#method-str-apa)
The `Str::apa` method converts the given string to title case following the
```


1use Illuminate\Support\Str;




2 



3$title = Str::apa('Creating A Project');




4 



5// 'Creating a Project'




use Illuminate\Support\Str;

$title = Str::apa('Creating A Project');

// 'Creating a Project'

```

#### [`Str::ascii()`](https://laravel.com/docs/12.x/strings#method-str-ascii)
The `Str::ascii` method will attempt to transliterate the string into an ASCII value:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::ascii('û');




4 



5// 'u'




use Illuminate\Support\Str;

$slice = Str::ascii('û');

// 'u'

```

#### [`Str::before()`](https://laravel.com/docs/12.x/strings#method-str-before)
The `Str::before` method returns everything before the given value in a string:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::before('This is my name', 'my name');




4 



5// 'This is '




use Illuminate\Support\Str;

$slice = Str::before('This is my name', 'my name');

// 'This is '

```

#### [`Str::beforeLast()`](https://laravel.com/docs/12.x/strings#method-str-before-last)
The `Str::beforeLast` method returns everything before the last occurrence of the given value in a string:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::beforeLast('This is my name', 'is');




4 



5// 'This '




use Illuminate\Support\Str;

$slice = Str::beforeLast('This is my name', 'is');

// 'This '

```

#### [`Str::between()`](https://laravel.com/docs/12.x/strings#method-str-between)
The `Str::between` method returns the portion of a string between two values:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::between('This is my name', 'This', 'name');




4 



5// ' is my '




use Illuminate\Support\Str;

$slice = Str::between('This is my name', 'This', 'name');

// ' is my '

```

#### [`Str::betweenFirst()`](https://laravel.com/docs/12.x/strings#method-str-between-first)
The `Str::betweenFirst` method returns the smallest possible portion of a string between two values:
```


1use Illuminate\Support\Str;




2 



3$slice = Str::betweenFirst('[a] bc [d]', '[', ']');




4 



5// 'a'




use Illuminate\Support\Str;

$slice = Str::betweenFirst('[a] bc [d]', '[', ']');

// 'a'

```

#### [`Str::camel()`](https://laravel.com/docs/12.x/strings#method-camel-case)
The `Str::camel` method converts the given string to `camelCase`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::camel('foo_bar');




4 



5// 'fooBar'




use Illuminate\Support\Str;

$converted = Str::camel('foo_bar');

// 'fooBar'

```

#### [`Str::charAt()`](https://laravel.com/docs/12.x/strings#method-char-at)
The `Str::charAt` method returns the character at the specified index. If the index is out of bounds, `false` is returned:
```


1use Illuminate\Support\Str;




2 



3$character = Str::charAt('This is my name.', 6);




4 



5// 's'




use Illuminate\Support\Str;

$character = Str::charAt('This is my name.', 6);

// 's'

```

#### [`Str::chopStart()`](https://laravel.com/docs/12.x/strings#method-str-chop-start)
The `Str::chopStart` method removes the first occurrence of the given value only if the value appears at the start of the string:
```


1use Illuminate\Support\Str;




2 



3$url = Str::chopStart('https://laravel.com', 'https://');




4 



5// 'laravel.com'




use Illuminate\Support\Str;

$url = Str::chopStart('https://laravel.com', 'https://');

// 'laravel.com'

```

You may also pass an array as the second argument. If the string starts with any of the values in the array then that value will be removed from string:
```


1use Illuminate\Support\Str;




2 



3$url = Str::chopStart('http://laravel.com', ['https://', 'http://']);




4 



5// 'laravel.com'




use Illuminate\Support\Str;

$url = Str::chopStart('http://laravel.com', ['https://', 'http://']);

// 'laravel.com'

```

#### [`Str::chopEnd()`](https://laravel.com/docs/12.x/strings#method-str-chop-end)
The `Str::chopEnd` method removes the last occurrence of the given value only if the value appears at the end of the string:
```


1use Illuminate\Support\Str;




2 



3$url = Str::chopEnd('app/Models/Photograph.php', '.php');




4 



5// 'app/Models/Photograph'




use Illuminate\Support\Str;

$url = Str::chopEnd('app/Models/Photograph.php', '.php');

// 'app/Models/Photograph'

```

You may also pass an array as the second argument. If the string ends with any of the values in the array then that value will be removed from string:
```


1use Illuminate\Support\Str;




2 



3$url = Str::chopEnd('laravel.com/index.php', ['/index.html', '/index.php']);




4 



5// 'laravel.com'




use Illuminate\Support\Str;

$url = Str::chopEnd('laravel.com/index.php', ['/index.html', '/index.php']);

// 'laravel.com'

```

#### [`Str::contains()`](https://laravel.com/docs/12.x/strings#method-str-contains)
The `Str::contains` method determines if the given string contains the given value. By default, this method is case sensitive:
```


1use Illuminate\Support\Str;




2 



3$contains = Str::contains('This is my name', 'my');




4 



5// true




use Illuminate\Support\Str;

$contains = Str::contains('This is my name', 'my');

// true

```

You may also pass an array of values to determine if the given string contains any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$contains = Str::contains('This is my name', ['my', 'foo']);




4 



5// true




use Illuminate\Support\Str;

$contains = Str::contains('This is my name', ['my', 'foo']);

// true

```

You may disable case sensitivity by setting the `ignoreCase` argument to `true`:
```


1use Illuminate\Support\Str;




2 



3$contains = Str::contains('This is my name', 'MY', ignoreCase: true);




4 



5// true




use Illuminate\Support\Str;

$contains = Str::contains('This is my name', 'MY', ignoreCase: true);

// true

```

#### [`Str::containsAll()`](https://laravel.com/docs/12.x/strings#method-str-contains-all)
The `Str::containsAll` method determines if the given string contains all of the values in a given array:
```


1use Illuminate\Support\Str;




2 



3$containsAll = Str::containsAll('This is my name', ['my', 'name']);




4 



5// true




use Illuminate\Support\Str;

$containsAll = Str::containsAll('This is my name', ['my', 'name']);

// true

```

You may disable case sensitivity by setting the `ignoreCase` argument to `true`:
```


1use Illuminate\Support\Str;




2 



3$containsAll = Str::containsAll('This is my name', ['MY', 'NAME'], ignoreCase: true);




4 



5// true




use Illuminate\Support\Str;

$containsAll = Str::containsAll('This is my name', ['MY', 'NAME'], ignoreCase: true);

// true

```

#### [`Str::doesntContain()`](https://laravel.com/docs/12.x/strings#method-str-doesnt-contain)
The `Str::doesntContain` method determines if the given string doesn't contain the given value. By default, this method is case sensitive:
```


1use Illuminate\Support\Str;




2 



3$doesntContain = Str::doesntContain('This is name', 'my');




4 



5// true




use Illuminate\Support\Str;

$doesntContain = Str::doesntContain('This is name', 'my');

// true

```

You may also pass an array of values to determine if the given string doesn't contain any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$doesntContain = Str::doesntContain('This is name', ['my', 'framework']);




4 



5// true




use Illuminate\Support\Str;

$doesntContain = Str::doesntContain('This is name', ['my', 'framework']);

// true

```

You may disable case sensitivity by setting the `ignoreCase` argument to `true`:
```


1use Illuminate\Support\Str;




2 



3$doesntContain = Str::doesntContain('This is name', 'MY', ignoreCase: true);




4 



5// true




use Illuminate\Support\Str;

$doesntContain = Str::doesntContain('This is name', 'MY', ignoreCase: true);

// true

```

#### [`Str::deduplicate()`](https://laravel.com/docs/12.x/strings#method-deduplicate)
The `Str::deduplicate` method replaces consecutive instances of a character with a single instance of that character in the given string. By default, the method deduplicates spaces:
```


1use Illuminate\Support\Str;




2 



3$result = Str::deduplicate('The   Laravel   Framework');




4 



5// The Laravel Framework




use Illuminate\Support\Str;

$result = Str::deduplicate('The   Laravel   Framework');

// The Laravel Framework

```

You may specify a different character to deduplicate by passing it in as the second argument to the method:
```


1use Illuminate\Support\Str;




2 



3$result = Str::deduplicate('The---Laravel---Framework', '-');




4 



5// The-Laravel-Framework




use Illuminate\Support\Str;

$result = Str::deduplicate('The---Laravel---Framework', '-');

// The-Laravel-Framework

```

#### [`Str::doesntEndWith()`](https://laravel.com/docs/12.x/strings#method-str-doesnt-end-with)
The `Str::doesntEndWith` method determines if the given string doesn't end with the given value:
```


1use Illuminate\Support\Str;




2 



3$result = Str::doesntEndWith('This is my name', 'dog');




4 



5// true




use Illuminate\Support\Str;

$result = Str::doesntEndWith('This is my name', 'dog');

// true

```

You may also pass an array of values to determine if the given string doesn't end with any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$result = Str::doesntEndWith('This is my name', ['this', 'foo']);




4 



5// true




6 



7$result = Str::doesntEndWith('This is my name', ['name', 'foo']);




8 



9// false




use Illuminate\Support\Str;

$result = Str::doesntEndWith('This is my name', ['this', 'foo']);

// true

$result = Str::doesntEndWith('This is my name', ['name', 'foo']);

// false

```

#### [`Str::doesntStartWith()`](https://laravel.com/docs/12.x/strings#method-str-doesnt-start-with)
The `Str::doesntStartWith` method determines if the given string doesn't begin with the given value:
```


1use Illuminate\Support\Str;




2 



3$result = Str::doesntStartWith('This is my name', 'That');




4 



5// true




use Illuminate\Support\Str;

$result = Str::doesntStartWith('This is my name', 'That');

// true

```

If an array of possible values is passed, the `doesntStartWith` method will return `true` if the string doesn't begin with any of the given values:
```


1$result = Str::doesntStartWith('This is my name', ['What', 'That', 'There']);




2 



3// true




$result = Str::doesntStartWith('This is my name', ['What', 'That', 'There']);

// true

```

#### [`Str::endsWith()`](https://laravel.com/docs/12.x/strings#method-ends-with)
The `Str::endsWith` method determines if the given string ends with the given value:
```


1use Illuminate\Support\Str;




2 



3$result = Str::endsWith('This is my name', 'name');




4 



5// true




use Illuminate\Support\Str;

$result = Str::endsWith('This is my name', 'name');

// true

```

You may also pass an array of values to determine if the given string ends with any of the values in the array:
```


1use Illuminate\Support\Str;




2 



3$result = Str::endsWith('This is my name', ['name', 'foo']);




4 



5// true




6 



7$result = Str::endsWith('This is my name', ['this', 'foo']);




8 



9// false




use Illuminate\Support\Str;

$result = Str::endsWith('This is my name', ['name', 'foo']);

// true

$result = Str::endsWith('This is my name', ['this', 'foo']);

// false

```

#### [`Str::excerpt()`](https://laravel.com/docs/12.x/strings#method-excerpt)
The `Str::excerpt` method extracts an excerpt from a given string that matches the first instance of a phrase within that string:
```


1use Illuminate\Support\Str;




2 



3$excerpt = Str::excerpt('This is my name', 'my', [




4    'radius' => 3




5]);




6 



7// '...is my na...'




use Illuminate\Support\Str;

$excerpt = Str::excerpt('This is my name', 'my', [
    'radius' => 3
]);

// '...is my na...'

```

The `radius` option, which defaults to `100`, allows you to define the number of characters that should appear on each side of the truncated string.
In addition, you may use the `omission` option to define the string that will be prepended and appended to the truncated string:
```


1use Illuminate\Support\Str;




2 



3$excerpt = Str::excerpt('This is my name', 'name', [




4    'radius' => 3,




5    'omission' => '(...) '




6]);




7 



8// '(...) my name'




use Illuminate\Support\Str;

$excerpt = Str::excerpt('This is my name', 'name', [
    'radius' => 3,
    'omission' => '(...) '
]);

// '(...) my name'

```

#### [`Str::finish()`](https://laravel.com/docs/12.x/strings#method-str-finish)
The `Str::finish` method adds a single instance of the given value to a string if it does not already end with that value:
```


1use Illuminate\Support\Str;




2 



3$adjusted = Str::finish('this/string', '/');




4 



5// this/string/




6 



7$adjusted = Str::finish('this/string/', '/');




8 



9// this/string/




use Illuminate\Support\Str;

$adjusted = Str::finish('this/string', '/');

// this/string/

$adjusted = Str::finish('this/string/', '/');

// this/string/

```

#### [`Str::fromBase64()`](https://laravel.com/docs/12.x/strings#method-str-from-base64)
The `Str::fromBase64` method decodes the given Base64 string:
```


1use Illuminate\Support\Str;




2 



3$decoded = Str::fromBase64('TGFyYXZlbA==');




4 



5// Laravel




use Illuminate\Support\Str;

$decoded = Str::fromBase64('TGFyYXZlbA==');

// Laravel

```

#### [`Str::headline()`](https://laravel.com/docs/12.x/strings#method-str-headline)
The `Str::headline` method will convert strings delimited by casing, hyphens, or underscores into a space delimited string with each word's first letter capitalized:
```


1use Illuminate\Support\Str;




2 



3$headline = Str::headline('steve_jobs');




4 



5// Steve Jobs




6 



7$headline = Str::headline('EmailNotificationSent');




8 



9// Email Notification Sent




use Illuminate\Support\Str;

$headline = Str::headline('steve_jobs');

// Steve Jobs

$headline = Str::headline('EmailNotificationSent');

// Email Notification Sent

```

#### [`Str::inlineMarkdown()`](https://laravel.com/docs/12.x/strings#method-str-inline-markdown)
The `Str::inlineMarkdown` method converts GitHub flavored Markdown into inline HTML using `markdown` method, it does not wrap all generated HTML in a block-level element:
```


1use Illuminate\Support\Str;




2 



3$html = Str::inlineMarkdown('**Laravel**');




4 



5// <strong>Laravel</strong>




use Illuminate\Support\Str;

$html = Str::inlineMarkdown('**Laravel**');

// <strong>Laravel</strong>

```

#### Markdown Security
By default, Markdown supports raw HTML, which will expose Cross-Site Scripting (XSS) vulnerabilities when used with raw user input. As per the `html_input` option to either escape or strip raw HTML, and the `allow_unsafe_links` option to specify whether to allow unsafe links. If you need to allow some raw HTML, you should pass your compiled Markdown through an HTML Purifier:
```


1use Illuminate\Support\Str;




2 



3Str::inlineMarkdown('Inject: <script>alert("Hello XSS!");</script>', [




4    'html_input' => 'strip',




5    'allow_unsafe_links' => false,




6]);




7 



8// Inject: alert(&quot;Hello XSS!&quot;);




use Illuminate\Support\Str;

Str::inlineMarkdown('Inject: <script>alert("Hello XSS!");</script>', [
    'html_input' => 'strip',
    'allow_unsafe_links' => false,
]);

// Inject: alert(&quot;Hello XSS!&quot;);

```

#### [`Str::is()`](https://laravel.com/docs/12.x/strings#method-str-is)
The `Str::is` method determines if a given string matches a given pattern. Asterisks may be used as wildcard values:
```


1use Illuminate\Support\Str;




2 



3$matches = Str::is('foo*', 'foobar');




4 



5// true




6 



7$matches = Str::is('baz*', 'foobar');




8 



9// false




use Illuminate\Support\Str;

$matches = Str::is('foo*', 'foobar');

// true

$matches = Str::is('baz*', 'foobar');

// false

```

You may disable case sensitivity by setting the `ignoreCase` argument to `true`:
```


1use Illuminate\Support\Str;




2 



3$matches = Str::is('*.jpg', 'photo.JPG', ignoreCase: true);




4 



5// true




use Illuminate\Support\Str;

$matches = Str::is('*.jpg', 'photo.JPG', ignoreCase: true);

// true

```

#### [`Str::isAscii()`](https://laravel.com/docs/12.x/strings#method-str-is-ascii)
The `Str::isAscii` method determines if a given string is 7 bit ASCII:
```


1use Illuminate\Support\Str;




2 



3$isAscii = Str::isAscii('Taylor');




4 



5// true




6 



7$isAscii = Str::isAscii('ü');




8 



9// false




use Illuminate\Support\Str;

$isAscii = Str::isAscii('Taylor');

// true

$isAscii = Str::isAscii('ü');

// false

```

#### [`Str::isJson()`](https://laravel.com/docs/12.x/strings#method-str-is-json)
The `Str::isJson` method determines if the given string is valid JSON:
```


 1use Illuminate\Support\Str;




 2 



 3$result = Str::isJson('[1,2,3]');




 4 



 5// true




 6 



 7$result = Str::isJson('{"first": "John", "last": "Doe"}');




 8 



 9// true




10 



11$result = Str::isJson('{first: "John", last: "Doe"}');




12 



13// false




use Illuminate\Support\Str;

$result = Str::isJson('[1,2,3]');

// true

$result = Str::isJson('{"first": "John", "last": "Doe"}');

// true

$result = Str::isJson('{first: "John", last: "Doe"}');

// false

```

#### [`Str::isUrl()`](https://laravel.com/docs/12.x/strings#method-str-is-url)
The `Str::isUrl` method determines if the given string is a valid URL:
```


1use Illuminate\Support\Str;




2 



3$isUrl = Str::isUrl('http://example.com');




4 



5// true




6 



7$isUrl = Str::isUrl('laravel');




8 



9// false




use Illuminate\Support\Str;

$isUrl = Str::isUrl('http://example.com');

// true

$isUrl = Str::isUrl('laravel');

// false

```

The `isUrl` method considers a wide range of protocols as valid. However, you may specify the protocols that should be considered valid by providing them to the `isUrl` method:
```


1$isUrl = Str::isUrl('http://example.com', ['http', 'https']);




$isUrl = Str::isUrl('http://example.com', ['http', 'https']);

```

#### [`Str::isUlid()`](https://laravel.com/docs/12.x/strings#method-str-is-ulid)
The `Str::isUlid` method determines if the given string is a valid ULID:
```


1use Illuminate\Support\Str;




2 



3$isUlid = Str::isUlid('01gd6r360bp37zj17nxb55yv40');




4 



5// true




6 



7$isUlid = Str::isUlid('laravel');




8 



9// false




use Illuminate\Support\Str;

$isUlid = Str::isUlid('01gd6r360bp37zj17nxb55yv40');

// true

$isUlid = Str::isUlid('laravel');

// false

```

#### [`Str::isUuid()`](https://laravel.com/docs/12.x/strings#method-str-is-uuid)
The `Str::isUuid` method determines if the given string is a valid UUID:
```


1use Illuminate\Support\Str;




2 



3$isUuid = Str::isUuid('a0a2a2d2-0b87-4a18-83f2-2529882be2de');




4 



5// true




6 



7$isUuid = Str::isUuid('laravel');




8 



9// false




use Illuminate\Support\Str;

$isUuid = Str::isUuid('a0a2a2d2-0b87-4a18-83f2-2529882be2de');

// true

$isUuid = Str::isUuid('laravel');

// false

```

You may also validate that the given UUID matches a UUID specification by version (1, 3, 4, 5, 6, 7, or 8):
```


1use Illuminate\Support\Str;




2 



3$isUuid = Str::isUuid('a0a2a2d2-0b87-4a18-83f2-2529882be2de', version: 4);




4 



5// true




6 



7$isUuid = Str::isUuid('a0a2a2d2-0b87-4a18-83f2-2529882be2de', version: 1);




8 



9// false




use Illuminate\Support\Str;

$isUuid = Str::isUuid('a0a2a2d2-0b87-4a18-83f2-2529882be2de', version: 4);

// true

$isUuid = Str::isUuid('a0a2a2d2-0b87-4a18-83f2-2529882be2de', version: 1);

// false

```

#### [`Str::kebab()`](https://laravel.com/docs/12.x/strings#method-kebab-case)
The `Str::kebab` method converts the given string to `kebab-case`:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::kebab('fooBar');




4 



5// foo-bar




use Illuminate\Support\Str;

$converted = Str::kebab('fooBar');

// foo-bar

```

#### [`Str::lcfirst()`](https://laravel.com/docs/12.x/strings#method-str-lcfirst)
The `Str::lcfirst` method returns the given string with the first character lowercased:
```


1use Illuminate\Support\Str;




2 



3$string = Str::lcfirst('Foo Bar');




4 



5// foo Bar




use Illuminate\Support\Str;

$string = Str::lcfirst('Foo Bar');

// foo Bar

```

#### [`Str::length()`](https://laravel.com/docs/12.x/strings#method-str-length)
The `Str::length` method returns the length of the given string:
```


1use Illuminate\Support\Str;




2 



3$length = Str::length('Laravel');




4 



5// 7




use Illuminate\Support\Str;

$length = Str::length('Laravel');

// 7

```

#### [`Str::limit()`](https://laravel.com/docs/12.x/strings#method-str-limit)
The `Str::limit` method truncates the given string to the specified length:
```


1use Illuminate\Support\Str;




2 



3$truncated = Str::limit('The quick brown fox jumps over the lazy dog', 20);




4 



5// The quick brown fox...




use Illuminate\Support\Str;

$truncated = Str::limit('The quick brown fox jumps over the lazy dog', 20);

// The quick brown fox...

```

You may pass a third argument to the method to change the string that will be appended to the end of the truncated string:
```


1$truncated = Str::limit('The quick brown fox jumps over the lazy dog', 20, ' (...)');




2 



3// The quick brown fox (...)




$truncated = Str::limit('The quick brown fox jumps over the lazy dog', 20, ' (...)');

// The quick brown fox (...)

```

If you would like to preserve complete words when truncating the string, you may utilize the `preserveWords` argument. When this argument is `true`, the string will be truncated to the nearest complete word boundary:
```


1$truncated = Str::limit('The quick brown fox', 12, preserveWords: true);




2 



3// The quick...




$truncated = Str::limit('The quick brown fox', 12, preserveWords: true);

// The quick...

```

#### [`Str::lower()`](https://laravel.com/docs/12.x/strings#method-str-lower)
The `Str::lower` method converts the given string to lowercase:
```


1use Illuminate\Support\Str;




2 



3$converted = Str::lower('LARAVEL');




4 



5// laravel




use Illuminate\Support\Str;

$converted = Str::lower('LARAVEL');

// laravel

```

#### [`Str::markdown()`](https://laravel.com/docs/12.x/strings#method-str-markdown)
The `Str::markdown` method converts GitHub flavored Markdown into HTML using
