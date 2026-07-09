## Installer
### Pass Flags for Alternative Node Package Managers
Pull request by
When running `laravel new`, there are now additional flags you can pass to specify which Node package manager you'd like to use: `--npm`, `--pnpm`, `--bun`, or `--yarn`. Passing one of these flags will also update any `composer` script that references a Node command to reflect the correct command specific to the selected package manager.
## Installer
### Check for New Version of Installer on `new`
Pull request by
The installer now checks if there are updates available on Packagist to ensure you are using the latest version when running `laravel new`.
### Support PNPM and Yarn Package Managers
Pull request by
The installer now detects lock files for the PNPM and Yarn package managers, falling back to NPM if neither are found.
### Add the Ability to Use a Git Repo as Custom Kit
Pull request by
```


1laravel new --using https://github.com/user/project




laravel new --using https://github.com/user/project

```

You can specify a git repo as a custom starter kit when running `laravel new`.
