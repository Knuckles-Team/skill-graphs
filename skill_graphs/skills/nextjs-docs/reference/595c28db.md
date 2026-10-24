## Why This Error Occurred[](https://nextjs.org/docs/messages/no-page-custom-font#why-this-error-occurred)
  * The custom font you're adding was added to a page - this only adds the font to the specific page and not the entire application.
  * The custom font you're adding was added to a separate component within `pages/_document.js` - this disables automatic font optimization.
