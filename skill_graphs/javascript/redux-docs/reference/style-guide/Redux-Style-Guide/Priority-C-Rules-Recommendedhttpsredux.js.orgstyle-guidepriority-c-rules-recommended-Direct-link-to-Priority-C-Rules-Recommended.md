## Priority C Rules: Recommended[​](https://redux.js.org/style-guide#priority-c-rules-recommended "Direct link to Priority C Rules: Recommended")
### Write Action Types as `domain/eventName`[​](https://redux.js.org/style-guide#write-action-types-as-domaineventname "Direct link to write-action-types-as-domaineventname")
The original Redux docs and examples generally used a "SCREAMING_SNAKE_CASE" convention for defining action types, such as `"ADD_TODO"` and `"INCREMENT"`. This matches typical conventions in most programming languages for declaring constant values. The downside is that the uppercase strings can be hard to read.
Other communities have adopted other conventions, usually with some indication of the "feature" or "domain" the action is related to, and the specific action type. The NgRx community typically uses a pattern like `"[Domain] Action Type"`, such as `"[Login Page] Login"`. Other patterns like `"domain:action"` have been used as well.
Redux Toolkit's `createSlice` function currently generates action types that look like `"domain/action"`, such as `"todos/addTodo"`. Going forward, **we suggest using the`"domain/action"` convention for readability**.
### Write Actions Using the Flux Standard Action Convention[​](https://redux.js.org/style-guide#write-actions-using-the-flux-standard-action-convention "Direct link to Write Actions Using the Flux Standard Action Convention")
The original "Flux Architecture" documentation only specified that action objects should have a `type` field, and did not give any further guidance on what kinds of fields or naming conventions should be used for fields in actions. To provide consistency, Andrew Clark created a convention called
  * Should always put their data into a `payload` field
  * May have a `meta` field for additional info
  * May have an `error` field to indicate the action represents a failure of some kind


