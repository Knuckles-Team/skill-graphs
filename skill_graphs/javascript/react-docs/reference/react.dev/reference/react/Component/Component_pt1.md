---
title: Component
---

<Pitfall>

We recommend defining components as functions instead of classes. [See how to migrate.](#alternatives)

</Pitfall>

<Intro>

`Component` is the base class for the React components defined as [JavaScript classes.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) Class components are still supported by React, but we don't recommend using them in new code.

```js
class Greeting extends Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

</Intro>

<InlineToc />

---

## Reference {/*reference*/}

### `Component` {/*component*/}

To define a React component as a class, extend the built-in `Component` class and define a [`render` method:](#render)

```js
import { Component } from 'react';

class Greeting extends Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

Only the `render` method is required, other methods are optional.

[See more examples below.](#usage)

---

### `context` {/*context*/}

The [context](/learn/passing-data-deeply-with-context) of a class component is available as `this.context`. It is only available if you specify *which* context you want to receive using [`static contextType`](#static-contexttype).

A class component can only read one context at a time.

```js {2,5}
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

### `props` {/*props*/}

The props passed to a class component are available as `this.props`.

```js {3}
class Greeting extends Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}

<Greeting name="Taylor" />
```

<Note>

Reading `this.props` in class components is equivalent to [declaring props](/learn/passing-props-to-a-component#step-2-read-props-inside-the-child-component) in function components.

[See how to migrate.](#migrating-a-simple-component-from-a-class-to-a-function)

</Note>

---

### `state` {/*state*/}

The state of a class component is available as `this.state`. The `state` field must be an object. Do not mutate the state directly. If you wish to change the state, call `setState` with the new state.

```js {2-4,7-9,18}
class Counter extends Component {
  state = {
    age: 42,
  };

  handleAgeChange = () => {
    this.setState({
      age: this.state.age + 1
    });
  };

  render() {
    return (
      <>
        <button onClick={this.handleAgeChange}>
        Increment age
        </button>
        <p>You are {this.state.age}.</p>
      </>
    );
  }
}
```

<Note>

Defining `state` in class components is equivalent to calling [`useState`](/reference/react/useState) in function components.

[See how to migrate.](#migrating-a-component-with-state-from-a-class-to-a-function)

</Note>

---

### `constructor(props)` {/*constructor*/}

The [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor) runs before your class component *mounts* (gets added to the screen). Typically, a constructor is only used for two purposes in React. It lets you declare state and [bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind) your class methods to the class instance:

```js {2-6}
class Counter extends Component {
  constructor(props) {
    super(props);
    this.state = { counter: 0 };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    // ...
  }
```

If you use modern JavaScript syntax, constructors are rarely needed. Instead, you can rewrite this code above using the [public class field syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields) which is supported both by modern browsers and tools like [Babel:](https://babeljs.io/)

```js {2,4}
class Counter extends Component {
  state = { counter: 0 };

  handleClick = () => {
    // ...
  }
```

A constructor should not contain any side effects or subscriptions.

#### Parameters {/*constructor-parameters*/}

* `props`: The component's initial props.

#### Returns {/*constructor-returns*/}

`constructor` should not return anything.

#### Caveats {/*constructor-caveats*/}

* Do not run any side effects or subscriptions in the constructor. Instead, use [`componentDidMount`](#componentdidmount) for that.

* Inside a constructor, you need to call `super(props)` before any other statement. If you don't do that, `this.props` will be `undefined` while the constructor runs, which can be confusing and cause bugs.

* Constructor is the only place where you can assign [`this.state`](#state) directly. In all other methods, you need to use [`this.setState()`](#setstate) instead. Do not call `setState` in the constructor.

* When you use [server rendering,](/reference/react-dom/server) the constructor will run on the server too, followed by the [`render`](#render) method. However, lifecycle methods like `componentDidMount` or `componentWillUnmount` will not run on the server.

* When [Strict Mode](/reference/react/StrictMode) is on, React will call `constructor` twice in development and then throw away one of the instances. This helps you notice the accidental side effects that need to be moved out of the `constructor`.

<Note>

There is no exact equivalent for `constructor` in function components. To declare state in a function component, call [`useState`.](/reference/react/useState) To avoid recalculating the initial state, [pass a function to `useState`.](/reference/react/useState#avoiding-recreating-the-initial-state)

</Note>

---

### `componentDidCatch(error, info)` {/*componentdidcatch*/}

If you define `componentDidCatch`, React will call it when some child component (including distant children) throws an error during rendering. This lets you log that error to an error reporting service in production.

Typically, it is used together with [`static getDerivedStateFromError`](#static-getderivedstatefromerror) which lets you update state in response to an error and display an error message to the user. A component with these methods is called an *Error Boundary*.

[See an example.](#catching-rendering-errors-with-an-error-boundary)

#### Parameters {/*componentdidcatch-parameters*/}

* `error`: The error that was thrown. In practice, it will usually be an instance of [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) but this is not guaranteed because JavaScript allows to [`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw) any value, including strings or even `null`.

* `info`: An object containing additional information about the error. Its `componentStack` field contains a stack trace with the component that threw, as well as the names and source locations of all its parent components. In production, the component names will be minified. If you set up production error reporting, you can decode the component stack using sourcemaps the same way as you would do for regular JavaScript error stacks.

#### Returns {/*componentdidcatch-returns*/}

`componentDidCatch` should not return anything.

#### Caveats {/*componentdidcatch-caveats*/}

* In the past, it was common to call `setState` inside `componentDidCatch` in order to update the UI and display the fallback error message. This is deprecated in favor of defining [`static getDerivedStateFromError`.](#static-getderivedstatefromerror)

* Production and development builds of React slightly differ in the way `componentDidCatch` handles errors. In development, the errors will bubble up to `window`, which means that any `window.onerror` or `window.addEventListener('error', callback)` will intercept the errors that have been caught by `componentDidCatch`. In production, instead, the errors will not bubble up, which means any ancestor error handler will only receive errors not explicitly caught by `componentDidCatch`.

<Note>

There is no direct equivalent for `componentDidCatch` in function components yet. If you'd like to avoid creating class components, write a single `ErrorBoundary` component like above and use it throughout your app. Alternatively, you can use the [`react-error-boundary`](https://github.com/bvaughn/react-error-boundary) package which does that for you.

</Note>

---

### `componentDidMount()` {/*componentdidmount*/}

If you define the `componentDidMount` method, React will call it when your component is added *(mounted)* to the screen. This is a common place to start data fetching, set up subscriptions, or manipulate the DOM nodes.

If you implement `componentDidMount`, you usually need to implement other lifecycle methods to avoid bugs. For example, if `componentDidMount` reads some state or props, you also have to implement [`componentDidUpdate`](#componentdidupdate) to handle their changes, and [`componentWillUnmount`](#componentwillunmount) to clean up whatever `componentDidMount` was doing.

```js {6-8}
class ChatRoom extends Component {
  state = {
    serverUrl: 'https://localhost:1234'
  };

  componentDidMount() {
    this.setupConnection();
  }

  componentDidUpdate(prevProps, prevState) {
    if (
      this.props.roomId !== prevProps.roomId ||
      this.state.serverUrl !== prevState.serverUrl
    ) {
      this.destroyConnection();
      this.setupConnection();
    }
  }

  componentWillUnmount() {
    this.destroyConnection();
  }

  // ...
}
```

[See more examples.](#adding-lifecycle-methods-to-a-class-component)

#### Parameters {/*componentdidmount-parameters*/}

`componentDidMount` does not take any parameters.

#### Returns {/*componentdidmount-returns*/}

`componentDidMount` should not return anything.

#### Caveats {/*componentdidmount-caveats*/}

- When [Strict Mode](/reference/react/StrictMode) is on, in development React will call `componentDidMount`, then immediately call [`componentWillUnmount`,](#componentwillunmount) and then call `componentDidMount` again. This helps you notice if you forgot to implement `componentWillUnmount` or if its logic doesn't fully "mirror" what `componentDidMount` does.

- Although you may call [`setState`](#setstate) immediately in `componentDidMount`, it's best to avoid that when you can. It will trigger an extra rendering, but it will happen before the browser updates the screen. This guarantees that even though the [`render`](#render) will be called twice in this case, the user won't see the intermediate state. Use this pattern with caution because it often causes performance issues. In most cases, you should be able to assign the initial state in the [`constructor`](#constructor) instead. It can, however, be necessary for cases like modals and tooltips when you need to measure a DOM node before rendering something that depends on its size or position.

<Note>

For many use cases, defining `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` together in class components is equivalent to calling [`useEffect`](/reference/react/useEffect) in function components. In the rare cases where it's important for the code to run before browser paint, [`useLayoutEffect`](/reference/react/useLayoutEffect) is a closer match.

[See how to migrate.](#migrating-a-component-with-lifecycle-methods-from-a-class-to-a-function)

</Note>

---

### `componentDidUpdate(prevProps, prevState, snapshot?)` {/*componentdidupdate*/}

If you define the `componentDidUpdate` method, React will call it immediately after your component has been re-rendered with updated props or state.  This method is not called for the initial render.

You can use it to manipulate the DOM after an update. This is also a common place to do network requests as long as you compare the current props to previous props (e.g. a network request may not be necessary if the props have not changed). Typically, you'd use it together with [`componentDidMount`](#componentdidmount) and [`componentWillUnmount`:](#componentwillunmount)

```js {10-18}
class ChatRoom extends Component {
  state = {
    serverUrl: 'https://localhost:1234'
  };

  componentDidMount() {
    this.setupConnection();
  }

  componentDidUpdate(prevProps, prevState) {
    if (
      this.props.roomId !== prevProps.roomId ||
      this.state.serverUrl !== prevState.serverUrl
    ) {
      this.destroyConnection();
      this.setupConnection();
    }
  }

  componentWillUnmount() {
    this.destroyConnection();
  }

  // ...
}
```

[See more examples.](#adding-lifecycle-methods-to-a-class-component)

#### Parameters {/*componentdidupdate-parameters*/}

* `prevProps`: Props before the update. Compare `prevProps` to [`this.props`](#props) to determine what changed.

* `prevState`: State before the update. Compare `prevState` to [`this.state`](#state) to determine what changed.

* `snapshot`: If you implemented [`getSnapshotBeforeUpdate`](#getsnapshotbeforeupdate), `snapshot` will contain the value you returned from that method. Otherwise, it will be `undefined`.

#### Returns {/*componentdidupdate-returns*/}

`componentDidUpdate` should not return anything.

#### Caveats {/*componentdidupdate-caveats*/}

- `componentDidUpdate` will not get called if [`shouldComponentUpdate`](#shouldcomponentupdate) is defined and returns `false`.

- The logic inside `componentDidUpdate` should usually be wrapped in conditions comparing `this.props` with `prevProps`, and `this.state` with `prevState`. Otherwise, there's a risk of creating infinite loops.

- Although you may call [`setState`](#setstate) immediately in `componentDidUpdate`, it's best to avoid that when you can. It will trigger an extra rendering, but it will happen before the browser updates the screen. This guarantees that even though the [`render`](#render) will be called twice in this case, the user won't see the intermediate state. This pattern often causes performance issues, but it may be necessary for rare cases like modals and tooltips when you need to measure a DOM node before rendering something that depends on its size or position.

<Note>

For many use cases, defining `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` together in class components is equivalent to calling [`useEffect`](/reference/react/useEffect) in function components. In the rare cases where it's important for the code to run before browser paint, [`useLayoutEffect`](/reference/react/useLayoutEffect) is a closer match.

[See how to migrate.](#migrating-a-component-with-lifecycle-methods-from-a-class-to-a-function)

</Note>
---

### `componentWillMount()` {/*componentwillmount*/}

<Deprecated>

This API has been renamed from `componentWillMount` to [`UNSAFE_componentWillMount`.](#unsafe_componentwillmount) The old name has been deprecated. In a future major version of React, only the new name will work.

Run the [`rename-unsafe-lifecycles` codemod](https://github.com/reactjs/react-codemod#rename-unsafe-lifecycles) to automatically update your components.

</Deprecated>

---

### `componentWillReceiveProps(nextProps)` {/*componentwillreceiveprops*/}

<Deprecated>

This API has been renamed from `componentWillReceiveProps` to [`UNSAFE_componentWillReceiveProps`.](#unsafe_componentwillreceiveprops) The old name has been deprecated. In a future major version of React, only the new name will work.

Run the [`rename-unsafe-lifecycles` codemod](https://github.com/reactjs/react-codemod#rename-unsafe-lifecycles) to automatically update your components.

</Deprecated>

---

### `componentWillUpdate(nextProps, nextState)` {/*componentwillupdate*/}

<Deprecated>

This API has been renamed from `componentWillUpdate` to [`UNSAFE_componentWillUpdate`.](#unsafe_componentwillupdate) The old name has been deprecated. In a future major version of React, only the new name will work.

Run the [`rename-unsafe-lifecycles` codemod](https://github.com/reactjs/react-codemod#rename-unsafe-lifecycles) to automatically update your components.

</Deprecated>

---

### `componentWillUnmount()` {/*componentwillunmount*/}

If you define the `componentWillUnmount` method, React will call it before your component is removed *(unmounted)* from the screen. This is a common place to cancel data fetching or remove subscriptions.

The logic inside `componentWillUnmount` should "mirror" the logic inside [`componentDidMount`.](#componentdidmount) For example, if `componentDidMount` sets up a subscription, `componentWillUnmount` should clean up that subscription. If the cleanup logic in your `componentWillUnmount` reads some props or state, you will usually also need to implement [`componentDidUpdate`](#componentdidupdate) to clean up resources (such as subscriptions) corresponding to the old props and state.

```js {20-22}
class ChatRoom extends Component {
  state = {
    serverUrl: 'https://localhost:1234'
  };

  componentDidMount() {
    this.setupConnection();
  }

  componentDidUpdate(prevProps, prevState) {
    if (
      this.props.roomId !== prevProps.roomId ||
      this.state.serverUrl !== prevState.serverUrl
    ) {
      this.destroyConnection();
      this.setupConnection();
    }
  }

  componentWillUnmount() {
    this.destroyConnection();
  }

  // ...
}
```

[See more examples.](#adding-lifecycle-methods-to-a-class-component)

#### Parameters {/*componentwillunmount-parameters*/}

`componentWillUnmount` does not take any parameters.

#### Returns {/*componentwillunmount-returns*/}

`componentWillUnmount` should not return anything.

#### Caveats {/*componentwillunmount-caveats*/}

- When [Strict Mode](/reference/react/StrictMode) is on, in development React will call [`componentDidMount`,](#componentdidmount) then immediately call `componentWillUnmount`, and then call `componentDidMount` again. This helps you notice if you forgot to implement `componentWillUnmount` or if its logic doesn't fully "mirror" what `componentDidMount` does.

<Note>

For many use cases, defining `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` together in class components is equivalent to calling [`useEffect`](/reference/react/useEffect) in function components. In the rare cases where it's important for the code to run before browser paint, [`useLayoutEffect`](/reference/react/useLayoutEffect) is a closer match.

[See how to migrate.](#migrating-a-component-with-lifecycle-methods-from-a-class-to-a-function)

</Note>

---

### `forceUpdate(callback?)` {/*forceupdate*/}

Forces a component to re-render.

Usually, this is not necessary. If your component's [`render`](#render) method only reads from [`this.props`](#props), [`this.state`](#state), or [`this.context`,](#context) it will re-render automatically when you call [`setState`](#setstate) inside your component or one of its parents. However, if your component's `render` method reads directly from an external data source, you have to tell React to update the user interface when that data source changes. That's what `forceUpdate` lets you do.

Try to avoid all uses of `forceUpdate` and only read from `this.props` and `this.state` in `render`.

#### Parameters {/*forceupdate-parameters*/}

* **optional** `callback` If specified, React will call the `callback` you've provided after the update is committed.

#### Returns {/*forceupdate-returns*/}

`forceUpdate` does not return anything.

#### Caveats {/*forceupdate-caveats*/}

- If you call `forceUpdate`, React will re-render without calling [`shouldComponentUpdate`.](#shouldcomponentupdate)

<Note>

Reading an external data source and forcing class components to re-render in response to its changes with `forceUpdate` has been superseded by [`useSyncExternalStore`](/reference/react/useSyncExternalStore) in function components.

</Note>

---

### `getSnapshotBeforeUpdate(prevProps, prevState)` {/*getsnapshotbeforeupdate*/}

If you implement `getSnapshotBeforeUpdate`, React will call it immediately before React updates the DOM. It enables your component to capture some information from the DOM (e.g. scroll position) before it is potentially changed. Any value returned by this lifecycle method will be passed as a parameter to [`componentDidUpdate`.](#componentdidupdate)

For example, you can use it in a UI like a chat thread that needs to preserve its scroll position during updates:

```js {7-15,17}
class ScrollingList extends React.Component {
  constructor(props) {
    super(props);
    this.listRef = React.createRef();
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    // Are we adding new items to the list?
    // Capture the scroll position so we can adjust scroll later.
    if (prevProps.list.length < this.props.list.length) {
      const list = this.listRef.current;
      return list.scrollHeight - list.scrollTop;
    }
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    // If we have a snapshot value, we've just added new items.
    // Adjust scroll so these new items don't push the old ones out of view.
    // (snapshot here is the value returned from getSnapshotBeforeUpdate)
    if (snapshot !== null) {
      const list = this.listRef.current;
      list.scrollTop = list.scrollHeight - snapshot;
    }
  }

  render() {
    return (
      <div ref={this.listRef}>{/* ...contents... */}</div>
    );
  }
}
```

In the above example, it is important to read the `scrollHeight` property directly in `getSnapshotBeforeUpdate`. It is not safe to read it in [`render`](#render), [`UNSAFE_componentWillReceiveProps`](#unsafe_componentwillreceiveprops), or [`UNSAFE_componentWillUpdate`](#unsafe_componentwillupdate) because there is a potential time gap between these methods getting called and React updating the DOM.

#### Parameters {/*getsnapshotbeforeupdate-parameters*/}

* `prevProps`: Props before the update. Compare `prevProps` to [`this.props`](#props) to determine what changed.

* `prevState`: State before the update. Compare `prevState` to [`this.state`](#state) to determine what changed.

#### Returns {/*getsnapshotbeforeupdate-returns*/}

You should return a snapshot value of any type that you'd like, or `null`. The value you returned will be passed as the third argument to [`componentDidUpdate`.](#componentdidupdate)

#### Caveats {/*getsnapshotbeforeupdate-caveats*/}

- `getSnapshotBeforeUpdate` will not get called if [`shouldComponentUpdate`](#shouldcomponentupdate) is defined and returns `false`.

<Note>

At the moment, there is no equivalent to `getSnapshotBeforeUpdate` for function components. This use case is very uncommon, but if you have the need for it, for now you'll have to write a class component.

</Note>

---

### `render()` {/*render*/}

The `render` method is the only required method in a class component.

The `render` method should specify what you want to appear on the screen, for example:

```js {4-6}
import { Component } from 'react';

class Greeting extends Component {
  render() {
    return <h1>Hello, {this.props.name}!</h1>;
  }
}
```

React may call `render` at any moment, so you shouldn't assume that it runs at a particular time. Usually, the `render` method should return a piece of [JSX](/learn/writing-markup-with-jsx), but a few [other return types](#render-returns) (like strings) are supported. To calculate the returned JSX, the `render` method can read [`this.props`](#props), [`this.state`](#state), and [`this.context`](#context).

You should write the `render` method as a pure function, meaning that it should return the same result if props, state, and context are the same. It also shouldn't contain side effects (like setting up subscriptions) or interact with the browser APIs. Side effects should happen either in event handlers or methods like [`componentDidMount`.](#componentdidmount)

#### Parameters {/*render-parameters*/}

`render` does not take any parameters.

#### Returns {/*render-returns*/}

`render` can return any valid React node. This includes React elements such as `<div />`, strings, numbers, [portals](/reference/react-dom/createPortal), empty nodes (`null`, `undefined`, `true`, and `false`), and arrays of React nodes.

#### Caveats {/*render-caveats*/}

- `render` should be written as a pure function of props, state, and context. It should not have side effects.

- `render` will not get called if [`shouldComponentUpdate`](#shouldcomponentupdate) is defined and returns `false`.

- When [Strict Mode](/reference/react/StrictMode) is on, React will call `render` twice in development and then throw away one of the results. This helps you notice the accidental side effects that need to be moved out of the `render` method.

- There is no one-to-one correspondence between the `render` call and the subsequent `componentDidMount` or `componentDidUpdate` call. Some of the `render` call results may be discarded by React when it's beneficial.

---

### `setState(nextState, callback?)` {/*setstate*/}

Call `setState` to update the state of your React component.

```js {8-10}
class Form extends Component {
  state = {
    name: 'Taylor',
  };

  handleNameChange = (e) => {
    const newName = e.target.value;
    this.setState({
      name: newName
    });
  }

  render() {
    return (
      <>
        <input value={this.state.name} onChange={this.handleNameChange} />
