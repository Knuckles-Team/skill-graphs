## FastAPI Responses[¶](https://fastapi.tiangolo.com/reference/responses/#fastapi-responses)
There were a couple of custom FastAPI response classes that were intended to optimize JSON performance.
However, they are now deprecated as you will now get better performance by using a [Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/).
That way, Pydantic will serialize the data into JSON bytes on the Rust side, which will achieve better performance than these custom JSON responses.
Read more about it in [Custom Response - HTML, Stream, File, others - `orjson` or Response Model](https://fastapi.tiangolo.com/advanced/custom-response/#orjson-or-response-model).
