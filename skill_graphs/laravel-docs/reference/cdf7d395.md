## [Testing](https://laravel.com/docs/12.x/prompts#testing)
Laravel provides a variety of methods for testing that your command displays the expected Prompt messages:
Pest PHPUnit
```


 1test('report generation', function () {




 2    $this->artisan('report:generate')




 3        ->expectsPromptsInfo('Welcome to the application!')




 4        ->expectsPromptsWarning('This action cannot be undone')




 5        ->expectsPromptsError('Something went wrong')




 6        ->expectsPromptsAlert('Important notice!')




 7        ->expectsPromptsIntro('Starting process...')




 8        ->expectsPromptsOutro('Process completed!')




 9        ->expectsPromptsTable(




10            headers: ['Name', 'Email'],




11            rows: [




12                ['Taylor Otwell', 'taylor@example.com'],




13                ['Jason Beggs', 'jason@example.com'],




14            ]




15        )




16        ->assertExitCode(0);




17});




test('report generation', function () {
    $this->artisan('report:generate')
        ->expectsPromptsInfo('Welcome to the application!')
        ->expectsPromptsWarning('This action cannot be undone')
        ->expectsPromptsError('Something went wrong')
        ->expectsPromptsAlert('Important notice!')
        ->expectsPromptsIntro('Starting process...')
        ->expectsPromptsOutro('Process completed!')
        ->expectsPromptsTable(
            headers: ['Name', 'Email'],
            rows: [
                ['Taylor Otwell', 'taylor@example.com'],
                ['Jason Beggs', 'jason@example.com'],
            ]
        )
        ->assertExitCode(0);
});

```

```


 1public function test_report_generation(): void




 2{




 3    $this->artisan('report:generate')




 4        ->expectsPromptsInfo('Welcome to the application!')




 5        ->expectsPromptsWarning('This action cannot be undone')




 6        ->expectsPromptsError('Something went wrong')




 7        ->expectsPromptsAlert('Important notice!')




 8        ->expectsPromptsIntro('Starting process...')




 9        ->expectsPromptsOutro('Process completed!')




10        ->expectsPromptsTable(




11            headers: ['Name', 'Email'],




12            rows: [




13                ['Taylor Otwell', 'taylor@example.com'],




14                ['Jason Beggs', 'jason@example.com'],




15            ]




16        )




17        ->assertExitCode(0);




18}




public function test_report_generation(): void
{
    $this->artisan('report:generate')
        ->expectsPromptsInfo('Welcome to the application!')
        ->expectsPromptsWarning('This action cannot be undone')
        ->expectsPromptsError('Something went wrong')
        ->expectsPromptsAlert('Important notice!')
        ->expectsPromptsIntro('Starting process...')
        ->expectsPromptsOutro('Process completed!')
        ->expectsPromptsTable(
            headers: ['Name', 'Email'],
            rows: [
                ['Taylor Otwell', 'taylor@example.com'],
                ['Jason Beggs', 'jason@example.com'],
            ]
        )
        ->assertExitCode(0);
}

```

Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/prompts#introduction)
  * [ Installation ](https://laravel.com/docs/12.x/prompts#installation)
  * [ Available Prompts ](https://laravel.com/docs/12.x/prompts#available-prompts)
    * [ Text ](https://laravel.com/docs/12.x/prompts#text)
    * [ Textarea ](https://laravel.com/docs/12.x/prompts#textarea)
    * [ Number ](https://laravel.com/docs/12.x/prompts#number)
    * [ Password ](https://laravel.com/docs/12.x/prompts#password)
    * [ Confirm ](https://laravel.com/docs/12.x/prompts#confirm)
    * [ Select ](https://laravel.com/docs/12.x/prompts#select)
    * [ Multi-select ](https://laravel.com/docs/12.x/prompts#multiselect)
    * [ Suggest ](https://laravel.com/docs/12.x/prompts#suggest)
    * [ Search ](https://laravel.com/docs/12.x/prompts#search)
    * [ Multi-search ](https://laravel.com/docs/12.x/prompts#multisearch)
    * [ Pause ](https://laravel.com/docs/12.x/prompts#pause)
  * [ Transforming Input Before Validation ](https://laravel.com/docs/12.x/prompts#transforming-input-before-validation)
  * [ Forms ](https://laravel.com/docs/12.x/prompts#forms)
  * [ Informational Messages ](https://laravel.com/docs/12.x/prompts#informational-messages)
  * [ Tables ](https://laravel.com/docs/12.x/prompts#tables)
  * [ Spin ](https://laravel.com/docs/12.x/prompts#spin)
  * [ Progress Bar ](https://laravel.com/docs/12.x/prompts#progress)
  * [ Clearing the Terminal ](https://laravel.com/docs/12.x/prompts#clear)
  * [ Terminal Considerations ](https://laravel.com/docs/12.x/prompts#terminal-considerations)
  * [ Unsupported Environments and Fallbacks ](https://laravel.com/docs/12.x/prompts#fallbacks)
  * [ Testing ](https://laravel.com/docs/12.x/prompts#testing)


[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [ More Partners ](https://partners.laravel.com)
