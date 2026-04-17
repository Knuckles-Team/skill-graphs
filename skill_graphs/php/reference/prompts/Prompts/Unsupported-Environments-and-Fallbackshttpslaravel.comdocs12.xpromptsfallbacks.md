## [Unsupported Environments and Fallbacks](https://laravel.com/docs/12.x/prompts#fallbacks)
Laravel Prompts supports macOS, Linux, and Windows with WSL. Due to limitations in the Windows version of PHP, it is not currently possible to use Laravel Prompts on Windows outside of WSL.
For this reason, Laravel Prompts supports falling back to an alternative implementation such as the
When using Laravel Prompts with the Laravel framework, fallbacks for each prompt have been configured for you and will be automatically enabled in unsupported environments.
#### [Fallback Conditions](https://laravel.com/docs/12.x/prompts#fallback-conditions)
If you are not using Laravel or need to customize when the fallback behavior is used, you may pass a boolean to the `fallbackWhen` static method on the `Prompt` class:
```


1use Laravel\Prompts\Prompt;




2 



3Prompt::fallbackWhen(




4    ! $input->isInteractive() || windows_os() || app()->runningUnitTests()




5);




use Laravel\Prompts\Prompt;

Prompt::fallbackWhen(
    ! $input->isInteractive() || windows_os() || app()->runningUnitTests()
);

```

#### [Fallback Behavior](https://laravel.com/docs/12.x/prompts#fallback-behavior)
If you are not using Laravel or need to customize the fallback behavior, you may pass a closure to the `fallbackUsing` static method on each prompt class:
```


 1use Laravel\Prompts\TextPrompt;




 2use Symfony\Component\Console\Question\Question;




 3use Symfony\Component\Console\Style\SymfonyStyle;




 4 



 5TextPrompt::fallbackUsing(function (TextPrompt $prompt) use ($input, $output) {




 6    $question = (new Question($prompt->label, $prompt->default ?: null))




 7        ->setValidator(function ($answer) use ($prompt) {




 8            if ($prompt->required && $answer === null) {




 9                throw new \RuntimeException(




10                    is_string($prompt->required) ? $prompt->required : 'Required.'




11                );




12            }




13 



14            if ($prompt->validate) {




15                $error = ($prompt->validate)($answer ?? '');




16 



17                if ($error) {




18                    throw new \RuntimeException($error);




19                }




20            }




21 



22            return $answer;




23        });




24 



25    return (new SymfonyStyle($input, $output))




26        ->askQuestion($question);




27});




use Laravel\Prompts\TextPrompt;
use Symfony\Component\Console\Question\Question;
use Symfony\Component\Console\Style\SymfonyStyle;

TextPrompt::fallbackUsing(function (TextPrompt $prompt) use ($input, $output) {
    $question = (new Question($prompt->label, $prompt->default ?: null))
        ->setValidator(function ($answer) use ($prompt) {
            if ($prompt->required && $answer === null) {
                throw new \RuntimeException(
                    is_string($prompt->required) ? $prompt->required : 'Required.'
                );
            }

            if ($prompt->validate) {
                $error = ($prompt->validate)($answer ?? '');

                if ($error) {
                    throw new \RuntimeException($error);
                }
            }

            return $answer;
        });

    return (new SymfonyStyle($input, $output))
        ->askQuestion($question);
});

```

Fallbacks must be configured individually for each prompt class. The closure will receive an instance of the prompt class and must return an appropriate type for the prompt.
