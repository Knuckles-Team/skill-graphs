## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-css-tags#possible-ways-to-fix-it)
There are multiple ways to include styles using Next.js' built-in CSS support, including the option to use `@import` within the root stylesheet that is imported in `pages/_app.js`:
styles.css
```
/* Root stylesheet */
@import 'extra.css';

body {
  /* ... */
}
```

Another option is to use CSS Modules to import the CSS file scoped specifically to the component.
pages/index.js
```
import styles from './extra.module.css'

export class Home {
  render() {
    return (
      <div>
        <button type="button" className={styles.active}>
          Open
        </button>
      </div>
    )
  }
}
```

Refer to the [Built-In CSS Support](https://nextjs.org/docs/app/getting-started/css) documentation to learn about all the ways to include CSS to your application.
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
