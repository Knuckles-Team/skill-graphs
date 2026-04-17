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
# Incremental Adoption[](https://react.dev/learn/react-compiler/incremental-adoption#undefined "Link for this heading")
React Compiler can be adopted incrementally, allowing you to try it on specific parts of your codebase first. This guide shows you how to gradually roll out the compiler in existing projects.
### You will learn
  * Why incremental adoption is recommended
  * Using Babel overrides for directory-based adoption
  * Using the “use memo” directive for opt-in compilation
  * Using the “use no memo” directive to exclude components
  * Runtime feature flags with gating
  * Monitoring your adoption progress


## Why Incremental Adoption? [](https://react.dev/learn/react-compiler/incremental-adoption#why-incremental-adoption "Link for Why Incremental Adoption? ")
React Compiler is designed to optimize your entire codebase automatically, but you don’t have to adopt it all at once. Incremental adoption gives you control over the rollout process, letting you test the compiler on small parts of your app before expanding to the rest.
Starting small helps you build confidence in the compiler’s optimizations. You can verify that your app behaves correctly with compiled code, measure performance improvements, and identify any edge cases specific to your codebase. This approach is especially valuable for production applications where stability is critical.
Incremental adoption also makes it easier to address any Rules of React violations the compiler might find. Instead of fixing violations across your entire codebase at once, you can tackle them systematically as you expand compiler coverage. This keeps the migration manageable and reduces the risk of introducing bugs.
By controlling which parts of your code get compiled, you can also run A/B tests to measure the real-world impact of the compiler’s optimizations. This data helps you make informed decisions about full adoption and demonstrates the value to your team.
## Approaches to Incremental Adoption [](https://react.dev/learn/react-compiler/incremental-adoption#approaches-to-incremental-adoption "Link for Approaches to Incremental Adoption ")
There are three main approaches to adopt React Compiler incrementally:
  1. **Babel overrides** - Apply the compiler to specific directories
  2. **Opt-in with “use memo”** - Only compile components that explicitly opt in
  3. **Runtime gating** - Control compilation with feature flags


All approaches allow you to test the compiler on specific parts of your application before full rollout.
## Directory-Based Adoption with Babel Overrides [](https://react.dev/learn/react-compiler/incremental-adoption#directory-based-adoption "Link for Directory-Based Adoption with Babel Overrides ")
Babel’s `overrides` option lets you apply different plugins to different parts of your codebase. This is ideal for gradually adopting React Compiler directory by directory.
### Basic Configuration [](https://react.dev/learn/react-compiler/incremental-adoption#basic-configuration "Link for Basic Configuration ")
Start by applying the compiler to a specific directory:
```


// babel.config.js





module.exports = {




  plugins: [




    // Global plugins that apply to all files




  ],




  overrides: [




    {




      test: './src/modern/**/*.{js,jsx,ts,tsx}',




      plugins: [




        'babel-plugin-react-compiler'




      ]




    }




  ]





};


```

### Expanding Coverage [](https://react.dev/learn/react-compiler/incremental-adoption#expanding-coverage "Link for Expanding Coverage ")
As you gain confidence, add more directories:
```


// babel.config.js





module.exports = {




  plugins: [




    // Global plugins




  ],




  overrides: [




    {




      test: ['./src/modern/**/*.{js,jsx,ts,tsx}', './src/features/**/*.{js,jsx,ts,tsx}'],




      plugins: [




        'babel-plugin-react-compiler'




      ]




    },




    {




      test: './src/legacy/**/*.{js,jsx,ts,tsx}',




      plugins: [




        // Different plugins for legacy code




      ]




    }




  ]





};


```

### With Compiler Options [](https://react.dev/learn/react-compiler/incremental-adoption#with-compiler-options "Link for With Compiler Options ")
You can also configure compiler options per override:
```


// babel.config.js





module.exports = {




  plugins: [],




  overrides: [




    {




      test: './src/experimental/**/*.{js,jsx,ts,tsx}',




      plugins: [




        ['babel-plugin-react-compiler', {




          // options ...




        }]




      ]




    },




    {




      test: './src/production/**/*.{js,jsx,ts,tsx}',




      plugins: [




        ['babel-plugin-react-compiler', {




          // options ...




        }]




      ]




    }




  ]





};


```

## Opt-in Mode with “use memo” [](https://react.dev/learn/react-compiler/incremental-adoption#opt-in-mode-with-use-memo "Link for Opt-in Mode with “use memo” ")
For maximum control, you can use `compilationMode: 'annotation'` to only compile components and hooks that explicitly opt in with the `"use memo"` directive.
This approach gives you fine-grained control over individual components and hooks. It’s useful when you want to test the compiler on specific components without affecting entire directories.
### Annotation Mode Configuration [](https://react.dev/learn/react-compiler/incremental-adoption#annotation-mode-configuration "Link for Annotation Mode Configuration ")
```


// babel.config.js





module.exports = {




  plugins: [




    ['babel-plugin-react-compiler', {




      compilationMode: 'annotation',




    }],




  ],





};


```

