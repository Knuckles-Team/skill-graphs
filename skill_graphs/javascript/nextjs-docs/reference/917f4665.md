# reactCompiler
Last updated February 27, 2026
Next.js includes support for the `useMemo` and `useCallback`.
Next.js includes a custom performance optimization written in SWC that makes the React Compiler more efficient. Instead of running the compiler on every file, Next.js analyzes your project and only applies the React Compiler to relevant files. This avoids unnecessary work and leads to faster builds compared to using the Babel plugin on its own.