Many libraries in the Redux ecosystem have adopted the FSA convention, and Redux Toolkit generates action creators that match the FSA format.
**Prefer using FSA-formatted actions for consistency**.
> **Note** : The FSA spec says that "error" actions should set `error: true`, and use the same action type as the "valid" form of the action. In practice, most developers write separate action types for the "success" and "error" cases. Either is acceptable.
### Use Action Creators[​](https://redux.js.org/style-guide#use-action-creators "Direct link to Use Action Creators")
"Action creator" functions started with the original "Flux Architecture" approach. With Redux, action creators are not strictly required. Components and other logic can always call `dispatch({type: "some/action"})` with the action object written inline.
However, using action creators provides consistency, especially in cases where some kind of preparation or additional logic is needed to fill in the contents of the action (such as generating a unique ID).
**Prefer using action creators for dispatching any actions**. However, rather than writing action creators by hand, **we recommend using the`createSlice` function from Redux Toolkit, which will generate action creators and action types automatically**.
### Use RTK Query for Data Fetching[​](https://redux.js.org/style-guide#use-rtk-query-for-data-fetching "Direct link to Use RTK Query for Data Fetching")
In practice, **the single most common use case for side effects in a typical Redux app is fetching and caching data from the server**.
Because of this, **we recommend using[RTK Query](https://redux.js.org/tutorials/essentials/part-7-rtk-query-basics) as the default approach for data fetching and caching in a Redux app**. RTK Query has been designed to correctly manage the logic for fetching data from the server as needed, caching it, deduplicating requests, updating components, and much more. We recommend _against_ writing data fetching logic by hand in almost all cases.
### Use Thunks and Listeners for Other Async Logic[​](https://redux.js.org/style-guide#use-thunks-and-listeners-for-other-async-logic "Direct link to Use Thunks and Listeners for Other Async Logic")
Redux was designed to be extensible, and the middleware API was specifically created to allow different forms of async logic to be plugged into the Redux store. That way, users wouldn't be forced to learn a specific library like RxJS if it wasn't appropriate for their needs.
This led to a wide variety of Redux async middleware addons being created, and that in turn has caused confusion and questions over which async middleware should be used.
**We recommend using[the Redux thunk middleware](https://redux.js.org/usage/writing-logic-thunks) for imperative logic**, such as complex sync logic that needs access to `dispatch` or `getState`, and moderately complex async logic. This includes use cases like moving logic out of components.
**We recommend using[the RTK "listener" middleware"](https://redux-toolkit.js.org/api/createListenerMiddleware) for "reactive" logic that needs to respond to dispatched actions or state changes**, such as longer-running async workflows and "background thread"-type behavior.
We recommend _against_ using the more complex Redux-Saga and Redux-Observable libraries in most cases, especially for async data fetching. Only use these libraries if no other tool is powerful enough to handle your use case.
### Move Complex Logic Outside Components[​](https://redux.js.org/style-guide#move-complex-logic-outside-components "Direct link to Move Complex Logic Outside Components")
We have traditionally suggested keeping as much logic as possible outside components. That was partly due to encouraging the "container/presentational" pattern, where many components simply accept data as props and display UI accordingly, but also because dealing with async logic in class component lifecycle methods can become difficult to maintain.
**We still encourage moving complex synchronous or async logic outside components, usually into thunks**. This is especially true if the logic needs to read from the store state.
However, **the use of React hooks does make it somewhat easier to manage logic like data fetching directly inside a component** , and this may replace the need for thunks in some cases.
### Use Selector Functions to Read from Store State[​](https://redux.js.org/style-guide#use-selector-functions-to-read-from-store-state "Direct link to Use Selector Functions to Read from Store State")
"Selector functions" are a powerful tool for encapsulating reading values from the Redux store state and deriving further data from those values. In addition, libraries like Reselect enable creating memoized selector functions that only recalculate results when the inputs have changed, which is an important aspect of optimizing performance.
**We strongly recommend using memoized selector functions for reading store state whenever possible** , and recommend creating those selectors with Reselect.
However, don't feel that you _must_ write selector functions for every field in your state. Find a reasonable balance for granularity, based on how often fields are accessed and updated, and how much actual benefit the selectors are providing in your application.
### Name Selector Functions as `selectThing`[​](https://redux.js.org/style-guide#name-selector-functions-as-selectthing "Direct link to name-selector-functions-as-selectthing")
**We recommend prefixing selector function names with the word`select`** , combined with a description of the value being selected. Examples of this would be `selectTodos`, `selectVisibleTodos`, and `selectTodoById`.
### Avoid Putting Form State In Redux[​](https://redux.js.org/style-guide#avoid-putting-form-state-in-redux "Direct link to Avoid Putting Form State In Redux")
**Most form state shouldn't go in Redux**. In most use cases, the data is not truly global, is not being cached, and is not being used by multiple components at once. In addition, connecting forms to Redux often involves dispatching actions on every single change event, which causes performance overhead and provides no real benefit. (You probably don't need to time-travel backwards one character from `name: "Mark"` to `name: "Mar"`.)
Even if the data ultimately ends up in Redux, prefer keeping the form edits themselves in local component state, and only dispatching an action to update the Redux store once the user has completed the form.
There are use cases when keeping form state in Redux does actually make sense, such as WYSIWYG live previews of edited item attributes. But, in most cases, this isn't necessary.
Last updated on **Nov 25, 2023**
[ Previous Miscellaneous](https://redux.js.org/faq/miscellaneous)[Next API Reference](https://redux.js.org/api/api-reference)
  * [Introduction](https://redux.js.org/style-guide#introduction)
  * [Rule Categories](https://redux.js.org/style-guide#rule-categories)
    * [Priority A: Essential](https://redux.js.org/style-guide#priority-a-essential)
    * [Priority B: Strongly Recommended](https://redux.js.org/style-guide#priority-b-strongly-recommended)
    * [Priority C: Recommended](https://redux.js.org/style-guide#priority-c-recommended)
  * [Priority A Rules: Essential](https://redux.js.org/style-guide#priority-a-rules-essential)
    * [Do Not Mutate State](https://redux.js.org/style-guide#do-not-mutate-state)
    * [Reducers Must Not Have Side Effects](https://redux.js.org/style-guide#reducers-must-not-have-side-effects)
    * [Do Not Put Non-Serializable Values in State or Actions](https://redux.js.org/style-guide#do-not-put-non-serializable-values-in-state-or-actions)
    * [Only One Redux Store Per App](https://redux.js.org/style-guide#only-one-redux-store-per-app)
  * [Priority B Rules: Strongly Recommended](https://redux.js.org/style-guide#priority-b-rules-strongly-recommended)
    * [Use Redux Toolkit for Writing Redux Logic](https://redux.js.org/style-guide#use-redux-toolkit-for-writing-redux-logic)
    * [Use Immer for Writing Immutable Updates](https://redux.js.org/style-guide#use-immer-for-writing-immutable-updates)
    * [Structure Files as Feature Folders with Single-File Logic](https://redux.js.org/style-guide#structure-files-as-feature-folders-with-single-file-logic)
    * [Put as Much Logic as Possible in Reducers](https://redux.js.org/style-guide#put-as-much-logic-as-possible-in-reducers)
    * [Reducers Should Own the State Shape](https://redux.js.org/style-guide#reducers-should-own-the-state-shape)
    * [Name State Slices Based On the Stored Data](https://redux.js.org/style-guide#name-state-slices-based-on-the-stored-data)
    * [Organize State Structure Based on Data Types, Not Components](https://redux.js.org/style-guide#organize-state-structure-based-on-data-types-not-components)
    * [Treat Reducers as State Machines](https://redux.js.org/style-guide#treat-reducers-as-state-machines)
    * [Normalize Complex Nested/Relational State](https://redux.js.org/style-guide#normalize-complex-nestedrelational-state)
    * [Keep State Minimal and Derive Additional Values](https://redux.js.org/style-guide#keep-state-minimal-and-derive-additional-values)
    * [Model Actions as Events, Not Setters](https://redux.js.org/style-guide#model-actions-as-events-not-setters)
    * [Write Meaningful Action Names](https://redux.js.org/style-guide#write-meaningful-action-names)
    * [Allow Many Reducers to Respond to the Same Action](https://redux.js.org/style-guide#allow-many-reducers-to-respond-to-the-same-action)
    * [Avoid Dispatching Many Actions Sequentially](https://redux.js.org/style-guide#avoid-dispatching-many-actions-sequentially)
    * [Evaluate Where Each Piece of State Should Live](https://redux.js.org/style-guide#evaluate-where-each-piece-of-state-should-live)
    * [Use the React-Redux Hooks API](https://redux.js.org/style-guide#use-the-react-redux-hooks-api)
    * [Connect More Components to Read Data from the Store](https://redux.js.org/style-guide#connect-more-components-to-read-data-from-the-store)
    * [Use the Object Shorthand Form of `mapDispatch` with `connect`](https://redux.js.org/style-guide#use-the-object-shorthand-form-of-mapdispatch-with-connect)
    * [Call `useSelector` Multiple Times in Function Components](https://redux.js.org/style-guide#call-useselector-multiple-times-in-function-components)
    * [Use Static Typing](https://redux.js.org/style-guide#use-static-typing)
    * [Use the Redux DevTools Extension for Debugging](https://redux.js.org/style-guide#use-the-redux-devtools-extension-for-debugging)
    * [Use Plain JavaScript Objects for State](https://redux.js.org/style-guide#use-plain-javascript-objects-for-state)
  * [Priority C Rules: Recommended](https://redux.js.org/style-guide#priority-c-rules-recommended)
    * [Write Action Types as `domain/eventName`](https://redux.js.org/style-guide#write-action-types-as-domaineventname)
    * [Write Actions Using the Flux Standard Action Convention](https://redux.js.org/style-guide#write-actions-using-the-flux-standard-action-convention)
    * [Use Action Creators](https://redux.js.org/style-guide#use-action-creators)
    * [Use RTK Query for Data Fetching](https://redux.js.org/style-guide#use-rtk-query-for-data-fetching)
    * [Use Thunks and Listeners for Other Async Logic](https://redux.js.org/style-guide#use-thunks-and-listeners-for-other-async-logic)
    * [Move Complex Logic Outside Components](https://redux.js.org/style-guide#move-complex-logic-outside-components)
    * [Use Selector Functions to Read from Store State](https://redux.js.org/style-guide#use-selector-functions-to-read-from-store-state)
    * [Name Selector Functions as `selectThing`](https://redux.js.org/style-guide#name-selector-functions-as-selectthing)
    * [Avoid Putting Form State In Redux](https://redux.js.org/style-guide#avoid-putting-form-state-in-redux)


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
