# `pydantic_ai.common_tools`
###  DuckDuckGoResult
Bases:
A DuckDuckGo search result.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py`
```
24
25
26
27
28
29
30
31
32
```
| ```
class DuckDuckGoResult(TypedDict):
    """A DuckDuckGo search result."""

    title: str
    """The title of the search result."""
    href: str
    """The URL of the search result."""
    body: str
    """The body of the search result."""

```

---|---
####  title `instance-attribute`
```
title:

```

The title of the search result.
####  href `instance-attribute`
```
href:

```

The URL of the search result.
####  body `instance-attribute`
```
body:

```

The body of the search result.
###  DuckDuckGoSearchTool `dataclass`
The DuckDuckGo search tool.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py`
```
38
39
40
41
42
43
44
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
```
| ```
@dataclass
class DuckDuckGoSearchTool:
    """The DuckDuckGo search tool."""

    client: DDGS
    """The DuckDuckGo search client."""

    _: KW_ONLY

    max_results: int | None
    """The maximum number of results. If None, returns results only from the first response."""

    async def __call__(self, query: str) -> list[DuckDuckGoResult]:
        """Searches DuckDuckGo for the given query and returns the results.

        Args:
            query: The query to search for.

        Returns:
            The search results.
        """
        search = functools.partial(self.client.text, max_results=self.max_results)
        results = await anyio.to_thread.run_sync(search, query)
        return duckduckgo_ta.validate_python(results)

```

---|---
####  client `instance-attribute`
```
client: DDGS

```

The DuckDuckGo search client.
####  max_results `instance-attribute`
```
max_results:  | None

```

The maximum number of results. If None, returns results only from the first response.
####  __call__ `async`
```
__call__(query: ) -> [DuckDuckGoResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.duckduckgo.DuckDuckGoResult "DuckDuckGoResult \(pydantic_ai.common_tools.duckduckgo.DuckDuckGoResult\)")]

```

Searches DuckDuckGo for the given query and returns the results.
Parameters:
Name | Type | Description | Default
---|---|---|---
`query` |  |  The query to search for. |  _required_
Returns:
Type | Description
---|---
`DuckDuckGoResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.duckduckgo.DuckDuckGoResult "DuckDuckGoResult \(pydantic_ai.common_tools.duckduckgo.DuckDuckGoResult\)")]` |  The search results.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py`
```
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
```
| ```
async def __call__(self, query: str) -> list[DuckDuckGoResult]:
    """Searches DuckDuckGo for the given query and returns the results.

    Args:
        query: The query to search for.

    Returns:
        The search results.
    """
    search = functools.partial(self.client.text, max_results=self.max_results)
    results = await anyio.to_thread.run_sync(search, query)
    return duckduckgo_ta.validate_python(results)

```

---|---
###  duckduckgo_search_tool
```
duckduckgo_search_tool(
    duckduckgo_client: DDGS | None = None,
    max_results:  | None = None,
)

```

Creates a DuckDuckGo search tool.
Parameters:
Name | Type | Description | Default
---|---|---|---
`duckduckgo_client` |  `DDGS | None` |  The DuckDuckGo search client. |  `None`
`max_results` |  |  The maximum number of results. If None, returns results only from the first response. |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py`
```
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
```
| ```
def duckduckgo_search_tool(duckduckgo_client: DDGS | None = None, max_results: int | None = None):
    """Creates a DuckDuckGo search tool.

    Args:
        duckduckgo_client: The DuckDuckGo search client.
        max_results: The maximum number of results. If None, returns results only from the first response.
    """
    return Tool[Any](
        DuckDuckGoSearchTool(client=duckduckgo_client or DDGS(), max_results=max_results).__call__,
        name='duckduckgo_search',
        description='Searches DuckDuckGo for the given query and returns the results.',
    )

```

