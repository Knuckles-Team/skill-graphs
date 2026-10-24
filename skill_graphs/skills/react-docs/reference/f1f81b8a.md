        <p>Hello, {this.state.name}.</p>
      </>
    );
  }
}
```

`setState` enqueues changes to the component state. It tells React that this component and its children need to re-render with the new state. This is the main way you'll update the user interface in response to interactions.

<Pitfall>

Calling `setState` **does not** change the current state in the already executing code:

```js {6}
function handleClick() {
  console.log(this.state.name); // "Taylor"
  this.setState({
    name: 'Robin'
  });
  console.log(this.state.name); // Still "Taylor"!
}
```

It only affects what `this.state` will return starting from the *next* render.

</Pitfall>

You can also pass a function to `setState`. It lets you update state based on the previous state:

```js {2-6}
  handleIncreaseAge = () => {
    this.setState(prevState => {
      return {
        age: prevState.age + 1
      };
    });
  }
```

You don't have to do this, but it's handy if you want to update state multiple times during the same event.

#### Parameters {/*setstate-parameters*/}

* `nextState`: Either an object or a function.
  * If you pass an object as `nextState`, it will be shallowly merged into `this.state`.
  * If you pass a function as `nextState`, it will be treated as an _updater function_. It must be pure, should take the pending state and props as arguments, and should return the object to be shallowly merged into `this.state`. React will put your updater function in a queue and re-render your component. During the next render, React will calculate the next state by applying all of the queued updaters to the previous state.

* **optional** `callback`: If specified, React will call the `callback` you've provided after the update is committed.

#### Returns {/*setstate-returns*/}

`setState` does not return anything.

#### Caveats {/*setstate-caveats*/}

- Think of `setState` as a *request* rather than an immediate command to update the component. When multiple components update their state in response to an event, React will batch their updates and re-render them together in a single pass at the end of the event. In the rare case that you need to force a particular state update to be applied synchronously, you may wrap it in [`flushSync`,](/reference/react-dom/flushSync) but this may hurt performance.

- `setState` does not update `this.state` immediately. This makes reading `this.state` right after calling `setState` a potential pitfall. Instead, use [`componentDidUpdate`](#componentdidupdate) or the setState `callback` argument, either of which are guaranteed to fire after the update has been applied. If you need to set the state based on the previous state, you can pass a function to `nextState` as described above.

<Note>

Calling `setState` in class components is similar to calling a [`set` function](/reference/react/useState#setstate) in function components.

[See how to migrate.](#migrating-a-component-with-state-from-a-class-to-a-function)

</Note>

---

### `shouldComponentUpdate(nextProps, nextState, nextContext)` {/*shouldcomponentupdate*/}

If you define `shouldComponentUpdate`, React will call it to determine whether a re-render can be skipped.

If you are confident you want to write it by hand, you may compare `this.props` with `nextProps` and `this.state` with `nextState` and return `false` to tell React the update can be skipped.

```js {6-18}
class Rectangle extends Component {
  state = {
    isHovered: false
  };

  shouldComponentUpdate(nextProps, nextState) {
    if (
      nextProps.position.x === this.props.position.x &&
      nextProps.position.y === this.props.position.y &&
      nextProps.size.width === this.props.size.width &&
      nextProps.size.height === this.props.size.height &&
      nextState.isHovered === this.state.isHovered
    ) {
      // Nothing has changed, so a re-render is unnecessary
      return false;
    }
    return true;
  }

  // ...
}

