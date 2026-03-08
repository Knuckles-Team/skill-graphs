# NO_SERIAL_ASYNC_CALLS
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Sequential execution of async/await calls can significantly impact performance because each await call prevents further execution until resolving its Promise. This rule aims to refactor sequential async/await calls into parallel executions to enhance performance.
You should note that this rule might not flag some async/await usage patterns. For example:
  * Patterns involving conditional statements
  * Call expressions
  * Patterns that await in a manner that suggests non-serial dependencies between calls


For instance, scenarios where async calls depend conditionally on each other or are part of complex expressions are not flagged. This includes cases where one async call's outcome is necessary for subsequent calls, requiring serial execution due to logical or dependency reasons.
The following example will not be flagged by this rule:
```
async function updateDatabase() {
  const result1 = await async1();
  const result2 = await async2();
  doSomething(result1, result2);
}
```

These patterns fall outside the scope of this rule because safely suggesting parallelization requires more context, and the rule uses conservative heuristics to avoid false positives.
