# useRouter
Last updated February 27, 2026
If you want to access the [`router` object](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) inside any function component in your app, you can use the `useRouter` hook, take a look at the following example:
```
import { useRouter } from 'next/router'

function ActiveLink({ children, href }) {
  const router = useRouter()
  const style = {
    marginRight: 10,
    color: router.asPath === href ? 'red' : 'black',
  }

  const handleClick = (e) => {
    e.preventDefault()
    router.push(href)
  }

  return (
    <a href={href} onClick={handleClick} style={style}>
      {children}
    </a>
  )
}

export default ActiveLink
```

> `useRouter` is a [withRouter](https://nextjs.org/docs/pages/api-reference/functions/use-router#withrouter) or wrap your class in a function component.
