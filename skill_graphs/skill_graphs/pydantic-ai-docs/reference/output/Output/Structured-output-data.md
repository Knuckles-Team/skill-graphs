## Structured output data
The [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent "Agent



      dataclass
  ") class constructor takes an `output_type` argument that takes one or more types or [output functions](https://ai.pydantic.dev/output/#output-functions). It supports simple scalar types, list and dict types (including `TypedDict`s and [`StructuredDict`s](https://ai.pydantic.dev/output/#structured-dict)), dataclasses and Pydantic models, as well as type unions -- generally everything supported as type hints in a Pydantic model. You can also pass a list of multiple choices.
By default, Pydantic AI leverages the model's tool calling capability to make it return structured data. When multiple output types are specified (in a union or list), each member is registered with the model as a separate output tool in order to reduce the complexity of the schema and maximise the chances a model will respond correctly. This has been shown to work well across a wide range of models. If you'd like to change the names of the output tools, use a model's native structured output feature, or pass the output schema to the model in its [instructions](https://ai.pydantic.dev/agent/#instructions), you can use an [output mode](https://ai.pydantic.dev/output/#output-modes) marker class.
When no output type is specified, or when `str` is among the output types, any plain text response from the model will be used as the output data. If `str` is not among the output types, the model is forced to return structured data or call an output function.
If the output type schema is not of type `"object"` (e.g. it's `int` or `list[int]`), the output type is wrapped in a single element object, so the schema of all tools registered with the model are object schemas.
Structured outputs (like tools) use Pydantic to build the JSON schema used for the tool, and to validate the data returned by the model.
Type checking considerations
The Agent class is generic in its output type, and this type is carried through to `AgentRunResult.output` and `StreamedRunResult.output` so that your IDE or static type checker can warn you when your code doesn't properly take into account all the possible values those outputs could have.
Static type checkers like pyright and mypy will do their best to infer the agent's output type from the `output_type` you've specified, but they're not always able to do so correctly when you provide functions or multiple types in a union or list, even though Pydantic AI will behave correctly. When this happens, your type checker will complain even when you're confident you've passed a valid `output_type`, and you'll need to help the type checker by explicitly specifying the generic parameters on the `Agent` constructor. This is shown in the second example below and the output functions example further down.
Specifically, there are three valid uses of `output_type` where you'll need to do this:
  1. When using a union of types, e.g. `output_type=Foo | Bar`. Until `output_type`. In addition to the generic parameters on the `Agent` constructor, you'll need to add `# type: ignore` to the line that passes the union to `output_type`. Alternatively, you can use a list: `output_type=[Foo, Bar]`.
  2. With mypy: When using a list, as a functionally equivalent alternative to a union, or because you're passing in [output functions](https://ai.pydantic.dev/output/#output-functions). Pyright does handle this correctly, and we've filed
  3. With mypy: when using an async output function. Pyright does handle this correctly, and we've filed


Here's an example of returning either text or structured data:
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_2_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_2_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) box_or_error.py```
from pydantic import BaseModel

from pydantic_ai import Agent


class Box(BaseModel):
    width: int
    height: int
    depth: int
    units: str


agent = Agent(
    'gateway/openai:gpt-5-mini',
    output_type=[Box, str], [](https://ai.pydantic.dev/output/#__code_2_annotation_1)
    instructions=(
        "Extract me the dimensions of a box, "
        "if you can't extract all data, ask the user to try again."
    ),
)

result = agent.run_sync('The box is 10x20x30')
print(result.output)
#> Please provide the units for the dimensions (e.g., cm, in, m).

result = agent.run_sync('The box is 10x20x30 cm')
print(result.output)
#> width=10 height=20 depth=30 units='cm'

```

box_or_error.py```
from pydantic import BaseModel

from pydantic_ai import Agent


class Box(BaseModel):
    width: int
    height: int
    depth: int
    units: str


agent = Agent(
    'openai:gpt-5-mini',
    output_type=[Box, str],

[](https://ai.pydantic.dev/output/#__code_3_annotation_1)
    instructions=(
        "Extract me the dimensions of a box, "
        "if you can't extract all data, ask the user to try again."
    ),
)

result = agent.run_sync('The box is 10x20x30')
print(result.output)
#> Please provide the units for the dimensions (e.g., cm, in, m).

result = agent.run_sync('The box is 10x20x30 cm')
print(result.output)
#> width=10 height=20 depth=30 units='cm'

```

  1. This could also have been a union: `output_type=Box | str`. However, as explained in the "Type checking considerations" section above, that would've required explicitly specifying the generic parameters on the `Agent` constructor and adding `# type: ignore` to this line in order to be type checked correctly.


_(This example is complete, it can be run "as is")_
Here's an example of using a union return type, which will register multiple output tools and wrap non-object schemas in an object:
colors_or_sizes.py```
from pydantic_ai import Agent

agent = Agent[None, list[str] | list[int]](
    'openai:gpt-5-mini',
    output_type=list[str] | list[int],  [](https://ai.pydantic.dev/output/#__code_4_annotation_1)
    instructions='Extract either colors or sizes from the shapes provided.',
)

result = agent.run_sync('red square, blue circle, green triangle')
print(result.output)
#> ['red', 'blue', 'green']

result = agent.run_sync('square size 10, circle size 20, triangle size 30')
print(result.output)
#> [10, 20, 30]

```

_(This example is complete, it can be run "as is")_
### Output functions
Instead of plain text or structured data, you may want the output of your agent run to be the result of a function called with arguments provided by the model, for example to further process or validate the data provided through the arguments (with the option to tell the model to try again), or to hand off to another agent.
Output functions are similar to [function tools](https://ai.pydantic.dev/tools/), but the model is forced to call one of them, the call ends the agent run, and the result is not passed back to the model.
As with tool functions, output function arguments provided by the model are validated using Pydantic (with optional [validation context](https://ai.pydantic.dev/output/#validation-context)), can optionally take [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as the first argument, and can raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") to ask the model to try again with modified arguments (or with a different output type).
To specify output functions, you set the agent's `output_type` to either a single function (or bound instance method), or a list of functions. The list can also contain other output types like simple scalars or entire Pydantic models. You typically do not want to also register your output function as a tool (using the `@agent.tool` decorator or `tools` argument), as this could confuse the model about which it should be calling.
Here's an example of all of these features in action:
output_functions.py```
import re

from pydantic import BaseModel

from pydantic_ai import Agent, ModelRetry, RunContext, UnexpectedModelBehavior


class Row(BaseModel):
    name: str
    country: str


tables = {
    'capital_cities': [
        Row(name='Amsterdam', country='Netherlands'),
        Row(name='Mexico City', country='Mexico'),
    ]
}


class SQLFailure(BaseModel):
    """An unrecoverable failure. Only use this when you can't change the query to make it work."""

    explanation: str


def run_sql_query(query: str) -> list[Row]:
    """Run a SQL query on the database."""

    select_table = re.match(r'SELECT (.+) FROM (\w+)', query)
    if select_table:
        column_names = select_table.group(1)
        if column_names != '*':
            raise ModelRetry("Only 'SELECT *' is supported, you'll have to do column filtering manually.")

        table_name = select_table.group(2)
        if table_name not in tables:
            raise ModelRetry(
                f"Unknown table '{table_name}' in query '{query}'. Available tables: {', '.join(tables.keys())}."
            )

        return tables[table_name]

    raise ModelRetry(f"Unsupported query: '{query}'.")


sql_agent = Agent[None, list[Row] | SQLFailure](
    'openai:gpt-5.2',
    output_type=[run_sql_query, SQLFailure],
    instructions='You are a SQL agent that can run SQL queries on a database.',
)


async def hand_off_to_sql_agent(ctx: RunContext, query: str) -> list[Row]:
    """I take natural language queries, turn them into SQL, and run them on a database."""

    # Drop the final message with the output tool call, as it shouldn't be passed on to the SQL agent
    messages = ctx.messages[:-1]
    try:
        result = await sql_agent.run(query, message_history=messages)
        output = result.output
        if isinstance(output, SQLFailure):
            raise ModelRetry(f'SQL agent failed: {output.explanation}')
        return output
    except UnexpectedModelBehavior as e:
        # Bubble up potentially retryable errors to the router agent
        if (cause := e.__cause__) and isinstance(cause, ModelRetry):
            raise ModelRetry(f'SQL agent failed: {cause.message}') from e
        else:
            raise


class RouterFailure(BaseModel):
    """Use me when no appropriate agent is found or the used agent failed."""

    explanation: str


router_agent = Agent[None, list[Row] | RouterFailure](
    'openai:gpt-5.2',
    output_type=[hand_off_to_sql_agent, RouterFailure],
    instructions='You are a router to other agents. Never try to solve a problem yourself, just pass it on.',
)

result = router_agent.run_sync('Select the names and countries of all capitals')
print(result.output)
"""
[
    Row(name='Amsterdam', country='Netherlands'),
    Row(name='Mexico City', country='Mexico'),
]
"""

result = router_agent.run_sync('Select all pets')
print(repr(result.output))
"""
RouterFailure(explanation="The requested table 'pets' does not exist in the database. The only available table is 'capital_cities', which does not contain data about pets.")
"""

result = router_agent.run_sync('How do I fly from Amsterdam to Mexico City?')
print(repr(result.output))
"""
RouterFailure(explanation='I am not equipped to provide travel information, such as flights from Amsterdam to Mexico City.')
"""

```

#### Text output
If you provide an output function that takes a string, Pydantic AI will by default create an output tool like for any other output function. If instead you'd like the model to provide the string using plain text output, you can wrap the function in the [`TextOutput`](https://ai.pydantic.dev/api/output/#pydantic_ai.output.TextOutput "TextOutput



      dataclass
  ") marker class.
If desired, this marker class can be used alongside one or more [`ToolOutput`](https://ai.pydantic.dev/output/#tool-output) marker classes (or unmarked types or functions) in a list provided to `output_type`.
Like other output functions, text output functions can optionally take [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") as the first argument, and can raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry "ModelRetry") to ask the model to try again with modified arguments (or with a different output type).
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_3_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_3_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) text_output_function.py```
from pydantic_ai import Agent, TextOutput


def split_into_words(text: str) -> list[str]:
    return text.split()


agent = Agent(
    'gateway/openai:gpt-5.2',
    output_type=TextOutput(split_into_words),
)
result = agent.run_sync('Who was Albert Einstein?')
print(result.output)
#> ['Albert', 'Einstein', 'was', 'a', 'German-born', 'theoretical', 'physicist.']

```

text_output_function.py```
from pydantic_ai import Agent, TextOutput


def split_into_words(text: str) -> list[str]:
    return text.split()


agent = Agent(
    'openai:gpt-5.2',
    output_type=TextOutput(split_into_words),
)
result = agent.run_sync('Who was Albert Einstein?')
print(result.output)
#> ['Albert', 'Einstein', 'was', 'a', 'German-born', 'theoretical', 'physicist.']

```

_(This example is complete, it can be run "as is")_
#### Handling partial output in output functions
When streaming with `run_stream()` or `run_stream_sync()`, output functions are called **multiple times** — once for each partial output received from the model, and once for the final complete output.
You should check the [`RunContext.partial_output`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.partial_output "partial_output



      class-attribute
      instance-attribute
  ") flag when your output function has **side effects** (e.g., sending notifications, logging, database updates) that should only execute on the final output.
When streaming, `partial_output` is `True` for each partial output and `False` for the final complete output. For all [other run methods](https://ai.pydantic.dev/agent/#running-agents), `partial_output` is always `False` as the function is only called once with the complete output.
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_4_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_4_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) output_function_with_side_effects.py```
from pydantic import BaseModel

from pydantic_ai import Agent, RunContext


class DatabaseRecord(BaseModel):
    name: str
    value: int | None = None  # Make optional to allow partial output


def save_to_database(ctx: RunContext, record: DatabaseRecord) -> DatabaseRecord:
    """Output function with side effect - only save final output to database."""
    if ctx.partial_output:
        # Skip side effects for partial outputs
        return record

    # Only execute side effect for the final output
    print(f'Saving to database: {record.name} = {record.value}')
    #> Saving to database: test = 42
    return record


agent = Agent('gateway/openai:gpt-5.2', output_type=save_to_database)


async def main():
    async with agent.run_stream('Create a record with name "test" and value 42') as result:
        async for output in result.stream_output(debounce_by=None):
            print(output)
            #> name='test' value=None
            #> name='test' value=42

```

output_function_with_side_effects.py```
from pydantic import BaseModel

from pydantic_ai import Agent, RunContext


class DatabaseRecord(BaseModel):
    name: str
    value: int | None = None  # Make optional to allow partial output


def save_to_database(ctx: RunContext, record: DatabaseRecord) -> DatabaseRecord:
    """Output function with side effect - only save final output to database."""
    if ctx.partial_output:
        # Skip side effects for partial outputs
        return record

    # Only execute side effect for the final output
    print(f'Saving to database: {record.name} = {record.value}')
    #> Saving to database: test = 42
    return record


agent = Agent('openai:gpt-5.2', output_type=save_to_database)


async def main():
    async with agent.run_stream('Create a record with name "test" and value 42') as result:
        async for output in result.stream_output(debounce_by=None):
            print(output)
            #> name='test' value=None
            #> name='test' value=42

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
### Output modes
Pydantic AI implements three different methods to get a model to output structured data:
  1. [Tool Output](https://ai.pydantic.dev/output/#tool-output), where tool calls are used to produce the output.
  2. [Native Output](https://ai.pydantic.dev/output/#native-output), where the model is required to produce text content compliant with a provided JSON schema.
  3. [Prompted Output](https://ai.pydantic.dev/output/#prompted-output), where a prompt is injected into the model instructions including the desired JSON schema, and we attempt to parse the model's plain-text response as appropriate.


#### Tool Output
In the default Tool Output mode, the output JSON schema of each output type (or function) is provided to the model as the parameters schema of a special output tool. This is the default as it's supported by virtually all models and has been shown to work very well.
If you'd like to change the name of the output tool, pass a custom description to aid the model, or turn on or off strict mode, you can wrap the type(s) in the [`ToolOutput`](https://ai.pydantic.dev/api/output/#pydantic_ai.output.ToolOutput "ToolOutput



      dataclass
  ") marker class and provide the appropriate arguments. Note that by default, the description is taken from the docstring specified on a Pydantic model or output function, so specifying it using the marker class is typically not necessary.
To dynamically modify or filter the available output tools during an agent run, you can define an agent-wide `prepare_output_tools` function that will be called ahead of each step of a run. This function should be of type [`ToolsPrepareFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolsPrepareFunc "ToolsPrepareFunc



      module-attribute
  "), which takes the [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") and a list of [`ToolDefinition`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "ToolDefinition



      dataclass
  "), and returns a new list of tool definitions (or `None` to disable all tools for that step). This is analogous to the [`prepare_tools` function](https://ai.pydantic.dev/tools-advanced/#prepare-tools) for non-output tools.
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_5_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_5_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) tool_output.py```
from pydantic import BaseModel

from pydantic_ai import Agent, ToolOutput


class Fruit(BaseModel):
    name: str
    color: str


class Vehicle(BaseModel):
    name: str
    wheels: int


agent = Agent(
    'gateway/openai:gpt-5.2',
    output_type=[ [](https://ai.pydantic.dev/output/#__code_10_annotation_1)
        ToolOutput(Fruit, name='return_fruit'),
        ToolOutput(Vehicle, name='return_vehicle'),
    ],
)
result = agent.run_sync('What is a banana?')
print(repr(result.output))
#> Fruit(name='banana', color='yellow')

```

tool_output.py```
from pydantic import BaseModel

from pydantic_ai import Agent, ToolOutput


class Fruit(BaseModel):
    name: str
    color: str


class Vehicle(BaseModel):
    name: str
    wheels: int


agent = Agent(
    'openai:gpt-5.2',
    output_type=[

[](https://ai.pydantic.dev/output/#__code_11_annotation_1)
        ToolOutput(Fruit, name='return_fruit'),
        ToolOutput(Vehicle, name='return_vehicle'),
    ],
)
result = agent.run_sync('What is a banana?')
print(repr(result.output))
#> Fruit(name='banana', color='yellow')

```

  1. If we were passing just `Fruit` and `Vehicle` without custom tool names, we could have used a union: `output_type=Fruit | Vehicle`. However, as `ToolOutput` is an object rather than a type, we have to use a list.


_(This example is complete, it can be run "as is")_
##### Parallel Output Tool Calls
When the model calls other tools in parallel with an output tool, you can control how tool calls are executed by setting the agent's [`end_strategy`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.end_strategy "end_strategy



      instance-attribute
  "):
  * `'early'` (default): Output tools are executed first. Once a valid final result is found, remaining function and output tool calls are skipped
  * `'exhaustive'`: Output tools are executed first, then all function tools are executed. The first valid output tool result becomes the final output


The `'exhaustive'` strategy is useful when tools have important side effects (like logging, sending notifications, or updating metrics) that should always execute.
Priority of output and deferred tools in streaming methods
The [`run_stream()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream "run_stream



      async
  ") and [`run_stream_sync()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AbstractAgent.run_stream_sync "run_stream_sync") methods will consider the first output that matches the [output type](https://ai.pydantic.dev/output/#structured-output) (which could be text, an [output tool](https://ai.pydantic.dev/output/#tool-output) call, or a [deferred](https://ai.pydantic.dev/deferred-tools/) tool call) to be the final output of the agent run, even when the model generates (additional) tool calls after this "final" output.
This means that if the model calls deferred tools before output tools when using these methods, the deferred tool calls determine the agent run's final output, while the other [run methods](https://ai.pydantic.dev/agent/#running-agents) would have prioritized the tool output.
#### Native Output
Native Output mode uses a model's native "Structured Outputs" feature (aka "JSON Schema response format"), where the model is forced to only output text matching the provided JSON schema. Note that this is not supported by all models, and sometimes comes with restrictions. For example, Gemini cannot use tools at the same time as structured output, and attempting to do so will result in an error.
To use this mode, you can wrap the output type(s) in the [`NativeOutput`](https://ai.pydantic.dev/api/output/#pydantic_ai.output.NativeOutput "NativeOutput



      dataclass
  ") marker class that also lets you specify a `name` and `description` if the name and docstring of the type or function are not sufficient.
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_6_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_6_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) native_output.py```
from pydantic_ai import Agent, NativeOutput

from tool_output import Fruit, Vehicle

agent = Agent(
    'gateway/openai:gpt-5.2',
    output_type=NativeOutput(
        [Fruit, Vehicle], [](https://ai.pydantic.dev/output/#__code_12_annotation_1)
        name='Fruit_or_vehicle',
        description='Return a fruit or vehicle.'
    ),
)
result = agent.run_sync('What is a Ford Explorer?')
print(repr(result.output))
#> Vehicle(name='Ford Explorer', wheels=4)

```

native_output.py```
from pydantic_ai import Agent, NativeOutput

from tool_output import Fruit, Vehicle

agent = Agent(
    'openai:gpt-5.2',
    output_type=NativeOutput(
        [Fruit, Vehicle],

[](https://ai.pydantic.dev/output/#__code_13_annotation_1)
        name='Fruit_or_vehicle',
        description='Return a fruit or vehicle.'
    ),
)
result = agent.run_sync('What is a Ford Explorer?')
print(repr(result.output))
#> Vehicle(name='Ford Explorer', wheels=4)

```

  1. This could also have been a union: `output_type=Fruit | Vehicle`. However, as explained in the "Type checking considerations" section above, that would've required explicitly specifying the generic parameters on the `Agent` constructor and adding `# type: ignore` to this line in order to be type checked correctly.


_(This example is complete, it can be run "as is")_
#### Prompted Output
In this mode, the model is prompted to output text matching the provided JSON schema through its [instructions](https://ai.pydantic.dev/agent/#instructions) and it's up to the model to interpret those instructions correctly. This is usable with all models, but is often the least reliable approach as the model is not forced to match the schema.
While we would generally suggest starting with tool or native output, in some cases this mode may result in higher quality outputs, and for models without native tool calling or structured output support it is the only option for producing structured outputs.
If the model API supports the "JSON Mode" feature (aka "JSON Object response format") to force the model to output valid JSON, this is enabled, but it's still up to the model to abide by the schema. Pydantic AI will validate the returned structured data and tell the model to try again if validation fails, but if the model is not intelligent enough this may not be sufficient.
To use this mode, you can wrap the output type(s) in the [`PromptedOutput`](https://ai.pydantic.dev/api/output/#pydantic_ai.output.PromptedOutput "PromptedOutput



      dataclass
  ") marker class that also lets you specify a `name` and `description` if the name and docstring of the type or function are not sufficient. Additionally, `template` lets you specify a custom instructions template to be used instead of the [default](https://ai.pydantic.dev/api/profiles/#pydantic_ai.profiles.ModelProfile.prompted_output_template "prompted_output_template



      class-attribute
      instance-attribute
  "), or `template=False` to disable the schema prompt entirely.
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_7_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_7_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) prompted_output.py```
from pydantic import BaseModel

from pydantic_ai import Agent, PromptedOutput

from tool_output import Vehicle


class Device(BaseModel):
    name: str
    kind: str


agent = Agent(
    'gateway/openai:gpt-5.2',
    output_type=PromptedOutput(
        [Vehicle, Device], [](https://ai.pydantic.dev/output/#__code_14_annotation_1)
        name='Vehicle or device',
        description='Return a vehicle or device.'
    ),
)
result = agent.run_sync('What is a MacBook?')
print(repr(result.output))
#> Device(name='MacBook', kind='laptop')

agent = Agent(
    'gateway/openai:gpt-5.2',
    output_type=PromptedOutput(
        [Vehicle, Device],
        template='Gimme some JSON: {schema}'
    ),
)
result = agent.run_sync('What is a Ford Explorer?')
print(repr(result.output))
#> Vehicle(name='Ford Explorer', wheels=4)

```

prompted_output.py```
from pydantic import BaseModel

from pydantic_ai import Agent, PromptedOutput

from tool_output import Vehicle


class Device(BaseModel):
    name: str
    kind: str


agent = Agent(
    'openai:gpt-5.2',
    output_type=PromptedOutput(
        [Vehicle, Device],

[](https://ai.pydantic.dev/output/#__code_15_annotation_1)
        name='Vehicle or device',
        description='Return a vehicle or device.'
    ),
)
result = agent.run_sync('What is a MacBook?')
print(repr(result.output))
#> Device(name='MacBook', kind='laptop')

agent = Agent(
    'openai:gpt-5.2',
    output_type=PromptedOutput(
        [Vehicle, Device],
        template='Gimme some JSON: {schema}'
    ),
)
result = agent.run_sync('What is a Ford Explorer?')
print(repr(result.output))
#> Vehicle(name='Ford Explorer', wheels=4)

```

  1. This could also have been a union: `output_type=Vehicle | Device`. However, as explained in the "Type checking considerations" section above, that would've required explicitly specifying the generic parameters on the `Agent` constructor and adding `# type: ignore` to this line in order to be type checked correctly.


_(This example is complete, it can be run "as is")_
### Custom JSON schema
If it's not feasible to define your desired structured output object using a Pydantic `BaseModel`, dataclass, or `TypedDict`, for example when you get a JSON schema from an external source or generate it dynamically, you can use the [`StructuredDict()`](https://ai.pydantic.dev/api/output/#pydantic_ai.output.StructuredDict "StructuredDict") helper function to generate a `dict[str, Any]` subclass with a JSON schema attached that Pydantic AI will pass to the model.
Note that Pydantic AI will not perform any validation of the received JSON object and it's up to the model to correctly interpret the schema and any constraints expressed in it, like required fields or integer value ranges.
The output type will be a `dict[str, Any]` and it's up to your code to defensively read from it in case the model made a mistake. You can use an [output validator](https://ai.pydantic.dev/output/#output-validator-functions) to reflect validation errors back to the model and get it to try again.
Along with the JSON schema, you can optionally pass `name` and `description` arguments to provide additional context to the model:
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_8_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_8_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway)```
from pydantic_ai import Agent, StructuredDict

HumanDict = StructuredDict(
    {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'age': {'type': 'integer'}
        },
        'required': ['name', 'age']
    },
    name='Human',
    description='A human with a name and age',
)

agent = Agent('gateway/openai:gpt-5.2', output_type=HumanDict)
result = agent.run_sync('Create a person')
#> {'name': 'John Doe', 'age': 30}

```

```
from pydantic_ai import Agent, StructuredDict

HumanDict = StructuredDict(
    {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'age': {'type': 'integer'}
        },
        'required': ['name', 'age']
    },
    name='Human',
    description='A human with a name and age',
)

agent = Agent('openai:gpt-5.2', output_type=HumanDict)
result = agent.run_sync('Create a person')
#> {'name': 'John Doe', 'age': 30}

```

### Validation context
Some validation relies on an extra Pydantic [context](https://docs.pydantic.dev/latest/concepts/validators/#validation-context) object. You can pass such an object to an `Agent` at definition-time via its [`validation_context`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__ "__init__") parameter. It will be used in the validation of both structured outputs and [tool arguments](https://ai.pydantic.dev/tools-advanced/#tool-retries).
This validation context can be either:
  * the context object itself (`Any`), used as-is to validate outputs, or
  * a function that takes the [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "RunContext



      dataclass
  ") and returns a context object (`Any`). This function will be called automatically before each validation, allowing you to build a dynamic validation context.


Don't confuse this _validation_ context with the _LLM_ context
This Pydantic validation context object is only used internally by Pydantic AI for tool arg and output validation. In particular, it is **not** included in the prompts or messages sent to the language model.
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_9_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_9_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) validation_context.py```
from dataclasses import dataclass

from pydantic import BaseModel, ValidationInfo, field_validator

from pydantic_ai import Agent


class Value(BaseModel):
    x: int

    @field_validator('x')
    def increment_value(cls, value: int, info: ValidationInfo):
        return value + (info.context or 0)


agent = Agent(
    'gateway/gemini:gemini-3-flash-preview',
    output_type=Value,
    validation_context=10,
)
result = agent.run_sync('Give me a value of 5.')
print(repr(result.output))  # 5 from the model + 10 from the validation context
#> Value(x=15)


@dataclass
class Deps:
    increment: int


agent = Agent(
    'gateway/gemini:gemini-3-flash-preview',
    output_type=Value,
    deps_type=Deps,
    validation_context=lambda ctx: ctx.deps.increment,
)
result = agent.run_sync('Give me a value of 5.', deps=Deps(increment=10))
print(repr(result.output))  # 5 from the model + 10 from the validation context
#> Value(x=15)

```

validation_context.py```
from dataclasses import dataclass

from pydantic import BaseModel, ValidationInfo, field_validator

from pydantic_ai import Agent


class Value(BaseModel):
    x: int

    @field_validator('x')
    def increment_value(cls, value: int, info: ValidationInfo):
        return value + (info.context or 0)


agent = Agent(
    'google-gla:gemini-3-flash-preview',
    output_type=Value,
    validation_context=10,
)
result = agent.run_sync('Give me a value of 5.')
print(repr(result.output))  # 5 from the model + 10 from the validation context
#> Value(x=15)


@dataclass
class Deps:
    increment: int


agent = Agent(
    'google-gla:gemini-3-flash-preview',
    output_type=Value,
    deps_type=Deps,
    validation_context=lambda ctx: ctx.deps.increment,
)
result = agent.run_sync('Give me a value of 5.', deps=Deps(increment=10))
print(repr(result.output))  # 5 from the model + 10 from the validation context
#> Value(x=15)

```

_(This example is complete, it can be run "as is")_
### Output validators
Some validation is inconvenient or impossible to do in Pydantic validators, in particular when the validation requires IO and is asynchronous. Pydantic AI provides a way to add validation functions via the [`agent.output_validator`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.output_validator "output_validator") decorator.
If you want to implement separate validation logic for different output types, it's recommended to use [output functions](https://ai.pydantic.dev/output/#output-functions) instead, to save you from having to do `isinstance` checks inside the output validator. If you want the model to output plain text, do your own processing or validation, and then have the agent's final output be the result of your function, it's recommended to use an [output function](https://ai.pydantic.dev/output/#output-functions) with the [`TextOutput` marker class](https://ai.pydantic.dev/output/#text-output).
Here's a simplified variant of the [SQL Generation example](https://ai.pydantic.dev/examples/sql-gen/):
sql_gen.py```
from fake_database import DatabaseConn, QueryError
from pydantic import BaseModel

from pydantic_ai import Agent, RunContext, ModelRetry


class Success(BaseModel):
    sql_query: str


class InvalidRequest(BaseModel):
    error_message: str


Output = Success | InvalidRequest
agent = Agent[DatabaseConn, Output](
    'google-gla:gemini-3-flash-preview',
    output_type=Output,  # type: ignore
    deps_type=DatabaseConn,
    instructions='Generate PostgreSQL flavored SQL queries based on user input.',
)


@agent.output_validator
async def validate_sql(ctx: RunContext[DatabaseConn], output: Output) -> Output:
    if isinstance(output, InvalidRequest):
        return output
    try:
        await ctx.deps.execute(f'EXPLAIN {output.sql_query}')
    except QueryError as e:
        raise ModelRetry(f'Invalid query: {e}') from e
    else:
        return output


result = agent.run_sync(
    'get me users who were last active yesterday.', deps=DatabaseConn()
)
print(result.output)
#> sql_query='SELECT * FROM users WHERE last_active::date = today() - interval 1 day'

```

_(This example is complete, it can be run "as is")_
#### Handling partial output in output validators
When streaming with `run_stream()` or `run_stream_sync()`, output validators are called **multiple times** — once for each partial output received from the model, and once for the final complete output.
You should check the [`RunContext.partial_output`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.partial_output "partial_output



      class-attribute
      instance-attribute
  ") flag when you want to **validate only the complete result** , not intermediate partial values.
When streaming, `partial_output` is `True` for each partial output and `False` for the final complete output. For all [other run methods](https://ai.pydantic.dev/agent/#running-agents), `partial_output` is always `False` as the validator is only called once with the complete output.
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_10_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_10_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) partial_validation_streaming.py```
from pydantic_ai import Agent, ModelRetry, RunContext

agent = Agent('gateway/openai:gpt-5.2')


@agent.output_validator
def validate_output(ctx: RunContext, output: str) -> str:
    if ctx.partial_output:
        return output

    if len(output) < 50:
        raise ModelRetry('Output is too short.')
    return output


async def main():
    async with agent.run_stream('Write a long story about a cat') as result:
        async for message in result.stream_text():
            print(message)
            #> Once upon a
            #> Once upon a time, there was
            #> Once upon a time, there was a curious cat
            #> Once upon a time, there was a curious cat named Whiskers who
            #> Once upon a time, there was a curious cat named Whiskers who loved to explore
            #> Once upon a time, there was a curious cat named Whiskers who loved to explore the world around
            #> Once upon a time, there was a curious cat named Whiskers who loved to explore the world around him...

```

partial_validation_streaming.py```
from pydantic_ai import Agent, ModelRetry, RunContext

agent = Agent('openai:gpt-5.2')


@agent.output_validator
def validate_output(ctx: RunContext, output: str) -> str:
    if ctx.partial_output:
        return output

    if len(output) < 50:
        raise ModelRetry('Output is too short.')
    return output


async def main():
    async with agent.run_stream('Write a long story about a cat') as result:
        async for message in result.stream_text():
            print(message)
            #> Once upon a
            #> Once upon a time, there was
            #> Once upon a time, there was a curious cat
            #> Once upon a time, there was a curious cat named Whiskers who
            #> Once upon a time, there was a curious cat named Whiskers who loved to explore
            #> Once upon a time, there was a curious cat named Whiskers who loved to explore the world around
            #> Once upon a time, there was a curious cat named Whiskers who loved to explore the world around him...

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
