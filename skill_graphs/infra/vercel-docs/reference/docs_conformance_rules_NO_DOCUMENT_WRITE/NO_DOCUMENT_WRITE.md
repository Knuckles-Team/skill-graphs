# NO_DOCUMENT_WRITE
Last updated March 4, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Calls to `document.write()` or `document.writeln()` manipulate DOM directly without any sanitization and should be avoided.
Furthermore, these APIs can also cause performance issues and trigger will clear the page contents if used after page load.
