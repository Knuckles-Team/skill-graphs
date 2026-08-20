## Starter Kits
We made a slew of updates to all of our Starter Kits this month! Amongst the various tune-ups:
### Add Safer Defaults to `AppServiceProvider`
Pull request by
Safer defaults in the `AppServiceProvider` reduce the "oops" factor on new projects, helping you start with a more secure, production-friendly baseline while keeping the kit lightweight and easy to customize.
- Enforcing immutable dates with `CarbonImmutable`
- Not allowing destructive commands in production
- Requiring safer passwords by default in production
### Livewire 4 Support
Pull request by
The Livewire starter kits are now ready for Livewire 4, so you can begin new builds on the latest Livewire foundation without spending time on upgrade plumbing. If you're planning a fresh app, this keeps your starting line modern.
### Add Pint Config File and Util Composer Scripts for Linting
Pull request by
Out-of-the-box linting makes teams faster: consistent formatting, fewer style nits in code review, and easier onboarding. The included [Pint](https://laravel.com/docs/pint) config plus utility scripts make "format everything" a one-command habit.
## Starter Kits
### Integration of Additional Fortify Features
Pull requests by
All starter kits now use Fortify for login, registration, password reset, and email verification. Fortify is a battle-tested solution, removing code from your codebase that is rarely changed, keeping your application code streamlined and maintainable.
