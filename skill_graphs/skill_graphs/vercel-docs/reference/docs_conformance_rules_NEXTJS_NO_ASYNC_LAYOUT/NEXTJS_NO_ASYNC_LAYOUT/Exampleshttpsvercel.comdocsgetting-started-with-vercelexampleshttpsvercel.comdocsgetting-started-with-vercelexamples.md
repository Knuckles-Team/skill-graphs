##  [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)[](https://vercel.com/docs/getting-started-with-vercel#examples)
This rule will catch the following code.
app/layout.tsx
```
export default async function RootLayout() {
  const data = await fetch();
  return <div>{data}</div>;
}
```

app/layout.jsx
```
async function AuthButton() {
  const isAuthorized = await auth();
  return <div>{isAuthorized ? 'Authorized' : 'Unauthorized'}</div>;
}

export default function Layout() {
  return <AuthButton />;
}
```
