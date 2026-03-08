[ Skip to content ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#bigger-applications-multiple-files)
[ ![logo](https://fastapi.tiangolo.com/img/icon-white.svg) ](https://fastapi.tiangolo.com/ "FastAPI") FastAPI
  * [ FastAPI  ](https://fastapi.tiangolo.com/)
  * [ Features  ](https://fastapi.tiangolo.com/features/)
  * [ Learn  ](https://fastapi.tiangolo.com/learn/)
    * [ Python Types Intro  ](https://fastapi.tiangolo.com/python-types/)
    * [ Concurrency and async / await  ](https://fastapi.tiangolo.com/async/)
    * [ Environment Variables  ](https://fastapi.tiangolo.com/environment-variables/)
    * [ Virtual Environments  ](https://fastapi.tiangolo.com/virtual-environments/)
    * [ Tutorial - User Guide  ](https://fastapi.tiangolo.com/tutorial/)
      * [ First Steps  ](https://fastapi.tiangolo.com/tutorial/first-steps/)
      * [ Path Parameters  ](https://fastapi.tiangolo.com/tutorial/path-params/)
      * [ Query Parameters  ](https://fastapi.tiangolo.com/tutorial/query-params/)
      * [ Request Body  ](https://fastapi.tiangolo.com/tutorial/body/)
      * [ Query Parameters and String Validations  ](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
      * [ Path Parameters and Numeric Validations  ](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/)
      * [ Query Parameter Models  ](https://fastapi.tiangolo.com/tutorial/query-param-models/)
      * [ Body - Multiple Parameters  ](https://fastapi.tiangolo.com/tutorial/body-multiple-params/)
      * [ Body - Fields  ](https://fastapi.tiangolo.com/tutorial/body-fields/)
      * [ Body - Nested Models  ](https://fastapi.tiangolo.com/tutorial/body-nested-models/)
      * [ Declare Request Example Data  ](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
      * [ Extra Data Types  ](https://fastapi.tiangolo.com/tutorial/extra-data-types/)
      * [ Cookie Parameters  ](https://fastapi.tiangolo.com/tutorial/cookie-params/)
      * [ Header Parameters  ](https://fastapi.tiangolo.com/tutorial/header-params/)
      * [ Cookie Parameter Models  ](https://fastapi.tiangolo.com/tutorial/cookie-param-models/)
      * [ Header Parameter Models  ](https://fastapi.tiangolo.com/tutorial/header-param-models/)
      * [ Response Model - Return Type  ](https://fastapi.tiangolo.com/tutorial/response-model/)
      * [ Extra Models  ](https://fastapi.tiangolo.com/tutorial/extra-models/)
      * [ Response Status Code  ](https://fastapi.tiangolo.com/tutorial/response-status-code/)
      * [ Form Data  ](https://fastapi.tiangolo.com/tutorial/request-forms/)
      * [ Form Models  ](https://fastapi.tiangolo.com/tutorial/request-form-models/)
      * [ Request Files  ](https://fastapi.tiangolo.com/tutorial/request-files/)
      * [ Request Forms and Files  ](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/)
      * [ Handling Errors  ](https://fastapi.tiangolo.com/tutorial/handling-errors/)
      * [ Path Operation Configuration  ](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/)
      * [ JSON Compatible Encoder  ](https://fastapi.tiangolo.com/tutorial/encoder/)
      * [ Body - Updates  ](https://fastapi.tiangolo.com/tutorial/body-updates/)
      * [ Dependencies  ](https://fastapi.tiangolo.com/tutorial/dependencies/)
        * [ Classes as Dependencies  ](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/)
        * [ Sub-dependencies  ](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/)
        * [ Dependencies in path operation decorators  ](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/)
        * [ Global Dependencies  ](https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/)
        * [ Dependencies with yield  ](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)
      * [ Security  ](https://fastapi.tiangolo.com/tutorial/security/)
        * [ Security - First Steps  ](https://fastapi.tiangolo.com/tutorial/security/first-steps/)
        * [ Get Current User  ](https://fastapi.tiangolo.com/tutorial/security/get-current-user/)
        * [ Simple OAuth2 with Password and Bearer  ](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)
        * [ OAuth2 with Password (and hashing), Bearer with JWT tokens  ](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
      * [ Middleware  ](https://fastapi.tiangolo.com/tutorial/middleware/)
      * [ CORS (Cross-Origin Resource Sharing)  ](https://fastapi.tiangolo.com/tutorial/cors/)
      * [ SQL (Relational) Databases  ](https://fastapi.tiangolo.com/tutorial/sql-databases/)
      * Bigger Applications - Multiple Files  [ Bigger Applications - Multiple Files  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
        * [ An example file structure  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure)
        * [ `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter)
          * [ Import `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter)
          * [ _Path operations_ with `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#path-operations-with-apirouter)
        * [ Dependencies  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#dependencies)
        * [ Another module with `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter)
          * [ Import the dependencies  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-dependencies)
            * [ How relative imports work  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-relative-imports-work)
          * [ Add some custom `tags`, `responses`, and `dependencies` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#add-some-custom-tags-responses-and-dependencies)
        * [ The main `FastAPI` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi)
          * [ Import `FastAPI` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi)
          * [ Import the `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-apirouter)
          * [ How the importing works  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-the-importing-works)
          * [ Avoid name collisions  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#avoid-name-collisions)
          * [ Include the `APIRouter`s for `users` and `items` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-apirouters-for-users-and-items)
          * [ Include an `APIRouter` with a custom `prefix`, `tags`, `responses`, and `dependencies` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies)
          * [ Include a _path operation_ ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-a-path-operation)
        * [ Configure the `entrypoint` in `pyproject.toml` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#configure-the-entrypoint-in-pyproject-toml)
        * [ Check the automatic API docs  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#check-the-automatic-api-docs)
        * [ Include the same router multiple times with different `prefix` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-same-router-multiple-times-with-different-prefix)
        * [ Include an `APIRouter` in another  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-in-another)
      * [ Stream JSON Lines  ](https://fastapi.tiangolo.com/tutorial/stream-json-lines/)
      * [ Server-Sent Events (SSE)  ](https://fastapi.tiangolo.com/tutorial/server-sent-events/)
      * [ Background Tasks  ](https://fastapi.tiangolo.com/tutorial/background-tasks/)
      * [ Metadata and Docs URLs  ](https://fastapi.tiangolo.com/tutorial/metadata/)
      * [ Static Files  ](https://fastapi.tiangolo.com/tutorial/static-files/)
      * [ Testing  ](https://fastapi.tiangolo.com/tutorial/testing/)
      * [ Debugging  ](https://fastapi.tiangolo.com/tutorial/debugging/)
    * [ Advanced User Guide  ](https://fastapi.tiangolo.com/advanced/)
      * [ Stream Data  ](https://fastapi.tiangolo.com/advanced/stream-data/)
      * [ Path Operation Advanced Configuration  ](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/)
      * [ Additional Status Codes  ](https://fastapi.tiangolo.com/advanced/additional-status-codes/)
      * [ Return a Response Directly  ](https://fastapi.tiangolo.com/advanced/response-directly/)
      * [ Custom Response - HTML, Stream, File, others  ](https://fastapi.tiangolo.com/advanced/custom-response/)
      * [ Additional Responses in OpenAPI  ](https://fastapi.tiangolo.com/advanced/additional-responses/)
      * [ Response Cookies  ](https://fastapi.tiangolo.com/advanced/response-cookies/)
      * [ Response Headers  ](https://fastapi.tiangolo.com/advanced/response-headers/)
      * [ Response - Change Status Code  ](https://fastapi.tiangolo.com/advanced/response-change-status-code/)
      * [ Advanced Dependencies  ](https://fastapi.tiangolo.com/advanced/advanced-dependencies/)
      * [ Advanced Security  ](https://fastapi.tiangolo.com/advanced/security/)
        * [ OAuth2 scopes  ](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)
        * [ HTTP Basic Auth  ](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/)
      * [ Using the Request Directly  ](https://fastapi.tiangolo.com/advanced/using-request-directly/)
      * [ Using Dataclasses  ](https://fastapi.tiangolo.com/advanced/dataclasses/)
      * [ Advanced Middleware  ](https://fastapi.tiangolo.com/advanced/middleware/)
      * [ Sub Applications - Mounts  ](https://fastapi.tiangolo.com/advanced/sub-applications/)
      * [ Behind a Proxy  ](https://fastapi.tiangolo.com/advanced/behind-a-proxy/)
      * [ Templates  ](https://fastapi.tiangolo.com/advanced/templates/)
      * [ WebSockets  ](https://fastapi.tiangolo.com/advanced/websockets/)
      * [ Lifespan Events  ](https://fastapi.tiangolo.com/advanced/events/)
      * [ Testing WebSockets  ](https://fastapi.tiangolo.com/advanced/testing-websockets/)
      * [ Testing Events: lifespan and startup - shutdown  ](https://fastapi.tiangolo.com/advanced/testing-events/)
      * [ Testing Dependencies with Overrides  ](https://fastapi.tiangolo.com/advanced/testing-dependencies/)
      * [ Async Tests  ](https://fastapi.tiangolo.com/advanced/async-tests/)
      * [ Settings and Environment Variables  ](https://fastapi.tiangolo.com/advanced/settings/)
      * [ OpenAPI Callbacks  ](https://fastapi.tiangolo.com/advanced/openapi-callbacks/)
      * [ OpenAPI Webhooks  ](https://fastapi.tiangolo.com/advanced/openapi-webhooks/)
      * [ Including WSGI - Flask, Django, others  ](https://fastapi.tiangolo.com/advanced/wsgi/)
      * [ Generating SDKs  ](https://fastapi.tiangolo.com/advanced/generate-clients/)
      * [ Advanced Python Types  ](https://fastapi.tiangolo.com/advanced/advanced-python-types/)
      * [ JSON with Bytes as Base64  ](https://fastapi.tiangolo.com/advanced/json-base64-bytes/)
      * [ Strict Content-Type Checking  ](https://fastapi.tiangolo.com/advanced/strict-content-type/)
    * [ FastAPI CLI  ](https://fastapi.tiangolo.com/fastapi-cli/)
    * [ Editor Support  ](https://fastapi.tiangolo.com/editor-support/)
    * [ Deployment  ](https://fastapi.tiangolo.com/deployment/)
      * [ About FastAPI versions  ](https://fastapi.tiangolo.com/deployment/versions/)
      * [ FastAPI Cloud  ](https://fastapi.tiangolo.com/deployment/fastapicloud/)
      * [ About HTTPS  ](https://fastapi.tiangolo.com/deployment/https/)
      * [ Run a Server Manually  ](https://fastapi.tiangolo.com/deployment/manually/)
      * [ Deployments Concepts  ](https://fastapi.tiangolo.com/deployment/concepts/)
      * [ Deploy FastAPI on Cloud Providers  ](https://fastapi.tiangolo.com/deployment/cloud/)
      * [ Server Workers - Uvicorn with Workers  ](https://fastapi.tiangolo.com/deployment/server-workers/)
      * [ FastAPI in Containers - Docker  ](https://fastapi.tiangolo.com/deployment/docker/)
    * [ How To - Recipes  ](https://fastapi.tiangolo.com/how-to/)
      * [ General - How To - Recipes  ](https://fastapi.tiangolo.com/how-to/general/)
      * [ Migrate from Pydantic v1 to Pydantic v2  ](https://fastapi.tiangolo.com/how-to/migrate-from-pydantic-v1-to-pydantic-v2/)
      * [ GraphQL  ](https://fastapi.tiangolo.com/how-to/graphql/)
      * [ Custom Request and APIRoute class  ](https://fastapi.tiangolo.com/how-to/custom-request-and-route/)
      * [ Conditional OpenAPI  ](https://fastapi.tiangolo.com/how-to/conditional-openapi/)
      * [ Extending OpenAPI  ](https://fastapi.tiangolo.com/how-to/extending-openapi/)
      * [ Separate OpenAPI Schemas for Input and Output or Not  ](https://fastapi.tiangolo.com/how-to/separate-openapi-schemas/)
      * [ Custom Docs UI Static Assets (Self-Hosting)  ](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/)
      * [ Configure Swagger UI  ](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)
      * [ Testing a Database  ](https://fastapi.tiangolo.com/how-to/testing-database/)
      * [ Use Old 403 Authentication Error Status Codes  ](https://fastapi.tiangolo.com/how-to/authentication-error-status-code/)
  * [ Reference  ](https://fastapi.tiangolo.com/reference/)
    * [ `FastAPI` class  ](https://fastapi.tiangolo.com/reference/fastapi/)
    * [ Request Parameters  ](https://fastapi.tiangolo.com/reference/parameters/)
    * [ Status Codes  ](https://fastapi.tiangolo.com/reference/status/)
    * [ `UploadFile` class  ](https://fastapi.tiangolo.com/reference/uploadfile/)
    * [ Exceptions - `HTTPException` and `WebSocketException` ](https://fastapi.tiangolo.com/reference/exceptions/)
    * [ Dependencies - `Depends()` and `Security()` ](https://fastapi.tiangolo.com/reference/dependencies/)
    * [ `APIRouter` class  ](https://fastapi.tiangolo.com/reference/apirouter/)
    * [ Background Tasks - `BackgroundTasks` ](https://fastapi.tiangolo.com/reference/background/)
    * [ `Request` class  ](https://fastapi.tiangolo.com/reference/request/)
    * [ WebSockets  ](https://fastapi.tiangolo.com/reference/websockets/)
    * [ `HTTPConnection` class  ](https://fastapi.tiangolo.com/reference/httpconnection/)
    * [ `Response` class  ](https://fastapi.tiangolo.com/reference/response/)
    * [ Custom Response Classes - File, HTML, Redirect, Streaming, etc.  ](https://fastapi.tiangolo.com/reference/responses/)
    * [ Middleware  ](https://fastapi.tiangolo.com/reference/middleware/)
    * [ OpenAPI  ](https://fastapi.tiangolo.com/reference/openapi/)
      * [ OpenAPI `docs` ](https://fastapi.tiangolo.com/reference/openapi/docs/)
      * [ OpenAPI `models` ](https://fastapi.tiangolo.com/reference/openapi/models/)
    * [ Security Tools  ](https://fastapi.tiangolo.com/reference/security/)
    * [ Encoders - `jsonable_encoder` ](https://fastapi.tiangolo.com/reference/encoders/)
    * [ Static Files - `StaticFiles` ](https://fastapi.tiangolo.com/reference/staticfiles/)
    * [ Templating - `Jinja2Templates` ](https://fastapi.tiangolo.com/reference/templating/)
    * [ Test Client - `TestClient` ](https://fastapi.tiangolo.com/reference/testclient/)
  * [ FastAPI People  ](https://fastapi.tiangolo.com/fastapi-people/)
  * [ Resources  ](https://fastapi.tiangolo.com/resources/)
    * [ Help FastAPI - Get Help  ](https://fastapi.tiangolo.com/help-fastapi/)
    * [ Development - Contributing  ](https://fastapi.tiangolo.com/contributing/)
    * [ Full Stack FastAPI Template  ](https://fastapi.tiangolo.com/project-generation/)
    * [ External Links  ](https://fastapi.tiangolo.com/external-links/)
    * [ FastAPI and friends newsletter  ](https://fastapi.tiangolo.com/newsletter/)
    * [ Repository Management Tasks  ](https://fastapi.tiangolo.com/management-tasks/)
  * [ About  ](https://fastapi.tiangolo.com/about/)
    * [ Alternatives, Inspiration and Comparisons  ](https://fastapi.tiangolo.com/alternatives/)
    * [ History, Design and Future  ](https://fastapi.tiangolo.com/history-design-future/)
    * [ Benchmarks  ](https://fastapi.tiangolo.com/benchmarks/)
    * [ Repository Management  ](https://fastapi.tiangolo.com/management/)
  * [ Release Notes  ](https://fastapi.tiangolo.com/release-notes/)


  * [ An example file structure  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure)
  * [ `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter)
    * [ Import `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter)
    * [ _Path operations_ with `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#path-operations-with-apirouter)
  * [ Dependencies  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#dependencies)
  * [ Another module with `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter)
    * [ Import the dependencies  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-dependencies)
      * [ How relative imports work  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-relative-imports-work)
    * [ Add some custom `tags`, `responses`, and `dependencies` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#add-some-custom-tags-responses-and-dependencies)
  * [ The main `FastAPI` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi)
    * [ Import `FastAPI` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi)
    * [ Import the `APIRouter` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-apirouter)
    * [ How the importing works  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-the-importing-works)
    * [ Avoid name collisions  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#avoid-name-collisions)
    * [ Include the `APIRouter`s for `users` and `items` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-apirouters-for-users-and-items)
    * [ Include an `APIRouter` with a custom `prefix`, `tags`, `responses`, and `dependencies` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies)
    * [ Include a _path operation_ ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-a-path-operation)
  * [ Configure the `entrypoint` in `pyproject.toml` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#configure-the-entrypoint-in-pyproject-toml)
  * [ Check the automatic API docs  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#check-the-automatic-api-docs)
  * [ Include the same router multiple times with different `prefix` ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-same-router-multiple-times-with-different-prefix)
  * [ Include an `APIRouter` in another  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-in-another)


  1. [ FastAPI  ](https://fastapi.tiangolo.com/)
  2. [ Learn  ](https://fastapi.tiangolo.com/learn/)
  3. [ Tutorial - User Guide  ](https://fastapi.tiangolo.com/tutorial/)


# Bigger Applications - Multiple Files[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#bigger-applications-multiple-files)
If you are building an application or a web API, it's rarely the case that you can put everything in a single file.
**FastAPI** provides a convenience tool to structure your application while keeping all the flexibility.
Info
If you come from Flask, this would be the equivalent of Flask's Blueprints.
## An example file structure[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure)
Let's say you have a file structure like this:
```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py

```

Tip
There are several `__init__.py` files: one in each directory or subdirectory.
This is what allows importing code from one file into another.
For example, in `app/main.py` you could have a line like:
```
from app.routers import items

```

  * The `app` directory contains everything. And it has an empty file `app/__init__.py`, so it is a "Python package" (a collection of "Python modules"): `app`.
  * It contains an `app/main.py` file. As it is inside a Python package (a directory with a file `__init__.py`), it is a "module" of that package: `app.main`.
  * There's also an `app/dependencies.py` file, just like `app/main.py`, it is a "module": `app.dependencies`.
  * There's a subdirectory `app/routers/` with another file `__init__.py`, so it's a "Python subpackage": `app.routers`.
  * The file `app/routers/items.py` is inside a package, `app/routers/`, so, it's a submodule: `app.routers.items`.
  * The same with `app/routers/users.py`, it's another submodule: `app.routers.users`.
  * There's also a subdirectory `app/internal/` with another file `__init__.py`, so it's another "Python subpackage": `app.internal`.
  * And the file `app/internal/admin.py` is another submodule: `app.internal.admin`.


![](https://fastapi.tiangolo.com/img/tutorial/bigger-applications/package.drawio.svg)
The same file structure with comments:
```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin

```

##  `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter)
Let's say the file dedicated to handling just users is the submodule at `/app/routers/users.py`.
You want to have the _path operations_ related to your users separated from the rest of the code, to keep it organized.
But it's still part of the same **FastAPI** application/web API (it's part of the same "Python Package").
You can create the _path operations_ for that module using `APIRouter`.
### Import `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-apirouter)
You import it and create an "instance" the same way you would with the class `FastAPI`:
[Python 3.8+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_1_1)
app/routers/users.py```
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

```

###  _Path operations_ with `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#path-operations-with-apirouter)
And then you use it to declare your _path operations_.
Use it the same way you would use the `FastAPI` class:
[Python 3.8+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_2_1)
app/routers/users.py```
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

```

You can think of `APIRouter` as a "mini `FastAPI`" class.
All the same options are supported.
All the same `parameters`, `responses`, `dependencies`, `tags`, etc.
Tip
In this example, the variable is called `router`, but you can name it however you want.
We are going to include this `APIRouter` in the main `FastAPI` app, but first, let's check the dependencies and another `APIRouter`.
## Dependencies[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#dependencies)
We see that we are going to need some dependencies used in several places of the application.
So we put them in their own `dependencies` module (`app/dependencies.py`).
We will now use a simple dependency to read a custom `X-Token` header:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_3_1)
app/dependencies.py```
from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")

```

Tip
We are using an invented header to simplify this example.
But in real cases you will get better results using the integrated [Security utilities](https://fastapi.tiangolo.com/tutorial/security/).
## Another module with `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter)
Let's say you also have the endpoints dedicated to handling "items" from your application in the module at `app/routers/items.py`.
You have _path operations_ for:
  * `/items/`
  * `/items/{item_id}`


It's all the same structure as with `app/routers/users.py`.
But we want to be smarter and simplify the code a bit.
We know all the _path operations_ in this module have the same:
  * Path `prefix`: `/items`.
  * `tags`: (just one tag: `items`).
  * Extra `responses`.
  * `dependencies`: they all need that `X-Token` dependency we created.


So, instead of adding all that to each _path operation_ , we can add it to the `APIRouter`.
[Python 3.8+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_4_1)
app/routers/items.py```
from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}

```

As the path of each _path operation_ has to start with `/`, like in:
```
@router.get("/{item_id}")
async def read_item(item_id: str):
    ...

```

...the prefix must not include a final `/`.
So, the prefix in this case is `/items`.
We can also add a list of `tags` and extra `responses` that will be applied to all the _path operations_ included in this router.
And we can add a list of `dependencies` that will be added to all the _path operations_ in the router and will be executed/solved for each request made to them.
Tip
Note that, much like [dependencies in _path operation decorators_](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/), no value will be passed to your _path operation function_.
The end result is that the item paths are now:
  * `/items/`
  * `/items/{item_id}`


...as we intended.
  * They will be marked with a list of tags that contain a single string `"items"`.
    * These "tags" are especially useful for the automatic interactive documentation systems (using OpenAPI).
  * All of them will include the predefined `responses`.
  * All these _path operations_ will have the list of `dependencies` evaluated/executed before them.
    * If you also declare dependencies in a specific _path operation_ , **they will be executed too**.
    * The router dependencies are executed first, then the [`dependencies` in the decorator](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/), and then the normal parameter dependencies.
    * You can also add [`Security` dependencies with `scopes`](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).


Tip
Having `dependencies` in the `APIRouter` can be used, for example, to require authentication for a whole group of _path operations_. Even if the dependencies are not added individually to each one of them.
Check
The `prefix`, `tags`, `responses`, and `dependencies` parameters are (as in many other cases) just a feature from **FastAPI** to help you avoid code duplication.
### Import the dependencies[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-dependencies)
This code lives in the module `app.routers.items`, the file `app/routers/items.py`.
And we need to get the dependency function from the module `app.dependencies`, the file `app/dependencies.py`.
So we use a relative import with `..` for the dependencies:
[Python 3.8+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_5_1)
app/routers/items.py```
from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}

```

#### How relative imports work[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-relative-imports-work)
Tip
If you know perfectly how imports work, continue to the next section below.
A single dot `.`, like in:
```
from .dependencies import get_token_header

```

would mean:
  * Starting in the same package that this module (the file `app/routers/items.py`) lives in (the directory `app/routers/`)...
  * find the module `dependencies` (an imaginary file at `app/routers/dependencies.py`)...
  * and from it, import the function `get_token_header`.


But that file doesn't exist, our dependencies are in a file at `app/dependencies.py`.
Remember how our app/file structure looks like:
![](https://fastapi.tiangolo.com/img/tutorial/bigger-applications/package.drawio.svg)
* * *
The two dots `..`, like in:
```
from ..dependencies import get_token_header

```

mean:
  * Starting in the same package that this module (the file `app/routers/items.py`) lives in (the directory `app/routers/`)...
  * go to the parent package (the directory `app/`)...
  * and in there, find the module `dependencies` (the file at `app/dependencies.py`)...
  * and from it, import the function `get_token_header`.


That works correctly! 🎉
* * *
The same way, if we had used three dots `...`, like in:
```
from ...dependencies import get_token_header

```

that would mean:
  * Starting in the same package that this module (the file `app/routers/items.py`) lives in (the directory `app/routers/`)...
  * go to the parent package (the directory `app/`)...
  * then go to the parent of that package (there's no parent package, `app` is the top level 😱)...
  * and in there, find the module `dependencies` (the file at `app/dependencies.py`)...
  * and from it, import the function `get_token_header`.


That would refer to some package above `app/`, with its own file `__init__.py`, etc. But we don't have that. So, that would throw an error in our example. 🚨
But now you know how it works, so you can use relative imports in your own apps no matter how complex they are. 🤓
### Add some custom `tags`, `responses`, and `dependencies`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#add-some-custom-tags-responses-and-dependencies)
We are not adding the prefix `/items` nor the `tags=["items"]` to each _path operation_ because we added them to the `APIRouter`.
But we can still add _more_ `tags` that will be applied to a specific _path operation_ , and also some extra `responses` specific to that _path operation_ :
[Python 3.8+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_6_1)
app/routers/items.py```
from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}

```

Tip
This last path operation will have the combination of tags: `["items", "custom"]`.
And it will also have both responses in the documentation, one for `404` and one for `403`.
## The main `FastAPI`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi)
Now, let's see the module at `app/main.py`.
Here's where you import and use the class `FastAPI`.
This will be the main file in your application that ties everything together.
And as most of your logic will now live in its own specific module, the main file will be quite simple.
### Import `FastAPI`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-fastapi)
You import and create a `FastAPI` class as normally.
And we can even declare [global dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/) that will be combined with the dependencies for each `APIRouter`:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_7_1)
app/main.py```
from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

```

### Import the `APIRouter`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#import-the-apirouter)
Now we import the other submodules that have `APIRouter`s:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_8_1)
app/main.py```
from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

```

As the files `app/routers/users.py` and `app/routers/items.py` are submodules that are part of the same Python package `app`, we can use a single dot `.` to import them using "relative imports".
### How the importing works[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#how-the-importing-works)
The section:
```
from .routers import items, users

```

means:
  * Starting in the same package that this module (the file `app/main.py`) lives in (the directory `app/`)...
  * look for the subpackage `routers` (the directory at `app/routers/`)...
  * and from it, import the submodule `items` (the file at `app/routers/items.py`) and `users` (the file at `app/routers/users.py`)...


The module `items` will have a variable `router` (`items.router`). This is the same one we created in the file `app/routers/items.py`, it's an `APIRouter` object.
And then we do the same for the module `users`.
We could also import them like:
```
from app.routers import items, users

```

Info
The first version is a "relative import":
```
from .routers import items, users

```

The second version is an "absolute import":
```
from app.routers import items, users

```

To learn more about Python Packages and Modules, read
### Avoid name collisions[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#avoid-name-collisions)
We are importing the submodule `items` directly, instead of importing just its variable `router`.
This is because we also have another variable named `router` in the submodule `users`.
If we had imported one after the other, like:
```
from .routers.items import router
from .routers.users import router

```

the `router` from `users` would overwrite the one from `items` and we wouldn't be able to use them at the same time.
So, to be able to use both of them in the same file, we import the submodules directly:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_9_1)
app/main.py```
from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

```

### Include the `APIRouter`s for `users` and `items`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-apirouters-for-users-and-items)
Now, let's include the `router`s from the submodules `users` and `items`:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_10_1)
app/main.py```
from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

```

Info
`users.router` contains the `APIRouter` inside of the file `app/routers/users.py`.
And `items.router` contains the `APIRouter` inside of the file `app/routers/items.py`.
With `app.include_router()` we can add each `APIRouter` to the main `FastAPI` application.
It will include all the routes from that router as part of it.
Technical Details
It will actually internally create a _path operation_ for each _path operation_ that was declared in the `APIRouter`.
So, behind the scenes, it will actually work as if everything was the same single app.
Check
You don't have to worry about performance when including routers.
This will take microseconds and will only happen at startup.
So it won't affect performance. ⚡
### Include an `APIRouter` with a custom `prefix`, `tags`, `responses`, and `dependencies`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-with-a-custom-prefix-tags-responses-and-dependencies)
Now, let's imagine your organization gave you the `app/internal/admin.py` file.
It contains an `APIRouter` with some admin _path operations_ that your organization shares between several projects.
For this example it will be super simple. But let's say that because it is shared with other projects in the organization, we cannot modify it and add a `prefix`, `dependencies`, `tags`, etc. directly to the `APIRouter`:
[Python 3.8+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_11_1)
app/internal/admin.py```
from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}

```

But we still want to set a custom `prefix` when including the `APIRouter` so that all its _path operations_ start with `/admin`, we want to secure it with the `dependencies` we already have for this project, and we want to include `tags` and `responses`.
We can declare all that without having to modify the original `APIRouter` by passing those parameters to `app.include_router()`:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_12_1)
app/main.py```
from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

```

That way, the original `APIRouter` will stay unmodified, so we can still share that same `app/internal/admin.py` file with other projects in the organization.
The result is that in our app, each of the _path operations_ from the `admin` module will have:
  * The prefix `/admin`.
  * The tag `admin`.
  * The dependency `get_token_header`.
  * The response `418`. 🍵


But that will only affect that `APIRouter` in our app, not in any other code that uses it.
So, for example, other projects could use the same `APIRouter` with a different authentication method.
### Include a _path operation_[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-a-path-operation)
We can also add _path operations_ directly to the `FastAPI` app.
Here we do it... just to show that we can 🤷:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/bigger-applications/#__tabbed_13_1)
app/main.py```
from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

```

and it will work correctly, together with all the other _path operations_ added with `app.include_router()`.
Very Technical Details
**Note** : this is a very technical detail that you probably can **just skip**.
* * *
The `APIRouter`s are not "mounted", they are not isolated from the rest of the application.
This is because we want to include their _path operations_ in the OpenAPI schema and the user interfaces.
As we cannot just isolate them and "mount" them independently of the rest, the _path operations_ are "cloned" (re-created), not included directly.
## Configure the `entrypoint` in `pyproject.toml`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#configure-the-entrypoint-in-pyproject-toml)
As your FastAPI `app` object lives in `app/main.py`, you can configure the `entrypoint` in your `pyproject.toml` file like this:
```
[tool.fastapi]
entrypoint = "app.main:app"

```

that is equivalent to importing like:
```
from app.main import app

```

That way the `fastapi` command will know where to find your app.
Note
You could also pass the path to the command, like:
```
$ fastapi dev app/main.py

```

But you would have to remember to pass the correct path every time you call the `fastapi` command.
Additionally, other tools might not be able to find it, for example the [VS Code Extension](https://fastapi.tiangolo.com/editor-support/) or `entrypoint` in `pyproject.toml`.
## Check the automatic API docs[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#check-the-automatic-api-docs)
Now, run your app:
```
fastapi dev

fastapi dev
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)




```

And open the docs at
You will see the automatic API docs, including the paths from all the submodules, using the correct paths (and prefixes) and the correct tags:
![](https://fastapi.tiangolo.com/img/tutorial/bigger-applications/image01.png)
## Include the same router multiple times with different `prefix`[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-the-same-router-multiple-times-with-different-prefix)
You can also use `.include_router()` multiple times with the _same_ router using different prefixes.
This could be useful, for example, to expose the same API under different prefixes, e.g. `/api/v1` and `/api/latest`.
This is an advanced usage that you might not really need, but it's there in case you do.
## Include an `APIRouter` in another[¶](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-in-another)
The same way you can include an `APIRouter` in a `FastAPI` application, you can include an `APIRouter` in another `APIRouter` using:
```
router.include_router(other_router)

```

Make sure you do it before including `router` in the `FastAPI` app, so that the _path operations_ from `other_router` are also included.
