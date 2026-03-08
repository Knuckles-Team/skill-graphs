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
[Describing the UI](https://react.dev/learn/describing-the-ui)
Copy pageCopy
# Importing and Exporting Components[](https://react.dev/learn/importing-and-exporting-components#undefined "Link for this heading")
The magic of components lies in their reusability: you can create components that are composed of other components. But as you nest more and more components, it often makes sense to start splitting them into different files. This lets you keep your files easy to scan and reuse components in more places.
### You will learn
  * What a root component file is
  * How to import and export a component
  * When to use default and named imports and exports
  * How to import and export multiple components from one file
  * How to split components into multiple files


## The root component file [](https://react.dev/learn/importing-and-exporting-components#the-root-component-file "Link for The root component file ")
In [Your First Component](https://react.dev/learn/your-first-component), you made a `Profile` component and a `Gallery` component that renders it:
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
function Profile() {
return (
<img
src="https://i.imgur.com/MK3eW3As.jpg"
alt="Katherine Johnson"
/>
);
}


export default function Gallery() {
return (
<section>
<h1>Amazing scientists</h1>
<Profile />
<Profile />
<Profile />
</section>
);
}


These currently live in a **root component file,** named `App.js` in this example. Depending on your setup, your root component could be in another file, though. If you use a framework with file-based routing, such as Next.js, your root component will be different for every page.
## Exporting and importing a component [](https://react.dev/learn/importing-and-exporting-components#exporting-and-importing-a-component "Link for Exporting and importing a component ")
What if you want to change the landing screen in the future and put a list of science books there? Or place all the profiles somewhere else? It makes sense to move `Gallery` and `Profile` out of the root component file. This will make them more modular and reusable in other files. You can move a component in three steps:
  1. **Make** a new JS file to put the components in.
  2. **Export** your function component from that file (using either
  3. **Import** it in the file where you’ll use the component (using the corresponding technique for importing


Here both `Profile` and `Gallery` have been moved out of `App.js` into a new file called `Gallery.js`. Now you can change `App.js` to import `Gallery` from `Gallery.js`:
App.jsGallery.js
App.js
ReloadClear Fork
```
import Gallery from './Gallery.js';

export default function App() {
  return (
    <Gallery />
  );
}


```

Notice how this example is broken down into two component files now:
  1. `Gallery.js`:
     * Defines the `Profile` component which is only used within the same file and is not exported.
     * Exports the `Gallery` component as a **default export.**
  2. `App.js`:
     * Imports `Gallery` as a **default import** from `Gallery.js`.
     * Exports the root `App` component as a **default export.**


You may encounter files that leave off the `.js` file extension like so:
```


import Gallery from './Gallery';


```

Either `'./Gallery.js'` or `'./Gallery'` will work with React, though the former is closer to how
#### Default vs named exports [](https://react.dev/learn/importing-and-exporting-components#default-vs-named-exports "Link for Default vs named exports ")
There are two primary ways to export values with JavaScript: default exports and named exports. So far, our examples have only used default exports. But you can use one or both of them in the same file. **A file can have no more than one _default_ export, but it can have as many _named_ exports as you like.**
![Default and named exports](https://react.dev/images/docs/illustrations/i_import-export.svg)
How you export your component dictates how you must import it. You will get an error if you try to import a default export the same way you would a named export! This chart can help you keep track:
Syntax | Export statement | Import statement
---|---|---
Default | `export default function Button() {}` | `import Button from './Button.js';`
Named | `export function Button() {}` | `import { Button } from './Button.js';`
When you write a _default_ import, you can put any name you want after `import`. For example, you could write `import Banana from './Button.js'` instead and it would still provide you with the same default export. In contrast, with named imports, the name has to match on both sides. That’s why they are called _named_ imports!
**People often use default exports if the file exports only one component, and use named exports if it exports multiple components and values.** Regardless of which coding style you prefer, always give meaningful names to your component functions and the files that contain them. Components without names, like `export default () => {}`, are discouraged because they make debugging harder.
## Exporting and importing multiple components from the same file [](https://react.dev/learn/importing-and-exporting-components#exporting-and-importing-multiple-components-from-the-same-file "Link for Exporting and importing multiple components from the same file ")
What if you want to show just one `Profile` instead of a gallery? You can export the `Profile` component, too. But `Gallery.js` already has a _default_ export, and you can’t have _two_ default exports. You could create a new file with a default export, or you could add a _named_ export for `Profile`. **A file can only have one default export, but it can have numerous named exports!**
To reduce the potential confusion between default and named exports, some teams choose to only stick to one style (default or named), or avoid mixing them in a single file. Do what works best for you!
First, **export** `Profile` from `Gallery.js` using a named export (no `default` keyword):
```


export function Profile() {




  // ...




}

```

Then, **import** `Profile` from `Gallery.js` to `App.js` using a named import (with the curly braces):
```


import { Profile } from './Gallery.js';


```

Finally, **render** `<Profile />` from the `App` component:
```


export default function App() {




  return <Profile />;




}

```

Now `Gallery.js` contains two exports: a default `Gallery` export, and a named `Profile` export. `App.js` imports both of them. Try editing `<Profile />` to `<Gallery />` and back in this example:
App.jsGallery.js
App.js
ReloadClear Fork
```
import Gallery from './Gallery.js';
import { Profile } from './Gallery.js';

export default function App() {
  return (
    <Profile />
  );
}


```

Now you’re using a mix of default and named exports:
  * `Gallery.js`:
    * Exports the `Profile` component as a **named export called`Profile`.**
    * Exports the `Gallery` component as a **default export.**
  * `App.js`:
    * Imports `Profile` as a **named import called`Profile`** from `Gallery.js`.
    * Imports `Gallery` as a **default import** from `Gallery.js`.
    * Exports the root `App` component as a **default export.**


## Recap[](https://react.dev/learn/importing-and-exporting-components#recap "Link for Recap")
On this page you learned:
  * What a root component file is
  * How to import and export a component
  * When and how to use default and named imports and exports
  * How to export multiple components from the same file


## Try out some challenges[](https://react.dev/learn/importing-and-exporting-components#challenges "Link for Try out some challenges")
####
Challenge 1 of 1:
Split the components further [](https://react.dev/learn/importing-and-exporting-components#split-the-components-further "Link for this heading")
Currently, `Gallery.js` exports both `Profile` and `Gallery`, which is a bit confusing.
Move the `Profile` component to its own `Profile.js`, and then change the `App` component to render both `<Profile />` and `<Gallery />` one after another.
You may use either a default or a named export for `Profile`, but make sure that you use the corresponding import syntax in both `App.js` and `Gallery.js`! You can refer to the table from the deep dive above:
Syntax | Export statement | Import statement
---|---|---
Default | `export default function Button() {}` | `import Button from './Button.js';`
Named | `export function Button() {}` | `import { Button } from './Button.js';`
App.jsGallery.jsProfile.js
Gallery.js
ReloadClear Fork
```
// Move me to Profile.js!
export function Profile() {
  return (
    <img
      src="https://i.imgur.com/QIrZWGIs.jpg"
      alt="Alan L. Hart"
    />
  );
}

export default function Gallery() {
  return (
    <section>
      <h1>Amazing scientists</h1>
      <Profile />
      <Profile />
      <Profile />
    </section>
  );
}


```

After you get it working with one kind of exports, make it work with the other kind.
Show hintShow solution
[ PreviousYour First Component ](https://react.dev/learn/your-first-component)[ NextWriting Markup with JSX ](https://react.dev/learn/writing-markup-with-jsx)
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
  * [Overview](https://react.dev/learn/importing-and-exporting-components)
  * [The root component file ](https://react.dev/learn/importing-and-exporting-components#the-root-component-file)
  * [Exporting and importing a component ](https://react.dev/learn/importing-and-exporting-components#exporting-and-importing-a-component)
  * [Exporting and importing multiple components from the same file ](https://react.dev/learn/importing-and-exporting-components#exporting-and-importing-multiple-components-from-the-same-file)
  * [Recap](https://react.dev/learn/importing-and-exporting-components#recap)
  * [Challenges](https://react.dev/learn/importing-and-exporting-components#challenges)
