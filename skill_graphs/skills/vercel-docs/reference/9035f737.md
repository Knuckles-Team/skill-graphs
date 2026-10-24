##  [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)[](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)
Instead, we should use `getServerSideProps` instead of `getInitialProps`:
src/pages/index.tsx
```
import { type GetServerSideProps } from 'next';

const Home = ({ users }) => {
  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};

export getServerSideProps: GetServerSideProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return {
    props: {
      stars: json.stargazers_count
    },
  };
};

export default Home;
```

* * *
[ Previous Vercel Documentation ](https://vercel.com/docs)[ Next Projects and Deployments ](https://vercel.com/docs/getting-started-with-vercel/projects-deployments)
Was this helpful?
Send
On this page
  * [Example](https://vercel.com/docs/getting-started-with-vercel#example)
  * [How to fix](https://vercel.com/docs/getting-started-with-vercel#how-to-fix)


Copy as MarkdownGive feedbackAsk AI about this page
