
**A mutable value like [`ref.current`](/reference/react/useRef#reference) or things you read from it also can't be a dependency.** The ref object returned by `useRef` itself can be a dependency, but its `current` property is intentionally mutable. It lets you [keep track of something without triggering a re-render.](/learn/referencing-values-with-refs) But since changing it doesn't trigger a re-render, it's not a reactive value, and React won't know to re-run your Effect when it changes.

As you'll learn below on this page, a linter will check for these issues automatically.

</DeepDive>

### React verifies that you specified every reactive value as a dependency {/*react-verifies-that-you-specified-every-reactive-value-as-a-dependency*/}

If your linter is [configured for React,](/learn/editor-setup#linting) it will check that every reactive value used by your Effect's code is declared as its dependency. For example, this is a lint error because both `roomId` and `serverUrl` are reactive:

<Sandpack>

```js
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

function ChatRoom({ roomId }) { // roomId is reactive
  const [serverUrl, setServerUrl] = useState('https://localhost:1234'); // serverUrl is reactive

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => connection.disconnect();
  }, []); // <-- Something's wrong here!

  return (
    <>
      <label>
        Server URL:{' '}
        <input
          value={serverUrl}
          onChange={e => setServerUrl(e.target.value)}
        />
      </label>
      <h1>Welcome to the {roomId} room!</h1>
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

```js src/chat.js
export function createConnection(serverUrl, roomId) {
  // A real implementation would actually connect to the server
  return {
    connect() {
      console.log('✅ Connecting to "' + roomId + '" room at ' + serverUrl + '...');
    },
    disconnect() {
      console.log('❌ Disconnected from "' + roomId + '" room at ' + serverUrl);
    }
  };
}
```

```css
input { display: block; margin-bottom: 20px; }
button { margin-left: 10px; }
```

</Sandpack>

This may look like a React error, but really React is pointing out a bug in your code. Both `roomId` and `serverUrl` may change over time, but you're forgetting to re-synchronize your Effect when they change. You will remain connected to the initial `roomId` and `serverUrl` even after the user picks different values in the UI.

To fix the bug, follow the linter's suggestion to specify `roomId` and `serverUrl` as dependencies of your Effect:

```js {9}
function ChatRoom({ roomId }) { // roomId is reactive
  const [serverUrl, setServerUrl] = useState('https://localhost:1234'); // serverUrl is reactive
  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, [serverUrl, roomId]); // ✅ All dependencies declared
  // ...
}
```

Try this fix in the sandbox above. Verify that the linter error is gone, and the chat re-connects when needed.

<Note>

In some cases, React *knows* that a value never changes even though it's declared inside the component. For example, the [`set` function](/reference/react/useState#setstate) returned from `useState` and the ref object returned by [`useRef`](/reference/react/useRef) are *stable*--they are guaranteed to not change on a re-render. Stable values aren't reactive, so you may omit them from the list. Including them is allowed: they won't change, so it doesn't matter.

</Note>

### What to do when you don't want to re-synchronize {/*what-to-do-when-you-dont-want-to-re-synchronize*/}

In the previous example, you've fixed the lint error by listing `roomId` and `serverUrl` as dependencies.

**However, you could instead "prove" to the linter that these values aren't reactive values,** i.e. that they *can't* change as a result of a re-render. For example, if `serverUrl` and `roomId` don't depend on rendering and always have the same values, you can move them outside the component. Now they don't need to be dependencies:

```js {1,2,11}
const serverUrl = 'https://localhost:1234'; // serverUrl is not reactive
const roomId = 'general'; // roomId is not reactive

function ChatRoom() {
  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, []); // ✅ All dependencies declared
  // ...
}
```

You can also move them *inside the Effect.* They aren't calculated during rendering, so they're not reactive:

```js {3,4,10}
function ChatRoom() {
  useEffect(() => {
    const serverUrl = 'https://localhost:1234'; // serverUrl is not reactive
    const roomId = 'general'; // roomId is not reactive
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, []); // ✅ All dependencies declared
  // ...
}
```

**Effects are reactive blocks of code.** They re-synchronize when the values you read inside of them change. Unlike event handlers, which only run once per interaction, Effects run whenever synchronization is necessary.

**You can't "choose" your dependencies.** Your dependencies must include every [reactive value](#all-variables-declared-in-the-component-body-are-reactive) you read in the Effect. The linter enforces this. Sometimes this may lead to problems like infinite loops and to your Effect re-synchronizing too often. Don't fix these problems by suppressing the linter! Here's what to try instead:

* **Check that your Effect represents an independent synchronization process.** If your Effect doesn't synchronize anything, [it might be unnecessary.](/learn/you-might-not-need-an-effect) If it synchronizes several independent things, [split it up.](#each-effect-represents-a-separate-synchronization-process)

* **If you want to read the latest value of props or state without "reacting" to it and re-synchronizing the Effect,** you can split your Effect into a reactive part (which you'll keep in the Effect) and a non-reactive part (which you'll extract into something called an _Effect Event_). [Read about separating Events from Effects.](/learn/separating-events-from-effects)

* **Avoid relying on objects and functions as dependencies.** If you create objects and functions during rendering and then read them from an Effect, they will be different on every render. This will cause your Effect to re-synchronize every time. [Read more about removing unnecessary dependencies from Effects.](/learn/removing-effect-dependencies)

<Pitfall>

The linter is your friend, but its powers are limited. The linter only knows when the dependencies are *wrong*. It doesn't know *the best* way to solve each case. If the linter suggests a dependency, but adding it causes a loop, it doesn't mean the linter should be ignored. You need to change the code inside (or outside) the Effect so that that value isn't reactive and doesn't *need* to be a dependency.

If you have an existing codebase, you might have some Effects that suppress the linter like this:

```js {3-4}
useEffect(() => {
  // ...
  // 🔴 Avoid suppressing the linter like this:
  // eslint-ignore-next-line react-hooks/exhaustive-deps
}, []);
```

On the [next](/learn/separating-events-from-effects) [pages](/learn/removing-effect-dependencies), you'll learn how to fix this code without breaking the rules. It's always worth fixing!

</Pitfall>

<Recap>

- Components can mount, update, and unmount.
- Each Effect has a separate lifecycle from the surrounding component.
- Each Effect describes a separate synchronization process that can *start* and *stop*.
- When you write and read Effects, think from each individual Effect's perspective (how to start and stop synchronization) rather than from the component's perspective (how it mounts, updates, or unmounts).
- Values declared inside the component body are "reactive".
- Reactive values should re-synchronize the Effect because they can change over time.
- The linter verifies that all reactive values used inside the Effect are specified as dependencies.
- All errors flagged by the linter are legitimate. There's always a way to fix the code to not break the rules.

</Recap>

<Challenges>

#### Fix reconnecting on every keystroke {/*fix-reconnecting-on-every-keystroke*/}

In this example, the `ChatRoom` component connects to the chat room when the component mounts, disconnects when it unmounts, and reconnects when you select a different chat room. This behavior is correct, so you need to keep it working.

However, there is a problem. Whenever you type into the message box input at the bottom, `ChatRoom` *also* reconnects to the chat. (You can notice this by clearing the console and typing into the input.) Fix the issue so that this doesn't happen.

<Hint>

You might need to add a dependency array for this Effect. What dependencies should be there?

</Hint>

<Sandpack>

```js
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => connection.disconnect();
  });

  return (
    <>
      <h1>Welcome to the {roomId} room!</h1>
      <input
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
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

```js src/chat.js
export function createConnection(serverUrl, roomId) {
  // A real implementation would actually connect to the server
  return {
    connect() {
      console.log('✅ Connecting to "' + roomId + '" room at ' + serverUrl + '...');
    },
    disconnect() {
      console.log('❌ Disconnected from "' + roomId + '" room at ' + serverUrl);
    }
  };
}
```

```css
input { display: block; margin-bottom: 20px; }
button { margin-left: 10px; }
```

</Sandpack>

<Solution>

This Effect didn't have a dependency array at all, so it re-synchronized after every re-render. First, add a dependency array. Then, make sure that every reactive value used by the Effect is specified in the array. For example, `roomId` is reactive (because it's a prop), so it should be included in the array. This ensures that when the user selects a different room, the chat reconnects. On the other hand, `serverUrl` is defined outside the component. This is why it doesn't need to be in the array.

