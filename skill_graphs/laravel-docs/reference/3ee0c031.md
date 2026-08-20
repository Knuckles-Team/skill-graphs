## [Authorization](https://laravel.com/docs/12.x/mcp#authorization)
You may access the currently authenticated user via the `$request->user()` method, allowing you to perform [authorization checks](https://laravel.com/docs/12.x/authorization) within your MCP tools and resources:
```


 1use Laravel\Mcp\Request;




 2use Laravel\Mcp\Response;




 3 



 4/**




 5 * Handle the tool request.




 6 */




 7public function handle(Request $request): Response




 8{




 9    if (! $request->user()->can('read-weather')) {




10        return Response::error('Permission denied.');




11    }




12 



13    // ...




14}




use Laravel\Mcp\Request;
use Laravel\Mcp\Response;

/**
 * Handle the tool request.
 */
public function handle(Request $request): Response
{
    if (! $request->user()->can('read-weather')) {
        return Response::error('Permission denied.');
    }

    // ...
}

```
