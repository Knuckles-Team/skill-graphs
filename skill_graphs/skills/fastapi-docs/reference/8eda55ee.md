## A `StreamingResponse` with `yield`[¶](https://fastapi.tiangolo.com/advanced/stream-data/#a-streamingresponse-with-yield)
If you declare a `response_class=StreamingResponse` in your _path operation function_ , you can use `yield` to send each chunk of data in turn.
[Python 3.10+](https://fastapi.tiangolo.com/advanced/stream-data/#__tabbed_1_1)
```
from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


message = """
Rick: (stumbles in drunkenly, and turns on the lights) Morty! You gotta come on. You got--... you gotta come with me.
Morty: (rubs his eyes) What, Rick? What's going on?
Rick: I got a surprise for you, Morty.
Morty: It's the middle of the night. What are you talking about?
Rick: (spills alcohol on Morty's bed) Come on, I got a surprise for you. (drags Morty by the ankle) Come on, hurry up. (pulls Morty out of his bed and into the hall)
Morty: Ow! Ow! You're tugging me too hard!
Rick: We gotta go, gotta get outta here, come on. Got a surprise for you Morty.
"""


@app.get("/story/stream", response_class=StreamingResponse)
async def stream_story() -> AsyncIterable[str]:
    for line in message.splitlines():
        yield line

# Code below omitted 👇

```

👀 Full file preview
[Python 3.10+](https://fastapi.tiangolo.com/advanced/stream-data/#__tabbed_2_1)
```
from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


message = """
Rick: (stumbles in drunkenly, and turns on the lights) Morty! You gotta come on. You got--... you gotta come with me.
Morty: (rubs his eyes) What, Rick? What's going on?
Rick: I got a surprise for you, Morty.
Morty: It's the middle of the night. What are you talking about?
Rick: (spills alcohol on Morty's bed) Come on, I got a surprise for you. (drags Morty by the ankle) Come on, hurry up. (pulls Morty out of his bed and into the hall)
Morty: Ow! Ow! You're tugging me too hard!
Rick: We gotta go, gotta get outta here, come on. Got a surprise for you Morty.
"""


@app.get("/story/stream", response_class=StreamingResponse)
async def stream_story() -> AsyncIterable[str]:
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-async", response_class=StreamingResponse)
def stream_story_no_async() -> Iterable[str]:
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-annotation", response_class=StreamingResponse)
async def stream_story_no_annotation():
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-async-no-annotation", response_class=StreamingResponse)
def stream_story_no_async_no_annotation():
    for line in message.splitlines():
        yield line


@app.get("/story/stream-bytes", response_class=StreamingResponse)
async def stream_story_bytes() -> AsyncIterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-async-bytes", response_class=StreamingResponse)
def stream_story_no_async_bytes() -> Iterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-annotation-bytes", response_class=StreamingResponse)
async def stream_story_no_annotation_bytes():
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-async-no-annotation-bytes", response_class=StreamingResponse)
def stream_story_no_async_no_annotation_bytes():
    for line in message.splitlines():
        yield line.encode("utf-8")

```

FastAPI will give each chunk of data to the `StreamingResponse` as is, it won't try to convert it to JSON or anything similar.
### Non-async _path operation functions_[¶](https://fastapi.tiangolo.com/advanced/stream-data/#non-async-path-operation-functions)
You can also use regular `def` functions (without `async`), and use `yield` the same way.
[Python 3.10+](https://fastapi.tiangolo.com/advanced/stream-data/#__tabbed_3_1)
```
# Code above omitted 👆

@app.get("/story/stream-no-async", response_class=StreamingResponse)
def stream_story_no_async() -> Iterable[str]:
    for line in message.splitlines():
        yield line

# Code below omitted 👇

```

👀 Full file preview
[Python 3.10+](https://fastapi.tiangolo.com/advanced/stream-data/#__tabbed_4_1)
```
from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


message = """
Rick: (stumbles in drunkenly, and turns on the lights) Morty! You gotta come on. You got--... you gotta come with me.
Morty: (rubs his eyes) What, Rick? What's going on?
Rick: I got a surprise for you, Morty.
Morty: It's the middle of the night. What are you talking about?
Rick: (spills alcohol on Morty's bed) Come on, I got a surprise for you. (drags Morty by the ankle) Come on, hurry up. (pulls Morty out of his bed and into the hall)
Morty: Ow! Ow! You're tugging me too hard!
Rick: We gotta go, gotta get outta here, come on. Got a surprise for you Morty.
"""


@app.get("/story/stream", response_class=StreamingResponse)
async def stream_story() -> AsyncIterable[str]:
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-async", response_class=StreamingResponse)
def stream_story_no_async() -> Iterable[str]:
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-annotation", response_class=StreamingResponse)
async def stream_story_no_annotation():
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-async-no-annotation", response_class=StreamingResponse)
def stream_story_no_async_no_annotation():
    for line in message.splitlines():
        yield line


@app.get("/story/stream-bytes", response_class=StreamingResponse)
async def stream_story_bytes() -> AsyncIterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-async-bytes", response_class=StreamingResponse)
def stream_story_no_async_bytes() -> Iterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-annotation-bytes", response_class=StreamingResponse)
async def stream_story_no_annotation_bytes():
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-async-no-annotation-bytes", response_class=StreamingResponse)
def stream_story_no_async_no_annotation_bytes():
    for line in message.splitlines():
        yield line.encode("utf-8")

```

### No Annotation[¶](https://fastapi.tiangolo.com/advanced/stream-data/#no-annotation)
You don't really need to declare the return type annotation for streaming binary data.
As FastAPI will not try to convert the data to JSON with Pydantic or serialize it in any way, in this case, the type annotation is only for your editor and tools to use, it won't be used by FastAPI.
[Python 3.10+](https://fastapi.tiangolo.com/advanced/stream-data/#__tabbed_5_1)
```
# Code above omitted 👆

@app.get("/story/stream-no-annotation", response_class=StreamingResponse)
async def stream_story_no_annotation():
    for line in message.splitlines():
        yield line

# Code below omitted 👇

```

👀 Full file preview
[Python 3.10+](https://fastapi.tiangolo.com/advanced/stream-data/#__tabbed_6_1)
```
from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


message = """
Rick: (stumbles in drunkenly, and turns on the lights) Morty! You gotta come on. You got--... you gotta come with me.
Morty: (rubs his eyes) What, Rick? What's going on?
Rick: I got a surprise for you, Morty.
Morty: It's the middle of the night. What are you talking about?
Rick: (spills alcohol on Morty's bed) Come on, I got a surprise for you. (drags Morty by the ankle) Come on, hurry up. (pulls Morty out of his bed and into the hall)
Morty: Ow! Ow! You're tugging me too hard!
Rick: We gotta go, gotta get outta here, come on. Got a surprise for you Morty.
"""


@app.get("/story/stream", response_class=StreamingResponse)
async def stream_story() -> AsyncIterable[str]:
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-async", response_class=StreamingResponse)
def stream_story_no_async() -> Iterable[str]:
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-annotation", response_class=StreamingResponse)
async def stream_story_no_annotation():
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-async-no-annotation", response_class=StreamingResponse)
def stream_story_no_async_no_annotation():
    for line in message.splitlines():
        yield line


@app.get("/story/stream-bytes", response_class=StreamingResponse)
async def stream_story_bytes() -> AsyncIterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-async-bytes", response_class=StreamingResponse)
def stream_story_no_async_bytes() -> Iterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-annotation-bytes", response_class=StreamingResponse)
async def stream_story_no_annotation_bytes():
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-async-no-annotation-bytes", response_class=StreamingResponse)
def stream_story_no_async_no_annotation_bytes():
    for line in message.splitlines():
        yield line.encode("utf-8")

```

This also means that with `StreamingResponse` you have the **freedom** and **responsibility** to produce and encode the data bytes exactly as you need them to be sent, independent of the type annotations. 🤓
### Stream Bytes[¶](https://fastapi.tiangolo.com/advanced/stream-data/#stream-bytes)
One of the main use cases would be to stream `bytes` instead of strings, you can of course do it.
[Python 3.10+](https://fastapi.tiangolo.com/advanced/stream-data/#__tabbed_7_1)
```
# Code above omitted 👆

@app.get("/story/stream-bytes", response_class=StreamingResponse)
async def stream_story_bytes() -> AsyncIterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")

# Code below omitted 👇

```

👀 Full file preview
[Python 3.10+](https://fastapi.tiangolo.com/advanced/stream-data/#__tabbed_8_1)
```
from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


message = """
Rick: (stumbles in drunkenly, and turns on the lights) Morty! You gotta come on. You got--... you gotta come with me.
Morty: (rubs his eyes) What, Rick? What's going on?
Rick: I got a surprise for you, Morty.
Morty: It's the middle of the night. What are you talking about?
Rick: (spills alcohol on Morty's bed) Come on, I got a surprise for you. (drags Morty by the ankle) Come on, hurry up. (pulls Morty out of his bed and into the hall)
Morty: Ow! Ow! You're tugging me too hard!
Rick: We gotta go, gotta get outta here, come on. Got a surprise for you Morty.
"""


@app.get("/story/stream", response_class=StreamingResponse)
async def stream_story() -> AsyncIterable[str]:
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-async", response_class=StreamingResponse)
def stream_story_no_async() -> Iterable[str]:
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-annotation", response_class=StreamingResponse)
async def stream_story_no_annotation():
    for line in message.splitlines():
        yield line


@app.get("/story/stream-no-async-no-annotation", response_class=StreamingResponse)
def stream_story_no_async_no_annotation():
    for line in message.splitlines():
        yield line


@app.get("/story/stream-bytes", response_class=StreamingResponse)
async def stream_story_bytes() -> AsyncIterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-async-bytes", response_class=StreamingResponse)
def stream_story_no_async_bytes() -> Iterable[bytes]:
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-annotation-bytes", response_class=StreamingResponse)
async def stream_story_no_annotation_bytes():
    for line in message.splitlines():
        yield line.encode("utf-8")


@app.get("/story/stream-no-async-no-annotation-bytes", response_class=StreamingResponse)
def stream_story_no_async_no_annotation_bytes():
    for line in message.splitlines():
        yield line.encode("utf-8")

```
