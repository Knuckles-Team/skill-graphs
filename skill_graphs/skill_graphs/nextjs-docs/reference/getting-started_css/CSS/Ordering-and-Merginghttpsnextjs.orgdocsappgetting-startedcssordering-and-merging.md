## Ordering and Merging[](https://nextjs.org/docs/app/getting-started/css#ordering-and-merging)
Next.js optimizes CSS during production builds by automatically chunking (merging) stylesheets. The **order of your CSS** depends on the **order you import styles in your code**.
For example, `base-button.module.css` will be ordered before `page.module.css` since `<BaseButton>` is imported before `page.module.css`:
page.tsx
TypeScript
JavaScript TypeScript
```
import { BaseButton } from './base-button'
import styles from './page.module.css'

export default function Page() {
  return <BaseButton className={styles.primary} />
}
```

base-button.tsx
TypeScript
JavaScript TypeScript
```
import styles from './base-button.module.css'

export function BaseButton() {
  return <button className={styles.primary} />
}
```

### Recommendations[](https://nextjs.org/docs/app/getting-started/css#recommendations)
To keep CSS ordering predictable:
  * Try to contain CSS imports to a single JavaScript or TypeScript entry file
  * Import global styles and Tailwind stylesheets in the root of your application.
  * **Use Tailwind CSS** for most styling needs as it covers common design patterns with utility classes.
  * Use CSS Modules for component-specific styles when Tailwind utilities aren't sufficient.
  * Use a consistent naming convention for your CSS modules. For example, using `<name>.module.css` over `<name>.tsx`.
  * Extract shared styles into shared components to avoid duplicate imports.
  * Turn off linters or formatters that auto-sort imports like ESLint’s
  * You can use the [`cssChunking`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking) option in `next.config.js` to control how CSS is chunked.