---|---
Exa tools for Pydantic AI agents.
Provides web search, content retrieval, and AI-powered answer capabilities using the Exa API, a neural search engine that finds high-quality, relevant results across billions of web pages.
###  ExaSearchResult
Bases:
An Exa search result with content.
See
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
```
| ```
class ExaSearchResult(TypedDict):
    """An Exa search result with content.

    See [Exa Search API documentation](https://docs.exa.ai/reference/search)
    for more information.
    """

    title: str
    """The title of the search result."""
    url: str
    """The URL of the search result."""
    published_date: str | None
    """The published date of the content, if available."""
    author: str | None
    """The author of the content, if available."""
    text: str
    """The text content of the search result."""

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

The URL of the search result.
####  published_date `instance-attribute`
```
published_date:  | None

```

The published date of the content, if available.
####  author `instance-attribute`
```
author:  | None

```

The author of the content, if available.
####  text `instance-attribute`
```
text:

```

The text content of the search result.
###  ExaAnswerResult
Bases:
An Exa answer result with citations.
See
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
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
```
| ```
class ExaAnswerResult(TypedDict):
    """An Exa answer result with citations.

    See [Exa Answer API documentation](https://docs.exa.ai/reference/answer)
    for more information.
    """

    answer: str
    """The AI-generated answer to the query."""
    citations: list[dict[str, Any]]
    """Citations supporting the answer."""

```

---|---
####  answer `instance-attribute`
```
answer:

```

The AI-generated answer to the query.
####  citations `instance-attribute`
```
citations: [[, ]]

```

Citations supporting the answer.
###  ExaContentResult
Bases:
Content retrieved from a URL.
See
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
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
```
| ```
class ExaContentResult(TypedDict):
    """Content retrieved from a URL.

    See [Exa Contents API documentation](https://docs.exa.ai/reference/get-contents)
    for more information.
    """

    url: str
    """The URL of the content."""
    title: str
    """The title of the page."""
    text: str
    """The text content of the page."""
    author: str | None
    """The author of the content, if available."""
    published_date: str | None
    """The published date of the content, if available."""

```

---|---
####  url `instance-attribute`
```
url:

```

The URL of the content.
####  title `instance-attribute`
```
title:

```

The title of the page.
####  text `instance-attribute`
```
text:

```

The text content of the page.
####  author `instance-attribute`
```
author:  | None

```

The author of the content, if available.
####  published_date `instance-attribute`
```
published_date:  | None

```

The published date of the content, if available.
###  ExaSearchTool `dataclass`
The Exa search tool.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
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
```
| ```
@dataclass
class ExaSearchTool:
    """The Exa search tool."""

    client: AsyncExa
    """The Exa async client."""

    num_results: int
    """The number of results to return."""

    max_characters: int | None
    """Maximum characters of text content per result, or None for no limit."""

    async def __call__(
        self,
        query: str,
        search_type: Literal['auto', 'keyword', 'neural', 'fast', 'deep'] = 'auto',
    ) -> list[ExaSearchResult]:
        """Searches Exa for the given query and returns the results with content.

        Args:
            query: The search query to execute with Exa.
            search_type: The type of search to perform. 'auto' automatically chooses
                the best search type, 'keyword' for exact matches, 'neural' for
                semantic search, 'fast' for speed-optimized search, 'deep' for
                comprehensive multi-query search.

        Returns:
            The search results with text content.
        """
        text_config: bool | dict[str, int] = {'maxCharacters': self.max_characters} if self.max_characters else True
        response = await self.client.search(  # pyright: ignore[reportUnknownMemberType]
            query,
            num_results=self.num_results,
            type=search_type,
            contents={'text': text_config},
        )

        return [
            ExaSearchResult(
                title=result.title or '',
                url=result.url,
                published_date=result.published_date,
                author=result.author,
                text=result.text or '',
            )
            for result in response.results
        ]

```

---|---
####  client `instance-attribute`
```
client: AsyncExa

```

The Exa async client.
####  num_results `instance-attribute`
```
num_results:

