## Convention[](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention)
Intercepting routes can be defined with the `(..)` convention, which is similar to relative path convention `../` but for route segments.
You can use:
  * `(.)` to match segments on the **same level**
  * `(..)` to match segments **one level above**
  * `(..)(..)` to match segments **two levels above**
  * `(...)` to match segments from the **root** `app` directory


For example, you can intercept the `photo` segment from within the `feed` segment by creating a `(..)photo` directory.
![Intercepting routes folder structure](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fintercepted-routes-files.png&w=3840&q=75)![Intercepting routes folder structure](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fintercepted-routes-files.png&w=3840&q=75)
> **Good to know:** The `(..)` convention is based on _route segments_ , not the file-system. For example, it does not consider `@slot` folders in [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes).
