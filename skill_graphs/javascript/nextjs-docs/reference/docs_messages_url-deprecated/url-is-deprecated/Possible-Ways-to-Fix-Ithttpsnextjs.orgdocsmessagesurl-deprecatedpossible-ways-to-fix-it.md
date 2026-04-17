## Possible Ways to Fix It[](https://nextjs.org/docs/messages/url-deprecated#possible-ways-to-fix-it)
Since Next 5 we provide a way to explicitly inject the Next.js router object into pages and all their descending components. The `router` property that is injected will hold the same values as `url`, like `pathname`, `asPath`, and `query`.
Here's an example of using `withRouter`:
pages/index.js
```
import { withRouter } from 'next/router'

class Page extends React.Component {
  render() {
    const { router } = this.props
    console.log(router)
    return <div>{router.pathname}</div>
  }
}

export default withRouter(Page)
```

We provide a codemod (a code to code transformation) to automatically change the `url` property usages to `withRouter`.
You can find this codemod and instructions on how to run it here: [Use `withRouter`](https://nextjs.org/docs/pages/guides/upgrading/codemods#url-to-withrouter)
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
