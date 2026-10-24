##  [Allowlist](https://vercel.com/docs/deployments/vercel-ignore#allowlist)[](https://vercel.com/docs/deployments/vercel-ignore#allowlist)
A typical `.vercelignore` file assumes all files are allowed and each entry is a pattern to ignore. Alternatively, you can ignore all files and each entry is a pattern to allow.
Add a wildcard `/*` as the first line in `.vercelignore` to ensure all directories and files in the project root are ignored. The following lines must then start with a `!` to invert the ignore action and ensure the directory or file is allowed.
.vercelignore
```
# Ignore everything (folders and files) on root only
/*
!api
!vercel.json
!*.html
```
