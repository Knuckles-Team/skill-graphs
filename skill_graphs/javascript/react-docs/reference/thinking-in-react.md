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
[Quick Start](https://react.dev/learn)
Copy pageCopy
# Thinking in React[](https://react.dev/learn/thinking-in-react#undefined "Link for this heading")
React can change how you think about the designs you look at and the apps you build. When you build a user interface with React, you will first break it apart into pieces called _components_. Then, you will describe the different visual states for each of your components. Finally, you will connect your components together so that the data flows through them. In this tutorial, we’ll guide you through the thought process of building a searchable product data table with React.
## Start with the mockup [](https://react.dev/learn/thinking-in-react#start-with-the-mockup "Link for Start with the mockup ")
Imagine that you already have a JSON API and a mockup from a designer.
The JSON API returns some data that looks like this:
```


[




  { category: "Fruits", price: "$1", stocked: true, name: "Apple" },




  { category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit" },




  { category: "Fruits", price: "$2", stocked: false, name: "Passionfruit" },




  { category: "Vegetables", price: "$2", stocked: true, name: "Spinach" },




  { category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin" },




  { category: "Vegetables", price: "$1", stocked: true, name: "Peas" }




]

```

The mockup looks like this:
![](https://react.dev/images/docs/s_thinking-in-react_ui.png)
To implement a UI in React, you will usually follow the same five steps.
## Step 1: Break the UI into a component hierarchy [](https://react.dev/learn/thinking-in-react#step-1-break-the-ui-into-a-component-hierarchy "Link for Step 1: Break the UI into a component hierarchy ")
Start by drawing boxes around every component and subcomponent in the mockup and naming them. If you work with a designer, they may have already named these components in their design tool. Ask them!
Depending on your background, you can think about splitting up a design into components in different ways:
  * **Programming** —use the same techniques for deciding if you should create a new function or object. One such technique is the
  * **CSS** —consider what you would make class selectors for. (However, components are a bit less granular.)
  * **Design** —consider how you would organize the design’s layers.


If your JSON is well-structured, you’ll often find that it naturally maps to the component structure of your UI. That’s because UI and data models often have the same information architecture—that is, the same shape. Separate your UI into components, where each component matches one piece of your data model.
There are five components on this screen:
![](https://react.dev/images/docs/s_thinking-in-react_ui_outline.png)
  1. `FilterableProductTable` (grey) contains the entire app.
  2. `SearchBar` (blue) receives the user input.
  3. `ProductTable` (lavender) displays and filters the list according to the user input.
  4. `ProductCategoryRow` (green) displays a heading for each category.
  5. `ProductRow` (yellow) displays a row for each product.


If you look at `ProductTable` (lavender), you’ll see that the table header (containing the “Name” and “Price” labels) isn’t its own component. This is a matter of preference, and you could go either way. For this example, it is a part of `ProductTable` because it appears inside the `ProductTable`’s list. However, if this header grows to be complex (e.g., if you add sorting), you can move it into its own `ProductTableHeader` component.
Now that you’ve identified the components in the mockup, arrange them into a hierarchy. Components that appear within another component in the mockup should appear as a child in the hierarchy:
  * `FilterableProductTable`
    * `SearchBar`
    * `ProductTable`
      * `ProductCategoryRow`
      * `ProductRow`


## Step 2: Build a static version in React [](https://react.dev/learn/thinking-in-react#step-2-build-a-static-version-in-react "Link for Step 2: Build a static version in React ")
Now that you have your component hierarchy, it’s time to implement your app. The most straightforward approach is to build a version that renders the UI from your data model without adding any interactivity… yet! It’s often easier to build the static version first and add interactivity later. Building a static version requires a lot of typing and no thinking, but adding interactivity requires a lot of thinking and not a lot of typing.
To build a static version of your app that renders your data model, you’ll want to build [components](https://react.dev/learn/your-first-component) that reuse other components and pass data using [props.](https://react.dev/learn/passing-props-to-a-component) Props are a way of passing data from parent to child. (If you’re familiar with the concept of [state](https://react.dev/learn/state-a-components-memory), don’t use state at all to build this static version. State is reserved only for interactivity, that is, data that changes over time. Since this is a static version of the app, you don’t need it.)
You can either build “top down” by starting with building the components higher up in the hierarchy (like `FilterableProductTable`) or “bottom up” by working from components lower down (like `ProductRow`). In simpler examples, it’s usually easier to go top-down, and on larger projects, it’s easier to go bottom-up.
App.js
App.js
ReloadClear Fork
```
function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">
        {category}
      </th>
    </tr>
  );
}

function ProductRow({ product }) {
  const name = product.stocked ? product.name :
    <span style={{ color: 'red' }}>
      {product.name}
    </span>;

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products }) {
  const rows = [];
  let lastCategory = null;

  products.forEach((product) => {
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category} />
      );
    }
    rows.push(
      <ProductRow
        product={product}
        key={product.name} />
    );
    lastCategory = product.category;
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function SearchBar() {
  return (
    <form>
      <input type="text" placeholder="Search..." />
      <label>
        <input type="checkbox" />
        {' '}
        Only show products in stock
      </label>
    </form>
  );
}

function FilterableProductTable({ products }) {
  return (
    <div>
      <SearchBar />
      <ProductTable products={products} />
    </div>
  );
}

const PRODUCTS = [
  {category: "Fruits", price: "$1", stocked: true, name: "Apple"},
  {category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit"},
  {category: "Fruits", price: "$2", stocked: false, name: "Passionfruit"},
  {category: "Vegetables", price: "$2", stocked: true, name: "Spinach"},
  {category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin"},
  {category: "Vegetables", price: "$1", stocked: true, name: "Peas"}
];

export default function App() {
  return <FilterableProductTable products={PRODUCTS} />;
}


```

(If this code looks intimidating, go through the [Quick Start](https://react.dev/learn) first!)
After building your components, you’ll have a library of reusable components that render your data model. Because this is a static app, the components will only return JSX. The component at the top of the hierarchy (`FilterableProductTable`) will take your data model as a prop. This is called _one-way data flow_ because the data flows down from the top-level component to the ones at the bottom of the tree.
At this point, you should not be using any state values. That’s for the next step!
## Step 3: Find the minimal but complete representation of UI state [](https://react.dev/learn/thinking-in-react#step-3-find-the-minimal-but-complete-representation-of-ui-state "Link for Step 3: Find the minimal but complete representation of UI state ")
To make the UI interactive, you need to let users change your underlying data model. You will use _state_ for this.
Think of state as the minimal set of changing data that your app needs to remember. The most important principle for structuring state is to keep it
Now think of all of the pieces of data in this example application:
  1. The original list of products
  2. The search text the user has entered
  3. The value of the checkbox
  4. The filtered list of products


Which of these are state? Identify the ones that are not:
  * Does it **remain unchanged** over time? If so, it isn’t state.
  * Is it **passed in from a parent** via props? If so, it isn’t state.
  * **Can you compute it** based on existing state or props in your component? If so, it _definitely_ isn’t state!


What’s left is probably state.
Let’s go through them one by one again:
  1. The original list of products is **passed in as props, so it’s not state.**
  2. The search text seems to be state since it changes over time and can’t be computed from anything.
  3. The value of the checkbox seems to be state since it changes over time and can’t be computed from anything.
  4. The filtered list of products **isn’t state because it can be computed** by taking the original list of products and filtering it according to the search text and value of the checkbox.


This means only the search text and the value of the checkbox are state! Nicely done!
#### Props vs State [](https://react.dev/learn/thinking-in-react#props-vs-state "Link for Props vs State ")
There are two types of “model” data in React: props and state. The two are very different:
  * [**Props** are like arguments you pass](https://react.dev/learn/passing-props-to-a-component) to a function. They let a parent component pass data to a child component and customize its appearance. For example, a `Form` can pass a `color` prop to a `Button`.
  * [**State** is like a component’s memory.](https://react.dev/learn/state-a-components-memory) It lets a component keep track of some information and change it in response to interactions. For example, a `Button` might keep track of `isHovered` state.


Props and state are different, but they work together. A parent component will often keep some information in state (so that it can change it), and _pass it down_ to child components as their props. It’s okay if the difference still feels fuzzy on the first read. It takes a bit of practice for it to really stick!
## Step 4: Identify where your state should live [](https://react.dev/learn/thinking-in-react#step-4-identify-where-your-state-should-live "Link for Step 4: Identify where your state should live ")
After identifying your app’s minimal state data, you need to identify which component is responsible for changing this state, or _owns_ the state. Remember: React uses one-way data flow, passing data down the component hierarchy from parent to child component. It may not be immediately clear which component should own what state. This can be challenging if you’re new to this concept, but you can figure it out by following these steps!
For each piece of state in your application:
  1. Identify _every_ component that renders something based on that state.
  2. Find their closest common parent component—a component above them all in the hierarchy.
  3. Decide where the state should live:
    1. Often, you can put the state directly into their common parent.
    2. You can also put the state into some component above their common parent.
    3. If you can’t find a component where it makes sense to own the state, create a new component solely for holding the state and add it somewhere in the hierarchy above the common parent component.


In the previous step, you found two pieces of state in this application: the search input text, and the value of the checkbox. In this example, they always appear together, so it makes sense to put them into the same place.
Now let’s run through our strategy for them:
  1. **Identify components that use state:**
     * `ProductTable` needs to filter the product list based on that state (search text and checkbox value).
     * `SearchBar` needs to display that state (search text and checkbox value).
  2. **Find their common parent:** The first parent component both components share is `FilterableProductTable`.
  3. **Decide where the state lives** : We’ll keep the filter text and checked state values in `FilterableProductTable`.


So the state values will live in `FilterableProductTable`.
Add state to the component with the [`useState()` Hook.](https://react.dev/reference/react/useState) Hooks are special functions that let you “hook into” React. Add two state variables at the top of `FilterableProductTable` and specify their initial state:
```


function FilterableProductTable({ products }) {




  const [filterText, setFilterText] = useState('');




  const [inStockOnly, setInStockOnly] = useState(false);


```

Then, pass `filterText` and `inStockOnly` to `ProductTable` and `SearchBar` as props:
```


<div>




  <SearchBar




    filterText={filterText}




    inStockOnly={inStockOnly} />




  <ProductTable




    products={products}




    filterText={filterText}




    inStockOnly={inStockOnly} />





</div>


```

You can start seeing how your application will behave. Edit the `filterText` initial value from `useState('')` to `useState('fruit')` in the sandbox code below. You’ll see both the search input text and the table update:
App.js
App.js
ReloadClear Fork
```
import { useState } from 'react';

function FilterableProductTable({ products }) {
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);

  return (
    <div>
      <SearchBar
        filterText={filterText}
        inStockOnly={inStockOnly} />
      <ProductTable
        products={products}
        filterText={filterText}
        inStockOnly={inStockOnly} />
    </div>
  );
}

function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">
        {category}
      </th>
    </tr>
  );
}

function ProductRow({ product }) {
  const name = product.stocked ? product.name :
    <span style={{ color: 'red' }}>
      {product.name}
    </span>;

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products, filterText, inStockOnly }) {
  const rows = [];
  let lastCategory = null;

  products.forEach((product) => {
    if (
      product.name.toLowerCase().indexOf(
        filterText.toLowerCase()
      ) === -1
    ) {
      return;
    }
    if (inStockOnly && !product.stocked) {
      return;
    }
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category} />
      );
    }
    rows.push(
      <ProductRow
        product={product}
        key={product.name} />
    );
    lastCategory = product.category;
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function SearchBar({ filterText, inStockOnly }) {
  return (
    <form>
      <input
        type="text"
        value={filterText}
        placeholder="Search..."/>
      <label>
        <input
          type="checkbox"
          checked={inStockOnly} />
        {' '}
        Only show products in stock
      </label>
    </form>
  );
}

const PRODUCTS = [
  {category: "Fruits", price: "$1", stocked: true, name: "Apple"},
  {category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit"},
  {category: "Fruits", price: "$2", stocked: false, name: "Passionfruit"},
  {category: "Vegetables", price: "$2", stocked: true, name: "Spinach"},
  {category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin"},
  {category: "Vegetables", price: "$1", stocked: true, name: "Peas"}
];

export default function App() {
  return <FilterableProductTable products={PRODUCTS} />;
}


```

Notice that editing the form doesn’t work yet. There is a console error in the sandbox above explaining why:
Console
You provided a `value` prop to a form field without an `onChange` handler. This will render a read-only field.
In the sandbox above, `ProductTable` and `SearchBar` read the `filterText` and `inStockOnly` props to render the table, the input, and the checkbox. For example, here is how `SearchBar` populates the input value:
```


function SearchBar({ filterText, inStockOnly }) {




  return (




    <form>




      <input




        type="text"




        value={filterText}




        placeholder="Search..."/>


```

However, you haven’t added any code to respond to the user actions like typing yet. This will be your final step.
## Step 5: Add inverse data flow [](https://react.dev/learn/thinking-in-react#step-5-add-inverse-data-flow "Link for Step 5: Add inverse data flow ")
Currently your app renders correctly with props and state flowing down the hierarchy. But to change the state according to user input, you will need to support data flowing the other way: the form components deep in the hierarchy need to update the state in `FilterableProductTable`.
React makes this data flow explicit, but it requires a little more typing than two-way data binding. If you try to type or check the box in the example above, you’ll see that React ignores your input. This is intentional. By writing `<input value={filterText} />`, you’ve set the `value` prop of the `input` to always be equal to the `filterText` state passed in from `FilterableProductTable`. Since `filterText` state is never set, the input never changes.
You want to make it so whenever the user changes the form inputs, the state updates to reflect those changes. The state is owned by `FilterableProductTable`, so only it can call `setFilterText` and `setInStockOnly`. To let `SearchBar` update the `FilterableProductTable`’s state, you need to pass these functions down to `SearchBar`:
```


function FilterableProductTable({ products }) {




  const [filterText, setFilterText] = useState('');




  const [inStockOnly, setInStockOnly] = useState(false);








  return (




    <div>




      <SearchBar




        filterText={filterText}




        inStockOnly={inStockOnly}




        onFilterTextChange={setFilterText}




        onInStockOnlyChange={setInStockOnly} />


```

Inside the `SearchBar`, you will add the `onChange` event handlers and set the parent state from them:
```


function SearchBar({




  filterText,




  inStockOnly,




  onFilterTextChange,




  onInStockOnlyChange





}) {




  return (




    <form>




      <input




        type="text"




        value={filterText}




        placeholder="Search..."




        onChange={(e) => onFilterTextChange(e.target.value)}




      />




      <label>




        <input




          type="checkbox"




          checked={inStockOnly}




          onChange={(e) => onInStockOnlyChange(e.target.checked)}


```

Now the application fully works!
App.js
App.js
ReloadClear Fork
```
import { useState } from 'react';

function FilterableProductTable({ products }) {
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);

  return (
    <div>
      <SearchBar
        filterText={filterText}
        inStockOnly={inStockOnly}
        onFilterTextChange={setFilterText}
        onInStockOnlyChange={setInStockOnly} />
      <ProductTable
        products={products}
        filterText={filterText}
        inStockOnly={inStockOnly} />
    </div>
  );
}

function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">
        {category}
      </th>
    </tr>
  );
}

function ProductRow({ product }) {
  const name = product.stocked ? product.name :
    <span style={{ color: 'red' }}>
      {product.name}
    </span>;

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products, filterText, inStockOnly }) {
  const rows = [];
  let lastCategory = null;

  products.forEach((product) => {
    if (
      product.name.toLowerCase().indexOf(
        filterText.toLowerCase()
      ) === -1
    ) {
      return;
    }
    if (inStockOnly && !product.stocked) {
      return;
    }
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category} />
      );
    }
    rows.push(
      <ProductRow
        product={product}
        key={product.name} />
    );
    lastCategory = product.category;
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function SearchBar({
  filterText,
  inStockOnly,
  onFilterTextChange,
  onInStockOnlyChange
}) {
  return (
    <form>
      <input
        type="text"
        value={filterText} placeholder="Search..."
        onChange={(e) => onFilterTextChange(e.target.value)} />
      <label>
        <input
          type="checkbox"
          checked={inStockOnly}
          onChange={(e) => onInStockOnlyChange(e.target.checked)} />
        {' '}
        Only show products in stock
      </label>
    </form>
  );
}

const PRODUCTS = [
  {category: "Fruits", price: "$1", stocked: true, name: "Apple"},
  {category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit"},
  {category: "Fruits", price: "$2", stocked: false, name: "Passionfruit"},
  {category: "Vegetables", price: "$2", stocked: true, name: "Spinach"},
  {category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin"},
  {category: "Vegetables", price: "$1", stocked: true, name: "Peas"}
];

export default function App() {
  return <FilterableProductTable products={PRODUCTS} />;
}


```

You can learn all about handling events and updating state in the [Adding Interactivity](https://react.dev/learn/adding-interactivity) section.
## Where to go from here [](https://react.dev/learn/thinking-in-react#where-to-go-from-here "Link for Where to go from here ")
This was a very brief introduction to how to think about building components and applications with React. You can [start a React project](https://react.dev/learn/installation) right now or [dive deeper on all the syntax](https://react.dev/learn/describing-the-ui) used in this tutorial.
[ PreviousTutorial: Tic-Tac-Toe ](https://react.dev/learn/tutorial-tic-tac-toe)[ NextInstallation ](https://react.dev/learn/installation)
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
  * [Overview](https://react.dev/learn/thinking-in-react)
  * [Start with the mockup ](https://react.dev/learn/thinking-in-react#start-with-the-mockup)
  * [Step 1: Break the UI into a component hierarchy ](https://react.dev/learn/thinking-in-react#step-1-break-the-ui-into-a-component-hierarchy)
  * [Step 2: Build a static version in React ](https://react.dev/learn/thinking-in-react#step-2-build-a-static-version-in-react)
  * [Step 3: Find the minimal but complete representation of UI state ](https://react.dev/learn/thinking-in-react#step-3-find-the-minimal-but-complete-representation-of-ui-state)
  * [Step 4: Identify where your state should live ](https://react.dev/learn/thinking-in-react#step-4-identify-where-your-state-should-live)
  * [Step 5: Add inverse data flow ](https://react.dev/learn/thinking-in-react#step-5-add-inverse-data-flow)
  * [Where to go from here ](https://react.dev/learn/thinking-in-react#where-to-go-from-here)
