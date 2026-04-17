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
# Writing Markup with JSX[](https://react.dev/learn/writing-markup-with-jsx#undefined "Link for this heading")
_JSX_ is a syntax extension for JavaScript that lets you write HTML-like markup inside a JavaScript file. Although there are other ways to write components, most React developers prefer the conciseness of JSX, and most codebases use it.
### You will learn
  * Why React mixes markup with rendering logic
  * How JSX is different from HTML
  * How to display information with JSX


## JSX: Putting markup into JavaScript [](https://react.dev/learn/writing-markup-with-jsx#jsx-putting-markup-into-javascript "Link for JSX: Putting markup into JavaScript ")
The Web has been built on HTML, CSS, and JavaScript. For many years, web developers kept content in HTML, design in CSS, and logic in JavaScript—often in separate files! Content was marked up inside HTML while the page’s logic lived separately in JavaScript:
![HTML markup with purple background and a div with two child tags: p and form. ](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fwriting_jsx_html.dark.png&w=750&q=75)
![HTML markup with purple background and a div with two child tags: p and form. ](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fwriting_jsx_html.png&w=750&q=75)
HTML
![Three JavaScript handlers with yellow background: onSubmit, onLogin, and onClick.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fwriting_jsx_js.dark.png&w=750&q=75)
![Three JavaScript handlers with yellow background: onSubmit, onLogin, and onClick.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fwriting_jsx_js.png&w=750&q=75)
JavaScript
But as the Web became more interactive, logic increasingly determined content. JavaScript was in charge of the HTML! This is why **in React, rendering logic and markup live together in the same place—components.**
![React component with HTML and JavaScript from previous examples mixed. Function name is Sidebar which calls the function isLoggedIn, highlighted in yellow. Nested inside the function highlighted in purple is the p tag from before, and a Form tag referencing the component shown in the next diagram.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fwriting_jsx_sidebar.dark.png&w=750&q=75)
![React component with HTML and JavaScript from previous examples mixed. Function name is Sidebar which calls the function isLoggedIn, highlighted in yellow. Nested inside the function highlighted in purple is the p tag from before, and a Form tag referencing the component shown in the next diagram.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fwriting_jsx_sidebar.png&w=750&q=75)
`Sidebar.js` React component
![React component with HTML and JavaScript from previous examples mixed. Function name is Form containing two handlers onClick and onSubmit highlighted in yellow. Following the handlers is HTML highlighted in purple. The HTML contains a form element with a nested input element, each with an onClick prop.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fwriting_jsx_form.dark.png&w=750&q=75)
![React component with HTML and JavaScript from previous examples mixed. Function name is Form containing two handlers onClick and onSubmit highlighted in yellow. Following the handlers is HTML highlighted in purple. The HTML contains a form element with a nested input element, each with an onClick prop.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fwriting_jsx_form.png&w=750&q=75)
`Form.js` React component
Keeping a button’s rendering logic and markup together ensures that they stay in sync with each other on every edit. Conversely, details that are unrelated, such as the button’s markup and a sidebar’s markup, are isolated from each other, making it safer to change either of them on their own.
Each React component is a JavaScript function that may contain some markup that React renders into the browser. React components use a syntax extension called JSX to represent that markup. JSX looks a lot like HTML, but it is a bit stricter and can display dynamic information. The best way to understand this is to convert some HTML markup to JSX markup.
JSX and React are two separate things. They’re often used together, but you _can_
## Converting HTML to JSX [](https://react.dev/learn/writing-markup-with-jsx#converting-html-to-jsx "Link for Converting HTML to JSX ")
Suppose that you have some (perfectly valid) HTML:
```


<h1>Hedy Lamarr's Todos</h1>





<img




  src="https://i.imgur.com/yXOvdOSs.jpg"




  alt="Hedy Lamarr"




  class="photo"





>





<ul>




    <li>Invent new traffic lights




    <li>Rehearse a movie scene




    <li>Improve the spectrum technology





</ul>


```

And you want to put it into your component:
```


export default function TodoList() {




  return (




    // ???




  )




}

```

If you copy and paste it as is, it will not work:
App.js
App.js
ReloadClear Fork
```
export default function TodoList() {
  return (
    // This doesn't quite work!
    <h1>Hedy Lamarr's Todos</h1>
    <img
      src="https://i.imgur.com/yXOvdOSs.jpg"
      alt="Hedy Lamarr"
      class="photo"
    >
    <ul>
      <li>Invent new traffic lights
      <li>Rehearse a movie scene
      <li>Improve the spectrum technology
    </ul>


```

This is because JSX is stricter and has a few more rules than HTML! If you read the error messages above, they’ll guide you to fix the markup, or you can follow the guide below.
Most of the time, React’s on-screen error messages will help you find where the problem is. Give them a read if you get stuck!
## The Rules of JSX [](https://react.dev/learn/writing-markup-with-jsx#the-rules-of-jsx "Link for The Rules of JSX ")
### 1. Return a single root element [](https://react.dev/learn/writing-markup-with-jsx#1-return-a-single-root-element "Link for 1. Return a single root element ")
To return multiple elements from a component, **wrap them with a single parent tag.**
For example, you can use a `<div>`:
```


<div>




  <h1>Hedy Lamarr's Todos</h1>




  <img




    src="https://i.imgur.com/yXOvdOSs.jpg"




    alt="Hedy Lamarr"




    class="photo"




  >




  <ul>




    ...




  </ul>





</div>


```

If you don’t want to add an extra `<div>` to your markup, you can write `<>` and `</>` instead:
```


<>




  <h1>Hedy Lamarr's Todos</h1>




  <img




    src="https://i.imgur.com/yXOvdOSs.jpg"




    alt="Hedy Lamarr"




    class="photo"




  >




  <ul>




    ...




  </ul>





</>


```