```

The number of results to return.
####  max_characters `instance-attribute`
```
max_characters:  | None

```

Maximum characters of text content per result, or None for no limit.
####  __call__ `async`
```
__call__(
    query: ,
    search_type: [
        "auto", "keyword", "neural", "fast", "deep"
    ] = "auto",
) -> [ExaSearchResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.exa.ExaSearchResult "ExaSearchResult \(pydantic_ai.common_tools.exa.ExaSearchResult\)")]

```

Searches Exa for the given query and returns the results with content.
Parameters:
Name | Type | Description | Default
---|---|---|---
`query` |  |  The search query to execute with Exa. |  _required_
`search_type` |  |  The type of search to perform. 'auto' automatically chooses the best search type, 'keyword' for exact matches, 'neural' for semantic search, 'fast' for speed-optimized search, 'deep' for comprehensive multi-query search. |  `'auto'`
Returns:
Type | Description
---|---
`ExaSearchResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.exa.ExaSearchResult "ExaSearchResult \(pydantic_ai.common_tools.exa.ExaSearchResult\)")]` |  The search results with text content.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
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
```
| ```
async def __call__(
    self,
    query: str,
    search_type: Literal['auto', 'keyword', 'neural', 'fast', 'deep'] = 'auto',
) -> list[ExaSearchResult]:
    """Searches Exa for the given query and returns the results with content.

    Args:
        query: The search query to execute with Exa.
        search_type: The type of search to perform. 'auto' automatically chooses
            the best search type, 'keyword' for exact matches, 'neural' for
            semantic search, 'fast' for speed-optimized search, 'deep' for
            comprehensive multi-query search.

    Returns:
        The search results with text content.
    """
    text_config: bool | dict[str, int] = {'maxCharacters': self.max_characters} if self.max_characters else True
    response = await self.client.search(  # pyright: ignore[reportUnknownMemberType]
        query,
        num_results=self.num_results,
        type=search_type,
        contents={'text': text_config},
    )

    return [
        ExaSearchResult(
            title=result.title or '',
            url=result.url,
            published_date=result.published_date,
            author=result.author,
            text=result.text or '',
        )
        for result in response.results
    ]

```

---|---
###  ExaFindSimilarTool `dataclass`
The Exa find similar tool.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
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
```
| ```
@dataclass
class ExaFindSimilarTool:
    """The Exa find similar tool."""

    client: AsyncExa
    """The Exa async client."""

    num_results: int
    """The number of results to return."""

    async def __call__(
        self,
        url: str,
        exclude_source_domain: bool = True,
    ) -> list[ExaSearchResult]:
        """Finds pages similar to the given URL and returns them with content.

        Args:
            url: The URL to find similar pages for.
            exclude_source_domain: Whether to exclude results from the same domain
                as the input URL. Defaults to True.

        Returns:
            Similar pages with text content.
        """
        response = await self.client.find_similar(  # pyright: ignore[reportUnknownMemberType]
            url,
            num_results=self.num_results,
            exclude_source_domain=exclude_source_domain,
            contents={'text': True},
        )

        return [
            ExaSearchResult(
                title=result.title or '',
                url=result.url,
                published_date=result.published_date,
                author=result.author,
                text=result.text or '',
            )
            for result in response.results
        ]

```

---|---
####  client `instance-attribute`
```
client: AsyncExa

```

The Exa async client.
####  num_results `instance-attribute`
```
num_results:

```

The number of results to return.
####  __call__ `async`
```
__call__(
    url: , exclude_source_domain:  = True
) -> [ExaSearchResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.exa.ExaSearchResult "ExaSearchResult \(pydantic_ai.common_tools.exa.ExaSearchResult\)")]

