## How to Contribute[](https://nextjs.org/docs/community/contribution-guide#how-to-contribute)
The docs content can be found on the
### GitHub Workflow[](https://nextjs.org/docs/community/contribution-guide#github-workflow)
If you're new to GitHub, we recommend reading the
> **Good to know** : The underlying docs code lives in a private codebase that is synced to the Next.js public repo. This means that you can't preview the docs locally. However, you'll see your changes on [nextjs.org](https://nextjs.org/docs) after merging a pull request.
### Writing MDX[](https://nextjs.org/docs/community/contribution-guide#writing-mdx)
The docs are written in
### VSCode[](https://nextjs.org/docs/community/contribution-guide#vscode)
#### Previewing Changes Locally[](https://nextjs.org/docs/community/contribution-guide#previewing-changes-locally)
VSCode has a built-in markdown previewer that you can use to see your edits locally. To enable the previewer for MDX files, you'll need to add a configuration option to your user settings.
Open the command palette (`⌘ + ⇧ + P` on Mac or `Ctrl + Shift + P` on Windows) and search from `Preferences: Open User Settings (JSON)`.
Then, add the following line to your `settings.json` file:
settings.json
```
{
  "files.associations": {
    "*.mdx": "markdown"
  }
}
```

Next, open the command palette again, and search for `Markdown: Preview File` or `Markdown: Open Preview to the Side`. This will open a preview window where you can see your formatted changes.
#### Extensions[](https://nextjs.org/docs/community/contribution-guide#extensions)
We also recommend the following extensions for VSCode users:
### Review Process[](https://nextjs.org/docs/community/contribution-guide#review-process)
Once you've submitted your contribution, the Next.js or Developer Experience teams will review your changes, provide feedback, and merge the pull request when it's ready.
Please let us know if you have any questions or need further assistance in your PR's comments. Thank you for contributing to the Next.js docs and being a part of our community!
> **Tip:** Run `pnpm prettier-fix` to run Prettier before submitting your PR.
