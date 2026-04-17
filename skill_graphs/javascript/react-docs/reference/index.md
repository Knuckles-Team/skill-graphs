[![logo by @sawaratsuki1004](https://react.dev/_next/image?url=%2Fimages%2Fuwu.png&w=128&q=75)](https://react.dev/)
[React](https://react.dev/)
[v19.2](https://react.dev/versions)
`⌘``Ctrl``K`
[Learn](https://react.dev/learn)
[Reference](https://react.dev/reference/react)
[Community](https://react.dev/community)
[Blog](https://react.dev/blog)
[](https://react.dev/community/translations)
![logo by @sawaratsuki1004](https://react.dev/_next/image?url=%2Fimages%2Fuwu.png&w=640&q=75)
# React
The library for web and native user interfaces
[Learn React](https://react.dev/learn)[API Reference](https://react.dev/reference/react)
## Create user interfaces from components
React lets you build user interfaces out of individual pieces called components. Create your own React components like `Thumbnail`, `LikeButton`, and `Video`. Then combine them into entire screens, pages, and apps.
### Video.js
```


function Video({ video }) {




  return (




    <div>




      <Thumbnail video={video} />




      <a href={video.url}>




        <h3>{video.title}</h3>




        <p>{video.description}</p>




      </a>




      <LikeButton video={video} />




    </div>




  );




}

```

My video Video description
Whether you work on your own or with thousands of other developers, using React feels the same. It is designed to let you seamlessly combine components written by independent people, teams, and organizations.
## Write components with code and markup
React components are JavaScript functions. Want to show some content conditionally? Use an `if` statement. Displaying a list? Try array `map()`. Learning React is learning programming.
### VideoList.js
```


function VideoList({ videos, emptyHeading }) {




  const count = videos.length;




  let heading = emptyHeading;




  if (count > 0) {




    const noun = count > 1 ? 'Videos' : 'Video';




    heading = count + ' ' + noun;




  }




  return (




    <section>




      <h2>{heading}</h2>




      {videos.map(video =>




        <Video key={video.id} video={video} />




      )}




    </section>




  );




}

```

## 3 Videos
First video Video description
Second video Video description
Third video Video description
This markup syntax is called JSX. It is a JavaScript syntax extension popularized by React. Putting JSX markup close to related rendering logic makes React components easy to create, maintain, and delete.
## Add interactivity wherever you need it
React components receive data and return what should appear on the screen. You can pass them new data in response to an interaction, like when the user types into an input. React will then update the screen to match the new data.
### SearchableVideoList.js
```


import { useState } from 'react';









function SearchableVideoList({ videos }) {




  const [searchText, setSearchText] = useState('');




  const foundVideos = filterVideos(videos, searchText);




  return (




    <>




      <SearchInput




        value={searchText}




        onChange={newText => setSearchText(newText)} />




      <VideoList




        videos={foundVideos}




        emptyHeading={`No matches for “${searchText}”`} />




    </>




  );




}

```

example.com/videos.html
# React Videos
A brief history of React
Search
## 5 Videos
You don’t have to build your whole page in React. Add React to your existing HTML page, and render interactive React components anywhere on it.
[](https://react.dev/learn/add-react-to-an-existing-project)
## Go full-stack
with a framework
React is a library. It lets you put components together, but it doesn’t prescribe how to do routing and data fetching. To build an entire app with React, we recommend a full-stack React framework like
### confs/[slug].js
```


import { db } from './database.js';





import { Suspense } from 'react';









async function ConferencePage({ slug }) {




  const conf = await db.Confs.find({ slug });




  return (




    <ConferenceLayout conf={conf}>




      <Suspense fallback={<TalksLoading />}>




        <Talks confId={conf.id} />




      </Suspense>




    </ConferenceLayout>




  );





}









async function Talks({ confId }) {




  const talks = await db.Talks.findAll({ confId });




  const videos = talks.map(talk => talk.video);




  return <SearchableVideoList videos={videos} />;




}

```

example.com/confs/react-conf-2021
React Conf 2021 React Conf 2019
![](https://react.dev/images/home/conf2021/cover.svg)
Search
## 19 Videos
React is also an architecture. Frameworks that implement it let you fetch data in asynchronous components that run on the server or even during the build. Read data from a file or a database, and pass it down to your interactive components.
[](https://react.dev/learn/creating-a-react-app)
## Use the best from every platform
People love web and native apps for different reasons. React lets you build both web apps and native apps using the same skills. It leans upon each platform’s unique strengths to let your interfaces feel just right on every platform.
example.com
#### Stay true to the web
People expect web app pages to load fast. On the server, React lets you start streaming HTML while you’re still fetching data, progressively filling in the remaining content before any JavaScript code loads. On the client, React can use standard web APIs to keep your UI responsive even in the middle of rendering.
4:27 PM
#### Go truly native
People expect native apps to look and feel like their platform. and let you build apps in React for Android, iOS, and more. They look and feel native because their UIs _are_ truly native. It’s not a web view—your React components render real Android and iOS views provided by the platform.
With React, you can be a web _and_ a native developer. Your team can ship to many platforms without sacrificing the user experience. Your organization can bridge the platform silos, and form teams that own entire features end-to-end.
## Upgrade when the future is ready
React approaches changes with care. Every React commit is tested on business-critical surfaces with over a billion users. Over 100,000 React components at Meta help validate every migration strategy.
The React team is always researching how to improve React. Some research takes years to pay off. React has a high bar for taking a research idea into production. Only proven approaches become a part of React.
[](https://react.dev/blog)
## [The React Foundation: A New Home for React Hosted by the Linux Foundation](https://react.dev/blog/2026/02/24/the-react-foundation)
## [Additional Vulnerabilities in RSC](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components)
## [Vulnerability in React Server Components](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)
## [React Conf 2025 Recap](https://react.dev/blog/2025/10/16/react-conf-2025-recap)
[](https://react.dev/blog)
## Join a community
of millions
You’re not alone. Two million developers from all over the world visit the React docs every month. React is something that people and teams can agree on.
![People singing karaoke at React Conf](https://react.dev/images/home/community/react_conf_fun.webp)
![Sunil Pai speaking at React India](https://react.dev/images/home/community/react_india_sunil.webp)
![A hallway conversation between two people at React Conf](https://react.dev/images/home/community/react_conf_hallway.webp)
![A hallway conversation at React India](https://react.dev/images/home/community/react_india_hallway.webp)
![Elizabet Oliveira speaking at React Conf](https://react.dev/images/home/community/react_conf_elizabet.webp)
![People taking a group selfie at React India](https://react.dev/images/home/community/react_india_selfie.webp)
![Nat Alison speaking at React Conf](https://react.dev/images/home/community/react_conf_nat.webp)
![Organizers greeting attendees at React India](https://react.dev/images/home/community/react_india_team.webp)
![People singing karaoke at React Conf](https://react.dev/images/home/community/react_conf_fun.webp)
![Sunil Pai speaking at React India](https://react.dev/images/home/community/react_india_sunil.webp)
![A hallway conversation between two people at React Conf](https://react.dev/images/home/community/react_conf_hallway.webp)
![A hallway conversation at React India](https://react.dev/images/home/community/react_india_hallway.webp)
![Elizabet Oliveira speaking at React Conf](https://react.dev/images/home/community/react_conf_elizabet.webp)
![People taking a group selfie at React India](https://react.dev/images/home/community/react_india_selfie.webp)
![Nat Alison speaking at React Conf](https://react.dev/images/home/community/react_conf_nat.webp)
![Organizers greeting attendees at React India](https://react.dev/images/home/community/react_india_team.webp)
This is why React is more than a library, an architecture, or even an ecosystem. React is a community. It’s a place where you can ask for help, find opportunities, and meet new friends. You will meet both developers and designers, beginners and experts, researchers and artists, teachers and students. Our backgrounds may be very different, but React lets us all create user interfaces together.
![logo by @sawaratsuki1004](https://react.dev/images/uwu.png)
## Welcome to the
React community
[Get Started](https://react.dev/learn)
Copyright © Meta Platforms, Inc
no uwu plz
uwu?
Logo by
[Learn React](https://react.dev/learn)
[Quick Start](https://react.dev/learn)
[Installation](https://react.dev/learn/installation)
[Describing the UI](https://react.dev/learn/describing-the-ui)
[Adding Interactivity](https://react.dev/learn/adding-interactivity)
[Managing State](https://react.dev/learn/managing-state)
[Escape Hatches](https://react.dev/learn/escape-hatches)
[API Reference](https://react.dev/reference/react)
[React APIs](https://react.dev/reference/react)
[React DOM APIs](https://react.dev/reference/react-dom)
[Community](https://react.dev/community)
[Meet the Team](https://react.dev/community/team)
[Docs Contributors](https://react.dev/community/docs-contributors)
[Acknowledgements](https://react.dev/community/acknowledgements)
More
[Blog](https://react.dev/blog)
