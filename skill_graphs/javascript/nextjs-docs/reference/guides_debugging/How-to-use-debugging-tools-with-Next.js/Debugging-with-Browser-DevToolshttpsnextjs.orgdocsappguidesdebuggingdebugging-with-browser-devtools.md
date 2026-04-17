## Debugging with Browser DevTools[](https://nextjs.org/docs/app/guides/debugging#debugging-with-browser-devtools)
### Client-side code[](https://nextjs.org/docs/app/guides/debugging#client-side-code)
Start your development server as usual by running `next dev`, `npm run dev`, or `yarn dev`. Once the server starts, open `http://localhost:3000` (or your alternate URL) in your preferred browser.
For Chrome:
  * Open Chrome's Developer Tools (`Ctrl+Shift+J` on Windows/Linux, `⌥+⌘+I` on macOS)
  * Go to the **Sources** tab


For Firefox:
  * Open Firefox's Developer Tools (`Ctrl+Shift+I` on Windows/Linux, `⌥+⌘+I` on macOS)
  * Go to the **Debugger** tab


In either browser, any time your client-side code reaches a
  * In Chrome: Press `Ctrl+P` on Windows/Linux or `⌘+P` on macOS
  * In Firefox: Press `Ctrl+P` on Windows/Linux or `⌘+P` on macOS, or use the file tree in the left panel


Note that when searching, your source files will have paths starting with `webpack://_N_E/./`.
### React Developer Tools[](https://nextjs.org/docs/app/guides/debugging#react-developer-tools)
For React-specific debugging, install the
  * Inspect React components
  * Edit props and state
  * Identify performance problems


### Server-side code[](https://nextjs.org/docs/app/guides/debugging#server-side-code)
To debug server-side Next.js code with browser DevTools, you need to pass the `--inspect` flag:
pnpmnpmyarnbun
Terminal
```
pnpm dev --inspect
```

The value of `--inspect` is passed to the underlying Node.js process. Check out the
> **Good to know** : Use `--inspect=0.0.0.0` to allow remote debugging access outside localhost, such as when running the app in a Docker container.
Launching the Next.js dev server with the `--inspect` flag will look something like this:
Terminal
```
Debugger listening on ws://127.0.0.1:9229/0cf90313-350d-4466-a748-cd60f4e47c95
For help, see: https://nodejs.org/en/docs/inspector
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
```

For Chrome:
  1. Open a new tab and visit `chrome://inspect`
  2. Look for your Next.js application in the **Remote Target** section
  3. Click **inspect** to open a separate DevTools window
  4. Go to the **Sources** tab


For Firefox:
  1. Open a new tab and visit `about:debugging`
  2. Click **This Firefox** in the left sidebar
  3. Under **Remote Targets** , find your Next.js application
  4. Click **Inspect** to open the debugger
  5. Go to the **Debugger** tab


Debugging server-side code works similarly to client-side debugging. When searching for files (`Ctrl+P`/`⌘+P`), your source files will have paths starting with `webpack://{application-name}/./` (where `{application-name}` will be replaced with the name of your application according to your `package.json` file).
To use `--inspect-brk` or `--inspect-wait`, you have to specify `NODE_OPTIONS` instead. e.g. `NODE_OPTIONS=--inspect-brk next dev`.
### Inspect Server Errors with Browser DevTools[](https://nextjs.org/docs/app/guides/debugging#inspect-server-errors-with-browser-devtools)
When you encounter an error, inspecting the source code can help trace the root cause of errors.
Next.js will display a Node.js icon underneath the Next.js version indicator on the error overlay. By clicking that icon, the DevTools URL is copied to your clipboard. You can open a new browser tab with that URL to inspect the Next.js server process.
### Debugging on Windows[](https://nextjs.org/docs/app/guides/debugging#debugging-on-windows)
Ensure Windows Defender is disabled on your machine. This external service will check _every file read_ , which has been reported to greatly increase Fast Refresh time with `next dev`. This is a known issue, not related to Next.js, but it does affect Next.js development.
