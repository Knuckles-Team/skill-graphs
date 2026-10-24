## File Structure[](https://nextjs.org/docs/community/contribution-guide#file-structure)
The docs use **file-system routing**. Each folder and files inside
The file structure reflects the navigation that you see on the site, and by default, navigation items are sorted alphabetically. However, we can change the order of the items by prepending a two-digit number (`00-`) to the folder or file name.
For example, in the [functions API Reference](https://nextjs.org/docs/app/api-reference/functions), the pages are sorted alphabetically because it makes it easier for developers to find a specific function:
```
04-functions
├── after.mdx
├── cacheLife.mdx
├── cacheTag.mdx
└── ...
```

But, in the [app router section](https://nextjs.org/docs/app), the files are prefixed with a two-digit number, sorted in the order developers should learn these concepts:
```
01-getting-started
├── 01-installation.mdx
├── 02-project-structure.mdx
├── 03-layouts-and-pages.mdx
└── ...
```

To quickly find a page, you can use `⌘ + P` (Mac) or `Ctrl + P` (Windows) to open the search bar on VSCode. Then, type the slug of the page you're looking for. E.g. `installation`
> **Why not use a manifest?**
> We considered using a manifest file (another popular way to generate the docs navigation), but we found that a manifest would quickly get out of sync with the files. File-system routing forces us to think about the structure of the docs and feels more native to Next.js.
