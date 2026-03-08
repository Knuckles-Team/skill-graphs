[Skip to main content](https://redux.js.org/faq#__docusaurus_skipToContent_fallback)
[![Redux Logo](https://redux.js.org/img/redux.svg) **Redux**](https://redux.js.org/)
[Getting Started](https://redux.js.org/introduction/getting-started)[Tutorial](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)[Usage Guide](https://redux.js.org/usage/)[API](https://redux.js.org/api/api-reference)[FAQ](https://redux.js.org/faq)[Best Practices](https://redux.js.org/style-guide/)[Need help?](https://redux.js.org/introduction/getting-started#help-and-discussion)
  * [Introduction](https://redux.js.org/faq)
    * [Getting Started with Redux](https://redux.js.org/introduction/getting-started)
    * [Installation](https://redux.js.org/introduction/installation)
    * [Why Redux Toolkit is How To Use Redux Today](https://redux.js.org/introduction/why-rtk-is-redux-today)
    * [Core Concepts](https://redux.js.org/introduction/core-concepts)
    * [Learning Resources](https://redux.js.org/introduction/learning-resources)
    * [Ecosystem](https://redux.js.org/introduction/ecosystem)
    * [Examples](https://redux.js.org/introduction/examples)
  * [Tutorials](https://redux.js.org/faq)
  * [Using Redux](https://redux.js.org/faq)
  * [Understanding Redux](https://redux.js.org/faq)
  * [FAQ](https://redux.js.org/faq)
    * [FAQ Index](https://redux.js.org/faq)
    * [General](https://redux.js.org/faq/general)
    * [Reducers](https://redux.js.org/faq/reducers)
    * [Organizing State](https://redux.js.org/faq/organizing-state)
    * [Store Setup](https://redux.js.org/faq/store-setup)
    * [Actions](https://redux.js.org/faq/actions)
    * [Immutable Data](https://redux.js.org/faq/immutable-data)
    * [Code Structure](https://redux.js.org/faq/code-structure)
    * [Performance](https://redux.js.org/faq/performance)
    * [Design Decisions](https://redux.js.org/faq/design-decisions)
    * [React Redux](https://redux.js.org/faq/react-redux)
    * [Miscellaneous](https://redux.js.org/faq/miscellaneous)
  * [Style Guide](https://redux.js.org/faq)
  * [API Reference](https://redux.js.org/faq)
  * [Redux Toolkit](https://redux.js.org/faq)


  * [](https://redux.js.org/)
  * FAQ
  * FAQ Index


On this page
# Redux FAQ
## Table of Contents[​](https://redux.js.org/faq#table-of-contents "Direct link to Table of Contents")
  * **General**
    * [When should I learn Redux?](https://redux.js.org/faq/general#when-should-i-learn-redux)
    * [When should I use Redux?](https://redux.js.org/faq/general#when-should-i-use-redux)
    * [Can Redux only be used with React?](https://redux.js.org/faq/general#can-redux-only-be-used-with-react)
    * [Do I need to have a particular build tool to use Redux?](https://redux.js.org/faq/general#do-i-need-to-have-a-particular-build-tool-to-use-redux)
  * **Reducers**
    * [How do I share state between two reducers? Do I have to use combineReducers?](https://redux.js.org/faq/reducers#how-do-i-share-state-between-two-reducers-do-i-have-to-use-combinereducers)
    * [Do I have to use the switch statement to handle actions?](https://redux.js.org/faq/reducers#do-i-have-to-use-the-switch-statement-to-handle-actions)
  * **Organizing State**
    * [Do I have to put all my state into Redux? Should I ever use React's `useState` or `useReducer`?](https://redux.js.org/faq/organizing-state#do-i-have-to-put-all-my-state-into-redux-should-i-ever-use-reacts-usestate-or-usereducer)
    * [Can I put functions, promises, or other non-serializable items in my store state?](https://redux.js.org/faq/organizing-state#can-i-put-functions-promises-or-other-non-serializable-items-in-my-store-state)
    * [How do I organize nested or duplicate data in my state?](https://redux.js.org/faq/organizing-state#how-do-i-organize-nested-or-duplicate-data-in-my-state)
    * [Should I put form state or other UI state in my store?](https://redux.js.org/faq/organizing-state#should-i-put-form-state-or-other-ui-state-in-my-store)
  * **Store Setup**
    * [Can or should I create multiple stores? Can I import my store directly, and use it in components myself?](https://redux.js.org/faq/store-setup#can-or-should-i-create-multiple-stores-can-i-import-my-store-directly-and-use-it-in-components-myself)
    * [Is it OK to have more than one middleware chain in my store enhancer? What is the difference between next and dispatch in a middleware function?](https://redux.js.org/faq/store-setup#is-it-ok-to-have-more-than-one-middleware-chain-in-my-store-enhancer-what-is-the-difference-between-next-and-dispatch-in-a-middleware-function)
    * [How do I subscribe to only a portion of the state? Can I get the dispatched action as part of the subscription?](https://redux.js.org/faq/store-setup#how-do-i-subscribe-to-only-a-portion-of-the-state-can-i-get-the-dispatched-action-as-part-of-the-subscription)
  * **Actions**
    * [Why should type be a string, or at least serializable? Why should my action types be constants?](https://redux.js.org/faq/actions#why-should-type-be-a-string-why-should-my-action-types-be-constants)
    * [Is there always a one-to-one mapping between reducers and actions?](https://redux.js.org/faq/actions#is-there-always-a-one-to-one-mapping-between-reducers-and-actions)
    * [How can I represent “side effects” such as AJAX calls? Why do we need things like “action creators”, “thunks”, and “middleware” to do async behavior?](https://redux.js.org/faq/actions#how-can-i-represent-side-effects-such-as-ajax-calls-why-do-we-need-things-like-action-creators-thunks-and-middleware-to-do-async-behavior)
    * [What async middleware should I use? How do you decide between thunks, sagas, observables, or something else?](https://redux.js.org/faq/actions#what-async-middleware-should-i-use-how-do-you-decide-between-thunks-sagas-observables-or-something-else)
    * [Should I dispatch multiple actions in a row from one action creator?](https://redux.js.org/faq/actions#should-i-dispatch-multiple-actions-in-a-row-from-one-action-creator)
  * **Immutable Data**
    * [What are the benefits of immutability?](https://redux.js.org/faq/immutable-data#what-are-the-benefits-of-immutability)
    * [Why is immutability required by Redux?](https://redux.js.org/faq/immutable-data#why-is-immutability-required-by-redux)
    * [What approaches are there for handling data immutability? Do I have to use Immer?](https://redux.js.org/faq/immutable-data#what-approaches-are-there-for-handling-data-immutability-do-i-have-to-use-immer)
    * [What are the issues with using JavaScript for immutable operations?](https://redux.js.org/faq/immutable-data#what-are-the-issues-with-using-plain-javascript-for-immutable-operations)
  * **Code Structure**
    * [What should my file structure look like? How should I group my action creators and reducers in my project? Where should my selectors go?](https://redux.js.org/faq/code-structure#what-should-my-file-structure-look-like-how-should-i-group-my-action-creators-and-reducers-in-my-project-where-should-my-selectors-go)
    * [How should I split my logic between reducers and action creators? Where should my “business logic” go?](https://redux.js.org/faq/code-structure#how-should-i-split-my-logic-between-reducers-and-action-creators-where-should-my-business-logic-go)
    * [Why should I use action creators?](https://redux.js.org/faq/code-structure#why-should-i-use-action-creators)
    * [Where should websockets and other persistent connections live?](https://redux.js.org/faq/code-structure#where-should-websockets-and-other-persistent-connections-live)
    * [How can I use the Redux store in non-component files?](https://redux.js.org/faq/code-structure#how-can-i-use-the-redux-store-in-non-component-files)
  * **Performance**
    * [How well does Redux “scale” in terms of performance and architecture?](https://redux.js.org/faq/performance#how-well-does-redux-scale-in-terms-of-performance-and-architecture)
    * [Won't calling “all my reducers” for each action be slow?](https://redux.js.org/faq/performance#wont-calling-all-my-reducers-for-each-action-be-slow)
    * [Do I have to deep-clone my state in a reducer? Isn't copying my state going to be slow?](https://redux.js.org/faq/performance#do-i-have-to-deep-clone-my-state-in-a-reducer-isnt-copying-my-state-going-to-be-slow)
    * [How can I reduce the number of store update events?](https://redux.js.org/faq/performance#how-can-i-reduce-the-number-of-store-update-events)
    * [Will having “one state tree” cause memory problems? Will dispatching many actions take up memory?](https://redux.js.org/faq/performance#will-having-one-state-tree-cause-memory-problems-will-dispatching-many-actions-take-up-memory)
    * [Will caching remote data cause memory problems?](https://redux.js.org/faq/performance#will-caching-remote-data-cause-memory-problems)
  * **Design Decisions**
    * [Why doesn't Redux pass the state and action to subscribers?](https://redux.js.org/faq/design-decisions#why-doesnt-redux-pass-the-state-and-action-to-subscribers)
    * [Why doesn't Redux support using classes for actions and reducers?](https://redux.js.org/faq/design-decisions#why-doesnt-redux-support-using-classes-for-actions-and-reducers)
    * [Why does the middleware signature use currying?](https://redux.js.org/faq/design-decisions#why-does-the-middleware-signature-use-currying)
    * [Why does applyMiddleware use a closure for dispatch?](https://redux.js.org/faq/design-decisions#why-does-applymiddleware-use-a-closure-for-dispatch)
    * [Why doesn't `combineReducers` include a third argument with the entire state when it calls each reducer?](https://redux.js.org/faq/design-decisions#why-doesnt-combinereducers-include-a-third-argument-with-the-entire-state-when-it-calls-each-reducer)
    * [Why doesn't mapDispatchToProps allow use of return values from `getState()` or `mapStateToProps()`?](https://redux.js.org/faq/design-decisions#why-doesnt-mapdispatchtoprops-allow-use-of-return-values-from-getstate-or-mapstatetoprops)
  * **React Redux**
    * [Why should I use React-Redux?](https://redux.js.org/faq/react-redux#why-should-i-use-react-redux)
    * [Why isn't my component re-rendering, or my mapStateToProps running?](https://redux.js.org/faq/react-redux#why-isnt-my-component-re-rendering-or-my-mapstatetoprops-running)
    * [Why is my component re-rendering too often?](https://redux.js.org/faq/react-redux#why-is-my-component-re-rendering-too-often)
    * [How can I speed up my mapStateToProps?](https://redux.js.org/faq/react-redux#how-can-i-speed-up-my-mapstatetoprops)
    * [Why don't I have this.props.dispatch available in my connected component?](https://redux.js.org/faq/react-redux#why-dont-i-have-thispropsdispatch-available-in-my-connected-component)
    * [Should I only connect my top component, or can I connect multiple components in my tree?](https://redux.js.org/faq/react-redux#should-i-only-connect-my-top-component-or-can-i-connect-multiple-components-in-my-tree)
  * **Miscellaneous**
    * [Are there any larger, “real” Redux projects?](https://redux.js.org/faq/miscellaneous#are-there-any-larger-real-redux-projects)
    * [How can I implement authentication in Redux?](https://redux.js.org/faq/miscellaneous#how-can-i-implement-authentication-in-redux)


Last updated on **Apr 21, 2025**
[ Previous Middleware](https://redux.js.org/understanding/history-and-design/middleware)[Next General](https://redux.js.org/faq/general)
  * [Table of Contents](https://redux.js.org/faq#table-of-contents)


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
