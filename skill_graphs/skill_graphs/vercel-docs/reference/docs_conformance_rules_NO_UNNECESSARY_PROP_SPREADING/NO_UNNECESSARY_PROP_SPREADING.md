# NO_UNNECESSARY_PROP_SPREADING
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
This rule is available from version 1.6.0.
This rule detects the usage of the spread operator when spreading an object as a prop within a JSX component.
When spreading an object in the component, the data types of the object's properties are not validated, potentially causing unexpected runtime errors or unintended behavior.
