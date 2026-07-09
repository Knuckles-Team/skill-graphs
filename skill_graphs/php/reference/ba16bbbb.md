## [Failover](https://laravel.com/docs/12.x/ai-sdk#failover)
When prompting or generating other media, you may provide an array of providers / models to automatically failover to a backup provider / model if a service interruption or rate limit is encountered on the primary provider:
```


 1use App\Ai\Agents\SalesCoach;




 2use Laravel\Ai\Image;




 3 



 4$response = (new SalesCoach)->prompt(




 5    'Analyze this sales transcript...',




 6    provider: [Lab::OpenAI, Lab::Anthropic],




 7);




 8 



 9$image = Image::of('A donut sitting on the kitchen counter')




10    ->generate(provider: [Lab::Gemini, Lab::xAI]);




use App\Ai\Agents\SalesCoach;
use Laravel\Ai\Image;

$response = (new SalesCoach)->prompt(
    'Analyze this sales transcript...',
    provider: [Lab::OpenAI, Lab::Anthropic],
);

$image = Image::of('A donut sitting on the kitchen counter')
    ->generate(provider: [Lab::Gemini, Lab::xAI]);

```
