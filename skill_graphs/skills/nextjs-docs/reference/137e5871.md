# getStaticPaths
Last updated February 27, 2026
If a page has [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes) and uses `getStaticProps`, it needs to define a list of paths to be statically generated.
When you export a function called `getStaticPaths` (Static Site Generation) from a page that uses dynamic routes, Next.js will statically pre-render all the paths specified by `getStaticPaths`.
pages/repo/[name].tsx
TypeScript
JavaScript TypeScript
```
import type {
  InferGetStaticPropsType,
  GetStaticProps,
  GetStaticPaths,
} from 'next'

type Repo = {
  name: string
  stargazers_count: number
}

export const getStaticPaths = (async () => {
  return {
    paths: [
      {
        params: {
          name: 'next.js',
        },
      }, // See the "paths" section below
    ],
    fallback: true, // false or "blocking"
  }
}) satisfies GetStaticPaths

export const getStaticProps = (async (context) => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const repo = await res.json()
  return { props: { repo } }
}) satisfies GetStaticProps<{
  repo: Repo
}>

export default function Page({
  repo,
}: InferGetStaticPropsType<typeof getStaticProps>) {
  return repo.stargazers_count
}
```

The [`getStaticPaths` API reference](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths) covers all parameters and props that can be used with `getStaticPaths`.
