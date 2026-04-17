##  [Examples](https://vercel.com/docs/getting-started-with-vercel#examples)[](https://vercel.com/docs/getting-started-with-vercel#examples)
Examples of incorrect code for this rule:
```
return <SomeContext.Provider value={{ foo: 'bar' }}>...</SomeContext.Provider>;
```

Examples of correct code for this rule:
```
const foo = useMemo(() => ({ foo: 'bar' }), []);

return <SomeContext.Provider value={foo}>...</SomeContext.Provider>;
```
