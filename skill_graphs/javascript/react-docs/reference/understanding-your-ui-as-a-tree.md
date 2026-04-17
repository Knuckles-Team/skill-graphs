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
# JavaScript in JSX with Curly Braces[](https://react.dev/learn/javascript-in-jsx-with-curly-braces#undefined "Link for this heading")
JSX lets you write HTML-like markup inside a JavaScript file, keeping rendering logic and content in the same place. Sometimes you will want to add a little JavaScript logic or reference a dynamic property inside that markup. In this situation, you can use curly braces in your JSX to open a window to JavaScript.
### You will learn
  * How to pass strings with quotes
  * How to reference a JavaScript variable inside JSX with curly braces
  * How to call a JavaScript function inside JSX with curly braces
  * How to use a JavaScript object inside JSX with curly braces


## Passing strings with quotes [](https://react.dev/learn/javascript-in-jsx-with-curly-braces#passing-strings-with-quotes "Link for Passing strings with quotes ")
When you want to pass a string attribute to JSX, you put it in single or double quotes:
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
export default function Avatar() {
return (
<img
className="avatar"
src="https://i.imgur.com/7vQD0fPs.jpg"
alt="Gregorio Y. Zara"
/>
);
}


Here, `"https://i.imgur.com/7vQD0fPs.jpg"` and `"Gregorio Y. Zara"` are being passed as strings.
But what if you want to dynamically specify the `src` or `alt` text? You could **use a value from JavaScript by replacing`"` and `"` with `{` and `}`**:
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
export default function Avatar() {
const avatar = 'https://i.imgur.com/7vQD0fPs.jpg';
const description = 'Gregorio Y. Zara';
return (
<img
className="avatar"
src={avatar}
alt={description}
/>
);
}


Notice the difference between `className="avatar"`, which specifies an `"avatar"` CSS class name that makes the image round, and `src={avatar}` that reads the value of the JavaScript variable called `avatar`. That’s because curly braces let you work with JavaScript right there in your markup!
## Using curly braces: A window into the JavaScript world [](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-curly-braces-a-window-into-the-javascript-world "Link for Using curly braces: A window into the JavaScript world ")
JSX is a special way of writing JavaScript. That means it’s possible to use JavaScript inside it—with curly braces `{ }`. The example below first declares a name for the scientist, `name`, then embeds it with curly braces inside the `<h1>`:
App.js
App.js
ReloadClear
```
export default function TodoList() {
  const name = 'Gregorio Y. Zara';
  return (
    <h1>{name}'s To Do List</h1>
  );
}


```

Try changing the `name`’s value from `'Gregorio Y. Zara'` to `'Hedy Lamarr'`. See how the list title changes?
Any JavaScript expression will work between curly braces, including function calls like `formatDate()`:
App.js
App.js
ReloadClear Fork
```
const today = new Date();

function formatDate(date) {
  return new Intl.DateTimeFormat(
    'en-US',
    { weekday: 'long' }
  ).format(date);
}

export default function TodoList() {
  return (
    <h1>To Do List for {formatDate(today)}</h1>
  );
}


```

### Where to use curly braces [](https://react.dev/learn/javascript-in-jsx-with-curly-braces#where-to-use-curly-braces "Link for Where to use curly braces ")
You can only use curly braces in two ways inside JSX:
  1. **As text** directly inside a JSX tag: `<h1>{name}'s To Do List</h1>` works, but `<{tag}>Gregorio Y. Zara's To Do List</{tag}>` will not.
  2. **As attributes** immediately following the `=` sign: `src={avatar}` will read the `avatar` variable, but `src="{avatar}"` will pass the string `"{avatar}"`.


## Using “double curlies”: CSS and other objects in JSX [](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-double-curlies-css-and-other-objects-in-jsx "Link for Using “double curlies”: CSS and other objects in JSX ")
In addition to strings, numbers, and other JavaScript expressions, you can even pass objects in JSX. Objects are also denoted with curly braces, like `{ name: "Hedy Lamarr", inventions: 5 }`. Therefore, to pass a JS object in JSX, you must wrap the object in another pair of curly braces: `person={{ name: "Hedy Lamarr", inventions: 5 }}`.
You may see this with inline CSS styles in JSX. React does not require you to use inline styles (CSS classes work great for most cases). But when you need an inline style, you pass an object to the `style` attribute:
App.js
App.js
ReloadClear Fork
```
export default function TodoList() {
  return (
    <ul style={{
      backgroundColor: 'black',
      color: 'pink'
    }}>
      <li>Improve the videophone</li>
      <li>Prepare aeronautics lectures</li>
      <li>Work on the alcohol-fuelled engine</li>
    </ul>
  );
}


```

