##  [Example](https://vercel.com/docs/getting-started-with-vercel#example)[](https://vercel.com/docs/getting-started-with-vercel#example)
component.ts
```
import { useState } from 'react';
import { useRouter } from 'next/router';
```

The `package.json` is missing a dependency on the `next` package.
package.json
```
{
  "name": "shared-component-pkg",
  "dependencies": {
    "react": "19.0.0-beta-4508873393-20240430"
  }
}
```
