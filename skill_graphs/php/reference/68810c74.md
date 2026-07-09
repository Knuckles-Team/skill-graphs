## [Events](https://laravel.com/docs/12.x/passport#events)
Passport raises events when issuing access tokens and refresh tokens. You may [listen for these events](https://laravel.com/docs/12.x/events) to prune or revoke other access tokens in your database:
Event Name
---
`Laravel\Passport\Events\AccessTokenCreated`
`Laravel\Passport\Events\AccessTokenRevoked`
`Laravel\Passport\Events\RefreshTokenCreated`
