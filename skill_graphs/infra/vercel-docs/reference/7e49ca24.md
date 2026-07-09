##  [Cannot load project settings](https://vercel.com/docs/getting-started-with-vercel#cannot-load-project-settings)[](https://vercel.com/docs/getting-started-with-vercel#cannot-load-project-settings)
If the Project configuration in `.vercel` belongs to a team you are not a member of, attempting to deploy the project will result in an error.
This can occur if you clone a Git repository that includes the `.vercel` directory, or you are logged in to the wrong Vercel account. Additionally, authentication issues can occur if you don't comply with the [two-factor enforcement](https://vercel.com/docs/two-factor-enforcement) policy of your team.
To fix, remove the `.vercel` directory and redeploy to link the project again by running these commands.
On macOS and Linux:
```
rm -rf .vercel
```
```
vercel
```

On Windows:
```
rmdir /s /q .vercel
```
```
vercel
```
