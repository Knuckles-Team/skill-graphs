## Image output
Some models can generate images as part of their response, for example those that support the [Image Generation built-in tool](https://ai.pydantic.dev/builtin-tools/#image-generation-tool) and OpenAI models using the [Code Execution built-in tool](https://ai.pydantic.dev/builtin-tools/#code-execution-tool) when told to generate a chart.
To use the generated image as the output of the agent run, you can set `output_type` to [`BinaryImage`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryImage "BinaryImage"). If no image-generating built-in tool is explicitly specified, the [`ImageGenerationTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.ImageGenerationTool "ImageGenerationTool



      dataclass
  ") will be enabled automatically.
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_11_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_11_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) image_output.py```
from pydantic_ai import Agent, BinaryImage

agent = Agent('gateway/openai-responses:gpt-5.2', output_type=BinaryImage)

result = agent.run_sync('Generate an image of an axolotl.')
assert isinstance(result.output, BinaryImage)

```

image_output.py```
from pydantic_ai import Agent, BinaryImage

agent = Agent('openai-responses:gpt-5.2', output_type=BinaryImage)

result = agent.run_sync('Generate an image of an axolotl.')
assert isinstance(result.output, BinaryImage)

```

_(This example is complete, it can be run "as is")_
If an agent does not need to always generate an image, you can use a union of `BinaryImage` and `str`. If the model generates both, the image will take precedence as output and the text will be available on [`ModelResponse.text`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.text "text



      property
  "):
[With Pydantic AI Gateway](https://ai.pydantic.dev/output/#__tabbed_12_1)[Directly to Provider API](https://ai.pydantic.dev/output/#__tabbed_12_2)
[Learn about Gateway](https://ai.pydantic.dev/gateway) image_output_union.py```
from pydantic_ai import Agent, BinaryImage

agent = Agent('gateway/openai-responses:gpt-5.2', output_type=BinaryImage | str)

result = agent.run_sync('Tell me a two-sentence story about an axolotl, no image please.')
print(result.output)
"""
Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!
"""

result = agent.run_sync('Tell me a two-sentence story about an axolotl with an illustration.')
assert isinstance(result.output, BinaryImage)
print(result.response.text)
"""
Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!
"""

```

image_output_union.py```
from pydantic_ai import Agent, BinaryImage

agent = Agent('openai-responses:gpt-5.2', output_type=BinaryImage | str)

result = agent.run_sync('Tell me a two-sentence story about an axolotl, no image please.')
print(result.output)
"""
Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!
"""

result = agent.run_sync('Tell me a two-sentence story about an axolotl with an illustration.')
assert isinstance(result.output, BinaryImage)
print(result.response.text)
"""
Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!
"""

```
