
    Returns:
        A downcast version of this result if the value is an instance of one of the given types,
        otherwise None.
    """
    # Check if value matches any of the target types, handling bool as a special case
    for value_type in value_types:
        if isinstance(self.value, value_type):
            # Only match bool with explicit bool type
            if isinstance(self.value, bool) and value_type is not bool:
                continue
            return cast(EvaluationResult[T], self)
    return None

```

---|---
###  Evaluator `dataclass`
Bases: `BaseEvaluator`, `InputsT, OutputT, MetadataT]`
Base class for all evaluators.
Evaluators can assess the performance of a task in a variety of ways, as a function of the EvaluatorContext.
Subclasses must implement the `evaluate` method. Note it can be defined with either `def` or `async def`.
Example:
```
from dataclasses import dataclass

from pydantic_evals.evaluators import Evaluator, EvaluatorContext


@dataclass
class ExactMatch(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> bool:
        return ctx.output == ctx.expected_output

```

Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
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
200
201
202
203
204
205
206
207
208
209
210
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
```
| ```
@dataclass(repr=False)
class Evaluator(BaseEvaluator, Generic[InputsT, OutputT, MetadataT]):
    """Base class for all evaluators.

    Evaluators can assess the performance of a task in a variety of ways, as a function of the EvaluatorContext.

    Subclasses must implement the `evaluate` method. Note it can be defined with either `def` or `async def`.

    Example:
