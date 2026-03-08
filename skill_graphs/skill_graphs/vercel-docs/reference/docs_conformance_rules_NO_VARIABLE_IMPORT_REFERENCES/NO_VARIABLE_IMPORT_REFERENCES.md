# NO_VARIABLE_IMPORT_REFERENCES
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
`import` and `require` statements load code from another file. When the location of the import is influenced by user input, the user may be able to load code that would otherwise be inaccessible to them. Such imports should protect against this by adding guards to make sure that arbitrary code can not be loaded from the import statement.
