## Linting[](https://nextjs.org/docs/architecture/accessibility#linting)
Next.js provides an [integrated ESLint experience](https://nextjs.org/docs/pages/api-reference/config/eslint) out of the box, including custom rules for Next.js. By default, Next.js includes `eslint-plugin-jsx-a11y` to help catch accessibility issues early, including warning on:
For example, this plugin helps ensure you add alt text to `img` tags, use correct `aria-*` attributes, use correct `role` attributes, and more.
