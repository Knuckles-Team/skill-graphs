## Handling Fonts[](https://nextjs.org/docs/pages/guides/testing/jest#handling-fonts)
To handle fonts, create the `nextFontMock.js` file inside the `__mocks__` directory, and add the following configuration:
__mocks__/nextFontMock.js
```
module.exports = new Proxy(
  {},
  {
    get: function getter() {
      return () => ({
        className: 'className',
        variable: 'variable',
        style: { fontFamily: 'fontFamily' },
      })
    },
  }
)
```