```

React calls `shouldComponentUpdate` before rendering when new props or state are being received. Defaults to `true`. This method is not called for the initial render or when [`forceUpdate`](#forceupdate) is used.

#### Parameters {/*shouldcomponentupdate-parameters*/}

- `nextProps`: The next props that the component is about to render with. Compare `nextProps` to [`this.props`](#props) to determine what changed.
- `nextState`: The next state that the component is about to render with. Compare `nextState` to [`this.state`](#props) to determine what changed.
- `nextContext`: The next context that the component is about to render with. Compare `nextContext` to [`this.context`](#context) to determine what changed. Only available if you specify [`static contextType`](#static-contexttype).

#### Returns {/*shouldcomponentupdate-returns*/}

Return `true` if you want the component to re-render. That's the default behavior.

Return `false` to tell React that re-rendering can be skipped.

#### Caveats {/*shouldcomponentupdate-caveats*/}

- This method *only* exists as a performance optimization. If your component breaks without it, fix that first.

- Consider using [`PureComponent`](/reference/react/PureComponent) instead of writing `shouldComponentUpdate` by hand. `PureComponent` shallowly compares props and state, and reduces the chance that you'll skip a necessary update.

- We do not recommend doing deep equality checks or using `JSON.stringify` in `shouldComponentUpdate`. It makes performance unpredictable and dependent on the data structure of every prop and state. In the best case, you risk introducing multi-second stalls to your application, and in the worst case you risk crashing it.

- Returning `false` does not prevent child components from re-rendering when *their* state changes.

- Returning `false` does not *guarantee* that the component will not re-render. React will use the return value as a hint but it may still choose to re-render your component if it makes sense to do for other reasons.

<Note>

Optimizing class components with `shouldComponentUpdate` is similar to optimizing function components with [`memo`.](/reference/react/memo) Function components also offer more granular optimization with [`useMemo`.](/reference/react/useMemo)

</Note>

---

### `UNSAFE_componentWillMount()` {/*unsafe_componentwillmount*/}

If you define `UNSAFE_componentWillMount`, React will call it immediately after the [`constructor`.](#constructor) It only exists for historical reasons and should not be used in any new code. Instead, use one of the alternatives:

- To initialize state, declare [`state`](#state) as a class field or set `this.state` inside the [`constructor`.](#constructor)
- If you need to run a side effect or set up a subscription, move that logic to [`componentDidMount`](#componentdidmount) instead.

[See examples of migrating away from unsafe lifecycles.](https://legacy.reactjs.org/blog/2018/03/27/update-on-async-rendering.html#examples)

#### Parameters {/*unsafe_componentwillmount-parameters*/}

`UNSAFE_componentWillMount` does not take any parameters.

#### Returns {/*unsafe_componentwillmount-returns*/}

`UNSAFE_componentWillMount` should not return anything.

#### Caveats {/*unsafe_componentwillmount-caveats*/}

- `UNSAFE_componentWillMount` will not get called if the component implements [`static getDerivedStateFromProps`](#static-getderivedstatefromprops) or [`getSnapshotBeforeUpdate`.](#getsnapshotbeforeupdate)

- Despite its naming, `UNSAFE_componentWillMount` does not guarantee that the component *will* get mounted if your app uses modern React features like [`Suspense`.](/reference/react/Suspense) If a render attempt is suspended (for example, because the code for some child component has not loaded yet), React will throw the in-progress tree away and attempt to construct the component from scratch during the next attempt. This is why this method is "unsafe". Code that relies on mounting (like adding a subscription) should go into [`componentDidMount`.](#componentdidmount)

- `UNSAFE_componentWillMount` is the only lifecycle method that runs during [server rendering.](/reference/react-dom/server) For all practical purposes, it is identical to [`constructor`,](#constructor) so you should use the `constructor` for this type of logic instead.

<Note>

Calling [`setState`](#setstate) inside `UNSAFE_componentWillMount` in a class component to initialize state is equivalent to passing that state as the initial state to [`useState`](/reference/react/useState) in a function component.

</Note>

---

### `UNSAFE_componentWillReceiveProps(nextProps, nextContext)` {/*unsafe_componentwillreceiveprops*/}

If you define `UNSAFE_componentWillReceiveProps`, React will call it when the component receives new props. It only exists for historical reasons and should not be used in any new code. Instead, use one of the alternatives:

- If you need to **run a side effect** (for example, fetch data, run an animation, or reinitialize a subscription) in response to prop changes, move that logic to [`componentDidUpdate`](#componentdidupdate) instead.
- If you need to **avoid re-computing some data only when a prop changes,** use a [memoization helper](https://legacy.reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#what-about-memoization) instead.
- If you need to **"reset" some state when a prop changes,** consider either making a component [fully controlled](https://legacy.reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#recommendation-fully-controlled-component) or [fully uncontrolled with a key](https://legacy.reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#recommendation-fully-uncontrolled-component-with-a-key) instead.
- If you need to **"adjust" some state when a prop changes,** check whether you can compute all the necessary information from props alone during rendering. If you can't, use [`static getDerivedStateFromProps`](/reference/react/Component#static-getderivedstatefromprops) instead.

[See examples of migrating away from unsafe lifecycles.](https://legacy.reactjs.org/blog/2018/03/27/update-on-async-rendering.html#updating-state-based-on-props)

#### Parameters {/*unsafe_componentwillreceiveprops-parameters*/}

- `nextProps`: The next props that the component is about to receive from its parent component. Compare `nextProps` to [`this.props`](#props) to determine what changed.
- `nextContext`: The next context that the component is about to receive from the closest provider. Compare `nextContext` to [`this.context`](#context) to determine what changed. Only available if you specify [`static contextType`](#static-contexttype).

#### Returns {/*unsafe_componentwillreceiveprops-returns*/}

`UNSAFE_componentWillReceiveProps` should not return anything.

#### Caveats {/*unsafe_componentwillreceiveprops-caveats*/}

- `UNSAFE_componentWillReceiveProps` will not get called if the component implements [`static getDerivedStateFromProps`](#static-getderivedstatefromprops) or [`getSnapshotBeforeUpdate`.](#getsnapshotbeforeupdate)

- Despite its naming, `UNSAFE_componentWillReceiveProps` does not guarantee that the component *will* receive those props if your app uses modern React features like [`Suspense`.](/reference/react/Suspense) If a render attempt is suspended (for example, because the code for some child component has not loaded yet), React will throw the in-progress tree away and attempt to construct the component from scratch during the next attempt. By the time of the next render attempt, the props might be different. This is why this method is "unsafe". Code that should run only for committed updates (like resetting a subscription) should go into [`componentDidUpdate`.](#componentdidupdate)

- `UNSAFE_componentWillReceiveProps` does not mean that the component has received *different* props than the last time. You need to compare `nextProps` and `this.props` yourself to check if something changed.

- React doesn't call `UNSAFE_componentWillReceiveProps` with initial props during mounting. It only calls this method if some of component's props are going to be updated. For example, calling [`setState`](#setstate) doesn't generally trigger `UNSAFE_componentWillReceiveProps` inside the same component.

<Note>

Calling [`setState`](#setstate) inside `UNSAFE_componentWillReceiveProps` in a class component to "adjust" state is equivalent to [calling the `set` function from `useState` during rendering](/reference/react/useState#storing-information-from-previous-renders) in a function component.

</Note>

---

### `UNSAFE_componentWillUpdate(nextProps, nextState)` {/*unsafe_componentwillupdate*/}

If you define `UNSAFE_componentWillUpdate`, React will call it before rendering with the new props or state. It only exists for historical reasons and should not be used in any new code. Instead, use one of the alternatives:

- If you need to run a side effect (for example, fetch data, run an animation, or reinitialize a subscription) in response to prop or state changes, move that logic to [`componentDidUpdate`](#componentdidupdate) instead.
- If you need to read some information from the DOM (for example, to save the current scroll position) so that you can use it in [`componentDidUpdate`](#componentdidupdate) later, read it inside [`getSnapshotBeforeUpdate`](#getsnapshotbeforeupdate) instead.

[See examples of migrating away from unsafe lifecycles.](https://legacy.reactjs.org/blog/2018/03/27/update-on-async-rendering.html#examples)

#### Parameters {/*unsafe_componentwillupdate-parameters*/}

- `nextProps`: The next props that the component is about to render with. Compare `nextProps` to [`this.props`](#props) to determine what changed.
- `nextState`: The next state that the component is about to render with. Compare `nextState` to [`this.state`](#state) to determine what changed.

#### Returns {/*unsafe_componentwillupdate-returns*/}

`UNSAFE_componentWillUpdate` should not return anything.

#### Caveats {/*unsafe_componentwillupdate-caveats*/}

- `UNSAFE_componentWillUpdate` will not get called if [`shouldComponentUpdate`](#shouldcomponentupdate) is defined and returns `false`.

- `UNSAFE_componentWillUpdate` will not get called if the component implements [`static getDerivedStateFromProps`](#static-getderivedstatefromprops) or [`getSnapshotBeforeUpdate`.](#getsnapshotbeforeupdate)

- It's not supported to call [`setState`](#setstate) (or any method that leads to `setState` being called, like dispatching a Redux action) during `componentWillUpdate`.

- Despite its naming, `UNSAFE_componentWillUpdate` does not guarantee that the component *will* update if your app uses modern React features like [`Suspense`.](/reference/react/Suspense) If a render attempt is suspended (for example, because the code for some child component has not loaded yet), React will throw the in-progress tree away and attempt to construct the component from scratch during the next attempt. By the time of the next render attempt, the props and state might be different. This is why this method is "unsafe". Code that should run only for committed updates (like resetting a subscription) should go into [`componentDidUpdate`.](#componentdidupdate)

- `UNSAFE_componentWillUpdate` does not mean that the component has received *different* props or state than the last time. You need to compare `nextProps` with `this.props` and `nextState` with `this.state` yourself to check if something changed.

- React doesn't call `UNSAFE_componentWillUpdate` with initial props and state during mounting.

<Note>

There is no direct equivalent to `UNSAFE_componentWillUpdate` in function components.

</Note>

---

### `static contextType` {/*static-contexttype*/}

If you want to read [`this.context`](#context-instance-field) from your class component, you must specify which context it needs to read. The context you specify as the `static contextType` must be a value previously created by [`createContext`.](/reference/react/createContext)

```js {2}
class Button extends Component {
  static contextType = ThemeContext;

