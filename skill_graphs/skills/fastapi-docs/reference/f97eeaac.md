# Custom Response Classes - File, HTML, Redirect, Streaming, etc.[¶](https://fastapi.tiangolo.com/reference/responses/#custom-response-classes-file-html-redirect-streaming-etc)
There are several custom response classes you can use to create an instance and return them directly from your _path operations_.
Read more about it in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/).
You can import them directly from `fastapi.responses`:
```
from fastapi.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    ORJSONResponse,
    PlainTextResponse,
    RedirectResponse,
    Response,
    StreamingResponse,
    UJSONResponse,
)

```
