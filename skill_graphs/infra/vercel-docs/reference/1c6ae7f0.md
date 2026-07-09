##  [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)[](https://vercel.com/docs/getting-started-with-vercel#examples)
In the following example, the `Header` component contains an object with the spread operator being applied to it.
We don't know if the props that the `Header` component reads will accept all the values contained in the `foo` object.
app/dashboard/page.tsx
```
function HomePage() {
  return <Header {...{ foo }}>Hello World</Header>;
}

export default HomePage;
```
