## Localization[](https://nextjs.org/docs/app/guides/internationalization#localization)
Changing displayed content based on the user’s preferred locale, or localization, is not something specific to Next.js. The patterns described below would work the same with any web application.
Let’s assume we want to support both English and Dutch content inside our application. We might maintain two different “dictionaries”, which are objects that give us a mapping from some key to a localized string. For example:
dictionaries/en.json
```
{
  "products": {
    "cart": "Add to Cart"
  }
}
```

dictionaries/nl.json
```
{
  "products": {
    "cart": "Toevoegen aan Winkelwagen"
  }
}
```

We can then create a `getDictionary` function to load the translations for the requested locale:
app/[lang]/dictionaries.ts
TypeScript
JavaScript TypeScript
```
import 'server-only'

const dictionaries = {
  en: () => import('./dictionaries/en.json').then((module) => module.default),
  nl: () => import('./dictionaries/nl.json').then((module) => module.default),
}

export type Locale = keyof typeof dictionaries

export const hasLocale = (locale: string): locale is Locale =>
  locale in dictionaries

export const getDictionary = async (locale: Locale) => dictionaries[locale]()
```

Given the currently selected language, we can fetch the dictionary inside of a layout or page.
Since `lang` is typed as `string`, using `hasLocale` narrows the type to your supported locales. It also ensures a 404 is returned if a translation is missing, rather than a runtime error.
app/[lang]/page.tsx
TypeScript
JavaScript TypeScript
```
import { notFound } from 'next/navigation'
import { getDictionary, hasLocale } from './dictionaries'

export default async function Page({ params }: PageProps<'/[lang]'>) {
  const { lang } = await params

  if (!hasLocale(lang)) notFound()

  const dict = await getDictionary(lang)
  return <button>{dict.products.cart}</button> // Add to Cart
}
```

Because all layouts and pages in the `app/` directory default to [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), we do not need to worry about the size of the translation files affecting our client-side JavaScript bundle size. This code will **only run on the server** , and only the resulting HTML will be sent to the browser.
