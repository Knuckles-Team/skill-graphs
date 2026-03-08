## CSS Modules[](https://nextjs.org/docs/app/getting-started/css#css-modules)
CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.
To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `app` directory:
app/blog/blog.module.css
```
.blog {
  padding: 24px;
}
```

app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
import styles from './blog.module.css'

export default function Page() {
  return <main className={styles.blog}></main>
}
```
