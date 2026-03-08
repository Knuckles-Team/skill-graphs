[ Skip to content ](https://docs.pydantic.dev/fastui/#fastui)
[ ![logo](https://docs.pydantic.dev/fastui/assets/logo-white.svg) ](https://docs.pydantic.dev/fastui/ "FastUI")
FastUI
Introduction
Type to start searching
  * [ Introduction ](https://docs.pydantic.dev/fastui/)
  * [ Guide ](https://docs.pydantic.dev/fastui/guide/)
  * [ API Documentation ](https://docs.pydantic.dev/fastui/api/python_components/)


[ ![logo](https://docs.pydantic.dev/fastui/assets/logo-white.svg) ](https://docs.pydantic.dev/fastui/ "FastUI") FastUI
  * Introduction  [ Introduction  ](https://docs.pydantic.dev/fastui/)
    * [ The Principle  ](https://docs.pydantic.dev/fastui/#the-principle)
    * [ The Practice - Installation  ](https://docs.pydantic.dev/fastui/#the-practice-installation)
    * [ Usage  ](https://docs.pydantic.dev/fastui/#usage)
      * [ The Principle (long version)  ](https://docs.pydantic.dev/fastui/#the-principle-long-version)
        * [ Beyond Python and React  ](https://docs.pydantic.dev/fastui/#beyond-python-and-react)
  * [ Guide  ](https://docs.pydantic.dev/fastui/guide/)
  * API Documentation
    * [ Python Components  ](https://docs.pydantic.dev/fastui/api/python_components/)
    * [ TypeScript Components  ](https://docs.pydantic.dev/fastui/api/typescript_components/)


  * [ The Principle  ](https://docs.pydantic.dev/fastui/#the-principle)
  * [ The Practice - Installation  ](https://docs.pydantic.dev/fastui/#the-practice-installation)
  * [ Usage  ](https://docs.pydantic.dev/fastui/#usage)
    * [ The Principle (long version)  ](https://docs.pydantic.dev/fastui/#the-principle-long-version)
      * [ Beyond Python and React  ](https://docs.pydantic.dev/fastui/#beyond-python-and-react)


# FastUI[¶](https://docs.pydantic.dev/fastui/#fastui "Permanent link")
## The Principle[¶](https://docs.pydantic.dev/fastui/#the-principle "Permanent link")
FastUI is a new way to build web application user interfaces defined by declarative Python code.
This means:
  * **If you're a Python developer** — you can build responsive web applications using React without writing a single line of JavaScript, or touching `npm`.
  * **If you're a frontend developer** — you can concentrate on building magical components that are truly reusable, no copy-pasting components for each view.
  * **For everyone** — a true separation of concerns, the backend defines the entire application; while the frontend is free to implement just the user interface


At its heart, FastUI is a set of matching [Pydantic](https://docs.pydantic.dev) models and TypeScript interfaces that allow you to define a user interface. This interface is validated at build time by TypeScript and pyright/mypy and at runtime by Pydantic.
You can see a simple demo of an application built with FastUI
## The Practice - Installation[¶](https://docs.pydantic.dev/fastui/#the-practice-installation "Permanent link")
FastUI is made up of 4 things:
## Usage[¶](https://docs.pydantic.dev/fastui/#usage "Permanent link")
Here's a simple but complete FastAPI application that uses FastUI to show some user profiles:
```
[](https://docs.pydantic.dev/fastui/#__codelineno-0-1)from datetime import date
[](https://docs.pydantic.dev/fastui/#__codelineno-0-2)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-3)from fastapi import FastAPI, HTTPException
[](https://docs.pydantic.dev/fastui/#__codelineno-0-4)from fastapi.responses import HTMLResponse
[](https://docs.pydantic.dev/fastui/#__codelineno-0-5)from fastui import FastUI, AnyComponent, prebuilt_html, components as c
[](https://docs.pydantic.dev/fastui/#__codelineno-0-6)from fastui.components.display import DisplayMode, DisplayLookup
[](https://docs.pydantic.dev/fastui/#__codelineno-0-7)from fastui.events import GoToEvent, BackEvent
[](https://docs.pydantic.dev/fastui/#__codelineno-0-8)from pydantic import BaseModel, Field
[](https://docs.pydantic.dev/fastui/#__codelineno-0-9)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-10)app = FastAPI()
[](https://docs.pydantic.dev/fastui/#__codelineno-0-11)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-12)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-13)class User(BaseModel):
[](https://docs.pydantic.dev/fastui/#__codelineno-0-14)    id: int
[](https://docs.pydantic.dev/fastui/#__codelineno-0-15)    name: str
[](https://docs.pydantic.dev/fastui/#__codelineno-0-16)    dob: date = Field(title='Date of Birth')
[](https://docs.pydantic.dev/fastui/#__codelineno-0-17)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-18)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-19)# define some users
[](https://docs.pydantic.dev/fastui/#__codelineno-0-20)users = [
[](https://docs.pydantic.dev/fastui/#__codelineno-0-21)    User(id=1, name='John', dob=date(1990, 1, 1)),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-22)    User(id=2, name='Jack', dob=date(1991, 1, 1)),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-23)    User(id=3, name='Jill', dob=date(1992, 1, 1)),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-24)    User(id=4, name='Jane', dob=date(1993, 1, 1)),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-25)]
[](https://docs.pydantic.dev/fastui/#__codelineno-0-26)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-27)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-28)@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-29)def users_table() -> list[AnyComponent]:
[](https://docs.pydantic.dev/fastui/#__codelineno-0-30)    """
[](https://docs.pydantic.dev/fastui/#__codelineno-0-31)    Show a table of four users, `/api` is the endpoint the frontend will connect to
[](https://docs.pydantic.dev/fastui/#__codelineno-0-32)    when a user visits `/` to fetch components to render.
[](https://docs.pydantic.dev/fastui/#__codelineno-0-33)    """
[](https://docs.pydantic.dev/fastui/#__codelineno-0-34)    return [
[](https://docs.pydantic.dev/fastui/#__codelineno-0-35)        c.Page(  # Page provides a basic container for components
[](https://docs.pydantic.dev/fastui/#__codelineno-0-36)            components=[
[](https://docs.pydantic.dev/fastui/#__codelineno-0-37)                c.Heading(text='Users', level=2),  # renders `<h2>Users</h2>`
[](https://docs.pydantic.dev/fastui/#__codelineno-0-38)                c.Table(
[](https://docs.pydantic.dev/fastui/#__codelineno-0-39)                    data=users,
[](https://docs.pydantic.dev/fastui/#__codelineno-0-40)                    # define two columns for the table
[](https://docs.pydantic.dev/fastui/#__codelineno-0-41)                    columns=[
[](https://docs.pydantic.dev/fastui/#__codelineno-0-42)                        # the first is the users, name rendered as a link to their profile
[](https://docs.pydantic.dev/fastui/#__codelineno-0-43)                        DisplayLookup(field='name', on_click=GoToEvent(url='/user/{id}/')),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-44)                        # the second is the date of birth, rendered as a date
[](https://docs.pydantic.dev/fastui/#__codelineno-0-45)                        DisplayLookup(field='dob', mode=DisplayMode.date),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-46)                    ],
[](https://docs.pydantic.dev/fastui/#__codelineno-0-47)                ),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-48)            ]
[](https://docs.pydantic.dev/fastui/#__codelineno-0-49)        ),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-50)    ]
[](https://docs.pydantic.dev/fastui/#__codelineno-0-51)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-52)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-53)@app.get("/api/user/{user_id}/", response_model=FastUI, response_model_exclude_none=True)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-54)def user_profile(user_id: int) -> list[AnyComponent]:
[](https://docs.pydantic.dev/fastui/#__codelineno-0-55)    """
[](https://docs.pydantic.dev/fastui/#__codelineno-0-56)    User profile page, the frontend will fetch this when the user visits `/user/{id}/`.
[](https://docs.pydantic.dev/fastui/#__codelineno-0-57)    """
[](https://docs.pydantic.dev/fastui/#__codelineno-0-58)    try:
[](https://docs.pydantic.dev/fastui/#__codelineno-0-59)        user = next(u for u in users if u.id == user_id)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-60)    except StopIteration:
[](https://docs.pydantic.dev/fastui/#__codelineno-0-61)        raise HTTPException(status_code=404, detail="User not found")
[](https://docs.pydantic.dev/fastui/#__codelineno-0-62)    return [
[](https://docs.pydantic.dev/fastui/#__codelineno-0-63)        c.Page(
[](https://docs.pydantic.dev/fastui/#__codelineno-0-64)            components=[
[](https://docs.pydantic.dev/fastui/#__codelineno-0-65)                c.Heading(text=user.name, level=2),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-66)                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-67)                c.Details(data=user),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-68)            ]
[](https://docs.pydantic.dev/fastui/#__codelineno-0-69)        ),
[](https://docs.pydantic.dev/fastui/#__codelineno-0-70)    ]
[](https://docs.pydantic.dev/fastui/#__codelineno-0-71)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-72)
[](https://docs.pydantic.dev/fastui/#__codelineno-0-73)@app.get('/{path:path}')
[](https://docs.pydantic.dev/fastui/#__codelineno-0-74)async def html_landing() -> HTMLResponse:
[](https://docs.pydantic.dev/fastui/#__codelineno-0-75)    """Simple HTML page which serves the React app, comes last as it matches all paths."""
[](https://docs.pydantic.dev/fastui/#__codelineno-0-76)    return HTMLResponse(prebuilt_html(title='FastUI Demo'))

```

Which renders like this:
![screenshot](https://raw.githubusercontent.com/pydantic/FastUI/main/screenshot.png)
Of course, that's a very simple application, the
### The Principle (long version)[¶](https://docs.pydantic.dev/fastui/#the-principle-long-version "Permanent link")
FastUI is an implementation of the RESTful principle; but not as it's usually understood, instead I mean the principle defined in the original
The RESTful principle as described in the HTMX article is that the frontend doesn't need to (and shouldn't) know anything about the application you're building. Instead, it should just provide all the components you need to construct the interface, the backend can then tell the frontend what to do.
Think of your frontend as a puppet, and the backend as the hand within it — the puppet doesn't need to know what to say, that's kind of the point.
Building an application this way has a number of significant advantages:
  * You only need to write code in one place to build a new feature — add a new view, change the behavior of an existing view or alter the URL structure
  * Deploying the front and backend can be completely decoupled, provided the frontend knows how to render all the components the backend is going to ask it to use, you're good to go
  * You should be able to reuse a rich set of opensource components, they should end up being better tested and more reliable than anything you could build yourself, this is possible because the components need no context about how they're going to be used (note: since FastUI is brand new, this isn't true yet, hopefully we get there)
  * We can use Pydantic, TypeScript and JSON Schema to provide guarantees that the two sides are communicating with an agreed schema


In the abstract, FastUI is like the opposite of GraphQL but with the same goal — GraphQL lets frontend developers extend an application without any new backend development; FastUI lets backend developers extend an application without any new frontend development.
#### Beyond Python and React[¶](https://docs.pydantic.dev/fastui/#beyond-python-and-react "Permanent link")
Of course, this principle shouldn't be limited to Python and React applications — provided we use the same set of agreed schemas and encoding to communicate, we should be able to use any frontend and backend that implements the schema. Interchangeably.
This could mean:
  * Implementing a web frontend using another JS framework like Vue — lots of work, limited value
  * Implementing a web frontend using an edge server, so the browser just sees HTML — lots of work but very valuable
  * Implementing frontends for other platforms like mobile or IOT — lots of work, no idea if it's actually a good idea?
  * Implementing the component models in another language like Rust or Go — since there's actually not that much code in the backend, so this would be a relatively small and mechanical task


Made with
