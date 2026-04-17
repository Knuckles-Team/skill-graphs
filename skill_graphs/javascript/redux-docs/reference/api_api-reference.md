[Skip to main content](https://redux.js.org/api/applymiddleware#__docusaurus_skipToContent_fallback)
[![Redux Logo](https://redux.js.org/img/redux.svg) **Redux**](https://redux.js.org/)
[Getting Started](https://redux.js.org/introduction/getting-started)[Tutorial](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)[Usage Guide](https://redux.js.org/usage/)[API](https://redux.js.org/api/api-reference)[FAQ](https://redux.js.org/faq)[Best Practices](https://redux.js.org/style-guide/)[Need help?](https://redux.js.org/introduction/getting-started#help-and-discussion)
  * [Introduction](https://redux.js.org/api/applymiddleware)
  * [Tutorials](https://redux.js.org/api/applymiddleware)
  * [Using Redux](https://redux.js.org/api/applymiddleware)
  * [Understanding Redux](https://redux.js.org/api/applymiddleware)
  * [FAQ](https://redux.js.org/api/applymiddleware)
  * [Style Guide](https://redux.js.org/api/applymiddleware)
  * [API Reference](https://redux.js.org/api/applymiddleware)
    * [API Reference](https://redux.js.org/api/api-reference)
    * [createStore](https://redux.js.org/api/createstore)
    * [Store](https://redux.js.org/api/store)
    * [combineReducers](https://redux.js.org/api/combinereducers)
    * [applyMiddleware](https://redux.js.org/api/applymiddleware)
    * [bindActionCreators](https://redux.js.org/api/bindactioncreators)
    * [compose](https://redux.js.org/api/compose)
    * [Additional Utilities](https://redux.js.org/api/utils)
    * [Error Messages](https://redux.js.org/errors)
  * [Redux Toolkit](https://redux.js.org/api/applymiddleware)


  * [](https://redux.js.org/)
  * API Reference
  * applyMiddleware


On this page
# `applyMiddleware(...middleware)`
## Overview[​](https://redux.js.org/api/applymiddleware#overview "Direct link to Overview")
Middleware is the suggested way to extend Redux with custom functionality. Middleware lets you wrap the store's [`dispatch`](https://redux.js.org/api/store#dispatchaction) method for fun and profit. The key feature of middleware is that it is composable. Multiple middleware can be combined together, where each middleware requires no knowledge of what comes before or after it in the chain.
You shouldn't have to call `applyMiddleware` directly. Redux Toolkit's [`configureStore` method](https://redux-toolkit.js.org/api/configureStore) automatically adds a default set of middleware to the store, or can accept a list of middleware to add.
The most common use case for middleware is to support asynchronous actions without much boilerplate code or a dependency on a library like [async actions](https://redux.js.org/understanding/thinking-in-redux/glossary#async-action) in addition to normal actions.
For example, [`dispatch`](https://redux.js.org/api/store#dispatchaction) as an argument and may call it asynchronously. Such functions are called _thunks_. Another example of middleware is
The original Redux [`createStore`](https://redux.js.org/api/createstore) method does not understand what middleware are out of the box - it has to be configured with `applyMiddleware` to add that behavior. However, Redux Toolkit's [`configureStore` method](https://redux-toolkit.js.org/api/configureStore) automatically adds middleware support by default.
## Arguments[​](https://redux.js.org/api/applymiddleware#arguments "Direct link to Arguments")
  * `...middleware` (_arguments_): Functions that conform to the Redux _middleware API_. Each middleware receives [`Store`](https://redux.js.org/api/store)'s [`dispatch`](https://redux.js.org/api/store#dispatchaction) and [`getState`](https://redux.js.org/api/store#getstate) functions as named arguments, and returns a function. That function will be given the `next` middleware's dispatch method, and is expected to return a function of `action` calling `next(action)` with a potentially different argument, or at a different time, or maybe not calling it at all. The last middleware in the chain will receive the real store's [`dispatch`](https://redux.js.org/api/store#dispatchaction) method as the `next` parameter, thus ending the chain. So, the middleware signature is `({ getState, dispatch }) => next => action`.


### Returns[​](https://redux.js.org/api/applymiddleware#returns "Direct link to Returns")
(_Function_) A store enhancer that applies the given middleware. The store enhancer signature is `createStore => createStore` but the easiest way to apply it is to pass it to [`createStore()`](https://redux.js.org/api/createstore) as the last `enhancer` argument.
## Examples[​](https://redux.js.org/api/applymiddleware#examples "Direct link to Examples")
#### Example: Custom Logger Middleware[​](https://redux.js.org/api/applymiddleware#example-custom-logger-middleware "Direct link to Example: Custom Logger Middleware")
```
import { createStore, applyMiddleware } from 'redux'
import todos from './reducers'

function logger({ getState }) {
  return next => action => {
    console.log('will dispatch', action)

    // Call the next dispatch method in the middleware chain.
    const returnValue = next(action)

    console.log('state after dispatch', getState())

    // This will likely be the action itself, unless
    // a middleware further in chain changed it.
    return returnValue
  }
}

const store = createStore(todos, ['Use Redux'], applyMiddleware(logger))

store.dispatch({
  type: 'ADD_TODO',
  text: 'Understand the middleware'
})
// (These lines will be logged by the middleware:)
// will dispatch: { type: 'ADD_TODO', text: 'Understand the middleware' }
// state after dispatch: [ 'Use Redux', 'Understand the middleware' ]

```

#### Example: Using Thunk Middleware for Async Actions[​](https://redux.js.org/api/applymiddleware#example-using-thunk-middleware-for-async-actions "Direct link to Example: Using Thunk Middleware for Async Actions")
```
import { createStore, combineReducers, applyMiddleware } from 'redux'
import { thunk } from 'redux-thunk'
import * as reducers from './reducers'

const reducer = combineReducers(reducers)
// applyMiddleware supercharges createStore with middleware:
const store = createStore(reducer, applyMiddleware(thunk))

function fetchSecretSauce() {
  return fetch('https://www.google.com/search?q=secret+sauce')
}

// These are the normal action creators you have seen so far.
// The actions they return can be dispatched without any middleware.
// However, they only express “facts” and not the “async flow”.
function makeASandwich(forPerson, secretSauce) {
  return {
    type: 'MAKE_SANDWICH',
    forPerson,
    secretSauce
  }
}

function apologize(fromPerson, toPerson, error) {
  return {
    type: 'APOLOGIZE',
    fromPerson,
    toPerson,
    error
  }
}

function withdrawMoney(amount) {
  return {
    type: 'WITHDRAW',
    amount
  }
}

// Even without middleware, you can dispatch an action:
store.dispatch(withdrawMoney(100))

// But what do you do when you need to start an asynchronous action,
// such as an API call, or a router transition?

// Meet thunks.
// A thunk is a function that returns a function.
// This is a thunk.
function makeASandwichWithSecretSauce(forPerson) {
  // Invert control!
  // Return a function that accepts `dispatch` so we can dispatch later.
  // Thunk middleware knows how to turn thunk async actions into actions.
  return function (dispatch) {
    return fetchSecretSauce().then(
      sauce => dispatch(makeASandwich(forPerson, sauce)),
      error => dispatch(apologize('The Sandwich Shop', forPerson, error))
    )
  }
}

// Thunk middleware lets me dispatch thunk async actions
// as if they were actions!
store.dispatch(makeASandwichWithSecretSauce('Me'))

// It even takes care to return the thunk's return value
// from the dispatch, so I can chain Promises as long as I return them.
store.dispatch(makeASandwichWithSecretSauce('My wife')).then(() => {
  console.log('Done!')
})

// In fact I can write action creators that dispatch
// actions and async actions from other action creators,
// and I can build my control flow with Promises.
function makeSandwichesForEverybody() {
  return function (dispatch, getState) {
    if (!getState().sandwiches.isShopOpen) {
      // You don't have to return Promises, but it's a handy convention
      // so the caller can always call .then() on async dispatch result.
      return Promise.resolve()
    }

    // We can dispatch both plain object actions and other thunks,
    // which lets us compose the asynchronous actions in a single flow.
    return dispatch(makeASandwichWithSecretSauce('My Grandma'))
      .then(() =>
        Promise.all([
          dispatch(makeASandwichWithSecretSauce('Me')),
          dispatch(makeASandwichWithSecretSauce('My wife'))
        ])
      )
      .then(() => dispatch(makeASandwichWithSecretSauce('Our kids')))
      .then(() =>
        dispatch(
          getState().myMoney > 42
            ? withdrawMoney(42)
            : apologize('Me', 'The Sandwich Shop')
        )
      )
  }
}

// This is very useful for server side rendering, because I can wait
// until data is available, then synchronously render the app.

import { renderToString } from 'react-dom/server'

store
  .dispatch(makeSandwichesForEverybody())
  .then(() => response.send(renderToString(<MyApp store={store} />)))

// I can also dispatch a thunk async action from a component
// any time its props change to load the missing data.

import React from 'react'
import { connect } from 'react-redux'

function SandwichShop(props) {
  const { dispatch, forPerson } = props

  useEffect(() => {
    dispatch(makeASandwichWithSecretSauce(forPerson))
  }, [forPerson])

  return <p>{this.props.sandwiches.join('mustard')}</p>
}

export default connect(state => ({
  sandwiches: state.sandwiches
}))(SandwichShop)

```

## Tips[​](https://redux.js.org/api/applymiddleware#tips "Direct link to Tips")
  * Middleware only wraps the store's [`dispatch`](https://redux.js.org/api/store#dispatchaction) function. Technically, anything a middleware can do, you can do manually by wrapping every `dispatch` call, but it's easier to manage this in a single place and define action transformations on the scale of the whole project.
  * If you use other store enhancers in addition to `applyMiddleware`, make sure to put `applyMiddleware` before them in the composition chain because the middleware is potentially asynchronous. For example, it should go before
  * If you want to conditionally apply a middleware, make sure to only import it when it's needed:
```
let middleware = [a, b]
if (process.env.NODE_ENV !== 'production') {
  const c = require('some-debug-middleware')
  const d = require('another-debug-middleware')
  middleware = [...middleware, c, d]
}

const store = createStore(
  reducer,
  preloadedState,
  applyMiddleware(...middleware)
)

```

This makes it easier for bundling tools to cut out unneeded modules and reduces the size of your builds.
  * Ever wondered what `applyMiddleware` itself is? It ought to be an extension mechanism more powerful than the middleware itself. Indeed, `applyMiddleware` is an example of the most powerful Redux extension mechanism called [store enhancers](https://redux.js.org/understanding/thinking-in-redux/glossary#store-enhancer). It is highly unlikely you'll ever want to write a store enhancer yourself. Another example of a store enhancer is
  * Middleware sounds much more complicated than it really is. The only way to really understand middleware is to see how the existing middleware works, and try to write your own. The function nesting can be intimidating, but most of the middleware you'll find are, in fact, 10-liners, and the nesting and composability is what makes the middleware system powerful.
  * To apply multiple store enhancers, you may use [`compose()`](https://redux.js.org/api/compose).


Last updated on **Apr 21, 2025**
[ Previous combineReducers](https://redux.js.org/api/combinereducers)[Next bindActionCreators](https://redux.js.org/api/bindactioncreators)
  * [Overview](https://redux.js.org/api/applymiddleware#overview)
  * [Arguments](https://redux.js.org/api/applymiddleware#arguments)
    * [Returns](https://redux.js.org/api/applymiddleware#returns)
  * [Examples](https://redux.js.org/api/applymiddleware#examples)
    * [Example: Custom Logger Middleware](https://redux.js.org/api/applymiddleware#example-custom-logger-middleware)
    * [Example: Using Thunk Middleware for Async Actions](https://redux.js.org/api/applymiddleware#example-using-thunk-middleware-for-async-actions)
  * [Tips](https://redux.js.org/api/applymiddleware#tips)


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
