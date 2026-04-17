[Skip to main content](https://testing-library.com/docs/example-reach-router)
[![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-64x64.png) **Testing Library**](https://testing-library.com/)[Docs](https://testing-library.com/docs/)[Examples](https://testing-library.com/docs/recipes)
[Help](https://testing-library.com/help)[Blog](https://testing-library.com/blog)
Search`K`
  * [About the Examples](https://testing-library.com/docs/recipes)
  * [Examples](https://testing-library.com/docs/example-reach-router)
    * [Codesandbox Examples](https://testing-library.com/docs/example-codesandbox)
    * [External Examples](https://testing-library.com/docs/example-external)
    * [Using findByText](https://testing-library.com/docs/example-findByText)
    * [Input Event](https://testing-library.com/docs/example-input-event)
    * [React Context](https://testing-library.com/docs/example-react-context)
    * [useReducer](https://testing-library.com/docs/example-react-hooks-useReducer)
    * [Formik](https://testing-library.com/docs/example-react-formik)
    * [React Intl](https://testing-library.com/docs/example-react-intl)
    * [React Redux](https://testing-library.com/docs/example-react-redux)
    * [React Router](https://testing-library.com/docs/example-react-router)
    * [Reach Router](https://testing-library.com/docs/example-reach-router)
    * [React Transition Group](https://testing-library.com/docs/example-react-transition-group)
    * [Modals](https://testing-library.com/docs/example-react-modal)
    * [Update Props](https://testing-library.com/docs/example-update-props)
  * [Help](https://testing-library.com/docs/example-reach-router)
    * [Learning Material](https://testing-library.com/docs/learning)
    * [Contributing](https://testing-library.com/docs/contributing)


  * [](https://testing-library.com/)
  * Examples
  * Reach Router


# Reach Router
```
import React from 'react'
import {render} from '@testing-library/react'
import {
  Router,
  Link,
  createHistory,
  createMemorySource,
  LocationProvider,
} from '@reach/router'
import '@testing-library/jest-dom'

const About = () => <div>You are on the about page</div>
const Home = () => <div>You are home</div>
const NoMatch = () => <div>No match</div>

function App() {
  return (
    <div>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Router>
        <Home path="/" />
        <About path="/about" />
        <NoMatch default />
      </Router>
    </div>
  )
}

// Ok, so here's what your tests might look like

// this is a handy function that I would utilize for any component
// that relies on the router being in context
function renderWithRouter(
  ui,
  {route = '/', history = createHistory(createMemorySource(route))} = {},
) {
  return {
    ...render(<LocationProvider history={history}>{ui}</LocationProvider>),
    // adding `history` to the returned utilities to allow us
    // to reference it in our tests (just try to avoid using
    // this to test implementation details).
    history,
  }
}

test('full app rendering/navigating', async () => {
  const {
    container,
    history: {navigate},
  } = renderWithRouter(<App />)
  const appContainer = container
  // normally I'd use a data-testid, but just wanted to show this is also possible
  expect(appContainer.innerHTML).toMatch('You are home')

  // with reach-router we don't need to simulate a click event, we can just transition
  // to the page using the navigate function returned from the history object.
  await navigate('/about')
  expect(container.innerHTML).toMatch('You are on the about page')
})

test('landing on a bad page', () => {
  const {container} = renderWithRouter(<App />, {
    route: '/something-that-does-not-match',
  })
  // normally I'd use a data-testid, but just wanted to show this is also possible
  expect(container.innerHTML).toMatch('No match')
})

// If your route component has parameters, you'll have to change the render function a little bit
// example of a route component with parameter
const Routes = () => (
  <Router>
    <SomeComponent path="/some-component/:id" />
  </Router>
)

// render function with Router wrapper from @reach/router
function renderWithRouterWrapper(
  ui,
  {route = '/', history = createHistory(createMemorySource(route))} = {},
) {
  return {
    ...render(
      <LocationProvider history={history}>
        <Router>{ui}</Router>
      </LocationProvider>,
    ),
    history,
  }
}

test('renders the component with params', () => {
  // you'll have to declare the path prop in the component, exactly like the route
  renderWithRouterWrapper(<SomeComponent path="/some-component/:id" />, {
    // and pass the parameter value on the route config
    route: '/some-component/1',
  })
})

```

Last updated on **Aug 14, 2021** by **Sidharth Vinod**
[ Previous React Router](https://testing-library.com/docs/example-react-router)[Next React Transition Group](https://testing-library.com/docs/example-react-transition-group)
Docs
  * [Getting Started](https://testing-library.com/docs)
  * [Examples](https://testing-library.com/docs/example-codesandbox)
  * [API](https://testing-library.com/docs/dom-testing-library/api)
  * [Help](https://testing-library.com/docs/dom-testing-library/faq)


Community
  * [Blog](https://testing-library.com/blog)


More
![An octopus representing the DOM Testing Library Logo](https://testing-library.com/img/octopus-128x128.png)
Copyright © 2018-2026 Kent C. Dodds and contributors
