## Horizon
### Add `horizon:listen` Command
Pull request by
Introducing a new `horizon:listen` command that watches for file changes and automatically restarts [Horizon](https://laravel.com/docs/horizon) during development. This new command mirrors Laravel's built-in `queue:listen` command behavior.
## Horizon
### Allow Naming of Horizon Instances
Pull request by
When you have several [Horizon](https://laravel.com/docs/horizon#running-horizon) instances running in different regions, all within a single application, it can be difficult to determine with instance of Horizon a notification is originating from. You can now specify a name for each instance, making identification straightforward.
Before:
```


1Long Wait Detected




2[Nightwatch] The "{queue}" queue on the "{connection}" connection has a wait time of {seconds} seconds.




Long Wait Detected
[Nightwatch] The "{queue}" queue on the "{connection}" connection has a wait time of {seconds} seconds.

```

After:
```


1Long Wait Detected




2[eu-central-1] The "{queue}" queue on the "{connection}" connection has a wait time of {seconds} seconds.




Long Wait Detected
[eu-central-1] The "{queue}" queue on the "{connection}" connection has a wait time of {seconds} seconds.

```
