[![Laravel](https://laravel.com/img/logotype.min.svg)](https://laravel.com/)
  * Framework
  * Products
  * Resources
  * Events
  * [Docs](https://laravel.com/docs)


Sign in
[![Laravel](https://laravel.com/img/logotype.min.svg)](https://laravel.com/)
  * Framework
  * Products
  * Resources
  * [Events](https://laravel.com/community)
  * [Docs](https://laravel.com/docs)


  * [Overview](https://laravel.com/)
  * [Starter Kits](https://laravel.com/starter-kits)
  * [Release Notes](https://laravel.com/docs/releases)
  * [Documentation](https://laravel.com/docs)
  * [Laravel Learn](https://laravel.com/learn)


  * [Laravel Cloud](https://cloud.laravel.com)
  * [Forge](https://forge.laravel.com)
  * [Nightwatch](https://nightwatch.laravel.com)
  * [Nova](https://nova.laravel.com)


  * [Blog](https://laravel.com/blog)
  * [Careers](https://laravel.com/careers)
  * [Trust](https://trust.laravel.com)
  * [Legal](https://laravel.com/legal)
  * [Status](https://status.laravel.com)


Search docs
Search`K`
`⌘K`
# The clean stack for Artisans and agents.
Laravel is batteries-included so everyone can build and ship web apps at ridiculous speed.
[Deploy on Cloud ](https://cloud.laravel.com)[View framework docs](https://laravel.com/docs)
v13.laravel.cloudskills.laravel.cloud
Powering ideas for the best & brightest
## Ship web apps with the
AI-enabled
framework
We’re ready when you’re ready
### A framework for developers and agents
Laravel has opinions on everything: routing, queues, authentication, and more. That's thousands of decisions an agent doesn't have to make. The result? Clean code that anyone can understand.
  * Starter kits for React, Vue, and Svelte
  * AI SDK and Boost AI assistant
  * Database ORM, queues, routing, and more
  * Open source ecosystem of over 30 packages


[Explore the framework](https://laravel.com/docs/12.x)
  * Auth
  * AI SDK
  * ORM
  * Migrations
  * Validation
  * Storage
  * Queues
  * Testing


web.php
UserController.php
```
Route::get('/dashboard', function (Request $request) {
    $user = $request->user();

    return view('dashboard', ['user' => $user]);
})->middleware('auth');
```

```
class FlightController
{
    #[Middleware('auth')]
    #[Authorize('view', 'flight')]
    public function show(Flight $flight): View
    {
        return view('dashboard', ['user' => $user]);
    }
}
```

### Laravel Cloud takes you from local to live in seconds
No more guessing how many servers you need: autoscale up under load and hibernate when idle. Only pay for what you actually use.
  * Full control via dashboard or CLI
  * Instantly add databases, workers, cache, and storage

[Explore Laravel Cloud](https://cloud.laravel.com)
01100010 01100101 0110010101100010 01100101 01100101
### Check pull requests from your team (or agents) in preview environments
Review every change in Cloud’s zero-risk, production-like preview environment before it ever hits your main branch.
  * Integrates seamlessly with GitHub Actions
  * Test migrations and heavy changes safely

[Explore Preview Environments](https://cloud.laravel.com/docs/environments#preview-environments)
laravel-ai.laravel.cloudskills.laravel.cloud
### Monitor and fix issues with Nightwatch
Laravel Nightwatch gives full observability to find errors and top performance issues in your apps, before your team does.
  * Fix errors and performance with recommended solutions
  * Trace requests, jobs, logs, commands, cache, and more
  * Let agents fix your code using Nightwatch MCP

[Explore Nightwatch](https://nightwatch.laravel.com)
![Nightwatch dashboard screenshot](https://laravel.com/build/assets/nightwatch-dashboard-BtrDybCK.avif)
### The best partner to any front-end
Easily craft frontend experiences with React, Vue, or Svelte alongside Laravel and Inertia. Or, accelerate your front-end development with Livewire.
[Explore front-ends](https://laravel.com/docs/frontend)
users.svelteusers.tsxusers.vueusers.blade.php
## Create without limits. What will you ship?
[Deploy on Cloud ](https://cloud.laravel.com)[View framework docs](https://laravel.com/docs)
## Trusted by millions of developers all over the world
> “I've been using Laravel for nearly a decade and have never been tempted to switch to anything else.”
Adam WathanFounder, Tailwind
![Adam Wathan](https://laravel.com/images/home/community/adam-wathan.png)
> “Laravel is our sourdough starter and multitool for web projects large and small. 10 years in, it remains fresh and useful.”
Ian CallahanHarvard Art Museums
![Ian Callahan](https://laravel.com/images/home/community/ian-callahan.jpg)
> “Laravel takes the pain out of building modern, scalable web apps.”
Aaron FrancisCo-founder, Try Hard Studios
![Aaron Francis](https://laravel.com/images/home/community/aaron-francis.png)
> “Laravel's elegance, performance, and developer experience are unmatched.”
Chandresh PatelCEO, Bacancy
![Chandresh Patel](https://laravel.com/images/home/community/chandresh-patel.jpg)
> “The Laravel ecosystem has been integral to the success of our business. The framework allows us to move fast and ship regularly.”
Jack EllisFounder, Fathom Analytics
![Jack Ellis](https://laravel.com/images/home/community/jack-ellis.png)
> “Laravel is a breath of fresh air in the PHP ecosystem, with a brilliant community around it.”
Erika HeidiCreator, Minicli
![Erika Heidi](https://laravel.com/images/home/community/erika-heidi.png)
> “The framework, the ecosystem and the community - it's the perfect package.”
Zuzana KunckovaFounder, Larabelles
![Zuzana Kunckova](https://laravel.com/images/home/community/zuzana-kunckova.jpg)
[ Events ]
## We’ll see you in London
Laravel is best known for its amazing community, where online friendships transform into real-world connections at Laracons, Lives, and meetups in over 34 countries.
[Find nearby meetups](https://laravel.com/events)
![](https://fls-9f826fcc-b2ad-40d8-813f-9cf7dac049fa.laravel.cloud/events/images/01KJTM5WE070343MAP184XDC0R.webp)
![Laravel Live Japan](https://fls-9f826fcc-b2ad-40d8-813f-9cf7dac049fa.laravel.cloud/events/images/01KJTN27BNG5GW88HBV3NPRC7E.svg)
May 26-272026TokyoJP
![](https://fls-9f826fcc-b2ad-40d8-813f-9cf7dac049fa.laravel.cloud/events/images/01KJTND1XHZK0Y2SZ62000KWC1.webp)
![Laravel Live UK](https://fls-9f826fcc-b2ad-40d8-813f-9cf7dac049fa.laravel.cloud/events/images/01KJXH1FBQXXM8SWA9ZZ37EJYF.svg)
Jun 18-192026LondonUK
![](https://fls-9f826fcc-b2ad-40d8-813f-9cf7dac049fa.laravel.cloud/events/images/01KJTHP4Y8HZY0Q756GQBKZ6RH.webp)
![Laracon US](https://fls-9f826fcc-b2ad-40d8-813f-9cf7dac049fa.laravel.cloud/events/images/01KJTN340Y077CJZKJ23F0VB1A.svg)
Jul 28-292026BostonUS
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
  *   * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [ More Partners ](https://partners.laravel.com)
