## [Creating Resources](https://laravel.com/docs/12.x/mcp#creating-resources)
To create a resource, run the `make:mcp-resource` Artisan command:
```


1php artisan make:mcp-resource WeatherGuidelinesResource




php artisan make:mcp-resource WeatherGuidelinesResource

```

After creating a resource, register it in your server's `$resources` property:
```


 1<?php




 2 



 3namespace App\Mcp\Servers;




 4 



 5use App\Mcp\Resources\WeatherGuidelinesResource;




 6use Laravel\Mcp\Server;




 7 



 8class WeatherServer extends Server




 9{




10    /**




11     * The resources registered with this MCP server.




12     *




13     * @var array<int, class-string<\Laravel\Mcp\Server\Resource>>




14     */




15    protected array $resources = [




16        WeatherGuidelinesResource::class,




17    ];




18}




<?php

namespace App\Mcp\Servers;

use App\Mcp\Resources\WeatherGuidelinesResource;
use Laravel\Mcp\Server;

class WeatherServer extends Server
{
    /**
     * The resources registered with this MCP server.
     *
     * @var array<int, class-string<\Laravel\Mcp\Server\Resource>>
     */
    protected array $resources = [
        WeatherGuidelinesResource::class,
    ];
}

```

#### [Resource Name, Title, and Description](https://laravel.com/docs/12.x/mcp#resource-name-title-and-description)
By default, the resource's name and title are derived from the class name. For example, `WeatherGuidelinesResource` will have a name of `weather-guidelines` and a title of `Weather Guidelines Resource`. You may customize these values using the `Name` and `Title` attributes:
```


1use Laravel\Mcp\Server\Attributes\Name;




2use Laravel\Mcp\Server\Attributes\Title;




3 



4#[Name('weather-api-docs')]




5#[Title('Weather API Documentation')]




6class WeatherGuidelinesResource extends Resource




7{




8    // ...




9}




use Laravel\Mcp\Server\Attributes\Name;
use Laravel\Mcp\Server\Attributes\Title;

#[Name('weather-api-docs')]
#[Title('Weather API Documentation')]
class WeatherGuidelinesResource extends Resource
{
    // ...
}

```

Resource descriptions are not automatically generated. You should always provide a meaningful description using the `Description` attribute:
```


1use Laravel\Mcp\Server\Attributes\Description;




2 



3#[Description('Comprehensive guidelines for using the Weather API.')]




4class WeatherGuidelinesResource extends Resource




5{




6    //




7}




use Laravel\Mcp\Server\Attributes\Description;

#[Description('Comprehensive guidelines for using the Weather API.')]
class WeatherGuidelinesResource extends Resource
{
    //
}

```

The description is a critical part of the resource's metadata, as it helps AI models understand when and how to use the resource effectively.
### [Resource Templates](https://laravel.com/docs/12.x/mcp#resource-templates)
#### [Creating Resource Templates](https://laravel.com/docs/12.x/mcp#creating-resource-templates)
To create a resource template, implement the `HasUriTemplate` interface on your resource class and define a `uriTemplate` method that returns a `UriTemplate` instance:
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Response;




 7use Laravel\Mcp\Server\Attributes\Description;




 8use Laravel\Mcp\Server\Attributes\MimeType;




 9use Laravel\Mcp\Server\Contracts\HasUriTemplate;




10use Laravel\Mcp\Server\Resource;




11use Laravel\Mcp\Support\UriTemplate;




12 



13#[Description('Access user files by ID')]




14#[MimeType('text/plain')]




15class UserFileResource extends Resource implements HasUriTemplate




16{




17    /**




18     * Get the URI template for this resource.




19     */




20    public function uriTemplate(): UriTemplate




21    {




22        return new UriTemplate('file://users/{userId}/files/{fileId}');




23    }




24 



25    /**




26     * Handle the resource request.




27     */




28    public function handle(Request $request): Response




29    {




30        $userId = $request->get('userId');




31        $fileId = $request->get('fileId');




32 



33        // Fetch and return the file content...




34 



35        return Response::text($content);




36    }




37}




