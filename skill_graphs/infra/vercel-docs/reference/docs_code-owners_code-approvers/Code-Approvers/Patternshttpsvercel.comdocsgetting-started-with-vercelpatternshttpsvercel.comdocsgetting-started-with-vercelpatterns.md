##  [Patterns](https://vercel.com/docs/getting-started-with-vercel#patterns)[](https://vercel.com/docs/getting-started-with-vercel#patterns)
The `.vercel.approvers` file supports specifying files with a limited set of glob patterns:
  * [Directory](https://vercel.com/docs/getting-started-with-vercel#directory-default)
  * [Current Directory](https://vercel.com/docs/getting-started-with-vercel#current-directory-pattern)
  * [Globstar](https://vercel.com/docs/getting-started-with-vercel#globstar-pattern)
  * [Specifying multiple owners](https://vercel.com/docs/getting-started-with-vercel#specifying-multiple-owners-for-the-same-pattern)


The patterns are case-insensitive.
###  [Directory (default)](https://vercel.com/docs/getting-started-with-vercel#directory-default)[](https://vercel.com/docs/getting-started-with-vercel#directory-default)
The default empty pattern represents ownership of the current directory and all subdirectories.
.vercel.approvers
```
# Matches all files in the current directory and all subdirectories.
@owner
```

###  [Current Directory Pattern](https://vercel.com/docs/getting-started-with-vercel#current-directory-pattern)[](https://vercel.com/docs/getting-started-with-vercel#current-directory-pattern)
A pattern that matches a file or set of files in the current directory.
.vercel.approvers
```
# Matches the single `package.json` file in the current directory only.
package.json @package-owner

# Matches all javascript files in the current directory only.
*.js @js-owner
```

###  [Globstar Pattern](https://vercel.com/docs/getting-started-with-vercel#globstar-pattern)[](https://vercel.com/docs/getting-started-with-vercel#globstar-pattern)
The globstar pattern begins with `**/`. And represents ownership of files matching the glob in the current directory and its subdirectories.
.vercel.approvers
```
# Matches all `package.json` files in the current directory and its subdirectories.
**/package.json @package-owner

# Matches all javascript files in the current directory and its subdirectories.
**/*.js @js-owner
```

Code Owners files are meant to encourage distributed ownership definitions across a codebase. Thus, the globstar `**/` and `/` can only be used at the start of a pattern. They cannot be used in the middle of a pattern to enumerate subdirectories.
For example, the following patterns are not allowed:
.vercel.approvers
```
# Instead add a `.vercel.approvers` file in the `src` directory.
src/**/*.js @js-owner

# Instead add a `.vercel.approvers` file in the `src/pages` directory.
src/pages/index.js @js-owner
```

###  [Specifying multiple owners for the same pattern](https://vercel.com/docs/getting-started-with-vercel#specifying-multiple-owners-for-the-same-pattern)[](https://vercel.com/docs/getting-started-with-vercel#specifying-multiple-owners-for-the-same-pattern)
Each owner for the same pattern should be specified on separate lines. All owners listed will be able to approve for that pattern.
.vercel.approvers
```
# Both @package-owner and @org/team will be able to approve changes to the
# package.json file.
package.json @package-owner
package.json @org/team
```
