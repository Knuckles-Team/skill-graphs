[![logo by @sawaratsuki1004](https://react.dev/_next/image?url=%2Fimages%2Fuwu.png&w=128&q=75)](https://react.dev/)
[React](https://react.dev/)
[v19.2](https://react.dev/versions)
`⌘``Ctrl``K`
[Learn](https://react.dev/learn)
[Reference](https://react.dev/reference/react)
[Community](https://react.dev/community)
[Blog](https://react.dev/blog)
[](https://react.dev/community/translations)
### GET STARTED
  * [Quick Start ](https://react.dev/learn "Quick Start")
    * [Tutorial: Tic-Tac-Toe ](https://react.dev/learn/tutorial-tic-tac-toe "Tutorial: Tic-Tac-Toe")
    * [Thinking in React ](https://react.dev/learn/thinking-in-react "Thinking in React")
  * [Installation ](https://react.dev/learn/installation "Installation")
    * [Creating a React App ](https://react.dev/learn/creating-a-react-app "Creating a React App")
    * [Build a React App from Scratch ](https://react.dev/learn/build-a-react-app-from-scratch "Build a React App from Scratch")
    * [Add React to an Existing Project ](https://react.dev/learn/add-react-to-an-existing-project "Add React to an Existing Project")
  * [Setup ](https://react.dev/learn/setup "Setup")
    * [Editor Setup ](https://react.dev/learn/editor-setup "Editor Setup")
    * [Using TypeScript ](https://react.dev/learn/typescript "Using TypeScript")
    * [React Developer Tools ](https://react.dev/learn/react-developer-tools "React Developer Tools")
  * [React Compiler ](https://react.dev/learn/react-compiler "React Compiler")
    * [Introduction ](https://react.dev/learn/react-compiler/introduction "Introduction")
    * [Installation ](https://react.dev/learn/react-compiler/installation "Installation")
    * [Incremental Adoption ](https://react.dev/learn/react-compiler/incremental-adoption "Incremental Adoption")
    * [Debugging and Troubleshooting ](https://react.dev/learn/react-compiler/debugging "Debugging and Troubleshooting")
### LEARN REACT
  * [Describing the UI ](https://react.dev/learn/describing-the-ui "Describing the UI")
    * [Your First Component ](https://react.dev/learn/your-first-component "Your First Component")
    * [Importing and Exporting Components ](https://react.dev/learn/importing-and-exporting-components "Importing and Exporting Components")
    * [Writing Markup with JSX ](https://react.dev/learn/writing-markup-with-jsx "Writing Markup with JSX")
    * [JavaScript in JSX with Curly Braces ](https://react.dev/learn/javascript-in-jsx-with-curly-braces "JavaScript in JSX with Curly Braces")
    * [Passing Props to a Component ](https://react.dev/learn/passing-props-to-a-component "Passing Props to a Component")
    * [Conditional Rendering ](https://react.dev/learn/conditional-rendering "Conditional Rendering")
    * [Rendering Lists ](https://react.dev/learn/rendering-lists "Rendering Lists")
    * [Keeping Components Pure ](https://react.dev/learn/keeping-components-pure "Keeping Components Pure")
    * [Your UI as a Tree ](https://react.dev/learn/understanding-your-ui-as-a-tree "Your UI as a Tree")
  * [Adding Interactivity ](https://react.dev/learn/adding-interactivity "Adding Interactivity")
    * [Responding to Events ](https://react.dev/learn/responding-to-events "Responding to Events")
    * [State: A Component's Memory ](https://react.dev/learn/state-a-components-memory "State: A Component's Memory")
    * [Render and Commit ](https://react.dev/learn/render-and-commit "Render and Commit")
    * [State as a Snapshot ](https://react.dev/learn/state-as-a-snapshot "State as a Snapshot")
    * [Queueing a Series of State Updates ](https://react.dev/learn/queueing-a-series-of-state-updates "Queueing a Series of State Updates")
    * [Updating Objects in State ](https://react.dev/learn/updating-objects-in-state "Updating Objects in State")
    * [Updating Arrays in State ](https://react.dev/learn/updating-arrays-in-state "Updating Arrays in State")
  * [Managing State ](https://react.dev/learn/managing-state "Managing State")
    * [Reacting to Input with State ](https://react.dev/learn/reacting-to-input-with-state "Reacting to Input with State")
    * [Choosing the State Structure ](https://react.dev/learn/choosing-the-state-structure "Choosing the State Structure")
    * [Sharing State Between Components ](https://react.dev/learn/sharing-state-between-components "Sharing State Between Components")
    * [Preserving and Resetting State ](https://react.dev/learn/preserving-and-resetting-state "Preserving and Resetting State")
    * [Extracting State Logic into a Reducer ](https://react.dev/learn/extracting-state-logic-into-a-reducer "Extracting State Logic into a Reducer")
    * [Passing Data Deeply with Context ](https://react.dev/learn/passing-data-deeply-with-context "Passing Data Deeply with Context")
    * [Scaling Up with Reducer and Context ](https://react.dev/learn/scaling-up-with-reducer-and-context "Scaling Up with Reducer and Context")
  * [Escape Hatches ](https://react.dev/learn/escape-hatches "Escape Hatches")
    * [Referencing Values with Refs ](https://react.dev/learn/referencing-values-with-refs "Referencing Values with Refs")
    * [Manipulating the DOM with Refs ](https://react.dev/learn/manipulating-the-dom-with-refs "Manipulating the DOM with Refs")
    * [Synchronizing with Effects ](https://react.dev/learn/synchronizing-with-effects "Synchronizing with Effects")
    * [You Might Not Need an Effect ](https://react.dev/learn/you-might-not-need-an-effect "You Might Not Need an Effect")
    * [Lifecycle of Reactive Effects ](https://react.dev/learn/lifecycle-of-reactive-effects "Lifecycle of Reactive Effects")
    * [Separating Events from Effects ](https://react.dev/learn/separating-events-from-effects "Separating Events from Effects")
    * [Removing Effect Dependencies ](https://react.dev/learn/removing-effect-dependencies "Removing Effect Dependencies")
    * [Reusing Logic with Custom Hooks ](https://react.dev/learn/reusing-logic-with-custom-hooks "Reusing Logic with Custom Hooks")


[Learn React](https://react.dev/learn)
Copy pageCopy
# Escape Hatches[](https://react.dev/learn/escape-hatches#undefined "Link for this heading")
Advanced
Some of your components may need to control and synchronize with systems outside of React. For example, you might need to focus an input using the browser API, play and pause a video player implemented without React, or connect and listen to messages from a remote server. In this chapter, you’ll learn the escape hatches that let you “step outside” React and connect to external systems. Most of your application logic and data flow should not rely on these features.
### In this chapter
  * [How to “remember” information without re-rendering](https://react.dev/learn/referencing-values-with-refs)
  * [How to access DOM elements managed by React](https://react.dev/learn/manipulating-the-dom-with-refs)
  * [How to synchronize components with external systems](https://react.dev/learn/synchronizing-with-effects)
  * [How to remove unnecessary Effects from your components](https://react.dev/learn/you-might-not-need-an-effect)
  * [How an Effect’s lifecycle is different from a component’s](https://react.dev/learn/lifecycle-of-reactive-effects)
  * [How to prevent some values from re-triggering Effects](https://react.dev/learn/separating-events-from-effects)
  * [How to make your Effect re-run less often](https://react.dev/learn/removing-effect-dependencies)
  * [How to share logic between components](https://react.dev/learn/reusing-logic-with-custom-hooks)


## Referencing values with refs [](https://react.dev/learn/escape-hatches#referencing-values-with-refs "Link for Referencing values with refs ")
When you want a component to “remember” some information, but you don’t want that information to [trigger new renders](https://react.dev/learn/render-and-commit), you can use a _ref_ :
```


const ref = useRef(0);


```

Like state, refs are retained by React between re-renders. However, setting state re-renders a component. Changing a ref does not! You can access the current value of that ref through the `ref.current` property.
App.js
App.js
ReloadClear Fork
```
import { useRef } from 'react';

export default function Counter() {
  let ref = useRef(0);

  function handleClick() {
    ref.current = ref.current + 1;
    alert('You clicked ' + ref.current + ' times!');
  }

  return (
    <button onClick={handleClick}>
      Click me!
    </button>
  );
}


```

A ref is like a secret pocket of your component that React doesn’t track. For example, you can use refs to store
## Ready to learn this topic?
Read **[Referencing Values with Refs](https://react.dev/learn/referencing-values-with-refs)** to learn how to use refs to remember information.
[Read More](https://react.dev/learn/referencing-values-with-refs)
* * *
## Manipulating the DOM with refs [](https://react.dev/learn/escape-hatches#manipulating-the-dom-with-refs "Link for Manipulating the DOM with refs ")
React automatically updates the DOM to match your render output, so your components won’t often need to manipulate it. However, sometimes you might need access to the DOM elements managed by React—for example, to focus a node, scroll to it, or measure its size and position. There is no built-in way to do those things in React, so you will need a ref to the DOM node. For example, clicking the button will focus the input using a ref:
App.js
App.js
ReloadClear Fork
```
import { useRef } from 'react';

export default function Form() {
  const inputRef = useRef(null);

  function handleClick() {
    inputRef.current.focus();
  }

  return (
    <>
      <input ref={inputRef} />
      <button onClick={handleClick}>
        Focus the input
      </button>
    </>
  );
}


```

## Ready to learn this topic?
Read **[Manipulating the DOM with Refs](https://react.dev/learn/manipulating-the-dom-with-refs)** to learn how to access DOM elements managed by React.
[Read More](https://react.dev/learn/manipulating-the-dom-with-refs)
* * *
## Synchronizing with Effects [](https://react.dev/learn/escape-hatches#synchronizing-with-effects "Link for Synchronizing with Effects ")
Some components need to synchronize with external systems. For example, you might want to control a non-React component based on the React state, set up a server connection, or send an analytics log when a component appears on the screen. Unlike event handlers, which let you handle particular events, _Effects_ let you run some code after rendering. Use them to synchronize your component with a system outside of React.
Press Play/Pause a few times and see how the video player stays synchronized to the `isPlaying` prop value:
App.js
App.js
ReloadClear Fork
```
import { useState, useRef, useEffect } from 'react';

function VideoPlayer({ src, isPlaying }) {
  const ref = useRef(null);

  useEffect(() => {
    if (isPlaying) {
      ref.current.play();
    } else {
      ref.current.pause();
    }
  }, [isPlaying]);

  return <video ref={ref} src={src} loop playsInline />;
}

export default function App() {
  const [isPlaying, setIsPlaying] = useState(false);
  return (
    <>
      <button onClick={() => setIsPlaying(!isPlaying)}>
        {isPlaying ? 'Pause' : 'Play'}
      </button>
      <VideoPlayer
        isPlaying={isPlaying}
        src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
      />
    </>
  );
}


```

Many Effects also “clean up” after themselves. For example, an Effect that sets up a connection to a chat server should return a _cleanup function_ that tells React how to disconnect your component from that server:
App.jschat.js
App.js
ReloadClear Fork
```
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

export default function ChatRoom() {
  useEffect(() => {
    const connection = createConnection();
    connection.connect();
    return () => connection.disconnect();
  }, []);
  return <h1>Welcome to the chat!</h1>;
}


```

In development, React will immediately run and clean up your Effect one extra time. This is why you see `"✅ Connecting..."` printed twice. This ensures that you don’t forget to implement the cleanup function.
## Ready to learn this topic?
Read **[Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects)** to learn how to synchronize components with external systems.
[Read More](https://react.dev/learn/synchronizing-with-effects)
* * *
## You Might Not Need An Effect [](https://react.dev/learn/escape-hatches#you-might-not-need-an-effect "Link for You Might Not Need An Effect ")
Effects are an escape hatch from the React paradigm. They let you “step outside” of React and synchronize your components with some external system. If there is no external system involved (for example, if you want to update a component’s state when some props or state change), you shouldn’t need an Effect. Removing unnecessary Effects will make your code easier to follow, faster to run, and less error-prone.
There are two common cases in which you don’t need Effects:
  * **You don’t need Effects to transform data for rendering.**
  * **You don’t need Effects to handle user events.**


For example, you don’t need an Effect to adjust some state based on other state:
```


function Form() {




  const [firstName, setFirstName] = useState('Taylor');




  const [lastName, setLastName] = useState('Swift');








  // 🔴 Avoid: redundant state and unnecessary Effect




  const [fullName, setFullName] = useState('');




  useEffect(() => {




    setFullName(firstName + ' ' + lastName);




  }, [firstName, lastName]);




  // ...




}

```

Instead, calculate as much as you can while rendering:
```


function Form() {




  const [firstName, setFirstName] = useState('Taylor');




  const [lastName, setLastName] = useState('Swift');




  // ✅ Good: calculated during rendering




  const fullName = firstName + ' ' + lastName;




  // ...




}

```

However, you _do_ need Effects to synchronize with external systems.
## Ready to learn this topic?
Read **[You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect)** to learn how to remove unnecessary Effects.
[Read More](https://react.dev/learn/you-might-not-need-an-effect)
* * *
## Lifecycle of reactive effects [](https://react.dev/learn/escape-hatches#lifecycle-of-reactive-effects "Link for Lifecycle of reactive effects ")
Effects have a different lifecycle from components. Components may mount, update, or unmount. An Effect can only do two things: to start synchronizing something, and later to stop synchronizing it. This cycle can happen multiple times if your Effect depends on props and state that change over time.
This Effect depends on the value of the `roomId` prop. Props are _reactive values,_ which means they can change on a re-render. Notice that the Effect _re-synchronizes_ (and re-connects to the server) if `roomId` changes:
App.jschat.js
App.js
ReloadClear Fork
```
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);

  return <h1>Welcome to the {roomId} room!</h1>;
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}


```

React provides a linter rule to check that you’ve specified your Effect’s dependencies correctly. If you forget to specify `roomId` in the list of dependencies in the above example, the linter will find that bug automatically.
## Ready to learn this topic?
Read **[Lifecycle of Reactive Events](https://react.dev/learn/lifecycle-of-reactive-effects)** to learn how an Effect’s lifecycle is different from a component’s.
[Read More](https://react.dev/learn/lifecycle-of-reactive-effects)
* * *
## Separating events from Effects [](https://react.dev/learn/escape-hatches#separating-events-from-effects "Link for Separating events from Effects ")
Event handlers only re-run when you perform the same interaction again. Unlike event handlers, Effects re-synchronize if any of the values they read, like props or state, are different than during last render. Sometimes, you want a mix of both behaviors: an Effect that re-runs in response to some values but not others.
All code inside Effects is _reactive._ It will run again if some reactive value it reads has changed due to a re-render. For example, this Effect will re-connect to the chat if either `roomId` or `theme` have changed:
App.jschat.jsnotifications.js
App.js
ReloadClear Fork
```
import { useState, useEffect } from 'react';
import { createConnection, sendMessage } from './chat.js';
import { showNotification } from './notifications.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId, theme }) {
  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.on('connected', () => {
      showNotification('Connected!', theme);
    });
    connection.connect();
    return () => connection.disconnect();
  }, [roomId, theme]);

  return <h1>Welcome to the {roomId} room!</h1>
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  const [isDark, setIsDark] = useState(false);
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <label>
        <input
          type="checkbox"
          checked={isDark}
          onChange={e => setIsDark(e.target.checked)}
        />
        Use dark theme
      </label>
      <hr />
      <ChatRoom
        roomId={roomId}
        theme={isDark ? 'dark' : 'light'}
      />
    </>
  );
}


```

This is not ideal. You want to re-connect to the chat only if the `roomId` has changed. Switching the `theme` shouldn’t re-connect to the chat! Move the code reading `theme` out of your Effect into an _Effect Event_ :
App.jschat.js
App.js
ReloadClear Fork
```
import { useState, useEffect } from 'react';
import { useEffectEvent } from 'react';
import { createConnection, sendMessage } from './chat.js';
import { showNotification } from './notifications.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId, theme }) {
  const onConnected = useEffectEvent(() => {
    showNotification('Connected!', theme);
  });

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.on('connected', () => {
      onConnected();
    });
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);

  return <h1>Welcome to the {roomId} room!</h1>
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  const [isDark, setIsDark] = useState(false);
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <label>
        <input
          type="checkbox"
          checked={isDark}
          onChange={e => setIsDark(e.target.checked)}
        />
        Use dark theme
      </label>
      <hr />
      <ChatRoom
        roomId={roomId}
        theme={isDark ? 'dark' : 'light'}
      />
    </>
  );
}


```

Code inside Effect Events isn’t reactive, so changing the `theme` no longer makes your Effect re-connect.
## Ready to learn this topic?
Read **[Separating Events from Effects](https://react.dev/learn/separating-events-from-effects)** to learn how to prevent some values from re-triggering Effects.
[Read More](https://react.dev/learn/separating-events-from-effects)
* * *
## Removing Effect dependencies [](https://react.dev/learn/escape-hatches#removing-effect-dependencies "Link for Removing Effect dependencies ")
When you write an Effect, the linter will verify that you’ve included every reactive value (like props and state) that the Effect reads in the list of your Effect’s dependencies. This ensures that your Effect remains synchronized with the latest props and state of your component. Unnecessary dependencies may cause your Effect to run too often, or even create an infinite loop. The way you remove them depends on the case.
For example, this Effect depends on the `options` object which gets re-created every time you edit the input:
App.jschat.js
App.js
ReloadClear Fork
```
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  const [message, setMessage] = useState('');

  const options = {
    serverUrl: serverUrl,
    roomId: roomId
  };

  useEffect(() => {
    const connection = createConnection(options);
    connection.connect();
    return () => connection.disconnect();
  }, [options]);

  return (
    <>
      <h1>Welcome to the {roomId} room!</h1>
      <input value={message} onChange={e => setMessage(e.target.value)} />
    </>
  );
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}


```

You don’t want the chat to re-connect every time you start typing a message in that chat. To fix this problem, move creation of the `options` object inside the Effect so that the Effect only depends on the `roomId` string:
App.jschat.js
App.js
ReloadClear Fork
```
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const options = {
      serverUrl: serverUrl,
      roomId: roomId
    };
    const connection = createConnection(options);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);

  return (
    <>
      <h1>Welcome to the {roomId} room!</h1>
      <input value={message} onChange={e => setMessage(e.target.value)} />
    </>
  );
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}


```

Notice that you didn’t start by editing the dependency list to remove the `options` dependency. That would be wrong. Instead, you changed the surrounding code so that the dependency became _unnecessary._ Think of the dependency list as a list of all the reactive values used by your Effect’s code. You don’t intentionally choose what to put on that list. The list describes your code. To change the dependency list, change the code.
## Ready to learn this topic?
Read **[Removing Effect Dependencies](https://react.dev/learn/removing-effect-dependencies)** to learn how to make your Effect re-run less often.
[Read More](https://react.dev/learn/removing-effect-dependencies)
* * *
## Reusing logic with custom Hooks [](https://react.dev/learn/escape-hatches#reusing-logic-with-custom-hooks "Link for Reusing logic with custom Hooks ")
React comes with built-in Hooks like `useState`, `useContext`, and `useEffect`. Sometimes, you’ll wish that there was a Hook for some more specific purpose: for example, to fetch data, to keep track of whether the user is online, or to connect to a chat room. To do this, you can create your own Hooks for your application’s needs.
In this example, the `usePointerPosition` custom Hook tracks the cursor position, while `useDelayedValue` custom Hook returns a value that’s “lagging behind” the value you passed by a certain number of milliseconds. Move the cursor over the sandbox preview area to see a moving trail of dots following the cursor:
App.jsusePointerPosition.jsuseDelayedValue.js
App.js
ReloadClear Fork
```
import { usePointerPosition } from './usePointerPosition.js';
import { useDelayedValue } from './useDelayedValue.js';

export default function Canvas() {
  const pos1 = usePointerPosition();
  const pos2 = useDelayedValue(pos1, 100);
  const pos3 = useDelayedValue(pos2, 200);
  const pos4 = useDelayedValue(pos3, 100);
  const pos5 = useDelayedValue(pos4, 50);
  return (
    <>
      <Dot position={pos1} opacity={1} />
      <Dot position={pos2} opacity={0.8} />
      <Dot position={pos3} opacity={0.6} />
      <Dot position={pos4} opacity={0.4} />
      <Dot position={pos5} opacity={0.2} />
    </>
  );
}

function Dot({ position, opacity }) {
  return (
    <div style={{
      position: 'absolute',
      backgroundColor: 'pink',
      borderRadius: '50%',
      opacity,
      transform: `translate(${position.x}px, ${position.y}px)`,
      pointerEvents: 'none',
      left: -20,
      top: -20,
      width: 40,
      height: 40,
    }} />
  );
}


```

You can create custom Hooks, compose them together, pass data between them, and reuse them between components. As your app grows, you will write fewer Effects by hand because you’ll be able to reuse custom Hooks you already wrote. There are also many excellent custom Hooks maintained by the React community.
## Ready to learn this topic?
Read **[Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks)** to learn how to share logic between components.
[Read More](https://react.dev/learn/reusing-logic-with-custom-hooks)
* * *
## What’s next? [](https://react.dev/learn/escape-hatches#whats-next "Link for What’s next? ")
Head over to [Referencing Values with Refs](https://react.dev/learn/referencing-values-with-refs) to start reading this chapter page by page!
[ PreviousScaling Up with Reducer and Context ](https://react.dev/learn/scaling-up-with-reducer-and-context)[ NextReferencing Values with Refs ](https://react.dev/learn/referencing-values-with-refs)
* * *
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
## On this page
  * [Overview](https://react.dev/learn/escape-hatches)
  * [Referencing values with refs ](https://react.dev/learn/escape-hatches#referencing-values-with-refs)
  * [Manipulating the DOM with refs ](https://react.dev/learn/escape-hatches#manipulating-the-dom-with-refs)
  * [Synchronizing with Effects ](https://react.dev/learn/escape-hatches#synchronizing-with-effects)
  * [You Might Not Need An Effect ](https://react.dev/learn/escape-hatches#you-might-not-need-an-effect)
  * [Lifecycle of reactive effects ](https://react.dev/learn/escape-hatches#lifecycle-of-reactive-effects)
  * [Separating events from Effects ](https://react.dev/learn/escape-hatches#separating-events-from-effects)
  * [Removing Effect dependencies ](https://react.dev/learn/escape-hatches#removing-effect-dependencies)
  * [Reusing logic with custom Hooks ](https://react.dev/learn/escape-hatches#reusing-logic-with-custom-hooks)
  * [What’s next? ](https://react.dev/learn/escape-hatches#whats-next)


Escape Hatches – React
