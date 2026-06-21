## Limitations[](https://nextjs.org/docs/architecture/fast-refresh#limitations)
Fast Refresh tries to preserve local React state in the component you're editing, but only if it's safe to do so. Here's a few reasons why you might see local state being reset on every edit to a file:
  * Local state is not preserved for class components (only function components and Hooks preserve state).
  * The file you're editing might have _other_ exports in addition to a React component.
  * Sometimes, a file would export the result of calling a higher-order component like `HOC(WrappedComponent)`. If the returned component is a class, its state will be reset.
  * Anonymous arrow functions like `export default () => <div />;` cause Fast Refresh to not preserve local component state. For large codebases you can use our [`name-default-component` codemod](https://nextjs.org/docs/pages/guides/upgrading/codemods#name-default-component).


As more of your codebase moves to function components and Hooks, you can expect state to be preserved in more cases.
