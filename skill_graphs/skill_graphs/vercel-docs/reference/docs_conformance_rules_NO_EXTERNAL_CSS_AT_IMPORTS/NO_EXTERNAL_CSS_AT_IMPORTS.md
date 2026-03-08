# NO_EXTERNAL_CSS_AT_IMPORTS
Last updated September 24, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Importing CSS through (
app.module.css
```
@import url('https://fonts.googleapis.com/css2?family=Inter');
```

This can result in a
Imports to relative paths are processed by frameworks like Next.js, and will not be affected by this issue.
app.module.css
```
/* This import is safe. */
@import './globals.css';
```

Note that this rule currently only parses CSS and not CSS written in Less, Sass, or other CSS preprocessor syntaxes.
