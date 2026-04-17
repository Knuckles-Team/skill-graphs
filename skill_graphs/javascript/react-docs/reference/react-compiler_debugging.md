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
# Debugging and Troubleshooting[](https://react.dev/learn/react-compiler/debugging#undefined "Link for this heading")
This guide helps you identify and fix issues when using React Compiler. Learn how to debug compilation problems and resolve common issues.
### You will learn
  * The difference between compiler errors and runtime issues
  * Common patterns that break compilation
  * Step-by-step debugging workflow


## Understanding Compiler Behavior [](https://react.dev/learn/react-compiler/debugging#understanding-compiler-behavior "Link for Understanding Compiler Behavior ")
React Compiler is designed to handle code that follows the [Rules of React](https://react.dev/reference/rules). When it encounters code that might break these rules, it safely skips optimization rather than risk changing your app’s behavior.
### Compiler Errors vs Runtime Issues [](https://react.dev/learn/react-compiler/debugging#compiler-errors-vs-runtime-issues "Link for Compiler Errors vs Runtime Issues ")
**Compiler errors** occur at build time and prevent your code from compiling. These are rare because the compiler is designed to skip problematic code rather than fail.
**Runtime issues** occur when compiled code behaves differently than expected. Most of the time, if you encounter an issue with React Compiler, it’s a runtime issue. This typically happens when your code violates the Rules of React in subtle ways that the compiler couldn’t detect, and the compiler mistakenly compiled a component it should have skipped.
When debugging runtime issues, focus your efforts on finding Rules of React violations in the affected components that were not detected by the ESLint rule. The compiler relies on your code following these rules, and when they’re broken in ways it can’t detect, that’s when runtime problems occur.
## Common Breaking Patterns [](https://react.dev/learn/react-compiler/debugging#common-breaking-patterns "Link for Common Breaking Patterns ")
One of the main ways React Compiler can break your app is if your code was written to rely on memoization for correctness. This means your app depends on specific values being memoized to work properly. Since the compiler may memoize differently than your manual approach, this can lead to unexpected behavior like effects over-firing, infinite loops, or missing updates.
Common scenarios where this occurs:
  * **Effects that rely on referential equality** - When effects depend on objects or arrays maintaining the same reference across renders
  * **Dependency arrays that need stable references** - When unstable dependencies cause effects to fire too often or create infinite loops
  * **Conditional logic based on reference checks** - When code uses referential equality checks for caching or optimization


## Debugging Workflow [](https://react.dev/learn/react-compiler/debugging#debugging-workflow "Link for Debugging Workflow ")
Follow these steps when you encounter issues:
### Compiler Build Errors [](https://react.dev/learn/react-compiler/debugging#compiler-build-errors "Link for Compiler Build Errors ")
If you encounter a compiler error that unexpectedly breaks your build, this is likely a bug in the compiler. Report it to the
  * The error message
  * The code that caused the error
  * Your React and compiler versions


### Runtime Issues [](https://react.dev/learn/react-compiler/debugging#runtime-issues "Link for Runtime Issues ")
For runtime behavior issues:
### 1. Temporarily Disable Compilation [](https://react.dev/learn/react-compiler/debugging#temporarily-disable-compilation "Link for 1. Temporarily Disable Compilation ")
Use `"use no memo"` to isolate whether an issue is compiler-related:
```


function ProblematicComponent() {




  "use no memo"; // Skip compilation for this component




  // ... rest of component




}

```

If the issue disappears, it’s likely related to a Rules of React violation.
You can also try removing manual memoization (useMemo, useCallback, memo) from the problematic component to verify that your app works correctly without any memoization. If the bug still occurs when all memoization is removed, you have a Rules of React violation that needs to be fixed.
### 2. Fix Issues Step by Step [](https://react.dev/learn/react-compiler/debugging#fix-issues-step-by-step "Link for 2. Fix Issues Step by Step ")
  1. Identify the root cause (often memoization-for-correctness)
  2. Test after each fix
  3. Remove `"use no memo"` once fixed
  4. Verify the component shows the ✨ badge in React DevTools


## Reporting Compiler Bugs [](https://react.dev/learn/react-compiler/debugging#reporting-compiler-bugs "Link for Reporting Compiler Bugs ")
If you believe you’ve found a compiler bug:
  1. **Verify it’s not a Rules of React violation** - Check with ESLint
  2. **Create a minimal reproduction** - Isolate the issue in a small example
  3. **Test without the compiler** - Confirm the issue only occurs with compilation
  4. **File an** :
     * React and compiler versions
     * Minimal reproduction code
     * Expected vs actual behavior
     * Any error messages


## Next Steps [](https://react.dev/learn/react-compiler/debugging#next-steps "Link for Next Steps ")
  * Review the [Rules of React](https://react.dev/reference/rules) to prevent issues
  * Check the [incremental adoption guide](https://react.dev/learn/react-compiler/incremental-adoption) for gradual rollout strategies


[ PreviousIncremental Adoption ](https://react.dev/learn/react-compiler/incremental-adoption)
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
  * [Overview](https://react.dev/learn/react-compiler/debugging)
  * [Understanding Compiler Behavior ](https://react.dev/learn/react-compiler/debugging#understanding-compiler-behavior)
  * [Compiler Errors vs Runtime Issues ](https://react.dev/learn/react-compiler/debugging#compiler-errors-vs-runtime-issues)
  * [Common Breaking Patterns ](https://react.dev/learn/react-compiler/debugging#common-breaking-patterns)
  * [Debugging Workflow ](https://react.dev/learn/react-compiler/debugging#debugging-workflow)
  * [Compiler Build Errors ](https://react.dev/learn/react-compiler/debugging#compiler-build-errors)
  * [Runtime Issues ](https://react.dev/learn/react-compiler/debugging#runtime-issues)
  * [1. Temporarily Disable Compilation ](https://react.dev/learn/react-compiler/debugging#temporarily-disable-compilation)
  * [2. Fix Issues Step by Step ](https://react.dev/learn/react-compiler/debugging#fix-issues-step-by-step)
  * [Reporting Compiler Bugs ](https://react.dev/learn/react-compiler/debugging#reporting-compiler-bugs)
  * [Next Steps ](https://react.dev/learn/react-compiler/debugging#next-steps)
