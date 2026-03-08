## Serialization[](https://nextjs.org/docs/app/api-reference/directives/use-cache#serialization)
Arguments to cached functions and their return values must be serializable.
For a complete reference, see:
  * **React Server Components** serialization
  * **React Client Components** serialization


> **Good to know:** Arguments and return values use different serialization systems. Server Component serialization (for arguments) is more restrictive than Client Component serialization (for return values). This means you can return JSX elements but cannot accept them as arguments unless using pass-through patterns.
### Supported types[](https://nextjs.org/docs/app/api-reference/directives/use-cache#supported-types)
**Arguments:**
  * Primitives: `string`, `number`, `boolean`, `null`, `undefined`
  * Plain objects: `{ key: value }`
  * Arrays: `[1, 2, 3]`
  * Dates, Maps, Sets, TypedArrays, ArrayBuffers
  * React elements (as pass-through only)


**Return values:**
  * Same as arguments, plus JSX elements


### Unsupported types[](https://nextjs.org/docs/app/api-reference/directives/use-cache#unsupported-types)
  * Class instances
  * Functions (except as pass-through)
  * Symbols, WeakMaps, WeakSets
  * URL instances


app/components/user-card.tsx
```
// Valid - primitives and plain objects
async function UserCard({
  id,
  config,
}: {
  id: string
  config: { theme: string }
}) {
  'use cache'
  return <div>{id}</div>
}

// Invalid - class instance
async function UserProfile({ user }: { user: UserClass }) {
  'use cache'
  // Error: Cannot serialize class instance
  return <div>{user.name}</div>
}
```

### Pass-through (non-serializable arguments)[](https://nextjs.org/docs/app/api-reference/directives/use-cache#pass-through-non-serializable-arguments)
You can accept non-serializable values **as long as you don't introspect them**. This enables composition patterns with `children` and Server Actions:
app/components/cached-wrapper.tsx
```
async function CachedWrapper({ children }: { children: ReactNode }) {
  'use cache'
  // Don't read or modify children - just pass it through
  return (
    <div className="wrapper">
      <header>Cached Header</header>
      {children}
    </div>
  )
}

// Usage: children can be dynamic
export default function Page() {
  return (
    <CachedWrapper>
      <DynamicComponent /> {/* Not cached, passed through */}
    </CachedWrapper>
  )
}
```

You can also pass Server Actions through cached components:
app/components/cached-form.tsx
```
async function CachedForm({ action }: { action: () => Promise<void> }) {
  'use cache'
  // Don't call action here - just pass it through
  return <form action={action}>{/* ... */}</form>
}
```
