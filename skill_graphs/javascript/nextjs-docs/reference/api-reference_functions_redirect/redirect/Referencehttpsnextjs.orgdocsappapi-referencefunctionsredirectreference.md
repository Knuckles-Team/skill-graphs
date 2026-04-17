## Reference[](https://nextjs.org/docs/app/api-reference/functions/redirect#reference)
### Parameters[](https://nextjs.org/docs/app/api-reference/functions/redirect#parameters)
The `redirect` function accepts two arguments:
```
redirect(path, type)
```

Parameter | Type | Description
---|---|---
`path` | `string` | The URL to redirect to. Can be a relative or absolute path.
`type` |  `'replace'` (default) or `'push'` (default in Server Actions) | The type of redirect to perform.
By default, `redirect` will use `push` (adding a new entry to the browser history stack) in [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.
The `RedirectType` object contains the available options for the `type` parameter.
```
import { redirect, RedirectType } from 'next/navigation'

redirect('/redirect-to', RedirectType.replace)
// or
redirect('/redirect-to', RedirectType.push)
```

The `type` parameter has no effect when used in Server Components.
### Returns[](https://nextjs.org/docs/app/api-reference/functions/redirect#returns)
`redirect` does not return a value.
