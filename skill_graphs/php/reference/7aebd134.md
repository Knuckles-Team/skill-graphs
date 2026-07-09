## [Events](https://laravel.com/docs/12.x/authentication#events)
Laravel dispatches a variety of [events](https://laravel.com/docs/12.x/events) during the authentication process. You may [define listeners](https://laravel.com/docs/12.x/events) for any of the following events:
Event Name
---
`Illuminate\Auth\Events\Registered`
`Illuminate\Auth\Events\Attempting`
`Illuminate\Auth\Events\Authenticated`
`Illuminate\Auth\Events\Login`
`Illuminate\Auth\Events\Failed`
`Illuminate\Auth\Events\Validated`
`Illuminate\Auth\Events\Verified`
`Illuminate\Auth\Events\Logout`
`Illuminate\Auth\Events\CurrentDeviceLogout`
`Illuminate\Auth\Events\OtherDeviceLogout`
`Illuminate\Auth\Events\Lockout`
`Illuminate\Auth\Events\PasswordReset`
`Illuminate\Auth\Events\PasswordResetLinkSent`
Copy as markdown
  * [ Introduction ](https://laravel.com/docs/12.x/authentication#introduction)
    * [ Starter Kits ](https://laravel.com/docs/12.x/authentication#starter-kits)
    * [ Database Considerations ](https://laravel.com/docs/12.x/authentication#introduction-database-considerations)
    * [ Ecosystem Overview ](https://laravel.com/docs/12.x/authentication#ecosystem-overview)
  * [ Authentication Quickstart ](https://laravel.com/docs/12.x/authentication#authentication-quickstart)
    * [ Install a Starter Kit ](https://laravel.com/docs/12.x/authentication#install-a-starter-kit)
    * [ Retrieving the Authenticated User ](https://laravel.com/docs/12.x/authentication#retrieving-the-authenticated-user)
    * [ Protecting Routes ](https://laravel.com/docs/12.x/authentication#protecting-routes)
    * [ Login Throttling ](https://laravel.com/docs/12.x/authentication#login-throttling)
  * [ Manually Authenticating Users ](https://laravel.com/docs/12.x/authentication#authenticating-users)
    * [ Remembering Users ](https://laravel.com/docs/12.x/authentication#remembering-users)
    * [ Other Authentication Methods ](https://laravel.com/docs/12.x/authentication#other-authentication-methods)
  * [ HTTP Basic Authentication ](https://laravel.com/docs/12.x/authentication#http-basic-authentication)
    * [ Stateless HTTP Basic Authentication ](https://laravel.com/docs/12.x/authentication#stateless-http-basic-authentication)
  * [ Logging Out ](https://laravel.com/docs/12.x/authentication#logging-out)
    * [ Invalidating Sessions on Other Devices ](https://laravel.com/docs/12.x/authentication#invalidating-sessions-on-other-devices)
  * [ Password Confirmation ](https://laravel.com/docs/12.x/authentication#password-confirmation)
    * [ Configuration ](https://laravel.com/docs/12.x/authentication#password-confirmation-configuration)
    * [ Routing ](https://laravel.com/docs/12.x/authentication#password-confirmation-routing)
    * [ Protecting Routes ](https://laravel.com/docs/12.x/authentication#password-confirmation-protecting-routes)
  * [ Adding Custom Guards ](https://laravel.com/docs/12.x/authentication#adding-custom-guards)
    * [ Closure Request Guards ](https://laravel.com/docs/12.x/authentication#closure-request-guards)
  * [ Adding Custom User Providers ](https://laravel.com/docs/12.x/authentication#adding-custom-user-providers)
    * [ The User Provider Contract ](https://laravel.com/docs/12.x/authentication#the-user-provider-contract)
    * [ The Authenticatable Contract ](https://laravel.com/docs/12.x/authentication#the-authenticatable-contract)
  * [ Automatic Password Rehashing ](https://laravel.com/docs/12.x/authentication#automatic-password-rehashing)
  * [ Social Authentication ](https://laravel.com/docs/12.x/socialite)
  * [ Events ](https://laravel.com/docs/12.x/authentication#events)


[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
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
  *   * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [ More Partners ](https://partners.laravel.com)
