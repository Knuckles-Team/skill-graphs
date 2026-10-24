##  [Startup and shutdown](https://vercel.com/docs/getting-started-with-vercel#startup-and-shutdown)[](https://vercel.com/docs/getting-started-with-vercel#startup-and-shutdown)
You can use
main.py
```
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("Starting up...")
    await startup_tasks()
    yield
    # Shutdown logic
    await cleanup_tasks()

app = FastAPI(lifespan=lifespan)
```

Cleanup logic during shutdown is limited to a maximum of 500ms after receiving the [SIGTERM signal](https://vercel.com/docs/functions/functions-api-reference#sigterm-signal). Logs printed during the shutdown step will not appear in the Vercel dashboard.
