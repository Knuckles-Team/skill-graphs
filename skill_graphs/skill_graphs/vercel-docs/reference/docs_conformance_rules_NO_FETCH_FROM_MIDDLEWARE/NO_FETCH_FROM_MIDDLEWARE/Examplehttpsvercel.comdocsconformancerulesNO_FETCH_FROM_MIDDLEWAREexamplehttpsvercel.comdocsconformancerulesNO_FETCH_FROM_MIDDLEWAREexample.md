##  [Example](https://vercel.com/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE#example)[](https://vercel.com/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE#example)
This check will fail when a `fetch` call is detected from Next.js middleware or transitive dependencies used by the middleware file.
In this example, there are two files. An experiments file asynchronously fetches experiments using `fetch`. The middleware file uses the experiments library to fetch the experiments and then decide to rewrite the URL.
experiments.ts
```
export async function getExperiments() {
  const res = await fetch('/experiments');
  return res.json();
}
```

middleware.ts
```
export async function middleware(
  request: NextRequest,
  event: NextFetchEvent,
): Promise<Response> {
  const experiments = await getExperiments();

  if (experiments.includes('new-marketing-page)) {
    return NextResponse.rewrite(MARKETING_PAGE_URL);
  }
  return NextResponse.next();
}
```
