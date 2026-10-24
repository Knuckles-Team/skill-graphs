## Usage[](https://nextjs.org/docs/app/api-reference/directives/use-client#usage)
To declare an entry point for the Client Components, add the `'use client'` directive **at the top of the file** , before any imports:
app/components/counter.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

When using the `'use client'` directive, the props of the Client Components must be
app/components/counter.tsx
TypeScript
JavaScript TypeScript
```
'use client'

export default function Counter({
  onClick /* ❌ Function is not serializable */,
}) {
  return (
    <div>
      <button onClick={onClick}>Increment</button>
    </div>
  )
}
```
