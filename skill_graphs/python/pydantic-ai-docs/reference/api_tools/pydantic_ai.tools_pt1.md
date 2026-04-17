# `pydantic_ai.tools`
###  AgentDepsT `module-attribute`
```
AgentDepsT = TypeVar(
    "AgentDepsT", default=None, contravariant=True
)

```

Type variable for agent dependencies.
###  RunContext `dataclass`
Bases: `RunContextAgentDepsT]`
Information about the current call.
Source code in `pydantic_ai_slim/pydantic_ai/_run_context.py`
```
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
```
| ```
@dataclasses.dataclass(repr=False, kw_only=True)
class RunContext(Generic[RunContextAgentDepsT]):
    """Information about the current call."""

    deps: RunContextAgentDepsT
    """Dependencies for the agent."""
    model: Model
    """The model used in this run."""
    usage: RunUsage
    """LLM usage associated with the run."""
    prompt: str | Sequence[_messages.UserContent] | None = None
    """The original user prompt passed to the run."""
    messages: list[_messages.ModelMessage] = field(default_factory=list[_messages.ModelMessage])
    """Messages exchanged in the conversation so far."""
    validation_context: Any = None
    """Pydantic [validation context](https://docs.pydantic.dev/latest/concepts/validators/#validation-context) for tool args and run outputs."""
    tracer: Tracer = field(default_factory=NoOpTracer)
    """The tracer to use for tracing the run."""
    trace_include_content: bool = False
    """Whether to include the content of the messages in the trace."""
    instrumentation_version: int = DEFAULT_INSTRUMENTATION_VERSION
    """Instrumentation settings version, if instrumentation is enabled."""
    retries: dict[str, int] = field(default_factory=dict[str, int])
    """Number of retries for each tool so far."""
    tool_call_id: str | None = None
    """The ID of the tool call."""
    tool_name: str | None = None
    """Name of the tool being called."""
    retry: int = 0
    """Number of retries so far.

    For tool calls, this is the number of retries of the specific tool.
    For output validation, this is the number of output validation retries.
    """
    max_retries: int = 0
    """The maximum number of retries allowed.

    For tool calls, this is the maximum retries for the specific tool.
    For output validation, this is the maximum output validation retries.
    """
    run_step: int = 0
    """The current step in the run."""
    tool_call_approved: bool = False
    """Whether a tool call that required approval has now been approved."""
    tool_call_metadata: Any = None
    """Metadata from `DeferredToolResults.metadata[tool_call_id]`, available when `tool_call_approved=True`."""
    partial_output: bool = False
    """Whether the output passed to an output validator is partial."""
    run_id: str | None = None
    """"Unique identifier for the agent run."""
    metadata: dict[str, Any] | None = None
    """Metadata associated with this agent run, if configured."""

    @property
    def last_attempt(self) -> bool:
        """Whether this is the last attempt at running this tool before an error is raised."""
        return self.retry == self.max_retries

    __repr__ = _utils.dataclasses_no_defaults_repr

```

---|---
####  deps `instance-attribute`
```
deps: RunContextAgentDepsT

```

Dependencies for the agent.
####  model `instance-attribute`
```
model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)")

```

The model used in this run.
####  usage `instance-attribute`
```
usage: RunUsage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.RunUsage "RunUsage



      dataclass
   \(pydantic_ai.result.RunUsage\)")

```

LLM usage associated with the run.
####  prompt `class-attribute` `instance-attribute`
```
prompt:  | [UserContent] | None = None

```

The original user prompt passed to the run.
####  messages `class-attribute` `instance-attribute`
```
messages: [ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")] = (
    default_factory=[ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "ModelMessage



      module-attribute
   \(pydantic_ai.messages.ModelMessage\)")]
)

```

Messages exchanged in the conversation so far.
####  validation_context `class-attribute` `instance-attribute`
```
validation_context:  = None

```

