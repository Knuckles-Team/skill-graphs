## Overview [](https://react.dev/learn/tutorial-tic-tac-toe#overview "Link for Overview ")
Now that you’re set up, let’s get an overview of React!
### Inspecting the starter code [](https://react.dev/learn/tutorial-tic-tac-toe#inspecting-the-starter-code "Link for Inspecting the starter code ")
In CodeSandbox you’ll see three main sections:
![CodeSandbox with starter code](https://react.dev/images/tutorial/react-starter-code-codesandbox.png)
  1. The _Files_ section with a list of files like `App.js`, `index.js`, `styles.css` in `src` folder and a folder called `public`
  2. The _code editor_ where you’ll see the source code of your selected file
  3. The _browser_ section where you’ll see how the code you’ve written will be displayed


The `App.js` file should be selected in the _Files_ section. The contents of that file in the _code editor_ should be:
```


export default function Square() {




  return <button className="square">X</button>;




}

```

The _browser_ section should be displaying a square with an X in it like this:
![x-filled square](https://react.dev/images/tutorial/x-filled-square.png)
Now let’s have a look at the files in the starter code.
####  `App.js` [](https://react.dev/learn/tutorial-tic-tac-toe#appjs "Link for this heading")
The code in `App.js` creates a _component_. In React, a component is a piece of reusable code that represents a part of a user interface. Components are used to render, manage, and update the UI elements in your application. Let’s look at the component line by line to see what’s going on:
```


export default function Square() {




  return <button className="square">X</button>;




}

```

The first line defines a function called `Square`. The `export` JavaScript keyword makes this function accessible outside of this file. The `default` keyword tells other files using your code that it’s the main function in your file.
```


export default function Square() {




  return <button className="square">X</button>;




}

```

The second line returns a button. The `return` JavaScript keyword means whatever comes after is returned as a value to the caller of the function. `<button>` is a _JSX element_. A JSX element is a combination of JavaScript code and HTML tags that describes what you’d like to display. `className="square"` is a button property or _prop_ that tells CSS how to style the button. `X` is the text displayed inside of the button and `</button>` closes the JSX element to indicate that any following content shouldn’t be placed inside the button.
####  `styles.css` [](https://react.dev/learn/tutorial-tic-tac-toe#stylescss "Link for this heading")
Click on the file labeled `styles.css` in the _Files_ section of CodeSandbox. This file defines the styles for your React app. The first two _CSS selectors_ (`*` and `body`) define the style of large parts of your app while the `.square` selector defines the style of any component where the `className` property is set to `square`. In your code, that would match the button from your Square component in the `App.js` file.
####  `index.js` [](https://react.dev/learn/tutorial-tic-tac-toe#indexjs "Link for this heading")
Click on the file labeled `index.js` in the _Files_ section of CodeSandbox. You won’t be editing this file during the tutorial but it is the bridge between the component you created in the `App.js` file and the web browser.
```


import { StrictMode } from 'react';





import { createRoot } from 'react-dom/client';





import './styles.css';









import App from './App';


```

Lines 1-5 bring all the necessary pieces together:
  * React
  * React’s library to talk to web browsers (React DOM)
  * the styles for your components
  * the component you created in `App.js`.


The remainder of the file brings all the pieces together and injects the final product into `index.html` in the `public` folder.
### Building the board [](https://react.dev/learn/tutorial-tic-tac-toe#building-the-board "Link for Building the board ")
Let’s get back to `App.js`. This is where you’ll spend the rest of the tutorial.
Currently the board is only a single square, but you need nine! If you just try and copy paste your square to make two squares like this:
```


export default function Square() {




  return <button className="square">X</button><button className="square">X</button>;




}

```

You’ll get this error:
Console
/src/App.js: Adjacent JSX elements must be wrapped in an enclosing tag. Did you want a JSX Fragment `<>...</>`?
React components need to return a single JSX element and not multiple adjacent JSX elements like two buttons. To fix this you can use _Fragments_ (`<>` and `</>`) to wrap multiple adjacent JSX elements like this:
```


export default function Square() {




  return (




    <>




      <button className="square">X</button>




      <button className="square">X</button>




    </>




  );




}

```

Now you should see:
![two x-filled squares](https://react.dev/images/tutorial/two-x-filled-squares.png)
Great! Now you just need to copy-paste a few times to add nine squares and…
![nine x-filled squares in a line](https://react.dev/images/tutorial/nine-x-filled-squares.png)
Oh no! The squares are all in a single line, not in a grid like you need for our board. To fix this you’ll need to group your squares into rows with `div`s and add some CSS classes. While you’re at it, you’ll give each square a number to make sure you know where each square is displayed.
In the `App.js` file, update the `Square` component to look like this:
```


export default function Square() {




  return (




    <>




      <div className="board-row">




        <button className="square">1</button>




        <button className="square">2</button>




        <button className="square">3</button>




      </div>




      <div className="board-row">




        <button className="square">4</button>




        <button className="square">5</button>




        <button className="square">6</button>




      </div>




      <div className="board-row">




        <button className="square">7</button>




        <button className="square">8</button>




        <button className="square">9</button>




      </div>




    </>




  );




}

```

The CSS defined in `styles.css` styles the divs with the `className` of `board-row`. Now that you’ve grouped your components into rows with the styled `div`s you have your tic-tac-toe board:
![tic-tac-toe board filled with numbers 1 through 9](https://react.dev/images/tutorial/number-filled-board.png)
But you now have a problem. Your component named `Square`, really isn’t a square anymore. Let’s fix that by changing the name to `Board`:
```


export default function Board() {




  //...




}

```

At this point your code should look something like this:
App.js
App.js
ReloadClear Fork
```
export default function Board() {
  return (
    <>
      <div className="board-row">
        <button className="square">1</button>
        <button className="square">2</button>
        <button className="square">3</button>
      </div>
      <div className="board-row">
        <button className="square">4</button>
        <button className="square">5</button>
        <button className="square">6</button>
      </div>
      <div className="board-row">
        <button className="square">7</button>
        <button className="square">8</button>
        <button className="square">9</button>
      </div>
    </>
  );
}


```

Psssst… That’s a lot to type! It’s okay to copy and paste code from this page. However, if you’re up for a little challenge, we recommend only copying code that you’ve manually typed at least once yourself.
### Passing data through props [](https://react.dev/learn/tutorial-tic-tac-toe#passing-data-through-props "Link for Passing data through props ")
Next, you’ll want to change the value of a square from empty to “X” when the user clicks on the square. With how you’ve built the board so far you would need to copy-paste the code that updates the square nine times (once for each square you have)! Instead of copy-pasting, React’s component architecture allows you to create a reusable component to avoid messy, duplicated code.
First, you are going to copy the line defining your first square (`<button className="square">1</button>`) from your `Board` component into a new `Square` component:
```


function Square() {




  return <button className="square">1</button>;





}









export default function Board() {




  // ...




}

```

Then you’ll update the Board component to render that `Square` component using JSX syntax:
```


// ...





export default function Board() {




  return (




    <>




      <div className="board-row">




        <Square />




        <Square />




        <Square />




      </div>




      <div className="board-row">




        <Square />




        <Square />




        <Square />




      </div>




      <div className="board-row">




        <Square />




        <Square />




        <Square />




      </div>




    </>




  );




}

```

Note how unlike the browser `div`s, your own components `Board` and `Square` must start with a capital letter.
Let’s take a look:
![one-filled board](https://react.dev/images/tutorial/board-filled-with-ones.png)
Oh no! You lost the numbered squares you had before. Now each square says “1”. To fix this, you will use _props_ to pass the value each square should have from the parent component (`Board`) to its child (`Square`).
Update the `Square` component to read the `value` prop that you’ll pass from the `Board`:
```


function Square({ value }) {




  return <button className="square">1</button>;




}

```

`function Square({ value })` indicates the Square component can be passed a prop called `value`.
Now you want to display that `value` instead of `1` inside every square. Try doing it like this:
```


function Square({ value }) {




  return <button className="square">value</button>;




}

```

Oops, this is not what you wanted:
![value-filled board](https://react.dev/images/tutorial/board-filled-with-value.png)
You wanted to render the JavaScript variable called `value` from your component, not the word “value”. To “escape into JavaScript” from JSX, you need curly braces. Add curly braces around `value` in JSX like so:
```


function Square({ value }) {




  return <button className="square">{value}</button>;




}

```

For now, you should see an empty board:
![empty board](https://react.dev/images/tutorial/empty-board.png)
This is because the `Board` component hasn’t passed the `value` prop to each `Square` component it renders yet. To fix it you’ll add the `value` prop to each `Square` component rendered by the `Board` component:
```


export default function Board() {




  return (




    <>




      <div className="board-row">




        <Square value="1" />




        <Square value="2" />




        <Square value="3" />




      </div>




      <div className="board-row">




        <Square value="4" />




        <Square value="5" />




        <Square value="6" />




      </div>




      <div className="board-row">




        <Square value="7" />




        <Square value="8" />




        <Square value="9" />




      </div>




    </>




  );




}

```

Now you should see a grid of numbers again:
![tic-tac-toe board filled with numbers 1 through 9](https://react.dev/images/tutorial/number-filled-board.png)
Your updated code should look like this:
App.js
App.js
ReloadClear Fork
```
function Square({ value }) {
  return <button className="square">{value}</button>;
}

export default function Board() {
  return (
    <>
      <div className="board-row">
        <Square value="1" />
        <Square value="2" />
        <Square value="3" />
      </div>
      <div className="board-row">
        <Square value="4" />
        <Square value="5" />
        <Square value="6" />
      </div>
      <div className="board-row">
        <Square value="7" />
        <Square value="8" />
        <Square value="9" />
      </div>
    </>
  );
}


```

### Making an interactive component [](https://react.dev/learn/tutorial-tic-tac-toe#making-an-interactive-component "Link for Making an interactive component ")
Let’s fill the `Square` component with an `X` when you click it. Declare a function called `handleClick` inside of the `Square`. Then, add `onClick` to the props of the button JSX element returned from the `Square`:
```


function Square({ value }) {




  function handleClick() {




    console.log('clicked!');




  }








  return (




    <button




      className="square"




      onClick={handleClick}




    >




      {value}




    </button>




  );




}

```

If you click on a square now, you should see a log saying `"clicked!"` in the _Console_ tab at the bottom of the _Browser_ section in CodeSandbox. Clicking the square more than once will log `"clicked!"` again. Repeated console logs with the same message will not create more lines in the console. Instead, you will see an incrementing counter next to your first `"clicked!"` log.
If you are following this tutorial using your local development environment, you need to open your browser’s Console. For example, if you use the Chrome browser, you can view the Console with the keyboard shortcut **Shift + Ctrl + J** (on Windows/Linux) or **Option + ⌘ + J** (on macOS).
As a next step, you want the Square component to “remember” that it got clicked, and fill it with an “X” mark. To “remember” things, components use _state_.
React provides a special function called `useState` that you can call from your component to let it “remember” things. Let’s store the current value of the `Square` in state, and change it when the `Square` is clicked.
Import `useState` at the top of the file. Remove the `value` prop from the `Square` component. Instead, add a new line at the start of the `Square` that calls `useState`. Have it return a state variable called `value`:
```


import { useState } from 'react';









function Square() {




  const [value, setValue] = useState(null);








  function handleClick() {




    //...


```

`value` stores the value and `setValue` is a function that can be used to change the value. The `null` passed to `useState` is used as the initial value for this state variable, so `value` here starts off equal to `null`.
Since the `Square` component no longer accepts props anymore, you’ll remove the `value` prop from all nine of the Square components created by the Board component:
```


// ...





export default function Board() {




  return (




    <>




      <div className="board-row">




        <Square />




        <Square />




        <Square />




      </div>




      <div className="board-row">




        <Square />




        <Square />




        <Square />




      </div>




      <div className="board-row">




        <Square />




        <Square />




        <Square />




      </div>




    </>




  );




}

```

Now you’ll change `Square` to display an “X” when clicked. Replace the `console.log("clicked!");` event handler with `setValue('X');`. Now your `Square` component looks like this:
```


function Square() {




  const [value, setValue] = useState(null);








  function handleClick() {




    setValue('X');




  }








  return (




    <button




      className="square"




      onClick={handleClick}




    >




      {value}




    </button>




  );




}

```

By calling this `set` function from an `onClick` handler, you’re telling React to re-render that `Square` whenever its `<button>` is clicked. After the update, the `Square`’s `value` will be `'X'`, so you’ll see the “X” on the game board. Click on any Square, and “X” should show up:
![adding xes to board](https://react.dev/images/tutorial/tictac-adding-x-s.gif)
Each Square has its own state: the `value` stored in each Square is completely independent of the others. When you call a `set` function in a component, React automatically updates the child components inside too.
After you’ve made the above changes, your code will look like this:
App.js
App.js
ReloadClear Fork
```
import { useState } from 'react';

function Square() {
  const [value, setValue] = useState(null);

  function handleClick() {
    setValue('X');
  }

  return (
    <button
      className="square"
      onClick={handleClick}
    >
      {value}
    </button>
  );
}

export default function Board() {
  return (
    <>
      <div className="board-row">
        <Square />
        <Square />
        <Square />
      </div>
      <div className="board-row">
        <Square />
        <Square />
        <Square />
      </div>
      <div className="board-row">
        <Square />
        <Square />
        <Square />
      </div>
    </>
  );
}


```

### React Developer Tools [](https://react.dev/learn/tutorial-tic-tac-toe#react-developer-tools "Link for React Developer Tools ")
React DevTools let you check the props and the state of your React components. You can find the React DevTools tab at the bottom of the _browser_ section in CodeSandbox:
![React DevTools in CodeSandbox](https://react.dev/images/tutorial/codesandbox-devtools.png)
To inspect a particular component on the screen, use the button in the top left corner of React DevTools:
![Selecting components on the page with React DevTools](https://react.dev/images/tutorial/devtools-select.gif)
For local development, React DevTools is available as a _Components_ tab will appear in your browser Developer Tools for sites using React.
