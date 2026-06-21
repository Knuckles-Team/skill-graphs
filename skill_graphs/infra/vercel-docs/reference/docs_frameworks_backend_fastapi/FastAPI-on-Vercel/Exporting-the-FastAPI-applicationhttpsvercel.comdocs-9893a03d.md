##  [Exporting the FastAPI application](https://vercel.com/docs/getting-started-with-vercel#exporting-the-fastapi-application)[](https://vercel.com/docs/getting-started-with-vercel#exporting-the-fastapi-application)
To run a FastAPI application on Vercel, define an `app` instance that initializes `FastAPI` at any of the following entrypoints:
  * `app.py`
  * `index.py`
  * `server.py`
  * `src/app.py`
  * `src/index.py`
  * `src/server.py`
  * `app/app.py`
  * `app/index.py`
  * `app/server.py`


For example:
src/index.py
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Python": "on Vercel"}
```

You can also define an application script in `pyproject.toml` to point to your FastAPI app in a different module:
pyproject.toml
```
[project.scripts]
app = "backend.server:app"
```

This script tells Vercel to look for a `FastAPI` instance named `app` in `./backend/server.py`.
###  [Build command](https://vercel.com/docs/getting-started-with-vercel#build-command)[](https://vercel.com/docs/getting-started-with-vercel#build-command)
The `build` property in `[tool.vercel.scripts]` defines the Build Command for FastAPI deployments. It runs after dependencies are installed and before your application is deployed.
pyproject.toml
```
[tool.vercel.scripts]
build = "python build.py"
```

For example:
build.py
```
def main():
    print("Running build command...")
    with open("build.txt", "w") as f:
        f.write("BUILD_COMMAND")

if __name__ == "__main__":
    main()
```

If you define a [Build Command](https://vercel.com/docs/project-configuration#buildcommand) in `vercel.json` or in the Project Settings dashboard, it takes precedence over a build script in `pyproject.toml`.
###  [Local development](https://vercel.com/docs/getting-started-with-vercel#local-development)[](https://vercel.com/docs/getting-started-with-vercel#local-development)
Use `vercel dev` to run your application locally.
terminal
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
vercel dev
```

Minimum CLI version required: 48.1.8
###  [Deploying the application](https://vercel.com/docs/getting-started-with-vercel#deploying-the-application)[](https://vercel.com/docs/getting-started-with-vercel#deploying-the-application)
To deploy, [connect your Git repository](https://vercel.com/new) or [use Vercel CLI](https://vercel.com/docs/cli/deploy):
terminal
```
vc deploy
```

Minimum CLI version required: 48.1.8
