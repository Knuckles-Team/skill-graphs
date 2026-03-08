    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncExa(api_key=api_key)
    return Tool[Any](
        ExaSearchTool(
            client=client,
            num_results=num_results,
            max_characters=max_characters,
        ).__call__,
        name='exa_search',
        description='Searches Exa for the given query and returns the results with content. Exa is a neural search engine that finds high-quality, relevant results.',
    )

```

---|---
###  exa_find_similar_tool
```
exa_find_similar_tool(
    api_key: , *, num_results:  = 5
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
exa_find_similar_tool(
    *, client: AsyncExa, num_results:  = 5
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
exa_find_similar_tool(
    api_key:  | None = None,
    *,
    client: AsyncExa | None = None,
    num_results:  = 5
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

Creates an Exa find similar tool.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The Exa API key. Required if `client` is not provided. You can get one by signing up at  |  `None`
`client` |  `AsyncExa | None` |  An existing AsyncExa client. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tools. |  `None`
`num_results` |  |  The number of similar results to return. Defaults to 5. |  `5`
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
```
| ```
def exa_find_similar_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
    num_results: int = 5,
) -> Tool[Any]:
    """Creates an Exa find similar tool.

    Args:
        api_key: The Exa API key. Required if `client` is not provided.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        client: An existing AsyncExa client. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tools.
        num_results: The number of similar results to return. Defaults to 5.
    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncExa(api_key=api_key)
    return Tool[Any](
        ExaFindSimilarTool(client=client, num_results=num_results).__call__,
        name='exa_find_similar',
        description='Finds web pages similar to a given URL. Useful for discovering related content, competitors, or alternative sources.',
    )

```

---|---
###  exa_get_contents_tool
```
exa_get_contents_tool(api_key: ) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
exa_get_contents_tool(*, client: AsyncExa) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
exa_get_contents_tool(
    api_key:  | None = None,
    *,
    client: AsyncExa | None = None
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

Creates an Exa get contents tool.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The Exa API key. Required if `client` is not provided. You can get one by signing up at  |  `None`
`client` |  `AsyncExa | None` |  An existing AsyncExa client. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tools. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
```
| ```
def exa_get_contents_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
) -> Tool[Any]:
    """Creates an Exa get contents tool.

    Args:
        api_key: The Exa API key. Required if `client` is not provided.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        client: An existing AsyncExa client. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tools.
    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncExa(api_key=api_key)
    return Tool[Any](
        ExaGetContentsTool(client=client).__call__,
        name='exa_get_contents',
        description='Gets the full text content of specified URLs. Useful for reading articles, documentation, or any web page when you have the exact URL.',
    )

```

---|---
###  exa_answer_tool
```
exa_answer_tool(api_key: ) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
exa_answer_tool(*, client: AsyncExa) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
exa_answer_tool(
    api_key:  | None = None,
    *,
    client: AsyncExa | None = None
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

Creates an Exa answer tool.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The Exa API key. Required if `client` is not provided. You can get one by signing up at  |  `None`
`client` |  `AsyncExa | None` |  An existing AsyncExa client. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tools. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
```
| ```
def exa_answer_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
) -> Tool[Any]:
    """Creates an Exa answer tool.

    Args:
        api_key: The Exa API key. Required if `client` is not provided.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        client: An existing AsyncExa client. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tools.
    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncExa(api_key=api_key)
    return Tool[Any](
        ExaAnswerTool(client=client).__call__,
        name='exa_answer',
        description='Generates an AI-powered answer to a question with citations from web sources. Returns a comprehensive answer backed by real sources.',
    )

```

---|---
###  ExaToolset
Bases: `FunctionToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FunctionToolset "FunctionToolset \(pydantic_ai.FunctionToolset\)")`
A toolset that provides Exa search tools with a shared client.
This is more efficient than creating individual tools when using multiple Exa tools, as it shares a single API client across all tools.
Example:
```
from pydantic_ai import Agent
from pydantic_ai.common_tools.exa import ExaToolset

toolset = ExaToolset(api_key='your-api-key')
agent = Agent('openai:gpt-5.2', toolsets=[toolset])

```

Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
```
| ```
class ExaToolset(FunctionToolset):
    """A toolset that provides Exa search tools with a shared client.

    This is more efficient than creating individual tools when using multiple
    Exa tools, as it shares a single API client across all tools.

    Example:
```python
    from pydantic_ai import Agent
    from pydantic_ai.common_tools.exa import ExaToolset

    toolset = ExaToolset(api_key='your-api-key')
    agent = Agent('openai:gpt-5.2', toolsets=[toolset])
```
    """

    def __init__(
        self,
        api_key: str,
        *,
        num_results: int = 5,
        max_characters: int | None = None,
        include_search: bool = True,
        include_find_similar: bool = True,
        include_get_contents: bool = True,
        include_answer: bool = True,
        id: str | None = None,
    ):
        """Creates an Exa toolset with a shared client.

        Args:
            api_key: The Exa API key.

                You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
            num_results: The number of results to return for search and find_similar. Defaults to 5.
            max_characters: Maximum characters of text content per result. Use this to limit
                token usage. Defaults to None (no limit).
            include_search: Whether to include the search tool. Defaults to True.
            include_find_similar: Whether to include the find_similar tool. Defaults to True.
            include_get_contents: Whether to include the get_contents tool. Defaults to True.
            include_answer: Whether to include the answer tool. Defaults to True.
            id: Optional ID for the toolset, used for durable execution environments.
        """
        client = AsyncExa(api_key=api_key)
        tools: list[Tool[Any]] = []

        if include_search:
            tools.append(exa_search_tool(client=client, num_results=num_results, max_characters=max_characters))

        if include_find_similar:
            tools.append(exa_find_similar_tool(client=client, num_results=num_results))

        if include_get_contents:
            tools.append(exa_get_contents_tool(client=client))

        if include_answer:
            tools.append(exa_answer_tool(client=client))

        super().__init__(tools, id=id)

```

---|---
####  __init__
```
__init__(
    api_key: ,
    *,
    num_results:  = 5,
    max_characters:  | None = None,
    include_search:  = True,
    include_find_similar:  = True,
    include_get_contents:  = True,
    include_answer:  = True,
    id:  | None = None
)

```

Creates an Exa toolset with a shared client.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The Exa API key. You can get one by signing up at  |  _required_
`num_results` |  |  The number of results to return for search and find_similar. Defaults to 5. |  `5`
`max_characters` |  |  Maximum characters of text content per result. Use this to limit token usage. Defaults to None (no limit). |  `None`
`include_search` |  |  Whether to include the search tool. Defaults to True. |  `True`
`include_find_similar` |  |  Whether to include the find_similar tool. Defaults to True. |  `True`
`include_get_contents` |  |  Whether to include the get_contents tool. Defaults to True. |  `True`
`include_answer` |  |  Whether to include the answer tool. Defaults to True. |  `True`
`id` |  |  Optional ID for the toolset, used for durable execution environments. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
```
| ```
def __init__(
    self,
    api_key: str,
    *,
    num_results: int = 5,
    max_characters: int | None = None,
    include_search: bool = True,
    include_find_similar: bool = True,
    include_get_contents: bool = True,
    include_answer: bool = True,
    id: str | None = None,
):
    """Creates an Exa toolset with a shared client.

    Args:
        api_key: The Exa API key.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        num_results: The number of results to return for search and find_similar. Defaults to 5.
        max_characters: Maximum characters of text content per result. Use this to limit
            token usage. Defaults to None (no limit).
        include_search: Whether to include the search tool. Defaults to True.
        include_find_similar: Whether to include the find_similar tool. Defaults to True.
        include_get_contents: Whether to include the get_contents tool. Defaults to True.
        include_answer: Whether to include the answer tool. Defaults to True.
        id: Optional ID for the toolset, used for durable execution environments.
    """
    client = AsyncExa(api_key=api_key)
    tools: list[Tool[Any]] = []

    if include_search:
        tools.append(exa_search_tool(client=client, num_results=num_results, max_characters=max_characters))

    if include_find_similar:
        tools.append(exa_find_similar_tool(client=client, num_results=num_results))

    if include_get_contents:
        tools.append(exa_get_contents_tool(client=client))

    if include_answer:
        tools.append(exa_answer_tool(client=client))

    super().__init__(tools, id=id)

```

---|---
###  TavilySearchResult
Bases:
A Tavily search result.
See
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/tavily.py`
```
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
```
| ```
class TavilySearchResult(TypedDict):
    """A Tavily search result.

    See [Tavily Search Endpoint documentation](https://docs.tavily.com/api-reference/endpoint/search)
    for more information.
    """

    title: str
    """The title of the search result."""
    url: str
    """The URL of the search result.."""
    content: str
    """A short description of the search result."""
    score: float
    """The relevance score of the search result."""

```

---|---
####  title `instance-attribute`
```
title:

```

The title of the search result.
####  url `instance-attribute`
```
url:

```

The URL of the search result..
####  content `instance-attribute`
```
content:

```

A short description of the search result.
####  score `instance-attribute`
```
score:

```

The relevance score of the search result.
###  TavilySearchTool `dataclass`
The Tavily search tool.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/tavily.py`
```
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
```
| ```
@dataclass
class TavilySearchTool:
    """The Tavily search tool."""

    client: AsyncTavilyClient
    """The Tavily search client."""

    _: KW_ONLY

    max_results: int | None = None
    """The maximum number of results. If None, the Tavily default is used."""

    async def __call__(
        self,
        query: str,
        search_depth: Literal['basic', 'advanced', 'fast', 'ultra-fast'] = 'basic',
        topic: Literal['general', 'news', 'finance'] = 'general',
        time_range: Literal['day', 'week', 'month', 'year'] | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
    ) -> list[TavilySearchResult]:
        """Searches Tavily for the given query and returns the results.

        Args:
            query: The search query to execute with Tavily.
            search_depth: The depth of the search.
            topic: The category of the search.
            time_range: The time range back from the current date to filter results.
            include_domains: List of domains to specifically include in the search results.
            exclude_domains: List of domains to specifically exclude from the search results.

        Returns:
            A list of search results from Tavily.
        """
        results: dict[str, Any] = await self.client.search(  # pyright: ignore[reportUnknownMemberType,reportUnknownVariableType]
            query,
            search_depth=search_depth,
            topic=topic,
            time_range=time_range,  # pyright: ignore[reportArgumentType]
            max_results=self.max_results,  # pyright: ignore[reportArgumentType]
            include_domains=include_domains,  # pyright: ignore[reportArgumentType]
            exclude_domains=exclude_domains,  # pyright: ignore[reportArgumentType]
        )
        return tavily_search_ta.validate_python(results['results'])

```

---|---
####  client `instance-attribute`
```
client: AsyncTavilyClient

```

The Tavily search client.
####  max_results `class-attribute` `instance-attribute`
```
max_results:  | None = None

```

The maximum number of results. If None, the Tavily default is used.
####  __call__ `async`
```
__call__(
    query: ,
    search_depth: [
        "basic", "advanced", "fast", "ultra-fast"
    ] = "basic",
    topic: [
        "general", "news", "finance"
    ] = "general",
    time_range: (
        ["day", "week", "month", "year"] | None
    ) = None,
    include_domains: [] | None = None,
    exclude_domains: [] | None = None,
) -> [TavilySearchResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.tavily.TavilySearchResult "TavilySearchResult \(pydantic_ai.common_tools.tavily.TavilySearchResult\)")]

```

Searches Tavily for the given query and returns the results.
Parameters:
Name | Type | Description | Default
---|---|---|---
`query` |  |  The search query to execute with Tavily. |  _required_
`search_depth` |  |  The depth of the search. |  `'basic'`
`topic` |  |  The category of the search. |  `'general'`
`time_range` |  |  The time range back from the current date to filter results. |  `None`
`include_domains` |  |  List of domains to specifically include in the search results. |  `None`
`exclude_domains` |  |  List of domains to specifically exclude from the search results. |  `None`
Returns:
Type | Description
---|---
`TavilySearchResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.tavily.TavilySearchResult "TavilySearchResult \(pydantic_ai.common_tools.tavily.TavilySearchResult\)")]` |  A list of search results from Tavily.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/tavily.py`
```
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
```
| ```
async def __call__(
    self,
    query: str,
    search_depth: Literal['basic', 'advanced', 'fast', 'ultra-fast'] = 'basic',
    topic: Literal['general', 'news', 'finance'] = 'general',
    time_range: Literal['day', 'week', 'month', 'year'] | None = None,
    include_domains: list[str] | None = None,
    exclude_domains: list[str] | None = None,
) -> list[TavilySearchResult]:
    """Searches Tavily for the given query and returns the results.

    Args:
        query: The search query to execute with Tavily.
        search_depth: The depth of the search.
        topic: The category of the search.
        time_range: The time range back from the current date to filter results.
        include_domains: List of domains to specifically include in the search results.
        exclude_domains: List of domains to specifically exclude from the search results.

    Returns:
        A list of search results from Tavily.
    """
    results: dict[str, Any] = await self.client.search(  # pyright: ignore[reportUnknownMemberType,reportUnknownVariableType]
        query,
        search_depth=search_depth,
        topic=topic,
        time_range=time_range,  # pyright: ignore[reportArgumentType]
        max_results=self.max_results,  # pyright: ignore[reportArgumentType]
        include_domains=include_domains,  # pyright: ignore[reportArgumentType]
        exclude_domains=exclude_domains,  # pyright: ignore[reportArgumentType]
    )
    return tavily_search_ta.validate_python(results['results'])

```

---|---
###  tavily_search_tool
```
tavily_search_tool(
    api_key: ,
    *,
    max_results:  | None = None,
    search_depth: [
        "basic", "advanced", "fast", "ultra-fast"
    ] = _UNSET,
    topic: ["general", "news", "finance"] = _UNSET,
    time_range: (
        ["day", "week", "month", "year"] | None
    ) = _UNSET,
    include_domains: [] | None = _UNSET,
    exclude_domains: [] | None = _UNSET
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
tavily_search_tool(
    *,
    client: AsyncTavilyClient,
    max_results:  | None = None,
    search_depth: [
        "basic", "advanced", "fast", "ultra-fast"
    ] = _UNSET,
    topic: ["general", "news", "finance"] = _UNSET,
    time_range: (
        ["day", "week", "month", "year"] | None
    ) = _UNSET,
    include_domains: [] | None = _UNSET,
    exclude_domains: [] | None = _UNSET
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
tavily_search_tool(
    api_key:  | None = None,
    *,
    client: AsyncTavilyClient | None = None,
    max_results:  | None = None,
    search_depth: [
        "basic", "advanced", "fast", "ultra-fast"
    ] = _UNSET,
    topic: ["general", "news", "finance"] = _UNSET,
    time_range: (
        ["day", "week", "month", "year"] | None
    ) = _UNSET,
    include_domains: [] | None = _UNSET,
    exclude_domains: [] | None = _UNSET
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

Creates a Tavily search tool.
`max_results` is always developer-controlled and does not appear in the LLM tool schema. Other parameters, when provided, are fixed for all searches and hidden from the LLM's tool schema. Parameters left unset remain available for the LLM to set per-call.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The Tavily API key. Required if `client` is not provided. You can get one by signing up at  |  `None`
`client` |  `AsyncTavilyClient | None` |  An existing AsyncTavilyClient. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tool instances. |  `None`
`max_results` |  |  The maximum number of results. If None, the Tavily default is used. |  `None`
`search_depth` |  |  The depth of the search. |  `_UNSET`
`topic` |  |  The category of the search. |  `_UNSET`
`time_range` |  |  The time range back from the current date to filter results. |  `_UNSET`
`include_domains` |  |  List of domains to specifically include in the search results. |  `_UNSET`
`exclude_domains` |  |  List of domains to specifically exclude from the search results. |  `_UNSET`
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/tavily.py`
```
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
```
| ```
def tavily_search_tool(
    api_key: str | None = None,
    *,
    client: AsyncTavilyClient | None = None,
    max_results: int | None = None,
    search_depth: Literal['basic', 'advanced', 'fast', 'ultra-fast'] = _UNSET,
    topic: Literal['general', 'news', 'finance'] = _UNSET,
    time_range: Literal['day', 'week', 'month', 'year'] | None = _UNSET,
    include_domains: list[str] | None = _UNSET,
    exclude_domains: list[str] | None = _UNSET,
) -> Tool[Any]:
    """Creates a Tavily search tool.

    `max_results` is always developer-controlled and does not appear in the LLM tool schema.
    Other parameters, when provided, are fixed for all searches and hidden from the LLM's
    tool schema. Parameters left unset remain available for the LLM to set per-call.

    Args:
        api_key: The Tavily API key. Required if `client` is not provided.

            You can get one by signing up at [https://app.tavily.com/home](https://app.tavily.com/home).
        client: An existing AsyncTavilyClient. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tool instances.
        max_results: The maximum number of results. If None, the Tavily default is used.
        search_depth: The depth of the search.
        topic: The category of the search.
        time_range: The time range back from the current date to filter results.
        include_domains: List of domains to specifically include in the search results.
        exclude_domains: List of domains to specifically exclude from the search results.
    """
    if client is None:
        if api_key is None:
            raise ValueError('Either api_key or client must be provided')
        client = AsyncTavilyClient(api_key)
    func = TavilySearchTool(client=client, max_results=max_results).__call__

    kwargs: dict[str, Any] = {}
    if search_depth is not _UNSET:
        kwargs['search_depth'] = search_depth
    if topic is not _UNSET:
        kwargs['topic'] = topic
    if time_range is not _UNSET:
        kwargs['time_range'] = time_range
    if include_domains is not _UNSET:
        kwargs['include_domains'] = include_domains
    if exclude_domains is not _UNSET:
        kwargs['exclude_domains'] = exclude_domains

    if kwargs:
        original = func
        func = partial(func, **kwargs)
