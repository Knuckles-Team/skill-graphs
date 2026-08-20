## [Introduction](https://laravel.com/docs/12.x/passport#introduction)
This documentation assumes you are already familiar with OAuth2. If you do not know anything about OAuth2, consider familiarizing yourself with the general
### [Passport or Sanctum?](https://laravel.com/docs/12.x/passport#passport-or-sanctum)
Before getting started, you may wish to determine if your application would be better served by Laravel Passport or [Laravel Sanctum](https://laravel.com/docs/12.x/sanctum). If your application absolutely needs to support OAuth2, then you should use Laravel Passport.
However, if you are attempting to authenticate a single-page application, mobile application, or issue API tokens, you should use [Laravel Sanctum](https://laravel.com/docs/12.x/sanctum). Laravel Sanctum does not support OAuth2; however, it provides a much simpler API authentication development experience.
