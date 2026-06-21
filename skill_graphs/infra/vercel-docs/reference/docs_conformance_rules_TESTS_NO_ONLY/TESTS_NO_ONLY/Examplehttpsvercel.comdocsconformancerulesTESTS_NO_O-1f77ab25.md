##  [Example](https://vercel.com/docs/conformance/rules/TESTS_NO_ONLY#example)[](https://vercel.com/docs/conformance/rules/TESTS_NO_ONLY#example)
src/button/button.test.ts
```
describe('button', () => {
  it.only('should render', () => {
    // ...
  });
});
```

Note that the following patterns (and variants of these patterns) will be reported as errors by this test. These should cover popular test frameworks and runners, including:
```
// Most test frameworks and runners
describe.only(/* ... */);
it.concurrent.only(/* ... */);
test.only.each([])(/* ... */);
// Jest - supported in addition to the above
fdescribe(/* ... */);
fit.each([])(/* ... */);
ftest(/* ... */);
```
