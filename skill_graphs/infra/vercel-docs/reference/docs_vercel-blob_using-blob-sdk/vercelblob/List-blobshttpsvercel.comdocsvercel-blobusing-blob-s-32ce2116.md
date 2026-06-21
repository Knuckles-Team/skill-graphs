##  [List blobs](https://vercel.com/docs/vercel-blob/using-blob-sdk#list-blobs)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#list-blobs)
This example creates a Function that returns a list of blob objects in a Blob store.
Next.js (/app)Next.js (/pages)Other frameworks
app/get-blobs/route.ts
TypeScript
TypeScript JavaScript Bash
```
import { list } from '@vercel/blob';

export async function GET(request: Request) {
  const { blobs } = await list();
  return Response.json(blobs);
}
```

###  [`list()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#list)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#list)
The `list` method returns a list of blob objects in a Blob store.
TypeScriptPython
```
list(options);
```

```
list_objects(
    *,
    limit: int | None = None,
    prefix: str | None = None,
    cursor: str | None = None,
    mode: str | None = None,
    token: str | None = None,
) -> ListBlobResult
```

It accepts the following parameters:
  * `options`: (Optional) A `JSON` object with the following optional parameters:


Parameter | Required | Values
---|---|---
`token` | No | A string specifying the read-write token to use when making requests. It defaults to `process.env.BLOB_READ_WRITE_TOKEN` when deployed on Vercel as explained in [Read-write token](https://vercel.com/docs/vercel-blob/using-blob-sdk#read-write-token)
`limit` | No | A number specifying the maximum number of blob objects to return. It defaults to 1000
`prefix` | No | A string used to filter for blob objects contained in a specific folder assuming that the folder name was used in the `pathname` when the blob object was uploaded
`cursor` | No | A string obtained from a previous `list` response to be used for reading the next page of results
`mode` | No | A string specifying the response format. Can either be `expanded` (default) or `folded`. In `folded` mode all blobs that are located inside a folder will be folded into a single folder string entry
`abortSignal` | No | An
`list()` returns a `JSON` object in the following format:
TypeScriptPython
```
{
  blobs: {
    size: number;
    uploadedAt: Date;
    pathname: string;
    url: string;
    downloadUrl: string;
    etag: string;
  }[];
  cursor?: string;
  hasMore: boolean;
  folders?: string[];
}
```

```
# ListBlobResult:
result.blobs          # list[ListBlobItem]
result.cursor         # str | None
result.has_more       # bool
result.folders        # list[str] | None

# ListBlobItem:
item.size # int
item.uploaded_at # datetime
item.pathname # str
item.url # str
item.download_url # str
item.etag # str
```

###  [Pagination](https://vercel.com/docs/vercel-blob/using-blob-sdk#pagination)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#pagination)
For a long list of blob objects (the default list `limit` is 1000), you can use the `cursor` and `hasMore` parameters to paginate through the results as shown in the example below:
TypeScriptPython
```
let hasMore = true;
let cursor;

while (hasMore) {
  const listResult = await list({
    cursor,
  });

  hasMore = listResult.hasMore;
  cursor = listResult.cursor;
}
```

```
from vercel.blob import list_objects

has_more = True
cursor = None

while has_more:
    page = list_objects(cursor=cursor, limit=1000)
    for b in page.blobs:
        # process each blob
        pass
    has_more = page.has_more
    cursor = page.cursor
```

###  [Folders](https://vercel.com/docs/vercel-blob/using-blob-sdk#folders)[](https://vercel.com/docs/vercel-blob/using-blob-sdk#folders)
To retrieve the folders from your blob store, alter the `mode` parameter to modify the response format of the list operation. The default value of `mode` is `expanded`, which returns all blobs in a single array of objects.
Alternatively, you can set `mode` to `folded` to roll up all blobs located inside a folder into a single entry. These entries will be included in the response as `folders`. Blobs that are not located in a folder will still be returned in the blobs property.
By using the `folded` mode, you can efficiently retrieve folders and subsequently list the blobs inside them by using the returned `folders` as a `prefix` for further requests. Omitting the `prefix` parameter entirely, will return all folders in the root of your store. Be aware that the blobs pathnames and the folder names will always be fully quantified and never relative to the prefix you passed.
TypeScriptPython
```
const {
  folders: [firstFolder],
  blobs: rootBlobs,
} = await list({ mode: 'folded' });

const { folders, blobs } = await list({ mode: 'folded', prefix: firstFolder });
```

```
from vercel.blob import list_objects

root = list_objects(mode="folded")
first_folder = root.folders[0]
sub = list_objects(mode="folded", prefix=first_folder)

```