Pydantic [validation context](https://docs.pydantic.dev/latest/concepts/validators/#validation-context) for tool args and run outputs.
####  tracer `class-attribute` `instance-attribute`
```
tracer: Tracer = (default_factory=NoOpTracer)

```

The tracer to use for tracing the run.
####  trace_include_content `class-attribute` `instance-attribute`
```
trace_include_content:  = False

```

Whether to include the content of the messages in the trace.
####  instrumentation_version `class-attribute` `instance-attribute`
```
instrumentation_version:  = (
    DEFAULT_INSTRUMENTATION_VERSION
)

```

Instrumentation settings version, if instrumentation is enabled.
####  retries `class-attribute` `instance-attribute`
```
retries: [, ] = (
    default_factory=[, ]
)

```

Number of retries for each tool so far.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id:  | None = None

```

The ID of the tool call.
####  tool_name `class-attribute` `instance-attribute`
```
tool_name:  | None = None

```

Name of the tool being called.
####  retry `class-attribute` `instance-attribute`
```
retry:  = 0

```

Number of retries so far.
For tool calls, this is the number of retries of the specific tool. For output validation, this is the number of output validation retries.
####  max_retries `class-attribute` `instance-attribute`
```
max_retries:  = 0

```

The maximum number of retries allowed.
For tool calls, this is the maximum retries for the specific tool. For output validation, this is the maximum output validation retries.
####  run_step `class-attribute` `instance-attribute`
```
run_step:  = 0

```

The current step in the run.
####  tool_call_approved `class-attribute` `instance-attribute`
```
tool_call_approved:  = False

```

Whether a tool call that required approval has now been approved.
####  tool_call_metadata `class-attribute` `instance-attribute`
```
tool_call_metadata:  = None

```

Metadata from `DeferredToolResults.metadata[tool_call_id]`, available when `tool_call_approved=True`.
####  partial_output `class-attribute` `instance-attribute`
```
partial_output:  = False

```

Whether the output passed to an output validator is partial.
####  run_id `class-attribute` `instance-attribute`
```
run_id:  | None = None

```

"Unique identifier for the agent run.
####  metadata `class-attribute` `instance-attribute`
```
metadata: [, ] | None = None

```

Metadata associated with this agent run, if configured.
####  last_attempt `property`
```
last_attempt:

```

Whether this is the last attempt at running this tool before an error is raised.
###  ToolParams `module-attribute`
```
ToolParams = ('ToolParams', default=...)

```

Retrieval function param spec.
###  SystemPromptFunc `module-attribute`
```
SystemPromptFunc:  = (
    [[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]],  | None]
    | [
        [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]], [ | None]
    ]
    | [[],  | None]
    | [[], [ | None]]
)

```

A function that may or maybe not take `RunContext` as an argument, and may or may not be async.
Functions which return None are excluded from model requests.
Usage `SystemPromptFunc[AgentDepsT]`.
###  ToolFuncContext `module-attribute`
```
ToolFuncContext:  = [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")], ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
]

```

A tool function that takes `RunContext` as the first argument.
Usage `ToolContextFunc[AgentDepsT, ToolParams]`.
###  ToolFuncPlain `module-attribute`
```
ToolFuncPlain:  = [ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)"), ]

```

A tool function that does not take `RunContext` as the first argument.
Usage `ToolPlainFunc[ToolParams]`.
###  ToolFuncEither `module-attribute`
```
ToolFuncEither:  = (
    ToolFuncContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "ToolFuncContext



      module-attribute
   \(pydantic_ai.tools.ToolFuncContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]
    | ToolFuncPlain[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "ToolFuncPlain



      module-attribute
   \(pydantic_ai.tools.ToolFuncPlain\)")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")]
)

```

Either kind of tool function.
This is just a union of [`ToolFuncContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "ToolFuncContext



      module-attribute
  ") and [`ToolFuncPlain`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "ToolFuncPlain



      module-attribute
  ").
Usage `ToolFuncEither[AgentDepsT, ToolParams]`.
###  ArgsValidatorFunc `module-attribute`
```
ArgsValidatorFunc:  = (
    [
        [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")], ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
        [None],
    ]
    | [
        [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")], ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "ToolParams



      module-attribute
   \(pydantic_ai.tools.ToolParams\)")],
        None,
    ]
)

```

