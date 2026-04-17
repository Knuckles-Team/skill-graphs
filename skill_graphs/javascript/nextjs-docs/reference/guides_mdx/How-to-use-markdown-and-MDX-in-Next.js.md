# How to use markdown and MDX in Next.js
Last updated February 27, 2026
You write...
```
I **love** using [Next.js](https://nextjs.org/)
```

Output:
```
<p>I <strong>love</strong> using <a href="https://nextjs.org/">Next.js</a></p>
```

Next.js can support both local MDX content inside your application, as well as remote MDX files fetched dynamically on the server. The Next.js plugin handles transforming markdown and React components into HTML, including support for usage in Server Components (the default in App Router).
> **Good to know** : View the