### Using the Directive [](https://react.dev/learn/react-compiler/incremental-adoption#using-the-directive "Link for Using the Directive ")
Add `"use memo"` at the beginning of functions you want to compile:
```


function TodoList({ todos }) {




  "use memo"; // Opt this component into compilation








  const sortedTodos = todos.slice().sort();








  return (




    <ul>




      {sortedTodos.map(todo => (




        <TodoItem key={todo.id} todo={todo} />




      ))}




    </ul>




  );





}









function useSortedData(data) {




  "use memo"; // Opt this hook into compilation








  return data.slice().sort();




}

```

With `compilationMode: 'annotation'`, you must:
  * Add `"use memo"` to every component you want optimized
  * Add `"use memo"` to every custom hook
  * Remember to add it to new components


This gives you precise control over which components are compiled while you evaluate the compiler’s impact.
## Runtime Feature Flags with Gating [](https://react.dev/learn/react-compiler/incremental-adoption#runtime-feature-flags-with-gating "Link for Runtime Feature Flags with Gating ")
The `gating` option enables you to control compilation at runtime using feature flags. This is useful for running A/B tests or gradually rolling out the compiler based on user segments.
### How Gating Works [](https://react.dev/learn/react-compiler/incremental-adoption#how-gating-works "Link for How Gating Works ")
The compiler wraps optimized code in a runtime check. If the gate returns `true`, the optimized version runs. Otherwise, the original code runs.
### Gating Configuration [](https://react.dev/learn/react-compiler/incremental-adoption#gating-configuration "Link for Gating Configuration ")
```


// babel.config.js





module.exports = {




  plugins: [




    ['babel-plugin-react-compiler', {




      gating: {




        source: 'ReactCompilerFeatureFlags',




        importSpecifierName: 'isCompilerEnabled',




      },




    }],




  ],





};


```

### Implementing the Feature Flag [](https://react.dev/learn/react-compiler/incremental-adoption#implementing-the-feature-flag "Link for Implementing the Feature Flag ")
Create a module that exports your gating function:
```


// ReactCompilerFeatureFlags.js





export function isCompilerEnabled() {




  // Use your feature flag system




  return getFeatureFlag('react-compiler-enabled');




}

```

## Troubleshooting Adoption [](https://react.dev/learn/react-compiler/incremental-adoption#troubleshooting-adoption "Link for Troubleshooting Adoption ")
If you encounter issues during adoption:
  1. Use `"use no memo"` to temporarily exclude problematic components
  2. Check the [debugging guide](https://react.dev/learn/react-compiler/debugging) for common issues
  3. Fix Rules of React violations identified by the ESLint plugin
  4. Consider using `compilationMode: 'annotation'` for more gradual adoption


## Next Steps [](https://react.dev/learn/react-compiler/incremental-adoption#next-steps "Link for Next Steps ")
  * Read the [configuration guide](https://react.dev/reference/react-compiler/configuration) for more options
  * Learn about [debugging techniques](https://react.dev/learn/react-compiler/debugging)
  * Check the [API reference](https://react.dev/reference/react-compiler/configuration) for all compiler options


[ PreviousInstallation ](https://react.dev/learn/react-compiler/installation)[ NextDebugging and Troubleshooting ](https://react.dev/learn/react-compiler/debugging)
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
  * [Overview](https://react.dev/learn/react-compiler/incremental-adoption)
  * [Why Incremental Adoption? ](https://react.dev/learn/react-compiler/incremental-adoption#why-incremental-adoption)
  * [Approaches to Incremental Adoption ](https://react.dev/learn/react-compiler/incremental-adoption#approaches-to-incremental-adoption)
  * [Directory-Based Adoption with Babel Overrides ](https://react.dev/learn/react-compiler/incremental-adoption#directory-based-adoption)
  * [Basic Configuration ](https://react.dev/learn/react-compiler/incremental-adoption#basic-configuration)
  * [Expanding Coverage ](https://react.dev/learn/react-compiler/incremental-adoption#expanding-coverage)
  * [With Compiler Options ](https://react.dev/learn/react-compiler/incremental-adoption#with-compiler-options)
  * [Opt-in Mode with “use memo” ](https://react.dev/learn/react-compiler/incremental-adoption#opt-in-mode-with-use-memo)
  * [Annotation Mode Configuration ](https://react.dev/learn/react-compiler/incremental-adoption#annotation-mode-configuration)
  * [Using the Directive ](https://react.dev/learn/react-compiler/incremental-adoption#using-the-directive)
  * [Runtime Feature Flags with Gating ](https://react.dev/learn/react-compiler/incremental-adoption#runtime-feature-flags-with-gating)
  * [How Gating Works ](https://react.dev/learn/react-compiler/incremental-adoption#how-gating-works)
  * [Gating Configuration ](https://react.dev/learn/react-compiler/incremental-adoption#gating-configuration)
  * [Implementing the Feature Flag ](https://react.dev/learn/react-compiler/incremental-adoption#implementing-the-feature-flag)
  * [Troubleshooting Adoption ](https://react.dev/learn/react-compiler/incremental-adoption#troubleshooting-adoption)
  * [Next Steps ](https://react.dev/learn/react-compiler/incremental-adoption#next-steps)
