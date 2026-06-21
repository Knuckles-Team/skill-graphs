## [Validation Quickstart](https://laravel.com/docs/12.x/validation#validation-quickstart)
To learn about Laravel's powerful validation features, let's look at a complete example of validating a form and displaying the error messages back to the user. By reading this high-level overview, you'll be able to gain a good general understanding of how to validate incoming request data using Laravel:
### [Defining the Routes](https://laravel.com/docs/12.x/validation#quick-defining-the-routes)
First, let's assume we have the following routes defined in our `routes/web.php` file:
```


1use App\Http\Controllers\PostController;




2 



3Route::get('/post/create', [PostController::class, 'create']);




4Route::post('/post', [PostController::class, 'store']);




use App\Http\Controllers\PostController;

Route::get('/post/create', [PostController::class, 'create']);
Route::post('/post', [PostController::class, 'store']);

```

The `GET` route will display a form for the user to create a new blog post, while the `POST` route will store the new blog post in the database.
### [Creating the Controller](https://laravel.com/docs/12.x/validation#quick-creating-the-controller)
Next, let's take a look at a simple controller that handles incoming requests to these routes. We'll leave the `store` method empty for now:
```


 1<?php




 2 



 3namespace App\Http\Controllers;




 4 



 5use Illuminate\Http\RedirectResponse;




 6use Illuminate\Http\Request;




 7use Illuminate\View\View;




 8 



 9class PostController extends Controller




10{




11    /**




12     * Show the form to create a new blog post.




13     */




14    public function create(): View




15    {




16        return view('post.create');




17    }




18 



19    /**




20     * Store a new blog post.




21     */




22    public function store(Request $request): RedirectResponse




23    {




24        // Validate and store the blog post...




25 



26        $post = /** ... */




27 



28        return to_route('post.show', ['post' => $post->id]);




29    }




30}




<?php

namespace App\Http\Controllers;

use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;

class PostController extends Controller
{
    /**
     * Show the form to create a new blog post.
     */
    public function create(): View
    {
        return view('post.create');
    }

    /**
     * Store a new blog post.
     */
    public function store(Request $request): RedirectResponse
    {
        // Validate and store the blog post...

        $post = /** ... */

        return to_route('post.show', ['post' => $post->id]);
    }
}

```

