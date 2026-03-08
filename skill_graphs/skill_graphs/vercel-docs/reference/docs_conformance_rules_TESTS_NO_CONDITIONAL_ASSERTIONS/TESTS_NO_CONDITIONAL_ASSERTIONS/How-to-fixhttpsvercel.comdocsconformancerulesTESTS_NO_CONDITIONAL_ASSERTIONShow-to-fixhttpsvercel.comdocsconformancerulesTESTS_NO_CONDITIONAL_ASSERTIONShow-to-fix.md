##  [How to fix](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#how-to-fix)[](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#how-to-fix)
There are two ways to resolve this error:
  1. Refactor the test code to ensure that assertions are no longer conditional.
  2. Use `expect.assertions` to inform the test runner that it should fail if the required number of assertions were not called during the test.


Taking our previous example, we can apply the second fix:
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
    expect.assertions(2);
  });
});
```

###  [Using `expect.assertions`](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#using-expect.assertions)[](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#using-expect.assertions)
Most test frameworks and runners support `expect.assertions`, and this is the preferred approach to resolving this error if you can't refactor your test code.
To satisfy this rule, the test must not conditionally call `expect.assertions`. This rule doesn't count or report on the number of assertions.
###  [What to do when you can't use `expect.assertions`](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#what-to-do-when-you-can't-use-expect.assertions)[](https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS#what-to-do-when-you-can't-use-expect.assertions)
There may be cases where you can't use `expect.assertions` (i.e. your test framework or runner doesn't support it), and refactoring the test code is not a viable solution. In those cases, you have the following options:
  1. You can use allowlists to allow individual violations (see: [Conformance Allowlists](https://vercel.com/docs/conformance/allowlist)).
  2. You can disable this test (see: [Customizing Conformance](https://vercel.com/docs/conformance/customize)).
