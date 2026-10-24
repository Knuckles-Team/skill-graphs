## Using Multiple Fonts[](https://nextjs.org/docs/pages/api-reference/edge#using-multiple-fonts)
You can import and use multiple fonts in your application. There are two approaches you can take.
The first approach is to create a utility function that exports a font, imports it, and applies its `className` where needed. This ensures the font is preloaded only when it's rendered:
app/fonts.ts
TypeScript
JavaScript TypeScript
```
import { Inter, Roboto_Mono } from 'next/font/google'

export const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
})
```

In the example above, `Inter` will be applied globally, and `Roboto Mono` can be imported and applied as needed.
Alternatively, you can create a [CSS variable](https://nextjs.org/docs/app/api-reference/components/font#variable) and use it with your preferred CSS solution:
app/global.css
```
html {
  font-family: var(--font-inter);
}

h1 {
  font-family: var(--font-roboto-mono);
}
```

In the example above, `Inter` will be applied globally, and any `<h1>` tags will be styled with `Roboto Mono`.
> **Recommendation** : Use multiple fonts conservatively since each new font is an additional resource the client has to download.
### Local Fonts[](https://nextjs.org/docs/pages/api-reference/edge#local-fonts)
Import `next/font/local` and specify the `src` of your local font file. We recommend using
pages/_app.js
```
import localFont from 'next/font/local'

// Font files can be colocated inside of `pages`
const myFont = localFont({ src: './my-font.woff2' })

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={myFont.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

If you want to use multiple files for a single font family, `src` can be an array:
```
const roboto = localFont({
  src: [
    {
      path: './Roboto-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './Roboto-Italic.woff2',
      weight: '400',
      style: 'italic',
    },
    {
      path: './Roboto-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
    {
      path: './Roboto-BoldItalic.woff2',
      weight: '700',
      style: 'italic',
    },
  ],
})
```

View the [Font API Reference](https://nextjs.org/docs/app/api-reference/components/font) for more information.
### With Tailwind CSS[](https://nextjs.org/docs/pages/api-reference/edge#with-tailwind-css)
`next/font` integrates seamlessly with [CSS variables](https://nextjs.org/docs/app/api-reference/components/font#css-variables).
In the example below, we use the `Inter` and `Roboto_Mono` fonts from `next/font/google` (you can use any Google Font or Local Font). Use the `variable` option to define a CSS variable name, such as `inter` and `roboto_mono` for these fonts, respectively. Then, apply `inter.variable` and `roboto_mono.variable` to include the CSS variables in your HTML document.
> **Good to know** : You can add these variables to the `<html>` or `<body>` tag, depending on your preference, styling needs or project requirements.
pages/_app.js
```
import { Inter } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
})

const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-roboto-mono',
})

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={`${inter.variable} ${roboto_mono.variable} font-sans`}>
      <Component {...pageProps} />
    </main>
  )
}
```

Finally, add the CSS variable to your [Tailwind CSS config](https://nextjs.org/docs/app/getting-started/css#tailwind-css):
global.css
```
@import 'tailwindcss';

