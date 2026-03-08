##  [Example](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#example)[](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#example)
In this abstract example, there are two potential points of failure:
  1. The button could throw a ButtonError during `render(Button)`, causing the first (`try`) assertion to be skipped.
  2. The `throwError()` function could fail to throw, causing the second (`catch`) assertion to be skipped.


src/button/button.test.ts
```
describe('button', () => {
  it('should render', () => {
    try {
      const button = render(Button);
      expect(button).not.toBe(null);
      button.throwAnError();
    } catch (error) {
      expect(error).toBeInstanceOf(ButtonError);
    }
  });
});
```