This empty tag is called a _[Fragment.](https://react.dev/reference/react/Fragment)_ Fragments let you group things without leaving any trace in the browser HTML tree.
#### Why do multiple JSX tags need to be wrapped? [](https://react.dev/learn/writing-markup-with-jsx#why-do-multiple-jsx-tags-need-to-be-wrapped "Link for Why do multiple JSX tags need to be wrapped? ")
JSX looks like HTML, but under the hood it is transformed into plain JavaScript objects. You can’t return two objects from a function without wrapping them into an array. This explains why you also can’t return two JSX tags without wrapping them into another tag or a Fragment.
### 2. Close all the tags [](https://react.dev/learn/writing-markup-with-jsx#2-close-all-the-tags "Link for 2. Close all the tags ")
JSX requires tags to be explicitly closed: self-closing tags like `<img>` must become `<img />`, and wrapping tags like `<li>oranges` must be written as `<li>oranges</li>`.
This is how Hedy Lamarr’s image and list items look closed:
```


<>




  <img




    src="https://i.imgur.com/yXOvdOSs.jpg"




    alt="Hedy Lamarr"




    class="photo"




   />




  <ul>




    <li>Invent new traffic lights</li>




    <li>Rehearse a movie scene</li>




    <li>Improve the spectrum technology</li>




  </ul>





</>


```

### 3. camelCase ~~all~~ most of the things! [](https://react.dev/learn/writing-markup-with-jsx#3-camelcase-salls-most-of-the-things "Link for this heading")
JSX turns into JavaScript and attributes written in JSX become keys of JavaScript objects. In your own components, you will often want to read those attributes into variables. But JavaScript has limitations on variable names. For example, their names can’t contain dashes or be reserved words like `class`.
This is why, in React, many HTML and SVG attributes are written in camelCase. For example, instead of `stroke-width` you use `strokeWidth`. Since `class` is a reserved word, in React you write `className` instead, named after the
```


<img




  src="https://i.imgur.com/yXOvdOSs.jpg"




  alt="Hedy Lamarr"




  className="photo"




/>

```

You can [find all these attributes in the list of DOM component props.](https://react.dev/reference/react-dom/components/common) If you get one wrong, don’t worry—React will print a message with a possible correction to the
For historical reasons,
### Pro-tip: Use a JSX Converter [](https://react.dev/learn/writing-markup-with-jsx#pro-tip-use-a-jsx-converter "Link for Pro-tip: Use a JSX Converter ")
Converting all these attributes in existing markup can be tedious! We recommend using a
Here is your final result:
App.js
App.js
ReloadClear Fork
```
export default function TodoList() {
  return (
    <>
      <h1>Hedy Lamarr's Todos</h1>
      <img
        src="https://i.imgur.com/yXOvdOSs.jpg"
        alt="Hedy Lamarr"
        className="photo"
      />
      <ul>
        <li>Invent new traffic lights</li>
        <li>Rehearse a movie scene</li>
        <li>Improve the spectrum technology</li>
      </ul>
    </>
  );
}


```

## Recap[](https://react.dev/learn/writing-markup-with-jsx#recap "Link for Recap")
Now you know why JSX exists and how to use it in components:
  * React components group rendering logic together with markup because they are related.
  * JSX is similar to HTML, with a few differences. You can use a
  * Error messages will often point you in the right direction to fixing your markup.


## Try out some challenges[](https://react.dev/learn/writing-markup-with-jsx#challenges "Link for Try out some challenges")
####
Challenge 1 of 1:
Convert some HTML to JSX [](https://react.dev/learn/writing-markup-with-jsx#convert-some-html-to-jsx "Link for this heading")
This HTML was pasted into a component, but it’s not valid JSX. Fix it:
App.js
App.js
ReloadClear Fork
```
export default function Bio() {
  return (
    <div class="intro">
      <h1>Welcome to my website!</h1>
    </div>
    <p class="summary">
      You can find my thoughts here.
      <br><br>
      <b>And <i>pictures</b></i> of scientists!
    </p>
  );
}


```

Whether to do it by hand or using the converter is up to you!
[ PreviousImporting and Exporting Components ](https://react.dev/learn/importing-and-exporting-components)[ NextJavaScript in JSX with Curly Braces ](https://react.dev/learn/javascript-in-jsx-with-curly-braces)
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
  * [Overview](https://react.dev/learn/writing-markup-with-jsx)
  * [JSX: Putting markup into JavaScript ](https://react.dev/learn/writing-markup-with-jsx#jsx-putting-markup-into-javascript)
  * [Converting HTML to JSX ](https://react.dev/learn/writing-markup-with-jsx#converting-html-to-jsx)
  * [The Rules of JSX ](https://react.dev/learn/writing-markup-with-jsx#the-rules-of-jsx)
  * [1. Return a single root element ](https://react.dev/learn/writing-markup-with-jsx#1-return-a-single-root-element)
  * [2. Close all the tags ](https://react.dev/learn/writing-markup-with-jsx#2-close-all-the-tags)
  * [3. camelCase ~~all~~ most of the things! ](https://react.dev/learn/writing-markup-with-jsx#3-camelcase-salls-most-of-the-things)
  * [Pro-tip: Use a JSX Converter ](https://react.dev/learn/writing-markup-with-jsx#pro-tip-use-a-jsx-converter)
  * [Recap](https://react.dev/learn/writing-markup-with-jsx#recap)
  * [Challenges](https://react.dev/learn/writing-markup-with-jsx#challenges)


Writing Markup with JSX – React