```python
    from dataclasses import dataclass

    from pydantic_evals.evaluators import Evaluator, EvaluatorContext


    @dataclass
    class ExactMatch(Evaluator):
        def evaluate(self, ctx: EvaluatorContext) -> bool:
            return ctx.output == ctx.expected_output
```
    """

    @classmethod
    @deprecated('`name` has been renamed, use `get_serialization_name` instead.')
    def name(cls) -> str:
        """`name` has been renamed, use `get_serialization_name` instead."""
        return cls.get_serialization_name()

    def get_default_evaluation_name(self) -> str:
        """Return the default name to use in reports for the output of this evaluator.

        By default, if the evaluator has an attribute called `evaluation_name` of type string, that will be used.
        Otherwise, the serialization name of the evaluator (which is usually the class name) will be used.

        This can be overridden to get a more descriptive name in evaluation reports, e.g. using instance information.

        Note that evaluators that return a mapping of results will always use the keys of that mapping as the names
        of the associated evaluation results.
        """
        evaluation_name = getattr(self, 'evaluation_name', None)
        if isinstance(evaluation_name, str):
            # If the evaluator has an attribute `name` of type string, use that
            return evaluation_name

        return self.get_serialization_name()

    @abstractmethod
    def evaluate(
        self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]
    ) -> EvaluatorOutput | Awaitable[EvaluatorOutput]:  # pragma: no cover
        """Evaluate the task output in the given context.

        This is the main evaluation method that subclasses must implement. It can be either synchronous
        or asynchronous, returning either an EvaluatorOutput directly or an Awaitable[EvaluatorOutput].

        Args:
            ctx: The context containing the inputs, outputs, and metadata for evaluation.

        Returns:
            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
            of evaluation names to either of those. Can be returned either synchronously or as an
            awaitable for asynchronous evaluation.
        """
        raise NotImplementedError('You must implement `evaluate`.')

    def evaluate_sync(self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]) -> EvaluatorOutput:
        """Run the evaluator synchronously, handling both sync and async implementations.

        This method ensures synchronous execution by running any async evaluate implementation
        to completion using run_until_complete.

        Args:
            ctx: The context containing the inputs, outputs, and metadata for evaluation.

        Returns:
            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
            of evaluation names to either of those.
        """
        output = self.evaluate(ctx)
        if inspect.iscoroutine(output):  # pragma: no cover
            return get_event_loop().run_until_complete(output)
        else:
            return cast(EvaluatorOutput, output)

    async def evaluate_async(self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]) -> EvaluatorOutput:
        """Run the evaluator asynchronously, handling both sync and async implementations.

        This method ensures asynchronous execution by properly awaiting any async evaluate
        implementation. For synchronous implementations, it returns the result directly.

        Args:
            ctx: The context containing the inputs, outputs, and metadata for evaluation.

        Returns:
            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
            of evaluation names to either of those.
        """
        # Note: If self.evaluate is synchronous, but you need to prevent this from blocking, override this method with:
        # return await anyio.to_thread.run_sync(self.evaluate, ctx)
        output = self.evaluate(ctx)
        if inspect.iscoroutine(output):
            return await output
        else:
            return cast(EvaluatorOutput, output)

```

---|---
####  name `classmethod` `deprecated`
```
name() ->

```

Deprecated
`name` has been renamed, use `get_serialization_name` instead.
`name` has been renamed, use `get_serialization_name` instead.
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
140
141
142
143
144
```
| ```
@classmethod
@deprecated('`name` has been renamed, use `get_serialization_name` instead.')
def name(cls) -> str:
    """`name` has been renamed, use `get_serialization_name` instead."""
    return cls.get_serialization_name()

```

---|---
####  get_default_evaluation_name
```
get_default_evaluation_name() ->

```

Return the default name to use in reports for the output of this evaluator.
By default, if the evaluator has an attribute called `evaluation_name` of type string, that will be used. Otherwise, the serialization name of the evaluator (which is usually the class name) will be used.
This can be overridden to get a more descriptive name in evaluation reports, e.g. using instance information.
Note that evaluators that return a mapping of results will always use the keys of that mapping as the names of the associated evaluation results.
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
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
```
| ```
def get_default_evaluation_name(self) -> str:
    """Return the default name to use in reports for the output of this evaluator.

    By default, if the evaluator has an attribute called `evaluation_name` of type string, that will be used.
    Otherwise, the serialization name of the evaluator (which is usually the class name) will be used.

    This can be overridden to get a more descriptive name in evaluation reports, e.g. using instance information.

    Note that evaluators that return a mapping of results will always use the keys of that mapping as the names
    of the associated evaluation results.
    """
    evaluation_name = getattr(self, 'evaluation_name', None)
    if isinstance(evaluation_name, str):
        # If the evaluator has an attribute `name` of type string, use that
        return evaluation_name

    return self.get_serialization_name()

```

---|---
####  evaluate `abstractmethod`
```
evaluate(
    ctx: EvaluatorContext[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorContext "EvaluatorContext



      dataclass
   \(pydantic_evals.evaluators.context.EvaluatorContext\)")[InputsT, OutputT, MetadataT],
) -> EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)") | [EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")]

```

Evaluate the task output in the given context.
This is the main evaluation method that subclasses must implement. It can be either synchronous or asynchronous, returning either an EvaluatorOutput directly or an Awaitable[EvaluatorOutput].
Parameters:
Name | Type | Description | Default
---|---|---|---
`ctx` |  `EvaluatorContext[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorContext "EvaluatorContext



      dataclass
   \(pydantic_evals.evaluators.context.EvaluatorContext\)")[InputsT, OutputT, MetadataT]` |  The context containing the inputs, outputs, and metadata for evaluation. |  _required_
Returns:
Type | Description
---|---
`EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)") | EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")]` |  The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
`EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)") | EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")]` |  of evaluation names to either of those. Can be returned either synchronously or as an
`EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)") | EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")]` |  awaitable for asynchronous evaluation.
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
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
@abstractmethod
def evaluate(
    self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]
) -> EvaluatorOutput | Awaitable[EvaluatorOutput]:  # pragma: no cover
    """Evaluate the task output in the given context.

    This is the main evaluation method that subclasses must implement. It can be either synchronous
    or asynchronous, returning either an EvaluatorOutput directly or an Awaitable[EvaluatorOutput].

    Args:
        ctx: The context containing the inputs, outputs, and metadata for evaluation.

    Returns:
        The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
        of evaluation names to either of those. Can be returned either synchronously or as an
        awaitable for asynchronous evaluation.
    """
    raise NotImplementedError('You must implement `evaluate`.')

```

---|---
####  evaluate_sync
```
evaluate_sync(
    ctx: EvaluatorContext[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorContext "EvaluatorContext



      dataclass
   \(pydantic_evals.evaluators.context.EvaluatorContext\)")[InputsT, OutputT, MetadataT],
) -> EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")

```

Run the evaluator synchronously, handling both sync and async implementations.
This method ensures synchronous execution by running any async evaluate implementation to completion using run_until_complete.
Parameters:
Name | Type | Description | Default
---|---|---|---
`ctx` |  `EvaluatorContext[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorContext "EvaluatorContext



      dataclass
   \(pydantic_evals.evaluators.context.EvaluatorContext\)")[InputsT, OutputT, MetadataT]` |  The context containing the inputs, outputs, and metadata for evaluation. |  _required_
Returns:
Type | Description
---|---
`EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")` |  The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
`EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")` |  of evaluation names to either of those.
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
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
```
| ```
def evaluate_sync(self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]) -> EvaluatorOutput:
    """Run the evaluator synchronously, handling both sync and async implementations.

    This method ensures synchronous execution by running any async evaluate implementation
    to completion using run_until_complete.

    Args:
        ctx: The context containing the inputs, outputs, and metadata for evaluation.

    Returns:
        The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
        of evaluation names to either of those.
    """
    output = self.evaluate(ctx)
    if inspect.iscoroutine(output):  # pragma: no cover
        return get_event_loop().run_until_complete(output)
    else:
        return cast(EvaluatorOutput, output)

```

---|---
####  evaluate_async `async`
```
evaluate_async(
    ctx: EvaluatorContext[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorContext "EvaluatorContext



      dataclass
   \(pydantic_evals.evaluators.context.EvaluatorContext\)")[InputsT, OutputT, MetadataT],
) -> EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")

```

Run the evaluator asynchronously, handling both sync and async implementations.
This method ensures asynchronous execution by properly awaiting any async evaluate implementation. For synchronous implementations, it returns the result directly.
Parameters:
Name | Type | Description | Default
---|---|---|---
`ctx` |  `EvaluatorContext[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorContext "EvaluatorContext



      dataclass
   \(pydantic_evals.evaluators.context.EvaluatorContext\)")[InputsT, OutputT, MetadataT]` |  The context containing the inputs, outputs, and metadata for evaluation. |  _required_
Returns:
Type | Description
---|---
`EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")` |  The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
`EvaluatorOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput



      module-attribute
   \(pydantic_evals.evaluators.evaluator.EvaluatorOutput\)")` |  of evaluation names to either of those.
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
202
203
204
205
206
207
208
209
210
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
```
| ```
async def evaluate_async(self, ctx: EvaluatorContext[InputsT, OutputT, MetadataT]) -> EvaluatorOutput:
    """Run the evaluator asynchronously, handling both sync and async implementations.

    This method ensures asynchronous execution by properly awaiting any async evaluate
    implementation. For synchronous implementations, it returns the result directly.

    Args:
        ctx: The context containing the inputs, outputs, and metadata for evaluation.

    Returns:
        The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping
        of evaluation names to either of those.
    """
    # Note: If self.evaluate is synchronous, but you need to prevent this from blocking, override this method with:
    # return await anyio.to_thread.run_sync(self.evaluate, ctx)
    output = self.evaluate(ctx)
    if inspect.iscoroutine(output):
        return await output
    else:
        return cast(EvaluatorOutput, output)

```

---|---
###  EvaluatorFailure `dataclass`
Represents a failure raised during the execution of an evaluator.
Source code in `pydantic_evals/pydantic_evals/evaluators/evaluator.py`
```
 97
 98
 99
100
101
102
103
104
```
| ```
@dataclass
class EvaluatorFailure:
    """Represents a failure raised during the execution of an evaluator."""

    name: str
    error_message: str
    error_stacktrace: str
    source: EvaluatorSpec

```

---|---
###  EvaluatorOutput `module-attribute`
```
EvaluatorOutput = (
    EvaluationScalar
    | EvaluationReason[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationReason "EvaluationReason



      dataclass
   \(pydantic_evals.evaluators.evaluator.EvaluationReason\)")
    | [, EvaluationScalar | EvaluationReason[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationReason "EvaluationReason



      dataclass
   \(pydantic_evals.evaluators.evaluator.EvaluationReason\)")]
)

```

Type for the output of an evaluator, which can be a scalar, an EvaluationReason, or a mapping of names to either.
###  EvaluatorSpec
Bases: `BaseModel[](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "pydantic.BaseModel")`
The specification of an evaluator to be run.
This class is used to represent evaluators in a serializable format, supporting various short forms for convenience when defining evaluators in YAML or JSON dataset files.
In particular, each of the following forms is supported for specifying an evaluator with name `MyEvaluator`: * `'MyEvaluator'` - Just the (string) name of the Evaluator subclass is used if its `__init__` takes no arguments * `{'MyEvaluator': first_arg}` - A single argument is passed as the first positional argument to `MyEvaluator.__init__` * `{'MyEvaluator': {k1: v1, k2: v2}}` - Multiple kwargs are passed to `MyEvaluator.__init__`
Source code in `pydantic_evals/pydantic_evals/evaluators/spec.py`
```
 23
 24
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
```
| ```
class EvaluatorSpec(BaseModel):
    """The specification of an evaluator to be run.

    This class is used to represent evaluators in a serializable format, supporting various
    short forms for convenience when defining evaluators in YAML or JSON dataset files.

    In particular, each of the following forms is supported for specifying an evaluator with name `MyEvaluator`:
    * `'MyEvaluator'` - Just the (string) name of the Evaluator subclass is used if its `__init__` takes no arguments
    * `{'MyEvaluator': first_arg}` - A single argument is passed as the first positional argument to `MyEvaluator.__init__`
    * `{'MyEvaluator': {k1: v1, k2: v2}}` - Multiple kwargs are passed to `MyEvaluator.__init__`
    """

    name: str
    """The name of the evaluator class; should be the value returned by `EvaluatorClass.get_serialization_name()`"""

    arguments: None | tuple[Any] | dict[str, Any]
    """The arguments to pass to the evaluator's constructor.

    Can be None (no arguments), a tuple (a single positional argument), or a dict (keyword arguments).
    """

    @property
    def args(self) -> tuple[Any, ...]:
        """Get the positional arguments for the evaluator.

        Returns:
            A tuple of positional arguments if arguments is a tuple, otherwise an empty tuple.
        """
        if isinstance(self.arguments, tuple):
            return self.arguments
        return ()

    @property
    def kwargs(self) -> dict[str, Any]:
        """Get the keyword arguments for the evaluator.

        Returns:
            A dictionary of keyword arguments if arguments is a dict, otherwise an empty dict.
        """
        if isinstance(self.arguments, dict):
            return self.arguments
        return {}

    @model_validator(mode='wrap')
    @classmethod
    def deserialize(cls, value: Any, handler: ModelWrapValidatorHandler[EvaluatorSpec]) -> EvaluatorSpec:
        """Deserialize an EvaluatorSpec from various formats.

        This validator handles the various short forms of evaluator specifications,
        converting them to a consistent EvaluatorSpec instance.

        Args:
            value: The value to deserialize.
            handler: The validator handler.

        Returns:
            The deserialized EvaluatorSpec.

        Raises:
            ValidationError: If the value cannot be deserialized.
        """
        try:
            result = handler(value)
            return result
        except ValidationError as exc:
            try:
                deserialized = _SerializedEvaluatorSpec.model_validate(value)
            except ValidationError:
                raise exc  # raise the original error
            return deserialized.to_evaluator_spec()

    @model_serializer(mode='wrap')
    def serialize(self, handler: SerializerFunctionWrapHandler, info: SerializationInfo) -> Any:
        """Serialize using the appropriate short-form if possible.

        Returns:
            The serialized evaluator specification, using the shortest form possible:
            - Just the name if there are no arguments
            - {name: first_arg} if there's a single positional argument
            - {name: {kwargs}} if there are multiple (keyword) arguments
        """
        if isinstance(info.context, dict) and info.context.get('use_short_form'):  # pyright: ignore[reportUnknownMemberType]
            if self.arguments is None:
                return self.name
            elif isinstance(self.arguments, tuple):
                return {self.name: self.arguments[0]}
            else:
                return {self.name: self.arguments}
        else:
            return handler(self)

```

---|---
####  name `instance-attribute`
```
name:

```

The name of the evaluator class; should be the value returned by `EvaluatorClass.get_serialization_name()`
####  arguments `instance-attribute`
```
arguments: None | [] | [, ]

```

The arguments to pass to the evaluator's constructor.
Can be None (no arguments), a tuple (a single positional argument), or a dict (keyword arguments).
####  args `property`
```
args: [, ...]

```

Get the positional arguments for the evaluator.
Returns:
Type | Description
---|---
|  A tuple of positional arguments if arguments is a tuple, otherwise an empty tuple.
####  kwargs `property`
```
kwargs: [, ]

```

Get the keyword arguments for the evaluator.
Returns:
Type | Description
---|---
|  A dictionary of keyword arguments if arguments is a dict, otherwise an empty dict.
####  deserialize `classmethod`
```
deserialize(
    value: ,
    handler: ModelWrapValidatorHandler[](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.ModelWrapValidatorHandler "pydantic.ModelWrapValidatorHandler")[EvaluatorSpec[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorSpec "EvaluatorSpec \(pydantic_evals.evaluators.spec.EvaluatorSpec\)")],
) -> EvaluatorSpec[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorSpec "EvaluatorSpec \(pydantic_evals.evaluators.spec.EvaluatorSpec\)")
