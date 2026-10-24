# env
This is a legacy API and no longer recommended. It's still supported for backward compatibility.
Last updated February 27, 2026
> Since the release of [Next.js 9.4](https://nextjs.org/blog/next-9-4) we now have a more intuitive and ergonomic experience for [adding environment variables](https://nextjs.org/docs/app/guides/environment-variables). Give it a try!
> **Good to know** : environment variables specified in this way will **always** be included in the JavaScript bundle, prefixing the environment variable name with `NEXT_PUBLIC_` only has an effect when specifying them [through the environment or .env files](https://nextjs.org/docs/app/guides/environment-variables).
To add environment variables to the JavaScript bundle, open `next.config.js` and add the `env` config:
next.config.js
```
module.exports = {
  env: {
    customKey: 'my-value',
  },
}
```

Now you can access `process.env.customKey` in your code. For example:
```
function Page() {
  return <h1>The value of customKey is: {process.env.customKey}</h1>
}

export default Page
```

Next.js will replace `process.env.customKey` with `'my-value'` at build time. Trying to destructure `process.env` variables won't work due to the nature of webpack
For example, the following line:
```
return <h1>The value of customKey is: {process.env.customKey}</h1>
```

Will end up being:
```
return <h1>The value of customKey is: {'my-value'}</h1>
```

[PreviousdistDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir)[NextexpireTime](https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime)
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