A function that validates tool arguments before execution.
The validator receives the same typed parameters as the tool function, with [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as the first argument for dependency access.
Should raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") on validation failure.
###  ToolPrepareFunc `module-attribute`
```
ToolPrepareFunc:  = [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")], "ToolDefinition"],
    ["ToolDefinition | None"],
]

```

Definition of a function that can prepare a tool definition at call time.
See [tool docs](https://ai.pydantic.dev/tools-advanced/#tool-prepare) for more information.
Example — here `only_if_42` is valid as a `ToolPrepareFunc`:
```
from pydantic_ai import RunContext, Tool
from pydantic_ai.tools import ToolDefinition

async def only_if_42(
    ctx: RunContext[int], tool_def: ToolDefinition
) -> ToolDefinition | None:
    if ctx.deps == 42:
        return tool_def

def hitchhiker(ctx: RunContext[int], answer: str) -> str:
    return f'{ctx.deps} {answer}'

hitchhiker = Tool(hitchhiker, prepare=only_if_42)

```

Usage `ToolPrepareFunc[AgentDepsT]`.
###  ToolsPrepareFunc `module-attribute`
```
ToolsPrepareFunc:  = [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")], ["ToolDefinition"]],
    ["list[ToolDefinition] | None"],
]

```

Definition of a function that can prepare the tool definition of all tools for each step. This is useful if you want to customize the definition of multiple tools or you want to register a subset of tools for a given step.
Example — here `turn_on_strict_if_openai` is valid as a `ToolsPrepareFunc`:
```
from dataclasses import replace

from pydantic_ai import Agent, RunContext
from pydantic_ai.tools import ToolDefinition


async def turn_on_strict_if_openai(
    ctx: RunContext[None], tool_defs: list[ToolDefinition]
) -> list[ToolDefinition] | None:
    if ctx.model.system == 'openai':
        return [replace(tool_def, strict=True) for tool_def in tool_defs]
    return tool_defs

agent = Agent('openai:gpt-5.2', prepare_tools=turn_on_strict_if_openai)

```

Usage `ToolsPrepareFunc[AgentDepsT]`.
###  BuiltinToolFunc `module-attribute`
```
BuiltinToolFunc:  = [
    [RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
   \(pydantic_ai._run_context.RunContext\)")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "AgentDepsT



      module-attribute
   \(pydantic_ai._run_context.AgentDepsT\)")]],
    [AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)") | None]
    | AbstractBuiltinTool[](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.AbstractBuiltinTool "AbstractBuiltinTool



      dataclass
   \(pydantic_ai.builtin_tools.AbstractBuiltinTool\)")
    | None,
]

```

Definition of a function that can prepare a builtin tool at call time.
This is useful if you want to customize the builtin tool based on the run context (e.g. user dependencies), or omit it completely from a step.
###  DocstringFormat `module-attribute`
```
DocstringFormat:  = [
    "google", "numpy", "sphinx", "auto"
]

```

Supported docstring formats.
  * `'google'` —
  * `'numpy'` —
  * `'sphinx'` —
  * `'auto'` — Automatically infer the format based on the structure of the docstring.


###  DeferredToolRequests `dataclass`
Tool calls that require approval or external execution.
This can be used as an agent's `output_type` and will be used as the output of the agent run if the model called any deferred tools.
Results can be passed to the next agent run using a [`DeferredToolResults`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults



      dataclass
  ") object with the same tool call IDs.
See [deferred tools docs](https://ai.pydantic.dev/deferred-tools/#deferred-tools) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
@dataclass(kw_only=True)
class DeferredToolRequests:
    """Tool calls that require approval or external execution.

    This can be used as an agent's `output_type` and will be used as the output of the agent run if the model called any deferred tools.

    Results can be passed to the next agent run using a [`DeferredToolResults`][pydantic_ai.tools.DeferredToolResults] object with the same tool call IDs.

    See [deferred tools docs](../deferred-tools.md#deferred-tools) for more information.
    """

    calls: list[ToolCallPart] = field(default_factory=list[ToolCallPart])
    """Tool calls that require external execution."""
    approvals: list[ToolCallPart] = field(default_factory=list[ToolCallPart])
    """Tool calls that require human-in-the-loop approval."""
    metadata: dict[str, dict[str, Any]] = field(default_factory=dict[str, dict[str, Any]])
    """Metadata for deferred tool calls, keyed by `tool_call_id`."""

```

---|---
####  calls `class-attribute` `instance-attribute`
```
calls: [ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")] = (
    default_factory=[ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")]
)

```

Tool calls that require external execution.
####  approvals `class-attribute` `instance-attribute`
```
approvals: [ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")] = (
    default_factory=[ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "ToolCallPart



      dataclass
   \(pydantic_ai.messages.ToolCallPart\)")]
)

```

Tool calls that require human-in-the-loop approval.
####  metadata `class-attribute` `instance-attribute`
```
metadata: [, [, ]] = (
    default_factory=[, [, ]]
)

```

Metadata for deferred tool calls, keyed by `tool_call_id`.
###  ToolApproved `dataclass`
Indicates that a tool call has been approved and that the tool function should be executed.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
179
180
181
182
183
184
185
186
```
| ```
@dataclass(kw_only=True)
class ToolApproved:
    """Indicates that a tool call has been approved and that the tool function should be executed."""

    override_args: dict[str, Any] | None = None
    """Optional tool call arguments to use instead of the original arguments."""

    kind: Literal['tool-approved'] = 'tool-approved'

```

---|---
####  override_args `class-attribute` `instance-attribute`
```
override_args: [, ] | None = None

```

Optional tool call arguments to use instead of the original arguments.
###  ToolDenied `dataclass`
Indicates that a tool call has been denied and that a denial message should be returned to the model.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
@dataclass
class ToolDenied:
    """Indicates that a tool call has been denied and that a denial message should be returned to the model."""

    message: str = 'The tool call was denied.'
    """The message to return to the model."""

    _: KW_ONLY

    kind: Literal['tool-denied'] = 'tool-denied'

```

---|---
####  message `class-attribute` `instance-attribute`
```
message:  = 'The tool call was denied.'

```

The message to return to the model.
###  DeferredToolApprovalResult `module-attribute`
```
DeferredToolApprovalResult:  = [
    ToolApproved[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolApproved "ToolApproved



      dataclass
   \(pydantic_ai.tools.ToolApproved\)") | ToolDenied[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDenied "ToolDenied



      dataclass
   \(pydantic_ai.tools.ToolDenied\)"), Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("kind")
]

```

Result for a tool call that required human-in-the-loop approval.
###  DeferredToolCallResult `module-attribute`
```
DeferredToolCallResult:  = [
    [ToolReturn[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturn "ToolReturn



      dataclass
   \(pydantic_ai.messages.ToolReturn\)"), Tag[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "pydantic.Tag")("tool-return")]
    | [ModelRetry[](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry \(pydantic_ai.exceptions.ModelRetry\)"), Tag[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "pydantic.Tag")("model-retry")]
    | [RetryPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart "RetryPromptPart



      dataclass
   \(pydantic_ai.messages.RetryPromptPart\)"), Tag[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "pydantic.Tag")("retry-prompt")],
    Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")(_deferred_tool_call_result_discriminator),
]

```

Result for a tool call that required external execution.
###  DeferredToolResult `module-attribute`
```
DeferredToolResult = (
    DeferredToolApprovalResult[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolApprovalResult "DeferredToolApprovalResult



      module-attribute
   \(pydantic_ai.tools.DeferredToolApprovalResult\)") | DeferredToolCallResult[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolCallResult "DeferredToolCallResult



      module-attribute
   \(pydantic_ai.tools.DeferredToolCallResult\)")
)

```

Result for a tool call that required approval or external execution.
###  DeferredToolResults `dataclass`
Results for deferred tool calls from a previous run that required approval or external execution.
The tool call IDs need to match those from the [`DeferredToolRequests`](https://ai.pydantic.dev/api/output/#pydantic_ai.output.DeferredToolRequests "DeferredToolRequests



      dataclass
  ") output object from the previous run.
See [deferred tools docs](https://ai.pydantic.dev/deferred-tools/#deferred-tools) for more information.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
243
244
```
| ```
@dataclass(kw_only=True)
class DeferredToolResults:
    """Results for deferred tool calls from a previous run that required approval or external execution.

    The tool call IDs need to match those from the [`DeferredToolRequests`][pydantic_ai.output.DeferredToolRequests] output object from the previous run.

    See [deferred tools docs](../deferred-tools.md#deferred-tools) for more information.
    """

    calls: dict[str, DeferredToolCallResult | Any] = field(default_factory=dict[str, DeferredToolCallResult | Any])
    """Map of tool call IDs to results for tool calls that required external execution."""
    approvals: dict[str, bool | DeferredToolApprovalResult] = field(
        default_factory=dict[str, bool | DeferredToolApprovalResult]
    )
    """Map of tool call IDs to results for tool calls that required human-in-the-loop approval."""
    metadata: dict[str, dict[str, Any]] = field(default_factory=dict[str, dict[str, Any]])
    """Metadata for deferred tool calls, keyed by `tool_call_id`. Each value will be available in the tool's RunContext as `tool_call_metadata`."""

```

---|---
####  calls `class-attribute` `instance-attribute`
```
calls: [, DeferredToolCallResult[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolCallResult "DeferredToolCallResult



      module-attribute
   \(pydantic_ai.tools.DeferredToolCallResult\)") | ] = (
    default_factory=[, DeferredToolCallResult[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolCallResult "DeferredToolCallResult



      module-attribute
   \(pydantic_ai.tools.DeferredToolCallResult\)") | ]
)

```

Map of tool call IDs to results for tool calls that required external execution.
####  approvals `class-attribute` `instance-attribute`
```
approvals: [,  | DeferredToolApprovalResult[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolApprovalResult "DeferredToolApprovalResult



      module-attribute
   \(pydantic_ai.tools.DeferredToolApprovalResult\)")] = (
    (
        default_factory=[
            ,  | DeferredToolApprovalResult[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolApprovalResult "DeferredToolApprovalResult



      module-attribute
   \(pydantic_ai.tools.DeferredToolApprovalResult\)")
        ]
    )
)

```

Map of tool call IDs to results for tool calls that required human-in-the-loop approval.
####  metadata `class-attribute` `instance-attribute`
```
metadata: [, [, ]] = (
    default_factory=[, [, ]]
)

```

Metadata for deferred tool calls, keyed by `tool_call_id`. Each value will be available in the tool's RunContext as `tool_call_metadata`.
###  ToolAgentDepsT `module-attribute`
```
ToolAgentDepsT = TypeVar(
    "ToolAgentDepsT", default=, contravariant=True
