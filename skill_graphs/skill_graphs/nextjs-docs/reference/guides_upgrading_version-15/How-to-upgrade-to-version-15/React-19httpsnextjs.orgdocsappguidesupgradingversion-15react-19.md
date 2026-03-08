## React 19[](https://nextjs.org/docs/app/guides/upgrading/version-15#react-19)
  * The minimum versions of `react` and `react-dom` is now 19.
  * `useFormState` has been replaced by `useActionState`. The `useFormState` hook is still available in React 19, but it is deprecated and will be removed in a future release. `useActionState` is recommended and includes additional properties like reading the `pending` state directly.
  * `useFormStatus` now includes additional keys like `data`, `method`, and `action`. If you are not using React 19, only the `pending` key is available.
  * Read more in the


> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.