<?php

namespace App\Mcp\Resources;

use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Attributes\Description;
use Laravel\Mcp\Server\Attributes\MimeType;
use Laravel\Mcp\Server\Contracts\HasUriTemplate;
use Laravel\Mcp\Server\Resource;
use Laravel\Mcp\Support\UriTemplate;

#[Description('Access user files by ID')]
#[MimeType('text/plain')]
class UserFileResource extends Resource implements HasUriTemplate
{
    /**
     * Get the URI template for this resource.
     */
    public function uriTemplate(): UriTemplate
    {
        return new UriTemplate('file://users/{userId}/files/{fileId}');
    }

    /**
     * Handle the resource request.
     */
    public function handle(Request $request): Response
    {
        $userId = $request->get('userId');
        $fileId = $request->get('fileId');

        // Fetch and return the file content...

        return Response::text($content);
    }
}

```

When a resource implements the `HasUriTemplate` interface, it will be registered as a resource template rather than a static resource. AI clients can then request resources using URIs that match the template pattern, and the variables from the URI will be automatically extracted and made available in your resource's `handle` method.
#### [URI Template Syntax](https://laravel.com/docs/12.x/mcp#uri-template-syntax)
URI templates use placeholders enclosed in curly braces to define variable segments in the URI:
```


1new UriTemplate('file://users/{userId}');




2new UriTemplate('file://users/{userId}/files/{fileId}');




3new UriTemplate('https://api.example.com/{version}/{resource}/{id}');




new UriTemplate('file://users/{userId}');
new UriTemplate('file://users/{userId}/files/{fileId}');
new UriTemplate('https://api.example.com/{version}/{resource}/{id}');

```

#### [Accessing Template Variables](https://laravel.com/docs/12.x/mcp#accessing-template-variables)
When a URI matches your resource template, the extracted variables are automatically merged into the request and can be accessed using the `get` method:
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Response;




 7use Laravel\Mcp\Server\Contracts\HasUriTemplate;




 8use Laravel\Mcp\Server\Resource;




 9use Laravel\Mcp\Support\UriTemplate;




10 



11class UserProfileResource extends Resource implements HasUriTemplate




12{




13    public function uriTemplate(): UriTemplate




14    {




15        return new UriTemplate('file://users/{userId}/profile');




16    }




17 



18    public function handle(Request $request): Response




19    {




20        // Access the extracted variable




21        $userId = $request->get('userId');




22 



23        // Access the full URI if needed




24        $uri = $request->uri();




25 



26        // Fetch user profile...




27 



28        return Response::text("Profile for user {$userId}");




29    }




30}




<?php

namespace App\Mcp\Resources;

use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Contracts\HasUriTemplate;
use Laravel\Mcp\Server\Resource;
use Laravel\Mcp\Support\UriTemplate;

class UserProfileResource extends Resource implements HasUriTemplate
{
    public function uriTemplate(): UriTemplate
    {
        return new UriTemplate('file://users/{userId}/profile');
    }

    public function handle(Request $request): Response
    {
        // Access the extracted variable
        $userId = $request->get('userId');

        // Access the full URI if needed
        $uri = $request->uri();

        // Fetch user profile...

        return Response::text("Profile for user {$userId}");
    }
}

```

The `Request` object provides both the extracted variables and the original URI that was requested, giving you full context for processing the resource request.
### [Resource URI and MIME Type](https://laravel.com/docs/12.x/mcp#resource-uri-and-mime-type)
Each resource is identified by a unique URI and has an associated MIME type that helps AI clients understand the resource's format.
By default, the resource's URI is generated based on the resource's name, so `WeatherGuidelinesResource` will have a URI of `weather://resources/weather-guidelines`. The default MIME type is `text/plain`.
You may customize these values using the `Uri` and `MimeType` attributes:
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use Laravel\Mcp\Server\Attributes\MimeType;




 6use Laravel\Mcp\Server\Attributes\Uri;




 7use Laravel\Mcp\Server\Resource;




 8 



 9#[Uri('weather://resources/guidelines')]




