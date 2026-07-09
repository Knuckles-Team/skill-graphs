## Layout Pattern[](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts#layout-pattern)
The React model allows us to deconstruct a [page](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts) into a series of components. Many of these components are often reused between pages. For example, you might have the same navigation bar and footer on every page.
components/layout.js
```
import Navbar from './navbar'
import Footer from './footer'

export default function Layout({ children }) {
  return (
    <>
      <Navbar />
      <main>{children}</main>
      <Footer />
    </>
  )
}
```
