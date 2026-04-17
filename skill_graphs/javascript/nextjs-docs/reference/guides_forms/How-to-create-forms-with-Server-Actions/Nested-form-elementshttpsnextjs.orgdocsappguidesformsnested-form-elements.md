## Nested form elements[](https://nextjs.org/docs/app/guides/forms#nested-form-elements)
You can call Server Actions in elements nested inside `<form>` such as `<button>`, `<input type="submit">`, and `<input type="image">`. These elements accept the `formAction` prop or event handlers.
This is useful in cases where you want to call multiple Server Actions within a form. For example, you can create a specific `<button>` element for saving a post draft in addition to publishing it. See the