```

Finds pages similar to the given URL and returns them with content.
Parameters:
Name | Type | Description | Default
---|---|---|---
`url` |  |  The URL to find similar pages for. |  _required_
`exclude_source_domain` |  |  Whether to exclude results from the same domain as the input URL. Defaults to True. |  `True`
Returns:
Type | Description
---|---
`ExaSearchResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.exa.ExaSearchResult "ExaSearchResult \(pydantic_ai.common_tools.exa.ExaSearchResult\)")]` |  Similar pages with text content.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
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
```
| ```
async def __call__(
    self,
    url: str,
    exclude_source_domain: bool = True,
) -> list[ExaSearchResult]:
    """Finds pages similar to the given URL and returns them with content.

    Args:
        url: The URL to find similar pages for.
        exclude_source_domain: Whether to exclude results from the same domain
            as the input URL. Defaults to True.

    Returns:
        Similar pages with text content.
    """
    response = await self.client.find_similar(  # pyright: ignore[reportUnknownMemberType]
        url,
        num_results=self.num_results,
        exclude_source_domain=exclude_source_domain,
        contents={'text': True},
    )

    return [
        ExaSearchResult(
            title=result.title or '',
            url=result.url,
            published_date=result.published_date,
            author=result.author,
            text=result.text or '',
        )
        for result in response.results
    ]

```

---|---
###  ExaGetContentsTool `dataclass`
The Exa get contents tool.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
```
| ```
@dataclass
class ExaGetContentsTool:
    """The Exa get contents tool."""

    client: AsyncExa
    """The Exa async client."""

    async def __call__(
        self,
        urls: list[str],
    ) -> list[ExaContentResult]:
        """Gets the content of the specified URLs.

        Args:
            urls: A list of URLs to get content for.

        Returns:
            The content of each URL.
        """
        response = await self.client.get_contents(urls, text=True)  # pyright: ignore[reportUnknownMemberType,reportUnknownVariableType]

        return [
            ExaContentResult(
                url=result.url,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
                title=result.title or '',  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
                text=result.text or '',  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
                author=result.author,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
                published_date=result.published_date,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            )
            for result in response.results  # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType]
        ]

```

---|---
####  client `instance-attribute`
```
client: AsyncExa

```

The Exa async client.
####  __call__ `async`
```
__call__(urls: []) -> [ExaContentResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.exa.ExaContentResult "ExaContentResult \(pydantic_ai.common_tools.exa.ExaContentResult\)")]

```

Gets the content of the specified URLs.
Parameters:
Name | Type | Description | Default
---|---|---|---
`urls` |  |  A list of URLs to get content for. |  _required_
Returns:
Type | Description
---|---
`ExaContentResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.exa.ExaContentResult "ExaContentResult \(pydantic_ai.common_tools.exa.ExaContentResult\)")]` |  The content of each URL.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
```
| ```
async def __call__(
    self,
    urls: list[str],
) -> list[ExaContentResult]:
    """Gets the content of the specified URLs.

    Args:
        urls: A list of URLs to get content for.

    Returns:
        The content of each URL.
    """
    response = await self.client.get_contents(urls, text=True)  # pyright: ignore[reportUnknownMemberType,reportUnknownVariableType]

    return [
        ExaContentResult(
            url=result.url,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            title=result.title or '',  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            text=result.text or '',  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            author=result.author,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
            published_date=result.published_date,  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        )
        for result in response.results  # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType]
    ]

```

---|---
###  ExaAnswerTool `dataclass`
The Exa answer tool.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
```
| ```
@dataclass
class ExaAnswerTool:
    """The Exa answer tool."""

    client: AsyncExa
    """The Exa async client."""

    async def __call__(
        self,
        query: str,
    ) -> ExaAnswerResult:
        """Generates an AI-powered answer to the query with citations.

        Args:
            query: The question to answer.

        Returns:
            An answer with supporting citations from web sources.
        """
        response = await self.client.answer(query, text=True)

        return ExaAnswerResult(
            answer=response.answer,  # pyright: ignore[reportUnknownMemberType,reportArgumentType,reportAttributeAccessIssue]
            citations=[
                {
                    'url': citation.url,  # pyright: ignore[reportUnknownMemberType]
                    'title': citation.title or '',  # pyright: ignore[reportUnknownMemberType]
                    'text': citation.text or '',  # pyright: ignore[reportUnknownMemberType]
                }
                for citation in response.citations  # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType,reportAttributeAccessIssue]
            ],
        )

