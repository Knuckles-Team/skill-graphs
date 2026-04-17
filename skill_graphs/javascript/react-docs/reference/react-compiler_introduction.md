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
[React Compiler](https://react.dev/learn/react-compiler)
Copy pageCopy
# Introduction[](https://react.dev/learn/react-compiler/introduction#undefined "Link for this heading")
React Compiler is a new build-time tool that automatically optimizes your React app. It works with plain JavaScript, and understands the [Rules of React](https://react.dev/reference/rules), so you don’t need to rewrite any code to use it.
### You will learn
  * What React Compiler does
  * Getting started with the compiler
  * Incremental adoption strategies
  * Debugging and troubleshooting when things go wrong
  * Using the compiler on your React library


## What does React Compiler do? [](https://react.dev/learn/react-compiler/introduction#what-does-react-compiler-do "Link for What does React Compiler do? ")
React Compiler automatically optimizes your React application at build time. React is often fast enough without optimization, but sometimes you need to manually memoize components and values to keep your app responsive. This manual memoization is tedious, easy to get wrong, and adds extra code to maintain. React Compiler does this optimization automatically for you, freeing you from this mental burden so you can focus on building features.
### Before React Compiler [](https://react.dev/learn/react-compiler/introduction#before-react-compiler "Link for Before React Compiler ")
Without the compiler, you need to manually memoize components and values to optimize re-renders:
```


import { useMemo, useCallback, memo } from 'react';









const ExpensiveComponent = memo(function ExpensiveComponent({ data, onClick }) {




  const processedData = useMemo(() => {




    return expensiveProcessing(data);




  }, [data]);








  const handleClick = useCallback((item) => {




    onClick(item.id);




  }, [onClick]);








  return (




    <div>




      {processedData.map(item => (




        <Item key={item.id} onClick={() => handleClick(item)} />




      ))}




    </div>




  );





});


```

This manual memoization has a subtle bug that breaks memoization:
```


<Item key={item.id} onClick={() => handleClick(item)} />


```

Even though `handleClick` is wrapped in `useCallback`, the arrow function `() => handleClick(item)` creates a new function every time the component renders. This means that `Item` will always receive a new `onClick` prop, breaking memoization.
React Compiler is able to optimize this correctly with or without the arrow function, ensuring that `Item` only re-renders when `props.onClick` changes.
### After React Compiler [](https://react.dev/learn/react-compiler/introduction#after-react-compiler "Link for After React Compiler ")
With React Compiler, you write the same code without manual memoization:
```


function ExpensiveComponent({ data, onClick }) {




  const processedData = expensiveProcessing(data);








  const handleClick = (item) => {




    onClick(item.id);




  };








  return (




    <div>




      {processedData.map(item => (




        <Item key={item.id} onClick={() => handleClick(item)} />




      ))}




    </div>




  );




}

```

_[See this example in the React Compiler Playground](https://playground.react.dev/#N4Igzg9grgTgxgUxALhAMygOzgFwJYSYAEAogB4AOCmYeAbggMIQC2Fh1OAFMEQCYBDHAIA0RQowA2eOAGsiAXwCURYAB1iROITA4iFGBERgwCPgBEhAogF4iCStVoMACoeO1MAcy6DhSgG4NDSItHT0ACwFMPkkmaTlbIi48HAQWFRsAPlUQ0PFMKRlZFLSWADo8PkC8hSDMPJgEHFhiLjzQgB4+eiyO-OADIwQTM0thcpYBClL02xz2zXz8zoBJMqJZBABPG2BU9Mq+BQKiuT2uTJyomLizkoOMk4B6PqX8pSUFfs7nnro3qEapgFCAFEA)_
React Compiler automatically applies the optimal memoization, ensuring your app only re-renders when necessary.
#### What kind of memoization does React Compiler add? [](https://react.dev/learn/react-compiler/introduction#what-kind-of-memoization-does-react-compiler-add "Link for What kind of memoization does React Compiler add? ")
React Compiler’s automatic memoization is primarily focused on **improving update performance** (re-rendering existing components), so it focuses on these two use cases:
  1. **Skipping cascading re-rendering of components**
     * Re-rendering `<Parent />` causes many components in its component tree to re-render, even though only `<Parent />` has changed
  2. **Skipping expensive calculations from outside of React**
     * For example, calling `expensivelyProcessAReallyLargeArrayOfObjects()` inside of your component or hook that needs that data


#### Optimizing Re-renders [](https://react.dev/learn/react-compiler/introduction#optimizing-re-renders "Link for Optimizing Re-renders ")
React lets you express your UI as a function of their current state (more concretely: their props, state, and context). In its current implementation, when a component’s state changes, React will re-render that component _and all of its children_ — unless you have applied some form of manual memoization with `useMemo()`, `useCallback()`, or `React.memo()`. For example, in the following example, `<MessageButton>` will re-render whenever `<FriendList>`’s state changes:
```


function FriendList({ friends }) {




  const onlineCount = useFriendOnlineCount();




  if (friends.length === 0) {




    return <NoFriends />;




  }




  return (




    <div>




      <span>{onlineCount} online</span>




      {friends.map((friend) => (




        <FriendListCard key={friend.id} friend={friend} />




      ))}




      <MessageButton />




    </div>




  );




}

```

[_See this example in the React Compiler Playground_](https://playground.react.dev/#N4Igzg9grgTgxgUxALhAMygOzgFwJYSYAEAYjHgpgCYAyeYOAFMEWuZVWEQL4CURwADrEicQgyKEANnkwIAwtEw4iAXiJQwCMhWoB5TDLmKsTXgG5hRInjRFGbXZwB0UygHMcACzWr1ABn4hEWsYBBxYYgAeADkIHQ4uAHoAPksRbisiMIiYYkYs6yiqPAA3FMLrIiiwAAcAQ0wU4GlZBSUcbklDNqikusaKkKrgR0TnAFt62sYHdmp+VRT7SqrqhOo6Bnl6mCoiAGsEAE9VUfmqZzwqLrHqM7ubolTVol5eTOGigFkEMDB6u4EAAhKA4HCEZ5DNZ9ErlLIWYTcEDcIA)
React Compiler automatically applies the equivalent of manual memoization, ensuring that only the relevant parts of an app re-render as state changes, which is sometimes referred to as “fine-grained reactivity”. In the above example, React Compiler determines that the return value of `<FriendListCard />` can be reused even as `friends` changes, and can avoid recreating this JSX _and_ avoid re-rendering `<MessageButton>` as the count changes.
#### Expensive calculations also get memoized [](https://react.dev/learn/react-compiler/introduction#expensive-calculations-also-get-memoized "Link for Expensive calculations also get memoized ")
React Compiler can also automatically memoize expensive calculations used during rendering:
```


// **Not** memoized by React Compiler, since this is not a component or hook





function expensivelyProcessAReallyLargeArrayOfObjects() { /* ... */ }









// Memoized by React Compiler since this is a component





function TableContainer({ items }) {




  // This function call would be memoized:




  const data = expensivelyProcessAReallyLargeArrayOfObjects(items);




  // ...




}

```

[_See this example in the React Compiler Playground_](https://playground.react.dev/#N4Igzg9grgTgxgUxALhAejQAgFTYHIQAuumAtgqRAJYBeCAJpgEYCemASggIZyGYDCEUgAcqAGwQwANJjBUAdokyEAFlTCZ1meUUxdMcIcIjyE8vhBiYVECAGsAOvIBmURYSonMCAB7CzcgBuCGIsAAowEIhgYACCnFxioQAyXDAA5gixMDBcLADyzvlMAFYIvGAAFACUmMCYaNiYAHStOFgAvk5OGJgAshTUdIysHNy8AkbikrIKSqpaWvqGIiZmhE6u7p7ymAAqXEwSguZcCpKV9VSEFBodtcBOmAYmYHz0XIT6ALzefgFUYKhCJRBAxeLcJIsVIZLI5PKFYplCqVa63aoAbm6u0wMAQhFguwAPPRAQA+YAfL4dIloUmBMlODogDpAA)
However, if `expensivelyProcessAReallyLargeArrayOfObjects` is truly an expensive function, you may want to consider implementing its own memoization outside of React, because:
  * React Compiler only memoizes React components and hooks, not every function
  * React Compiler’s memoization is not shared across multiple components or hooks


So if `expensivelyProcessAReallyLargeArrayOfObjects` was used in many different components, even if the same exact items were passed down, that expensive calculation would be run repeatedly. We recommend [profiling](https://react.dev/reference/react/useMemo#how-to-tell-if-a-calculation-is-expensive) first to see if it really is that expensive before making code more complicated.
## Should I try out the compiler? [](https://react.dev/learn/react-compiler/introduction#should-i-try-out-the-compiler "Link for Should I try out the compiler? ")
We encourage everyone to start using React Compiler. While the compiler is still an optional addition to React today, in the future some features may require the compiler in order to fully work.
### Is it safe to use? [](https://react.dev/learn/react-compiler/introduction#is-it-safe-to-use "Link for Is it safe to use? ")
React Compiler is now stable and has been tested extensively in production. While it has been used in production at companies like Meta, rolling out the compiler to production for your app will depend on the health of your codebase and how well you’ve followed the [Rules of React](https://react.dev/reference/rules).
## What build tools are supported? [](https://react.dev/learn/react-compiler/introduction#what-build-tools-are-supported "Link for What build tools are supported? ")
React Compiler can be installed across [several build tools](https://react.dev/learn/react-compiler/installation) such as Babel, Vite, Metro, and Rsbuild.
React Compiler is primarily a light Babel plugin wrapper around the core compiler, which was designed to be decoupled from Babel itself. While the initial stable version of the compiler will remain primarily a Babel plugin, we are working with the swc and
Next.js users can enable the swc-invoked React Compiler by using
## What should I do about useMemo, useCallback, and React.memo? [](https://react.dev/learn/react-compiler/introduction#what-should-i-do-about-usememo-usecallback-and-reactmemo "Link for What should I do about useMemo, useCallback, and React.memo? ")
By default, React Compiler will memoize your code based on its analysis and heuristics. In most cases, this memoization will be as precise, or moreso, than what you may have written.
However, in some cases developers may need more control over memoization. The `useMemo` and `useCallback` hooks can continue to be used with React Compiler as an escape hatch to provide control over which values are memoized. A common use-case for this is if a memoized value is used as an effect dependency, in order to ensure that an effect does not fire repeatedly even when its dependencies do not meaningfully change.
For new code, we recommend relying on the compiler for memoization and using `useMemo`/`useCallback` where needed to achieve precise control.
For existing code, we recommend either leaving existing memoization in place (removing it can change compilation output) or carefully testing before removing the memoization.
## Try React Compiler [](https://react.dev/learn/react-compiler/introduction#try-react-compiler "Link for Try React Compiler ")
This section will help you get started with React Compiler and understand how to use it effectively in your projects.
  * **[Installation](https://react.dev/learn/react-compiler/installation)** - Install React Compiler and configure it for your build tools
  * **[React Version Compatibility](https://react.dev/reference/react-compiler/target)** - Support for React 17, 18, and 19
  * **[Configuration](https://react.dev/reference/react-compiler/configuration)** - Customize the compiler for your specific needs
  * **[Incremental Adoption](https://react.dev/learn/react-compiler/incremental-adoption)** - Strategies for gradually rolling out the compiler in existing codebases
  * **[Debugging and Troubleshooting](https://react.dev/learn/react-compiler/debugging)** - Identify and fix issues when using the compiler
  * **[Compiling Libraries](https://react.dev/reference/react-compiler/compiling-libraries)** - Best practices for shipping compiled code
  * **[API Reference](https://react.dev/reference/react-compiler/configuration)** - Detailed documentation of all configuration options


## Additional resources [](https://react.dev/learn/react-compiler/introduction#additional-resources "Link for Additional resources ")
In addition to these docs, we recommend checking the
[ PreviousReact Compiler ](https://react.dev/learn/react-compiler)[ NextInstallation ](https://react.dev/learn/react-compiler/installation)
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
  * [Overview](https://react.dev/learn/react-compiler/introduction)
  * [What does React Compiler do? ](https://react.dev/learn/react-compiler/introduction#what-does-react-compiler-do)
  * [Before React Compiler ](https://react.dev/learn/react-compiler/introduction#before-react-compiler)
  * [After React Compiler ](https://react.dev/learn/react-compiler/introduction#after-react-compiler)
  * [Should I try out the compiler? ](https://react.dev/learn/react-compiler/introduction#should-i-try-out-the-compiler)
  * [Is it safe to use? ](https://react.dev/learn/react-compiler/introduction#is-it-safe-to-use)
  * [What build tools are supported? ](https://react.dev/learn/react-compiler/introduction#what-build-tools-are-supported)
  * [What should I do about useMemo, useCallback, and React.memo? ](https://react.dev/learn/react-compiler/introduction#what-should-i-do-about-usememo-usecallback-and-reactmemo)
  * [Try React Compiler ](https://react.dev/learn/react-compiler/introduction#try-react-compiler)
  * [Additional resources ](https://react.dev/learn/react-compiler/introduction#additional-resources)