<Sandpack>

```js
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);

  return (
    <>
      <h1>Welcome to the {roomId} room!</h1>
      <input
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
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

```js src/chat.js
export function createConnection(serverUrl, roomId) {
  // A real implementation would actually connect to the server
  return {
    connect() {
      console.log('✅ Connecting to "' + roomId + '" room at ' + serverUrl + '...');
    },
    disconnect() {
      console.log('❌ Disconnected from "' + roomId + '" room at ' + serverUrl);
    }
  };
}
```

```css
input { display: block; margin-bottom: 20px; }
button { margin-left: 10px; }
```

</Sandpack>

</Solution>

#### Switch synchronization on and off {/*switch-synchronization-on-and-off*/}

In this example, an Effect subscribes to the window [`pointermove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointermove_event) event to move a pink dot on the screen. Try hovering over the preview area (or touching the screen if you're on a mobile device), and see how the pink dot follows your movement.

There is also a checkbox. Ticking the checkbox toggles the `canMove` state variable, but this state variable is not used anywhere in the code. Your task is to change the code so that when `canMove` is `false` (the checkbox is ticked off), the dot should stop moving. After you toggle the checkbox back on (and set `canMove` to `true`), the box should follow the movement again. In other words, whether the dot can move or not should stay synchronized to whether the checkbox is checked.

<Hint>

You can't declare an Effect conditionally. However, the code inside the Effect can use conditions!

</Hint>

<Sandpack>

```js
import { useState, useEffect } from 'react';

export default function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [canMove, setCanMove] = useState(true);

  useEffect(() => {
    function handleMove(e) {
      setPosition({ x: e.clientX, y: e.clientY });
    }
    window.addEventListener('pointermove', handleMove);
    return () => window.removeEventListener('pointermove', handleMove);
  }, []);

  return (
    <>
      <label>
        <input type="checkbox"
          checked={canMove}
          onChange={e => setCanMove(e.target.checked)}
        />
        The dot is allowed to move
      </label>
      <hr />
      <div style={{
        position: 'absolute',
        backgroundColor: 'pink',
        borderRadius: '50%',
        opacity: 0.6,
        transform: `translate(${position.x}px, ${position.y}px)`,
        pointerEvents: 'none',
        left: -20,
        top: -20,
        width: 40,
        height: 40,
      }} />
    </>
  );
}
```

```css
body {
  height: 200px;
}
```

</Sandpack>

<Solution>

One solution is to wrap the `setPosition` call into an `if (canMove) { ... }` condition:

<Sandpack>

```js
import { useState, useEffect } from 'react';

export default function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [canMove, setCanMove] = useState(true);

  useEffect(() => {
    function handleMove(e) {
      if (canMove) {
        setPosition({ x: e.clientX, y: e.clientY });
      }
    }
    window.addEventListener('pointermove', handleMove);
    return () => window.removeEventListener('pointermove', handleMove);
  }, [canMove]);

  return (
    <>
      <label>
        <input type="checkbox"
          checked={canMove}
          onChange={e => setCanMove(e.target.checked)}
        />
        The dot is allowed to move
      </label>
      <hr />
      <div style={{
        position: 'absolute',
        backgroundColor: 'pink',
        borderRadius: '50%',
        opacity: 0.6,
        transform: `translate(${position.x}px, ${position.y}px)`,
        pointerEvents: 'none',
        left: -20,
        top: -20,
        width: 40,
        height: 40,
      }} />
    </>
  );
}
```

```css
body {
  height: 200px;
}
```

</Sandpack>

Alternatively, you could wrap the *event subscription* logic into an `if (canMove) { ... }` condition:

<Sandpack>

```js
import { useState, useEffect } from 'react';

export default function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [canMove, setCanMove] = useState(true);

  useEffect(() => {
    function handleMove(e) {
      setPosition({ x: e.clientX, y: e.clientY });
    }
    if (canMove) {
      window.addEventListener('pointermove', handleMove);
      return () => window.removeEventListener('pointermove', handleMove);
    }
  }, [canMove]);

  return (
    <>
      <label>
        <input type="checkbox"
          checked={canMove}
          onChange={e => setCanMove(e.target.checked)}
        />
        The dot is allowed to move
      </label>
      <hr />
      <div style={{
        position: 'absolute',
        backgroundColor: 'pink',
        borderRadius: '50%',
        opacity: 0.6,
        transform: `translate(${position.x}px, ${position.y}px)`,
        pointerEvents: 'none',
        left: -20,
        top: -20,
        width: 40,
        height: 40,
      }} />
    </>
  );
}
```

```css
body {
  height: 200px;
}
```

</Sandpack>

In both of these cases, `canMove` is a reactive variable that you read inside the Effect. This is why it must be specified in the list of Effect dependencies. This ensures that the Effect re-synchronizes after every change to its value.

</Solution>

#### Investigate a stale value bug {/*investigate-a-stale-value-bug*/}

In this example, the pink dot should move when the checkbox is on, and should stop moving when the checkbox is off. The logic for this has already been implemented: the `handleMove` event handler checks the `canMove` state variable.

However, for some reason, the `canMove` state variable inside `handleMove` appears to be "stale": it's always `true`, even after you tick off the checkbox. How is this possible? Find the mistake in the code and fix it.

<Hint>

If you see a linter rule being suppressed, remove the suppression! That's where the mistakes usually are.

</Hint>

<Sandpack>

```js {expectedErrors: {'react-compiler': [16]}}
import { useState, useEffect } from 'react';

export default function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [canMove, setCanMove] = useState(true);

  function handleMove(e) {
    if (canMove) {
      setPosition({ x: e.clientX, y: e.clientY });
    }
  }

  useEffect(() => {
    window.addEventListener('pointermove', handleMove);
    return () => window.removeEventListener('pointermove', handleMove);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <label>
        <input type="checkbox"
          checked={canMove}
          onChange={e => setCanMove(e.target.checked)}
        />
        The dot is allowed to move
      </label>
      <hr />
      <div style={{
        position: 'absolute',
        backgroundColor: 'pink',
        borderRadius: '50%',
        opacity: 0.6,
        transform: `translate(${position.x}px, ${position.y}px)`,
        pointerEvents: 'none',
        left: -20,
        top: -20,
        width: 40,
        height: 40,
      }} />
    </>
  );
}
```

```css
body {
  height: 200px;
}
```

</Sandpack>

<Solution>

The problem with the original code was suppressing the dependency linter. If you remove the suppression, you'll see that this Effect depends on the `handleMove` function. This makes sense: `handleMove` is declared inside the component body, which makes it a reactive value. Every reactive value must be specified as a dependency, or it can potentially get stale over time!

The author of the original code has "lied" to React by saying that the Effect does not depend (`[]`) on any reactive values. This is why React did not re-synchronize the Effect after `canMove` has changed (and `handleMove` with it). Because React did not re-synchronize the Effect, the `handleMove` attached as a listener is the `handleMove` function created during the initial render. During the initial render, `canMove` was `true`, which is why `handleMove` from the initial render will forever see that value.

**If you never suppress the linter, you will never see problems with stale values.** There are a few different ways to solve this bug, but you should always start by removing the linter suppression. Then change the code to fix the lint error.

You can change the Effect dependencies to `[handleMove]`, but since it's going to be a newly defined function for every render, you might as well remove dependencies array altogether. Then the Effect *will* re-synchronize after every re-render:

<Sandpack>

```js
import { useState, useEffect } from 'react';

export default function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [canMove, setCanMove] = useState(true);

  function handleMove(e) {
    if (canMove) {
      setPosition({ x: e.clientX, y: e.clientY });
    }
  }

  useEffect(() => {
    window.addEventListener('pointermove', handleMove);
    return () => window.removeEventListener('pointermove', handleMove);
  });

  return (
    <>
      <label>
        <input type="checkbox"
          checked={canMove}
          onChange={e => setCanMove(e.target.checked)}
        />
        The dot is allowed to move
      </label>
      <hr />
      <div style={{
        position: 'absolute',
        backgroundColor: 'pink',
        borderRadius: '50%',
        opacity: 0.6,
        transform: `translate(${position.x}px, ${position.y}px)`,
        pointerEvents: 'none',
        left: -20,
        top: -20,
        width: 40,
        height: 40,
      }} />
    </>
  );
}
```

```css
body {
  height: 200px;
}
```

</Sandpack>

This solution works, but it's not ideal. If you put `console.log('Resubscribing')` inside the Effect, you'll notice that it resubscribes after every re-render. Resubscribing is fast, but it would still be nice to avoid doing it so often.

A better fix would be to move the `handleMove` function *inside* the Effect. Then `handleMove` won't be a reactive value, and so your Effect won't depend on a function. Instead, it will need to depend on `canMove` which your code now reads from inside the Effect. This matches the behavior you wanted, since your Effect will now stay synchronized with the value of `canMove`:

<Sandpack>

```js
import { useState, useEffect } from 'react';

export default function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [canMove, setCanMove] = useState(true);

  useEffect(() => {
    function handleMove(e) {
      if (canMove) {
        setPosition({ x: e.clientX, y: e.clientY });
      }
    }

    window.addEventListener('pointermove', handleMove);
    return () => window.removeEventListener('pointermove', handleMove);
  }, [canMove]);

  return (
    <>
      <label>
        <input type="checkbox"
          checked={canMove}
          onChange={e => setCanMove(e.target.checked)}
        />
        The dot is allowed to move
      </label>
      <hr />
      <div style={{
        position: 'absolute',
        backgroundColor: 'pink',
        borderRadius: '50%',
        opacity: 0.6,
        transform: `translate(${position.x}px, ${position.y}px)`,
        pointerEvents: 'none',
        left: -20,
        top: -20,
        width: 40,
        height: 40,
      }} />
    </>
  );
}
```

```css
body {
  height: 200px;
}
```

</Sandpack>

Try adding `console.log('Resubscribing')` inside the Effect body and notice that now it only resubscribes when you toggle the checkbox (`canMove` changes) or edit the code. This makes it better than the previous approach that always resubscribed.

You'll learn a more general approach to this type of problem in [Separating Events from Effects.](/learn/separating-events-from-effects)

</Solution>

#### Fix a connection switch {/*fix-a-connection-switch*/}

In this example, the chat service in `chat.js` exposes two different APIs: `createEncryptedConnection` and `createUnencryptedConnection`. The root `App` component lets the user choose whether to use encryption or not, and then passes down the corresponding API method to the child `ChatRoom` component as the `createConnection` prop.

Notice that initially, the console logs say the connection is not encrypted. Try toggling the checkbox on: nothing will happen. However, if you change the selected room after that, then the chat will reconnect *and* enable encryption (as you'll see from the console messages). This is a bug. Fix the bug so that toggling the checkbox *also* causes the chat to reconnect.

<Hint>

Suppressing the linter is always suspicious. Could this be a bug?

</Hint>

<Sandpack>

```js src/App.js
import { useState } from 'react';
import ChatRoom from './ChatRoom.js';
import {
  createEncryptedConnection,
  createUnencryptedConnection,
} from './chat.js';

export default function App() {
  const [roomId, setRoomId] = useState('general');
  const [isEncrypted, setIsEncrypted] = useState(false);
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
