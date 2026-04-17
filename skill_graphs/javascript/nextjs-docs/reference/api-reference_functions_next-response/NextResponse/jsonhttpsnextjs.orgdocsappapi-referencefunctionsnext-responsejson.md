##  `json()`[](https://nextjs.org/docs/app/api-reference/functions/next-response#json)
Produce a response with the given JSON body.
app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse } from 'next/server'

export async function GET(request: Request) {
  return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 })
}
```
