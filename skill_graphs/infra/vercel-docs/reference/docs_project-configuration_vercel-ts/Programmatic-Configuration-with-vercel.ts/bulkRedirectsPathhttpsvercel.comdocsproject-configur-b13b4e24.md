##  [bulkRedirectsPath](https://vercel.com/docs/project-configuration/vercel-ts#bulkredirectspath)[](https://vercel.com/docs/project-configuration/vercel-ts#bulkredirectspath)
Learn more about [bulk redirects on Vercel](https://vercel.com/docs/redirects/bulk-redirects) and see [limits and pricing](https://vercel.com/docs/redirects/bulk-redirects#limits-and-pricing).
Type: `string` path to a file or folder.
The `bulkRedirectsPath` property can be used to import many thousands of redirects per project. These redirects do not support wildcard or header matching.
CSV, JSON, and JSONL file formats are supported, and the redirect files can be generated at build time as long as they end up in the location specified by `bulkRedirectsPath`. This can point to either a single file or a folder containing multiple redirect files.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  bulkRedirectsPath: 'redirects.csv',
};
```

###  [CSV](https://vercel.com/docs/project-configuration/vercel-ts#csv)[](https://vercel.com/docs/project-configuration/vercel-ts#csv)
CSV headers must match the field names below, can be specific in any order, and optional fields can be omitted.
redirects.csv
```
source,destination,permanent
/source/path,/destination/path,true
/source/path-2,https://destination-site.com/destination/path,true
```

###  [JSON](https://vercel.com/docs/project-configuration/vercel-ts#json)[](https://vercel.com/docs/project-configuration/vercel-ts#json)
redirects.json
```
[
    {
        "source": "/source/path",
        "destination": "/destination/path",
        "permanent": true
    },
    {
        "source": "/source/path-2",
        "destination": "https://destination-site.com/destination/path",
        "permanent": true
    }
]
```

###  [JSONL](https://vercel.com/docs/project-configuration/vercel-ts#jsonl)[](https://vercel.com/docs/project-configuration/vercel-ts#jsonl)
redirects.jsonl
```
{"source": "/source/path", "destination": "/destination/path", "permanent": true}
{"source": "/source/path-2", "destination": "https://destination-site.com/destination/path", "permanent": true}
```

Bulk redirects do not work locally while using `vercel dev`
###  [Bulk redirect field definition](https://vercel.com/docs/project-configuration/vercel-ts#bulk-redirect-field-definition)[](https://vercel.com/docs/project-configuration/vercel-ts#bulk-redirect-field-definition)
Field | Type | Required | Description
---|---|---|---
`source` | `string` | Yes | An absolute path that matches each incoming pathname (excluding querystring). Max 2048 characters.
`destination` | `string` | Yes | A location destination defined as an absolute pathname or external URL. Max 2048 characters.
`permanent` | `boolean` | No | Toggle between permanent (`false`.
`statusCode` | `integer` | No | Specify the exact status code. Can be
`caseSensitive` | `boolean` | No | Toggle whether source path matching is case sensitive. Default: `false`.
`preserveQueryParams` | `boolean` | No | Toggle whether to preserve the query string on the redirect. Default: `false`.
In order to improve space efficiency, all boolean values can be the single characters `t` (true) or `f` (false) while using the CSV format.
