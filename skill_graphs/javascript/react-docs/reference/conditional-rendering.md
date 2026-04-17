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
# Your First Component[](https://react.dev/learn/your-first-component#undefined "Link for this heading")
_Components_ are one of the core concepts of React. They are the foundation upon which you build user interfaces (UI), which makes them the perfect place to start your React journey!
### You will learn
  * What a component is
  * What role components play in a React application
  * How to write your first React component


## Components: UI building blocks [](https://react.dev/learn/your-first-component#components-ui-building-blocks "Link for Components: UI building blocks ")
On the Web, HTML lets us create rich structured documents with its built-in set of tags like `<h1>` and `<li>`:
```


<article>




  <h1>My First Component</h1>




  <ol>




    <li>Components: UI Building Blocks</li>




    <li>Defining a Component</li>




    <li>Using a Component</li>




  </ol>





</article>


```

This markup represents this article `<article>`, its heading `<h1>`, and an (abbreviated) table of contents as an ordered list `<ol>`. Markup like this, combined with CSS for style, and JavaScript for interactivity, lies behind every sidebar, avatar, modal, dropdown—every piece of UI you see on the Web.
React lets you combine your markup, CSS, and JavaScript into custom “components”, **reusable UI elements for your app.** The table of contents code you saw above could be turned into a `<TableOfContents />` component you could render on every page. Under the hood, it still uses the same HTML tags like `<article>`, `<h1>`, etc.
Just like with HTML tags, you can compose, order and nest components to design whole pages. For example, the documentation page you’re reading is made out of React components:
```


<PageLayout>




  <NavigationHeader>




    <SearchBar />




    <Link to="/docs">Docs</Link>




  </NavigationHeader>




  <Sidebar />




  <PageContent>




    <TableOfContents />




    <DocumentationText />




  </PageContent>





</PageLayout>


```

As your project grows, you will notice that many of your designs can be composed by reusing components you already wrote, speeding up your development. Our table of contents above could be added to any screen with `<TableOfContents />`! You can even jumpstart your project with the thousands of components shared by the React open source community like
## Defining a component [](https://react.dev/learn/your-first-component#defining-a-component "Link for Defining a component ")
Traditionally when creating web pages, web developers marked up their content and then added interaction by sprinkling on some JavaScript. This worked great when interaction was a nice-to-have on the web. Now it is expected for many sites and all apps. React puts interactivity first while still using the same technology: **a React component is a JavaScript function that you can _sprinkle with markup_.** Here’s what that looks like (you can edit the example below):
App.js
App.js
ReloadClear Fork
```
export default function Profile() {
  return (
    <img
      src="https://i.imgur.com/MK3eW3Am.jpg"
      alt="Katherine Johnson"
    />
  )
}


```

