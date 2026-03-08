##  [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)[](https://vercel.com/docs/getting-started-with-vercel#examples)
This rule will catch the following code.
app/page.tsx
```
export default async function Page() {
  const data = await fetch();
  return <div>{data}</div>;
}
```

app/page.jsx
```
async function AuthButton() {
  const isAuthorized = await auth();
  return <div>{isAuthorized ? 'Authorized' : 'Unauthorized'}</div>;
}

export default function Page() {
  return <AuthButton />;
}
```
