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
# Render and Commit[](https://react.dev/learn/render-and-commit#undefined "Link for this heading")
Before your components are displayed on screen, they must be rendered by React. Understanding the steps in this process will help you think about how your code executes and explain its behavior.
### You will learn
  * What rendering means in React
  * When and why React renders a component
  * The steps involved in displaying a component on screen
  * Why rendering does not always produce a DOM update


Imagine that your components are cooks in the kitchen, assembling tasty dishes from ingredients. In this scenario, React is the waiter who puts in requests from customers and brings them their orders. This process of requesting and serving UI has three steps:
  1. **Triggering** a render (delivering the guest’s order to the kitchen)
  2. **Rendering** the component (preparing the order in the kitchen)
  3. **Committing** to the DOM (placing the order on the table)


  1. ![React as a server in a restaurant, fetching orders from the users and delivering them to the Component Kitchen.](https://react.dev/images/docs/illustrations/i_render-and-commit1.png)
Trigger
  2. ![The Card Chef gives React a fresh Card component.](https://react.dev/images/docs/illustrations/i_render-and-commit2.png)
Render
  3. ![React delivers the Card to the user at their table.](https://react.dev/images/docs/illustrations/i_render-and-commit3.png)
Commit


Illustrated by
## Step 1: Trigger a render [](https://react.dev/learn/render-and-commit#step-1-trigger-a-render "Link for Step 1: Trigger a render ")
There are two reasons for a component to render:
  1. It’s the component’s **initial render.**
  2. The component’s (or one of its ancestors’) **state has been updated.**


### Initial render [](https://react.dev/learn/render-and-commit#initial-render "Link for Initial render ")
When your app starts, you need to trigger the initial render. Frameworks and sandboxes sometimes hide this code, but it’s done by calling [`createRoot`](https://react.dev/reference/react-dom/client/createRoot) with the target DOM node, and then calling its `render` method with your component:
index.jsImage.js
index.js
ReloadClear
9
1
2
3
4
5
6
import Image from './Image.js';
import { createRoot } from 'react-dom/client';


const root = createRoot(document.getElementById('root'))
root.render(<Image />);


Try commenting out the `root.render()` call and see the component disappear!
### Re-renders when state updates [](https://react.dev/learn/render-and-commit#re-renders-when-state-updates "Link for Re-renders when state updates ")
Once the component has been initially rendered, you can trigger further renders by updating its state with the [`set` function.](https://react.dev/reference/react/useState#setstate) Updating your component’s state automatically queues a render. (You can imagine these as a restaurant guest ordering tea, dessert, and all sorts of things after putting in their first order, depending on the state of their thirst or hunger.)
  1. ![React as a server in a restaurant, serving a Card UI to the user, represented as a patron with a cursor for their head. The patron expresses they want a pink card, not a black one!](https://react.dev/images/docs/illustrations/i_rerender1.png)
State update...
  2. ![React returns to the Component Kitchen and tells the Card Chef they need a pink Card.](https://react.dev/images/docs/illustrations/i_rerender2.png)
...triggers...
  3. ![The Card Chef gives React the pink Card.](https://react.dev/images/docs/illustrations/i_rerender3.png)
...render!


Illustrated by
## Step 2: React renders your components [](https://react.dev/learn/render-and-commit#step-2-react-renders-your-components "Link for Step 2: React renders your components ")
After you trigger a render, React calls your components to figure out what to display on screen. **“Rendering” is React calling your components.**
  * **On initial render,** React will call the root component.
  * **For subsequent renders,** React will call the function component whose state update triggered the render.


This process is recursive: if the updated component returns some other component, React will render _that_ component next, and if that component also returns something, it will render _that_ component next, and so on. The process will continue until there are no more nested components and React knows exactly what should be displayed on screen.
In the following example, React will call `Gallery()` and `Image()` several times:
index.jsGallery.js
Gallery.js
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
export default function Gallery() {
return (
<section>
<h1>Inspiring Sculptures</h1>
<Image />
<Image />
<Image />
</section>
);
}


function Image() {
return (
<img
src="https://i.imgur.com/ZF6s192.jpg"
alt="'Floralis Genérica' by Eduardo Catalano: a gigantic metallic flower sculpture with reflective petals"
/>
);
}


  * **During the initial render,** React will `<section>`, `<h1>`, and three `<img>` tags.
  * **During a re-render,** React will calculate which of their properties, if any, have changed since the previous render. It won’t do anything with that information until the next step, the commit phase.


Rendering must always be a [pure calculation](https://react.dev/learn/keeping-components-pure):
  * **Same inputs, same output.** Given the same inputs, a component should always return the same JSX. (When someone orders a salad with tomatoes, they should not receive a salad with onions!)
  * **It minds its own business.** It should not change any objects or variables that existed before rendering. (One order should not change anyone else’s order.)


Otherwise, you can encounter confusing bugs and unpredictable behavior as your codebase grows in complexity. When developing in “Strict Mode”, React calls each component’s function twice, which can help surface mistakes caused by impure functions.
#### Optimizing performance [](https://react.dev/learn/render-and-commit#optimizing-performance "Link for Optimizing performance ")
The default behavior of rendering all components nested within the updated component is not optimal for performance if the updated component is very high in the tree. If you run into a performance issue, there are several opt-in ways to solve it described in the **Don’t optimize prematurely!**
## Step 3: React commits changes to the DOM [](https://react.dev/learn/render-and-commit#step-3-react-commits-changes-to-the-dom "Link for Step 3: React commits changes to the DOM ")
After rendering (calling) your components, React will modify the DOM.
  * **For the initial render,** React will use the
  * **For re-renders,** React will apply the minimal necessary operations (calculated while rendering!) to make the DOM match the latest rendering output.


**React only changes the DOM nodes if there’s a difference between renders.** For example, here is a component that re-renders with different props passed from its parent every second. Notice how you can add some text into the `<input>`, updating its `value`, but the text doesn’t disappear when the component re-renders:
Clock.js
Clock.js
ReloadClear Fork
```
export default function Clock({ time }) {
  return (
    <>
      <h1>{time}</h1>
      <input />
    </>
  );
}


```

This works because during this last step, React only updates the content of `<h1>` with the new `time`. It sees that the `<input>` appears in the JSX in the same place as last time, so React doesn’t touch the `<input>`—or its `value`!
## Epilogue: Browser paint [](https://react.dev/learn/render-and-commit#epilogue-browser-paint "Link for Epilogue: Browser paint ")
After rendering is done and React updated the DOM, the browser will repaint the screen. Although this process is known as “browser rendering”, we’ll refer to it as “painting” to avoid confusion throughout the docs.
![A browser painting 'still life with card element'.](https://react.dev/images/docs/illustrations/i_browser-paint.png)
Illustrated by
## Recap[](https://react.dev/learn/render-and-commit#recap "Link for Recap")
  * Any screen update in a React app happens in three steps:
    1. Trigger
    2. Render
    3. Commit
  * You can use Strict Mode to find mistakes in your components
  * React does not touch the DOM if the rendering result is the same as last time


[ PreviousState: A Component's Memory ](https://react.dev/learn/state-a-components-memory)[ NextState as a Snapshot ](https://react.dev/learn/state-as-a-snapshot)
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
  * [Overview](https://react.dev/learn/render-and-commit)
  * [Step 1: Trigger a render ](https://react.dev/learn/render-and-commit#step-1-trigger-a-render)
  * [Initial render ](https://react.dev/learn/render-and-commit#initial-render)
  * [Re-renders when state updates ](https://react.dev/learn/render-and-commit#re-renders-when-state-updates)
  * [Step 2: React renders your components ](https://react.dev/learn/render-and-commit#step-2-react-renders-your-components)
  * [Step 3: React commits changes to the DOM ](https://react.dev/learn/render-and-commit#step-3-react-commits-changes-to-the-dom)
  * [Epilogue: Browser paint ](https://react.dev/learn/render-and-commit#epilogue-browser-paint)
  * [Recap](https://react.dev/learn/render-and-commit#recap)
