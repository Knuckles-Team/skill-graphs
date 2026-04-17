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
# Adding Interactivity[](https://react.dev/learn/adding-interactivity#undefined "Link for this heading")
Some things on the screen update in response to user input. For example, clicking an image gallery switches the active image. In React, data that changes over time is called _state._ You can add state to any component, and update it as needed. In this chapter, you’ll learn how to write components that handle interactions, update their state, and display different output over time.
### In this chapter
  * [How to handle user-initiated events](https://react.dev/learn/responding-to-events)
  * [How to make components “remember” information with state](https://react.dev/learn/state-a-components-memory)
  * [How React updates the UI in two phases](https://react.dev/learn/render-and-commit)
  * [Why state doesn’t update right after you change it](https://react.dev/learn/state-as-a-snapshot)
  * [How to queue multiple state updates](https://react.dev/learn/queueing-a-series-of-state-updates)
  * [How to update an object in state](https://react.dev/learn/updating-objects-in-state)
  * [How to update an array in state](https://react.dev/learn/updating-arrays-in-state)


## Responding to events [](https://react.dev/learn/adding-interactivity#responding-to-events "Link for Responding to events ")
React lets you add _event handlers_ to your JSX. Event handlers are your own functions that will be triggered in response to user interactions like clicking, hovering, focusing on form inputs, and so on.
Built-in components like `<button>` only support built-in browser events like `onClick`. However, you can also create your own components, and give their event handler props any application-specific names that you like.
App.js
App.js
ReloadClear Fork
99
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
export default function App() {
return (
<Toolbar
onPlayMovie={() => alert('Playing!')}
onUploadImage={() => alert('Uploading!')}
/>
);
}


function Toolbar({ onPlayMovie, onUploadImage }) {
return (
<div>
<Button onClick={onPlayMovie}>
Play Movie
</Button>
<Button onClick={onUploadImage}>
Upload Image
</Button>
</div>
);
}


function Button({ onClick, children }) {
return (
<button onClick={onClick}>
{children}
</button>
);
}


## Ready to learn this topic?
Read **[Responding to Events](https://react.dev/learn/responding-to-events)** to learn how to add event handlers.
[Read More](https://react.dev/learn/responding-to-events)
* * *
## State: a component’s memory [](https://react.dev/learn/adding-interactivity#state-a-components-memory "Link for State: a component’s memory ")
Components often need to change what’s on the screen as a result of an interaction. Typing into the form should update the input field, clicking “next” on an image carousel should change which image is displayed, clicking “buy” puts a product in the shopping cart. Components need to “remember” things: the current input value, the current image, the shopping cart. In React, this kind of component-specific memory is called _state._
You can add state to a component with a [`useState`](https://react.dev/reference/react/useState) Hook. _Hooks_ are special functions that let your components use React features (state is one of those features). The `useState` Hook lets you declare a state variable. It takes the initial state and returns a pair of values: the current state, and a state setter function that lets you update it.
```


const [index, setIndex] = useState(0);





const [showMore, setShowMore] = useState(false);


```

Here is how an image gallery uses and updates state on click:
App.jsdata.js
App.js
ReloadClear Fork
99
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
import { useState } from 'react';
import { sculptureList } from './data.js';


export default function Gallery() {
const [index, setIndex] = useState(0);
const [showMore, setShowMore] = useState(false);
const hasNext = index < sculptureList.length - 1;


function handleNextClick() {
if (hasNext) {
setIndex(index + 1);
} else {
setIndex(0);
}
}


function handleMoreClick() {
setShowMore(!showMore);
}


let sculpture = sculptureList[index];
return (
<>
<button onClick={handleNextClick}>
Next
</button>
<h2>
<i>{sculpture.name} </i>
by {sculpture.artist}
</h2>
<h3>
({index + 1} of {sculptureList.length})
</h3>
<button onClick={handleMoreClick}>
{showMore ? 'Hide' : 'Show'} details
</button>
## Ready to learn this topic?
Read **[State: A Component’s Memory](https://react.dev/learn/state-a-components-memory)** to learn how to remember a value and update it on interaction.
[Read More](https://react.dev/learn/state-a-components-memory)
* * *
## Render and commit [](https://react.dev/learn/adding-interactivity#render-and-commit "Link for Render and commit ")
Before your components are displayed on the screen, they must be rendered by React. Understanding the steps in this process will help you think about how your code executes and explain its behavior.
Imagine that your components are cooks in the kitchen, assembling tasty dishes from ingredients. In this scenario, React is the waiter who puts in requests from customers and brings them their orders. This process of requesting and serving UI has three steps:
  1. **Triggering** a render (delivering the diner’s order to the kitchen)
  2. **Rendering** the component (preparing the order in the kitchen)
  3. **Committing** to the DOM (placing the order on the table)


  1. ![React as a server in a restaurant, fetching orders from the users and delivering them to the Component Kitchen.](https://react.dev/images/docs/illustrations/i_render-and-commit1.png)
Trigger
  2. ![The Card Chef gives React a fresh Card component.](https://react.dev/images/docs/illustrations/i_render-and-commit2.png)
Render
  3. ![React delivers the Card to the user at their table.](https://react.dev/images/docs/illustrations/i_render-and-commit3.png)
Commit


Illustrated by
## Ready to learn this topic?
Read **[Render and Commit](https://react.dev/learn/render-and-commit)** to learn the lifecycle of a UI update.
[Read More](https://react.dev/learn/render-and-commit)
* * *
## State as a snapshot [](https://react.dev/learn/adding-interactivity#state-as-a-snapshot "Link for State as a snapshot ")
Unlike regular JavaScript variables, React state behaves more like a snapshot. Setting it does not change the state variable you already have, but instead triggers a re-render. This can be surprising at first!
```


console.log(count);  // 0





setCount(count + 1); // Request a re-render with 1





console.log(count);  // Still 0!


```

This behavior helps you avoid subtle bugs. Here is a little chat app. Try to guess what happens if you press “Send” first and _then_ change the recipient to Bob. Whose name will appear in the `alert` five seconds later?
App.js
App.js
ReloadClear Fork
```
import { useState } from 'react';

export default function Form() {
  const [to, setTo] = useState('Alice');
  const [message, setMessage] = useState('Hello');

  function handleSubmit(e) {
    e.preventDefault();
    setTimeout(() => {
      alert(`You said ${message} to ${to}`);
    }, 5000);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        To:{' '}
        <select
          value={to}
          onChange={e => setTo(e.target.value)}>
          <option value="Alice">Alice</option>
          <option value="Bob">Bob</option>
        </select>
      </label>
      <textarea
        placeholder="Message"
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
      <button type="submit">Send</button>
    </form>
  );
}


```

## Ready to learn this topic?
Read **[State as a Snapshot](https://react.dev/learn/state-as-a-snapshot)** to learn why state appears “fixed” and unchanging inside the event handlers.
[Read More](https://react.dev/learn/state-as-a-snapshot)
* * *
## Queueing a series of state updates [](https://react.dev/learn/adding-interactivity#queueing-a-series-of-state-updates "Link for Queueing a series of state updates ")
This component is buggy: clicking “+3” increments the score only once.
App.js
App.js
ReloadClear Fork
```
import { useState } from 'react';

export default function Counter() {
  const [score, setScore] = useState(0);

  function increment() {
    setScore(score + 1);
  }

  return (
    <>
      <button onClick={() => increment()}>+1</button>
      <button onClick={() => {
        increment();
        increment();
        increment();
      }}>+3</button>
      <h1>Score: {score}</h1>
    </>
  )
}


```

[State as a Snapshot](https://react.dev/learn/state-as-a-snapshot) explains why this is happening. Setting state requests a new re-render, but does not change it in the already running code. So `score` continues to be `0` right after you call `setScore(score + 1)`.
```


console.log(score);  // 0





setScore(score + 1); // setScore(0 + 1);





console.log(score);  // 0





setScore(score + 1); // setScore(0 + 1);





console.log(score);  // 0





setScore(score + 1); // setScore(0 + 1);





console.log(score);  // 0


```

You can fix this by passing an _updater function_ when setting state. Notice how replacing `setScore(score + 1)` with `setScore(s => s + 1)` fixes the “+3” button. This lets you queue multiple state updates.
App.js
App.js
ReloadClear Fork
```
import { useState } from 'react';

export default function Counter() {
  const [score, setScore] = useState(0);

  function increment() {
    setScore(s => s + 1);
  }

  return (
    <>
      <button onClick={() => increment()}>+1</button>
      <button onClick={() => {
        increment();
        increment();
        increment();
      }}>+3</button>
      <h1>Score: {score}</h1>
    </>
  )
}


```

## Ready to learn this topic?
Read **[Queueing a Series of State Updates](https://react.dev/learn/queueing-a-series-of-state-updates)** to learn how to queue a sequence of state updates.
[Read More](https://react.dev/learn/queueing-a-series-of-state-updates)
* * *
## Updating objects in state [](https://react.dev/learn/adding-interactivity#updating-objects-in-state "Link for Updating objects in state ")
State can hold any kind of JavaScript value, including objects. But you shouldn’t change objects and arrays that you hold in the React state directly. Instead, when you want to update an object and array, you need to create a new one (or make a copy of an existing one), and then update the state to use that copy.
Usually, you will use the `...` spread syntax to copy objects and arrays that you want to change. For example, updating a nested object could look like this:
App.js
App.js
ReloadClear Fork
```
import { useState } from 'react';

export default function Form() {
  const [person, setPerson] = useState({
    name: 'Niki de Saint Phalle',
    artwork: {
      title: 'Blue Nana',
      city: 'Hamburg',
      image: 'https://i.imgur.com/Sd1AgUOm.jpg',
    }
  });

  function handleNameChange(e) {
    setPerson({
      ...person,
      name: e.target.value
    });
  }

  function handleTitleChange(e) {
    setPerson({
      ...person,
      artwork: {
        ...person.artwork,
        title: e.target.value
      }
    });
  }

  function handleCityChange(e) {
    setPerson({
      ...person,
      artwork: {
        ...person.artwork,
        city: e.target.value
      }
    });
  }

  function handleImageChange(e) {
    setPerson({
      ...person,
      artwork: {
        ...person.artwork,
        image: e.target.value
      }
    });
  }

  return (
    <>
      <label>
        Name:
        <input
          value={person.name}
          onChange={handleNameChange}
        />
      </label>
      <label>
        Title:
        <input
          value={person.artwork.title}
          onChange={handleTitleChange}
        />
      </label>
      <label>
        City:
        <input
          value={person.artwork.city}
          onChange={handleCityChange}
        />
      </label>
      <label>
        Image:
        <input
          value={person.artwork.image}
          onChange={handleImageChange}
        />
      </label>
      <p>
        <i>{person.artwork.title}</i>
        {' by '}
        {person.name}
        <br />
        (located in {person.artwork.city})
      </p>
      <img
        src={person.artwork.image}
        alt={person.artwork.title}
      />
    </>
  );
}


```

If copying objects in code gets tedious, you can use a library like
package.jsonApp.js
package.json
ReloadClear Fork
```
{
  "dependencies": {
    "immer": "1.7.3",
    "react": "latest",
    "react-dom": "latest",
    "react-scripts": "latest",
    "use-immer": "0.5.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject"
  },
  "devDependencies": {}
}
```

## Ready to learn this topic?
Read **[Updating Objects in State](https://react.dev/learn/updating-objects-in-state)** to learn how to update objects correctly.
[Read More](https://react.dev/learn/updating-objects-in-state)
* * *
## Updating arrays in state [](https://react.dev/learn/adding-interactivity#updating-arrays-in-state "Link for Updating arrays in state ")
Arrays are another type of mutable JavaScript objects you can store in state and should treat as read-only. Just like with objects, when you want to update an array stored in state, you need to create a new one (or make a copy of an existing one), and then set state to use the new array:
App.js
App.js
ReloadClear Fork
```
import { useState } from 'react';

const initialList = [
  { id: 0, title: 'Big Bellies', seen: false },
  { id: 1, title: 'Lunar Landscape', seen: false },
  { id: 2, title: 'Terracotta Army', seen: true },
];

export default function BucketList() {
  const [list, setList] = useState(
    initialList
  );

  function handleToggle(artworkId, nextSeen) {
    setList(list.map(artwork => {
      if (artwork.id === artworkId) {
        return { ...artwork, seen: nextSeen };
      } else {
        return artwork;
      }
    }));
  }

  return (
    <>
      <h1>Art Bucket List</h1>
      <h2>My list of art to see:</h2>
      <ItemList
        artworks={list}
        onToggle={handleToggle} />
    </>
  );
}

function ItemList({ artworks, onToggle }) {
  return (
    <ul>
      {artworks.map(artwork => (
        <li key={artwork.id}>
          <label>
            <input
              type="checkbox"
              checked={artwork.seen}
              onChange={e => {
                onToggle(
                  artwork.id,
                  e.target.checked
                );
              }}
            />
            {artwork.title}
          </label>
        </li>
      ))}
    </ul>
  );
}


```

If copying arrays in code gets tedious, you can use a library like
package.jsonApp.js
package.json
ReloadClear Fork
```
{
  "dependencies": {
    "immer": "1.7.3",
    "react": "latest",
    "react-dom": "latest",
    "react-scripts": "latest",
    "use-immer": "0.5.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject"
  },
  "devDependencies": {}
}
```

## Ready to learn this topic?
Read **[Updating Arrays in State](https://react.dev/learn/updating-arrays-in-state)** to learn how to update arrays correctly.
[Read More](https://react.dev/learn/updating-arrays-in-state)
* * *
## What’s next? [](https://react.dev/learn/adding-interactivity#whats-next "Link for What’s next? ")
Head over to [Responding to Events](https://react.dev/learn/responding-to-events) to start reading this chapter page by page!
Or, if you’re already familiar with these topics, why not read about [Managing State](https://react.dev/learn/managing-state)?
[ PreviousYour UI as a Tree ](https://react.dev/learn/understanding-your-ui-as-a-tree)[ NextResponding to Events ](https://react.dev/learn/responding-to-events)
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
  * [Overview](https://react.dev/learn/adding-interactivity)
  * [Responding to events ](https://react.dev/learn/adding-interactivity#responding-to-events)
  * [State: a component’s memory ](https://react.dev/learn/adding-interactivity#state-a-components-memory)
  * [Render and commit ](https://react.dev/learn/adding-interactivity#render-and-commit)
  * [State as a snapshot ](https://react.dev/learn/adding-interactivity#state-as-a-snapshot)
  * [Queueing a series of state updates ](https://react.dev/learn/adding-interactivity#queueing-a-series-of-state-updates)
  * [Updating objects in state ](https://react.dev/learn/adding-interactivity#updating-objects-in-state)
  * [Updating arrays in state ](https://react.dev/learn/adding-interactivity#updating-arrays-in-state)
  * [What’s next? ](https://react.dev/learn/adding-interactivity#whats-next)
