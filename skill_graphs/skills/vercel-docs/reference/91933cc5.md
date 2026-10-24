##  [Using a Content Security Policy](https://vercel.com/docs/vercel-toolbar/managing-toolbar#using-a-content-security-policy)[](https://vercel.com/docs/vercel-toolbar/managing-toolbar#using-a-content-security-policy)
If you have a may need to adjust the CSP to enable access to the Vercel Toolbar or Comments.
You can make the following adjustments to the `Content-Security-Policy` [response header](https://vercel.com/docs/headers/cache-control-headers#custom-response-headers):
  * Add the following to `script-src` (Most commonly used):
```
  script-src https://vercel.live
```

  * Add the following to `connect-src`:
```
  connect-src https://vercel.live wss://ws-us3.pusher.com
```

  * Add the following to `img-src`:
```
  img-src https://vercel.live https://vercel.com data: blob:
```

  * Add the following to `frame-src`:
```
  frame-src https://vercel.live
```

  * Add the following to `style-src`:
```
  style-src https://vercel.live 'unsafe-inline'
```

  * Add the following to `font-src`:
```
  font-src https://vercel.live https://assets.vercel.com
```



* * *
[ Previous Add to Environments ](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost)[ Next Browser Extensions ](https://vercel.com/docs/vercel-toolbar/browser-extension)
Was this helpful?
Send
On this page
  * [Viewing the toolbar](https://vercel.com/docs/vercel-toolbar/managing-toolbar#viewing-the-toolbar)
  * [Enable or disable the toolbar team-wide](https://vercel.com/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-team-wide)
  * [Enable or disable the toolbar project-wide](https://vercel.com/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-project-wide)
  * [Disable toolbar for session](https://vercel.com/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-session)
  * [Disable toolbar for automation](https://vercel.com/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-automation)
  * [Enable or disable the toolbar for a specific branch](https://vercel.com/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-for-a-specific-branch)
  * [Using the toolbar with a custom alias domain](https://vercel.com/docs/vercel-toolbar/managing-toolbar#using-the-toolbar-with-a-custom-alias-domain)
  * [Using a Content Security Policy](https://vercel.com/docs/vercel-toolbar/managing-toolbar#using-a-content-security-policy)


Copy as MarkdownGive feedbackAsk AI about this page
