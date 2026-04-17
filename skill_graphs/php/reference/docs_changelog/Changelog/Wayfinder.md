## Wayfinder
The next version of
This version generates _far_ more TypeScript from your Laravel app than the previous version, including routes and controller actions, named routes, form requests, Eloquent models, PHP enums, Inertia.js page props, Inertia shared data, broadcast channels, broadcast events, environment variables, and more.
Two new packages used by Wayfinder were also introduced into public beta:
### Surveyor
```


 1use Laravel\Surveyor\Analyzer\Analyzer;




 2 



 3$analyzer = app(Analyzer::class);




 4 



 5// Analyze a file by path




 6$result = $analyzer->analyze('/path/to/your/File.php');




 7 



 8// Access the analyzed scope




 9$scope = $result->analyzed();




10 



11// Access the class result




12$classResult = $result->result();




use Laravel\Surveyor\Analyzer\Analyzer;

$analyzer = app(Analyzer::class);

// Analyze a file by path
$result = $analyzer->analyze('/path/to/your/File.php');

// Access the analyzed scope
$scope = $result->analyzed();

// Access the class result
$classResult = $result->result();

```

### Ranger
It uses Surveyor under the hood and extracts the results into detailed data transport objects for straightforward consumption.
```


 1use Laravel\Ranger\Ranger;




 2use Laravel\Ranger\Components;




 3use Illuminate\Support\Collection;




 4 



 5$ranger = app(Ranger::class);




 6 



 7// Register callbacks for individual items




 8$ranger->onRoute(function (Components\Route $route) {




 9    echo $route->uri();




10});




11 



12$ranger->onModel(function (Components\Model $model) {




13    foreach ($model->getAttributes() as $name => $type) {




14        //




15    }




16});




17 



18$ranger->onEnum(function (Components\Enum $enum) {




19    //




20});




21 



22$ranger->onBroadcastEvent(function (Components\BroadcastEvent $event) {




23    //




24});




25 



26// Or register callbacks for entire collections




27$ranger->onRoutes(function (Collection $routes) {




28    // Called once all of the routes have been discovered and processed




29});




30 



31$ranger->onModels(function (Collection $models) {




32    // Called once all of the models have been discovered and processed




33});




34 



35// Walk through the application and trigger all callbacks




36$ranger->walk();




use Laravel\Ranger\Ranger;
use Laravel\Ranger\Components;
use Illuminate\Support\Collection;

$ranger = app(Ranger::class);

// Register callbacks for individual items
$ranger->onRoute(function (Components\Route $route) {
    echo $route->uri();
});

$ranger->onModel(function (Components\Model $model) {
    foreach ($model->getAttributes() as $name => $type) {
        //
    }
});

$ranger->onEnum(function (Components\Enum $enum) {
    //
});

$ranger->onBroadcastEvent(function (Components\BroadcastEvent $event) {
    //
});

// Or register callbacks for entire collections
$ranger->onRoutes(function (Collection $routes) {
    // Called once all of the routes have been discovered and processed
});

$ranger->onModels(function (Collection $models) {
    // Called once all of the models have been discovered and processed
});

// Walk through the application and trigger all callbacks
$ranger->walk();

```

## Wayfinder
### Introduce Route Utility Types for Improved DX
Pull request by
```


1import type { RouteDefinition } from "@/wayfinder";




2 



3const sendRequest = (route: RouteDefinition<"post">) => {




4    //




5};




6 



7sendRequest(StorePostController());




import type { RouteDefinition } from "@/wayfinder";

const sendRequest = (route: RouteDefinition<"post">) => {
    //
};

sendRequest(StorePostController());

```

Utility types are now exported, making them easier to consume if your app requires them.
### Support for Providing Default URL Parameters via the Frontend
Pull request by
```


1setup({ el, App, props }) {




2  const root = createRoot(el);




3 



4  setUrlDefaults({




5    workspace: props.initialPage.props.workspace.slug




6  });




7 



8  root.render(<App {...props} />);




9},




setup({ el, App, props }) {
  const root = createRoot(el);

  setUrlDefaults({
    workspace: props.initialPage.props.workspace.slug
  });

  root.render(<App {...props} />);
},

```

In instances where Wayfinder is unable to determine the proper default URL params as defined by the server, you can now specify them on the client side using `setUrlDefaults`.
