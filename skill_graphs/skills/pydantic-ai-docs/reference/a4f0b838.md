
```

Judge the output of a model based on a rubric.
If the model is not specified, a default model is used. The default model starts as 'openai:gpt-5.2', but this can be changed using the `set_default_judge_model` function.
Source code in `pydantic_evals/pydantic_evals/evaluators/llm_as_a_judge.py`
```
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
```
| ```
async def judge_output(
    output: Any,
    rubric: str,
    model: models.Model | models.KnownModelName | str | None = None,
    model_settings: ModelSettings | None = None,
) -> GradingOutput:
    """Judge the output of a model based on a rubric.

    If the model is not specified, a default model is used. The default model starts as 'openai:gpt-5.2',
    but this can be changed using the `set_default_judge_model` function.
    """
    user_prompt = _build_prompt(output=output, rubric=rubric)
    return (
        await _judge_output_agent.run(user_prompt, model=model or _default_model, model_settings=model_settings)
    ).output

```

---|---
###  judge_input_output `async`
```
judge_input_output(
    inputs: ,
    output: ,
    rubric: ,
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
) -> GradingOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.llm_as_a_judge.GradingOutput "GradingOutput \(pydantic_evals.evaluators.llm_as_a_judge.GradingOutput\)")

```

Judge the output of a model based on the inputs and a rubric.
If the model is not specified, a default model is used. The default model starts as 'openai:gpt-5.2', but this can be changed using the `set_default_judge_model` function.
Source code in `pydantic_evals/pydantic_evals/evaluators/llm_as_a_judge.py`
```
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
async def judge_input_output(
    inputs: Any,
    output: Any,
    rubric: str,
    model: models.Model | models.KnownModelName | str | None = None,
    model_settings: ModelSettings | None = None,
) -> GradingOutput:
    """Judge the output of a model based on the inputs and a rubric.

    If the model is not specified, a default model is used. The default model starts as 'openai:gpt-5.2',
    but this can be changed using the `set_default_judge_model` function.
    """
    user_prompt = _build_prompt(inputs=inputs, output=output, rubric=rubric)

    return (
        await _judge_input_output_agent.run(user_prompt, model=model or _default_model, model_settings=model_settings)
    ).output

```

---|---
###  judge_input_output_expected `async`
```
judge_input_output_expected(
    inputs: ,
    output: ,
    expected_output: ,
    rubric: ,
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
) -> GradingOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.llm_as_a_judge.GradingOutput "GradingOutput \(pydantic_evals.evaluators.llm_as_a_judge.GradingOutput\)")

```

Judge the output of a model based on the inputs and a rubric.
If the model is not specified, a default model is used. The default model starts as 'openai:gpt-5.2', but this can be changed using the `set_default_judge_model` function.
Source code in `pydantic_evals/pydantic_evals/evaluators/llm_as_a_judge.py`
```
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
```
| ```
async def judge_input_output_expected(
    inputs: Any,
    output: Any,
    expected_output: Any,
    rubric: str,
    model: models.Model | models.KnownModelName | str | None = None,
    model_settings: ModelSettings | None = None,
) -> GradingOutput:
    """Judge the output of a model based on the inputs and a rubric.

    If the model is not specified, a default model is used. The default model starts as 'openai:gpt-5.2',
    but this can be changed using the `set_default_judge_model` function.
    """
    user_prompt = _build_prompt(inputs=inputs, output=output, rubric=rubric, expected_output=expected_output)

    return (
        await _judge_input_output_expected_agent.run(
            user_prompt, model=model or _default_model, model_settings=model_settings
        )
    ).output

```

---|---
###  judge_output_expected `async`
```
judge_output_expected(
    output: ,
    expected_output: ,
    rubric: ,
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)") |  | None = None,
    model_settings: ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "ModelSettings \(pydantic_ai.settings.ModelSettings\)") | None = None,
) -> GradingOutput[](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.llm_as_a_judge.GradingOutput "GradingOutput \(pydantic_evals.evaluators.llm_as_a_judge.GradingOutput\)")

```

Judge the output of a model based on the expected output, output, and a rubric.
If the model is not specified, a default model is used. The default model starts as 'openai:gpt-5.2', but this can be changed using the `set_default_judge_model` function.
Source code in `pydantic_evals/pydantic_evals/evaluators/llm_as_a_judge.py`
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
```
| ```
async def judge_output_expected(
    output: Any,
    expected_output: Any,
    rubric: str,
    model: models.Model | models.KnownModelName | str | None = None,
    model_settings: ModelSettings | None = None,
) -> GradingOutput:
    """Judge the output of a model based on the expected output, output, and a rubric.

    If the model is not specified, a default model is used. The default model starts as 'openai:gpt-5.2',
    but this can be changed using the `set_default_judge_model` function.
    """
    user_prompt = _build_prompt(output=output, rubric=rubric, expected_output=expected_output)
    return (
        await _judge_output_expected_agent.run(
            user_prompt, model=model or _default_model, model_settings=model_settings
        )
    ).output

```

---|---
###  set_default_judge_model
```
set_default_judge_model(
    model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "Model \(pydantic_ai.models.Model\)") | KnownModelName[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.KnownModelName "KnownModelName



      module-attribute
   \(pydantic_ai.models.KnownModelName\)"),
) -> None

```

Set the default model used for judging.
This model is used if `None` is passed to the `model` argument of `judge_output` and `judge_input_output`.
Source code in `pydantic_evals/pydantic_evals/evaluators/llm_as_a_judge.py`
```
205
206
207
208
209
210
211
```
| ```
def set_default_judge_model(model: models.Model | models.KnownModelName) -> None:
    """Set the default model used for judging.

    This model is used if `None` is passed to the `model` argument of `judge_output` and `judge_input_output`.
    """
    global _default_model
    _default_model = model

```

---|---
© Pydantic Services Inc. 2024 to present
