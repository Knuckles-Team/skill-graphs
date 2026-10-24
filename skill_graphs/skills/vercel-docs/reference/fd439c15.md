##  [Example](https://vercel.com/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS#example)[](https://vercel.com/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS#example)
An example of when this check would fail:
src/pages/index.tsx
```
import { type GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return {
    props: { stargazersCount: json.stargazers_count },
  };
};

function Home({ stargazersCount }) {
  return <h1>The Next.js repo has {stargazersCount} stars.</h1>;
}

export default Home;
```

In this example, the `getServerSideProps` function is used to pass data from an API to the page, but it isn't using any information from the context argument so `getServerSideProps` is unnecessary.