```

---|---
####  client `instance-attribute`
```
client: AsyncExa

```

The Exa async client.
####  __call__ `async`
```
__call__(query: ) -> ExaAnswerResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.exa.ExaAnswerResult "ExaAnswerResult \(pydantic_ai.common_tools.exa.ExaAnswerResult\)")

```

Generates an AI-powered answer to the query with citations.
Parameters:
Name | Type | Description | Default
---|---|---|---
`query` |  |  The question to answer. |  _required_
Returns:
Type | Description
---|---
`ExaAnswerResult[](https://ai.pydantic.dev/api/common_tools/#pydantic_ai.common_tools.exa.ExaAnswerResult "ExaAnswerResult \(pydantic_ai.common_tools.exa.ExaAnswerResult\)")` |  An answer with supporting citations from web sources.
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
```
| ```
async def __call__(
    self,
    query: str,
) -> ExaAnswerResult:
    """Generates an AI-powered answer to the query with citations.

    Args:
        query: The question to answer.

    Returns:
        An answer with supporting citations from web sources.
    """
    response = await self.client.answer(query, text=True)

    return ExaAnswerResult(
        answer=response.answer,  # pyright: ignore[reportUnknownMemberType,reportArgumentType,reportAttributeAccessIssue]
        citations=[
            {
                'url': citation.url,  # pyright: ignore[reportUnknownMemberType]
                'title': citation.title or '',  # pyright: ignore[reportUnknownMemberType]
                'text': citation.text or '',  # pyright: ignore[reportUnknownMemberType]
            }
            for citation in response.citations  # pyright: ignore[reportUnknownVariableType,reportUnknownMemberType,reportAttributeAccessIssue]
        ],
    )

```

---|---
###  exa_search_tool
```
exa_search_tool(
    api_key: ,
    *,
    num_results:  = 5,
    max_characters:  | None = None
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
exa_search_tool(
    *,
    client: AsyncExa,
    num_results:  = 5,
    max_characters:  | None = None
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

```
exa_search_tool(
    api_key:  | None = None,
    *,
    client: AsyncExa | None = None,
    num_results:  = 5,
    max_characters:  | None = None
) -> Tool[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool "Tool



      dataclass
   \(pydantic_ai.tools.Tool\)")[]

```

Creates an Exa search tool.
Parameters:
Name | Type | Description | Default
---|---|---|---
`api_key` |  |  The Exa API key. Required if `client` is not provided. You can get one by signing up at  |  `None`
`client` |  `AsyncExa | None` |  An existing AsyncExa client. If provided, `api_key` is ignored. This is useful for sharing a client across multiple tools. |  `None`
`num_results` |  |  The number of results to return. Defaults to 5. |  `5`
`max_characters` |  |  Maximum characters of text content per result. Use this to limit token usage. Defaults to None (no limit). |  `None`
Source code in `pydantic_ai_slim/pydantic_ai/common_tools/exa.py`
```
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
```
| ```
def exa_search_tool(
    api_key: str | None = None,
    *,
    client: AsyncExa | None = None,
    num_results: int = 5,
    max_characters: int | None = None,
) -> Tool[Any]:
    """Creates an Exa search tool.

    Args:
        api_key: The Exa API key. Required if `client` is not provided.

            You can get one by signing up at [https://dashboard.exa.ai](https://dashboard.exa.ai).
        client: An existing AsyncExa client. If provided, `api_key` is ignored.
            This is useful for sharing a client across multiple tools.
        num_results: The number of results to return. Defaults to 5.
        max_characters: Maximum characters of text content per result. Use this to limit
            token usage. Defaults to None (no limit).
