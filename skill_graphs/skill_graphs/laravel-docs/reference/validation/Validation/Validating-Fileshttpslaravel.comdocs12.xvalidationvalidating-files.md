## [Validating Files](https://laravel.com/docs/12.x/validation#validating-files)
Laravel provides a variety of validation rules that may be used to validate uploaded files, such as `mimes`, `image`, `min`, and `max`. While you are free to specify these rules individually when validating files, Laravel also offers a fluent file validation rule builder that you may find convenient:
```


 1use Illuminate\Support\Facades\Validator;




 2use Illuminate\Validation\Rules\File;




 3 



 4Validator::validate($input, [




 5    'attachment' => [




 6        'required',




 7        File::types(['mp3', 'wav'])




 8            ->min(1024)




 9            ->max(12 * 1024),




10    ],




11]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rules\File;

Validator::validate($input, [
    'attachment' => [
        'required',
        File::types(['mp3', 'wav'])
            ->min(1024)
            ->max(12 * 1024),
    ],
]);

```

#### [Validating File Types](https://laravel.com/docs/12.x/validation#validating-files-file-types)
Even though you only need to specify the extensions when invoking the `types` method, this method actually validates the MIME type of the file by reading the file's contents and guessing its MIME type. A full listing of MIME types and their corresponding extensions may be found at the following location:
#### [Validating File Sizes](https://laravel.com/docs/12.x/validation#validating-files-file-sizes)
For convenience, minimum and maximum file sizes may be specified as a string with a suffix indicating the file size units. The `kb`, `mb`, `gb`, and `tb` suffixes are supported:
```


1File::types(['mp3', 'wav'])




2    ->min('1kb')




3    ->max('10mb');




File::types(['mp3', 'wav'])
    ->min('1kb')
    ->max('10mb');

```

#### [Validating Image Files](https://laravel.com/docs/12.x/validation#validating-files-image-files)
If your application accepts images uploaded by your users, you may use the `File` rule's `image` constructor method to ensure that the file under validation is an image (jpg, jpeg, png, bmp, gif, or webp).
In addition, the `dimensions` rule may be used to limit the dimensions of the image:
```


 1use Illuminate\Support\Facades\Validator;




 2use Illuminate\Validation\Rule;




 3use Illuminate\Validation\Rules\File;




 4 



 5Validator::validate($input, [




 6    'photo' => [




 7        'required',




 8        File::image()




 9            ->min(1024)




10            ->max(12 * 1024)




11            ->dimensions(Rule::dimensions()->maxWidth(1000)->maxHeight(500)),




12    ],




13]);




use Illuminate\Support\Facades\Validator;
use Illuminate\Validation\Rule;
use Illuminate\Validation\Rules\File;

Validator::validate($input, [
    'photo' => [
        'required',
        File::image()
            ->min(1024)
            ->max(12 * 1024)
            ->dimensions(Rule::dimensions()->maxWidth(1000)->maxHeight(500)),
    ],
]);

```

More information regarding validating image dimensions may be found in the [dimension rule documentation](https://laravel.com/docs/12.x/validation#rule-dimensions).
By default, the `image` rule does not allow SVG files due to the possibility of XSS vulnerabilities. If you need to allow SVG files, you may pass `allowSvg: true` to the `image` rule: `File::image(allowSvg: true)`.
#### [Validating Image Dimensions](https://laravel.com/docs/12.x/validation#validating-files-image-dimensions)
You may also validate the dimensions of an image. For example, to validate that an uploaded image is at least 1000 pixels wide and 500 pixels tall, you may use the `dimensions` rule:
```


1use Illuminate\Validation\Rule;




2use Illuminate\Validation\Rules\File;




3 



4File::image()->dimensions(




5    Rule::dimensions()




6        ->maxWidth(1000)




7        ->maxHeight(500)




8)




use Illuminate\Validation\Rule;
use Illuminate\Validation\Rules\File;

File::image()->dimensions(
    Rule::dimensions()
        ->maxWidth(1000)
        ->maxHeight(500)
)

```

More information regarding validating image dimensions may be found in the [dimension rule documentation](https://laravel.com/docs/12.x/validation#rule-dimensions).