10#[MimeType('application/pdf')]




11class WeatherGuidelinesResource extends Resource




12{




13}




<?php

namespace App\Mcp\Resources;

use Laravel\Mcp\Server\Attributes\MimeType;
use Laravel\Mcp\Server\Attributes\Uri;
use Laravel\Mcp\Server\Resource;

#[Uri('weather://resources/guidelines')]
#[MimeType('application/pdf')]
class WeatherGuidelinesResource extends Resource
{
}

```

The URI and MIME type help AI clients determine how to process and interpret the resource content appropriately.
### [Resource Request](https://laravel.com/docs/12.x/mcp#resource-request)
Unlike tools and prompts, resources can not define input schemas or arguments. However, you can still interact with request object within your resource's `handle` method:
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Response;




 7use Laravel\Mcp\Server\Resource;




 8 



 9class WeatherGuidelinesResource extends Resource




10{




11    /**




12     * Handle the resource request.




13     */




14    public function handle(Request $request): Response




15    {




16        // ...




17    }




18}




<?php

namespace App\Mcp\Resources;

use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Resource;

class WeatherGuidelinesResource extends Resource
{
    /**
     * Handle the resource request.
     */
    public function handle(Request $request): Response
    {
        // ...
    }
}

```

### [Resource Dependency Injection](https://laravel.com/docs/12.x/mcp#resource-dependency-injection)
The Laravel [service container](https://laravel.com/docs/12.x/container) is used to resolve all resources. As a result, you are able to type-hint any dependencies your resource may need in its constructor. The declared dependencies will automatically be resolved and injected into the resource instance:
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use App\Repositories\WeatherRepository;




 6use Laravel\Mcp\Server\Resource;




 7 



 8class WeatherGuidelinesResource extends Resource




 9{




10    /**




11     * Create a new resource instance.




12     */




13    public function __construct(




14        protected WeatherRepository $weather,




15    ) {}




16 



17    // ...




18}




<?php

namespace App\Mcp\Resources;

use App\Repositories\WeatherRepository;
use Laravel\Mcp\Server\Resource;

class WeatherGuidelinesResource extends Resource
{
    /**
     * Create a new resource instance.
     */
    public function __construct(
        protected WeatherRepository $weather,
    ) {}

    // ...
}

```

In addition to constructor injection, you may also type-hint dependencies in your resource's `handle` method. The service container will automatically resolve and inject the dependencies when the method is called:
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use App\Repositories\WeatherRepository;




 6use Laravel\Mcp\Request;




 7use Laravel\Mcp\Response;




 8use Laravel\Mcp\Server\Resource;




 9 



10class WeatherGuidelinesResource extends Resource




11{




12    /**




13     * Handle the resource request.




14     */




15    public function handle(WeatherRepository $weather): Response




16    {




17        $guidelines = $weather->guidelines();




18 



19        return Response::text($guidelines);




20    }




21}




<?php

namespace App\Mcp\Resources;

use App\Repositories\WeatherRepository;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Resource;

class WeatherGuidelinesResource extends Resource
{
    /**
     * Handle the resource request.
     */
    public function handle(WeatherRepository $weather): Response
    {
        $guidelines = $weather->guidelines();

        return Response::text($guidelines);
    }
}

```

### [Resource Annotations](https://laravel.com/docs/12.x/mcp#resource-annotations)
You may enhance your resources with
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use Laravel\Mcp\Enums\Role;




 6use Laravel\Mcp\Server\Annotations\Audience;




 7use Laravel\Mcp\Server\Annotations\LastModified;




 8use Laravel\Mcp\Server\Annotations\Priority;




 9use Laravel\Mcp\Server\Resource;




10 



11#[Audience(Role::User)]




12#[LastModified('2025-01-12T15:00:58Z')]




13#[Priority(0.9)]




14class UserDashboardResource extends Resource




15{




16    //




17}




<?php

namespace App\Mcp\Resources;

use Laravel\Mcp\Enums\Role;
use Laravel\Mcp\Server\Annotations\Audience;
use Laravel\Mcp\Server\Annotations\LastModified;
use Laravel\Mcp\Server\Annotations\Priority;
use Laravel\Mcp\Server\Resource;

#[Audience(Role::User)]
#[LastModified('2025-01-12T15:00:58Z')]
#[Priority(0.9)]
class UserDashboardResource extends Resource
{
    //
}

```

Available annotations include:
Annotation | Type | Description
---|---|---
`#[Audience]` | Role or array | Specifies the intended audience (`Role::User`, `Role::Assistant`, or both).
`#[Priority]` | float | A numerical score between 0.0 and 1.0 indicating resource importance.
`#[LastModified]` | string | An ISO 8601 timestamp showing when the resource was last updated.
### [Conditional Resource Registration](https://laravel.com/docs/12.x/mcp#conditional-resource-registration)
You may conditionally register resources at runtime by implementing the `shouldRegister` method in your resource class. This method allows you to determine whether a resource should be available based on application state, configuration, or request parameters:
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use Laravel\Mcp\Request;




 6use Laravel\Mcp\Server\Resource;




 7 



 8class WeatherGuidelinesResource extends Resource




 9{




10    /**




11     * Determine if the resource should be registered.




12     */




13    public function shouldRegister(Request $request): bool




14    {




15        return $request?->user()?->subscribed() ?? false;




16    }




17}




<?php

namespace App\Mcp\Resources;

use Laravel\Mcp\Request;
use Laravel\Mcp\Server\Resource;

class WeatherGuidelinesResource extends Resource
{
    /**
     * Determine if the resource should be registered.
     */
    public function shouldRegister(Request $request): bool
    {
        return $request?->user()?->subscribed() ?? false;
    }
}

```

When a resource's `shouldRegister` method returns `false`, it will not appear in the list of available resources and cannot be accessed by AI clients.
### [Resource Responses](https://laravel.com/docs/12.x/mcp#resource-responses)
Resources must return an instance of `Laravel\Mcp\Response`. The Response class provides several convenient methods for creating different types of responses:
For simple text content, use the `text` method:
```


 1use Laravel\Mcp\Request;




 2use Laravel\Mcp\Response;




 3 



 4/**




 5 * Handle the resource request.




 6 */




 7public function handle(Request $request): Response




 8{




 9    // ...




10 



11    return Response::text($weatherData);




12}




use Laravel\Mcp\Request;
use Laravel\Mcp\Response;

/**
 * Handle the resource request.
 */
public function handle(Request $request): Response
{
    // ...

    return Response::text($weatherData);
}

```

#### [Blob Responses](https://laravel.com/docs/12.x/mcp#resource-blob-responses)
To return blob content, use the `blob` method, providing the blob content:
```


1return Response::blob(file_get_contents(storage_path('weather/radar.png')));




return Response::blob(file_get_contents(storage_path('weather/radar.png')));

```

When returning blob content, the MIME type will be determined by your resource's configured MIME type:
```


 1<?php




 2 



 3namespace App\Mcp\Resources;




 4 



 5use Laravel\Mcp\Server\Attributes\MimeType;




 6use Laravel\Mcp\Server\Resource;




 7 



 8#[MimeType('image/png')]




 9class WeatherGuidelinesResource extends Resource




10{




11    //




12}




<?php

namespace App\Mcp\Resources;

use Laravel\Mcp\Server\Attributes\MimeType;
use Laravel\Mcp\Server\Resource;

#[MimeType('image/png')]
class WeatherGuidelinesResource extends Resource
{
    //
}

```

#### [Error Responses](https://laravel.com/docs/12.x/mcp#resource-error-responses)
To indicate an error occurred during resource retrieval, use the `error()` method:
```


1return Response::error('Unable to fetch weather data for the specified location.');




return Response::error('Unable to fetch weather data for the specified location.');

```
