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
[Adding Interactivity](https://react.dev/learn/adding-interactivity)
Copy pageCopy
# Responding to Events[](https://react.dev/learn/responding-to-events#undefined "Link for this heading")
React lets you add _event handlers_ to your JSX. Event handlers are your own functions that will be triggered in response to interactions like clicking, hovering, focusing form inputs, and so on.
### You will learn
  * Different ways to write an event handler
  * How to pass event handling logic from a parent component
  * How events propagate and how to stop them


## Adding event handlers [](https://react.dev/learn/responding-to-events#adding-event-handlers "Link for Adding event handlers ")
To add an event handler, you will first define a function and then [pass it as a prop](https://react.dev/learn/passing-props-to-a-component) to the appropriate JSX tag. For example, here is a button that doesn’t do anything yet:
App.js
App.js
ReloadClear
9
1
2
3
4
5
6
7
8
export default function Button() {
return (
<button>
I don't do anything
</button>
);
}


You can make it show a message when a user clicks by following these three steps:
  1. Declare a function called `handleClick` _inside_ your `Button` component.
  2. Implement the logic inside that function (use `alert` to show the message).
  3. Add `onClick={handleClick}` to the `<button>` JSX.


App.js
App.js
ReloadClear Fork
```
export default function Button() {
  function handleClick() {
    alert('You clicked me!');
  }

  return (
    <button onClick={handleClick}>
      Click me
    </button>
  );
}


```

You defined the `handleClick` function and then [passed it as a prop](https://react.dev/learn/passing-props-to-a-component) to `<button>`. `handleClick` is an **event handler.** Event handler functions:
  * Are usually defined _inside_ your components.
  * Have names that start with `handle`, followed by the name of the event.


By convention, it is common to name event handlers as `handle` followed by the event name. You’ll often see `onClick={handleClick}`, `onMouseEnter={handleMouseEnter}`, and so on.
Alternatively, you can define an event handler inline in the JSX:
```


<button onClick={function handleClick() {




  alert('You clicked me!');





}}>


```

Or, more concisely, using an arrow function:
```


<button onClick={() => {




  alert('You clicked me!');





}}>


```

All of these styles are equivalent. Inline event handlers are convenient for short functions.
Functions passed to event handlers must be passed, not called. For example:
passing a function (correct) | calling a function (incorrect)
---|---
`<button onClick={handleClick}>` | `<button onClick={handleClick()}>`
The difference is subtle. In the first example, the `handleClick` function is passed as an `onClick` event handler. This tells React to remember it and only call your function when the user clicks the button.
In the second example, the `()` at the end of `handleClick()` fires the function _immediately_ during [rendering](https://react.dev/learn/render-and-commit), without any clicks. This is because JavaScript inside the [JSX `{` and `}`](https://react.dev/learn/javascript-in-jsx-with-curly-braces) executes right away.
When you write code inline, the same pitfall presents itself in a different way:
passing a function (correct) | calling a function (incorrect)
---|---
`<button onClick={() => alert('...')}>` | `<button onClick={alert('...')}>`
Passing inline code like this won’t fire on click—it fires every time the component renders:
```


// This alert fires when the component renders, not when clicked!





<button onClick={alert('You clicked me!')}>


```

If you want to define your event handler inline, wrap it in an anonymous function like so:
```


<button onClick={() => alert('You clicked me!')}>


```

Rather than executing the code inside with every render, this creates a function to be called later.
In both cases, what you want to pass is a function:
  * `<button onClick={handleClick}>` passes the `handleClick` function.
  * `<button onClick={() => alert('...')}>` passes the `() => alert('...')` function.


### Reading props in event handlers [](https://react.dev/learn/responding-to-events#reading-props-in-event-handlers "Link for Reading props in event handlers ")
Because event handlers are declared inside of a component, they have access to the component’s props. Here is a button that, when clicked, shows an alert with its `message` prop:
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
function AlertButton({ message, children }) {
return (
<button onClick={() => alert(message)}>
{children}
</button>
);
}


export default function Toolbar() {
return (
<div>
<AlertButton message="Playing!">
Play Movie
</AlertButton>
<AlertButton message="Uploading!">
Upload Image
</AlertButton>
</div>
);
}


This lets these two buttons show different messages. Try changing the messages passed to them.
### Passing event handlers as props [](https://react.dev/learn/responding-to-events#passing-event-handlers-as-props "Link for Passing event handlers as props ")
Often you’ll want the parent component to specify a child’s event handler. Consider buttons: depending on where you’re using a `Button` component, you might want to execute a different function—perhaps one plays a movie and another uploads an image.
To do this, pass a prop the component receives from its parent as the event handler like so:
App.js
App.js
ReloadClear Fork
```
function Button({ onClick, children }) {
  return (
    <button onClick={onClick}>
      {children}
    </button>
  );
}

function PlayButton({ movieName }) {
  function handlePlayClick() {
    alert(`Playing ${movieName}!`);
  }

  return (
    <Button onClick={handlePlayClick}>
      Play "{movieName}"
    </Button>
  );
}

function UploadButton() {
  return (
    <Button onClick={() => alert('Uploading!')}>
      Upload Image
    </Button>
  );
}

export default function Toolbar() {
  return (
    <div>
      <PlayButton movieName="Kiki's Delivery Service" />
      <UploadButton />
    </div>
  );
}


```

Here, the `Toolbar` component renders a `PlayButton` and an `UploadButton`:
  * `PlayButton` passes `handlePlayClick` as the `onClick` prop to the `Button` inside.
  * `UploadButton` passes `() => alert('Uploading!')` as the `onClick` prop to the `Button` inside.


Finally, your `Button` component accepts a prop called `onClick`. It passes that prop directly to the built-in browser `<button>` with `onClick={onClick}`. This tells React to call the passed function on click.
If you use a `PlayButton` and `UploadButton` will pass event handlers down.
### Naming event handler props [](https://react.dev/learn/responding-to-events#naming-event-handler-props "Link for Naming event handler props ")
Built-in components like `<button>` and `<div>` only support [browser event names](https://react.dev/reference/react-dom/components/common#common-props) like `onClick`. However, when you’re building your own components, you can name their event handler props any way that you like.
By convention, event handler props should start with `on`, followed by a capital letter.
For example, the `Button` component’s `onClick` prop could have been called `onSmash`:
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
function Button({ onSmash, children }) {
return (
<button onClick={onSmash}>
{children}
</button>
);
}


export default function App() {
return (
<div>
<Button onSmash={() => alert('Playing!')}>
Play Movie
</Button>
<Button onSmash={() => alert('Uploading!')}>
Upload Image
</Button>
</div>
);
}


In this example, `<button onClick={onSmash}>` shows that the browser `<button>` (lowercase) still needs a prop called `onClick`, but the prop name received by your custom `Button` component is up to you!
When your component supports multiple interactions, you might name event handler props for app-specific concepts. For example, this `Toolbar` component receives `onPlayMovie` and `onUploadImage` event handlers:
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


Notice how the `App` component does not need to know _what_ `Toolbar` will do with `onPlayMovie` or `onUploadImage`. That’s an implementation detail of the `Toolbar`. Here, `Toolbar` passes them down as `onClick` handlers to its `Button`s, but it could later also trigger them on a keyboard shortcut. Naming props after app-specific interactions like `onPlayMovie` gives you the flexibility to change how they’re used later.
Make sure that you use the appropriate HTML tags for your event handlers. For example, to handle clicks, use `<div onClick={handleClick}>`. Using a real browser `<button>` enables built-in browser behaviors like keyboard navigation. If you don’t like the default browser styling of a button and want to make it look more like a link or a different UI element, you can achieve it with CSS.
## Event propagation [](https://react.dev/learn/responding-to-events#event-propagation "Link for Event propagation ")
Event handlers will also catch events from any children your component might have. We say that an event “bubbles” or “propagates” up the tree: it starts with where the event happened, and then goes up the tree.
This `<div>` contains two buttons. Both the `<div>` _and_ each button have their own `onClick` handlers. Which handlers do you think will fire when you click a button?
App.js
App.js
ReloadClear Fork
```
export default function Toolbar() {
  return (
    <div className="Toolbar" onClick={() => {
      alert('You clicked on the toolbar!');
    }}>
      <button onClick={() => alert('Playing!')}>
        Play Movie
      </button>
      <button onClick={() => alert('Uploading!')}>
        Upload Image
      </button>
    </div>
  );
}


```

If you click on either button, its `onClick` will run first, followed by the parent `<div>`’s `onClick`. So two messages will appear. If you click the toolbar itself, only the parent `<div>`’s `onClick` will run.
All events propagate in React except `onScroll`, which only works on the JSX tag you attach it to.
### Stopping propagation [](https://react.dev/learn/responding-to-events#stopping-propagation "Link for Stopping propagation ")
Event handlers receive an **event object** as their only argument. By convention, it’s usually called `e`, which stands for “event”. You can use this object to read information about the event.
That event object also lets you stop the propagation. If you want to prevent an event from reaching parent components, you need to call `e.stopPropagation()` like this `Button` component does:
App.js
App.js
ReloadClear Fork
```
function Button({ onClick, children }) {
  return (
    <button onClick={e => {
      e.stopPropagation();
      onClick();
    }}>
      {children}
    </button>
  );
}

export default function Toolbar() {
  return (
    <div className="Toolbar" onClick={() => {
      alert('You clicked on the toolbar!');
    }}>
      <Button onClick={() => alert('Playing!')}>
        Play Movie
      </Button>
      <Button onClick={() => alert('Uploading!')}>
        Upload Image
      </Button>
    </div>
  );
}


```

When you click on a button:
  1. React calls the `onClick` handler passed to `<button>`.
  2. That handler, defined in `Button`, does the following:
     * Calls `e.stopPropagation()`, preventing the event from bubbling further.
     * Calls the `onClick` function, which is a prop passed from the `Toolbar` component.
  3. That function, defined in the `Toolbar` component, displays the button’s own alert.
  4. Since the propagation was stopped, the parent `<div>`’s `onClick` handler does _not_ run.


As a result of `e.stopPropagation()`, clicking on the buttons now only shows a single alert (from the `<button>`) rather than the two of them (from the `<button>` and the parent toolbar `<div>`). Clicking a button is not the same thing as clicking the surrounding toolbar, so stopping the propagation makes sense for this UI.
#### Capture phase events [](https://react.dev/learn/responding-to-events#capture-phase-events "Link for Capture phase events ")
In rare cases, you might need to catch all events on child elements, _even if they stopped propagation_. For example, maybe you want to log every click to analytics, regardless of the propagation logic. You can do this by adding `Capture` at the end of the event name:
```


<div onClickCapture={() => { /* this runs first */ }}>




  <button onClick={e => e.stopPropagation()} />




  <button onClick={e => e.stopPropagation()} />





</div>


```

Each event propagates in three phases:
  1. It travels down, calling all `onClickCapture` handlers.
  2. It runs the clicked element’s `onClick` handler.
  3. It travels upwards, calling all `onClick` handlers.


Capture events are useful for code like routers or analytics, but you probably won’t use them in app code.
### Passing handlers as alternative to propagation [](https://react.dev/learn/responding-to-events#passing-handlers-as-alternative-to-propagation "Link for Passing handlers as alternative to propagation ")
Notice how this click handler runs a line of code _and then_ calls the `onClick` prop passed by the parent:
```


function Button({ onClick, children }) {




  return (




    <button onClick={e => {




      e.stopPropagation();




      onClick();




    }}>




      {children}




    </button>




  );




}

```

You could add more code to this handler before calling the parent `onClick` event handler, too. This pattern provides an _alternative_ to propagation. It lets the child component handle the event, while also letting the parent component specify some additional behavior. Unlike propagation, it’s not automatic. But the benefit of this pattern is that you can clearly follow the whole chain of code that executes as a result of some event.
If you rely on propagation and it’s difficult to trace which handlers execute and why, try this approach instead.
### Preventing default behavior [](https://react.dev/learn/responding-to-events#preventing-default-behavior "Link for Preventing default behavior ")
Some browser events have default behavior associated with them. For example, a `<form>` submit event, which happens when a button inside of it is clicked, will reload the whole page by default:
App.js
App.js
ReloadClear Fork
```
export default function Signup() {
  return (
    <form onSubmit={() => alert('Submitting!')}>
      <input />
      <button>Send</button>
    </form>
  );
}


```

You can call `e.preventDefault()` on the event object to stop this from happening:
App.js
App.js
ReloadClear Fork
```
export default function Signup() {
  return (
    <form onSubmit={e => {
      e.preventDefault();
      alert('Submitting!');
    }}>
      <input />
      <button>Send</button>
    </form>
  );
}


```

Don’t confuse `e.stopPropagation()` and `e.preventDefault()`. They are both useful, but are unrelated:
## Can event handlers have side effects? [](https://react.dev/learn/responding-to-events#can-event-handlers-have-side-effects "Link for Can event handlers have side effects? ")
Absolutely! Event handlers are the best place for side effects.
Unlike rendering functions, event handlers don’t need to be [pure](https://react.dev/learn/keeping-components-pure), so it’s a great place to _change_ something—for example, change an input’s value in response to typing, or change a list in response to a button press. However, in order to change some information, you first need some way to store it. In React, this is done by using [state, a component’s memory.](https://react.dev/learn/state-a-components-memory) You will learn all about it on the next page.
## Recap[](https://react.dev/learn/responding-to-events#recap "Link for Recap")
  * You can handle events by passing a function as a prop to an element like `<button>`.
  * Event handlers must be passed, **not called!** `onClick={handleClick}`, not `onClick={handleClick()}`.
  * You can define an event handler function separately or inline.
  * Event handlers are defined inside a component, so they can access props.
  * You can declare an event handler in a parent and pass it as a prop to a child.
  * You can define your own event handler props with application-specific names.
  * Events propagate upwards. Call `e.stopPropagation()` on the first argument to prevent that.
  * Events may have unwanted default browser behavior. Call `e.preventDefault()` to prevent that.
  * Explicitly calling an event handler prop from a child handler is a good alternative to propagation.


## Try out some challenges[](https://react.dev/learn/responding-to-events#challenges "Link for Try out some challenges")
1. Fix an event handler 2. Wire up the events
####
Challenge 1 of 2:
Fix an event handler [](https://react.dev/learn/responding-to-events#fix-an-event-handler "Link for this heading")
Clicking this button is supposed to switch the page background between white and black. However, nothing happens when you click it. Fix the problem. (Don’t worry about the logic inside `handleClick`—that part is fine.)
App.js
App.js
ReloadClear Fork
```
export default function LightSwitch() {
  function handleClick() {
    let bodyStyle = document.body.style;
    if (bodyStyle.backgroundColor === 'black') {
      bodyStyle.backgroundColor = 'white';
    } else {
      bodyStyle.backgroundColor = 'black';
    }
  }

  return (
    <button onClick={handleClick()}>
      Toggle the lights
    </button>
  );
}


```

Show solutionNext Challenge
[ PreviousAdding Interactivity ](https://react.dev/learn/adding-interactivity)[ NextState: A Component's Memory ](https://react.dev/learn/state-a-components-memory)
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
  * [Overview](https://react.dev/learn/responding-to-events)
  * [Adding event handlers ](https://react.dev/learn/responding-to-events#adding-event-handlers)
  * [Reading props in event handlers ](https://react.dev/learn/responding-to-events#reading-props-in-event-handlers)
  * [Passing event handlers as props ](https://react.dev/learn/responding-to-events#passing-event-handlers-as-props)
  * [Naming event handler props ](https://react.dev/learn/responding-to-events#naming-event-handler-props)
  * [Event propagation ](https://react.dev/learn/responding-to-events#event-propagation)
  * [Stopping propagation ](https://react.dev/learn/responding-to-events#stopping-propagation)
  * [Passing handlers as alternative to propagation ](https://react.dev/learn/responding-to-events#passing-handlers-as-alternative-to-propagation)
  * [Preventing default behavior ](https://react.dev/learn/responding-to-events#preventing-default-behavior)
  * [Can event handlers have side effects? ](https://react.dev/learn/responding-to-events#can-event-handlers-have-side-effects)
  * [Recap](https://react.dev/learn/responding-to-events#recap)
  * [Challenges](https://react.dev/learn/responding-to-events#challenges)