### [Writing the Validation Logic](https://laravel.com/docs/12.x/validation#quick-writing-the-validation-logic)
Now we are ready to fill in our `store` method with the logic to validate the new blog post. To do this, we will use the `validate` method provided by the `Illuminate\Http\Request` object. If the validation rules pass, your code will keep executing normally; however, if validation fails, an `Illuminate\Validation\ValidationException` exception will be thrown and the proper error response will automatically be sent back to the user.
If validation fails during a traditional HTTP request, a redirect response to the previous URL will be generated. If the incoming request is an XHR request, a [JSON response containing the validation error messages](https://laravel.com/docs/12.x/validation#validation-error-response-format) will be returned.
To get a better understanding of the `validate` method, let's jump back into the `store` method:
```


 1/**




 2 * Store a new blog post.




 3 */




 4public function store(Request $request): RedirectResponse




 5{




 6    $validated = $request->validate([




 7        'title' => 'required|unique:posts|max:255',




 8        'body' => 'required',




 9    ]);




10 



11    // The blog post is valid...




12 



13    return redirect('/posts');




14}




/**
 * Store a new blog post.
 */
public function store(Request $request): RedirectResponse
{
    $validated = $request->validate([
        'title' => 'required|unique:posts|max:255',
        'body' => 'required',
    ]);

    // The blog post is valid...

    return redirect('/posts');
}

```

As you can see, the validation rules are passed into the `validate` method. Don't worry - all available validation rules are [documented](https://laravel.com/docs/12.x/validation#available-validation-rules). Again, if the validation fails, the proper response will automatically be generated. If the validation passes, our controller will continue executing normally.
Alternatively, validation rules may be specified as arrays of rules instead of a single `|` delimited string:
```


1$validatedData = $request->validate([




2    'title' => ['required', 'unique:posts', 'max:255'],




3    'body' => ['required'],




4]);




$validatedData = $request->validate([
    'title' => ['required', 'unique:posts', 'max:255'],
    'body' => ['required'],
]);

```

In addition, you may use the `validateWithBag` method to validate a request and store any error messages within a [named error bag](https://laravel.com/docs/12.x/validation#named-error-bags):
```


1$validatedData = $request->validateWithBag('post', [




2    'title' => ['required', 'unique:posts', 'max:255'],




3    'body' => ['required'],




4]);




$validatedData = $request->validateWithBag('post', [
    'title' => ['required', 'unique:posts', 'max:255'],
    'body' => ['required'],
]);

```

#### [Stopping on First Validation Failure](https://laravel.com/docs/12.x/validation#stopping-on-first-validation-failure)
Sometimes you may wish to stop running validation rules on an attribute after the first validation failure. To do so, assign the `bail` rule to the attribute:
```


1$request->validate([




2    'title' => 'bail|required|unique:posts|max:255',




3    'body' => 'required',




4]);




$request->validate([
    'title' => 'bail|required|unique:posts|max:255',
    'body' => 'required',
]);

```

In this example, if the `unique` rule on the `title` attribute fails, the `max` rule will not be checked. Rules will be validated in the order they are assigned.
#### [A Note on Nested Attributes](https://laravel.com/docs/12.x/validation#a-note-on-nested-attributes)
If the incoming HTTP request contains "nested" field data, you may specify these fields in your validation rules using "dot" syntax:
```


1$request->validate([




2    'title' => 'required|unique:posts|max:255',




3    'author.name' => 'required',




4    'author.description' => 'required',




5]);




$request->validate([
    'title' => 'required|unique:posts|max:255',
    'author.name' => 'required',
    'author.description' => 'required',
]);

```

On the other hand, if your field name contains a literal period, you can explicitly prevent this from being interpreted as "dot" syntax by escaping the period with a backslash:
```


1$request->validate([




2    'title' => 'required|unique:posts|max:255',




3    'v1\.0' => 'required',




4]);




$request->validate([
    'title' => 'required|unique:posts|max:255',
    'v1\.0' => 'required',
]);

```

### [Displaying the Validation Errors](https://laravel.com/docs/12.x/validation#quick-displaying-the-validation-errors)
So, what if the incoming request fields do not pass the given validation rules? As mentioned previously, Laravel will automatically redirect the user back to their previous location. In addition, all of the validation errors and [request input](https://laravel.com/docs/12.x/requests#retrieving-old-input) will automatically be [flashed to the session](https://laravel.com/docs/12.x/session#flash-data).
An `$errors` variable is shared with all of your application's views by the `Illuminate\View\Middleware\ShareErrorsFromSession` middleware, which is provided by the `web` middleware group. When this middleware is applied an `$errors` variable will always be available in your views, allowing you to conveniently assume the `$errors` variable is always defined and can be safely used. The `$errors` variable will be an instance of `Illuminate\Support\MessageBag`. For more information on working with this object, [check out its documentation](https://laravel.com/docs/12.x/validation#working-with-error-messages).
So, in our example, the user will be redirected to our controller's `create` method when validation fails, allowing us to display the error messages in the view:
```


 1<!-- /resources/views/post/create.blade.php -->




 2 



 3<h1>Create Post</h1>




 4 



 5@if ($errors->any())




 6    <div class="alert alert-danger">




 7        <ul>




 8            @foreach ($errors->all() as $error)




 9                <li>{{ $error }}</li>




10            @endforeach




11        </ul>




12    </div>




13@endif




14 



15<!-- Create Post Form -->




<!-- /resources/views/post/create.blade.php -->

<h1>Create Post</h1>

@if ($errors->any())
    <div class="alert alert-danger">
        <ul>
            @foreach ($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif

<!-- Create Post Form -->

```

#### [Customizing the Error Messages](https://laravel.com/docs/12.x/validation#quick-customizing-the-error-messages)
Laravel's built-in validation rules each have an error message that is located in your application's `lang/en/validation.php` file. If your application does not have a `lang` directory, you may instruct Laravel to create it using the `lang:publish` Artisan command.
Within the `lang/en/validation.php` file, you will find a translation entry for each validation rule. You are free to change or modify these messages based on the needs of your application.
In addition, you may copy this file to another language directory to translate the messages for your application's language. To learn more about Laravel localization, check out the complete [localization documentation](https://laravel.com/docs/12.x/localization).
By default, the Laravel application skeleton does not include the `lang` directory. If you would like to customize Laravel's language files, you may publish them via the `lang:publish` Artisan command.
#### [XHR Requests and Validation](https://laravel.com/docs/12.x/validation#quick-xhr-requests-and-validation)
In this example, we used a traditional form to send data to the application. However, many applications receive XHR requests from a JavaScript powered frontend. When using the `validate` method during an XHR request, Laravel will not generate a redirect response. Instead, Laravel generates a [JSON response containing all of the validation errors](https://laravel.com/docs/12.x/validation#validation-error-response-format). This JSON response will be sent with a 422 HTTP status code.
#### [The `@error` Directive](https://laravel.com/docs/12.x/validation#the-at-error-directive)
You may use the `@error` [Blade](https://laravel.com/docs/12.x/blade) directive to quickly determine if validation error messages exist for a given attribute. Within an `@error` directive, you may echo the `$message` variable to display the error message:
```


 1<!-- /resources/views/post/create.blade.php -->




 2 



 3<label for="title">Post Title</label>




 4 



 5<input




 6    id="title"




 7    type="text"




 8    name="title"




 9    class="@error('title') is-invalid @enderror"




10/>




11 



12@error('title')




13    <div class="alert alert-danger">{{ $message }}</div>




14@enderror




<!-- /resources/views/post/create.blade.php -->

<label for="title">Post Title</label>

<input
    id="title"
    type="text"
    name="title"
    class="@error('title') is-invalid @enderror"
/>

@error('title')
    <div class="alert alert-danger">{{ $message }}</div>
@enderror

```

If you are using [named error bags](https://laravel.com/docs/12.x/validation#named-error-bags), you may pass the name of the error bag as the second argument to the `@error` directive:
```


1<input ... class="@error('title', 'post') is-invalid @enderror">




<input ... class="@error('title', 'post') is-invalid @enderror">

```

### [Repopulating Forms](https://laravel.com/docs/12.x/validation#repopulating-forms)
When Laravel generates a redirect response due to a validation error, the framework will automatically [flash all of the request's input to the session](https://laravel.com/docs/12.x/session#flash-data). This is done so that you may conveniently access the input during the next request and repopulate the form that the user attempted to submit.
To retrieve flashed input from the previous request, invoke the `old` method on an instance of `Illuminate\Http\Request`. The `old` method will pull the previously flashed input data from the [session](https://laravel.com/docs/12.x/session):
```


1$title = $request->old('title');




$title = $request->old('title');

```

Laravel also provides a global `old` helper. If you are displaying old input within a [Blade template](https://laravel.com/docs/12.x/blade), it is more convenient to use the `old` helper to repopulate the form. If no old input exists for the given field, `null` will be returned:
```


1<input type="text" name="title" value="{{ old('title') }}">




<input type="text" name="title" value="{{ old('title') }}">

```

### [A Note on Optional Fields](https://laravel.com/docs/12.x/validation#a-note-on-optional-fields)
By default, Laravel includes the `TrimStrings` and `ConvertEmptyStringsToNull` middleware in your application's global middleware stack. Because of this, you will often need to mark your "optional" request fields as `nullable` if you do not want the validator to consider `null` values as invalid. For example:
```


1$request->validate([




2    'title' => 'required|unique:posts|max:255',




3    'body' => 'required',




4    'publish_at' => 'nullable|date',




5]);




$request->validate([
    'title' => 'required|unique:posts|max:255',
    'body' => 'required',
    'publish_at' => 'nullable|date',
]);

```

In this example, we are specifying that the `publish_at` field may be either `null` or a valid date representation. If the `nullable` modifier is not added to the rule definition, the validator would consider `null` an invalid date.
### [Validation Error Response Format](https://laravel.com/docs/12.x/validation#validation-error-response-format)
When your application throws a `Illuminate\Validation\ValidationException` exception and the incoming HTTP request is expecting a JSON response, Laravel will automatically format the error messages for you and return a `422 Unprocessable Entity` HTTP response.
Below, you can review an example of the JSON response format for validation errors. Note that nested error keys are flattened into "dot" notation format:
```


 1{




 2    "message": "The team name must be a string. (and 4 more errors)",




 3    "errors": {




 4        "team_name": [




 5            "The team name must be a string.",




 6            "The team name must be at least 1 characters."




 7        ],




 8        "authorization.role": [




 9            "The selected authorization.role is invalid."




10        ],




11        "users.0.email": [




12            "The users.0.email field is required."




13        ],




14        "users.2.email": [




15            "The users.2.email must be a valid email address."




16        ]




17    }




18}




{
    "message": "The team name must be a string. (and 4 more errors)",
    "errors": {
        "team_name": [
            "The team name must be a string.",
            "The team name must be at least 1 characters."
        ],
        "authorization.role": [
            "The selected authorization.role is invalid."
        ],
        "users.0.email": [
            "The users.0.email field is required."
        ],
        "users.2.email": [
            "The users.2.email must be a valid email address."
        ]
    }
}

```
