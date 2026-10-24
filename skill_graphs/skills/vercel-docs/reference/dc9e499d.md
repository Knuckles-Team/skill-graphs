##  [Example](https://vercel.com/docs/getting-started-with-vercel#example)[](https://vercel.com/docs/getting-started-with-vercel#example)
An example of when this check would fail:
src/pages/index.tsx
```
import { type NextPage } from 'next';

const Home: NextPage = ({ users }) => {
  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};

Home.getInitialProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return { stars: json.stargazers_count };
};

export default Home;
```

In this example, the `getInitialProps` function is used to fetch data from an API, but it isn't necessary that we fetch the data on both the client and the server so we can fix it below.
