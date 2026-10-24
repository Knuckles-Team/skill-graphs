[Skip to main content](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#__docusaurus_skipToContent_fallback)
[![Redux Logo](https://redux.js.org/img/redux.svg) **Redux**](https://redux.js.org/)
[Getting Started](https://redux.js.org/introduction/getting-started)[Tutorial](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)[Usage Guide](https://redux.js.org/usage/)[API](https://redux.js.org/api/api-reference)[FAQ](https://redux.js.org/faq)[Best Practices](https://redux.js.org/style-guide/)[Need help?](https://redux.js.org/introduction/getting-started#help-and-discussion)
  * [Introduction](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
    * [Getting Started with Redux](https://redux.js.org/introduction/getting-started)
    * [Installation](https://redux.js.org/introduction/installation)
    * [Why Redux Toolkit is How To Use Redux Today](https://redux.js.org/introduction/why-rtk-is-redux-today)
    * [Core Concepts](https://redux.js.org/introduction/core-concepts)
    * [Learning Resources](https://redux.js.org/introduction/learning-resources)
    * [Ecosystem](https://redux.js.org/introduction/ecosystem)
    * [Examples](https://redux.js.org/introduction/examples)
  * [Tutorials](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
    * [Tutorials Index](https://redux.js.org/tutorials/index)
    * [Quick Start](https://redux.js.org/tutorials/quick-start)
    * [TypeScript Quick Start](https://redux.js.org/tutorials/typescript-quick-start)
    * [Redux Essentials](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
      * [Redux Overview and Concepts](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
      * [Redux Toolkit App Structure](https://redux.js.org/tutorials/essentials/part-2-app-structure)
      * [Basic Redux Data Flow](https://redux.js.org/tutorials/essentials/part-3-data-flow)
      * [Using Redux Data](https://redux.js.org/tutorials/essentials/part-4-using-data)
      * [Async Logic and Data Fetching](https://redux.js.org/tutorials/essentials/part-5-async-logic)
      * [Performance, Normalizing Data, and Reactive Logic](https://redux.js.org/tutorials/essentials/part-6-performance-normalization)
      * [RTK Query Basics](https://redux.js.org/tutorials/essentials/part-7-rtk-query-basics)
      * [RTK Query Advanced Patterns](https://redux.js.org/tutorials/essentials/part-8-rtk-query-advanced)
    * [Redux Fundamentals](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
    * [Videos](https://redux.js.org/tutorials/videos)
  * [Using Redux](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
  * [Understanding Redux](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
  * [FAQ](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
  * [Style Guide](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
  * [API Reference](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
  * [Redux Toolkit](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)


  * [](https://redux.js.org/)
  * Tutorials
  * Redux Essentials
  * Redux Overview and Concepts


On this page
# Redux Essentials, Part 1: Redux Overview and Concepts
  * What Redux is and why you might want to use it
  * Key Redux terms and concepts
  * How data flows through a Redux app


## Introduction[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#introduction "Direct link to Introduction")
Welcome to the Redux Essentials tutorial! **This tutorial will introduce you to Redux and teach you how to use it the right way, using our latest recommended tools and best practices**. By the time you finish, you should be able to start building your own Redux applications using the tools and patterns you've learned here.
In Part 1 of this tutorial, we'll cover the key concepts and terms you need to know to use Redux, and in [Part 2: Redux App Structure](https://redux.js.org/tutorials/essentials/part-2-app-structure) we'll examine a typical React + Redux app to see how the pieces fit together.
Starting in [Part 3: Basic Redux Data Flow](https://redux.js.org/tutorials/essentials/part-3-data-flow), we'll use that knowledge to build a small social media feed app with some real-world features, see how those pieces actually work in practice, and talk about some important patterns and guidelines for using Redux.
### How to Read This Tutorial[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#how-to-read-this-tutorial "Direct link to How to Read This Tutorial")
This tutorial focuses on showing you _how_ to use Redux the right way, and explains concepts along the way so that you can understand how to build Redux apps correctly.
We've tried to keep these explanations beginner-friendly, but we do need to make some assumptions about what you know already:
  * Familiarity with
  * Familiarity with
  * Knowledge of React terminology:
  * Knowledge of
  * Basic understanding of


**If you're not already comfortable with those topics, we encourage you to take some time to become comfortable with them first, and then come back to learn about Redux**. We'll be here when you're ready!
You should also make sure that you have the React and Redux DevTools extensions installed in your browser:
  * React DevTools Extension:
  * Redux DevTools Extension:


## What is Redux?[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#what-is-redux "Direct link to What is Redux?")
It helps to understand what this "Redux" thing is in the first place. What does it do? What problems does it help me solve? Why would I want to use it?
**Redux is a pattern and library for managing and updating global application state, where the UI triggers events called "actions" to describe what happened, and separate update logic called "reducers" updates the state in response.** It serves as a centralized store for state that needs to be used across your entire application, with rules ensuring that the state can only be updated in a predictable fashion.
### Why Should I Use Redux?[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#why-should-i-use-redux "Direct link to Why Should I Use Redux?")
Redux helps you manage "global" state - state that is needed across many parts of your application.
**The patterns and tools provided by Redux make it easier to understand when, where, why, and how the state in your application is being updated, and how your application logic will behave when those changes occur**. Redux guides you towards writing code that is predictable and testable, which helps give you confidence that your application will work as expected.
### When Should I Use Redux?[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#when-should-i-use-redux "Direct link to When Should I Use Redux?")
Redux helps you deal with shared state management, but like any tool, it has tradeoffs. There are more concepts to learn, and more code to write. It also adds some indirection to your code, and asks you to follow certain restrictions. It's a trade-off between short term and long term productivity.
Redux is more useful when:
  * You have large amounts of application state that are needed in many places in the app
  * The app state is updated frequently over time
  * The logic to update that state may be complex
  * The app has a medium or large-sized codebase, and might be worked on by many people


**Not all apps need Redux. Take some time to think about the kind of app you're building, and decide what tools would be best to help solve the problems you're working on.**
If you're not sure whether Redux is a good choice for your app, these resources give some more guidance:
  * **[Redux FAQ: When should I use Redux?](https://redux.js.org/faq/general#when-should-i-use-redux)**


### Redux Libraries and Tools[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-libraries-and-tools "Direct link to Redux Libraries and Tools")
Redux at its core is a small standalone JS library. It is commonly used with several other packages:
#### Redux Toolkit[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-toolkit "Direct link to Redux Toolkit")
[**Redux Toolkit**](https://redux-toolkit.js.org) is our recommended approach for writing Redux logic. It contains packages and functions that we think are essential for building a Redux app. Redux Toolkit builds in our suggested best practices, simplifies most Redux tasks, prevents common mistakes, and makes it easier to write Redux applications.
#### React-Redux[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#react-redux "Direct link to React-Redux")
Redux can integrate with any UI framework, and is most frequently used with React. [**React-Redux**](https://react-redux.js.org/) is our official package that lets your React components interact with a Redux store by reading pieces of state and dispatching actions to update the store.
#### Redux DevTools Extension[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-devtools-extension "Direct link to Redux DevTools Extension")
The
## Redux Terms and Concepts[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-terms-and-concepts "Direct link to Redux Terms and Concepts")
Before we dive into some actual code, let's talk about some of the terms and concepts you'll need to know to use Redux.
### State Management[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#state-management "Direct link to State Management")
Let's start by looking at a small React counter component. It tracks a number in component state, and increments the number when a button is clicked:
```
function Counter() {
  // State: a counter value
  const [counter, setCounter] = useState(0)

  // Action: code that causes an update to the state when something happens
  const increment = () => {
    setCounter(prevCounter => prevCounter + 1)
  }

  // View: the UI definition
  return (
    <div>
      Value: {counter} <button onClick={increment}>Increment</button>
    </div>
  )
}

```

It is a self-contained app with the following parts:
  * The **state** , the source of truth that drives our app
  * The **view** , a declarative description of the UI based on the current state
  * The **actions** , the events that occur in the app based on user input, and trigger updates in the state


This is a small example of **"one-way data flow"** :
  * State describes the condition of the app at a specific point in time
  * The UI is rendered based on that state
  * When something happens (such as a user clicking a button), the state is updated based on what occurred
  * The UI re-renders based on the new state


![One-way data flow](https://redux.js.org/assets/images/one-way-data-flow-04fe46332c1ccb3497ecb04b94e55b97.png)
However, the simplicity can break down when we have **multiple components that need to share and use the same state** , especially if those components are located in different parts of the application. Sometimes this can be solved by
One way to solve this is to extract the shared state from the components, and put it into a centralized location outside the component tree. With this, our component tree becomes a big "view", and any component can access the state or trigger actions, no matter where they are in the tree!
By defining and separating the concepts involved in state management and enforcing rules that maintain independence between views and states, we give our code more structure and maintainability.
This is the basic idea behind Redux: a single centralized place to contain the global state in your application, and specific patterns to follow when updating that state to make the code predictable.
### Immutability[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#immutability "Direct link to Immutability")
"Mutable" means "changeable". If something is "immutable", it can never be changed.
JavaScript objects and arrays are all mutable by default. If I create an object, I can change the contents of its fields. If I create an array, I can change the contents as well:
```
const obj = { a: 1, b: 2 }
// still the same object outside, but the contents have changed
obj.b = 3

const arr = ['a', 'b']
// In the same way, we can change the contents of this array
arr.push('c')
arr[1] = 'd'

```

This is called _mutating_ the object or array. It's the same object or array reference in memory, but now the contents inside the object have changed.
**In order to update values immutably, your code must make _copies_ of existing objects/arrays, and then modify the copies**.
We can do this by hand using JavaScript's array / object spread operators, as well as array methods that return new copies of the array instead of mutating the original array:
```
const obj = {
  a: {
    // To safely update obj.a.c, we have to copy each piece
    c: 3
  },
  b: 2
}

const obj2 = {
  // copy obj
  ...obj,
  // overwrite a
  a: {
    // copy obj.a
    ...obj.a,
    // overwrite c
    c: 42
  }
}

const arr = ['a', 'b']
// Create a new copy of arr, with "c" appended to the end
const arr2 = arr.concat('c')

// or, we can make a copy of the original array:
const arr3 = arr.slice()
// and mutate the copy:
arr3.push('c')

```

**React and Redux expect that all state updates are done immutably**. We'll look at where and how this is important a bit later, as well as some easier ways to write immutable update logic.
For more info on how immutability works in JavaScript, see:
### Terminology[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#terminology "Direct link to Terminology")
There are some important Redux terms that you'll need to be familiar with before we continue:
#### Actions[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#actions "Direct link to Actions")
An **action** is a plain JavaScript object that has a `type` field. **You can think of an action as an event that describes something that happened in the application**.
The `type` field should be a string that gives this action a descriptive name, like `"todos/todoAdded"`. We usually write that type string like `"domain/eventName"`, where the first part is the feature or category that this action belongs to, and the second part is the specific thing that happened.
An action object can have other fields with additional information about what happened. By convention, we put that information in a field called `payload`.
A typical action object might look like this:
```
const addTodoAction = {
  type: 'todos/todoAdded',
  payload: 'Buy milk'
}

```

#### Action Creators[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#action-creators "Direct link to Action Creators")
An **action creator** is a function that creates and returns an action object. We typically use these so we don't have to write the action object by hand every time:
```
const addTodo = text => {
  return {
    type: 'todos/todoAdded',
    payload: text
  }
}

```

#### Reducers[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#reducers "Direct link to Reducers")
A **reducer** is a function that receives the current `state` and an `action` object, decides how to update the state if necessary, and returns the new state: `(state, action) => newState`. **You can think of a reducer as an event listener which handles events based on the received action (event) type.**
"Reducer" functions get their name because they're similar to the kind of callback function you pass to the
Reducers must _always_ follow some specific rules:
  * They should only calculate the new state value based on the `state` and `action` arguments
  * They are not allowed to modify the existing `state`. Instead, they must make _immutable updates_ , by copying the existing `state` and making changes to the copied values.
  * They must be "pure" - they cannot do any asynchronous logic, calculate random values, or cause other "side effects"


We'll talk more about the rules of reducers later, including why they're important and how to follow them correctly.
The logic inside reducer functions typically follows the same series of steps:
  * Check to see if the reducer cares about this action
    * If so, make a copy of the state, update the copy with new values, and return it
  * Otherwise, return the existing state unchanged


Here's a small example of a reducer, showing the steps that each reducer should follow:
```
const initialState = { value: 0 }

function counterReducer(state = initialState, action) {
  // Check to see if the reducer cares about this action
  if (action.type === 'counter/increment') {
    // If so, make a copy of `state`
    return {
      ...state,
      // and update the copy with the new value
      value: state.value + 1
    }
  }
  // otherwise return the existing state unchanged
  return state
}

```

Reducers can use any kind of logic inside to decide what the new state should be: `if/else`, `switch`, loops, and so on.
#### Detailed Explanation: Why Are They Called 'Reducers?'
The
`Array.reduce()` takes a callback function as an argument, which will be called one time for each item in the array. It takes two arguments:
  * `previousResult`, the value that your callback returned last time
  * `currentItem`, the current item in the array


The first time that the callback runs, there isn't a `previousResult` available, so we need to also pass in an initial value that will be used as the first `previousResult`.
If we wanted to add together an array of numbers to find out what the total is, we could write a reduce callback that looks like this:
```
const numbers = [2, 5, 8]

const addNumbers = (previousResult, currentItem) => {
  console.log({ previousResult, currentItem })
  return previousResult + currentItem
}

const initialValue = 0

const total = numbers.reduce(addNumbers, initialValue)
// {previousResult: 0, currentItem: 2}
// {previousResult: 2, currentItem: 5}
// {previousResult: 7, currentItem: 8}

console.log(total)
// 15

```

Notice that this `addNumbers` "reduce callback" function doesn't need to keep track of anything itself. It takes the `previousResult` and `currentItem` arguments, does something with them, and returns a new result value.
**A Redux reducer function is exactly the same idea as this "reduce callback" function!** It takes a "previous result" (the `state`), and the "current item" (the `action` object), decides a new state value based on those arguments, and returns that new state.
If we were to create an array of Redux actions, call `reduce()`, and pass in a reducer function, we'd get a final result the same way:
```
const actions = [
  { type: 'counter/increment' },
  { type: 'counter/increment' },
  { type: 'counter/increment' }
]

const initialState = { value: 0 }

const finalResult = actions.reduce(counterReducer, initialState)
console.log(finalResult)
// {value: 3}

```

We can say that **Redux reducers reduce a set of actions (over time) into a single state**. The difference is that with `Array.reduce()` it happens all at once, and with Redux, it happens over the lifetime of your running app.
#### Store[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#store "Direct link to Store")
The current Redux application state lives in an object called the **store** .
The store is created by passing in a reducer, and has a method called `getState` that returns the current state value:
```
import { configureStore } from '@reduxjs/toolkit'

const store = configureStore({ reducer: counterReducer })

console.log(store.getState())
// {value: 0}

```

#### Dispatch[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#dispatch "Direct link to Dispatch")
The Redux store has a method called `dispatch`. **The only way to update the state is to call`store.dispatch()` and pass in an action object**. The store will run its reducer function and save the new state value inside, and we can call `getState()` to retrieve the updated value:
```
store.dispatch({ type: 'counter/increment' })

console.log(store.getState())
// {value: 1}

```

**You can think of dispatching actions as "triggering an event"** in the application. Something happened, and we want the store to know about it. Reducers act like event listeners, and when they hear an action they are interested in, they update the state in response.
We typically call action creators to dispatch the right action:
```
const increment = () => {
  return {
    type: 'counter/increment'
  }
}

store.dispatch(increment())

console.log(store.getState())
// {value: 2}

```

#### Selectors[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#selectors "Direct link to Selectors")
**Selectors** are functions that know how to extract specific pieces of information from a store state value. As an application grows bigger, this can help avoid repeating logic as different parts of the app need to read the same data:
```
const selectCounterValue = state => state.value

const currentValue = selectCounterValue(store.getState())
console.log(currentValue)
// 2

```

### Redux Application Data Flow[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-application-data-flow "Direct link to Redux Application Data Flow")
Earlier, we talked about "one-way data flow", which describes this sequence of steps to update the app:
  * State describes the condition of the app at a specific point in time
  * The UI is rendered based on that state
  * When something happens (such as a user clicking a button), the state is updated based on what occurred
  * The UI re-renders based on the new state


For Redux specifically, we can break these steps into more detail:
  * Initial setup:
    * A Redux store is created using a root reducer function
    * The store calls the root reducer once, and saves the return value as its initial `state`
    * When the UI is first rendered, UI components access the current state of the Redux store, and use that data to decide what to render. They also subscribe to any future store updates so they can know if the state has changed.
  * Updates:
    * Something happens in the app, such as a user clicking a button
    * The app code dispatches an action to the Redux store, like `dispatch({type: 'counter/increment'})`
    * The store runs the reducer function again with the previous `state` and the current `action`, and saves the return value as the new `state`
    * The store notifies all parts of the UI that are subscribed that the store has been updated
    * Each UI component that needs data from the store checks to see if the parts of the state they need have changed.
    * Each component that sees its data has changed forces a re-render with the new data, so it can update what's shown on the screen


Here's what that data flow looks like visually:
![Redux data flow diagram](https://redux.js.org/assets/images/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif)
## What You've Learned[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#what-youve-learned "Direct link to What You've Learned")
Redux does have a number of new terms and concepts to remember. As a reminder, here's what we just covered:
  * **Redux is a library for managing global application state**
    * Redux is typically used with the React-Redux library for integrating Redux and React together
    * Redux Toolkit is the standard way to write Redux logic
  * **Redux's update pattern separates "what happened" from "how the state changes"**
    * _Actions_ are plain objects with a `type` field, and describe "what happened" in the app
    * _Reducers_ are functions that calculate a new state value based on previous state + an action
    * A Redux _store_ runs the root reducer whenever an action is _dispatched_
  * **Redux uses a "one-way data flow" app structure**
    * State describes the condition of the app at a point in time, and UI renders based on that state
    * When something happens in the app:
      * The UI dispatches an action
      * The store runs the reducers, and the state is updated based on what occurred
      * The store notifies the UI that the state has changed
    * The UI re-renders based on the new state


## What's Next?[​](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#whats-next "Direct link to What's Next?")
We've seen each of the individual pieces of a Redux app. Next, continue on to [Part 2: Redux Toolkit App Structure](https://redux.js.org/tutorials/essentials/part-2-app-structure), where we'll look at a full working example to see how the pieces fit together.
Last updated on **Aug 29, 2024**
[ Previous TypeScript Quick Start](https://redux.js.org/tutorials/typescript-quick-start)[Next Redux Toolkit App Structure](https://redux.js.org/tutorials/essentials/part-2-app-structure)
  * [Introduction](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#introduction)
    * [How to Read This Tutorial](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#how-to-read-this-tutorial)
  * [What is Redux?](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#what-is-redux)
    * [Why Should I Use Redux?](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#why-should-i-use-redux)
    * [When Should I Use Redux?](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#when-should-i-use-redux)
    * [Redux Libraries and Tools](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-libraries-and-tools)
      * [Redux Toolkit](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-toolkit)
      * [React-Redux](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#react-redux)
      * [Redux DevTools Extension](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-devtools-extension)
  * [Redux Terms and Concepts](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-terms-and-concepts)
    * [State Management](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#state-management)
    * [Immutability](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#immutability)
    * [Terminology](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#terminology)
      * [Actions](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#actions)
      * [Action Creators](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#action-creators)
      * [Reducers](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#reducers)
      * [Store](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#store)
      * [Dispatch](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#dispatch)
      * [Selectors](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#selectors)
    * [Redux Application Data Flow](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#redux-application-data-flow)
  * [What You've Learned](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#what-youve-learned)
  * [What's Next?](https://redux.js.org/tutorials/essentials/part-1-overview-concepts#whats-next)


Docs
  * [Getting Started](https://redux.js.org/introduction/getting-started)
  * [Usage Guide](https://redux.js.org/usage)
  * [Tutorial](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
  * [FAQ](https://redux.js.org/faq)
  * [API Reference](https://redux.js.org/api/api-reference)


Community
  * [Feedback](https://redux.js.org/introduction/getting-started#help-and-discussion)


More
[![Redux Logo](https://redux.js.org/img/redux.svg)](https://redux.js.org/)
Copyright © 2015–2026 Dan Abramov and the Redux documentation authors.
