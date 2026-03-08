## Check your Custom App File (`pages/_app.js`)[](https://nextjs.org/docs/pages/guides/upgrading/version-9#check-your-custom-app-file-pages_appjs)
If you previously copied the [Custom `<App>`](https://nextjs.org/docs/pages/building-your-application/routing/custom-app) example, you may be able to remove your `getInitialProps`.
Removing `getInitialProps` from `pages/_app.js` (when possible) is important to leverage new Next.js features!
The following `getInitialProps` does nothing and may be removed:
```
class MyApp extends App {
  // Remove me, I do nothing!
  static async getInitialProps({ Component, ctx }) {
    let pageProps = {}

    if (Component.getInitialProps) {
      pageProps = await Component.getInitialProps(ctx)
    }

    return { pageProps }
  }

  render() {
    // ... etc
  }
}
```
