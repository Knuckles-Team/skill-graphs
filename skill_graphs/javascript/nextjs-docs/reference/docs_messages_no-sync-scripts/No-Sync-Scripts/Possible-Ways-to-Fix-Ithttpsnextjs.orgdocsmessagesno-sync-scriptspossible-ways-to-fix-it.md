## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-sync-scripts#possible-ways-to-fix-it)
### Script component (recommended)[](https://nextjs.org/docs/messages/no-sync-scripts#script-component-recommended)
pages/index.js
```
import Script from 'next/script'

function Home() {
  return (
    <div class="container">
      <Script src="https://third-party-script.js"></Script>
      <div>Home Page</div>
    </div>
  )
}

export default Home
```

### Use `async` or `defer`[](https://nextjs.org/docs/messages/no-sync-scripts#use-async-or-defer)
```
<script src="https://third-party-script.js" async />
<script src="https://third-party-script.js" defer />
```
