## External stylesheets[](https://nextjs.org/docs/pages/getting-started/css#external-stylesheets)
Next.js allows you to import CSS files from a JavaScript file. This is possible because Next.js extends the concept of
### Import styles from `node_modules`[](https://nextjs.org/docs/pages/getting-started/css#import-styles-from-node_modules)
Since Next.js **9.5.4** , importing a CSS file from `node_modules` is permitted anywhere in your application.
For global stylesheets, like `bootstrap` or `nprogress`, you should import the file inside `pages/_app.js`. For example:
pages/_app.js
```
import 'bootstrap/dist/css/bootstrap.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

To import CSS required by a third-party component, you can do so in your component. For example:
components/example-dialog.js
```
import { useState } from 'react'
import { Dialog } from '@reach/dialog'
import VisuallyHidden from '@reach/visually-hidden'
import '@reach/dialog/styles.css'

function ExampleDialog(props) {
  const [showDialog, setShowDialog] = useState(false)
  const open = () => setShowDialog(true)
  const close = () => setShowDialog(false)

  return (
    <div>
      <button onClick={open}>Open Dialog</button>
      <Dialog isOpen={showDialog} onDismiss={close}>
        <button className="close-button" onClick={close}>
          <VisuallyHidden>Close</VisuallyHidden>
          <span aria-hidden>×</span>
        </button>
        <p>Hello there. I am a dialog</p>
      </Dialog>
    </div>
  )
}
```
