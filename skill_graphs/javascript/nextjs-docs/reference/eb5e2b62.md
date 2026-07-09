# distDir
Last updated February 27, 2026
You can specify a name to use for a custom build directory to use instead of `.next`.
Open `next.config.js` and add the `distDir` config:
next.config.js
```
module.exports = {
  distDir: 'build',
}
```

Now if you run `next build` Next.js will use `build` instead of the default `.next` folder.
> `distDir` **should not** leave your project directory. For example, `../build` is an **invalid** directory.
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