  render() {
    const theme = this.context;
    const className = 'button-' + theme;
    return (
      <button className={className}>
        {this.props.children}
      </button>
    );
  }
}
```

<Note>

Reading `this.context` in class components is equivalent to [`useContext`](/reference/react/useContext) in function components.

[See how to migrate.](#migrating-a-component-with-context-from-a-class-to-a-function)

</Note>

---

### `static defaultProps` {/*static-defaultprops*/}

You can define `static defaultProps` to set the default props for the class. They will be used for `undefined` and missing props, but not for `null` props.

For example, here is how you define that the `color` prop should default to `'blue'`:

```js {2-4}
class Button extends Component {
  static defaultProps = {
    color: 'blue'
  };

  render() {
    return <button className={this.props.color}>click me</button>;
  }
}
```

If the `color` prop is not provided or is `undefined`, it will be set by default to `'blue'`:

```js
<>
  {/* this.props.color is "blue" */}
  <Button />

  {/* this.props.color is "blue" */}
  <Button color={undefined} />

  {/* this.props.color is null */}
  <Button color={null} />

  {/* this.props.color is "red" */}
  <Button color="red" />
</>
```

<Note>

Defining `defaultProps` in class components is similar to using [default values](/learn/passing-props-to-a-component#specifying-a-default-value-for-a-prop) in function components.

</Note>

---

### `static getDerivedStateFromError(error)` {/*static-getderivedstatefromerror*/}

If you define `static getDerivedStateFromError`, React will call it when a child component (including distant children) throws an error during rendering. This lets you display an error message instead of clearing the UI.

Typically, it is used together with [`componentDidCatch`](#componentdidcatch) which lets you send the error report to some analytics service. A component with these methods is called an *Error Boundary*.

[See an example.](#catching-rendering-errors-with-an-error-boundary)

#### Parameters {/*static-getderivedstatefromerror-parameters*/}

* `error`: The error that was thrown. In practice, it will usually be an instance of [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) but this is not guaranteed because JavaScript allows to [`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw) any value, including strings or even `null`.