@theme inline {
  --font-sans: var(--font-inter);
  --font-mono: var(--font-roboto-mono);
}
```

### Tailwind CSS v3[](https://nextjs.org/docs/pages/api-reference/edge#tailwind-css-v3)
tailwind.config.js
```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-inter)'],
        mono: ['var(--font-roboto-mono)'],
      },
    },
  },
  plugins: [],
}
```

You can now use the `font-sans` and `font-mono` utility classes to apply the font to your elements.
```
<p class="font-sans ...">The quick brown fox ...</p>
<p class="font-mono ...">The quick brown fox ...</p>
```

### Applying Styles[](https://nextjs.org/docs/pages/api-reference/edge#applying-styles)
You can apply the font styles in three ways:
  * [`className`](https://nextjs.org/docs/pages/api-reference/edge#classname)
  * [`style`](https://nextjs.org/docs/pages/api-reference/edge#style-1)
  * [CSS Variables](https://nextjs.org/docs/pages/api-reference/edge#css-variables)


####  `className`[](https://nextjs.org/docs/pages/api-reference/edge#classname)
Returns a read-only CSS `className` for the loaded font to be passed to an HTML element.
```
<p className={inter.className}>Hello, Next.js!</p>
```

####  `style`[](https://nextjs.org/docs/pages/api-reference/edge#style-1)
Returns a read-only CSS `style` object for the loaded font to be passed to an HTML element, including `style.fontFamily` to access the font family name and fallback fonts.
```
<p style={inter.style}>Hello World</p>
```

#### CSS Variables[](https://nextjs.org/docs/pages/api-reference/edge#css-variables)
If you would like to set your styles in an external style sheet and specify additional options there, use the CSS variable method.
In addition to importing the font, also import the CSS file where the CSS variable is defined and set the variable option of the font loader object as follows:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { Inter } from 'next/font/google'
import styles from '../styles/component.module.css'

const inter = Inter({
  variable: '--font-inter',
})
```

To use the font, set the `className` of the parent container of the text you would like to style to the font loader's `variable` value and the `className` of the text to the `styles` property from the external CSS file.
app/page.tsx
TypeScript
JavaScript TypeScript
```
<main className={inter.variable}>
  <p className={styles.text}>Hello World</p>
</main>
```

Define the `text` selector class in the `component.module.css` CSS file as follows:
styles/component.module.css
```
.text {
  font-family: var(--font-inter);
  font-weight: 200;
  font-style: italic;
}
```

In the example above, the text `Hello World` is styled using the `Inter` font and the generated font fallback with `font-weight: 200` and `font-style: italic`.
### Using a font definitions file[](https://nextjs.org/docs/pages/api-reference/edge#using-a-font-definitions-file)
Every time you call the `localFont` or Google font function, that font will be hosted as one instance in your application. Therefore, if you need to use the same font in multiple places, you should load it in one place and import the related font object where you need it. This is done using a font definitions file.
For example, create a `fonts.ts` file in a `styles` folder at the root of your app directory.
Then, specify your font definitions as follows:
styles/fonts.ts
TypeScript
JavaScript TypeScript
```
import { Inter, Lora, Source_Sans_3 } from 'next/font/google'
import localFont from 'next/font/local'

// define your variable fonts
const inter = Inter()
const lora = Lora()
// define 2 weights of a non-variable font
const sourceCodePro400 = Source_Sans_3({ weight: '400' })
const sourceCodePro700 = Source_Sans_3({ weight: '700' })
// define a custom local font where GreatVibes-Regular.ttf is stored in the styles folder
const greatVibes = localFont({ src: './GreatVibes-Regular.ttf' })

export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }
```

You can now use these definitions in your code as follows:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { inter, lora, sourceCodePro700, greatVibes } from '../styles/fonts'

export default function Page() {
  return (
    <div>
      <p className={inter.className}>Hello world using Inter font</p>
      <p style={lora.style}>Hello world using Lora font</p>
      <p className={sourceCodePro700.className}>
        Hello world using Source_Sans_3 font with weight 700
      </p>
      <p className={greatVibes.className}>My title in Great Vibes font</p>
    </div>
  )
}
```

To make it easier to access the font definitions in your code, you can define a path alias in your `tsconfig.json` or `jsconfig.json` files as follows:
tsconfig.json
```
{
  "compilerOptions": {
    "paths": {
      "@/fonts": ["./styles/fonts"]
    }
  }
}
```

You can now import any font definition as follows:
app/about/page.tsx
TypeScript
JavaScript TypeScript
```
import { greatVibes, sourceCodePro400 } from '@/fonts'
```

### Preloading[](https://nextjs.org/docs/pages/api-reference/edge#preloading)
When a font function is called on a page of your site, it is not globally available and preloaded on all routes. Rather, the font is only preloaded on the related route/s based on the type of file where it is used:
  * if it's a [unique page](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts), it is preloaded on the unique route for that page
  * if it's in the [custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app), it is preloaded on all the routes of the site under `/pages`
