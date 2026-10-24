##  [Serving static assets](https://vercel.com/docs/getting-started-with-vercel#serving-static-assets)[](https://vercel.com/docs/getting-started-with-vercel#serving-static-assets)
To serve static assets, place them in the `public/**` directory. They will be served as a part of our [CDN](https://vercel.com/docs/cdn) using default [headers](https://vercel.com/docs/headers) unless otherwise specified in `vercel.json`.
app.py
```
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    # /vercel.svg is automatically served when included in the public/** directory.
    return RedirectResponse("/vercel.svg", status_code=307)
```

`app.mount("/public", ...)` is not needed and should not be used.