#### Returns {/*static-getderivedstatefromerror-returns*/}

`static getDerivedStateFromError` should return the state telling the component to display the error message.

#### Caveats {/*static-getderivedstatefromerror-caveats*/}

* `static getDerivedStateFromError` should be a pure function. If you want to perform a side effect (for example, to call an analytics service), you need to also implement [`componentDidCatch`.](#componentdidcatch)

<Note>

There is no direct equivalent for `static getDerivedStateFromError` in function components yet. If you'd like to avoid creating class components, write a single `ErrorBoundary` component like above and use it throughout your app. Alternatively, use the [`react-error-boundary`](https://github.com/bvaughn/react-error-boundary) package which does that.

</Note>

---

### `static getDerivedStateFromProps(props, state)` {/*static-getderivedstatefromprops*/}

If you define `static getDerivedStateFromProps`, React will call it right before calling [`render`,](#render) both on the initial mount and on subsequent updates. It should return an object to update the state, or `null` to update nothing.

This method exists for [rare use cases](https://legacy.reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#when-to-use-derived-state) where the state depends on changes in props over time. For example, this `Form` component resets the `email` state when the `userID` prop changes:

```js {7-18}
class Form extends Component {
  state = {
    email: this.props.defaultEmail,
    prevUserID: this.props.userID
  };

  static getDerivedStateFromProps(props, state) {
    // Any time the current user changes,
    // Reset any parts of state that are tied to that user.
    // In this simple example, that's just the email.
    if (props.userID !== state.prevUserID) {
      return {
        prevUserID: props.userID,
        email: props.defaultEmail
      };
    }
    return null;
  }

  // ...
}
```

Note that this pattern requires you to keep a previous value of the prop (like `userID`) in state (like `prevUserID`).

<Pitfall>

Deriving state leads to verbose code and makes your components difficult to think about. [Make sure you're familiar with simpler alternatives:](https://legacy.reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html)

- If you need to **perform a side effect** (for example, data fetching or an animation) in response to a change in props, use [`componentDidUpdate`](#componentdidupdate) method instead.
- If you want to **re-compute some data only when a prop changes,** [use a memoization helper instead.](https://legacy.reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#what-about-memoization)
- If you want to **"reset" some state when a prop changes,** consider either making a component [fully controlled](https://legacy.reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#recommendation-fully-controlled-component) or [fully uncontrolled with a key](https://legacy.reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#recommendation-fully-uncontrolled-component-with-a-key) instead.

</Pitfall>

#### Parameters {/*static-getderivedstatefromprops-parameters*/}

- `props`: The next props that the component is about to render with.
- `state`: The next state that the component is about to render with.

#### Returns {/*static-getderivedstatefromprops-returns*/}

`static getDerivedStateFromProps` return an object to update the state, or `null` to update nothing.

#### Caveats {/*static-getderivedstatefromprops-caveats*/}

- This method is fired on *every* render, regardless of the cause. This is different from [`UNSAFE_componentWillReceiveProps`](#unsafe_cmoponentwillreceiveprops), which only fires when the parent causes a re-render and not as a result of a local `setState`.

- This method doesn't have access to the component instance. If you'd like, you can reuse some code between `static getDerivedStateFromProps` and the other class methods by extracting pure functions of the component props and state outside the class definition.

<Note>

Implementing `static getDerivedStateFromProps` in a class component is equivalent to [calling the `set` function from `useState` during rendering](/reference/react/useState#storing-information-from-previous-renders) in a function component.

</Note>

---

## Usage {/*usage*/}

### Defining a class component {/*defining-a-class-component*/}

To define a React component as a class, extend the built-in `Component` class and define a [`render` method:](#render)

```js
import { Component } from 'react';

class Greeting extends Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

React will call your [`render`](#render) method whenever it needs to figure out what to display on the screen. Usually, you will return some [JSX](/learn/writing-markup-with-jsx) from it. Your `render` method should be a [pure function:](https://en.wikipedia.org/wiki/Pure_function) it should only calculate the JSX.

Similarly to [function components,](/learn/your-first-component#defining-a-component) a class component can [receive information by props](/learn/your-first-component#defining-a-component) from its parent component. However, the syntax for reading props is different. For example, if the parent component renders `<Greeting name="Taylor" />`, then you can read the `name` prop from [`this.props`](#props), like `this.props.name`:

<Sandpack>

```js
import { Component } from 'react';

class Greeting extends Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}

export default function App() {
  return (
    <>
      <Greeting name="Sara" />
      <Greeting name="Cahal" />
      <Greeting name="Edite" />
    </>
  );
}
```

</Sandpack>

Note that Hooks (functions starting with `use`, like [`useState`](/reference/react/useState)) are not supported inside class components.

<Pitfall>

We recommend defining components as functions instead of classes. [See how to migrate.](#migrating-a-simple-component-from-a-class-to-a-function)

</Pitfall>

---

### Adding state to a class component {/*adding-state-to-a-class-component*/}

To add [state](/learn/state-a-components-memory) to a class, assign an object to a property called [`state`](#state). To update state, call [`this.setState`](#setstate).

<Sandpack>

```js
import { Component } from 'react';

export default class Counter extends Component {
  state = {
    name: 'Taylor',
    age: 42,
  };

  handleNameChange = (e) => {
    this.setState({
      name: e.target.value
    });
  }

  handleAgeChange = () => {
    this.setState({
      age: this.state.age + 1
    });
  };

  render() {
    return (
      <>
        <input
          value={this.state.name}
          onChange={this.handleNameChange}
        />
        <button onClick={this.handleAgeChange}>
          Increment age
        </button>
        <p>Hello, {this.state.name}. You are {this.state.age}.</p>
