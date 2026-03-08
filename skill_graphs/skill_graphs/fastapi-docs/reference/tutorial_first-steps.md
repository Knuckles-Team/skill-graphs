[ Skip to content ](https://fastapi.tiangolo.com/tutorial/first-steps/#first-steps)
[ ![logo](https://fastapi.tiangolo.com/img/icon-white.svg) ](https://fastapi.tiangolo.com/ "FastAPI") FastAPI
  * [ FastAPI  ](https://fastapi.tiangolo.com/)
  * [ Features  ](https://fastapi.tiangolo.com/features/)
  * [ Learn  ](https://fastapi.tiangolo.com/learn/)
    * [ Python Types Intro  ](https://fastapi.tiangolo.com/python-types/)
    * [ Concurrency and async / await  ](https://fastapi.tiangolo.com/async/)
    * [ Environment Variables  ](https://fastapi.tiangolo.com/environment-variables/)
    * [ Virtual Environments  ](https://fastapi.tiangolo.com/virtual-environments/)
    * [ Tutorial - User Guide  ](https://fastapi.tiangolo.com/tutorial/)
      * First Steps  [ First Steps  ](https://fastapi.tiangolo.com/tutorial/first-steps/)
        * [ Check it  ](https://fastapi.tiangolo.com/tutorial/first-steps/#check-it)
        * [ Interactive API docs  ](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs)
        * [ Alternative API docs  ](https://fastapi.tiangolo.com/tutorial/first-steps/#alternative-api-docs)
        * [ OpenAPI  ](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi)
          * [ "Schema"  ](https://fastapi.tiangolo.com/tutorial/first-steps/#schema)
          * [ API "schema"  ](https://fastapi.tiangolo.com/tutorial/first-steps/#api-schema)
          * [ Data "schema"  ](https://fastapi.tiangolo.com/tutorial/first-steps/#data-schema)
          * [ OpenAPI and JSON Schema  ](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi-and-json-schema)
          * [ Check the `openapi.json` ](https://fastapi.tiangolo.com/tutorial/first-steps/#check-the-openapi-json)
          * [ What is OpenAPI for  ](https://fastapi.tiangolo.com/tutorial/first-steps/#what-is-openapi-for)
        * [ Configure the app `entrypoint` in `pyproject.toml` ](https://fastapi.tiangolo.com/tutorial/first-steps/#configure-the-app-entrypoint-in-pyproject-toml)
        * [ `fastapi dev` with path  ](https://fastapi.tiangolo.com/tutorial/first-steps/#fastapi-dev-with-path)
        * [ Deploy your app (optional)  ](https://fastapi.tiangolo.com/tutorial/first-steps/#deploy-your-app-optional)
        * [ Recap, step by step  ](https://fastapi.tiangolo.com/tutorial/first-steps/#recap-step-by-step)
          * [ Step 1: import `FastAPI` ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-1-import-fastapi)
          * [ Step 2: create a `FastAPI` "instance"  ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-2-create-a-fastapi-instance)
          * [ Step 3: create a _path operation_ ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-3-create-a-path-operation)
            * [ Path  ](https://fastapi.tiangolo.com/tutorial/first-steps/#path)
            * [ Operation  ](https://fastapi.tiangolo.com/tutorial/first-steps/#operation)
            * [ Define a _path operation decorator_ ](https://fastapi.tiangolo.com/tutorial/first-steps/#define-a-path-operation-decorator)
          * [ Step 4: define the **path operation function** ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-4-define-the-path-operation-function)
          * [ Step 5: return the content  ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-5-return-the-content)
          * [ Step 6: Deploy it  ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-6-deploy-it)
            * [ About FastAPI Cloud  ](https://fastapi.tiangolo.com/tutorial/first-steps/#about-fastapi-cloud)
            * [ Deploy to other cloud providers  ](https://fastapi.tiangolo.com/tutorial/first-steps/#deploy-to-other-cloud-providers)
        * [ Recap  ](https://fastapi.tiangolo.com/tutorial/first-steps/#recap)
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
      * [ Bigger Applications - Multiple Files  ](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
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


  * [ Check it  ](https://fastapi.tiangolo.com/tutorial/first-steps/#check-it)
  * [ Interactive API docs  ](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs)
  * [ Alternative API docs  ](https://fastapi.tiangolo.com/tutorial/first-steps/#alternative-api-docs)
  * [ OpenAPI  ](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi)
    * [ "Schema"  ](https://fastapi.tiangolo.com/tutorial/first-steps/#schema)
    * [ API "schema"  ](https://fastapi.tiangolo.com/tutorial/first-steps/#api-schema)
    * [ Data "schema"  ](https://fastapi.tiangolo.com/tutorial/first-steps/#data-schema)
    * [ OpenAPI and JSON Schema  ](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi-and-json-schema)
    * [ Check the `openapi.json` ](https://fastapi.tiangolo.com/tutorial/first-steps/#check-the-openapi-json)
    * [ What is OpenAPI for  ](https://fastapi.tiangolo.com/tutorial/first-steps/#what-is-openapi-for)
  * [ Configure the app `entrypoint` in `pyproject.toml` ](https://fastapi.tiangolo.com/tutorial/first-steps/#configure-the-app-entrypoint-in-pyproject-toml)
  * [ `fastapi dev` with path  ](https://fastapi.tiangolo.com/tutorial/first-steps/#fastapi-dev-with-path)
  * [ Deploy your app (optional)  ](https://fastapi.tiangolo.com/tutorial/first-steps/#deploy-your-app-optional)
  * [ Recap, step by step  ](https://fastapi.tiangolo.com/tutorial/first-steps/#recap-step-by-step)
    * [ Step 1: import `FastAPI` ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-1-import-fastapi)
    * [ Step 2: create a `FastAPI` "instance"  ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-2-create-a-fastapi-instance)
    * [ Step 3: create a _path operation_ ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-3-create-a-path-operation)
      * [ Path  ](https://fastapi.tiangolo.com/tutorial/first-steps/#path)
      * [ Operation  ](https://fastapi.tiangolo.com/tutorial/first-steps/#operation)
      * [ Define a _path operation decorator_ ](https://fastapi.tiangolo.com/tutorial/first-steps/#define-a-path-operation-decorator)
    * [ Step 4: define the **path operation function** ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-4-define-the-path-operation-function)
    * [ Step 5: return the content  ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-5-return-the-content)
    * [ Step 6: Deploy it  ](https://fastapi.tiangolo.com/tutorial/first-steps/#step-6-deploy-it)
      * [ About FastAPI Cloud  ](https://fastapi.tiangolo.com/tutorial/first-steps/#about-fastapi-cloud)
      * [ Deploy to other cloud providers  ](https://fastapi.tiangolo.com/tutorial/first-steps/#deploy-to-other-cloud-providers)
  * [ Recap  ](https://fastapi.tiangolo.com/tutorial/first-steps/#recap)


  1. [ FastAPI  ](https://fastapi.tiangolo.com/)
  2. [ Learn  ](https://fastapi.tiangolo.com/learn/)
  3. [ Tutorial - User Guide  ](https://fastapi.tiangolo.com/tutorial/)


# First Steps[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#first-steps)
The simplest FastAPI file could look like this:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/first-steps/#__tabbed_1_1)
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

Copy that to a file `main.py`.
Run the live server:
```
<font color="#4E9A06">fastapi</font> dev

fastapi dev
   FastAPI   Starting development server 🚀

             Searching for package file structure from directories
             with __init__.py files
             Importing from /home/user/code/awesomeapp

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with
             the following code:

             _from __**main**__ import __**app**_

       app   Using import string: main:app

    server   Server started at _http://127.0.0.1:8000_
    server   Documentation at _http://127.0.0.1:8000/docs_

       tip   Running in development mode, for production use:
             **fastapi run**

             Logs:

      INFO   Will watch for changes in these directories:
             **[**'/home/user/code/awesomeapp'**]**
      INFO   Uvicorn running on _http://127.0.0.1:8000_ **(**Press CTRL+C
             to quit**)**
      INFO   Started reloader process **[****383138****]** using WatchFiles
      INFO   Started server process **[****383153****]**
      INFO   Waiting for application startup.
      INFO   Application startup complete.




```

In the output, there's a line with something like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

```

That line shows the URL where your app is being served on your local machine.
### Check it[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#check-it)
Open your browser at
You will see the JSON response as:
```
{"message": "Hello World"}

```

### Interactive API docs[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs)
Now go to
You will see the automatic interactive API documentation (provided by
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Alternative API docs[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#alternative-api-docs)
And now, go to
You will see the alternative automatic documentation (provided by
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
### OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi)
**FastAPI** generates a "schema" with all your API using the **OpenAPI** standard for defining APIs.
#### "Schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#schema)
A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.
#### API "schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#api-schema)
In this case,
This schema definition includes your API paths, the possible parameters they take, etc.
#### Data "schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#data-schema)
The term "schema" might also refer to the shape of some data, like a JSON content.
In that case, it would mean the JSON attributes, and data types they have, etc.
#### OpenAPI and JSON Schema[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi-and-json-schema)
OpenAPI defines an API schema for your API. And that schema includes definitions (or "schemas") of the data sent and received by your API using **JSON Schema** , the standard for JSON data schemas.
#### Check the `openapi.json`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#check-the-openapi-json)
If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.
You can see it directly at:
It will show a JSON starting with something like:
```
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {



...

```

#### What is OpenAPI for[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#what-is-openapi-for)
The OpenAPI schema is what powers the two interactive documentation systems included.
And there are dozens of alternatives, all based on OpenAPI. You could easily add any of those alternatives to your application built with **FastAPI**.
You could also use it to generate code automatically, for clients that communicate with your API. For example, frontend, mobile or IoT applications.
### Configure the app `entrypoint` in `pyproject.toml`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#configure-the-app-entrypoint-in-pyproject-toml)
You can configure where your app is located in a `pyproject.toml` file like:
```
[tool.fastapi]
entrypoint = "main:app"

```

That `entrypoint` will tell the `fastapi` command that it should import the app like:
```
from main import app

```

If your code was structured like:
```
.
├── backend
│   ├── main.py
│   ├── __init__.py

```

Then you would set the `entrypoint` as:
```
[tool.fastapi]
entrypoint = "backend.main:app"

```

which would be equivalent to:
```
from backend.main import app

```

###  `fastapi dev` with path[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#fastapi-dev-with-path)
You can also pass the file path to the `fastapi dev` command, and it will guess the FastAPI app object to use:
```
$ fastapi dev main.py

```

But you would have to remember to pass the correct path every time you call the `fastapi` command.
Additionally, other tools might not be able to find it, for example the [VS Code Extension](https://fastapi.tiangolo.com/editor-support/) or `entrypoint` in `pyproject.toml`.
### Deploy your app (optional)[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#deploy-your-app-optional)
You can optionally deploy your FastAPI app to
If you already have a **FastAPI Cloud** account (we invited you from the waiting list 😉), you can deploy your application with one command.
Before deploying, make sure you are logged in:
```
fastapi login

fastapi login
You are logged in to FastAPI Cloud 🚀




```

Then deploy your app:
```
fastapi deploy

fastapi deploy
Deploying to FastAPI Cloud...

✅ Deployment successful!

🐔 Ready the chicken! Your app is ready at https://myapp.fastapicloud.dev




```

That's it! Now you can access your app at that URL. ✨
## Recap, step by step[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#recap-step-by-step)
### Step 1: import `FastAPI`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-1-import-fastapi)
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/first-steps/#__tabbed_2_1)
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

`FastAPI` is a Python class that provides all the functionality for your API.
Technical Details
`FastAPI` is a class that inherits directly from `Starlette`.
You can use all the `FastAPI` too.
### Step 2: create a `FastAPI` "instance"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-2-create-a-fastapi-instance)
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/first-steps/#__tabbed_3_1)
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

Here the `app` variable will be an "instance" of the class `FastAPI`.
This will be the main point of interaction to create all your API.
### Step 3: create a _path operation_[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-3-create-a-path-operation)
#### Path[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#path)
"Path" here refers to the last part of the URL starting from the first `/`.
So, in a URL like:
```
https://example.com/items/foo

```

...the path would be:
```
/items/foo

```

Info
A "path" is also commonly called an "endpoint" or a "route".
While building an API, the "path" is the main way to separate "concerns" and "resources".
#### Operation[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#operation)
"Operation" here refers to one of the HTTP "methods".
One of:
  * `POST`
  * `GET`
  * `PUT`
  * `DELETE`


...and the more exotic ones:
  * `OPTIONS`
  * `HEAD`
  * `PATCH`
  * `TRACE`


In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".
* * *
When building APIs, you normally use these specific HTTP methods to perform a specific action.
Normally you use:
  * `POST`: to create data.
  * `GET`: to read data.
  * `PUT`: to update data.
  * `DELETE`: to delete data.


So, in OpenAPI, each of the HTTP methods is called an "operation".
We are going to call them "**operations** " too.
#### Define a _path operation decorator_[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#define-a-path-operation-decorator)
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/first-steps/#__tabbed_4_1)
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

The `@app.get("/")` tells **FastAPI** that the function right below is in charge of handling requests that go to:
  * the path `/`
  * using a `get` operation


`@decorator` Info
That `@something` syntax in Python is called a "decorator".
You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).
A "decorator" takes the function below and does something with it.
In our case, this decorator tells **FastAPI** that the function below corresponds to the **path** `/` with an **operation** `get`.
It is the "**path operation decorator** ".
You can also use the other operations:
  * `@app.post()`
  * `@app.put()`
  * `@app.delete()`


And the more exotic ones:
  * `@app.options()`
  * `@app.head()`
  * `@app.patch()`
  * `@app.trace()`


Tip
You are free to use each operation (HTTP method) as you wish.
**FastAPI** doesn't enforce any specific meaning.
The information here is presented as a guideline, not a requirement.
For example, when using GraphQL you normally perform all the actions using only `POST` operations.
### Step 4: define the **path operation function**[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-4-define-the-path-operation-function)
This is our "**path operation function** ":
  * **path** : is `/`.
  * **operation** : is `get`.
  * **function** : is the function below the "decorator" (below `@app.get("/")`).


[Python 3.10+](https://fastapi.tiangolo.com/tutorial/first-steps/#__tabbed_5_1)
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

This is a Python function.
It will be called by **FastAPI** whenever it receives a request to the URL "`/`" using a `GET` operation.
In this case, it is an `async` function.
* * *
You could also define it as a normal function instead of `async def`:
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/first-steps/#__tabbed_6_1)
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

```

Note
If you don't know the difference, check the [Async: _"In a hurry?"_](https://fastapi.tiangolo.com/async/#in-a-hurry).
### Step 5: return the content[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-5-return-the-content)
[Python 3.10+](https://fastapi.tiangolo.com/tutorial/first-steps/#__tabbed_7_1)
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

You can return a `dict`, `list`, singular values as `str`, `int`, etc.
You can also return Pydantic models (you'll see more about that later).
There are many other objects and models that will be automatically converted to JSON (including ORMs, etc). Try using your favorite ones, it's highly probable that they are already supported.
### Step 6: Deploy it[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-6-deploy-it)
Deploy your app to `fastapi deploy`. 🎉
#### About FastAPI Cloud[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#about-fastapi-cloud)
**FastAPI**.
It streamlines the process of **building** , **deploying** , and **accessing** an API with minimal effort.
It brings the same **developer experience** of building apps with FastAPI to **deploying** them to the cloud. 🎉
FastAPI Cloud is the primary sponsor and funding provider for the _FastAPI and friends_ open source projects. ✨
#### Deploy to other cloud providers[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#deploy-to-other-cloud-providers)
FastAPI is open source and based on standards. You can deploy FastAPI apps to any cloud provider you choose.
Follow your cloud provider's guides to deploy FastAPI apps with them. 🤓
## Recap[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#recap)
  * Import `FastAPI`.
  * Create an `app` instance.
  * Write a **path operation decorator** using decorators like `@app.get("/")`.
  * Define a **path operation function** ; for example, `def root(): ...`.
  * Run the development server using the command `fastapi dev`.
  * Optionally deploy your app with `fastapi deploy`.
