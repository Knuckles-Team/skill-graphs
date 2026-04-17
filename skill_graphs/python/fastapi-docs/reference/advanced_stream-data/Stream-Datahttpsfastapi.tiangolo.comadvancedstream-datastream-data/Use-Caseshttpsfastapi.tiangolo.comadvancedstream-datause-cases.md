## Use Cases[¶](https://fastapi.tiangolo.com/advanced/stream-data/#use-cases)
You could use this if you want to stream pure strings, for example directly from the output of an **AI LLM** service.
You could also use it to stream **large binary files** , where you stream each chunk of data as you read it, without having to read it all in memory at once.
You could also stream **video** or **audio** this way, it could even be generated as you process and send it.