Try changing the values of `backgroundColor` and `color`.
You can really see the JavaScript object inside the curly braces when you write it like this:
```


<ul style={




  {




    backgroundColor: 'black',




    color: 'pink'




  }





}>


```

The next time you see `{{` and `}}` in JSX, know that it’s nothing more than an object inside the JSX curlies!
Inline `style` properties are written in camelCase. For example, HTML `<ul style="background-color: black">` would be written as `<ul style={{ backgroundColor: 'black' }}>` in your component.
## More fun with JavaScript objects and curly braces [](https://react.dev/learn/javascript-in-jsx-with-curly-braces#more-fun-with-javascript-objects-and-curly-braces "Link for More fun with JavaScript objects and curly braces ")
You can move several expressions into one object, and reference them in your JSX inside curly braces:
App.js
App.js
ReloadClear Fork
```
const person = {
  name: 'Gregorio Y. Zara',
  theme: {
    backgroundColor: 'black',
    color: 'pink'
  }
};

export default function TodoList() {
  return (
    <div style={person.theme}>
      <h1>{person.name}'s Todos</h1>
      <img
        className="avatar"
        src="https://i.imgur.com/7vQD0fPs.jpg"
        alt="Gregorio Y. Zara"
      />
      <ul>
        <li>Improve the videophone</li>
        <li>Prepare aeronautics lectures</li>
        <li>Work on the alcohol-fuelled engine</li>
      </ul>
    </div>
  );
}


```

In this example, the `person` JavaScript object contains a `name` string and a `theme` object:
```


const person = {




  name: 'Gregorio Y. Zara',




  theme: {




    backgroundColor: 'black',




    color: 'pink'




  }





};


```

The component can use these values from `person` like so:
```


<div style={person.theme}>




  <h1>{person.name}'s Todos</h1>


```

JSX is very minimal as a templating language because it lets you organize data and logic using JavaScript.
## Recap[](https://react.dev/learn/javascript-in-jsx-with-curly-braces#recap "Link for Recap")
Now you know almost everything about JSX:
  * JSX attributes inside quotes are passed as strings.
  * Curly braces let you bring JavaScript logic and variables into your markup.
  * They work inside the JSX tag content or immediately after `=` in attributes.
  * `{{` and `}}` is not special syntax: it’s a JavaScript object tucked inside JSX curly braces.


## Try out some challenges[](https://react.dev/learn/javascript-in-jsx-with-curly-braces#challenges "Link for Try out some challenges")
1. Fix the mistake 2. Extract information into an object 3. Write an expression inside JSX curly braces
####
Challenge 1 of 3:
Fix the mistake [](https://react.dev/learn/javascript-in-jsx-with-curly-braces#fix-the-mistake "Link for this heading")
This code crashes with an error saying `Objects are not valid as a React child`:
App.js
App.js
ReloadClear Fork
```
const person = {
  name: 'Gregorio Y. Zara',
  theme: {
    backgroundColor: 'black',
    color: 'pink'
  }
};

export default function TodoList() {
  return (
    <div style={person.theme}>
      <h1>{person}'s Todos</h1>
      <img
        className="avatar"
        src="https://i.imgur.com/7vQD0fPs.jpg"
        alt="Gregorio Y. Zara"
      />
      <ul>
        <li>Improve the videophone</li>
        <li>Prepare aeronautics lectures</li>
        <li>Work on the alcohol-fuelled engine</li>
      </ul>
    </div>
  );
}


```

Can you find the problem?
Next Challenge
[ PreviousWriting Markup with JSX ](https://react.dev/learn/writing-markup-with-jsx)[ NextPassing Props to a Component ](https://react.dev/learn/passing-props-to-a-component)
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
  * [Overview](https://react.dev/learn/javascript-in-jsx-with-curly-braces)
  * [Passing strings with quotes ](https://react.dev/learn/javascript-in-jsx-with-curly-braces#passing-strings-with-quotes)
  * [Using curly braces: A window into the JavaScript world ](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-curly-braces-a-window-into-the-javascript-world)
  * [Where to use curly braces ](https://react.dev/learn/javascript-in-jsx-with-curly-braces#where-to-use-curly-braces)
  * [Using “double curlies”: CSS and other objects in JSX ](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-double-curlies-css-and-other-objects-in-jsx)
  * [More fun with JavaScript objects and curly braces ](https://react.dev/learn/javascript-in-jsx-with-curly-braces#more-fun-with-javascript-objects-and-curly-braces)
  * [Recap](https://react.dev/learn/javascript-in-jsx-with-curly-braces#recap)
  * [Challenges](https://react.dev/learn/javascript-in-jsx-with-curly-braces#challenges)


JavaScript in JSX with Curly Braces – React