And here’s how to build a component:
### Step 1: Export the component [](https://react.dev/learn/your-first-component#step-1-export-the-component "Link for Step 1: Export the component ")
The `export default` prefix is a [Importing and Exporting Components](https://react.dev/learn/importing-and-exporting-components)!)
### Step 2: Define the function [](https://react.dev/learn/your-first-component#step-2-define-the-function "Link for Step 2: Define the function ")
With `function Profile() { }` you define a JavaScript function with the name `Profile`.
React components are regular JavaScript functions, but **their names must start with a capital letter** or they won’t work!
### Step 3: Add markup [](https://react.dev/learn/your-first-component#step-3-add-markup "Link for Step 3: Add markup ")
The component returns an `<img />` tag with `src` and `alt` attributes. `<img />` is written like HTML, but it is actually JavaScript under the hood! This syntax is called [JSX](https://react.dev/learn/writing-markup-with-jsx), and it lets you embed markup inside JavaScript.
Return statements can be written all on one line, as in this component:
```


return <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />;


```

But if your markup isn’t all on the same line as the `return` keyword, you must wrap it in a pair of parentheses:
```


return (




  <div>




    <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />




  </div>





);


```

Without parentheses, any code on the lines after `return`
## Using a component [](https://react.dev/learn/your-first-component#using-a-component "Link for Using a component ")
Now that you’ve defined your `Profile` component, you can nest it inside other components. For example, you can export a `Gallery` component that uses multiple `Profile` components:
App.js
App.js
ReloadClear Fork
```
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


```

### What the browser sees [](https://react.dev/learn/your-first-component#what-the-browser-sees "Link for What the browser sees ")
Notice the difference in casing:
  * `<section>` is lowercase, so React knows we refer to an HTML tag.
  * `<Profile />` starts with a capital `P`, so React knows that we want to use our component called `Profile`.


And `Profile` contains even more HTML: `<img />`. In the end, this is what the browser sees:
```


<section>




  <h1>Amazing scientists</h1>




  <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />




  <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />




  <img src="https://i.imgur.com/MK3eW3As.jpg" alt="Katherine Johnson" />





</section>


```

### Nesting and organizing components [](https://react.dev/learn/your-first-component#nesting-and-organizing-components "Link for Nesting and organizing components ")
Components are regular JavaScript functions, so you can keep multiple components in the same file. This is convenient when components are relatively small or tightly related to each other. If this file gets crowded, you can always move `Profile` to a separate file. You will learn how to do this shortly on the [page about imports.](https://react.dev/learn/importing-and-exporting-components)
Because the `Profile` components are rendered inside `Gallery`—even several times!—we can say that `Gallery` is a **parent component,** rendering each `Profile` as a “child”. This is part of the magic of React: you can define a component once, and then use it in as many places and as many times as you like.
Components can render other components, but **you must never nest their definitions:**
```


export default function Gallery() {




  // 🔴 Never define a component inside another component!




  function Profile() {




    // ...




  }




  // ...




}

```

The snippet above is [very slow and causes bugs.](https://react.dev/learn/preserving-and-resetting-state#different-components-at-the-same-position-reset-state) Instead, define every component at the top level:
```


export default function Gallery() {




  // ...





}









// ✅ Declare components at the top level





function Profile() {




  // ...




}

```

When a child component needs some data from a parent, [pass it by props](https://react.dev/learn/passing-props-to-a-component) instead of nesting definitions.
#### Components all the way down [](https://react.dev/learn/your-first-component#components-all-the-way-down "Link for Components all the way down ")
Your React application begins at a “root” component. Usually, it is created automatically when you start a new project. For example, if you use `pages/index.js`. In these examples, you’ve been exporting root components.
Most React apps use components all the way down. This means that you won’t only use components for reusable pieces like buttons, but also for larger pieces like sidebars, lists, and ultimately, complete pages! Components are a handy way to organize UI code and markup, even if some of them are only used once.
[React-based frameworks](https://react.dev/learn/creating-a-react-app) take this a step further. Instead of using an empty HTML file and letting React “take over” managing the page with JavaScript, they _also_ generate the HTML automatically from your React components. This allows your app to show some content before the JavaScript code loads.
Still, many websites only use React to [add interactivity to existing HTML pages.](https://react.dev/learn/add-react-to-an-existing-project#using-react-for-a-part-of-your-existing-page) They have many root components instead of a single one for the entire page. You can use as much—or as little—React as you need.
## Recap[](https://react.dev/learn/your-first-component#recap "Link for Recap")
You’ve just gotten your first taste of React! Let’s recap some key points.
  * React lets you create components, **reusable UI elements for your app.**
  * In a React app, every piece of UI is a component.
  * React components are regular JavaScript functions except:
    1. Their names always begin with a capital letter.
    2. They return JSX markup.


## Try out some challenges[](https://react.dev/learn/your-first-component#challenges "Link for Try out some challenges")
1. Export the component 2. Fix the return statement 3. Spot the mistake 4. Your own component
####
Challenge 1 of 4:
Export the component [](https://react.dev/learn/your-first-component#export-the-component "Link for this heading")
This sandbox doesn’t work because the root component is not exported:
App.js
App.js
ReloadClear
```
function Profile() {
  return (
    <img
      src="https://i.imgur.com/lICfvbD.jpg"
      alt="Aklilu Lemma"
    />
  );
}


```

## Error
```
Element type is invalid: expected a string (for built-in components) or a class/function (for composite components) but got: object. You likely forgot to export your component from the file it's defined in, or you might have mixed up default and named imports.
```

Try to fix it yourself before looking at the solution!
Next Challenge
[ PreviousDescribing the UI ](https://react.dev/learn/describing-the-ui)[ NextImporting and Exporting Components ](https://react.dev/learn/importing-and-exporting-components)
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
  * [Overview](https://react.dev/learn/your-first-component)
  * [Components: UI building blocks ](https://react.dev/learn/your-first-component#components-ui-building-blocks)
  * [Defining a component ](https://react.dev/learn/your-first-component#defining-a-component)
  * [Step 1: Export the component ](https://react.dev/learn/your-first-component#step-1-export-the-component)
  * [Step 2: Define the function ](https://react.dev/learn/your-first-component#step-2-define-the-function)
  * [Step 3: Add markup ](https://react.dev/learn/your-first-component#step-3-add-markup)
  * [Using a component ](https://react.dev/learn/your-first-component#using-a-component)
  * [What the browser sees ](https://react.dev/learn/your-first-component#what-the-browser-sees)
  * [Nesting and organizing components ](https://react.dev/learn/your-first-component#nesting-and-organizing-components)
  * [Recap](https://react.dev/learn/your-first-component#recap)
  * [Challenges](https://react.dev/learn/your-first-component#challenges)


Your First Component – React
