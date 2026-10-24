# How to use Sass
Last updated February 27, 2026
Next.js has built-in support for integrating with Sass after the package is installed using both the `.scss` and `.sass` extensions. You can use component-level Sass via CSS Modules and the `.module.scss`or `.module.sass` extension.
First, install
pnpmnpmyarnbun
Terminal
```
pnpm add -D sass
```

> **Good to know** :
> Sass supports `.scss` extension requires you use the `.sass` extension requires you use the
> If you're not sure which to choose, start with the `.scss` extension which is a superset of CSS, and doesn't require you learn the Indented Syntax ("Sass").
### Customizing Sass Options[](https://nextjs.org/docs/app/guides/sass#customizing-sass-options)
If you want to configure your Sass options, use `sassOptions` in `next.config`.
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  sassOptions: {
    additionalData: `$var: red;`,
  },
}

export default nextConfig
```

#### Implementation[](https://nextjs.org/docs/app/guides/sass#implementation)
You can use the `implementation` property to specify the Sass implementation to use. By default, Next.js uses the
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  sassOptions: {
    implementation: 'sass-embedded',
  },
}

export default nextConfig
```

### Sass Variables[](https://nextjs.org/docs/app/guides/sass#sass-variables)
Next.js supports Sass variables exported from CSS Module files.
For example, using the exported `primaryColor` Sass variable:
app/variables.module.scss
```
$primary-color: #64ff00;

:export {
  primaryColor: $primary-color;
}
```

app/page.js
```
// maps to root `/` URL

import variables from './variables.module.scss'

export default function Page() {
  return <h1 style={{ color: variables.primaryColor }}>Hello, Next.js!</h1>
}
```

[PreviousRedirecting](https://nextjs.org/docs/app/guides/redirecting)[NextScripts](https://nextjs.org/docs/app/guides/scripts)
Was this helpful?
Send
