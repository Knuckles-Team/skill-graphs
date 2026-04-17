# TESTS_NO_CONDITIONAL_ASSERTIONS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
When possible, conditional test assertions should be avoided as they can lead to false test passes if and when conditions are not evaluated as expected.
If you can't avoid using a condition in your test, you can satisfy this rule by using an `expect.assertions` statement.
