## withRouter[](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter)
If [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) is not the best fit for you, `withRouter` can also add the same [`router` object](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) to any component.
### Usage[](https://nextjs.org/docs/pages/api-reference/functions/use-router#usage)
```
import { withRouter } from 'next/router'

function Page({ router }) {
  return <p>{router.pathname}</p>
}

export default withRouter(Page)
```

### TypeScript[](https://nextjs.org/docs/pages/api-reference/functions/use-router#typescript)
To use class components with `withRouter`, the component needs to accept a router prop:
```
import React from 'react'
import { withRouter, NextRouter } from 'next/router'

interface WithRouterProps {
  router: NextRouter
}

interface MyComponentProps extends WithRouterProps {}

class MyComponent extends React.Component<MyComponentProps> {
  render() {
    return <p>{this.props.router.pathname}</p>
  }
}

export default withRouter(MyComponent)
```

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
