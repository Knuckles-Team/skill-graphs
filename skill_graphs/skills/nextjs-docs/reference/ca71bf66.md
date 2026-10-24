## Parameters[](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect#parameters)
The `permanentRedirect` function accepts two arguments:
```
permanentRedirect(path, type)
```

Parameter | Type | Description
---|---|---
`path` | `string` | The URL to redirect to. Can be a relative or absolute path.
`type` |  `'replace'` (default) or `'push'` (default in Server Actions) | The type of redirect to perform.
By default, `permanentRedirect` will use `push` (adding a new entry to the browser history stack) in [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.
The `RedirectType` object contains the available options for the `type` parameter.
```
import { permanentRedirect, RedirectType } from 'next/navigation'

permanentRedirect('/redirect-to', RedirectType.replace)
// or
permanentRedirect('/redirect-to', RedirectType.push)
```

The `type` parameter has no effect when used in Server Components.
