# How to use CSS-in-JS libraries
Last updated February 27, 2026
Examples
It's possible to use any existing CSS-in-JS solution. The simplest one is inline styles:
```
function HiThere() {
  return <p style={{ color: 'red' }}>hi there</p>
}

export default HiThere
```

We bundle
See the above examples for other popular CSS-in-JS solutions (like Styled Components).
A component using `styled-jsx` looks like this:
```
function HelloWorld() {
  return (
    <div>
      Hello world
      <p>scoped!</p>
      <style jsx>{`
        p {
          color: blue;
        }
        div {
          background: red;
        }
        @media (max-width: 600px) {
          div {
            background: blue;
          }
        }
      `}</style>
      <style global jsx>{`
        body {
          background: black;
        }
      `}</style>
    </div>
  )
}

export default HelloWorld
```

Please see the
### Disabling JavaScript[](https://nextjs.org/docs/pages/guides/css-in-js#disabling-javascript)
Yes, if you disable JavaScript the CSS will still be loaded in the production build (`next start`). During development, we require JavaScript to be enabled to provide the best developer experience with [Fast Refresh](https://nextjs.org/blog/next-9-4#fast-refresh).
Was this helpful?
Send
