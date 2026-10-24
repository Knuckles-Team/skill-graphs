## Possible Ways to Fix It[](https://nextjs.org/docs/messages/app-container-deprecated#possible-ways-to-fix-it)
To resolve this issue, you need to remove the `<Container>` component from your custom `<App>` (`pages/_app.js`).
**Before**
pages/_app.js
```
import React from 'react'
import App, { Container } from 'next/app'

class MyApp extends App {
  render() {
    const { Component, pageProps } = this.props
    return (
      <Container>
        <Component {...pageProps} />
      </Container>
    )
  }
}

export default MyApp
```

**After**
pages/_app.js
```
import React from 'react'
import App from 'next/app'

class MyApp extends App {
  render() {
    const { Component, pageProps } = this.props
    return <Component {...pageProps} />
  }
}

export default MyApp
```

After making this change, your custom `<App>` should work as expected without the `<Container>` component.
