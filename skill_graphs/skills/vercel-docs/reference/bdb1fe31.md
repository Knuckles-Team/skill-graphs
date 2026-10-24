##  [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS#how-to-fix)[](https://vercel.com/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS#how-to-fix)
Instead, we can convert the page to use `getStaticProps`. This will generate the page at build time and serve it statically. If you need the page to be updated more frequently, then you can also use
src/pages/index.tsx
```
import { type GetStaticProps } from 'next';

export const getStaticProps: GetStaticProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return {
    props: { stargazersCount: json.stargazers_count },
    revalidate: 60, // Using ISR, regenerate the page every 60 seconds
  };
};

function Home({ stargazersCount }) {
  return <h1>The Next.js repo has {stargazersCount} stars.</h1>;
}

export default Home;
```

Or, you can use information from the context argument to customize the page:
src/pages/index.tsx
```
import { type GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async (context) => {
  const res = await fetch(
    `https://api.github.com/repos/vercel/${context.query.repoName}`,
  );
  const json = await res.json();
  return {
    props: {
      repoName: context.query.repoName,
      stargazersCount: json.stargazers_count,
    },
  };
};

function Home({ repoName, stargazersCount }) {
  return (
    <h1>
      The {repoName} repo has {stargazersCount} stars.
    </h1>
  );
}

export default Home;
```

* * *
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS#example)
  * [How to fix](https://vercel.com/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
