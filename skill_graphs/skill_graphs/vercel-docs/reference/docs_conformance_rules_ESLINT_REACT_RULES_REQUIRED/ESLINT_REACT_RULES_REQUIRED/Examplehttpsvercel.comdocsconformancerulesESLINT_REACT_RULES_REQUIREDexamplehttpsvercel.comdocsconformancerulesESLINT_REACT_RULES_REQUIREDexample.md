##  [Example](https://vercel.com/docs/conformance/rules/ESLINT_REACT_RULES_REQUIRED#example)[](https://vercel.com/docs/conformance/rules/ESLINT_REACT_RULES_REQUIRED#example)
```
A Conformance error occurred in test "ESLINT_REACT_RULES_REQUIRED".

These ESLint plugins must have rules configured to run: @next/next

To find out more information and how to fix this error, visit
https://vercel.com/docs/conformance/rules/ESLINT_REACT_RULES_REQUIRED.

If this violation should be ignored, add the following entry to
/apps/dashboard/.allowlists/ESLINT_REACT_RULES_REQUIRED.allowlist.json and
get approval from the appropriate person.

{
  "testName": "ESLINT_REACT_RULES_REQUIRED",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "dashboard"
  },
}
```

This check requires that certain ESLint plugins are installed and rules within those plugins are configured to be errors. If you are missing required plugins, you will receive an error such as:
```
ESLint configuration is missing required security plugins:
  Missing plugins: react, react-hooks, and jsx-a11y
  Registered plugins: import and @typescript-eslint
```

For more information on ESLint plugins and rules, see
