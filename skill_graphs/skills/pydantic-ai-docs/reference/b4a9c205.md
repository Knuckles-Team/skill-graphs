# `pydantic_ai.toolsets`
###  AbstractToolset
Bases: `AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]`
A toolset is a collection of tools that can be used by an agent.
It is responsible for:
  * Listing the tools it contains
  * Validating the arguments of the tools
  * Calling the tools


See [toolset docs](https://ai.pydantic.dev/toolsets/) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
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
```
| ```
class AbstractToolset(ABC, Generic[AgentDepsT]):
    """A toolset is a collection of tools that can be used by an agent.

    It is responsible for:

    - Listing the tools it contains
    - Validating the arguments of the tools
    - Calling the tools

    See [toolset docs](../toolsets.md) for more information.
    """

    @property
    @abstractmethod
    def id(self) -> str | None:
        """An ID for the toolset that is unique among all toolsets registered with the same agent.

        If you're implementing a concrete implementation that users can instantiate more than once, you should let them optionally pass a custom ID to the constructor and return that here.

        A toolset needs to have an ID in order to be used in a durable execution environment like Temporal, in which case the ID will be used to identify the toolset's activities within the workflow.
        """
        raise NotImplementedError()

    @property
    def label(self) -> str:
        """The name of the toolset for use in error messages."""
        label = self.__class__.__name__
        if self.id:  # pragma: no branch
            label += f' {self.id!r}'
        return label

    @property
    def tool_name_conflict_hint(self) -> str:
        """A hint for how to avoid name conflicts with other toolsets for use in error messages."""
        return 'Rename the tool or wrap the toolset in a `PrefixedToolset` to avoid name conflicts.'

    async def __aenter__(self) -> Self:
        """Enter the toolset context.

        This is where you can set up network connections in a concrete implementation.
        """
        return self

    async def __aexit__(self, *args: Any) -> bool | None:
        """Exit the toolset context.

        This is where you can tear down network connections in a concrete implementation.
        """
        return None

    @abstractmethod
    async def get_tools(self, ctx: RunContext[AgentDepsT]) -> dict[str, ToolsetTool[AgentDepsT]]:
        """The tools that are available in this toolset."""
        raise NotImplementedError()

    @abstractmethod
    async def call_tool(
        self, name: str, tool_args: dict[str, Any], ctx: RunContext[AgentDepsT], tool: ToolsetTool[AgentDepsT]
    ) -> Any:
        """Call a tool with the given arguments.

        Args:
            name: The name of the tool to call.
            tool_args: The arguments to pass to the tool.
            ctx: The run context.
            tool: The tool definition returned by [`get_tools`][pydantic_ai.toolsets.AbstractToolset.get_tools] that was called.
        """
        raise NotImplementedError()

    def apply(self, visitor: Callable[[AbstractToolset[AgentDepsT]], None]) -> None:
        """Run a visitor function on all "leaf" toolsets (i.e. those that implement their own tool listing and calling)."""
        visitor(self)

    def visit_and_replace(
        self, visitor: Callable[[AbstractToolset[AgentDepsT]], AbstractToolset[AgentDepsT]]
    ) -> AbstractToolset[AgentDepsT]:
        """Run a visitor function on all "leaf" toolsets (i.e. those that implement their own tool listing and calling) and replace them in the hierarchy with the result of the function."""
        return visitor(self)

    def filtered(
        self, filter_func: Callable[[RunContext[AgentDepsT], ToolDefinition], bool]
    ) -> FilteredToolset[AgentDepsT]:
        """Returns a new toolset that filters this toolset's tools using a filter function that takes the agent context and the tool definition.

        See [toolset docs](../toolsets.md#filtering-tools) for more information.
        """
        from .filtered import FilteredToolset

        return FilteredToolset(self, filter_func)

    def prefixed(self, prefix: str) -> PrefixedToolset[AgentDepsT]:
        """Returns a new toolset that prefixes the names of this toolset's tools.

        See [toolset docs](../toolsets.md#prefixing-tool-names) for more information.
        """
        from .prefixed import PrefixedToolset

        return PrefixedToolset(self, prefix)

    def prepared(self, prepare_func: ToolsPrepareFunc[AgentDepsT]) -> PreparedToolset[AgentDepsT]:
        """Returns a new toolset that prepares this toolset's tools using a prepare function that takes the agent context and the original tool definitions.

        See [toolset docs](../toolsets.md#preparing-tool-definitions) for more information.
        """
        from .prepared import PreparedToolset

        return PreparedToolset(self, prepare_func)

    def renamed(self, name_map: dict[str, str]) -> RenamedToolset[AgentDepsT]:
        """Returns a new toolset that renames this toolset's tools using a dictionary mapping new names to original names.

        See [toolset docs](../toolsets.md#renaming-tools) for more information.
        """
        from .renamed import RenamedToolset

        return RenamedToolset(self, name_map)

    def approval_required(
        self,
        approval_required_func: Callable[[RunContext[AgentDepsT], ToolDefinition, dict[str, Any]], bool] = (
            lambda ctx, tool_def, tool_args: True
        ),
    ) -> ApprovalRequiredToolset[AgentDepsT]:
        """Returns a new toolset that requires (some) calls to tools it contains to be approved.

        See [toolset docs](../toolsets.md#requiring-tool-approval) for more information.
        """
        from .approval_required import ApprovalRequiredToolset

        return ApprovalRequiredToolset(self, approval_required_func)

```

---|---
####  id `abstractmethod` `property`
```
id:  | None

```

An ID for the toolset that is unique among all toolsets registered with the same agent.
If you're implementing a concrete implementation that users can instantiate more than once, you should let them optionally pass a custom ID to the constructor and return that here.
A toolset needs to have an ID in order to be used in a durable execution environment like Temporal, in which case the ID will be used to identify the toolset's activities within the workflow.
####  label `property`
```
label:

```

The name of the toolset for use in error messages.
####  tool_name_conflict_hint `property`
```
tool_name_conflict_hint:

```

A hint for how to avoid name conflicts with other toolsets for use in error messages.
####  __aenter__ `async`
```
__aenter__() ->

```

Enter the toolset context.
This is where you can set up network connections in a concrete implementation.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
106
107
108
109
110
111
```
| ```
async def __aenter__(self) -> Self:
    """Enter the toolset context.

    This is where you can set up network connections in a concrete implementation.
    """
    return self

```

---|---
####  __aexit__ `async`
```
__aexit__(*args: ) ->  | None

```

Exit the toolset context.
This is where you can tear down network connections in a concrete implementation.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
113
114
115
116
117
118
```
| ```
async def __aexit__(self, *args: Any) -> bool | None:
    """Exit the toolset context.

    This is where you can tear down network connections in a concrete implementation.
    """
    return None

```

---|---
####  get_tools `abstractmethod` `async`
```
get_tools(
    ctx: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")],
) -> [, ToolsetTool[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]]

```

The tools that are available in this toolset.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
120
121
122
123
```
| ```
@abstractmethod
async def get_tools(self, ctx: RunContext[AgentDepsT]) -> dict[str, ToolsetTool[AgentDepsT]]:
    """The tools that are available in this toolset."""
    raise NotImplementedError()

```

---|---
####  call_tool `abstractmethod` `async`
```
call_tool(
    name: ,
    tool_args: [, ],
    ctx: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")],
    tool: ToolsetTool[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")],
) ->

```

Call a tool with the given arguments.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  The name of the tool to call. |  _required_
`tool_args` |  |  The arguments to pass to the tool. |  _required_
`ctx` |  `RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]` |  The run context. |  _required_
`tool` |  `ToolsetTool[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]` |  The tool definition returned by [`get_tools`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset.get_tools "get_tools



      abstractmethod
      async
  ") that was called. |  _required_
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
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
```
| ```
@abstractmethod
async def call_tool(
    self, name: str, tool_args: dict[str, Any], ctx: RunContext[AgentDepsT], tool: ToolsetTool[AgentDepsT]
) -> Any:
    """Call a tool with the given arguments.

    Args:
        name: The name of the tool to call.
        tool_args: The arguments to pass to the tool.
        ctx: The run context.
        tool: The tool definition returned by [`get_tools`][pydantic_ai.toolsets.AbstractToolset.get_tools] that was called.
    """
    raise NotImplementedError()

```

---|---
####  apply
```
apply(
    visitor: [[AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]], None],
) -> None

```

Run a visitor function on all "leaf" toolsets (i.e. those that implement their own tool listing and calling).
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
139
140
141
```
| ```
def apply(self, visitor: Callable[[AbstractToolset[AgentDepsT]], None]) -> None:
    """Run a visitor function on all "leaf" toolsets (i.e. those that implement their own tool listing and calling)."""
    visitor(self)

```

---|---
####  visit_and_replace
```
visit_and_replace(
    visitor: [
        [AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]],
        AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")],
    ],
) -> AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]

```

Run a visitor function on all "leaf" toolsets (i.e. those that implement their own tool listing and calling) and replace them in the hierarchy with the result of the function.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
143
144
145
146
147
```
| ```
def visit_and_replace(
    self, visitor: Callable[[AbstractToolset[AgentDepsT]], AbstractToolset[AgentDepsT]]
) -> AbstractToolset[AgentDepsT]:
    """Run a visitor function on all "leaf" toolsets (i.e. those that implement their own tool listing and calling) and replace them in the hierarchy with the result of the function."""
    return visitor(self)

```

---|---
####  filtered
```
filtered(
    filter_func: [
        [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")], ToolDefinition[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
   \(pydantic_ai.tools.ToolDefinition\)")],
    ],
) -> FilteredToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.FilteredToolset "FilteredToolset



      dataclass
   \(pydantic_ai.toolsets.filtered.FilteredToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]

```

Returns a new toolset that filters this toolset's tools using a filter function that takes the agent context and the tool definition.
See [toolset docs](https://ai.pydantic.dev/toolsets/#filtering-tools) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
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
```
| ```
def filtered(
    self, filter_func: Callable[[RunContext[AgentDepsT], ToolDefinition], bool]
) -> FilteredToolset[AgentDepsT]:
    """Returns a new toolset that filters this toolset's tools using a filter function that takes the agent context and the tool definition.

    See [toolset docs](../toolsets.md#filtering-tools) for more information.
    """
    from .filtered import FilteredToolset

    return FilteredToolset(self, filter_func)

```

---|---
####  prefixed
```
prefixed(prefix: ) -> PrefixedToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.PrefixedToolset "PrefixedToolset



      dataclass
   \(pydantic_ai.toolsets.prefixed.PrefixedToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]

```

Returns a new toolset that prefixes the names of this toolset's tools.
See [toolset docs](https://ai.pydantic.dev/toolsets/#prefixing-tool-names) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
160
161
162
163
164
165
166
167
```
| ```
def prefixed(self, prefix: str) -> PrefixedToolset[AgentDepsT]:
    """Returns a new toolset that prefixes the names of this toolset's tools.

    See [toolset docs](../toolsets.md#prefixing-tool-names) for more information.
    """
    from .prefixed import PrefixedToolset

    return PrefixedToolset(self, prefix)

```

---|---
####  prepared
```
prepared(
    prepare_func: ToolsPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
   \(pydantic_ai.tools.ToolsPrepareFunc\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")],
) -> PreparedToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.PreparedToolset "PreparedToolset



      dataclass
   \(pydantic_ai.toolsets.prepared.PreparedToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]

```

Returns a new toolset that prepares this toolset's tools using a prepare function that takes the agent context and the original tool definitions.
See [toolset docs](https://ai.pydantic.dev/toolsets/#preparing-tool-definitions) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
169
170
171
172
173
174
175
176
```
| ```
def prepared(self, prepare_func: ToolsPrepareFunc[AgentDepsT]) -> PreparedToolset[AgentDepsT]:
    """Returns a new toolset that prepares this toolset's tools using a prepare function that takes the agent context and the original tool definitions.

    See [toolset docs](../toolsets.md#preparing-tool-definitions) for more information.
    """
    from .prepared import PreparedToolset

    return PreparedToolset(self, prepare_func)

```

---|---
####  renamed
```
renamed(
    name_map: [, ],
) -> RenamedToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.RenamedToolset "RenamedToolset



      dataclass
   \(pydantic_ai.toolsets.renamed.RenamedToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]

```

Returns a new toolset that renames this toolset's tools using a dictionary mapping new names to original names.
See [toolset docs](https://ai.pydantic.dev/toolsets/#renaming-tools) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
178
179
180
181
182
183
184
185
```
| ```
def renamed(self, name_map: dict[str, str]) -> RenamedToolset[AgentDepsT]:
    """Returns a new toolset that renames this toolset's tools using a dictionary mapping new names to original names.

    See [toolset docs](../toolsets.md#renaming-tools) for more information.
    """
    from .renamed import RenamedToolset

    return RenamedToolset(self, name_map)

```

---|---
####  approval_required
```
approval_required(
    approval_required_func: [
        [
            RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")],
            ToolDefinition[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
   \(pydantic_ai.tools.ToolDefinition\)"),
            [, ],
        ],
        ,
    ] = lambda ctx, tool_def, tool_args: True
) -> ApprovalRequiredToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.ApprovalRequiredToolset "ApprovalRequiredToolset



      dataclass
   \(pydantic_ai.toolsets.approval_required.ApprovalRequiredToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]

```

Returns a new toolset that requires (some) calls to tools it contains to be approved.
See [toolset docs](https://ai.pydantic.dev/toolsets/#requiring-tool-approval) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/abstract.py`
```
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
```
| ```
def approval_required(
    self,
    approval_required_func: Callable[[RunContext[AgentDepsT], ToolDefinition, dict[str, Any]], bool] = (
        lambda ctx, tool_def, tool_args: True
    ),
) -> ApprovalRequiredToolset[AgentDepsT]:
    """Returns a new toolset that requires (some) calls to tools it contains to be approved.

    See [toolset docs](../toolsets.md#requiring-tool-approval) for more information.
    """
    from .approval_required import ApprovalRequiredToolset

    return ApprovalRequiredToolset(self, approval_required_func)

```

---|---
###  CombinedToolset `dataclass`
Bases: `AbstractToolset[](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.AbstractToolset "AbstractToolset \(pydantic_ai.toolsets.abstract.AbstractToolset\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]`
A toolset that combines multiple toolsets.
See [toolset docs](https://ai.pydantic.dev/toolsets/#combining-toolsets) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/toolsets/combined.py`
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
```
| ```
@dataclass
class CombinedToolset(AbstractToolset[AgentDepsT]):
    """A toolset that combines multiple toolsets.

    See [toolset docs](../toolsets.md#combining-toolsets) for more information.
    """

    toolsets: Sequence[AbstractToolset[AgentDepsT]]

    _enter_lock: Lock = field(compare=False, init=False, default_factory=Lock)
    _entered_count: int = field(init=False, default=0)
    _exit_stack: AsyncExitStack | None = field(init=False, default=None)

    @property
    def id(self) -> str | None:
        return None  # pragma: no cover

    @property
    def label(self) -> str:
        return f'{self.__class__.__name__}({", ".join(toolset.label for toolset in self.toolsets)})'  # pragma: no cover

    async def __aenter__(self) -> Self:
        async with self._enter_lock:
            if self._entered_count == 0:
                async with AsyncExitStack() as exit_stack:
                    for toolset in self.toolsets:
                        await exit_stack.enter_async_context(toolset)
                    self._exit_stack = exit_stack.pop_all()
            self._entered_count += 1
        return self

    async def __aexit__(self, *args: Any) -> bool | None:
        async with self._enter_lock:
            self._entered_count -= 1
            if self._entered_count == 0 and self._exit_stack is not None:
                await self._exit_stack.aclose()
                self._exit_stack = None

    async def get_tools(self, ctx: RunContext[AgentDepsT]) -> dict[str, ToolsetTool[AgentDepsT]]:
        toolsets_tools = await asyncio.gather(*(toolset.get_tools(ctx) for toolset in self.toolsets))
        all_tools: dict[str, ToolsetTool[AgentDepsT]] = {}

        for toolset, tools in zip(self.toolsets, toolsets_tools):
            for name, tool in tools.items():
                tool_toolset = tool.toolset
                if existing_tool := all_tools.get(name):
                    capitalized_toolset_label = tool_toolset.label[0].upper() + tool_toolset.label[1:]
                    raise UserError(
                        f'{capitalized_toolset_label} defines a tool whose name conflicts with existing tool from {existing_tool.toolset.label}: {name!r}. {toolset.tool_name_conflict_hint}'
                    )

                all_tools[name] = _CombinedToolsetTool(
                    toolset=tool_toolset,
                    tool_def=tool.tool_def,
                    max_retries=tool.max_retries,
                    args_validator=tool.args_validator,
                    args_validator_func=tool.args_validator_func,
                    source_toolset=toolset,
                    source_tool=tool,
                )
        return all_tools

    async def call_tool(
        self, name: str, tool_args: dict[str, Any], ctx: RunContext[AgentDepsT], tool: ToolsetTool[AgentDepsT]
    ) -> Any:
        assert isinstance(tool, _CombinedToolsetTool)
        return await tool.source_toolset.call_tool(name, tool_args, ctx, tool.source_tool)

    def apply(self, visitor: Callable[[AbstractToolset[AgentDepsT]], None]) -> None:
        for toolset in self.toolsets:
            toolset.apply(visitor)

    def visit_and_replace(
        self, visitor: Callable[[AbstractToolset[AgentDepsT]], AbstractToolset[AgentDepsT]]
    ) -> AbstractToolset[AgentDepsT]:
